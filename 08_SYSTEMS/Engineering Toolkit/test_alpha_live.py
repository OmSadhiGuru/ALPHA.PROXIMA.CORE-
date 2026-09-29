#!/usr/bin/env python3
"""Tests for the live projections: activity, presence, notifications, badge.

The projections are where a live system most easily starts lying — a presence
badge that outlived its process, a badge count that grew with activity instead
of obligation, a feed that looks empty during an outage. Each of those is a
test here, written as the refusal rather than the feature.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

TOOLKIT_DIR = Path(__file__).resolve().parent


def _load(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLKIT_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ev = _load("alpha_events.py", "alpha_events")
ad = _load("alpha_adapters.py", "alpha_adapters")
live = _load("alpha_live.py", "alpha_live")

NOON = "2026-09-29T12:00:00+00:00"


def event(severity: str = "update", **overrides) -> dict:
    fields = dict(
        source="github", actor="CODEX", department="ENGINEERING",
        event_type="github.pr.opened", entity_type="pull_request",
        entity_id="PR-48", title="PR-48 opened", summary="Three files modified",
        severity=severity, occurred_at=NOON, received_at=NOON,
        deep_link="alpha-proxima://github/pr/48",
    )
    fields.update(overrides)
    return ev.make_event(**fields)


class NotificationPolicyTests(unittest.TestCase):
    def test_each_severity_earns_exactly_the_channels_the_policy_states(self):
        expected = {
            "info": ["feed"],
            "update": ["feed", "badge"],
            "action": ["feed", "badge", "push"],
            "critical": ["feed", "badge", "push"],
        }
        for severity, channels in expected.items():
            with self.subTest(severity=severity):
                decision = live.evaluate_notification(event(severity))
                self.assertEqual(decision["channels"], channels)

    def test_information_never_pushes(self):
        self.assertNotIn("push", live.evaluate_notification(event("info"))["channels"])

    def test_requires_founder_raises_an_ordinary_event_to_action(self):
        decision = live.evaluate_notification(event("info", requires_founder=True))
        self.assertEqual(decision["effective_severity"], "action")
        self.assertIn("push", decision["channels"])

    def test_requires_founder_cannot_lower_a_critical_event(self):
        decision = live.evaluate_notification(event("critical", requires_founder=False))
        self.assertEqual(decision["effective_severity"], "critical")
        self.assertIn("push", decision["channels"])

    def test_the_declared_severity_is_preserved_alongside_the_effective_one(self):
        decision = live.evaluate_notification(event("info", requires_founder=True))
        self.assertEqual(decision["severity"], "info")
        self.assertEqual(decision["effective_severity"], "action")

    def test_an_unroutable_severity_is_an_error_not_a_silent_drop(self):
        broken = event()
        broken["severity"] = "whenever"
        with self.assertRaises(ev.EventError):
            live.evaluate_notification(broken)

    def test_a_subscription_can_withhold_a_channel_and_says_so(self):
        subscription = {"id": "SUB-quiet", "source": "github", "channels": ["feed", "badge"]}
        decision = live.evaluate_notification(event("action"), [subscription])
        self.assertNotIn("push", decision["channels"])
        self.assertEqual(decision["withheld"][0]["channel"], "push")
        self.assertIn("SUB-quiet", decision["withheld"][0]["reason"])

    def test_a_critical_event_overrides_preferences(self):
        subscription = {"id": "SUB-quiet", "source": "github", "channels": ["feed"]}
        decision = live.evaluate_notification(event("critical"), [subscription])
        self.assertIn("push", decision["channels"])
        self.assertTrue(decision["bypassed_preferences"])

    def test_the_most_specific_subscription_wins(self):
        broad = {"id": "SUB-broad", "source": "github", "channels": ["feed"]}
        narrow = {"id": "SUB-narrow", "source": "github", "department": "ENGINEERING",
                  "channels": ["feed", "badge", "push"]}
        decision = live.evaluate_notification(event("action"), [broad, narrow])
        self.assertEqual(decision["subscription_id"], "SUB-narrow")
        self.assertIn("push", decision["channels"])

    def test_a_subscription_for_another_source_does_not_apply(self):
        other = {"id": "SUB-notion", "source": "notion", "channels": ["feed"]}
        decision = live.evaluate_notification(event("action"), [other])
        self.assertIsNone(decision["subscription_id"])
        self.assertIn("push", decision["channels"])

    def test_a_severity_floor_excludes_quieter_events(self):
        floor = {"id": "SUB-floor", "min_severity": "critical", "channels": ["feed"]}
        decision = live.evaluate_notification(event("update"), [floor])
        self.assertIsNone(decision["subscription_id"])


class ActivityProjectionTests(unittest.TestCase):
    def test_the_feed_is_newest_first(self):
        early = event(entity_id="PR-1", occurred_at="2026-09-29T10:00:00+00:00")
        late = event(entity_id="PR-2", occurred_at="2026-09-29T11:00:00+00:00")
        view = live.build_activities([early, late], now=NOON)
        self.assertEqual([row["entity_id"] for row in view["activities"]], ["PR-2", "PR-1"])

    def test_ages_are_computed_against_the_reference_instant(self):
        view = live.build_activities([event(occurred_at="2026-09-29T11:30:00+00:00")], now=NOON)
        self.assertEqual(view["activities"][0]["age_seconds"], 1800)

    def test_a_future_timestamp_does_not_produce_a_negative_age(self):
        view = live.build_activities([event(occurred_at="2026-09-29T13:00:00+00:00")], now=NOON)
        self.assertEqual(view["activities"][0]["age_seconds"], 0)

    def test_every_row_carries_both_a_native_and_a_web_link(self):
        view = live.build_activities([event()], now=NOON)
        row = view["activities"][0]
        self.assertEqual(row["deep_link"], "alpha-proxima://github/pr/48")
        self.assertEqual(row["web_link"], "#github/pr/48")

    def test_an_event_with_no_link_does_not_break_the_feed(self):
        view = live.build_activities([event(deep_link="")], now=NOON)
        self.assertEqual(view["activities"][0]["web_link"], "")

    def test_counts_describe_the_whole_ledger_not_the_returned_page(self):
        events = [event(entity_id=f"PR-{n}", occurred_at=f"2026-09-29T10:{n:02d}:00+00:00")
                  for n in range(10)]
        view = live.build_activities(events, limit=3, now=NOON)
        self.assertEqual(view["counts"]["returned"], 3)
        self.assertEqual(view["counts"]["total"], 10)

    def test_the_founder_attention_count_is_reported_separately(self):
        events = [event("action", entity_id="PR-1", requires_founder=True),
                  event("info", entity_id="PR-2")]
        view = live.build_activities(events, now=NOON)
        self.assertEqual(view["counts"]["requires_founder"], 1)

    def test_the_projection_never_mutates_the_events_it_reads(self):
        original = event()
        snapshot = dict(original)
        live.build_activities([original], now=NOON)
        self.assertEqual(original, snapshot)


class EntityHistoryTests(unittest.TestCase):
    def setUp(self):
        self.events = [
            event("update", entity_id="PR-48", actor="CODEX",
                  event_type="github.pr.opened", occurred_at="2026-09-29T10:00:00+00:00"),
            event("action", entity_id="PR-48", actor="Founder",
                  event_type="github.review.changes_requested", entity_type="pull_request",
                  occurred_at="2026-09-29T11:00:00+00:00"),
            event("update", entity_id="PR-48", actor="CODEX",
                  event_type="github.pr.merged", occurred_at="2026-09-29T12:00:00+00:00"),
            event("info", entity_id="PR-99", actor="CODEX",
                  event_type="github.pr.opened", occurred_at="2026-09-29T09:00:00+00:00"),
        ]

    def test_a_history_holds_only_that_entitys_events_in_order(self):
        history = live.build_entity_history(self.events, "PR-48")
        self.assertEqual(history["counts"]["events"], 3)
        self.assertEqual(history["first_seen"], "2026-09-29T10:00:00+00:00")
        self.assertEqual(history["last_seen"], "2026-09-29T12:00:00+00:00")

    def test_a_history_names_everyone_who_touched_the_entity(self):
        history = live.build_entity_history(self.events, "PR-48")
        self.assertEqual(history["actors"], ["CODEX", "Founder"])

    def test_an_unknown_entity_returns_an_honest_empty_history(self):
        history = live.build_entity_history(self.events, "PR-404")
        self.assertEqual(history["counts"]["events"], 0)
        self.assertIsNone(history["first_seen"])


class PresenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = live.LiveStore(Path(self.tmp.name) / "live.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_a_fresh_report_is_live_and_shows_its_activity(self):
        self.store.set_presence("CODEX", "coding", activity="PR-48", at=NOON)
        view = self.store.presence_view(now="2026-09-29T12:00:30+00:00")
        row = view["presence"][0]
        self.assertEqual(row["state"], "coding")
        self.assertFalse(row["stale"])
        self.assertEqual(row["activity"], "PR-48")

    def test_an_expired_report_is_offline_not_still_coding(self):
        self.store.set_presence("CODEX", "coding", activity="PR-48", at=NOON)
        view = self.store.presence_view(now="2026-09-29T12:20:00+00:00")
        row = view["presence"][0]
        self.assertEqual(row["state"], "offline")
        self.assertTrue(row["stale"])

    def test_an_expired_report_keeps_what_it_last_reported_for_context(self):
        self.store.set_presence("CODEX", "coding", activity="PR-48", at=NOON)
        row = self.store.presence_view(now="2026-09-29T12:20:00+00:00")["presence"][0]
        self.assertEqual(row["reported_state"], "coding")
        self.assertEqual(row["activity"], "", "a stale activity must not read as current")
        self.assertEqual(row["age_seconds"], 1200)

    def test_expiry_happens_exactly_at_the_ttl(self):
        self.store.set_presence("CODEX", "coding", at=NOON)
        inside = self.store.presence_view(
            now="2026-09-29T12:02:59+00:00")["presence"][0]
        outside = self.store.presence_view(
            now="2026-09-29T12:03:01+00:00")["presence"][0]
        self.assertFalse(inside["stale"])
        self.assertTrue(outside["stale"])

    def test_presence_declares_itself_ephemeral(self):
        view = self.store.presence_view(now=NOON)
        self.assertTrue(view["ephemeral"])
        self.assertEqual(view["ttl_seconds"], live.PRESENCE_TTL_SECONDS)

    def test_a_report_overwrites_rather_than_accumulating(self):
        self.store.set_presence("CODEX", "thinking", at=NOON)
        self.store.set_presence("CODEX", "coding", at=NOON)
        view = self.store.presence_view(now=NOON)
        self.assertEqual(len(view["presence"]), 1)
        self.assertEqual(view["presence"][0]["state"], "coding")

    def test_an_unknown_state_is_refused(self):
        with self.assertRaises(ev.EventError):
            self.store.set_presence("CODEX", "vibing")

    def test_only_working_states_count_as_working(self):
        self.store.set_presence("CODEX", "coding", at=NOON)
        self.store.set_presence("VORTEX", "waiting", at=NOON)
        self.store.set_presence("ATHENA", "blocked", at=NOON)
        counts = self.store.presence_view(now=NOON)["counts"]
        self.assertEqual(counts["live"], 3)
        self.assertEqual(counts["working"], 1)

    def test_stale_records_are_counted_separately_from_live_ones(self):
        self.store.set_presence("CODEX", "coding", at=NOON)
        self.store.set_presence("JERANIUM", "indexing", at="2026-09-29T11:00:00+00:00")
        counts = self.store.presence_view(now=NOON)["counts"]
        self.assertEqual(counts["live"], 1)
        self.assertEqual(counts["stale"], 1)

    def test_pruning_drops_records_too_old_to_inform_anything(self):
        self.store.set_presence("OLD", "coding", at="2026-09-01T12:00:00+00:00")
        self.store.set_presence("NEW", "coding", at=NOON)
        self.assertEqual(self.store.prune_presence(now=NOON), 1)
        self.assertEqual(len(self.store.presence_view(now=NOON)["presence"]), 1)

    def test_presence_survives_a_reload_but_still_expires(self):
        self.store.set_presence("CODEX", "coding", at=NOON)
        self.store.save()
        reloaded = live.LiveStore(self.store.path)
        row = reloaded.presence_view(now="2026-09-29T12:30:00+00:00")["presence"][0]
        self.assertTrue(row["stale"])


class NotificationLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = live.LiveStore(Path(self.tmp.name) / "live.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_an_information_event_produces_no_notification(self):
        self.assertIsNone(self.store.notify(event("info")))

    def test_an_update_produces_a_queued_badge_notification(self):
        record = self.store.notify(event("update"), at=NOON)
        self.assertEqual(record["state"], "queued")
        self.assertEqual(record["channels"], ["badge"])

    def test_an_action_produces_a_push_notification(self):
        record = self.store.notify(event("action"), at=NOON)
        self.assertIn("push", record["channels"])

    def test_notifying_twice_for_one_event_creates_one_record(self):
        first = self.store.notify(event("action", event_id="e-1"), at=NOON)
        second = self.store.notify(event("action", event_id="e-1"), at=NOON)
        self.assertEqual(first["id"], second["id"])
        self.assertEqual(len(self.store.state["notifications"]), 1)

    def test_a_notification_carries_a_link_back_to_its_context(self):
        record = self.store.notify(event("action"), at=NOON)
        self.assertEqual(record["deep_link"], "alpha-proxima://github/pr/48")
        self.assertEqual(record["web_link"], "#github/pr/48")

    def test_the_lifecycle_transitions_are_recorded_with_their_instants(self):
        record = self.store.notify(event("action"), at=NOON)
        delivered = self.store.mark_delivered(record["id"], at="2026-09-29T12:00:05+00:00")
        self.assertEqual(delivered["state"], "delivered")
        self.assertEqual(delivered["delivered_at"], "2026-09-29T12:00:05+00:00")
        read = self.store.mark_read(record["id"], at="2026-09-29T12:05:00+00:00")
        self.assertEqual(read["state"], "read")
        self.assertEqual(read["read_at"], "2026-09-29T12:05:00+00:00")

    def test_dismissing_is_distinct_from_reading(self):
        record = self.store.notify(event("action"), at=NOON)
        dismissed = self.store.dismiss(record["id"], at=NOON)
        self.assertEqual(dismissed["state"], "dismissed")
        self.assertIsNone(dismissed["read_at"])

    def test_a_failure_records_its_reason_and_stays_retryable(self):
        record = self.store.notify(event("action"), at=NOON)
        failed = self.store.mark_failed(record["id"], "APNs 503", at=NOON)
        self.assertEqual(failed["state"], "failed")
        self.assertIn("APNs 503", failed["last_error"]["reason"])
        self.assertTrue(failed["retryable"])

    def test_a_notification_stops_being_retryable_at_the_attempt_ceiling(self):
        record = self.store.notify(event("action"), at=NOON)
        for _ in range(live.MAX_DELIVERY_ATTEMPTS):
            self.store.mark_failed(record["id"], "APNs 503", at=NOON)
        self.assertFalse(record["retryable"])
        self.assertNotIn(record, self.store.queued())

    def test_an_exhausted_notification_is_kept_rather_than_deleted(self):
        record = self.store.notify(event("action"), at=NOON)
        for _ in range(live.MAX_DELIVERY_ATTEMPTS):
            self.store.mark_failed(record["id"], "APNs 503", at=NOON)
        self.assertEqual(len(self.store.state["notifications"]), 1)

    def test_the_queue_holds_queued_and_retryable_failures(self):
        first = self.store.notify(event("action", event_id="e-1"), at=NOON)
        second = self.store.notify(event("action", event_id="e-2"), at=NOON)
        self.store.mark_failed(second["id"], "transient", at=NOON)
        self.store.mark_delivered(first["id"], at=NOON)
        queued_ids = {record["id"] for record in self.store.queued()}
        self.assertEqual(queued_ids, {second["id"]})

    def test_marking_an_unknown_notification_is_an_error(self):
        with self.assertRaises(ev.EventError):
            self.store.mark_read("NTF-nope")

    def test_a_projection_run_creates_records_only_for_events_that_earn_them(self):
        events = [event("info", event_id="e-1"), event("update", event_id="e-2"),
                  event("action", event_id="e-3")]
        result = self.store.project_notifications(events)
        self.assertEqual(result["created"], 2)
        self.assertEqual(result["no_channel"], 1)
        self.assertEqual(result["existing"], 0)

    def test_rerunning_the_projection_does_not_double_anything(self):
        events = [event("action", event_id="e-1"), event("update", event_id="e-2")]
        self.store.project_notifications(events)
        again = self.store.project_notifications(events)
        self.assertEqual(again["created"], 0)
        self.assertEqual(again["existing"], 2)
        self.assertEqual(self.store.badge_count(), 2)


class BadgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = live.LiveStore(Path(self.tmp.name) / "live.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_the_badge_counts_obligations_not_activity(self):
        # Twenty information events, which is a busy hour and no obligation.
        for n in range(20):
            self.store.notify(event("info", event_id=f"i-{n}"), at=NOON)
        self.assertEqual(self.store.badge_count(), 0)

    def test_the_badge_counts_unread_actionable_notifications(self):
        self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.notify(event("update", event_id="u-1"), at=NOON)
        self.assertEqual(self.store.badge_count(), 2)

    def test_reading_a_notification_lowers_the_badge(self):
        record = self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.mark_read(record["id"], at=NOON)
        self.assertEqual(self.store.badge_count(), 0)

    def test_dismissing_a_notification_lowers_the_badge(self):
        record = self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.dismiss(record["id"], at=NOON)
        self.assertEqual(self.store.badge_count(), 0)

    def test_delivery_does_not_lower_the_badge_because_delivery_is_not_reading(self):
        record = self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.mark_delivered(record["id"], at=NOON)
        self.assertEqual(self.store.badge_count(), 1)

    def test_a_failed_push_still_counts_because_the_obligation_remains(self):
        record = self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.mark_failed(record["id"], "APNs 503", at=NOON)
        self.assertEqual(self.store.badge_count(), 1)

    def test_synchronizing_reports_one_number_every_device_should_show(self):
        self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.notify(event("update", event_id="u-1"), at=NOON)
        synced = self.store.synchronize_badge(at=NOON)
        self.assertEqual(synced["badge"], 2)
        self.assertEqual(synced["unread_push"], 1)
        self.assertEqual(synced["by_state"]["queued"], 2)

    def test_opening_the_app_does_not_mark_anything_read(self):
        self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.synchronize_badge(at=NOON)
        self.assertEqual(self.store.badge_count(), 1)

    def test_the_badge_is_consistent_across_a_reload(self):
        self.store.notify(event("action", event_id="a-1"), at=NOON)
        self.store.save()
        self.assertEqual(live.LiveStore(self.store.path).badge_count(), 1)


class DeviceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = live.LiveStore(Path(self.tmp.name) / "live.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_a_raw_device_token_is_never_stored(self):
        self.store.register_device("iphone", platform="ios", token="apns-raw-token", at=NOON)
        self.store.save()
        stored = self.store.path.read_text(encoding="utf-8")
        self.assertNotIn("apns-raw-token", stored)

    def test_the_public_read_model_exposes_no_fingerprint_either(self):
        self.store.register_device("iphone", platform="ios", token="apns-raw-token", at=NOON)
        for device in self.store.devices_view():
            self.assertNotIn("token_fingerprint", device)
            self.assertNotIn("token", device)

    def test_registering_the_same_device_twice_replaces_rather_than_duplicates(self):
        self.store.register_device("iphone", platform="ios", token="one", at=NOON)
        self.store.register_device("iphone", platform="ios", token="two", at=NOON)
        self.assertEqual(len(self.store.devices_view()), 1)

    def test_a_registration_without_a_token_is_refused(self):
        with self.assertRaises(ev.EventError):
            self.store.register_device("iphone", platform="ios", token="")


class SubscriptionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = live.LiveStore(Path(self.tmp.name) / "live.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_a_subscription_records_its_constraints(self):
        record = self.store.set_subscription("SUB-eng", channels=["feed", "badge"],
                                             source="github", department="ENGINEERING",
                                             min_severity="update")
        self.assertEqual(record["channels"], ["feed", "badge"])
        self.assertEqual(record["min_severity"], "update")

    def test_an_unknown_channel_is_refused(self):
        with self.assertRaises(ev.EventError):
            self.store.set_subscription("SUB-x", channels=["telepathy"])

    def test_an_unknown_severity_floor_is_refused(self):
        with self.assertRaises(ev.EventError):
            self.store.set_subscription("SUB-x", channels=["feed"], min_severity="whenever")

    def test_a_subscription_is_replaced_by_id_not_duplicated(self):
        self.store.set_subscription("SUB-x", channels=["feed"])
        self.store.set_subscription("SUB-x", channels=["feed", "push"])
        self.assertEqual(len(self.store.subscriptions()), 1)

    def test_stored_subscriptions_are_applied_by_notify(self):
        self.store.set_subscription("SUB-quiet", channels=["feed", "badge"], source="github")
        record = self.store.notify(event("action"), at=NOON)
        self.assertNotIn("push", record["channels"])


class DegradedModeTests(unittest.TestCase):
    def test_with_no_transport_the_layer_says_unconfigured_not_live(self):
        status = live.realtime_status(NOON, realtime_configured=False, now=NOON)
        self.assertEqual(status["mode"], "unconfigured")
        self.assertFalse(status["presence_trustworthy"])

    def test_canonical_knowledge_is_readable_in_every_mode(self):
        for configured, last in ((False, None), (True, None), (True, NOON)):
            with self.subTest(configured=configured):
                status = live.realtime_status(last, realtime_configured=configured, now=NOON)
                self.assertTrue(status["canonical_readable"])

    def test_a_configured_transport_that_has_never_spoken_is_stale(self):
        status = live.realtime_status(None, realtime_configured=True, now=NOON)
        self.assertEqual(status["mode"], "stale")

    def test_silence_past_the_window_is_stale_and_says_how_long(self):
        status = live.realtime_status("2026-09-29T11:00:00+00:00",
                                     realtime_configured=True, now=NOON)
        self.assertEqual(status["mode"], "stale")
        self.assertEqual(status["last_event_age_seconds"], 3600)

    def test_a_recent_event_on_a_configured_transport_is_live(self):
        status = live.realtime_status("2026-09-29T11:59:00+00:00",
                                     realtime_configured=True, now=NOON)
        self.assertEqual(status["mode"], "live")
        self.assertTrue(status["presence_trustworthy"])

    def test_presence_is_only_trustworthy_when_the_transport_is_live(self):
        for mode_inputs in ((None, False), (None, True), ("2026-09-29T10:00:00+00:00", True)):
            last, configured = mode_inputs
            with self.subTest(last=last, configured=configured):
                status = live.realtime_status(last, realtime_configured=configured, now=NOON)
                self.assertFalse(status["presence_trustworthy"])


class ComposedViewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.ledger = ev.EventLedger(self.dir / "ledger.jsonl")
        self.store = live.LiveStore(self.dir / "live.json")
        self.registry = ad.AdapterRegistry(self.dir / "registry.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_an_empty_system_produces_a_complete_honest_view(self):
        view = live.build_live_view(self.ledger, self.store, self.registry, now=NOON)
        for section in ("realtime", "activity", "presence", "notifications",
                        "badge", "integrations", "devices", "subscriptions"):
            self.assertIn(section, view)
        self.assertEqual(view["mode"], "read_only")
        self.assertEqual(view["realtime"]["mode"], "unconfigured")
        self.assertEqual(view["badge"]["badge"], 0)

    def test_the_view_names_where_canonical_truth_actually_lives(self):
        view = live.build_live_view(self.ledger, self.store, self.registry, now=NOON)
        self.assertEqual(view["canonical_sources"]["know"], "obsidian_markdown")
        self.assertIn("founder-state.json", view["canonical_sources"]["operate"])

    def test_the_view_never_reports_a_planned_adapter_as_connected(self):
        view = live.build_live_view(self.ledger, self.store, self.registry, now=NOON)
        for row in view["integrations"]["adapters"]:
            if row["declared_status"] in ("planned", "blocked"):
                self.assertFalse(row["connected"])

    def test_the_whole_lifecycle_runs_end_to_end(self):
        """External activity → event → dedup → projection → notification → badge.

        The Definition of Done for this phase, as one executable assertion.
        """
        delivery = {
            "provider": "github", "kind": "pull_request", "origin": "webhook",
            "delivery_id": "d-1", "received_at": NOON,
            "payload": {
                "action": "review_requested",
                "repository": {"full_name": "OmSadhiGuru/ALPHA.PROXIMA.CORE-"},
                "sender": {"login": "codex-bot"},
                "pull_request": {"number": 48, "title": "Memory navigation",
                                 "state": "open", "updated_at": "2026-09-29T11:59:00Z",
                                 "head": {"ref": "codex/x"}},
            },
        }
        first = self.registry.ingest(delivery, self.ledger)
        self.assertEqual(first["stored"], 1)

        # The retry a provider will certainly send changes nothing.
        retry = self.registry.ingest(dict(delivery, delivery_id="d-2"), self.ledger)
        self.assertEqual(retry["stored"], 0)

        self.store.project_notifications(self.ledger.events())
        self.store.set_presence("CODEX", "coding", activity="PR-48", at=NOON)

        view = live.build_live_view(self.ledger, self.store, self.registry, now=NOON)
        self.assertEqual(view["activity"]["counts"]["total"], 1)
        self.assertEqual(view["activity"]["counts"]["requires_founder"], 1)
        self.assertEqual(view["badge"]["badge"], 1)
        self.assertEqual(view["badge"]["unread_push"], 1)

        notification = view["notifications"]["notifications"][0]
        self.assertIn("push", notification["channels"])
        # The Founder opens the notification and lands on the right context.
        self.assertEqual(notification["deep_link"], "alpha-proxima://github/pr/48")
        self.assertEqual(notification["web_link"], "#github/pr/48")

        # And the whole history of that entity is navigable.
        history = live.build_entity_history(self.ledger.events(), "PR-48")
        self.assertEqual(history["counts"]["events"], 1)
        self.assertEqual(history["actors"], ["codex-bot"])

    def test_a_corrupt_live_store_degrades_rather_than_crashing(self):
        self.store.path.parent.mkdir(parents=True, exist_ok=True)
        self.store.path.write_text("{not json", encoding="utf-8")
        fresh = live.LiveStore(self.store.path)
        self.assertEqual(fresh.badge_count(), 0)
        self.assertEqual(fresh.presence_view(now=NOON)["presence"], [])


class CommandLineTests(unittest.TestCase):
    """The CLI surface, including the one place a real credential is handled."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.state = Path(self.tmp.name) / "live.json"
        self.ledger = Path(self.tmp.name) / "ledger.jsonl"
        self.registry = Path(self.tmp.name) / "registry.json"

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *args) -> tuple[int, str, str]:
        import contextlib
        import io
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = live.main(["--live-state", str(self.state), "--ledger", str(self.ledger),
                              "--registry", str(self.registry), *args])
        return code, out.getvalue(), err.getvalue()

    def test_registering_a_device_refuses_without_the_token_in_the_environment(self):
        import os
        with patch.dict(os.environ, {}, clear=True):
            code, _, err = self.run_cli("register-device", "iphone", "--platform", "ios")
        self.assertEqual(code, 1)
        # The reason matters: it is why the token is not simply an argument.
        self.assertIn("process list", err)

    def test_a_device_token_never_reaches_the_command_line_or_the_output(self):
        import os
        token = "an-apns-token-that-must-not-appear"
        with patch.dict(os.environ, {"ALPHA_DEVICE_TOKEN": token}):
            code, out, _ = self.run_cli("register-device", "iphone", "--platform", "ios")
        self.assertEqual(code, 0)
        self.assertNotIn(token, out)
        # Nor the fingerprint: confirming a registration does not require echoing
        # a stable identifier for the Founder's physical device.
        self.assertNotIn("token_fingerprint", out)
        self.assertNotIn(token, self.state.read_text(encoding="utf-8"))

    def test_a_subscription_can_be_set_and_read_back(self):
        code, _, _ = self.run_cli("subscribe", "SUB-eng", "--channel", "feed",
                                  "--channel", "badge", "--source", "github")
        self.assertEqual(code, 0)
        code, out, _ = self.run_cli("subscriptions")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)[0]["channels"], ["feed", "badge"])

    def test_a_stored_subscription_then_withholds_a_push(self):
        self.run_cli("subscribe", "SUB-quiet", "--channel", "feed", "--channel", "badge",
                     "--source", "github")
        store = live.LiveStore(self.state)
        record = store.notify(event("action"), at=NOON)
        self.assertNotIn("push", record["channels"])

    def test_the_queue_says_plainly_that_nothing_can_send(self):
        store = live.LiveStore(self.state)
        store.notify(event("action"), at=NOON)
        store.save()
        code, out, _ = self.run_cli("queue")
        self.assertEqual(code, 0)
        # Honest about the gap rather than implying a delivery attempt happened.
        self.assertIn("No push credential exists", out)

    def test_the_devices_view_from_the_cli_exposes_no_identifier_for_the_device(self):
        import os
        with patch.dict(os.environ, {"ALPHA_DEVICE_TOKEN": "t"}):
            self.run_cli("register-device", "iphone", "--platform", "ios")
        code, out, _ = self.run_cli("devices")
        self.assertEqual(code, 0)
        self.assertNotIn("fingerprint", out)

    def test_an_unknown_channel_is_refused_by_the_parser(self):
        with self.assertRaises(SystemExit):
            self.run_cli("subscribe", "SUB-x", "--channel", "telepathy")

    def test_status_reports_without_a_ledger_present(self):
        # The layer must be inspectable on a machine where nothing has happened.
        code, out, _ = self.run_cli("status")
        self.assertEqual(code, 0)
        self.assertIn("canonical", out)
        self.assertIn("readable", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
