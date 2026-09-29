#!/usr/bin/env python3
"""Tests for the adapter boundary.

Two things are under test here, and the second matters more than the first.

The first is translation: a GitHub payload becomes the right AlphaEvent, and a
payload the adapter does not understand is rejected rather than guessed at.

The second is honesty. A registry that reports `connected` for an adapter no
delivery ever reached would make the Founder's integration screen actively
misleading — worse than absent. Several tests here exist only to make that
failure loud, including the one that replays every committed fixture and asserts
that doing so changes nothing about any adapter's status.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
FIXTURES = VAULT_ROOT / "13_OPERATIONS" / "Live Integration Layer" / "fixtures" / "github"


def _load(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLKIT_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ev = _load("alpha_events.py", "alpha_events")
ad = _load("alpha_adapters.py", "alpha_adapters")


def delivery(kind: str, payload: dict, **extra) -> dict:
    envelope = {
        "provider": "github",
        "kind": kind,
        "delivery_id": "d-0001",
        "received_at": "2026-09-29T14:05:00+00:00",
        "payload": payload,
    }
    envelope.update(extra)
    return envelope


REPO = {"full_name": "OmSadhiGuru/ALPHA.PROXIMA.CORE-"}


class GitHubNormalizationTests(unittest.TestCase):
    def setUp(self):
        self.adapter = ad.GitHubAdapter()

    def normalize(self, kind: str, payload: dict) -> list[dict]:
        events = self.adapter.normalize(delivery(kind, payload))
        for event in events:
            self.assertEqual(ev.validate(event), [], f"{kind} produced an invalid event")
        return events

    # -- push and commits ------------------------------------------------
    def test_a_push_yields_the_push_and_each_commit(self):
        events = self.normalize("push", {
            "ref": "refs/heads/feature",
            "after": "a" * 40,
            "sender": {"login": "codex-bot"},
            "repository": REPO,
            "commits": [
                {"id": "a" * 40, "message": "feat: one", "timestamp": "2026-09-29T13:59:00Z",
                 "author": {"name": "CODEX"}, "modified": ["x.py"]},
                {"id": "b" * 40, "message": "feat: two", "timestamp": "2026-09-29T14:00:00Z",
                 "author": {"name": "CODEX"}, "modified": ["y.py", "z.py"]},
            ],
        })
        types = [e["event_type"] for e in events]
        self.assertEqual(types[0], "github.push.completed")
        self.assertEqual(types[1:], ["github.commit.created", "github.commit.created"])

    def test_commits_name_the_push_as_their_cause_and_share_its_correlation(self):
        events = self.normalize("push", {
            "ref": "refs/heads/feature", "after": "a" * 40, "repository": REPO,
            "sender": {"login": "codex-bot"},
            "commits": [{"id": "c" * 40, "message": "one",
                         "timestamp": "2026-09-29T13:59:00Z", "modified": []}],
        })
        push, commit = events
        self.assertEqual(commit["causation_id"], push["event_id"])
        self.assertEqual(commit["correlation_id"], push["correlation_id"])

    def test_a_push_is_an_update_and_a_commit_is_only_information(self):
        events = self.normalize("push", {
            "ref": "refs/heads/main", "after": "d" * 40, "repository": REPO,
            "sender": {"login": "codex-bot"},
            "commits": [{"id": "d" * 40, "message": "one",
                         "timestamp": "2026-09-29T13:00:00Z", "modified": []}],
        })
        self.assertEqual(events[0]["severity"], "update")
        self.assertEqual(events[1]["severity"], "info")

    def test_the_founders_own_login_is_named_as_the_founder(self):
        events = self.normalize("push", {
            "ref": "refs/heads/main", "after": "e" * 40, "repository": REPO,
            "sender": {"login": "OmSadhiGuru"}, "commits": [],
        })
        self.assertEqual(events[0]["actor"], "Founder")

    def test_an_unknown_login_passes_through_rather_than_being_guessed_at(self):
        events = self.normalize("push", {
            "ref": "refs/heads/main", "after": "f" * 40, "repository": REPO,
            "sender": {"login": "some-contributor"}, "commits": [],
        })
        self.assertEqual(events[0]["actor"], "some-contributor")

    # -- branches --------------------------------------------------------
    def test_a_branch_creation_is_reported(self):
        events = self.normalize("create", {
            "ref_type": "branch", "ref": "codex/live-layer",
            "repository": REPO, "sender": {"login": "codex-bot"},
        })
        self.assertEqual(events[0]["event_type"], "github.branch.created")

    def test_a_tag_creation_is_not_a_reported_event(self):
        with self.assertRaises(ad.AdapterError):
            self.adapter.normalize(delivery("create", {"ref_type": "tag", "ref": "v1"}))

    # -- pull requests ---------------------------------------------------
    def pull(self, action: str, **pull_fields) -> list[dict]:
        pull = {"number": 48, "title": "Memory navigation", "state": "open",
                "updated_at": "2026-09-29T14:00:00Z", "head": {"ref": "codex/x"}}
        pull.update(pull_fields)
        return self.normalize("pull_request", {
            "action": action, "pull_request": pull,
            "repository": REPO, "sender": {"login": "codex-bot"},
        })

    def test_pull_request_actions_map_to_the_expected_event_types(self):
        cases = {
            "opened": "github.pr.opened",
            "reopened": "github.pr.reopened",
            "edited": "github.pr.updated",
            "synchronize": "github.pr.updated",
            "ready_for_review": "github.pr.review_required",
            "review_requested": "github.pr.review_required",
            "closed": "github.pr.closed",
        }
        for action, expected in cases.items():
            with self.subTest(action=action):
                self.assertEqual(self.pull(action)[0]["event_type"], expected)

    def test_a_merged_close_is_a_merge_not_a_close(self):
        events = self.pull("closed", merged=True, merged_at="2026-09-29T14:30:00Z")
        self.assertEqual(events[0]["event_type"], "github.pr.merged")
        self.assertEqual(events[0]["occurred_at"], "2026-09-29T14:30:00+00:00")

    def test_a_review_request_is_the_founders_business(self):
        event = self.pull("review_requested")[0]
        self.assertEqual(event["severity"], "action")
        self.assertTrue(event["requires_founder"])

    def test_ordinary_progress_does_not_demand_the_founder(self):
        for action in ("opened", "edited", "synchronize", "closed"):
            with self.subTest(action=action):
                self.assertFalse(self.pull(action)[0]["requires_founder"])

    def test_every_event_about_one_pull_request_shares_its_correlation(self):
        opened = self.pull("opened")[0]
        merged = self.pull("closed", merged=True, merged_at="2026-09-29T15:00:00Z")[0]
        self.assertEqual(opened["correlation_id"], "github:pr:48")
        self.assertEqual(merged["correlation_id"], "github:pr:48")

    def test_a_pull_request_carries_a_deep_link_to_itself(self):
        self.assertEqual(self.pull("opened")[0]["deep_link"], "alpha-proxima://github/pr/48")

    def test_uninteresting_actions_are_rejected_rather_than_stored(self):
        for action in ("labeled", "assigned", "unlocked", "auto_merge_enabled"):
            with self.subTest(action=action):
                with self.assertRaises(ad.AdapterError):
                    self.pull(action)

    def test_a_pull_request_with_no_number_is_rejected(self):
        with self.assertRaises(ad.AdapterError):
            self.adapter.normalize(delivery("pull_request", {
                "action": "opened", "pull_request": {"title": "no number"}}))

    # -- reviews ---------------------------------------------------------
    def test_changes_requested_is_the_review_outcome_that_costs_attention(self):
        events = self.normalize("pull_request_review", {
            "action": "submitted", "repository": REPO, "sender": {"login": "OmSadhiGuru"},
            "review": {"id": 7001, "state": "changes_requested", "body": "Needs a test",
                       "submitted_at": "2026-09-29T14:10:00Z"},
            "pull_request": {"number": 48},
        })
        self.assertEqual(events[0]["event_type"], "github.review.changes_requested")
        self.assertEqual(events[0]["severity"], "action")
        self.assertTrue(events[0]["requires_founder"])

    def test_an_approval_is_progress_not_an_obligation(self):
        events = self.normalize("pull_request_review", {
            "action": "submitted", "repository": REPO, "sender": {"login": "OmSadhiGuru"},
            "review": {"id": 7002, "state": "approved",
                       "submitted_at": "2026-09-29T14:12:00Z"},
            "pull_request": {"number": 48},
        })
        self.assertEqual(events[0]["severity"], "update")
        self.assertFalse(events[0]["requires_founder"])

    def test_only_a_submitted_review_is_reported(self):
        with self.assertRaises(ad.AdapterError):
            self.adapter.normalize(delivery("pull_request_review", {
                "action": "dismissed", "review": {"id": 1}, "pull_request": {"number": 48}}))

    # -- CI --------------------------------------------------------------
    def check(self, status: str, conclusion: str | None, number: int | None = 48) -> list[dict]:
        run = {"id": 900, "name": "Foundation Integrity", "status": status,
               "conclusion": conclusion, "started_at": "2026-09-29T14:00:00Z",
               "completed_at": "2026-09-29T14:05:00Z",
               "pull_requests": [{"number": number}] if number else []}
        return self.normalize("check_run", {
            "check_run": run, "repository": REPO, "sender": {"login": "github-actions[bot]"}})

    def test_ci_outcomes_map_to_the_expected_event_types(self):
        self.assertEqual(self.check("in_progress", None)[0]["event_type"], "github.ci.started")
        self.assertEqual(self.check("completed", "success")[0]["event_type"], "github.ci.succeeded")
        self.assertEqual(self.check("completed", "failure")[0]["event_type"], "github.ci.failed")
        self.assertEqual(self.check("completed", "cancelled")[0]["event_type"], "github.ci.skipped")

    def test_a_failed_check_asks_for_the_founder_but_is_not_critical(self):
        event = self.check("completed", "failure")[0]
        self.assertEqual(event["severity"], "action")
        self.assertTrue(event["requires_founder"])

    def test_a_passing_check_is_only_information(self):
        self.assertEqual(self.check("completed", "success")[0]["severity"], "info")

    def test_ci_events_correlate_to_the_pull_request_they_ran_for(self):
        self.assertEqual(self.check("completed", "failure")[0]["correlation_id"], "github:pr:48")

    def test_a_check_with_no_pull_request_still_links_somewhere_openable(self):
        event = self.check("completed", "failure", number=None)[0]
        self.assertEqual(ev.validate_deep_link(event["deep_link"]), [])

    def test_a_check_with_no_outcome_is_rejected(self):
        with self.assertRaises(ad.AdapterError):
            self.adapter.normalize(delivery("check_run", {
                "check_run": {"id": 1, "status": "completed", "conclusion": "who_knows"}}))

    def test_a_workflow_run_reports_the_same_ci_vocabulary(self):
        events = self.normalize("workflow_run", {
            "workflow_run": {"id": 555, "name": "Foundation Integrity", "status": "completed",
                             "conclusion": "failure", "run_started_at": "2026-09-29T14:00:00Z",
                             "updated_at": "2026-09-29T14:06:00Z", "pull_requests": []},
            "repository": REPO, "sender": {"login": "github-actions[bot]"}})
        self.assertEqual(events[0]["event_type"], "github.ci.failed")
        self.assertEqual(events[0]["entity_type"], "workflow_run")

    # -- issues and deployments ------------------------------------------
    def test_issue_actions_map_to_the_expected_event_types(self):
        for action, expected in (("opened", "github.issue.created"),
                                 ("edited", "github.issue.updated"),
                                 ("closed", "github.issue.closed")):
            with self.subTest(action=action):
                events = self.normalize("issues", {
                    "action": action, "repository": REPO, "sender": {"login": "OmSadhiGuru"},
                    "issue": {"number": 12, "title": "Coherence debt", "state": "open",
                              "updated_at": "2026-09-29T14:00:00Z"}})
                self.assertEqual(events[0]["event_type"], expected)

    def test_a_failed_deployment_is_the_one_critical_github_event(self):
        events = self.normalize("deployment_status", {
            "deployment": {"id": 4242, "environment": "production",
                           "created_at": "2026-09-29T14:00:00Z"},
            "deployment_status": {"state": "failure", "description": "Ingress unreachable",
                                  "updated_at": "2026-09-29T14:02:00Z"},
            "repository": REPO, "sender": {"login": "github-actions[bot]"}})
        self.assertEqual(events[0]["severity"], "critical")
        self.assertTrue(events[0]["requires_founder"])

    def test_a_successful_deployment_is_not_an_emergency(self):
        events = self.normalize("deployment_status", {
            "deployment": {"id": 4243, "environment": "production",
                           "created_at": "2026-09-29T14:00:00Z"},
            "deployment_status": {"state": "success", "updated_at": "2026-09-29T14:02:00Z"},
            "repository": REPO, "sender": {"login": "github-actions[bot]"}})
        self.assertEqual(events[0]["severity"], "update")

    # -- boundary refusals -----------------------------------------------
    def test_an_unhandled_provider_event_name_is_refused(self):
        with self.assertRaises(ad.AdapterError):
            self.adapter.normalize(delivery("star", {"action": "created"}))

    def test_a_delivery_without_a_payload_is_refused(self):
        with self.assertRaises(ad.AdapterError):
            self.adapter.normalize({"provider": "github", "kind": "push"})

    def test_a_delivery_without_a_kind_is_refused(self):
        with self.assertRaises(ad.AdapterError):
            self.adapter.normalize({"provider": "github", "payload": {}})

    def test_a_non_object_delivery_is_refused(self):
        for payload in ([], "push", None, 3):
            with self.subTest(payload=payload):
                with self.assertRaises(ad.AdapterError):
                    self.adapter.normalize(payload)

    def test_an_unparseable_provider_timestamp_falls_back_rather_than_failing(self):
        events = self.normalize("pull_request", {
            "action": "opened", "repository": REPO, "sender": {"login": "codex-bot"},
            "pull_request": {"number": 48, "title": "x", "state": "open",
                             "updated_at": "whenever", "head": {"ref": "y"}}})
        self.assertEqual(events[0]["occurred_at"], "2026-09-29T14:05:00+00:00")

    def test_no_normalized_event_ever_carries_a_credential(self):
        events = self.normalize("pull_request", {
            "action": "opened", "repository": REPO,
            "sender": {"login": "codex-bot"},
            "pull_request": {"number": 48, "title": "x", "state": "open",
                             "updated_at": "2026-09-29T14:00:00Z", "head": {"ref": "y"},
                             # A provider payload carrying a token must not
                             # propagate it: the adapter copies named fields only.
                             "installation_token": "ghs_should_never_appear"}})
        self.assertNotIn("ghs_should_never_appear", json.dumps(events))


class SignatureTests(unittest.TestCase):
    def test_a_correct_signature_verifies(self):
        body = b'{"action":"opened"}'
        import hashlib
        import hmac
        secret = "s3cr3t"
        header = "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
        self.assertTrue(ad.verify_github_signature(secret, body, header))

    def test_a_tampered_body_does_not_verify(self):
        import hashlib
        import hmac
        secret = "s3cr3t"
        header = "sha256=" + hmac.new(secret.encode(), b"original", hashlib.sha256).hexdigest()
        self.assertFalse(ad.verify_github_signature(secret, b"tampered", header))

    def test_a_missing_secret_or_header_never_verifies(self):
        self.assertFalse(ad.verify_github_signature("", b"x", "sha256=abc"))
        self.assertFalse(ad.verify_github_signature("s", b"x", ""))


class PlannedAdapterTests(unittest.TestCase):
    def test_every_provider_in_the_brief_has_a_registered_adapter(self):
        registered = {cls.provider for cls in ad.ADAPTER_CLASSES}
        for provider in ("github", "chatgpt", "codex", "claude", "gemini", "perplexity",
                         "pocket_ai", "obsidian", "google_drive", "google_calendar",
                         "notion", "n8n"):
            self.assertIn(provider, registered)

    def test_a_planned_adapter_refuses_to_normalize_anything(self):
        for cls in ad.ADAPTER_CLASSES:
            adapter = cls()
            if adapter.declared_status in ("planned", "blocked"):
                with self.subTest(adapter=adapter.adapter_id):
                    with self.assertRaises(ad.AdapterError):
                        adapter.normalize(delivery("anything", {"x": 1}))

    def test_no_adapter_declares_itself_connected(self):
        # Connection is observed, never declared. A class attribute cannot
        # assert that an external system is reachable.
        for cls in ad.ADAPTER_CLASSES:
            self.assertNotEqual(cls.declared_status, "connected", cls.__name__)

    def test_every_unavailable_adapter_states_a_reason_and_its_configuration(self):
        for cls in ad.ADAPTER_CLASSES:
            adapter = cls()
            if adapter.declared_status != "connected":
                with self.subTest(adapter=adapter.adapter_id):
                    self.assertTrue(adapter.blocked_reason.strip(),
                                    "an unavailable adapter must say why")

    def test_a_descriptor_names_configuration_but_never_a_value(self):
        for cls in ad.ADAPTER_CLASSES:
            descriptor = cls().descriptor()
            with self.subTest(adapter=descriptor["adapter_id"]):
                # Credential-shaped *keys* would mean a value is being carried.
                # Names in `configuration_required` are values of an ordinary
                # key, which is the whole point: the name is publishable.
                self.assertEqual(ev.secret_leaks(descriptor, "descriptor"), [])
                for name in descriptor["configuration_required"]:
                    self.assertEqual(name, name.upper(),
                                     "configuration is named by environment variable")

    def test_the_blocked_adapter_is_distinguished_from_the_merely_unbuilt(self):
        blocked = [cls for cls in ad.ADAPTER_CLASSES if cls.declared_status == "blocked"]
        self.assertTrue(blocked, "the vector-index gap is a Founder decision, not a task")
        self.assertIn("Memory Architect", blocked[0].blocked_reason)


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.registry = ad.AdapterRegistry(self.dir / "registry.json")
        self.ledger = ev.EventLedger(self.dir / "ledger.jsonl")

    def tearDown(self):
        self.tmp.cleanup()

    def test_an_adapter_with_no_success_is_disconnected_not_connected(self):
        self.assertEqual(self.registry.observed_status("ADP-GITHUB"), "disconnected")

    def test_errors_alone_do_not_make_an_adapter_degraded(self):
        # Degraded means "it worked and then stopped". It has never worked.
        self.registry.record_failure("ADP-GITHUB", "bad payload")
        self.assertEqual(self.registry.observed_status("ADP-GITHUB"), "disconnected")

    def test_a_verified_success_earns_connected(self):
        self.registry.record_success("ADP-GITHUB", at="2026-09-29T14:00:00+00:00")
        self.assertEqual(
            self.registry.observed_status("ADP-GITHUB", now="2026-09-29T14:01:00+00:00"),
            "connected")

    def test_a_failure_after_a_success_is_degraded(self):
        self.registry.record_success("ADP-GITHUB", at="2026-09-29T14:00:00+00:00")
        self.registry.record_failure("ADP-GITHUB", "timeout", at="2026-09-29T14:05:00+00:00")
        self.assertEqual(
            self.registry.observed_status("ADP-GITHUB", now="2026-09-29T14:06:00+00:00"),
            "degraded")

    def test_silence_past_the_staleness_window_is_degraded_not_connected(self):
        self.registry.record_success("ADP-GITHUB", at="2026-09-01T14:00:00+00:00")
        self.assertEqual(
            self.registry.observed_status("ADP-GITHUB", now="2026-09-29T14:00:00+00:00"),
            "degraded")

    def test_telemetry_cannot_promote_a_planned_adapter(self):
        self.registry.record_success("ADP-NOTION", at="2026-09-29T14:00:00+00:00")
        self.assertEqual(
            self.registry.observed_status("ADP-NOTION", now="2026-09-29T14:00:30+00:00"),
            "planned")

    def test_an_unknown_adapter_has_no_health_to_record(self):
        with self.assertRaises(ad.AdapterError):
            self.registry.record_success("ADP-IMAGINARY")

    def test_the_view_never_reports_a_planned_adapter_as_connected(self):
        view = self.registry.view()
        for row in view["adapters"]:
            if row["declared_status"] in ("planned", "blocked"):
                self.assertFalse(row["connected"], row["adapter_id"])

    def test_the_view_answers_what_is_broken(self):
        view = self.registry.view()
        broken = {row["adapter_id"] for row in view["broken"]}
        self.assertIn("ADP-GITHUB", broken)
        for row in view["broken"]:
            self.assertTrue(row["reason"], f"{row['adapter_id']} is broken without a reason")

    def test_health_survives_a_reload(self):
        self.registry.record_success("ADP-GITHUB", events=3, at="2026-09-29T14:00:00+00:00")
        self.registry.save()
        reloaded = ad.AdapterRegistry(self.registry.path)
        self.assertEqual(
            reloaded.observed_status("ADP-GITHUB", now="2026-09-29T14:00:30+00:00"), "connected")

    def test_a_corrupt_health_file_degrades_rather_than_crashes(self):
        self.registry.path.parent.mkdir(parents=True, exist_ok=True)
        self.registry.path.write_text("{not json", encoding="utf-8")
        fresh = ad.AdapterRegistry(self.registry.path)
        self.assertEqual(fresh.observed_status("ADP-GITHUB"), "disconnected")


class IngestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.registry = ad.AdapterRegistry(self.dir / "registry.json")
        self.ledger = ev.EventLedger(self.dir / "ledger.jsonl")
        self.push = delivery("push", {
            "ref": "refs/heads/main", "after": "a" * 40, "repository": REPO,
            "sender": {"login": "codex-bot"},
            "commits": [{"id": "a" * 40, "message": "one",
                         "timestamp": "2026-09-29T14:00:00Z", "modified": []}]})

    def tearDown(self):
        self.tmp.cleanup()

    def test_ingest_normalizes_stores_and_reports(self):
        result = self.registry.ingest(dict(self.push, origin="webhook"), self.ledger)
        self.assertEqual(result["accepted"], 2)
        self.assertEqual(result["stored"], 2)
        self.assertEqual(result["duplicates"], 0)
        self.assertEqual(len(self.ledger.events()), 2)

    def test_a_retried_webhook_stores_nothing_the_second_time(self):
        self.registry.ingest(dict(self.push, origin="webhook"), self.ledger)
        again = self.registry.ingest(dict(self.push, origin="webhook"), self.ledger)
        self.assertEqual(again["stored"], 0)
        self.assertEqual(again["duplicates"], 2)
        self.assertEqual(len(self.ledger.events()), 2)

    def test_a_verified_webhook_promotes_the_adapter(self):
        self.registry.ingest(dict(self.push, origin="webhook"), self.ledger)
        self.assertEqual(self.registry.observed_status("ADP-GITHUB"), "connected")

    def test_a_rehearsal_stores_events_but_never_claims_a_connection(self):
        result = self.registry.ingest(self.push, self.ledger)
        self.assertFalse(result["verified"])
        self.assertEqual(result["stored"], 2)
        self.assertEqual(self.registry.observed_status("ADP-GITHUB"), "disconnected")

    def test_replaying_every_committed_fixture_changes_no_adapter_status(self):
        # The guard that matters: a developer can exercise the whole layer
        # locally without the integration screen ever becoming a fiction.
        before = {row["adapter_id"]: row["status"] for row in self.registry.view()["adapters"]}
        for path in sorted(FIXTURES.glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            try:
                self.registry.ingest(payload, self.ledger)
            except ad.AdapterError:
                continue  # the deliberately malformed fixtures
        after = {row["adapter_id"]: row["status"] for row in self.registry.view()["adapters"]}
        self.assertEqual(before, after)

    def test_a_rejected_payload_is_counted_as_a_failure_not_a_crash(self):
        with self.assertRaises(ad.AdapterError):
            self.registry.ingest(delivery("pull_request", {"action": "opened",
                                                           "pull_request": {}}), self.ledger)
        self.assertEqual(self.registry.health["ADP-GITHUB"]["error_count"], 1)
        self.assertEqual(self.ledger.events(), [])

    def test_an_unknown_provider_is_rejected_rather_than_stored(self):
        with self.assertRaises(ad.AdapterError):
            self.registry.ingest({"provider": "myspace", "kind": "poke", "payload": {}},
                                 self.ledger)
        self.assertEqual(self.ledger.events(), [])

    def test_a_planned_provider_delivery_is_refused_with_its_reason(self):
        with self.assertRaises(ad.AdapterError) as caught:
            self.registry.ingest({"provider": "notion", "kind": "page.updated",
                                  "payload": {"id": "x"}}, self.ledger)
        self.assertIn("planned", str(caught.exception))

    def test_ingest_records_latency_for_observability(self):
        result = self.registry.ingest(dict(self.push, origin="webhook"), self.ledger)
        self.assertGreaterEqual(result["latency_ms"], 0)
        self.assertIsNotNone(self.registry.health["ADP-GITHUB"]["last_latency_ms"])

    def test_the_committed_fixtures_all_normalize_or_are_labelled_malformed(self):
        for path in sorted(FIXTURES.glob("*.json")):
            with self.subTest(fixture=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                adapter = ad.GitHubAdapter()
                if "malformed" in path.name:
                    with self.assertRaises(ad.AdapterError):
                        adapter.normalize(payload)
                else:
                    for event in adapter.normalize(payload):
                        self.assertEqual(ev.validate(event), [])


class NoWriteTests(unittest.TestCase):
    def identifiers(self, filename: str) -> set[str]:
        """Every name the module's code actually references.

        Read from the parse tree rather than from the text, so a docstring that
        *discusses* the state engine does not fail a test about whether the code
        can *reach* it. Prose is free; imports are not.
        """
        import ast
        tree = ast.parse((TOOLKIT_DIR / filename).read_text(encoding="utf-8"))
        names: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                names.add(node.id)
            elif isinstance(node, ast.Attribute):
                names.add(node.attr)
            elif isinstance(node, ast.Import):
                names.update(alias.asname or alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                names.add(node.module or "")
                names.update(alias.asname or alias.name for alias in node.names)
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                    and node.func.id == "_load_sibling":
                names.update(arg.value for arg in node.args
                             if isinstance(arg, ast.Constant) and isinstance(arg.value, str))
        return names

    def test_the_adapter_module_cannot_reach_the_founder_state_engine(self):
        # Structural, not aspirational: the single-writer model holds because
        # this module has no way to write Founder state, not because it chooses
        # not to.
        names = self.identifiers("alpha_adapters.py")
        self.assertNotIn("founder_os", names)
        self.assertNotIn("founder_os.py", names)

    def test_the_live_projections_cannot_reach_the_founder_state_engine_either(self):
        names = self.identifiers("alpha_live.py")
        self.assertNotIn("founder_os", names)
        self.assertNotIn("founder_os.py", names)

    def test_neither_module_can_write_a_markdown_note(self):
        for filename in ("alpha_adapters.py", "alpha_live.py"):
            with self.subTest(module=filename):
                names = self.identifiers(filename)
                for writer in ("write_text", "write_bytes", "mkstemp"):
                    self.assertNotIn(writer, names)

    def test_each_module_writes_exactly_one_file_and_it_is_its_own(self):
        """Every write in the live layer goes through the atomic helper.

        One call site per module, each targeting that module's own store. A
        second call site is the review trigger: it would mean the layer had
        grown a second thing it can change.
        """
        import ast
        for filename, expected in (("alpha_adapters.py", "self.path"),
                                   ("alpha_live.py", "self.path")):
            with self.subTest(module=filename):
                tree = ast.parse((TOOLKIT_DIR / filename).read_text(encoding="utf-8"))
                calls = [
                    node for node in ast.walk(tree)
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "write_json_atomic"
                ]
                self.assertEqual(len(calls), 1, f"{filename} has more than one writer")
                self.assertEqual(ast.unparse(calls[0].args[0]), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
