#!/usr/bin/env python3
"""Tests for the derived role semantics layer.

Run: python3 "08_SYSTEMS/Engineering Toolkit/test_role_semantics.py"

Two properties are worth more than all the rest here, and most of these tests
exist to hold them:

  * Nothing is invented. Every field traces to a document, and a link that has no
    exact alias stays unresolved rather than becoming a plausible guess.
  * Nothing authored is dropped. The registry is written two ways, and a parser
    that reads one shape reports the other as empty -- which would tell the
    Foundation that two ratified functions are undocumented when they are not.
"""

from __future__ import annotations

import inspect
import re
import sys
import tempfile
import unittest
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT.parent.parent
sys.path.insert(0, str(TOOLKIT))

import entity_registry as er  # noqa: E402
import role_semantics as rs  # noqa: E402

CF_REGISTRY = """---
title: "Cognitive Function Registry"
---

| Code | Function | Category | Current Engine | Status |
|------|----------|----------|---------------|--------|
| CF-01 | Institutional Architecture | A — Core | Claude | Active |
| CF-07 | Engineering Intelligence | B — Specialist | Codex | Active |
| CF-08 | Institutional Observatory | B — Specialist | Comet | Active |
| CF-10 | Ethics Intelligence | A — Core | Ethics Council | Active |
| CF-12 | Health Intelligence (ATHENA) | B — Specialist | ATHENA Office | Active |
| CF-15 | Data & Systems Intelligence (JERANIUM) | B — Specialist | [To be appointed] | Registered (Epoch V) |

## CF-01 — Institutional Architecture

**Current Engine:** Claude (Anthropic)
**Category:** A — Core
**Status:** Active
**Intelligence Office:** LUMIAION

### Purpose

Synthesising knowledge into enduring institutional form.

### Mission

To translate cognitive output into institutional structure.

### Authority

- Final integration authority over research entering the Vault
- Constitutional drafting authority

### Inputs

- Research Intelligence outputs

### Outputs

- Constitutional documents

### Primary Responsibilities

1. Drafting constitutional documents
2. Maintaining the knowledge graph

### Limitations

- Does not independently investigate empirical questions

### Relationships with Other Functions

| Function | Relationship Type | Nature |
|----------|------------------|--------|
| CF-07 Engineering Intelligence | Downstream implementer | Builds what architecture specifies |
| CF-10 Ethics Intelligence | Accountable to | Constitutional outputs subject to review |
| All functions | Coordinator | Coordinates multi-function work |

### Review Cycle

- Quarterly review

### Succession Rules

Replacement engine must demonstrate constitutional drafting competence.

---

## CF-07 — Engineering Intelligence

**Current Engine:** Codex
**Category:** B — Specialist
**Status:** Active
**Intelligence Office:** Engineering Office

### Purpose

Building the Foundation's tools.

### Mission

To implement what architecture specifies.

### Authority

- Implementation authority

### Inputs

- Approved specifications

### Outputs

- Tools and validators

### Primary Responsibilities

1. Building and maintaining the toolkit

### Limitations

- No governance authority

### Review Cycle

- Daily

### Succession Rules

Replacement engine must pass the toolkit suite.

---

## CF-08 — Institutional Observatory

**Current Engine:** Comet
**Category:** B — Specialist
**Status:** Active
**Intelligence Office:** Institutional Observatory

### Purpose

Observing institutional health.

### Mission

To report drift before it compounds.

### Authority

- Observation authority

### Inputs

- Metrics

### Outputs

- Observation reports

### Primary Responsibilities

1. Monitoring institutional signals

### Limitations

- Not a decision authority

### Review Cycle

- Daily

### Succession Rules

Replacement engine must sustain continuous observation.

---

## CF-12 — Health Intelligence

**Current Engine:** ATHENA Office
**Category:** B — Specialist
**Status:** Active
**Intelligence Office:** ATHENA (09_OFFICES/ATHENA)

### Purpose

Health and human performance research.

### Mission

To ground human potential work in medical science.

### Authority

- Health research commission authority

### Inputs

- Health research commissions

### Outputs

- Health intelligence briefs

### Succession Rules

ATHENA Office functions as an integrated unit.

---

## CF-15 — Data & Systems Intelligence (JERANIUM)
**Category:** B — Specialist (infrastructure) · **Current Engine:** [To be appointed] · **Status:** Registered (Epoch V)

**Purpose.** Data orchestration, analytics, and system optimization.

**Mission.** Ensure the Foundation's data is well-orchestrated.

**Primary responsibilities.** Data pipeline maintenance; analytics and reporting; dashboard generation.

**Boundaries.** Does not adjudicate knowledge truth (Book III / CF-02/CF-03); infrastructure function only.

**Succession.** Engine appointed by the Cognitive Council per the Engine Succession Policy.

---
"""

