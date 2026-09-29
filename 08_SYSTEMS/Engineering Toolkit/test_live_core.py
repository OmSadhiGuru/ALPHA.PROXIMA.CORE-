#!/usr/bin/env python3
"""Tests for the Live Core: AlphaEvent, adapters, ledger and projections.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_live_core.py"
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLKIT))

import alpha_event as ev  # noqa: E402
import event_adapters as ad  # noqa: E402
import event_ledger as led  # noqa: E402


def sample(**kw):
    base = dict(
        source="github",
        event_type="github.pr.merged",
        entity_type="pull_request",
        entity_id="PR-50",
        title="Typed entity resolution",
        occurred_at="2026-09-29T06:00:00+00:00",
        received_at="2026-09-29T06:00:05+00:00",
        actor_id="agent:cf-07",
    )
    base.update(kw)
    return ev.new_event(**base)


class TestContract(unittest.TestCase):
    def test_a_well_formed_event_validates(self):
        self.assertTrue(ev.is_valid(sample()))

    def test_every_required_field_is_enforced(self):
        for field in ev.REQUIRED_FIELDS:
            event = sample()
            event[field] = None
            self.assertIn(f"missing required field: {field}", ev.validate(event))

    def test_validation_reports_every_problem_at_once(self):
        """An adapter emitting bad events should learn all the reasons together."""
        problems = ev.validate({"source": "GitHub!", "severity": "urgent",
                                "entity_type": "banana"})
        self.assertGreater(len(problems), 3)

    def test_event_type_must_look_like_provider_noun_verb(self):
        with self.assertRaises(ev.EventError):
            sample(event_type="merged")

    def test_event_type_must_belong_to_its_source(self):
        with self.assertRaises(ev.EventError):
            sample(event_type="notion.page.updated")

    def test_unknown_severity_is_rejected(self):
        with self.assertRaises(ev.EventError):
            sample(severity="urgent")

    def test_received_at_may_not_precede_occurred_at(self):
        with self.assertRaises(ev.EventError):
            sample(occurred_at="2026-09-29T06:00:05+00:00",
                   received_at="2026-09-29T06:00:00+00:00")

    def test_a_future_schema_version_is_refused(self):
        event = sample()
        event["schema_version"] = "2.0"
        self.assertTrue(any("schema_version" in p for p in ev.validate(event)))


class TestActorIsAnEntity(unittest.TestCase):
    """The join that makes an event navigable from the Council."""

    def test_actor_id_must_be_an_entity_id(self):
        with self.assertRaises(ev.EventError):
            sample(actor_id="CODEX")

    def test_each_entity_kind_is_accepted(self):
        for actor in ("agent:cf-07", "office:lumiaion",
                      "organization:alpha-proxima-foundation", "person:founder"):
            self.assertTrue(ev.is_valid(sample(actor_id=actor)), actor)

    def test_an_event_may_have_no_actor(self):
        """A CI run has no author; absence is not the same as a bad value."""
        self.assertTrue(ev.is_valid(sample(actor_id=None)))


class TestIdempotency(unittest.TestCase):
    def test_a_retried_delivery_produces_the_same_key(self):
        first = sample(received_at="2026-09-29T06:00:05+00:00")
        second = sample(received_at="2026-09-29T09:30:00+00:00")
        self.assertNotEqual(first["event_id"], second["event_id"])
        self.assertEqual(first["idempotency_key"], second["idempotency_key"])

    def test_a_different_fact_produces_a_different_key(self):
        self.assertNotEqual(sample()["idempotency_key"],
                            sample(entity_id="PR-51")["idempotency_key"])

    def test_a_provider_delivery_id_anchors_identity(self):
        a = sample(metadata={"provider_event_id": "d-1"})
        b = sample(occurred_at="2026-09-29T07:00:00+00:00",
                   received_at="2026-09-29T07:00:01+00:00",
                   metadata={"provider_event_id": "d-1"})
        self.assertEqual(a["idempotency_key"], b["idempotency_key"])


class TestNotificationPolicy(unittest.TestCase):
    """Severity is a decision to interrupt someone."""

    def test_info_reaches_the_feed_only(self):
        policy = ev.notification_policy(sample(severity="info"))
        self.assertEqual((policy["feed"], policy["badge"], policy["push"]), (True, False, False))

    def test_update_earns_a_badge_but_no_push(self):
        policy = ev.notification_policy(sample(severity="update"))
        self.assertTrue(policy["badge"])
        self.assertFalse(policy["push"])

    def test_action_pushes(self):
        policy = ev.notification_policy(sample(severity="action", requires_founder=True))
        self.assertTrue(policy["push"])
        self.assertFalse(policy["immediate"])

    def test_critical_pushes_immediately(self):
        policy = ev.notification_policy(sample(severity="critical", requires_founder=True))
        self.assertTrue(policy["immediate"])

    def test_critical_must_require_the_founder(self):
        """A critical event that claims not to need the Founder is a silent mistake."""
        with self.assertRaises(ev.EventError):
            sample(severity="critical", requires_founder=False)

    def test_requires_founder_pushes_whatever_the_severity(self):
        self.assertTrue(ev.notification_policy(sample(requires_founder=True))["push"])


class TestAdapterContract(unittest.TestCase):
    def test_every_declared_integration_is_planned_until_verified(self):
        registry = ad.build_registry()
        self.assertTrue(all(a["status"] == "planned" for a in registry["adapters"]))
        self.assertEqual(registry["counts"]["implemented"], 0)

    def test_connected_without_evidence_is_refused(self):
        """Never claim connected without verification."""
        with self.assertRaises(ad.AdapterError):
            ad.adapter_record("github", "GitHub", status="connected",
                              normalize=lambda p: [])

    def test_connected_with_evidence_is_allowed(self):
        record = ad.adapter_record("github", "GitHub", status="connected",
                                   normalize=lambda p: [],
                                   evidence="delivery 8f2c verified 2026-09-29")
        self.assertEqual(record["status"], "connected")

    def test_claiming_an_implementation_without_one_is_refused(self):
        with self.assertRaises(ad.AdapterError):
            ad.adapter_record("notion", "Notion", status="degraded",
                              evidence="observed")

    def test_an_adapter_may_not_claim_another_sources_event_type(self):
        with self.assertRaises(ad.AdapterError):
            ad.adapter_record("notion", "Notion", event_types=("github.pr.merged",))

    def test_registering_an_undeclared_source_is_refused(self):
        with self.assertRaises(ad.AdapterError):
            ad.build_registry({"salesforce": {"status": "planned"}})

    def test_an_unimplemented_adapter_ingests_nothing_and_says_why(self):
        events, problems = ad.ingest(ad.build_registry(), "github", {})
        self.assertEqual(events, [])
        self.assertIn("not implemented", problems[0])


class TestIngestion(unittest.TestCase):
    def registry(self, normalize):
        return ad.build_registry({"github": {
            "status": "degraded", "normalize": normalize,
            "evidence": "fixture exchange", "event_types": ("github.pr.merged",)}})

    def test_a_valid_payload_normalizes(self):
        events, problems = ad.ingest(self.registry(lambda p: [sample()]), "github", {})
        self.assertEqual((len(events), problems), (1, []))

    def test_an_adapter_that_raises_cannot_take_the_ledger_down(self):
        def boom(payload):
            raise RuntimeError("provider changed its mind")
        events, problems = ad.ingest(self.registry(boom), "github", {})
        self.assertEqual(events, [])
        self.assertIn("RuntimeError", problems[0])

    def test_adapter_output_is_validated_not_trusted(self):
        events, problems = ad.ingest(
            self.registry(lambda p: [{"source": "github", "title": "bad"}]), "github", {})
        self.assertEqual(events, [])
        self.assertTrue(problems)

    def test_an_adapter_may_not_forge_another_source(self):
        forged = dict(sample())
        forged["source"] = "github"
        forged["event_type"] = "github.pr.merged"
        registry = ad.build_registry({"notion": {
            "status": "degraded", "normalize": lambda p: [forged],
            "evidence": "fixture"}})
        events, problems = ad.ingest(registry, "notion", {})
        self.assertEqual(events, [])
        self.assertTrue(any("does not match adapter" in p for p in problems))


class TestLedgerIsAppendOnly(unittest.TestCase):
    def test_appending_preserves_order_and_never_rewrites(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            led.append([sample(entity_id="PR-1")], path)
            first = path.read_text(encoding="utf-8")
            led.append([sample(entity_id="PR-2")], path)
            second = path.read_text(encoding="utf-8")
            self.assertTrue(second.startswith(first))
            self.assertEqual(len(led.read_ledger(path)), 2)

    def test_a_retried_event_is_not_appended_twice(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            led.append([sample()], path)
            result = led.append([sample(received_at="2026-09-29T12:00:00+00:00")], path)
            self.assertEqual((result["appended"], result["duplicates"]), (0, 1))
            self.assertEqual(len(led.read_ledger(path)), 1)

    def test_duplicates_inside_one_batch_are_caught(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            result = led.append([sample(), sample()], path)
            self.assertEqual((result["appended"], result["duplicates"]), (1, 1))

    def test_an_invalid_event_is_rejected_with_reasons(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            result = led.append([{"source": "github"}], path)
            self.assertEqual(result["appended"], 0)
            self.assertTrue(result["rejected"][0]["problems"])
            self.assertFalse(path.exists())

    def test_a_corrupt_line_is_reported_never_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            led.append([sample()], path)
            with path.open("a", encoding="utf-8") as handle:
                handle.write("{not json\n")
            with self.assertRaises(led.LedgerError):
                led.read_ledger(path)

    def test_an_absent_ledger_reads_as_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(led.read_ledger(Path(tmp) / "none.jsonl"), [])


class TestPresenceExpires(unittest.TestCase):
    """Presence is a claim with an expiry, never a fact."""

    def presence_event(self, actor, state, at, ttl=90):
        return sample(source="codex", event_type="codex.presence.declared",
                      entity_type="presence", entity_id=f"{actor}:{state}",
                      title=f"{actor} is {state}", actor_id=actor,
                      occurred_at=at, received_at=at,
                      metadata={"presence_state": state, "ttl_seconds": ttl})

    def test_a_fresh_signal_reads_as_working(self):
        events = [self.presence_event("agent:cf-07", "coding", "2026-09-29T06:00:00+00:00")]
        view = led.presence(events, now="2026-09-29T06:00:30+00:00")
        actor = view["actors"][0]
        self.assertEqual(actor["state"], "coding")
        self.assertFalse(actor["expired"])
        self.assertEqual(view["counts"]["working"], 1)

    def test_a_crashed_agent_does_not_stay_coding_forever(self):
        events = [self.presence_event("agent:cf-07", "coding", "2026-09-29T06:00:00+00:00")]
        view = led.presence(events, now="2026-09-29T09:00:00+00:00")
        actor = view["actors"][0]
        self.assertEqual(actor["state"], "offline")
        self.assertEqual(actor["claimed_state"], "coding")
        self.assertTrue(actor["expired"])
        self.assertEqual(view["counts"]["working"], 0)

    def test_only_the_latest_signal_per_actor_counts(self):
        events = [
            self.presence_event("agent:cf-07", "thinking", "2026-09-29T06:00:00+00:00"),
            self.presence_event("agent:cf-07", "coding", "2026-09-29T06:00:30+00:00"),
        ]
        view = led.presence(events, now="2026-09-29T06:00:40+00:00")
        self.assertEqual(len(view["actors"]), 1)
        self.assertEqual(view["actors"][0]["state"], "coding")

    def test_a_per_event_ttl_is_honoured(self):
        events = [self.presence_event("agent:cf-07", "indexing",
                                      "2026-09-29T06:00:00+00:00", ttl=5)]
        view = led.presence(events, now="2026-09-29T06:00:10+00:00")
        self.assertTrue(view["actors"][0]["expired"])

    def test_non_presence_events_never_become_presence(self):
        self.assertEqual(led.presence([sample()], now="2026-09-29T06:00:10+00:00")["actors"], [])

    def test_an_unknown_claimed_state_falls_back_to_online(self):
        events = [self.presence_event("agent:cf-07", "vibing", "2026-09-29T06:00:00+00:00")]
        view = led.presence(events, now="2026-09-29T06:00:10+00:00")
        self.assertEqual(view["actors"][0]["state"], "online")


class TestProjections(unittest.TestCase):
    def test_activity_is_newest_first(self):
        events = [sample(entity_id="PR-1", occurred_at="2026-09-29T06:00:00+00:00",
                         received_at="2026-09-29T06:00:00+00:00"),
                  sample(entity_id="PR-2", occurred_at="2026-09-29T07:00:00+00:00",
                         received_at="2026-09-29T07:00:00+00:00")]
        self.assertEqual(led.activity(events)["items"][0]["entity_id"], "PR-2")

    def test_the_badge_counts_meaning_not_volume(self):
        """A hundred routine commits are a hundred feed items and zero badge."""
        noise = [sample(entity_id=f"c-{i}", event_type="github.commit.created",
                        entity_type="commit", severity="info") for i in range(100)]
        view = led.notifications(noise)
        self.assertEqual(view["badge_count"], 0)
        self.assertEqual(view["counts"]["total"], 0)

    def test_meaningful_events_earn_the_badge(self):
        view = led.notifications([sample(severity="update"),
                                  sample(entity_id="PR-9", severity="action",
                                         requires_founder=True)])
        self.assertEqual(view["badge_count"], 2)
        self.assertEqual(view["counts"]["push"], 1)

    def test_reading_a_notification_clears_it_from_the_badge(self):
        event = sample(severity="update")
        view = led.notifications([event], read_keys={event["idempotency_key"]})
        self.assertEqual(view["badge_count"], 0)
        self.assertEqual(view["counts"]["total"], 1)

    def test_the_live_view_composes_every_projection(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            led.append([sample(severity="update")], path)
            view = led.build_live_view(path)
        self.assertEqual(view["ledger"]["events"], 1)
        for key in ("activity", "presence", "notifications"):
            self.assertIn(key, view)

    def test_the_live_view_is_json_serialisable(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.jsonl"
            led.append([sample()], path)
            json.loads(json.dumps(led.build_live_view(path)))


class TestBoundaries(unittest.TestCase):
    """The Core owns schemas and projections. Infrastructure owns the network."""

    def test_no_module_in_the_live_core_imports_a_network_client(self):
        forbidden = ("import requests", "import httpx", "import urllib.request",
                     "from urllib.request", "import socket", "supabase", "boto3")
        for name in ("alpha_event.py", "event_adapters.py", "event_ledger.py"):
            source = (TOOLKIT / name).read_text(encoding="utf-8")
            for token in forbidden:
                self.assertNotIn(token, source, f"{name} must not contain {token!r}")

    def test_the_ledger_never_rewrites_in_place(self):
        source = (TOOLKIT / "event_ledger.py").read_text(encoding="utf-8")
        self.assertNotIn('"w"', source)
        self.assertNotIn("write_text(", source)
        self.assertIn('open("a"', source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
