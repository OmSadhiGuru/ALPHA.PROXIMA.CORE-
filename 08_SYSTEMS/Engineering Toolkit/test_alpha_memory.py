#!/usr/bin/env python3
"""Tests for the shared edge taxonomy and the memory graph.

The memory graph is the first thing in the Foundation that turns observations
into asserted relationships, which makes it the first thing that can fabricate
one. Most of these tests are about the two ways it could:

  * claiming a relationship type its source cannot witness — a registry saying
    one thing caused another;
  * attaching a provider's name for an actor to a Council seat because the two
    strings look alike.

Both are refused structurally, and these tests are what keep that true.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent


def _load(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLKIT_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ae = _load("alpha_edges.py", "alpha_edges")
ev = _load("alpha_events.py", "alpha_events")
mem = _load("alpha_memory.py", "alpha_memory")

REPO = "OmSadhiGuru/ALPHA.PROXIMA.CORE-"


def event(**overrides) -> dict:
    fields = dict(
        source="github", actor="codex-bot", department="ENGINEERING",
        event_type="github.pr.opened", entity_type="pull_request", entity_id="PR-48",
        title="PR-48 opened", summary="", severity="update",
        occurred_at="2026-09-29T14:00:00+00:00", received_at="2026-09-29T14:00:01+00:00",
        correlation_id="github:pr:48", deep_link="alpha-proxima://github/pr/48",
    )
    fields.update(overrides)
    return ev.make_event(**fields)


def role(role_id: str, named_role: str) -> dict:
    return {"id": role_id, "named_role": named_role}


# --------------------------------------------------------------------------
# the taxonomy
# --------------------------------------------------------------------------

class EdgeContractTests(unittest.TestCase):
    def test_a_well_formed_edge_carries_its_provenance(self):
        item = ae.edge("A", "B", "operational", authority="a record", confidence=1.0)
        self.assertEqual(item["type"], "operational")
        self.assertEqual(item["authority"], "a record")
        self.assertEqual(item["confidence"], 1.0)
        self.assertFalse(item["interpreted"])
        self.assertTrue(item["created_at"])

    def test_an_unknown_type_is_refused(self):
        with self.assertRaises(ae.EdgeError):
            ae.edge("A", "B", "vibes", authority="x", confidence=1.0)

    def test_an_unknown_direction_is_refused(self):
        with self.assertRaises(ae.EdgeError):
            ae.edge("A", "B", "operational", authority="x", confidence=1.0, direction="sideways")

    def test_confidence_outside_zero_to_one_is_refused(self):
        for value in (-0.01, 1.01, 2):
            with self.subTest(confidence=value):
                with self.assertRaises(ae.EdgeError):
                    ae.edge("A", "B", "operational", authority="x", confidence=value)

    def test_a_boolean_is_not_a_confidence(self):
        with self.assertRaises(ae.EdgeError):
            ae.edge("A", "B", "operational", authority="x", confidence=True)

    def test_an_edge_with_no_authority_is_refused(self):
        for authority in ("", "   "):
            with self.subTest(authority=authority):
                with self.assertRaises(ae.EdgeError):
                    ae.edge("A", "B", "operational", authority=authority, confidence=1.0)

    def test_an_edge_needs_both_ends(self):
        with self.assertRaises(ae.EdgeError):
            ae.edge("", "B", "operational", authority="x", confidence=1.0)
        with self.assertRaises(ae.EdgeError):
            ae.edge("A", "", "operational", authority="x", confidence=1.0)

    def test_an_interpretation_cannot_claim_certainty(self):
        # The exact confusion the taxonomy exists to prevent: it would render
        # with the visual weight of canon.
        with self.assertRaises(ae.EdgeError):
            ae.edge("A", "B", "inferred", authority="a layout", confidence=1.0, interpreted=True)
        # Lowered, it is allowed.
        item = ae.edge("A", "B", "inferred", authority="a layout", confidence=0.6, interpreted=True)
        self.assertTrue(item["interpreted"])


class SourceAsymmetryTests(unittest.TestCase):
    """A registry witnesses structure; only the ledger witnesses occurrence."""

    def test_a_registry_may_not_claim_causation_or_chronology(self):
        for edge_type in ae.LEDGER_ONLY_TYPES:
            with self.subTest(edge_type=edge_type):
                with self.assertRaises(ae.EdgeError) as caught:
                    ae.registry_edge("A", "B", edge_type, authority="registry", confidence=1.0)
                self.assertIn("event ledger", str(caught.exception))

    def test_a_registry_may_state_the_structural_types(self):
        for edge_type in ("semantic", "operational", "structural", "inferred"):
            with self.subTest(edge_type=edge_type):
                interpreted = edge_type == "inferred"
                ae.registry_edge("A", "B", edge_type, authority="registry",
                                 confidence=0.5 if interpreted else 1.0,
                                 interpreted=interpreted)

    def test_the_ledger_may_state_causation_chronology_action_and_navigation(self):
        for edge_type in ("causal", "temporal", "operational", "structural"):
            with self.subTest(edge_type=edge_type):
                ae.ledger_edge("A", "B", edge_type, authority="ledger", confidence=1.0)

    def test_the_ledger_may_not_claim_a_canonical_document_relationship(self):
        # `semantic` means the Foundation states it in a document. An event
        # cannot make a document say something.
        for edge_type in ("semantic", "inferred"):
            with self.subTest(edge_type=edge_type):
                with self.assertRaises(ae.EdgeError):
                    ae.ledger_edge("A", "B", edge_type, authority="ledger", confidence=0.5)

    def test_the_council_view_cannot_emit_a_ledger_only_edge(self):
        # The guard reached through the galaxy's own wrapper, not just the
        # taxonomy: this is the regression that would let the registry view
        # start asserting causation.
        galaxy = _load("council_galaxy_prototype.py", "memory_test_galaxy")
        for edge_type in ae.LEDGER_ONLY_TYPES:
            with self.subTest(edge_type=edge_type):
                with self.assertRaises(galaxy.PrototypeError):
                    galaxy.edge("A", "B", edge_type, authority="registry", confidence=1.0)


class SummaryTests(unittest.TestCase):
    def test_the_summary_splits_witnessed_from_interpreted(self):
        edges = [
            ae.edge("A", "B", "operational", authority="r", confidence=1.0),
            ae.edge("B", "C", "structural", authority="layout", confidence=0.0, interpreted=True),
        ]
        summary = ae.summarize(edges)
        self.assertEqual(summary["total"], 2)
        self.assertEqual(summary["canonical"], 1)
        self.assertEqual(summary["interpreted"], 1)
        self.assertEqual(sum(summary["counts"].values()), 2)

    def test_the_summary_reports_every_type_even_at_zero(self):
        summary = ae.summarize([])
        self.assertEqual(set(summary["counts"]), set(ae.EDGE_TYPES))
        self.assertEqual(summary["total"], 0)

    def test_orphans_names_nodes_no_edge_touches(self):
        edges = [ae.edge("A", "B", "operational", authority="r", confidence=1.0)]
        self.assertEqual(ae.orphans(edges, ["A", "B", "C"]), ["C"])
        self.assertEqual(ae.orphans(edges, ["A", "B"]), [])


# --------------------------------------------------------------------------
# resolving an actor
# --------------------------------------------------------------------------

class ActorResolutionTests(unittest.TestCase):
    """Two ratified sources, an exact match in each, and an honest tier."""

    def setUp(self):
        self.index = mem.build_role_index([
            role("AGT-007", "CODEX Engineering Lead"),
            role("AGT-002", "Research Lead"),
        ])

    def test_an_exact_registered_name_resolves_as_a_seat(self):
        found = mem.resolve_actor("CODEX Engineering Lead", self.index)
        self.assertEqual(found["id"], "AGT-007")
        self.assertEqual(found["tier"], "seat")
        self.assertEqual(found["confidence"], 1.0)
        self.assertFalse(found["interpreted"])
        self.assertIn("registered name for this seat", found["basis"])

    def test_a_role_id_resolves_to_itself(self):
        self.assertEqual(mem.resolve_actor("AGT-007", self.index)["id"], "AGT-007")

    def test_a_substring_never_resolves_from_either_source(self):
        # The heart of it: a string coincidence turned into an institutional
        # attribution is indistinguishable from a real one once on screen.
        index = mem.build_role_index(
            [role("AGT-007", "CODEX Engineering Lead")],
            mem.load_entity_registry(VAULT_ROOT))
        for actor in ("Codex Engineering", "Engineering Lead", "Research",
                      "Memory", "Lead"):
            with self.subTest(actor=actor):
                self.assertIsNone(mem.resolve_actor(actor, index))

    def test_a_provider_login_is_not_an_institutional_actor(self):
        index = mem.build_role_index([], mem.load_entity_registry(VAULT_ROOT))
        for actor in ("codex-bot", "github-actions[bot]", "OmSadhiGuru", "CI"):
            with self.subTest(actor=actor):
                self.assertIsNone(mem.resolve_actor(actor, index))

    def test_an_empty_actor_resolves_to_nothing(self):
        self.assertIsNone(mem.resolve_actor("", self.index))
        self.assertIsNone(mem.resolve_actor("   ", self.index))

    def test_a_stated_alias_resolves_as_a_seat(self):
        with patch.dict(mem.ACTOR_ALIASES, {"codex-bot": "CODEX Engineering Lead"}):
            found = mem.resolve_actor("codex-bot", self.index)
        self.assertEqual(found["id"], "AGT-007")
        self.assertIn("stated alias", found["basis"])

    def test_a_stale_alias_is_an_error_not_a_silent_miss(self):
        with patch.dict(mem.ACTOR_ALIASES, {"codex-bot": "A Role That Was Removed"}):
            with self.assertRaises(mem.MemoryError_) as caught:
                mem.resolve_actor("codex-bot", self.index)
        self.assertIn("Repair or remove", str(caught.exception))

    def test_the_shipped_alias_table_is_empty_and_that_is_deliberate(self):
        # The taxonomy supplies ratified names now, so a hand-written alias needs
        # a reason. If this fails, someone added an attribution that should have
        # been a registry entry.
        self.assertEqual(mem.ACTOR_ALIASES, {})

    def test_with_no_source_at_all_nothing_resolves(self):
        empty = mem.build_role_index([], None)
        for actor in ("CODEX Engineering Lead", "LUMIAION", "Founder"):
            with self.subTest(actor=actor):
                self.assertIsNone(mem.resolve_actor(actor, empty))


class RecognisedSeatNameTests(unittest.TestCase):
    """CODEX is a registered seat name now, so it attributes to the seat."""

    def setUp(self):
        self.roles = mem.load_roles(VAULT_ROOT)
        self.registry = mem.load_entity_registry(VAULT_ROOT)
        self.index = mem.build_role_index(self.roles, self.registry)

    def test_codex_resolves_to_its_seat_at_full_confidence(self):
        # Before the registry recognised the name, this resolved to the
        # cognitive function at engine tier, as an interpretation.
        found = mem.resolve_actor("CODEX", self.index)
        self.assertEqual(found["id"], "AGT-007")
        self.assertEqual(found["tier"], "seat")
        self.assertEqual(found["confidence"], 1.0)
        self.assertFalse(found["interpreted"])

    def test_the_seat_outranks_the_engine_citation_for_the_same_name(self):
        # Both sources name CODEX. The Council's own record of its seats is the
        # stronger claim about who acted, so the ladder must not fall through.
        self.assertIsNotNone(self.registry, "the taxonomy must still cite CODEX as an engine")
        self.assertEqual(mem.resolve_actor("CODEX", self.index)["tier"], "seat")

    def test_capitalisation_does_not_change_the_attribution(self):
        # An agent that reports itself as `codex` must not attribute differently
        # from one that reports `CODEX`.
        ids = {mem.resolve_actor(spelling, self.index)["id"]
               for spelling in ("CODEX", "codex", "CoDeX", "  CODEX  ")}
        tiers = {mem.resolve_actor(spelling, self.index)["tier"]
                 for spelling in ("CODEX", "codex", "CoDeX", "  CODEX  ")}
        self.assertEqual(ids, {"AGT-007"})
        self.assertEqual(tiers, {"seat"})

    def test_the_full_title_and_the_id_still_resolve(self):
        for actor in ("CODEX Engineering Lead", "AGT-007", "agt-007"):
            with self.subTest(actor=actor):
                self.assertEqual(mem.resolve_actor(actor, self.index)["id"], "AGT-007")

    def test_a_partial_name_still_identifies_no_seat(self):
        # Recognising a short name must not have loosened matching.
        for actor in ("Codex Engineering", "Engineering Lead", "CODE", "Lead"):
            with self.subTest(actor=actor):
                self.assertIsNone(mem.resolve_actor(actor, self.index))

    def test_a_provider_account_is_still_not_the_seat(self):
        for actor in ("codex-bot", "github-actions[bot]", "OmSadhiGuru"):
            with self.subTest(actor=actor):
                self.assertIsNone(mem.resolve_actor(actor, self.index))

    def test_a_placeholder_cell_never_becomes_a_seat_name(self):
        for actor in ("—", "-", "n/a", "none", "TBD", "pending"):
            with self.subTest(actor=actor):
                self.assertIsNone(mem.resolve_actor(actor, self.index))

    def test_two_seats_claiming_one_name_is_refused_rather_than_ordered(self):
        # Preferring whichever row parsed first would attribute work by accident
        # of document order.
        with self.assertRaises(mem.MemoryError_) as caught:
            mem.build_role_index([
                {"id": "AGT-007", "named_role": "CODEX Engineering Lead",
                 "recognised_names": ["CODEX"]},
                {"id": "AGT-017", "named_role": "Another Lead",
                 "recognised_names": ["codex"]},
            ])
        self.assertIn("cannot identify two seats", str(caught.exception))

    def test_a_recognised_name_may_repeat_within_one_seat(self):
        index = mem.build_role_index([
            {"id": "AGT-007", "named_role": "CODEX Engineering Lead",
             "recognised_names": ["CODEX", "CODEX"]},
        ])
        self.assertEqual(mem.resolve_actor("CODEX", index)["id"], "AGT-007")

    def test_a_seat_with_no_recognised_names_is_unaffected(self):
        by_id = {role["id"]: role for role in self.roles}
        self.assertEqual(by_id["AGT-002"]["recognised_names"], [])
        self.assertEqual(mem.resolve_actor("Research Lead", self.index)["id"], "AGT-002")


class InstitutionalTaxonomyTests(unittest.TestCase):
    """What the Institutional Node Taxonomy adds, and what it refuses to claim."""

    def setUp(self):
        self.registry = mem.load_entity_registry(VAULT_ROOT)
        if self.registry is None:
            self.skipTest("entity registry unavailable in this tree")
        self.index = mem.build_role_index([], self.registry)

    def test_the_names_the_foundation_uses_for_itself_resolve(self):
        # These are why the taxonomy was needed: names the Foundation uses
        # constantly that no Council seat holds.
        for actor, expected in (("LUMIAION", "office:lumiaion"),
                                ("Founder", "person:founder"),
                                ("JERANIUM", "agent:cf-15")):
            with self.subTest(actor=actor):
                found = mem.resolve_actor(actor, self.index)
                self.assertIsNotNone(found, f"{actor} should resolve")
                self.assertEqual(found["id"], expected)
                self.assertEqual(found["tier"], "identity")

    def test_an_identity_match_is_a_full_confidence_claim(self):
        found = mem.resolve_actor("LUMIAION", self.index)
        self.assertEqual(found["confidence"], 1.0)
        self.assertFalse(found["interpreted"])

    def test_an_engine_name_resolves_only_as_a_citation(self):
        # The taxonomy cites CODEX as the engine fulfilling CF-07. It does not
        # say an actor called CODEX *is* CF-07 — engines move between functions.
        found = mem.resolve_actor("CODEX", self.index)
        self.assertIsNotNone(found)
        self.assertEqual(found["tier"], "engine")
        self.assertLess(found["confidence"], 1.0)
        self.assertTrue(found["interpreted"])
        self.assertIn("engine", found["basis"])

    def test_every_engine_tier_match_is_an_interpretation(self):
        for actor in ("CODEX", "Claude", "Gemini", "Perplexity"):
            with self.subTest(actor=actor):
                found = mem.resolve_actor(actor, self.index)
                if found and found["tier"] == "engine":
                    self.assertTrue(found["interpreted"])
                    self.assertLess(found["confidence"], 1.0)

    def test_a_basis_always_names_the_document_conferring_identity(self):
        for actor in ("LUMIAION", "Founder", "CODEX"):
            with self.subTest(actor=actor):
                found = mem.resolve_actor(actor, self.index)
                self.assertTrue(found["basis"].strip())
                self.assertIn(".md", found["basis"])

    def test_a_council_seat_outranks_the_taxonomy(self):
        # Both sources can name the same actor. The Council's own record of its
        # seats is the stronger claim about who acted.
        index = mem.build_role_index([role("AGT-007", "CODEX Engineering Lead")],
                                     self.registry)
        found = mem.resolve_actor("CODEX Engineering Lead", index)
        self.assertEqual(found["tier"], "seat")
        self.assertEqual(found["id"], "AGT-007")

    def test_a_placeholder_is_never_an_actor(self):
        for actor in ("Owner pending", "TBD", "Unappointed"):
            with self.subTest(actor=actor):
                self.assertIsNone(mem.resolve_actor(actor, self.index))


# --------------------------------------------------------------------------
# the graph
# --------------------------------------------------------------------------

class MemoryGraphTests(unittest.TestCase):
    def setUp(self):
        # PR-48's life, as the ledger would hold it.
        self.push = event(entity_type="branch", entity_id="codex/x@aaa", event_id="push-1",
                          event_type="github.push.completed", actor="codex-bot",
                          correlation_id="push-1", occurred_at="2026-09-29T13:50:00+00:00")
        self.commit = event(entity_type="commit", entity_id="aaa111", event_id="commit-1",
                            event_type="github.commit.created", actor="CODEX",
                            correlation_id="push-1", causation_id="push-1",
                            occurred_at="2026-09-29T13:50:30+00:00")
        self.opened = event(event_id="pr-open", occurred_at="2026-09-29T14:00:00+00:00")
        self.ci = event(entity_type="check_run", entity_id="check-901", event_id="ci-1",
                        event_type="github.ci.failed", actor="CI", severity="action",
                        requires_founder=True, occurred_at="2026-09-29T14:19:00+00:00")
        self.merged = event(event_id="pr-merge", event_type="github.pr.merged",
                            severity="update", occurred_at="2026-09-29T15:30:00+00:00")
        self.events = [self.merged, self.ci, self.push, self.opened, self.commit]
        self.roles = [role("AGT-007", "CODEX Engineering Lead")]
        self.graph = mem.build_memory_graph(self.events, self.roles,
                                            now="2026-09-29T16:00:00+00:00")

    def nodes_of(self, kind: str) -> list[dict]:
        return [node for node in self.graph["nodes"] if node["kind"] == kind]

    def edges_of(self, edge_type: str) -> list[dict]:
        return [item for item in self.graph["edges"] if item["type"] == edge_type]

    # -- structure -------------------------------------------------------
    def test_each_entity_appears_once_however_many_events_touched_it(self):
        entity_ids = [node["entity_id"] for node in self.nodes_of("entity")]
        self.assertEqual(sorted(entity_ids),
                         ["PR-48", "aaa111", "check-901", "codex/x@aaa"])

    def test_entity_ids_are_namespaced_so_two_providers_cannot_merge(self):
        for node in self.nodes_of("entity"):
            self.assertTrue(node["id"].startswith("github:"))
        self.assertNotEqual(
            mem.entity_node_id(event(source="notion", entity_id="PR-48")),
            mem.entity_node_id(event(source="github", entity_id="PR-48")),
        )

    def test_no_node_is_orphaned(self):
        self.assertEqual(self.graph["orphans"], [])

    def test_no_edge_is_a_self_loop(self):
        for item in self.graph["edges"]:
            self.assertNotEqual(item["source"], item["target"])

    def test_every_edge_is_witnessed_rather_than_interpreted(self):
        # The ledger only ever reports what it saw, so nothing here is a guess.
        self.assertEqual(self.graph["edge_summary"]["interpreted"], 0)
        self.assertEqual(self.graph["edge_summary"]["canonical"],
                         self.graph["edge_summary"]["total"])

    def test_the_graph_states_that_it_asserts_no_registry_relationship(self):
        self.assertIn("event ledger only", self.graph["authority"])
        self.assertTrue(self.graph["read_only"])

    # -- the entity's own chronology --------------------------------------
    def test_an_entity_carries_its_timeline_in_occurrence_order(self):
        pr = next(n for n in self.nodes_of("entity") if n["entity_id"] == "PR-48")
        self.assertEqual([step["event_type"] for step in pr["timeline"]],
                         ["github.pr.opened", "github.pr.merged"])
        self.assertEqual(pr["event_count"], 2)
        self.assertEqual(pr["first_seen"], "2026-09-29T14:00:00+00:00")
        self.assertEqual(pr["last_seen"], "2026-09-29T15:30:00+00:00")

    def test_a_node_keeps_the_loudest_severity_it_ever_saw(self):
        # A resolved CI failure is still why this entity mattered; showing only
        # the latest severity would erase the reason it needed attention.
        check = next(n for n in self.nodes_of("entity") if n["entity_id"] == "check-901")
        self.assertEqual(check["severity"], "action")
        self.assertTrue(check["requires_founder"])

    def test_an_entitys_attention_flag_survives_a_later_quiet_event(self):
        later = event(entity_type="check_run", entity_id="check-901", event_id="ci-2",
                      event_type="github.ci.succeeded", actor="CI", severity="info",
                      occurred_at="2026-09-29T16:00:00+00:00")
        graph = mem.build_memory_graph(self.events + [later], self.roles)
        check = next(n for n in graph["nodes"] if n.get("entity_id") == "check-901")
        self.assertTrue(check["requires_founder"])
        self.assertEqual(check["severity"], "action")

    # -- causal -----------------------------------------------------------
    def test_causation_is_drawn_between_the_entities_the_events_touched(self):
        causal = self.edges_of("causal")
        self.assertEqual(len(causal), 1)
        self.assertEqual(causal[0]["source"], "github:branch:codex/x@aaa")
        self.assertEqual(causal[0]["target"], "github:commit:aaa111")
        self.assertIn("names", causal[0]["authority"])

    def test_causation_within_one_entity_is_not_drawn_as_an_edge(self):
        chained = event(event_id="pr-merge2", event_type="github.pr.merged",
                        causation_id="pr-open", occurred_at="2026-09-29T15:40:00+00:00")
        graph = mem.build_memory_graph([self.opened, chained], self.roles)
        self.assertEqual([item for item in graph["edges"] if item["type"] == "causal"], [])

    def test_a_dangling_causation_id_produces_no_edge(self):
        orphaned = event(event_id="x-1", causation_id="an-event-not-in-this-ledger",
                         entity_id="PR-99")
        graph = mem.build_memory_graph([orphaned], self.roles)
        self.assertEqual([item for item in graph["edges"] if item["type"] == "causal"], [])

    # -- temporal ---------------------------------------------------------
    def test_sequence_is_drawn_only_inside_one_workflow(self):
        # The push's workflow and the pull request's are separate correlations,
        # so no temporal edge crosses between them: two unrelated things in
        # sequence is a coincidence, not a relationship.
        for item in self.edges_of("temporal"):
            with self.subTest(edge=(item["source"], item["target"])):
                self.assertIn("within", item["authority"])
        crossing = {("github:commit:aaa111", "github:pull_request:PR-48")}
        drawn = {(item["source"], item["target"]) for item in self.edges_of("temporal")}
        self.assertEqual(drawn & crossing, set())

    def test_sequence_defers_to_causation_for_the_same_pair(self):
        # Causation is strictly stronger; drawing both would double the visual
        # weight of one fact.
        causal_pairs = {frozenset((i["source"], i["target"])) for i in self.edges_of("causal")}
        temporal_pairs = {frozenset((i["source"], i["target"])) for i in self.edges_of("temporal")}
        self.assertEqual(causal_pairs & temporal_pairs, set())

    def test_a_workflow_returning_to_an_entity_draws_one_edge_not_two(self):
        # opened(PR-48) -> failed(check) -> merged(PR-48) must not produce a
        # pair of arrows pointing at each other.
        pairs = [(i["source"], i["target"]) for i in self.edges_of("temporal")]
        self.assertEqual(len(pairs), len(set(frozenset(pair) for pair in pairs)))
        self.assertIn(("github:pull_request:PR-48", "github:check_run:check-901"), pairs)
        self.assertNotIn(("github:check_run:check-901", "github:pull_request:PR-48"), pairs)

    # -- who acted --------------------------------------------------------
    def test_an_actor_is_joined_to_every_entity_it_touched(self):
        actions = {(i["source"], i["target"]) for i in self.edges_of("operational")}
        self.assertIn(("actor:CI", "github:check_run:check-901"), actions)
        self.assertIn(("actor:codex-bot", "github:pull_request:PR-48"), actions)

    def test_an_actor_acting_twice_on_one_entity_yields_one_edge(self):
        pairs = [(i["source"], i["target"]) for i in self.edges_of("operational")]
        self.assertEqual(len(pairs), len(set(pairs)))

    def test_an_unresolved_actor_is_never_linked_to_a_council_seat(self):
        # The residue must stay visible. A structural edge to a seat would
        # assert an attribution nobody decided.
        role_ids = {"AGT-007"}
        for item in self.graph["edges"]:
            if item["target"] in role_ids:
                source = next(n for n in self.graph["nodes"] if n["id"] == item["source"])
                with self.subTest(source=source["label"]):
                    self.assertTrue(source["resolved"])

    def test_a_resolved_actor_is_joined_to_its_seat_with_its_basis(self):
        graph = mem.build_memory_graph(
            [event(actor="CODEX Engineering Lead", event_id="e-1")], self.roles)
        seat_edges = [i for i in graph["edges"] if i["target"] == "AGT-007"]
        self.assertEqual(len(seat_edges), 1)
        self.assertIn("registered name for this seat", seat_edges[0]["authority"])
        self.assertEqual(graph["counts"]["actors_resolved"], 1)

    def test_an_engine_tier_resolution_is_drawn_as_an_interpretation(self):
        # The one place in this graph where an edge is not a plain witness: the
        # taxonomy citing an engine for a function does not say the engine is it.
        registry = mem.load_entity_registry(VAULT_ROOT)
        if registry is None:
            self.skipTest("entity registry unavailable in this tree")
        graph = mem.build_memory_graph([event(actor="CODEX", event_id="e-1")], [],
                                       entity_registry=registry)
        seat_edges = [i for i in graph["edges"] if i["target"].startswith("agent:")]
        self.assertEqual(len(seat_edges), 1)
        self.assertTrue(seat_edges[0]["interpreted"])
        self.assertLess(seat_edges[0]["confidence"], 1.0)
        self.assertIn("engines move between functions", seat_edges[0]["note"])

    def test_an_identity_tier_resolution_is_drawn_as_witnessed(self):
        registry = mem.load_entity_registry(VAULT_ROOT)
        if registry is None:
            self.skipTest("entity registry unavailable in this tree")
        graph = mem.build_memory_graph([event(actor="LUMIAION", event_id="e-1")], [],
                                       entity_registry=registry)
        seat_edges = [i for i in graph["edges"] if i["target"].startswith("office:")]
        self.assertEqual(len(seat_edges), 1)
        self.assertFalse(seat_edges[0]["interpreted"])
        self.assertEqual(seat_edges[0]["confidence"], 1.0)

    def test_the_counts_split_resolutions_by_what_entitled_them(self):
        registry = mem.load_entity_registry(VAULT_ROOT)
        if registry is None:
            self.skipTest("entity registry unavailable in this tree")
        graph = mem.build_memory_graph(
            [event(actor="LUMIAION", event_id="e-1"),
             event(actor="CODEX", event_id="e-2", entity_id="PR-49"),
             event(actor="codex-bot", event_id="e-3", entity_id="PR-50")],
            [], entity_registry=registry)
        # "resolved" must never read as one uniform strength.
        self.assertEqual(graph["counts"]["actors_by_tier"], {"identity": 1, "engine": 1})
        self.assertEqual(graph["counts"]["actors_unresolved"], 1)

    def test_the_taxonomy_shrinks_the_residue_without_inventing_anything(self):
        registry = mem.load_entity_registry(VAULT_ROOT)
        if registry is None:
            self.skipTest("entity registry unavailable in this tree")
        without = mem.build_memory_graph(self.events, [])
        with_taxonomy = mem.build_memory_graph(self.events, [], entity_registry=registry)
        self.assertLess(with_taxonomy["counts"]["actors_unresolved"],
                        without["counts"]["actors_unresolved"])
        # Whatever still fails to resolve is genuinely not an institutional actor.
        still = {row["actor"] for row in with_taxonomy["unresolved_actors"]}
        self.assertTrue(still.issubset({"codex-bot", "CI", "github-actions[bot]"}),
                        f"unexpected residue: {still}")

    def test_no_actor_node_leaks_its_internal_resolution_scratch_field(self):
        registry = mem.load_entity_registry(VAULT_ROOT)
        graph = mem.build_memory_graph(self.events, [], entity_registry=registry)
        for node in graph["nodes"]:
            self.assertNotIn("_resolution", node)

    def test_every_actor_node_states_the_tier_that_resolved_it(self):
        registry = mem.load_entity_registry(VAULT_ROOT)
        graph = mem.build_memory_graph(self.events, [], entity_registry=registry)
        for node in graph["nodes"]:
            if node["kind"] != "actor":
                continue
            with self.subTest(actor=node["label"]):
                if node["resolved"]:
                    self.assertIn(node["resolution_tier"], mem.RESOLUTION_TIERS)
                    self.assertTrue(node["resolution_basis"])
                else:
                    self.assertEqual(node["resolution_tier"], "")
                    self.assertEqual(node["resolution_basis"], "")

    def test_the_unresolved_residue_is_reported_with_counts_worst_first(self):
        residue = self.graph["unresolved_actors"]
        self.assertEqual({row["actor"] for row in residue}, {"codex-bot", "CODEX", "CI"})
        counts = [row["event_count"] for row in residue]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(self.graph["counts"]["actors_unresolved"], 3)

    def test_with_no_registry_every_actor_is_unresolved_and_the_graph_still_builds(self):
        graph = mem.build_memory_graph(self.events, roles=[])
        self.assertEqual(graph["counts"]["actors_resolved"], 0)
        self.assertGreater(graph["counts"]["entities"], 0)
        self.assertEqual(graph["orphans"], [])

    # -- counts and emptiness ---------------------------------------------
    def test_the_counts_describe_the_graph(self):
        counts = self.graph["counts"]
        self.assertEqual(counts["events"], 5)
        self.assertEqual(counts["entities"], 4)
        self.assertEqual(counts["actors"], 3)
        self.assertEqual(counts["requires_founder"], 1)

    def test_an_empty_ledger_produces_an_honest_empty_graph(self):
        graph = mem.build_memory_graph([], self.roles)
        self.assertEqual(graph["nodes"], [])
        self.assertEqual(graph["edges"], [])
        self.assertEqual(graph["counts"]["events"], 0)
        self.assertEqual(graph["unresolved_actors"], [])
        self.assertEqual(graph["orphans"], [])

    def test_the_graph_never_mutates_the_events_it_reads(self):
        snapshot = json.dumps(self.events, sort_keys=True)
        mem.build_memory_graph(self.events, self.roles)
        self.assertEqual(json.dumps(self.events, sort_keys=True), snapshot)

    def test_the_graph_is_stable_across_input_order(self):
        forward = mem.build_memory_graph(self.events, self.roles, now="2026-09-29T16:00:00+00:00")
        backward = mem.build_memory_graph(list(reversed(self.events)), self.roles,
                                          now="2026-09-29T16:00:00+00:00")
        self.assertEqual([n["id"] for n in forward["nodes"]],
                         [n["id"] for n in backward["nodes"]])
        self.assertEqual(sorted((i["source"], i["target"], i["type"]) for i in forward["edges"]),
                         sorted((i["source"], i["target"], i["type"]) for i in backward["edges"]))


class ThoughtPathTests(unittest.TestCase):
    def setUp(self):
        self.events = [
            event(event_id="pr-open"),
            event(entity_type="check_run", entity_id="check-901", event_id="ci-1",
                  event_type="github.ci.failed", actor="CI",
                  occurred_at="2026-09-29T14:19:00+00:00"),
            event(entity_type="review", entity_id="PR-48-review-1", event_id="rev-1",
                  event_type="github.review.approved", actor="Founder",
                  occurred_at="2026-09-29T15:00:00+00:00"),
        ]
        self.graph = mem.build_memory_graph(self.events, [])

    def test_a_path_walks_outward_breadth_first(self):
        path = mem.thought_path(self.graph, "github:pull_request:PR-48", depth=2)
        depths = [step["depth"] for step in path["steps"]]
        self.assertEqual(depths, sorted(depths))
        self.assertGreater(path["reachable"], 0)

    def test_each_step_names_the_relationship_it_travelled(self):
        path = mem.thought_path(self.graph, "github:pull_request:PR-48", depth=2)
        for step in path["steps"]:
            self.assertIn(step["via"], ae.EDGE_TYPES)
            self.assertTrue(step["authority"])
            self.assertIn("interpreted", step)

    def test_the_depth_bound_is_respected(self):
        shallow = mem.thought_path(self.graph, "github:pull_request:PR-48", depth=1)
        deeper = mem.thought_path(self.graph, "github:pull_request:PR-48", depth=3)
        self.assertTrue(all(step["depth"] == 1 for step in shallow["steps"]))
        self.assertGreaterEqual(len(deeper["steps"]), len(shallow["steps"]))

    def test_a_depth_of_zero_returns_no_steps(self):
        path = mem.thought_path(self.graph, "github:pull_request:PR-48", depth=0)
        self.assertEqual(path["steps"], [])

    def test_no_node_is_visited_twice(self):
        path = mem.thought_path(self.graph, "github:pull_request:PR-48", depth=5)
        visited = [step["to"] for step in path["steps"]]
        self.assertEqual(len(visited), len(set(visited)))

    def test_an_unknown_node_is_an_error_rather_than_an_empty_path(self):
        with self.assertRaises(mem.MemoryError_):
            mem.thought_path(self.graph, "github:pull_request:PR-999")

    def test_the_path_is_traversable_in_both_directions_along_an_edge(self):
        # An edge is directed for meaning, not for navigation: the Founder can
        # arrive at a check run from its pull request and go back again.
        forward = mem.thought_path(self.graph, "github:pull_request:PR-48", depth=1)
        backward = mem.thought_path(self.graph, "github:check_run:check-901", depth=1)
        self.assertTrue(any(step["to"] == "github:check_run:check-901"
                            for step in forward["steps"]))
        self.assertTrue(any(step["to"] == "github:pull_request:PR-48"
                            for step in backward["steps"]))


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.ledger_path = Path(self.tmp.name) / "ledger.jsonl"
        ledger = ev.EventLedger(self.ledger_path)
        ledger.append(event(event_id="pr-open", provider_event_id="pr:48:opened"))
        ledger.append(event(entity_type="check_run", entity_id="check-901", event_id="ci-1",
                            event_type="github.ci.failed", actor="CI", severity="action",
                            requires_founder=True, provider_event_id="check:901",
                            occurred_at="2026-09-29T14:19:00+00:00"))

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *args) -> tuple[int, str, str]:
        import contextlib
        import io
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = mem.main(["--ledger", str(self.ledger_path), *args])
        return code, out.getvalue(), err.getvalue()

    def test_view_emits_valid_json(self):
        code, out, _ = self.run_cli("view")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["counts"]["events"], 2)

    def test_the_report_names_the_unrecognized_actors_honestly(self):
        code, out, _ = self.run_cli("report")
        self.assertEqual(code, 0)
        self.assertIn("ACTORS NO RATIFIED REGISTRY NAMES", out)
        self.assertIn("honest state", out)
        # And says what it checked, so "unresolved" is not mistaken for "unchecked".
        self.assertIn("Institutional Node Taxonomy", out)

    def test_the_report_marks_what_awaits_the_founder(self):
        _, out, _ = self.run_cli("report")
        self.assertIn("awaiting the Founder", out)

    def test_nodes_lists_ids_usable_with_path(self):
        _, out, _ = self.run_cli("nodes")
        self.assertIn("github:pull_request:PR-48", out)

    def test_path_walks_from_a_listed_node(self):
        code, out, _ = self.run_cli("path", "github:pull_request:PR-48")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["start"], "github:pull_request:PR-48")

    def test_an_unknown_node_exits_non_zero_with_a_reason(self):
        code, _, err = self.run_cli("path", "github:pull_request:PR-999")
        self.assertEqual(code, 2)
        self.assertIn("No node", err)

    def test_an_absent_ledger_reports_an_empty_graph_rather_than_failing(self):
        # The graph must be inspectable on a machine where nothing has happened.
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = mem.main(["--ledger", str(Path(self.tmp.name) / "nope.jsonl"), "view"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out.getvalue())["counts"]["events"], 0)


class NoWriteTests(unittest.TestCase):
    def identifiers(self, filename: str) -> set[str]:
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
        return names

    def test_the_memory_graph_writes_nothing_at_all(self):
        # Derived and disposable by construction: the graph is rebuilt from the
        # ledger on every call and has nowhere to persist an opinion.
        names = self.identifiers("alpha_memory.py")
        for writer in ("write_text", "write_bytes", "write_json_atomic", "mkstemp"):
            with self.subTest(writer=writer):
                self.assertNotIn(writer, names)

    def test_the_memory_graph_cannot_reach_the_founder_state_engine(self):
        self.assertNotIn("founder_os", self.identifiers("alpha_memory.py"))

    def test_the_taxonomy_module_reads_and_writes_nothing(self):
        names = self.identifiers("alpha_edges.py")
        for forbidden in ("open", "Path", "write_text", "environ", "urlopen"):
            self.assertNotIn(forbidden, names)


if __name__ == "__main__":
    unittest.main(verbosity=2)