OFFICE_REGISTRY = """---
title: "Office Registry"
---

## Core Content

| Office | Purpose | Authority | Inputs | Outputs | Artifacts Produced | Review Cycle | Dependencies | Responsible Cognitive Function | Preferred Reasoning Engine | Engineering Support |
|---|---|---|---|---|---|---|---|---|---|---|
| LUMIAION / Institutional Intelligence | Orchestrate the Foundation | Orchestration within defined scope | Founder requests | Routing decisions | Summaries | Daily | [[LUMIAION Charter]] | Orchestration | LUMIAION | Context |
| Engineering Office | Build the toolkit | Implementation only; no governance authority | Approved architecture, engineering debt | Tools, reports, scripts | Standards, validators | Daily and weekly | [[Book I, Chapter 2]], [[Engineering Handbook]] | Implementation | CODEX | Primary |
| Institutional Observatory | Observe institutional health | Observation and reporting; not decision authority | Metrics, vault state | Observation reports | Drift logs | Daily | [[Metrics Registry]] | Observation | Comet | Support |
"""

AGENT_REGISTRY = """---
title: "Agent and Subagent Registry"
version: "1.0.0"
---

## Core Content

### Agent Roles

| ID | Named role | Parent Function | Operating owner | Current implementation | State | May instantiate | Recognised names |
|----|-----------|-----------------|-----------------|------------------------|-------|-----------------|------------------|
| AGT-001 | LUMIAION Orchestrator | CF-01 | LUMIAION | Claude-family | available | context loader; constitutional drafter | — |
| AGT-007 | CODEX Engineering Lead | CF-07 | Engineering Office | Codex | available | architect; builder | CODEX |
| AGT-012 | ATHENA Domain Lead | CF-12 | ATHENA Office | ATHENA | available | health evidence scout | — |
| AGT-015 | JERANIUM Data & Systems Lead | CF-15 | JERANIUM | none | blocked | none until appointment | — |

### Standard Subagent Profiles

| Profile | Output | Boundary |
|---------|--------|----------|
| context loader | Loaded context | Reads only |

### Invocation Rules

1. Every task has one accountable Agent Role.
2. Results return to the Founder as one review surface and one next action.
"""


def fixture_vault(tmp: str) -> Path:
    root = Path(tmp)
    for relative, text in (
        (er.CF_REGISTRY, CF_REGISTRY),
        (er.OFFICE_REGISTRY, OFFICE_REGISTRY),
        (er.AGENT_REGISTRY, AGENT_REGISTRY),
        (er.CONSTITUTION, '---\ntitle: "Book I"\n---\n\n# Book I\n'),
    ):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return root


def build_fixture():
    with tempfile.TemporaryDirectory() as tmp:
        return rs.build(fixture_vault(tmp))


def by_id(contract):
    return {record["entity_id"]: record for record in contract["entities"]}


def codes(contract, code):
    return [item for item in contract["findings"] if item["code"] == code]


