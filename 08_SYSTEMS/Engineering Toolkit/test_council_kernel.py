"""Tests for the Minimum Viable Council session kernel."""
from __future__ import annotations
import tempfile
import unittest
from pathlib import Path
import council_kernel as ck

class CouncilKernelTests(unittest.TestCase):
    def open(self, state, cls="III", ethics="none"):
        return ck.open_session(state, "Test bounded implementation", cls, "IAI §3", "AGT-007", ethics)

    def test_lifecycle_and_packet(self):
        state = ck.empty_state(); item = self.open(state)
        run = ck.assign(state, item["session_id"], "AGT-002", "Return a source packet", "subagent")
        ck.record_output(state, item["session_id"], run["id"], "Two sources; one unknown.")
        ck.synthesize(state, item["session_id"], "Proceed with a bounded draft.", "Source quality remains provisional.")
        ck.decide(state, item["session_id"], "approve", "Founder", "AGT-007")
        self.assertEqual(item["state"], "executing")
        self.assertIn("Source quality remains provisional.", ck.render(item))

    def test_non_founder_cannot_decide(self):
        state = ck.empty_state(); item = self.open(state); ck.synthesize(state, item["session_id"], "r", None)
        with self.assertRaisesRegex(ck.StateError, "Only the Founder"):
            ck.decide(state, item["session_id"], "approve", "AGT-001", "AGT-007")

    def test_class_one_requires_ratification(self):
        state = ck.empty_state(); item = self.open(state, "I"); ck.synthesize(state, item["session_id"], "r", None)
        with self.assertRaisesRegex(ck.StateError, "require explicit ratify"):
            ck.decide(state, item["session_id"], "approve", "founder", None)

    def test_blocked_and_advisory_roles_cannot_own(self):
        for role in ("AGT-010", "AGT-011", "AGT-015", "AGT-016"):
            with self.assertRaises(ck.StateError):
                ck.open_session(ck.empty_state(), "x", "III", "IAI", role, "none")

    def test_formal_ethics_trigger_stops_work(self):
        state = ck.empty_state(); item = self.open(state, ethics="formal-review-required")
        self.assertEqual(item["state"], "blocked")
        with self.assertRaises(ck.StateError): ck.assign(state, item["session_id"], "AGT-002", "x")

    def test_round_trip(self):
        state = ck.empty_state(); self.open(state)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "state.json"; ck.save(state, path)
            self.assertEqual(len(ck.load(path)["sessions"]), 1)

    def test_dashboard_is_read_only_and_names_next_action(self):
        state = ck.empty_state(); self.open(state)
        view = ck.build_view(state)
        self.assertEqual(view["counts"]["active"], 1)
        dashboard = ck.render_dashboard(state)
        self.assertIn("Council Console", dashboard)
        self.assertIn("Test bounded implementation", dashboard)
