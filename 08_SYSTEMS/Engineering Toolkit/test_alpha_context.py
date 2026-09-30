#!/usr/bin/env python3
"""Tests for ContextItem v1 and the capture adapters.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_alpha_context.py"
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import alpha_adapters as ad  # noqa: E402
import alpha_context as ctx  # noqa: E402
import alpha_events as ev  # noqa: E402

FIXTURES = Path(__file__).resolve().parent.parent.parent / "13_OPERATIONS" / "Live Integration Layer" / "fixtures"


def fixture(provider: str, name: str) -> dict:
    return json.loads((FIXTURES / provider / f"{name}.json").read_text(encoding="utf-8"))


def item(**overrides) -> dict:
    base = dict(provider="omi", provider_item_id="omi-1", capture_kind="memory",
                occurred_at="2026-09-29T10:00:00+00:00", title="A capture")
    base.update(overrides)
    return ctx.make_context_item(**base)


class TestContentNeverTravels(unittest.TestCase):
    """The load-bearing rule: a ContextItem references a capture, never copies one."""

    def test_every_body_field_is_refused(self):
        for field in sorted(ctx.BODY_FIELDS):
            with self.assertRaises(ctx.ContextError, msg=f"{field} was accepted"):
                item(metadata={field: "the Founder's words"})

    def test_refusal_is_found_however_deeply_nested(self):
        with self.assertRaises(ctx.ContextError):
            item(metadata={"omi": {"segments": [{"transcript": "words"}]}})

    def test_a_chatty_delivery_yields_a_content_free_event(self):
        """The provider may send anything; the adapter reads only what it should."""
        delivery = fixture("omi", "content-bearing")
        secret = delivery["payload"]["transcript"]
        event = ad.OmiAdapter().normalize(delivery)[0]
        self.assertNotIn(secret, json.dumps(event))

    def test_every_capture_event_states_where_the_content_is(self):
        event = ad.OmiAdapter().normalize(fixture("omi", "memory.created"))[0]
        self.assertEqual(event["metadata"]["content_location"], "provider")


class TestSensitivityIsConservative(unittest.TestCase):
    def test_the_default_is_sensitive(self):
        self.assertEqual(ctx.DEFAULT_SENSITIVITY, "sensitive")
        self.assertEqual(item()["sensitivity"], "sensitive")

    def test_an_absent_flag_does_not_lower_it(self):
        """Omi marks most of its corpus sensitive; silence is not permission."""
        payload = dict(fixture("omi", "memory.created")["payload"])
        payload.pop("sensitive", None)
        event = ad.OmiAdapter().normalize({"kind": "memory.created", "payload": payload})[0]
        self.assertEqual(event["metadata"]["sensitivity"], "sensitive")

    def test_only_an_explicit_false_lowers_it(self):
        payload = dict(fixture("omi", "memory.created")["payload"])
        payload["sensitive"] = False
        event = ad.OmiAdapter().normalize({"kind": "memory.created", "payload": payload})[0]
        self.assertEqual(event["metadata"]["sensitivity"], "standard")

    def test_pocket_ai_states_nothing_so_everything_is_sensitive(self):
        event = ad.PocketAIAdapter().normalize(fixture("pocket_ai", "capture.created"))[0]
        self.assertEqual(event["metadata"]["sensitivity"], "sensitive")


class TestACaptureIsAProposal(unittest.TestCase):
    """A device that records the Founder does not get to interrupt the Founder."""

    def test_severity_is_always_info(self):
        for provider, name in (("omi", "memory.created"), ("omi", "conversation.created"),
                               ("pocket_ai", "capture.created")):
            adapter = ad.OmiAdapter() if provider == "omi" else ad.PocketAIAdapter()
            event = adapter.normalize(fixture(provider, name))[0]
            self.assertEqual(event["severity"], "info")
            self.assertFalse(event["requires_founder"])

    def test_classification_is_suggested_never_asserted(self):
        event = ad.OmiAdapter().normalize(fixture("omi", "memory.created"))[0]
        self.assertIn("suggested_kind", event["metadata"])
        self.assertNotIn("kind", event["metadata"])

    def test_an_unrecognised_category_proposes_nothing(self):
        payload = dict(fixture("omi", "memory.created")["payload"])
        payload["category"] = "weather"
        event = ad.OmiAdapter().normalize({"kind": "memory.created", "payload": payload})[0]
        self.assertEqual(event["metadata"]["suggested_kind"], "none")

    def test_a_known_category_proposes_something(self):
        event = ad.OmiAdapter().normalize(fixture("omi", "memory.created"))[0]
        self.assertEqual(event["metadata"]["suggested_kind"], "task")


class TestIdentityAndNavigation(unittest.TestCase):
    def test_the_actor_is_the_founder_not_the_device(self):
        event = ad.OmiAdapter().normalize(fixture("omi", "memory.created"))[0]
        self.assertEqual(event["actor"], "person:founder")

    def test_the_deep_link_is_alpha_proximas_own_scheme(self):
        event = ad.OmiAdapter().normalize(fixture("omi", "memory.created"))[0]
        self.assertFalse(ev.validate_deep_link(event["deep_link"]))
        self.assertTrue(event["deep_link"].startswith("alpha-proxima://memory/"))

    def test_the_provider_url_travels_in_metadata_not_the_deep_link(self):
        event = ad.OmiAdapter().normalize(fixture("omi", "memory.created"))[0]
        self.assertIn("omi.me", event["metadata"]["provider_url"])
        self.assertNotIn("omi.me", event["deep_link"])

    def test_the_provider_id_survives_for_deduplication(self):
        event = ad.OmiAdapter().normalize(fixture("omi", "memory.created"))[0]
        self.assertEqual(event["metadata"]["provider_event_id"], "omi-mem-8f21c4")
        self.assertTrue(ev.dedup_key(event).startswith("p:"))

    def test_a_missing_provider_id_is_refused(self):
        with self.assertRaises(ad.AdapterError):
            ad.OmiAdapter().normalize({"kind": "memory.created", "payload": {"title": "x"}})


class TestTheContractItself(unittest.TestCase):
    def test_validation_reports_every_fault_not_the_first(self):
        problems = ctx.validate({"schema_version": ctx.SCHEMA_VERSION, "provider": "OMI!",
                                 "provider_item_id": "", "capture_kind": "nope",
                                 "occurred_at": "not-a-date", "title": "",
                                 "sensitivity": "maybe", "suggested_kind": "whatever",
                                 "reference": ""})
        self.assertGreater(len(problems), 4)

    def test_counts_survive_being_sent_as_strings(self):
        event = ad.PocketAIAdapter().normalize(fixture("pocket_ai", "capture.created"))[0]
        self.assertEqual(event["metadata"]["duration_seconds"], 96)

    def test_a_negative_count_becomes_none_rather_than_a_lie(self):
        self.assertIsNone(ad._as_count(-5))
        self.assertIsNone(ad._as_count("banana"))

    def test_omi_is_a_declared_source(self):
        self.assertIn("omi", ev.SOURCES)


class TestNeitherAdapterClaimsAConnection(unittest.TestCase):
    """Normalization is implemented. Nothing has been observed. Both are true."""

    def registry_row(self, provider: str) -> dict:
        view = ad.AdapterRegistry(path="/nonexistent-registry.json").view()
        return next(r for r in view["adapters"] if r["provider"] == provider)

    def test_both_are_implemented(self):
        for provider in ("omi", "pocket_ai"):
            self.assertTrue(self.registry_row(provider)["implemented"])

    def test_neither_reads_connected(self):
        for provider in ("omi", "pocket_ai"):
            self.assertNotEqual(self.registry_row(provider)["status"], "connected")

    def test_each_names_what_a_human_must_supply(self):
        self.assertEqual(self.registry_row("omi")["configuration_required"], ["OMI_WEBHOOK_SECRET"])

    def test_omi_says_session_tooling_is_not_an_integration(self):
        """The distinction that keeps an agent's own connector out of the registry."""
        self.assertIn("tooling", self.registry_row("omi")["blocked_reason"])

    def test_an_unhandled_provider_event_is_refused(self):
        with self.assertRaises(ad.AdapterError):
            ad.OmiAdapter().normalize({"kind": "memory.deleted", "payload": {"id": "x"}})


class TestNoNetworkInTheContract(unittest.TestCase):
    def test_the_contract_opens_no_socket(self):
        source = Path(ctx.__file__).read_text(encoding="utf-8")
        for forbidden in ("import requests", "urllib.request", "http.client", "socket"):
            self.assertNotIn(forbidden, source)

    def test_the_contract_writes_nothing(self):
        source = Path(ctx.__file__).read_text(encoding="utf-8")
        self.assertNotIn(".write_text(", source)
        self.assertNotIn("open(", source.replace("Path(args.path).read_text", ""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
