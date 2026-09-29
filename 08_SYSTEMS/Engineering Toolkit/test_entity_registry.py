#!/usr/bin/env python3
"""Tests for the Entity Registry and the Truth Kernel's entity/document split.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_entity_registry.py"
"""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT.parent.parent
sys.path.insert(0, str(TOOLKIT))

import entity_registry as er  # noqa: E402


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


truth_kernel = _load(
    VAULT_ROOT / "08_SYSTEMS" / "Institutional Knowledge Graph" / "Tools" / "truth_kernel.py",
    "tk_under_test",
)


CF_REGISTRY = """---
title: "Cognitive Function Registry"
---

| Code | Function | Category | Current Engine | Status |
|------|----------|----------|---------------|--------|
| CF-01 | Institutional Architecture | A — Core | Claude | Active |
| CF-07 | Engineering Intelligence | B — Specialist | Codex / DeepSeek | Active |
| CF-12 | Health Intelligence | B — Specialist | ATHENA Office | Active |
"""

OFFICE_REGISTRY = """---
title: "Office Registry"
---

| Office | Purpose | Authority | Inputs | Outputs | Artifacts | Review | Dependencies | Function | Engine | Support |
|---|---|---|---|---|---|---|---|---|---|---|
| LUMIAION / Institutional Intelligence | Orchestrate | Orchestration | Requests | Routing | Summaries | Daily | None | Orchestration | LUMIAION | Context |
| Engineering Office | Build tools | Implementation | Specs | Tools | Standards | Daily | None | Implementation | CODEX | Primary |
"""

AGENT_REGISTRY = """---
title: "Agent and Subagent Registry"
---

| ID | Named Role | Parent Function | Operating Owner | Current Implementation | State | May Instantiate |
|----|-----------|-----------------|-----------------|------------------------|-------|-----------------|
| AGT-001 | LUMIAION Orchestrator | CF-01 | LUMIAION | Claude-family | available | Yes |
| AGT-007 | CODEX Engineering Lead | CF-07 | Engineering Office | Codex | available | Yes |
"""


def fixture_vault(tmp: str) -> Path:
    root = Path(tmp)
    for relative, text in (
        (er.CF_REGISTRY, CF_REGISTRY),
        (er.OFFICE_REGISTRY, OFFICE_REGISTRY),
        (er.AGENT_REGISTRY, AGENT_REGISTRY),
        (er.CONSTITUTION, "---\ntitle: \"Book I\"\n---\n\n# Book I\n"),
    ):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return root


class TestDerivedFromRatifiedRegistries(unittest.TestCase):
    """Entities are derived, never authored. Nothing here invents an actor."""

    def test_cognitive_functions_become_agents(self):
        with tempfile.TemporaryDirectory() as tmp:
            reg = er.build(fixture_vault(tmp))
        ids = {e["entity_id"] for e in reg["entities"]}
        self.assertIn("agent:cf-01", ids)
        self.assertIn("agent:cf-07", ids)

    def test_every_entity_carries_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            reg = er.build(fixture_vault(tmp))
        for item in reg["entities"]:
            self.assertTrue(item["canonical_source"],
                            f"{item['entity_id']} has no canonical source")
            self.assertIn(item["entity_type"], er.ENTITY_TYPES)

    def test_a_name_in_no_registry_does_not_resolve(self):
        """Silence is not resolution. An unratified actor stays visible."""
        with tempfile.TemporaryDirectory() as tmp:
            reg = er.build(fixture_vault(tmp))
        self.assertIsNone(er.resolve(reg, "Some Unregistered Consultant"))

    def test_missing_registry_raises_in_strict_mode(self):
        """A real vault without its Council registries is misconfigured."""
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(er.EntityError):
                er.build(Path(tmp))

    def test_missing_registry_degrades_and_reports_in_lenient_mode(self):
        """The Truth Kernel indexes fixture roots; absence must never be silent."""
        with tempfile.TemporaryDirectory() as tmp:
            reg = er.build(Path(tmp), strict=False)
        self.assertEqual(len(reg["missing_sources"]), 4)
        self.assertTrue(all(e["entity_type"] in ("organization", "person")
                            for e in reg["entities"]))

    def test_the_shipped_vault_is_missing_no_canonical_source(self):
        self.assertEqual(er.build(VAULT_ROOT)["missing_sources"], [])