class TestDerivedNeverAuthored(unittest.TestCase):
    """Every field traces to a document. This module writes no institutional text."""

    def setUp(self):
        self.contract = build_fixture()

    def test_every_field_carries_a_source_and_a_locator(self):
        for record in self.contract["entities"]:
            for name, value in record["fields"].items():
                self.assertTrue(value["source"],
                                f"{record['entity_id']}.{name} has no source")
                self.assertTrue(value["locator"],
                                f"{record['entity_id']}.{name} has no locator")

    def test_a_locator_names_the_place_inside_the_document(self):
        """A document-level citation is too coarse to check one claim against."""
        record = by_id(self.contract)["agent:cf-01"]
        self.assertIn("Authority", record["fields"]["authority"]["locator"])
        office = by_id(self.contract)["office:engineering-office"]
        self.assertIn("Engineering Office", office["fields"]["authority"]["locator"])
        self.assertIn("Authority", office["fields"]["authority"]["locator"])

    def test_every_semantics_record_has_an_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = fixture_vault(tmp)
            identity = er.build(root)
            contract = rs.build(root)
        known = {item["entity_id"] for item in identity["entities"]}
        for record in contract["entities"]:
            self.assertIn(record["entity_id"], known,
                          f"{record['entity_id']} has semantics but no identity")

    def test_no_field_is_synthesised_for_an_absent_section(self):
        """CF-12 states no responsibilities. The field is absent, not filled in."""
        record = by_id(self.contract)["agent:cf-12"]
        self.assertNotIn("responsibilities", record["fields"])
        self.assertIn("responsibilities", record["coverage"]["absent"])

    def test_prose_defined_entities_get_identity_but_no_derived_fields(self):
        founder = by_id(self.contract)["person:founder"]
        self.assertEqual(founder["fields"], {})
        self.assertTrue(codes(self.contract, "semantics_source_is_prose"))

    def test_a_missing_registry_fails_rather_than_deriving_a_partial_institution(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises((rs.SemanticsError, er.EntityError)):
                rs.build(Path(tmp))


class TestBothAuthoredFormats(unittest.TestCase):
    """CF-15 is documented. A heading-only parser reports it as empty."""

    def setUp(self):
        self.contract = build_fixture()

    def test_the_compact_form_yields_its_authored_fields(self):
        record = by_id(self.contract)["agent:cf-15"]
        self.assertEqual(record["source_format"], "compact")
        for name in ("purpose", "mission", "responsibilities", "limitations",
                     "succession"):
            self.assertIn(name, record["fields"],
                          f"CF-15 states {name} and it was not read")

    def test_the_compact_form_metadata_is_read_from_one_line(self):
        record = by_id(self.contract)["agent:cf-15"]
        self.assertEqual(record["fields"]["status"]["value"], "Registered (Epoch V)")
        self.assertIn("appointed", record["fields"]["engine"]["value"].lower())

    def test_boundaries_and_limitations_are_one_field(self):
        """Two dialects of one registry, not two different claims."""
        compact = by_id(self.contract)["agent:cf-15"]["fields"]["limitations"]
        sectioned = by_id(self.contract)["agent:cf-01"]["fields"]["limitations"]
        self.assertIsInstance(compact["value"], list)
        self.assertIsInstance(sectioned["value"], list)
        self.assertIn("Boundaries", compact["locator"])
        self.assertIn("Limitations", sectioned["locator"])

    def test_no_field_value_carries_the_section_separator(self):
        for record in self.contract["entities"]:
            for name, value in record["fields"].items():
                items = value["value"] if isinstance(value["value"], list) else [value["value"]]
                for item in items:
                    self.assertNotIn("---", str(item),
                                     f"{record['entity_id']}.{name} carries layout")
                    self.assertEqual(str(item), str(item).strip(),
                                     f"{record['entity_id']}.{name} carries whitespace")

    def test_format_divergence_is_reported_not_smoothed_over(self):
        self.assertTrue(codes(self.contract, "registry_format_divergence"))

    def test_a_compact_gap_is_not_blamed_on_an_appointment(self):
        """The compact form has no authority slot. That is editorial, not pending."""
        reported = codes(self.contract, "compact_entry_incomplete")
        self.assertTrue(reported)
        self.assertTrue(all(item["severity"] == "warning" for item in reported))


class TestTypeConstrainedResolution(unittest.TestCase):
    """A link resolves by exact alias under the type its field declares, or not at all."""

    def setUp(self):
        self.contract = build_fixture()

    def test_a_function_is_never_its_own_office(self):
        """CF-08 shares the label `Institutional Observatory` with an office."""
        record = by_id(self.contract)["agent:cf-08"]
        self.assertNotEqual(record["office"]["entity_id"], "agent:cf-08")
        self.assertEqual(record["office"]["entity_id"], "office:institutional-observatory")
        self.assertEqual(record["office"]["method"], "alias+type")

    def test_a_contested_alias_is_reported_even_once_recovered(self):
        """Resolution succeeded; the ambiguity is still the Founder's to settle."""
        self.assertTrue(codes(self.contract, "office_alias_contested"))

    def test_an_office_field_naming_the_functions_own_alias_stays_unresolved(self):
        record = by_id(self.contract)["agent:cf-12"]
        self.assertIsNone(record["office"]["entity_id"])
        self.assertEqual(record["office"]["reason"], "self_reference")
        self.assertTrue(codes(self.contract, "office_is_self_alias"))

    def test_an_unresolved_link_names_its_reason(self):
        for record in self.contract["entities"]:
            for key in ("office", "responsible_cognitive_function", "parent_function"):
                link = record.get(key)
                if link and link["entity_id"] is None:
                    self.assertTrue(link["reason"],
                                    f"{record['entity_id']}.{key} is silent about why")

    def test_a_resolved_link_records_how_it_resolved(self):
        for record in self.contract["entities"]:
            for key in ("office", "responsible_cognitive_function", "parent_function"):
                link = record.get(key)
                if link and link["entity_id"]:
                    self.assertIn(link["method"], ("alias", "alias+type"))

    def test_the_office_registrys_role_verbs_are_not_matched_by_resemblance(self):
        """`Implementation` is not `Engineering Intelligence` until a human says so."""
        for record in self.contract["entities"]:
            if record["role_class"] != "office":
                continue
            self.assertIsNone(record["responsible_cognitive_function"]["entity_id"])
        reported = codes(self.contract, "office_cf_vocabulary_mismatch")
        self.assertEqual(len(reported), 1)
        self.assertEqual(reported[0]["severity"], "warning")

    def test_the_function_to_office_direction_is_the_one_that_binds(self):
        record = by_id(self.contract)["agent:cf-01"]
        self.assertEqual(record["office"]["entity_id"], "office:lumiaion")
        self.assertEqual(by_id(self.contract)["agent:cf-07"]["office"]["entity_id"],
                         "office:engineering-office")

    def test_resolve_typed_refuses_an_entity_of_the_wrong_type(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = er.build(fixture_vault(tmp))
        link = rs.resolve_typed(registry, "CF-01", "office")
        self.assertIsNone(link["entity_id"])
        self.assertIn("not_office", link["reason"])

    def test_an_unratified_name_never_resolves(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = er.build(fixture_vault(tmp))
        link = rs.resolve_typed(registry, "Department of Plausible Names", "office")
        self.assertIsNone(link["entity_id"])
        self.assertEqual(link["reason"], "no_office_of_that_name")


class TestEscalationIsAuthoredOnly(unittest.TestCase):
    """Escalation comes from the registry's own words, never from work-flow edges."""

    def setUp(self):
        self.contract = build_fixture()

    def test_only_accountability_becomes_a_functions_escalation(self):
        record = by_id(self.contract)["agent:cf-01"]
        bases = {link["basis"] for link in record["escalation"]}
        self.assertEqual(bases, {"Accountable to"})
        types = {edge["type"] for edge in record["relationships"]}
        self.assertIn("Downstream implementer", types)

    def test_every_escalation_edge_names_its_basis_and_source(self):
        for record in self.contract["entities"]:
            for link in record["escalation"]:
                self.assertTrue(link["basis"])
                self.assertTrue(link["source"])
                self.assertTrue(link["locator"])

    def test_escalation_counts_are_split_by_basis(self):
        """A function's accountability and an agent's parent are not the same claim."""
        basis = self.contract["counts"]["escalation_edges_by_basis"]
        self.assertIn("Accountable to", basis)
        self.assertIn("Parent Function", basis)

    def test_an_office_gets_no_escalation_from_prose(self):
        """`subject to Founder approval` is prose; inferring an edge from it is inference."""
        for record in self.contract["entities"]:
            if record["role_class"] == "office":
                self.assertEqual(record["escalation"], [])

    def test_a_collective_target_stays_one_edge(self):
        edges = [edge for record in self.contract["entities"]
                 for edge in record["relationships"] if edge["scope"] == "collective"]
        self.assertTrue(edges)
        for edge in edges:
            self.assertIsNone(edge["target_entity_id"])
        reported = codes(self.contract, "collective_relationship_targets")
        self.assertEqual(reported[0]["severity"], "info")

    def test_an_unresolvable_relationship_target_is_counted_and_reported(self):
        """A count with no finding is a failure the reader can miss."""
        broken = CF_REGISTRY.replace("| CF-07 Engineering Intelligence |",
                                     "| CF-99 Imagined Intelligence |")
        with tempfile.TemporaryDirectory() as tmp:
            root = fixture_vault(tmp)
            (root / er.CF_REGISTRY).write_text(broken, encoding="utf-8")
            contract = rs.build(root)
        self.assertEqual(contract["counts"]["relationship_edges_unresolved"], 1)
        reported = codes(contract, "relationship_target_unresolved")
        self.assertEqual(len(reported), 1)
        self.assertEqual(reported[0]["severity"], "warning")

    def test_a_collective_edge_is_not_counted_as_a_failure(self):
        counts = self.contract["counts"]
        self.assertEqual(counts["relationship_edges_unresolved"], 0)
        self.assertGreater(counts["relationship_edges_collective"], 0)

    def test_invocation_rules_are_carried_not_expanded_into_edges(self):
        self.assertTrue(self.contract["invocation_rules"])
        for record in self.contract["entities"]:
            targets = {link["entity_id"] for link in record["escalation"]}
            self.assertNotIn("person:founder", targets)


class TestSeveritySemantics(unittest.TestCase):
    """error invalidates, warning is real, info is the expected state of a gap."""

    def setUp(self):
        self.contract = build_fixture()

    def test_the_fixture_institution_is_sound(self):
        errors = [item for item in self.contract["findings"]
                  if item["severity"] == "error"]
        self.assertEqual(errors, [], f"unexpected errors: {errors}")

    def test_an_active_function_missing_its_mandate_is_a_warning(self):
        reported = [item for item in codes(self.contract, "cognitive_function_incomplete")
                    if item["entity_id"] == "agent:cf-12"]
        self.assertEqual(len(reported), 1)
        self.assertEqual(reported[0]["severity"], "warning")

    def test_an_unappointed_function_missing_sections_is_informational(self):
        """Reporting an expected gap as a problem trains the reader to ignore the report."""
        for item in codes(self.contract, "cognitive_function_incomplete"):
            record = by_id(self.contract)[item["entity_id"]]
            if rs._is_unappointed(record):
                self.assertEqual(item["severity"], "info")

    def test_a_dispatchable_role_without_a_documented_mandate_is_a_warning(self):
        reported = codes(self.contract, "agent_available_without_mandate")
        self.assertTrue(any(item["entity_id"] == "agent:agt-012" for item in reported))
        self.assertTrue(all(item["severity"] == "warning" for item in reported))

    def test_a_blocked_role_is_informational(self):
        reported = [item for item in codes(self.contract, "agent_state_limited")
                    if item["entity_id"] == "agent:agt-015"]
        self.assertEqual(len(reported), 1)
        self.assertEqual(reported[0]["severity"], "info")

    def test_a_states_cause_is_claimed_only_where_a_registry_states_it(self):
        """AGT-015 is blocked and CF-15 has no engine. Both facts are in documents."""
        reported = [item for item in codes(self.contract, "agent_state_limited")
                    if item["entity_id"] == "agent:agt-015"][0]
        self.assertIn("CF-15", reported["message"])

    def test_an_unresolved_parent_function_is_an_error(self):
        """A role with no mandate to inherit makes the layer unsound, not merely thin."""
        broken = AGENT_REGISTRY.replace("| AGT-007 | CODEX Engineering Lead | CF-07 |",
                                        "| AGT-007 | CODEX Engineering Lead | CF-99 |")
        with tempfile.TemporaryDirectory() as tmp:
            root = fixture_vault(tmp)
            (root / er.AGENT_REGISTRY).write_text(broken, encoding="utf-8")
            contract = rs.build(root)
        reported = codes(contract, "agent_parent_unresolved")
        self.assertEqual(len(reported), 1)
        self.assertEqual(reported[0]["severity"], "error")

    def test_every_finding_uses_the_shared_severity_vocabulary(self):
        for item in self.contract["findings"]:
            self.assertIn(item["severity"], ("error", "warning", "info"))
            self.assertTrue(item["code"])
            self.assertTrue(item["message"])

    def test_checks_that_pass_still_report(self):
        """A reader must be able to tell a clean result from an absent one."""
        counts = self.contract["counts"]
        for key in ("relationship_edges", "relationship_edges_unresolved",
                    "functions_bound_to_office", "escalation_edges"):
            self.assertIsInstance(counts[key], int)


class TestTableReading(unittest.TestCase):
    """Columns are located by name, and a cell's separators are respected."""

    def setUp(self):
        self.contract = build_fixture()

    def test_a_reshaped_office_table_fails_rather_than_misattributing(self):
        reshaped = OFFICE_REGISTRY.replace("| Office | Purpose |", "| Bureau | Purpose |")
        with tempfile.TemporaryDirectory() as tmp:
            root = fixture_vault(tmp)
            (root / er.OFFICE_REGISTRY).write_text(reshaped, encoding="utf-8")
            with self.assertRaises(rs.SemanticsError):
                rs.build(root)

    def test_an_inserted_column_does_not_re_point_every_field(self):
        """Position-indexed reading turns one insertion into seven wrong attributions."""
        shifted = (OFFICE_REGISTRY
                   .replace("| Office | Purpose |", "| Office | Epoch | Purpose |")
                   .replace("|---|---|---|---|---|---|---|---|---|---|---|",
                            "|---|---|---|---|---|---|---|---|---|---|---|---|")
                   .replace("| LUMIAION / Institutional Intelligence | Orchestrate",
                            "| LUMIAION / Institutional Intelligence | V | Orchestrate")
                   .replace("| Engineering Office | Build the toolkit",
                            "| Engineering Office | V | Build the toolkit")
                   .replace("| Institutional Observatory | Observe institutional health",
                            "| Institutional Observatory | V | Observe institutional health"))
        with tempfile.TemporaryDirectory() as tmp:
            root = fixture_vault(tmp)
            (root / er.OFFICE_REGISTRY).write_text(shifted, encoding="utf-8")
            contract = rs.build(root)
        record = by_id(contract)["office:engineering-office"]
        self.assertEqual(record["fields"]["purpose"]["value"], "Build the toolkit")
        self.assertIn("Implementation only", record["fields"]["authority"]["value"])

    def test_a_comma_inside_a_wiki_link_is_not_a_list_separator(self):
        """`[[Book I, Chapter 2]]` is one document, not two that do not exist."""
        record = by_id(self.contract)["office:engineering-office"]
        self.assertIn("[[Book I, Chapter 2]]", record["fields"]["dependencies"]["value"])

    def test_a_cell_enumeration_becomes_a_list(self):
        record = by_id(self.contract)["office:engineering-office"]
        self.assertEqual(record["fields"]["outputs"]["value"],
                         ["Tools", "reports", "scripts"])

    def test_prose_in_a_list_column_survives_as_one_item(self):
        record = by_id(self.contract)["office:engineering-office"]
        self.assertEqual(record["fields"]["review_cycle"]["value"], ["Daily and weekly"])

    def test_the_fixture_agent_table_matches_the_parsers_schema(self):
        """The fixture duplicates the registry's shape, so it drifts when that shape moves.

        It already did: the Recognised names column landed in the Agent and
        Subagent Registry while this fixture still wrote seven columns, and the
        mismatch surfaced as forty-four unrelated errors rather than one. This
        asserts the agreement directly, so the next schema change fails here with
        a sentence that names the cause.
        """
        header = next(line for line in AGENT_REGISTRY.splitlines()
                      if line.strip().startswith("| ID |"))
        columns = len(header.strip().strip("|").split("|"))
        # Read the parser's own expectation rather than restating it here, so the
        # two cannot drift apart the way the fixture and the registry just did.
        source = inspect.getsource(rs.rr.parse_roles_table)
        wanted = int(re.search(r"expected_columns=(\d+)", source).group(1))
        self.assertEqual(columns, wanted,
                         f"fixture agent table has {columns} columns; "
                         f"role_registry.parse_roles_table expects {wanted}")

    def test_the_agent_table_is_read_through_its_existing_parser(self):
        """One parser per document. A second would drift from the first."""
        self.assertTrue(hasattr(rs.rr, "load_roles"))
        record = by_id(self.contract)["agent:agt-001"]
        self.assertIn("context loader", record["fields"]["may_instantiate"]["value"])


class TestShippedVault(unittest.TestCase):
    """The claims this layer makes about the Foundation as it stands today."""

    @classmethod
    def setUpClass(cls):
        cls.contract = rs.build(VAULT_ROOT)

    def test_all_forty_two_entities_have_semantics(self):
        identity = er.build(VAULT_ROOT)
        self.assertEqual(self.contract["counts"]["entities"],
                         identity["counts"]["entities"])
        self.assertEqual(self.contract["counts"]["entities"], 42)

    def test_the_shipped_vault_derives_without_error(self):
        errors = [item for item in self.contract["findings"]
                  if item["severity"] == "error"]
        self.assertEqual(errors, [], f"unexpected errors: {errors}")

    def test_every_agent_role_inherits_a_real_function(self):
        for record in self.contract["entities"]:
            if record["role_class"] == "agent_role":
                self.assertIsNotNone(record["parent_function"]["entity_id"],
                                     f"{record['code']} has no parent function")

    def test_cf_fifteen_and_sixteen_are_documented(self):
        """They are written in the compact form, which is not the same as empty."""
        for entity_id in ("agent:cf-15", "agent:cf-16"):
            record = by_id(self.contract)[entity_id]
            self.assertEqual(record["source_format"], "compact")
            self.assertIn("purpose", record["fields"])
            self.assertIn("responsibilities", record["fields"])

    def test_no_office_row_binds_to_a_cognitive_function_today(self):
        """Seven rows, zero matches. Recorded so the gap cannot be lost."""
        offices = [record for record in self.contract["entities"]
                   if record["role_class"] == "office"]
        self.assertEqual(len(offices), 7)
        bound = [record for record in offices
                 if record["responsible_cognitive_function"]["entity_id"]]
        self.assertEqual(bound, [])

    def test_the_relationship_graph_resolves_except_for_collective_targets(self):
        counts = self.contract["counts"]
        self.assertEqual(counts["relationship_edges_unresolved"], 0)
        self.assertEqual(
            counts["relationship_edges"],
            counts["relationship_edges_resolved"] + counts["relationship_edges_collective"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
