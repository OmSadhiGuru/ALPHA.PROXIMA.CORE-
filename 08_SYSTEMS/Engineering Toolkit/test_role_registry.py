#!/usr/bin/env python3
"""Tests for the Agent and Subagent Registry parser.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_role_registry.py"
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import role_registry as rr  # noqa: E402


MINIMAL_DOC = """---
version: "9.9.9"
---

## Core Content

### Agent Roles

| ID | Named role | Parent Function | Operating owner | Current implementation | State | May instantiate |
|----|------------|-----------------|-----------------|------------------------|-------|-----------------|
| AGT-001 | Test Lead | CF-01 | Test Office | Claude | available | context loader; tester |
| AGT-002 | Blocked Lead | CF-02 | Test Office | Unappointed | blocked | none |

### Standard Subagent Profiles

| Profile | Output | Required boundary |
|---------|--------|-------------------|
| Context Loader | Minimal source packet | Read-only |

### Invocation Rules

1. Every task has one accountable Agent Role.
2. Subagents receive one bounded deliverable.

## Related Notes
"""


def write_doc(tmp: str, text: str) -> Path:
    path = Path(tmp) / "registry.md"
    path.write_text(text, encoding="utf-8")
    return path


class TestParsing(unittest.TestCase):
    def test_parses_the_minimal_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = rr.load_roles(path=write_doc(tmp, MINIMAL_DOC))
        self.assertEqual(len(registry["roles"]), 2)
        self.assertEqual(len(registry["subagent_profiles"]), 1)
        self.assertEqual(registry["invocation_rules"],
                         ["Every task has one accountable Agent Role.",
                          "Subagents receive one bounded deliverable."])
        self.assertEqual(registry["document_version"], "9.9.9")

    def test_may_instantiate_is_split_on_semicolons(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = rr.load_roles(path=write_doc(tmp, MINIMAL_DOC))
        self.assertEqual(rr.role(registry, "AGT-001")["may_instantiate"], ["context loader", "tester"])


class TestRealRegistry(unittest.TestCase):
    """The shipped registry is the actual source of truth this module protects."""

    def test_parses_all_sixteen_roles(self):
        registry = rr.load_roles()
        self.assertEqual(len(registry["roles"]), 16)
        yuna = rr.role(registry, "AGT-016")
        self.assertEqual(yuna["named_role"], "YUNA Synthesis & Learning Lead")
        self.assertEqual(yuna["operating_owner"], "Owner pending")
        self.assertEqual(yuna["state"], "blocked")
        self.assertEqual(yuna["may_instantiate"],
                         ["synthesis planner", "translation worker", "learning adapter after appointment"])

    def test_state_values_are_normalized_and_validated(self):
        registry = rr.load_roles()
        for record in registry["roles"]:
            self.assertIn(record["state"], rr.VALID_ROLE_STATES)

    def test_counts_match_the_known_registry_shape(self):
        counts = rr.load_roles()["counts"]
        self.assertEqual(counts["roles"], 16)
        self.assertEqual(counts["available"], 12)
        self.assertEqual(counts["advisory_only"], 1)
        self.assertEqual(counts["blocked"], 3)
        self.assertEqual(counts["owners"], 10)

    def test_owners_grouping_matches_the_registry_exactly(self):
        owners = {o["owner"]: o["role_ids"] for o in rr.load_roles()["owners"]}
        self.assertEqual(owners["LUMIAION"], ["AGT-001", "AGT-009"])
        self.assertEqual(owners["Research Intelligence Office"], ["AGT-002", "AGT-003", "AGT-004"])
        self.assertEqual(owners["Engineering Office"], ["AGT-005", "AGT-007"])
        self.assertEqual(owners["Executive Office"], ["AGT-006", "AGT-011"])
        self.assertEqual(owners["Institutional Observatory"], ["AGT-008"])
        # Exact source text, not normalized -- fidelity to the document is the point.
        self.assertEqual(owners["Ethics Council when convened"], ["AGT-010"])
        self.assertEqual(owners["ATHENA"], ["AGT-012"])
        self.assertEqual(owners["VORTEX"], ["AGT-013"])
        self.assertEqual(owners["SOHMA"], ["AGT-014"])
        self.assertEqual(owners["Owner pending"], ["AGT-015", "AGT-016"])

    def test_thirteen_subagent_profiles_and_seven_invocation_rules(self):
        registry = rr.load_roles()
        self.assertEqual(len(registry["subagent_profiles"]), 13)
        self.assertEqual(len(registry["invocation_rules"]), 7)


class TestErrors(unittest.TestCase):
    def test_missing_registry_file_raises(self):
        with self.assertRaises(rr.RegistryError):
            rr.load_roles(path=Path("/nonexistent/registry.md"))

    def test_malformed_row_raises(self):
        bad = MINIMAL_DOC.replace(
            "| AGT-002 | Blocked Lead | CF-02 | Test Office | Unappointed | blocked | none |",
            "| AGT-002 | Blocked Lead | CF-02 | Test Office | blocked | none |",  # one column short
        )
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(rr.RegistryError):
                rr.load_roles(path=write_doc(tmp, bad))

    def test_duplicate_role_id_raises(self):
        bad = MINIMAL_DOC.replace(
            "| AGT-002 | Blocked Lead | CF-02 | Test Office | Unappointed | blocked | none |",
            "| AGT-001 | Blocked Lead | CF-02 | Test Office | Unappointed | blocked | none |",
        )
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(rr.RegistryError):
                rr.load_roles(path=write_doc(tmp, bad))

    def test_unrecognized_state_raises(self):
        bad = MINIMAL_DOC.replace(
            "| AGT-002 | Blocked Lead | CF-02 | Test Office | Unappointed | blocked | none |",
            "| AGT-002 | Blocked Lead | CF-02 | Test Office | Unappointed | pending | none |",
        )
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(rr.RegistryError):
                rr.load_roles(path=write_doc(tmp, bad))

    def test_missing_roles_table_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(rr.RegistryError):
                rr.load_roles(path=write_doc(tmp, "## Core Content\n\nNo tables here.\n"))

    def test_zero_data_rows_raises(self):
        headers_only = """### Agent Roles

| ID | Named role | Parent Function | Operating owner | Current implementation | State | May instantiate |
|----|------------|-----------------|-----------------|------------------------|-------|-----------------|

### Standard Subagent Profiles

| Profile | Output | Required boundary |
|---------|--------|-------------------|

### Invocation Rules

1. Placeholder.
"""
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(rr.RegistryError):
                rr.load_roles(path=write_doc(tmp, headers_only))

    def test_unknown_role_lookup_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = rr.load_roles(path=write_doc(tmp, MINIMAL_DOC))
        with self.assertRaises(rr.RegistryError):
            rr.role(registry, "AGT-999")


class TestNeverWrites(unittest.TestCase):
    def test_module_defines_no_writer(self):
        """The registry is Founder-edited Markdown; this module only ever reads it."""
        source = Path(rr.__file__).read_text(encoding="utf-8")
        for forbidden in ("write_text(", ".write(", "save_state", "save_roles"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
