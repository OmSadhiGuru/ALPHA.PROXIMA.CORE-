#!/usr/bin/env python3
"""Tests for the Founder OS state engine.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_founder_os.py"
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import founder_os as fos  # noqa: E402


def seeded() -> dict:
    state = fos.empty_state()
    fos.set_mission(state, "Ship the Founder Console vertical slice", sprint_id="RBT-001")
    fos.add_priority(state, "Land Console V1", why="One cockpit", owner="CODEX")
    state["agents"].append({
        "id": "AGT-001", "name": "LUMIAION", "role": "Orchestration",
        "status": "active", "authority": "Class III/IV within scope",
    })
    return state


class TestStateLifecycle(unittest.TestCase):
    def test_empty_state_validates(self):
        self.assertEqual(fos.validate_state(fos.empty_state()), [])

    def test_round_trip_through_disk(self):
        state = seeded()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "founder-state.json"
            fos.save_state(state, path)
            reloaded = fos.load_state(path)
        self.assertEqual(reloaded["daily_mission"]["mission"], state["daily_mission"]["mission"])
        self.assertEqual(len(reloaded["priorities"]), 1)

    def test_load_missing_file_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(fos.StateError):
                fos.load_state(Path(tmp) / "absent.json")

    def test_unsupported_schema_version_rejected(self):
        state = fos.empty_state()
        state["schema_version"] = "0.0.1"
        with self.assertRaises(fos.StateError):
            fos.validate_state(state)

    def test_duplicate_ids_rejected(self):
        state = fos.empty_state()
        record = {"id": "PRI-001", "rank": 1, "title": "a", "why": "b",
                  "owner": "CODEX", "status": "open"}
        state["priorities"] = [record, dict(record)]
        with self.assertRaises(fos.StateError):
            fos.validate_state(state)

    def test_missing_provenance_field_rejected(self):
        state = fos.empty_state()
        state["tasks"] = [{"id": "TSK-001", "title": "x", "owner": "CODEX", "state": "assigned"}]
        with self.assertRaisesRegex(fos.StateError, "requested_by"):
            fos.validate_state(state)


class TestMission(unittest.TestCase):
    def test_set_mission_records_provenance(self):
        state = fos.empty_state()
        record = fos.set_mission(state, "  Restore routing coherence  ", set_by="founder")
        self.assertEqual(record["mission"], "Restore routing coherence")
        self.assertEqual(record["set_by"], "founder")
        self.assertEqual(record["date"], fos.today_iso())
        self.assertTrue(record["set_at"])

    def test_empty_mission_rejected(self):
        with self.assertRaises(fos.StateError):
            fos.set_mission(fos.empty_state(), "   ")

    def test_mission_from_another_day_is_stale(self):
        state = fos.empty_state()
        fos.set_mission(state, "Yesterday's mission", on_date="2020-01-01")
        self.assertTrue(fos.build_view(state)["mission_is_stale"])

    def test_today_mission_is_not_stale(self):
        state = fos.empty_state()
        fos.set_mission(state, "Today's mission")
        self.assertFalse(fos.build_view(state)["mission_is_stale"])


class TestPriorities(unittest.TestCase):
    def _fill(self, state):
        for i in range(fos.MAX_PRIORITIES):
            fos.add_priority(state, f"P{i}", why="w", owner="CODEX")

    def test_ranks_are_sequential(self):
        state = fos.empty_state()
        self._fill(state)
        self.assertEqual([p["rank"] for p in fos.open_priorities(state)], [1, 2, 3])

    def test_fourth_priority_rejected(self):
        state = fos.empty_state()
        self._fill(state)
        with self.assertRaisesRegex(fos.StateError, "Top 3 is full"):
            fos.add_priority(state, "P4", why="w", owner="CODEX")

    def test_completing_one_frees_a_slot_and_renumbers(self):
        state = fos.empty_state()
        self._fill(state)
        fos.set_priority_status(state, "PRI-001", "done")
        self.assertEqual([p["rank"] for p in fos.open_priorities(state)], [1, 2])
        fos.add_priority(state, "P4", why="w", owner="CODEX")
        self.assertEqual(len(fos.open_priorities(state)), 3)

    def test_ids_increment_without_reuse(self):
        state = fos.empty_state()
        self._fill(state)
        fos.set_priority_status(state, "PRI-001", "done")
        self.assertEqual(fos.add_priority(state, "P4", why="w", owner="CODEX")["id"], "PRI-004")

    def test_unknown_priority_id_raises(self):
        with self.assertRaises(fos.StateError):
            fos.set_priority_status(fos.empty_state(), "PRI-999", "done")


class TestNextAction(unittest.TestCase):
    def test_next_action_links_to_priority(self):
        state = seeded()
        record = fos.set_next_action(state, "Write the schema", owner="CODEX", priority_id="PRI-001")
        self.assertEqual(record["priority_id"], "PRI-001")
        self.assertEqual(fos.validate_state(state), [])

    def test_next_action_with_unknown_priority_rejected(self):
        with self.assertRaises(fos.StateError):
            fos.set_next_action(fos.empty_state(), "x", owner="CODEX", priority_id="PRI-404")

    def test_closing_the_linked_priority_clears_the_next_action(self):
        state = seeded()
        fos.set_next_action(state, "Write the schema", owner="CODEX", priority_id="PRI-001")
        fos.set_priority_status(state, "PRI-001", "done")
        self.assertIsNone(state["next_action"])

    def test_dangling_next_action_fails_validation(self):
        state = seeded()
        fos.set_next_action(state, "x", owner="CODEX", priority_id="PRI-001")
        state["priorities"] = []
        with self.assertRaises(fos.StateError):
            fos.validate_state(state)


class TestDecisions(unittest.TestCase):
    def test_decision_lifecycle(self):
        state = fos.empty_state()
        record = fos.add_decision(
            state, "Adopt vault-native state", context="c",
            recommendation="Adopt", options=["Adopt", "Add a database"],
            consequence_of_delay="Console cannot persist",
        )
        self.assertEqual(record["status"], "open")
        self.assertEqual(len(fos.open_decisions(state)), 1)
        fos.resolve_decision(state, record["id"], "approved", note="ok")
        self.assertEqual(fos.open_decisions(state), [])
        self.assertTrue(state["decisions"][0]["decided_at"])

    def test_invalid_resolution_rejected(self):
        state = fos.empty_state()
        d = fos.add_decision(state, "t", context="c", recommendation="r",
                             options=["a"], consequence_of_delay="x")
        with self.assertRaises(fos.StateError):
            fos.resolve_decision(state, d["id"], "maybe")


class TestTasksAgentsBlockers(unittest.TestCase):
    def test_task_state_machine_accepts_every_documented_state(self):
        state = fos.empty_state()
        task = fos.add_task(state, "t", owner="CODEX", why="w", requested_by="founder")
        self.assertEqual(task["state"], "assigned")
        for value in fos.TASK_STATES:
            self.assertEqual(fos.set_task_state(state, task["id"], value)["state"], value)

    def test_invalid_task_state_rejected(self):
        state = fos.empty_state()
        task = fos.add_task(state, "t", owner="CODEX", why="w", requested_by="founder")
        with self.assertRaises(fos.StateError):
            fos.set_task_state(state, task["id"], "almost-done")

    def test_completed_tasks_leave_the_execution_view(self):
        state = fos.empty_state()
        task = fos.add_task(state, "t", owner="CODEX", why="w", requested_by="founder")
        fos.set_task_state(state, task["id"], "complete", output_ref="[[Result]]")
        self.assertEqual(fos.active_tasks(state), [])
        self.assertEqual(state["tasks"][0]["output_ref"], "[[Result]]")

    def test_agent_status_transitions(self):
        state = seeded()
        self.assertEqual(fos.set_agent_status(state, "AGT-001", "working")["status"], "working")
        with self.assertRaises(fos.StateError):
            fos.set_agent_status(state, "AGT-001", "vibing")

    def test_blocker_lifecycle_and_founder_count(self):
        state = fos.empty_state()
        task = fos.add_task(state, "t", owner="CODEX", why="w", requested_by="founder")
        blocker = fos.add_blocker(state, "No credentials", impact="i", owner="founder",
                                  needs_founder=True, blocking_ids=[task["id"]])
        self.assertEqual(fos.build_view(state)["counts"]["founder_blockers"], 1)
        self.assertEqual(fos.validate_state(state), [])
        fos.resolve_blocker(state, blocker["id"], note="granted")
        self.assertEqual(fos.open_blockers(state), [])

    def test_blocker_pointing_at_unknown_work_is_noted_not_fatal(self):
        state = fos.empty_state()
        fos.add_blocker(state, "b", impact="i", owner="o", blocking_ids=["TSK-404"])
        self.assertEqual(len(fos.validate_state(state)), 1)


class TestRendering(unittest.TestCase):
    def test_console_embeds_the_mission(self):
        state = seeded()
        html = fos.render_console(state, fos.DEFAULT_TEMPLATE)
        self.assertNotIn(fos.STATE_PLACEHOLDER, html)
        self.assertIn("Ship the Founder Console vertical slice", html)
        self.assertIn("LUMIAION", html)

    def test_console_escapes_a_script_terminator_in_state(self):
        state = seeded()
        fos.set_mission(state, "danger </script><b>x</b>")
        html = fos.render_console(state, fos.DEFAULT_TEMPLATE)
        self.assertNotIn("</script><b>", html)
        self.assertIn("<\\/script>", html)

    def test_console_survives_a_missing_placeholder(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "t.html"
            bad.write_text("<html></html>")
            with self.assertRaises(fos.StateError):
                fos.render_console(seeded(), bad)

    def test_mirror_has_frontmatter_and_the_four_questions(self):
        md = fos.render_mirror(seeded())
        self.assertTrue(md.startswith("---\n"))
        self.assertIn('artifact_type: operations-dashboard', md)
        for heading in ("## Today", "### Top 3 Priorities", "### Next Action",
                        "## Decisions Requiring Founder", "## Execution",
                        "## Agents / Systems", "## Blockers", "## System Health"):
            self.assertIn(heading, md)

    def test_render_all_writes_both_artifacts(self):
        state = seeded()
        with tempfile.TemporaryDirectory() as tmp:
            console = Path(tmp) / "console.html"
            mirror = Path(tmp) / "Founder Console.md"
            fos.render_all(state, fos.DEFAULT_TEMPLATE, console, mirror)
            self.assertIn("Founder Console", console.read_text())
            self.assertIn("Founder Console", mirror.read_text())


class TestView(unittest.TestCase):
    def test_view_answers_the_four_questions(self):
        view = fos.build_view(seeded())
        for key in ("mission", "priorities", "next_action", "decisions",
                    "tasks", "blockers", "agents", "counts"):
            self.assertIn(key, view)

    def test_summary_is_terminal_safe(self):
        text = fos.summarize(seeded())
        self.assertIn("FOUNDER CONSOLE", text)
        self.assertIn("NEXT ACTION", text)


class TestCli(unittest.TestCase):
    def _run(self, tmp, *argv):
        return fos.main([
            "--state", str(Path(tmp) / "founder-state.json"),
            "--template", str(fos.DEFAULT_TEMPLATE),
            "--console", str(Path(tmp) / "console.html"),
            "--mirror", str(Path(tmp) / "mirror.md"),
            *argv,
        ])

    def test_end_to_end_vertical_slice(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "founder-state.json"
            self.assertEqual(self._run(tmp, "init"), 0)
            self.assertEqual(self._run(tmp, "mission", "Close RBT-001"), 0)
            self.assertEqual(self._run(tmp, "priority-add", "Land Console V1",
                                       "--why", "One cockpit", "--owner", "CODEX"), 0)
            self.assertEqual(self._run(tmp, "next-action", "Seed real state",
                                       "--owner", "CODEX", "--priority", "PRI-001"), 0)
            stored = json.loads(state_path.read_text())
            self.assertEqual(stored["daily_mission"]["mission"], "Close RBT-001")
            self.assertEqual(stored["next_action"]["priority_id"], "PRI-001")
            # Mutating commands re-render both artifacts automatically.
            self.assertIn("Close RBT-001", (Path(tmp) / "console.html").read_text())
            self.assertIn("Close RBT-001", (Path(tmp) / "mirror.md").read_text())
            self.assertEqual(self._run(tmp, "check"), 0)

    def test_init_twice_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self._run(tmp, "init"), 0)
            self.assertEqual(self._run(tmp, "init"), 1)

    def test_every_mutating_subcommand_works_through_the_cli(self):
        """Regression: `task-state` once failed because its `state` positional
        shared an argparse dest with the global --state option, so the task
        state overwrote the state-file path. Drive every subcommand through
        main() so a dest collision cannot hide behind a direct function call."""
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "founder-state.json"
            self.assertEqual(self._run(tmp, "init"), 0)
            self.assertEqual(self._run(tmp, "mission", "M"), 0)
            self.assertEqual(self._run(tmp, "priority-add", "P", "--why", "w",
                                       "--owner", "CODEX"), 0)
            self.assertEqual(self._run(tmp, "next-action", "N", "--owner", "CODEX"), 0)
            self.assertEqual(self._run(tmp, "task-add", "T", "--owner", "CODEX",
                                       "--why", "w", "--by", "founder"), 0)
            self.assertEqual(self._run(tmp, "task-state", "TSK-001", "working"), 0)
            self.assertEqual(self._run(tmp, "task-state", "TSK-001", "complete",
                                       "--output", "[[Out]]"), 0)
            self.assertEqual(self._run(tmp, "decision-add", "D", "--context", "c",
                                       "--recommendation", "r", "--option", "a",
                                       "--consequence", "x"), 0)
            self.assertEqual(self._run(tmp, "decision-resolve", "FD-001", "approved",
                                       "--note", "ok"), 0)
            self.assertEqual(self._run(tmp, "blocker-add", "B", "--impact", "i",
                                       "--owner", "o", "--needs-founder"), 0)
            self.assertEqual(self._run(tmp, "blocker-resolve", "BLK-001", "--note", "n"), 0)
            self.assertEqual(self._run(tmp, "priority-status", "PRI-001", "done"), 0)

            stored = json.loads(state_path.read_text())
            self.assertEqual(stored["tasks"][0]["state"], "complete")
            self.assertEqual(stored["tasks"][0]["output_ref"], "[[Out]]")
            self.assertEqual(stored["decisions"][0]["status"], "approved")
            self.assertEqual(stored["blockers"][0]["status"], "resolved")
            self.assertEqual(stored["priorities"][0]["status"], "done")

    def test_agent_status_works_through_the_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "founder-state.json"
            self._run(tmp, "init")
            state = fos.load_state(state_path)
            state["agents"].append({"id": "AGT-001", "name": "LUMIAION",
                                    "role": "Orchestration", "status": "idle",
                                    "authority": "Class III/IV"})
            fos.save_state(state, state_path)
            self.assertEqual(self._run(tmp, "agent-status", "AGT-001", "working"), 0)
            self.assertEqual(json.loads(state_path.read_text())["agents"][0]["status"],
                             "working")

    def test_no_subcommand_dest_shadows_a_global_option(self):
        """A subparser positional that reuses a global option's dest silently
        overwrites it. Assert the namespaces stay disjoint for every subcommand."""
        parser = fos.build_parser()
        global_dests = {a.dest for a in parser._actions if a.option_strings} - {"help"}
        subparsers = [a for a in parser._actions
                      if isinstance(a, argparse._SubParsersAction)][0]
        for name, sub in subparsers.choices.items():
            sub_dests = {a.dest for a in sub._actions if a.dest != "help"}
            collisions = sub_dests & global_dests
            self.assertFalse(collisions,
                             f"subcommand {name!r} reuses global dest(s): {collisions}")

    def test_bad_command_returns_nonzero_without_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._run(tmp, "init")
            self.assertEqual(self._run(tmp, "priority-status", "PRI-999", "done"), 1)


class TestShippedState(unittest.TestCase):
    """The state committed to the Vault must always be loadable and renderable."""

    def test_shipped_state_is_valid(self):
        if not fos.DEFAULT_STATE.exists():
            self.skipTest("no shipped state yet")
        state = fos.load_state(fos.DEFAULT_STATE)
        fos.render_console(state, fos.DEFAULT_TEMPLATE)
        fos.render_mirror(state)

    def test_shipped_integrations_declare_honest_status(self):
        if not fos.DEFAULT_STATE.exists():
            self.skipTest("no shipped state yet")
        state = fos.load_state(fos.DEFAULT_STATE)
        for integration in state["integrations"]:
            self.assertIn(integration["status"], fos.INTEGRATION_STATES)


if __name__ == "__main__":
    unittest.main(verbosity=2)
