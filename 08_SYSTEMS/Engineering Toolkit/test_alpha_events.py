#!/usr/bin/env python3
"""Tests for the AlphaEvent v1 contract, its ledger, and its deep links.

These tests are the contract's teeth. Each one locks in a refusal — an invalid
event that must not be stored, a secret that must not be published, a duplicate
that must not be counted twice — because every one of those failures is silent
if nothing checks for it.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLKIT_DIR = Path(__file__).resolve().parent


def _load(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLKIT_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ev = _load("alpha_events.py", "alpha_events")


def sample(**overrides) -> dict:
    """A valid event, minimally specified, for a test to then break on purpose."""
    fields = dict(
        source="github",
        actor="CODEX",
        department="ENGINEERING",
        event_type="github.pr.opened",
        entity_type="pull_request",
        entity_id="PR-48",
        title="PR-48 opened",
        summary="Three files modified",
        severity="update",
        occurred_at="2026-09-29T14:00:00+00:00",
        received_at="2026-09-29T14:00:02+00:00",
    )
    fields.update(overrides)
    return ev.make_event(**fields)


class ValidationTests(unittest.TestCase):
    def test_a_well_formed_event_validates(self):
        self.assertEqual(ev.validate(sample()), [])
        self.assertTrue(ev.is_valid(sample()))

    def test_every_required_field_is_required(self):
        for field in ev.REQUIRED_FIELDS:
            event = sample()
            del event[field]
            errors = ev.validate(event)
            self.assertTrue(
                any(field in error for error in errors),
                f"removing {field} was not reported as missing",
            )

    def test_provider_fields_cannot_smuggle_themselves_in(self):
        event = sample()
        event["pull_request"] = {"number": 48}
        errors = ev.validate(event)
        self.assertTrue(any("pull_request" in e and "metadata" in e for e in errors))

    def test_unknown_provider_is_rejected(self):
        with self.assertRaises(ev.EventError):
            sample(source="myspace")

    def test_unknown_severity_is_rejected(self):
        with self.assertRaises(ev.EventError):
            sample(severity="urgent")

    def test_unknown_department_is_rejected_rather_than_invented(self):
        with self.assertRaises(ev.EventError):
            sample(department="MARKETING")
        # The escape hatch exists, and it is honest about not knowing.
        self.assertEqual(ev.validate(sample(department="UNATTRIBUTED")), [])

    def test_unknown_schema_version_is_refused(self):
        event = sample()
        event["schema_version"] = "2.0"
        errors = ev.validate(event)
        self.assertTrue(any("schema_version" in e for e in errors))

    def test_event_type_must_follow_the_taxonomy(self):
        for bad in ("PR_MERGED", "github..pr", "github pr opened", "github", ""):
            event = sample()
            event["event_type"] = bad
            self.assertTrue(ev.validate(event), f"{bad!r} should not validate")

    def test_requires_founder_must_be_a_real_boolean(self):
        event = sample()
        event["requires_founder"] = "yes"
        self.assertTrue(any("boolean" in e for e in ev.validate(event)))

    def test_malformed_timestamps_are_rejected(self):
        event = sample()
        event["occurred_at"] = "last tuesday"
        self.assertTrue(any("occurred_at" in e for e in ev.validate(event)))

    def test_an_anonymous_event_has_no_provenance_and_is_refused(self):
        with self.assertRaises(ev.EventError):
            sample(actor="   ")

    def test_oversized_metadata_is_refused_so_the_ledger_is_not_a_mirror(self):
        with self.assertRaises(ev.EventError):
            sample(metadata={"blob": "x" * (ev.MAX_METADATA_BYTES + 1)})

    def test_validation_reports_every_fault_not_just_the_first(self):
        event = sample()
        event["severity"] = "urgent"
        event["source"] = "myspace"
        event["event_type"] = "NOPE"
        self.assertGreaterEqual(len(ev.validate(event)), 3)

    def test_a_non_object_is_not_an_event(self):
        for payload in ([], "event", 7, None):
            self.assertTrue(ev.validate(payload))


class SecretLeakTests(unittest.TestCase):
    def test_a_credential_shaped_key_is_refused_at_any_depth(self):
        for metadata in (
            {"api_key": "abc"},
            {"headers": {"Authorization": "Bearer abc"}},
            {"devices": [{"device_token": "abc"}]},
            {"nested": {"deeper": {"client_secret": "abc"}}},
        ):
            with self.subTest(metadata=metadata):
                with self.assertRaises(ev.EventError):
                    sample(metadata=metadata)

    def test_an_ordinary_payload_is_not_falsely_accused(self):
        self.assertEqual(ev.secret_leaks({"number": 48, "branch": "main"}), [])

    def test_the_leak_report_names_the_path(self):
        leaks = ev.secret_leaks({"outer": {"api_key": "x"}})
        self.assertTrue(leaks and "metadata.outer.api_key" in leaks[0])


class DeepLinkTests(unittest.TestCase):
    def test_native_links_are_built_for_known_surfaces(self):
        self.assertEqual(ev.deep_link("council", "agent", "CODEX"),
                         "alpha-proxima://council/agent/CODEX")
        self.assertEqual(ev.deep_link("github", "pr", "48"), "alpha-proxima://github/pr/48")
        self.assertEqual(ev.deep_link("memory"), "alpha-proxima://memory")

    def test_a_link_to_nowhere_is_refused(self):
        with self.assertRaises(ev.EventError):
            ev.deep_link("nowhere", "x")

    def test_an_unnavigable_root_fails_validation(self):
        event = sample()
        event["deep_link"] = "alpha-proxima://nowhere/1"
        self.assertTrue(ev.validate(event))

    def test_a_fragment_is_already_portable(self):
        self.assertEqual(ev.validate(sample(deep_link="#memory")), [])
        self.assertEqual(ev.web_deep_link("#memory"), "#memory")

    def test_web_equivalents_exist_for_platforms_without_schemes(self):
        self.assertEqual(ev.web_deep_link("alpha-proxima://github/pr/48"), "#github/pr/48")
        self.assertEqual(
            ev.web_deep_link("alpha-proxima://council/agent/CODEX", base="https://example.test"),
            "https://example.test/#council/agent/CODEX",
        )

    def test_a_foreign_scheme_cannot_be_converted(self):
        with self.assertRaises(ev.EventError):
            ev.web_deep_link("https://example.test/x")


class DeduplicationTests(unittest.TestCase):
    def test_the_same_provider_delivery_has_one_key_however_often_it_arrives(self):
        first = sample(provider_event_id="pr:48:opened", event_id="a" * 8)
        second = sample(provider_event_id="pr:48:opened", event_id="b" * 8,
                        received_at="2026-09-29T15:00:00+00:00")
        self.assertEqual(ev.dedup_key(first), ev.dedup_key(second))

    def test_different_event_types_on_one_entity_stay_distinct(self):
        opened = sample(provider_event_id="pr:48", event_type="github.pr.opened")
        merged = sample(provider_event_id="pr:48", event_type="github.pr.merged")
        self.assertNotEqual(ev.dedup_key(opened), ev.dedup_key(merged))

    def test_the_fallback_key_is_marked_as_weaker(self):
        self.assertTrue(ev.dedup_key(sample()).startswith("d:"))
        self.assertTrue(ev.dedup_key(sample(provider_event_id="x")).startswith("p:"))

    def test_the_fallback_key_uses_semantic_content(self):
        one = sample(event_id="a" * 8)
        two = sample(event_id="b" * 8)
        self.assertEqual(ev.dedup_key(one), ev.dedup_key(two))
        three = sample(entity_id="PR-49")
        self.assertNotEqual(ev.dedup_key(one), ev.dedup_key(three))


class OrderingTests(unittest.TestCase):
    def test_events_sort_by_occurrence_not_arrival(self):
        early_occurred_late_received = sample(
            entity_id="PR-1", occurred_at="2026-09-29T10:00:00+00:00",
            received_at="2026-09-29T18:00:00+00:00")
        late_occurred_early_received = sample(
            entity_id="PR-2", occurred_at="2026-09-29T12:00:00+00:00",
            received_at="2026-09-29T12:00:01+00:00")
        ordered = ev.sort_events([late_occurred_early_received, early_occurred_late_received])
        self.assertEqual([e["entity_id"] for e in ordered], ["PR-1", "PR-2"])

    def test_the_sort_is_total_and_stable_across_input_order(self):
        events = [sample(entity_id=f"PR-{n}", occurred_at="2026-09-29T10:00:00+00:00",
                         received_at="2026-09-29T10:00:00+00:00") for n in range(5)]
        forward = [e["event_id"] for e in ev.sort_events(events)]
        backward = [e["event_id"] for e in ev.sort_events(list(reversed(events)))]
        self.assertEqual(forward, backward)

    def test_mixed_offsets_compare_correctly(self):
        utc = sample(entity_id="PR-1", occurred_at="2026-09-29T12:00:00+00:00")
        offset = sample(entity_id="PR-2", occurred_at="2026-09-29T09:00:00-05:00")  # 14:00 UTC
        ordered = ev.sort_events([offset, utc])
        self.assertEqual([e["entity_id"] for e in ordered], ["PR-1", "PR-2"])

    def test_a_z_suffix_and_a_naive_stamp_are_both_read_as_utc(self):
        self.assertEqual(ev.parse_iso("2026-09-29T12:00:00Z"),
                         ev.parse_iso("2026-09-29T12:00:00+00:00"))
        self.assertEqual(ev.parse_iso("2026-09-29T12:00:00"),
                         ev.parse_iso("2026-09-29T12:00:00+00:00"))


class ChainTests(unittest.TestCase):
    def setUp(self):
        self.push = sample(entity_id="main@abc", event_id="push-1",
                           correlation_id="mission-1")
        self.commit = sample(entity_id="abc123", event_id="commit-1",
                             correlation_id="mission-1", causation_id="push-1")
        self.ci = sample(entity_id="check-1", event_id="ci-1",
                         correlation_id="mission-1", causation_id="commit-1")
        self.unrelated = sample(entity_id="PR-99", event_id="other-1",
                                correlation_id="mission-2")
        self.all = [self.ci, self.unrelated, self.push, self.commit]

    def test_a_causation_chain_reads_from_root_cause_to_effect(self):
        chain = ev.causation_chain(self.all, "ci-1")
        self.assertEqual([e["event_id"] for e in chain], ["push-1", "commit-1", "ci-1"])

    def test_a_correlation_group_collects_one_workflow_in_order(self):
        group = ev.correlation_group(self.all, "mission-1")
        self.assertEqual(len(group), 3)
        self.assertNotIn("other-1", [e["event_id"] for e in group])

    def test_an_event_with_no_cause_is_its_own_chain(self):
        self.assertEqual([e["event_id"] for e in ev.causation_chain(self.all, "push-1")],
                         ["push-1"])

    def test_a_cyclic_chain_terminates_instead_of_hanging(self):
        first = sample(event_id="a-1", causation_id="b-1")
        second = sample(event_id="b-1", causation_id="a-1")
        chain = ev.causation_chain([first, second], "a-1")
        self.assertEqual(len(chain), 2)

    def test_an_event_defaults_to_being_its_own_correlation_root(self):
        event = sample()
        self.assertEqual(event["correlation_id"], event["event_id"])


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "ledger.jsonl"
        self.ledger = ev.EventLedger(self.path)

    def tearDown(self):
        self.tmp.cleanup()

    def test_an_absent_ledger_reads_as_empty_rather_than_failing(self):
        self.assertEqual(self.ledger.events(), [])

    def test_appending_stores_one_line_per_event(self):
        stored, _ = self.ledger.append(sample(provider_event_id="one"))
        self.assertTrue(stored)
        self.assertEqual(len(self.path.read_text().strip().splitlines()), 1)

    def test_a_retried_delivery_is_ignored_without_being_an_error(self):
        self.ledger.append(sample(provider_event_id="one", event_id="first"))
        stored, _ = self.ledger.append(sample(provider_event_id="one", event_id="second"))
        self.assertFalse(stored)
        self.assertEqual(len(self.ledger.events()), 1)

    def test_a_batch_reports_new_and_retried_separately(self):
        first = sample(provider_event_id="one")
        again = sample(provider_event_id="one", event_id="different-id")
        second = sample(provider_event_id="two")
        result = self.ledger.extend([first, again, second])
        self.assertEqual(result, {"stored": 2, "duplicates": 1})

    def test_an_invalid_event_is_never_stored(self):
        broken = sample()
        broken["severity"] = "urgent"
        with self.assertRaises(ev.EventError):
            self.ledger.append(broken)
        self.assertFalse(self.path.exists())

    def test_the_ledger_offers_no_way_to_change_history(self):
        for forbidden in ("update", "delete", "edit", "remove", "set"):
            self.assertFalse(hasattr(self.ledger, forbidden),
                             f"EventLedger must not expose {forbidden}()")

    def test_a_torn_final_line_does_not_make_history_unreadable(self):
        self.ledger.append(sample(provider_event_id="one"))
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write('{"schema_version": "1.0", "event_id": "trunc')
        fresh = ev.EventLedger(self.path)
        self.assertEqual(len(fresh.events()), 1)
        self.assertEqual(fresh.damaged_lines(), [2])

    def test_repair_reports_exactly_what_it_dropped(self):
        self.ledger.append(sample(provider_event_id="one"))
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write("not json\n")
        result = ev.EventLedger(self.path).repair()
        self.assertEqual(result["removed"], 1)
        self.assertEqual(result["kept"], 1)
        self.assertEqual(ev.EventLedger(self.path).damaged_lines(), [])

    def test_the_idempotency_index_survives_a_reopen(self):
        self.ledger.append(sample(provider_event_id="one"))
        reopened = ev.EventLedger(self.path)
        self.assertTrue(reopened.contains(sample(provider_event_id="one",
                                                 event_id="another")))

    def test_events_are_returned_in_occurrence_order_regardless_of_write_order(self):
        self.ledger.append(sample(provider_event_id="late",
                                  occurred_at="2026-09-29T18:00:00+00:00"))
        self.ledger.append(sample(provider_event_id="early",
                                  occurred_at="2026-09-29T09:00:00+00:00"))
        occurred = [e["occurred_at"] for e in self.ledger.events()]
        self.assertEqual(occurred, sorted(occurred))


class ContractTests(unittest.TestCase):
    def test_the_published_contract_names_canonical_truth_elsewhere(self):
        contract = ev._contract()
        self.assertIn("Markdown", contract["canonical_truth"])
        self.assertEqual(contract["schema_version"], ev.SCHEMA_VERSION)

    def test_severity_order_is_the_notification_policy_and_is_stable(self):
        self.assertEqual(ev.SEVERITIES, ("info", "update", "action", "critical"))
        self.assertLess(ev.SEVERITY_RANK["update"], ev.SEVERITY_RANK["action"])

    def test_the_cli_validates_a_file_and_reports_failure_by_exit_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            good = Path(tmp) / "good.json"
            good.write_text(json.dumps([sample()]), encoding="utf-8")
            self.assertEqual(ev.main(["validate", str(good)]), 0)
            bad = Path(tmp) / "bad.json"
            bad.write_text(json.dumps([{"schema_version": "1.0"}]), encoding="utf-8")
            self.assertEqual(ev.main(["validate", str(bad)]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