class TestResolution(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.registry = er.build(fixture_vault(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def test_engine_name_resolves_to_its_function(self):
        self.assertEqual(er.resolve(self.registry, "CODEX"), "agent:cf-07")

    def test_explicit_cf_code_outranks_any_alias(self):
        """`LUMIAION (CF-01)` names CF-01, whatever LUMIAION alone resolves to."""
        self.assertEqual(er.resolve(self.registry, "LUMIAION (CF-01)"), "agent:cf-01")
        self.assertNotEqual(er.resolve(self.registry, "LUMIAION"), "agent:cf-01")

    def test_a_registry_label_outranks_a_cited_engine_name(self):
        """LUMIAION is an office by name; CF-09 merely runs on it."""
        self.assertEqual(er.resolve(self.registry, "LUMIAION"), "office:lumiaion")

    def test_bare_office_name_resolves_when_registry_says_x_office(self):
        self.assertEqual(er.resolve(self.registry, "ATHENA"), "agent:cf-12")

    def test_organization_resolves(self):
        self.assertEqual(er.resolve(self.registry, "Alpha Proxima Foundation"),
                         "organization:alpha-proxima-foundation")

    def test_resolution_is_case_and_whitespace_insensitive(self):
        self.assertEqual(er.resolve(self.registry, "  codex  "), "agent:cf-07")

    def test_placeholders_never_resolve(self):
        for value in ("<AUTHOR>", "[Author]", "null", "TBD", "To be appointed", "—"):
            self.assertTrue(er.is_placeholder(value), value)
            self.assertIsNone(er.resolve(self.registry, value), value)

    def test_a_real_name_is_not_mistaken_for_a_placeholder(self):
        for value in ("CODEX", "Alpha Proxima Foundation", "Engineering Office"):
            self.assertFalse(er.is_placeholder(value), value)


class TestEntityDocumentDistinction(unittest.TestCase):
    """The distinction this whole change exists to draw."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.registry = er.build(fixture_vault(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def rel(self, **kw):
        base = {"relationship_type": "PRODUCED_BY", "source_path": "a.md",
                "source_detail": "authors", "target_raw": "CODEX",
                "relationship_source": "yaml_field"}
        base.update(kw)
        return base

    def test_an_actor_reference_becomes_a_typed_entity_edge(self):
        edges, placeholders, remaining = truth_kernel.partition_unresolved(
            [self.rel()], self.registry)
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0]["target_entity_id"], "agent:cf-07")
        self.assertEqual(edges[0]["target_kind"], "entity")
        self.assertEqual((placeholders, remaining), ([], []))

    def test_an_entity_edge_keeps_its_provenance(self):
        edges, _, _ = truth_kernel.partition_unresolved([self.rel()], self.registry)
        self.assertEqual(edges[0]["source_path"], "a.md")
        self.assertEqual(edges[0]["source_detail"], "authors")
        self.assertEqual(edges[0]["relationship_type"], "PRODUCED_BY")

    def test_a_missing_document_reference_is_never_reclassified(self):
        """A wiki-link to a document that does not exist stays a defect."""
        missing = self.rel(relationship_type="REFERENCES", source_detail="",
                           relationship_source="wiki_link",
                           target_raw="A Document That Does Not Exist")
        edges, placeholders, remaining = truth_kernel.partition_unresolved(
            [missing], self.registry)
        self.assertEqual((edges, placeholders), ([], []))
        self.assertEqual(len(remaining), 1)

    def test_an_actor_name_in_a_wiki_link_is_still_a_document_reference(self):
        """Prose linking `[[CODEX]]` asks for a document, not the actor."""
        link = self.rel(relationship_type="REFERENCES", source_detail="",
                        relationship_source="wiki_link", target_raw="CODEX")
        edges, _, remaining = truth_kernel.partition_unresolved([link], self.registry)
        self.assertEqual(edges, [])
        self.assertEqual(len(remaining), 1)

    def test_template_scaffolding_is_separated_from_both(self):
        edges, placeholders, remaining = truth_kernel.partition_unresolved(
            [self.rel(target_raw="<AUTHOR>")], self.registry)
        self.assertEqual((edges, remaining), ([], []))
        self.assertEqual(placeholders[0]["resolution"], "template_placeholder")

    def test_an_unregistered_author_remains_unresolved(self):
        edges, placeholders, remaining = truth_kernel.partition_unresolved(
            [self.rel(target_raw="Some Unregistered Person")], self.registry)
        self.assertEqual((edges, placeholders), ([], []))
        self.assertEqual(len(remaining), 1)


class TestSeveritySemantics(unittest.TestCase):
    """Errors are integrity failures. Warnings are real. Info is expected state."""

    def test_placeholders_are_informational_not_warnings(self):
        findings = truth_kernel.validate(
            [], [], [{"relationship_type": "PRODUCED_BY", "source_path": "t.md",
                      "target_raw": "<AUTHOR>"}])
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "info")
        self.assertEqual(findings[0]["code"], "template_placeholder")

    def test_a_missing_wiki_link_target_is_an_error(self):
        findings = truth_kernel.validate([], [{
            "relationship_source": "wiki_link", "resolution_status": "missing",
            "relationship_type": "REFERENCES", "source_path": "a.md",
            "target_raw": "Nowhere"}])
        self.assertEqual([f["severity"] for f in findings], ["error"])

    def test_an_empty_note_is_an_error(self):
        findings = truth_kernel.validate(
            [{"node_id": "n1", "source_path": "e.md", "node_type": "policy",
              "canonical_owner": "X", "has_yaml": True, "word_count": 0,
              "validation_findings": []}], [])
        self.assertIn("empty_note", [f["code"] for f in findings])

    def test_info_findings_do_not_drive_status(self):
        """A vault whose only findings are informational is ready, not attention."""
        from collections import Counter
        findings = truth_kernel.validate(
            [], [], [{"relationship_type": "PRODUCED_BY", "source_path": "t.md",
                      "target_raw": "null"}])
        severities = Counter(f["severity"] for f in findings)
        status = "attention" if severities.get("error", 0) else "ready"
        self.assertEqual(status, "ready")


class TestShippedVault(unittest.TestCase):
    """What is committed must resolve the actors the Foundation actually names."""

    @classmethod
    def setUpClass(cls):
        cls.registry = er.build(VAULT_ROOT)

    def test_the_named_actors_resolve(self):
        for name, expected_type in (
            ("CODEX", "agent"),
            ("LUMIAION", "office"),
            ("Alpha Proxima Foundation", "organization"),
            ("OSG", "organization"),
            ("CLAUDE", "agent"),
        ):
            entity_id = er.resolve(self.registry, name)
            self.assertIsNotNone(entity_id, f"{name} did not resolve")
            self.assertTrue(entity_id.startswith(expected_type + ":"),
                            f"{name} resolved to {entity_id}, expected {expected_type}")

    def test_every_alias_maps_to_a_real_entity(self):
        ids = {e["entity_id"] for e in self.registry["entities"]}
        for alias, entity_id in self.registry["alias_index"].items():
            self.assertIn(entity_id, ids, f"alias {alias!r} points at nothing")

    def test_the_kernel_resolves_the_bulk_of_former_unresolved_edges(self):
        contract = truth_kernel.build(VAULT_ROOT)
        counts = contract["counts"]
        self.assertGreater(counts["entity_relationships"], 400)
        self.assertLess(counts["unresolved_relationships"], 400)

    def test_real_errors_survive_entity_resolution(self):
        """Entity resolution must not have quieted a single genuine defect."""
        contract = truth_kernel.build(VAULT_ROOT)
        codes = {f["code"] for f in contract["validation"]["findings"]
                 if f["severity"] == "error"}
        self.assertIn("empty_note", codes)
        self.assertIn("identity_collision", codes)


if __name__ == "__main__":
    unittest.main(verbosity=2)
