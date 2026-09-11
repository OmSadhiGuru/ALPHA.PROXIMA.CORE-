#!/usr/bin/env python3
"""Tests for the 3D office spatial view.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_office_spatial.py"
"""

from __future__ import annotations

import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import office_spatial as office  # noqa: E402
import council_kernel as ck  # noqa: E402


TEMPLATE = "<html><body><script>var V=" + office.VIEW_PLACEHOLDER + ";</script></body></html>"


def council_state_with_one_assignment(tmp: str) -> Path:
    state = ck.empty_state()
    item = ck.open_session(state, "Test intent", "III", "IAI §3", "AGT-007", "none")
    ck.assign(state, item["session_id"], "AGT-002", "Return a source packet", "subagent")
    path = Path(tmp) / "council-state.json"
    ck.save(state, path)
    return path


class TestBuildOfficeView(unittest.TestCase):
    def test_composes_registry_and_council(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = council_state_with_one_assignment(tmp)
            view = office.build_office_view(office.VAULT_ROOT, state_path)
        self.assertEqual(len(view["desks"]), 16)
        ids = {d["id"] for d in view["registry"]["roles"]}
        for desk in view["desks"]:
            self.assertIn(desk["id"], ids)

    def test_active_assignment_surfaces_on_the_right_desk(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = council_state_with_one_assignment(tmp)
            view = office.build_office_view(office.VAULT_ROOT, state_path)
        desk = next(d for d in view["desks"] if d["id"] == "AGT-002")
        self.assertIsNotNone(desk["active_assignment"])
        self.assertEqual(desk["active_assignment"]["status"], "assigned")
        other = next(d for d in view["desks"] if d["id"] == "AGT-003")
        self.assertIsNone(other["active_assignment"])


class TestRenderer(unittest.TestCase):
    def test_render_inlines_the_view(self):
        with tempfile.TemporaryDirectory() as tmp:
            template_path = Path(tmp) / "office.template.html"
            template_path.write_text(TEMPLATE, encoding="utf-8")
            html = office.render_app({"today": "2026-09-10"}, template_path)
        self.assertIn('"today":"2026-09-10"', html)

    def test_render_escapes_closing_script_tags(self):
        with tempfile.TemporaryDirectory() as tmp:
            template_path = Path(tmp) / "office.template.html"
            template_path.write_text(TEMPLATE, encoding="utf-8")
            html = office.render_app({"x": "</script><script>alert(1)"}, template_path)
        self.assertNotIn("</script><script>alert(1)", html)

    def test_missing_template_raises(self):
        with self.assertRaises(office.OfficeError):
            office.render_app({}, Path("/nonexistent/office.template.html"))

    def test_template_without_placeholder_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            template_path = Path(tmp) / "office.template.html"
            template_path.write_text("<html></html>", encoding="utf-8")
            with self.assertRaises(office.OfficeError):
                office.render_app({}, template_path)


class TestNeverWrites(unittest.TestCase):
    def test_office_never_writes_council_state(self):
        source = Path(office.__file__).read_text(encoding="utf-8")
        for forbidden in ("council_kernel.save(", "record_output(", "execute_assignment(", "ck.assign("):
            self.assertNotIn(forbidden, source)

    def test_no_post_endpoint_exists(self):
        source = Path(office.__file__).read_text(encoding="utf-8")
        self.assertNotIn("do_POST", source)


class TestReusesReachabilityGate(unittest.TestCase):
    def test_imports_rather_than_reimplements_the_gate(self):
        source = Path(office.__file__).read_text(encoding="utf-8")
        self.assertIn('_load_sibling("alpha_app.py"', source)
        self.assertIn("check_reachability_gate = alpha_app.check_reachability_gate", source)
        self.assertNotIn("def check_reachability_gate", source)

    def test_refuses_non_loopback_without_token(self):
        with self.assertRaises(Exception):
            office.check_reachability_gate("0.0.0.0", 8789, None)

    def test_loopback_needs_no_token(self):
        office.check_reachability_gate("127.0.0.1", 8789, None)  # must not raise

    def test_cli_refuses_non_loopback_cleanly_not_with_a_traceback(self):
        exit_code = office.main(["serve", "--host", "0.0.0.0", "--port", "8799"])
        self.assertEqual(exit_code, 2)


class TestTemplate(unittest.TestCase):
    def test_pins_an_exact_three_js_version(self):
        text = office.DEFAULT_TEMPLATE.read_text(encoding="utf-8")
        match = re.search(r'three@([\w.\-]+)/build/three\.min\.js', text)
        self.assertIsNotNone(match, "no pinned three.js version found in the template")
        self.assertNotEqual(match.group(1), "latest")
        self.assertRegex(match.group(1), r"^\d+\.\d+\.\d+$")


if __name__ == "__main__":
    unittest.main(verbosity=2)
