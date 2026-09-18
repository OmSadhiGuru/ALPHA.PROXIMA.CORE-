"""Tests for the Minimum Viable Council session kernel."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import council_kernel as ck  # noqa: E402

class CouncilKernelTests(unittest.TestCase):
    def open(self, state, cls="III", ethics="none"):
        return ck.open_session(state, "Test bounded implementation", cls, "IAI §3", "AGT-007", ethics)

    def test_same_day_sessions_survive_save_and_reload(self):
        state = ck.empty_state()
        first = self.open(state)
        second = self.open(state)
        self.assertNotEqual(first['session_id'], second['session_id'])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'council-state.json'
            ck.save(state, path)
            restored = ck.load(path)
            third = self.open(restored)
            self.assertNotIn(third['session_id'], [first['session_id'], second['session_id']])
            ck.validate_state(restored)

    def test_session_serial_continues_after_three_digits(self):
        state = ck.empty_state()
        first = self.open(state)
        first['session_id'] = first['session_id'].rsplit('-', 1)[0] + '-1000'
        self.assertTrue(self.open(state)['session_id'].endswith('-1001'))

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

    def test_require_role_derives_from_the_registry_not_hardcoded_sets(self):
        """The old AVAILABLE/ADVISORY_ONLY/BLOCKED module constants are gone."""
        for name in ("AVAILABLE", "ADVISORY_ONLY", "BLOCKED"):
            self.assertFalse(hasattr(ck, name))
        ck.require_role("AGT-001")  # available, must not raise
        with self.assertRaises(ck.StateError):
            ck.require_role("AGT-011")  # blocked


def _completed(stdout: str = "", returncode: int = 0, stderr: str = "") -> subprocess.CompletedProcess:
    return subprocess.CompletedProcess(args=["claude"], returncode=returncode, stdout=stdout, stderr=stderr)


class ExecuteAssignmentTests(unittest.TestCase):
    def setUp(self):
        self.state = ck.empty_state()
        self.item = ck.open_session(self.state, "Test bounded implementation", "III", "IAI §3", "AGT-007", "none")
        self.run = ck.assign(self.state, self.item["session_id"], "AGT-002", "Return a source packet", "subagent")

    def test_blocked_role_refuses_execution_before_any_subprocess_call(self):
        run = ck.assign(self.state, self.item["session_id"], "AGT-001", "x", "subagent")
        # AGT-015 is blocked; force the run's role to it directly for this check.
        run["role"] = "AGT-015"
        with patch("subprocess.run") as mock_run:
            with self.assertRaises(ck.ExecutionError):
                ck.execute_assignment(self.state, self.item["session_id"], run["id"], "prompt")
            mock_run.assert_not_called()

    def test_advisory_only_role_refuses_execution_before_any_subprocess_call(self):
        run = ck.assign(self.state, self.item["session_id"], "AGT-001", "x", "subagent")
        run["role"] = "AGT-010"
        with patch("subprocess.run") as mock_run:
            with self.assertRaises(ck.ExecutionError):
                ck.execute_assignment(self.state, self.item["session_id"], run["id"], "prompt")
            mock_run.assert_not_called()

    def test_claude_not_on_path_raises_execution_error(self):
        with patch("subprocess.run", side_effect=FileNotFoundError()):
            with self.assertRaisesRegex(ck.ExecutionError, "not found on PATH"):
                ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")

    def test_timeout_raises_execution_error(self):
        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="claude", timeout=120)):
            with self.assertRaisesRegex(ck.ExecutionError, "timed out"):
                ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")

    def test_non_zero_exit_raises_execution_error(self):
        with patch("subprocess.run", return_value=_completed(returncode=1, stderr="boom")):
            with self.assertRaisesRegex(ck.ExecutionError, "exited 1"):
                ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")

    def test_marks_executing_during_the_call(self):
        seen = {}
        def fake_run(args, **kwargs):
            seen["status"] = self.run["status"]
            seen["has_timestamp"] = "executing_since" in self.run
            return _completed(stdout=json.dumps({"result": "ok"}))
        with patch("subprocess.run", side_effect=fake_run):
            ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")
        self.assertEqual(seen["status"], "executing")
        self.assertTrue(seen["has_timestamp"])
        # Cleared again once the call completes.
        self.assertNotIn("executing_since", self.run)

    def test_executing_status_is_saved_to_disk_before_the_subprocess_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            ck.save(self.state, path)
            seen = {}
            def fake_run(args, **kwargs):
                seen["on_disk_status"] = ck.load(path)["sessions"][0]["assignments"][0]["status"]
                return _completed(stdout=json.dumps({"result": "ok"}))
            with patch("subprocess.run", side_effect=fake_run):
                ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt",
                                      state_path=path)
        self.assertEqual(seen["on_disk_status"], "executing")

    def test_failed_execution_reverts_status_to_assigned_not_stuck_executing(self):
        with patch("subprocess.run", return_value=_completed(returncode=1, stderr="boom")):
            with self.assertRaises(ck.ExecutionError):
                ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")
        self.assertEqual(self.run["status"], "assigned")
        self.assertNotIn("executing_since", self.run)

    def test_empty_output_raises_execution_error(self):
        with patch("subprocess.run", return_value=_completed(stdout=json.dumps({"result": "  "}))):
            with self.assertRaisesRegex(ck.ExecutionError, "no usable result"):
                ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")

    def test_successful_run_records_output_via_the_single_writer(self):
        payload = json.dumps({"result": "Two sources; one unknown."})
        with patch("subprocess.run", return_value=_completed(stdout=payload)):
            result = ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["output"], "Two sources; one unknown.")
        self.assertEqual(self.run["output"], "Two sources; one unknown.")

    def test_falls_back_to_ndjson_result_event(self):
        stream = "\n".join([
            json.dumps({"type": "system", "subtype": "init"}),
            json.dumps({"type": "assistant", "message": {"content": []}}),
            json.dumps({"type": "result", "result": "Fallback text."}),
        ])
        with patch("subprocess.run", return_value=_completed(stdout=stream)):
            result = ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")
        self.assertEqual(result["output"], "Fallback text.")

    def test_runs_in_an_empty_temporary_directory(self):
        captured = {}
        def fake_run(args, **kwargs):
            cwd = kwargs.get("cwd")
            captured["cwd"] = cwd
            captured["existed"] = cwd is not None and Path(cwd).is_dir()
            captured["contents"] = list(Path(cwd).iterdir()) if cwd else None
            return _completed(stdout=json.dumps({"result": "ok"}))
        with patch("subprocess.run", side_effect=fake_run):
            ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")
        self.assertIsNotNone(captured["cwd"])
        self.assertTrue(captured["existed"])
        self.assertEqual(captured["contents"], [])

    def test_strips_claudecode_env_var(self):
        import os
        captured = {}
        def fake_run(args, **kwargs):
            captured["env"] = kwargs.get("env")
            return _completed(stdout=json.dumps({"result": "ok"}))
        with patch.dict(os.environ, {"CLAUDECODE": "1"}):
            with patch("subprocess.run", side_effect=fake_run):
                ck.execute_assignment(self.state, self.item["session_id"], self.run["id"], "prompt")
        self.assertNotIn("CLAUDECODE", captured["env"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
