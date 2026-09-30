#!/usr/bin/env python3
"""The memory graph — the event ledger as a navigable temporal structure.

The Council galaxy shows who exists. This shows what happened, and joins the
two: an entity the Foundation has observed (a pull request, a commit, a check
run) becomes a node, the actor who touched it becomes a node, and the ledger's
own causation and chronology become edges.

This is the half of Memory that `Alpha Proxima Live Integration Layer` §13 calls
temporal. Selecting `PR-48` and seeing that CODEX opened it, that CI failed on
it, and that a review was then requested is one traversal of this graph rather
than four queries.

## Why this module is the only one allowed to emit causal and temporal edges

A registry can tell you that two roles share an owner. It cannot tell you that
one thing caused another, because causation is an occurrence and a registry
witnesses structure. `alpha_edges.ledger_edge` enforces that asymmetry: the
galaxy builds through `registry_edge` and is refused those two types outright,
and everything here builds through `ledger_edge`.

## The honesty problem this module actually has

Events name their actor as the provider knows them — `codex-bot`, `CI`,
`Founder`. The Council knows its members as registry roles — `AGT-007`,
`CODEX Engineering Lead`. Joining the two is where a memory graph would most
easily start lying: matching `codex-bot` to `CODEX Engineering Lead` because
both contain "codex" would fabricate an institutional attribution from a string
coincidence, and it would look identical to a real one.

So the join is exact, and the residue is visible. An actor is linked to a
Council role only by an exact match on the role's registered name, or by an
explicit alias this module states and a reader can audit. Every other actor
becomes an unresolved node, counted and reported. Today that residue is most of
them — which is the true state of a Foundation whose Council does not yet report
its own activity, and is worth seeing rather than smoothing over.

Standard library only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Iterable

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent

sys.path.insert(0, str(TOOLKIT_DIR))
import alpha_edges as ae  # noqa: E402
import alpha_events as ev  # noqa: E402

MEMORY_SCHEMA_VERSION = "1.0.0"

# Node kinds this graph places. `entity` is a thing the Foundation observed;
# `actor` is who acted; `role` is a Council seat an actor resolved to.
NODE_KINDS = ("entity", "actor", "role")

# Actors whose Council identity is *stated*, not guessed. Each entry is a claim
# a reader can check against the registry, and the list is deliberately short:
# an alias table is where a fabricated attribution would hide, so it holds only
# mappings the Foundation has actually decided.
#
# `Founder` and `CI` are intentionally absent. The Founder is not a Council
# role, and CI is not a person — attaching either to a seat would misrepresent
# the registry rather than enrich it.
ACTOR_ALIASES: dict[str, str] = {}


class MemoryError_(Exception):
    """Raised when the memory graph cannot be built."""


def _load_sibling(filename: str, name: str):
    path = (TOOLKIT_DIR / filename).resolve()
    if not path.exists():
        raise MemoryError_(f"Required toolkit module not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise MemoryError_(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# --------------------------------------------------------------------------
# resolving an actor to a Council seat
# --------------------------------------------------------------------------

# A resolution's strength, and what each tier is allowed to claim.
#
#   seat       The Agent and Subagent Registry names this actor as a role. The
#              Council's own record of who it has; nothing is stronger.
#   identity   The Institutional Node Taxonomy names this actor outright — its
#              label, its code, its identifier. A ratified institutional actor.
#   engine     The taxonomy cites this name only as an *engine* fulfilling a
#              cognitive function. Engines move between functions and labels do
#              not, so "the actor called CODEX did this" is not the same claim as
#              "CF-07 did this". It resolves, and it resolves weakly, and the
#              edge it produces says so.
RESOLUTION_TIERS = {
    "seat": {"confidence": 1.0, "interpreted": False},
    "identity": {"confidence": 1.0, "interpreted": False},
    "engine": {"confidence": 0.5, "interpreted": True},
}


def build_role_index(roles: Iterable[dict[str, Any]] = (),
                     entity_registry: dict[str, Any] | None = None) -> dict[str, Any]:
    """The identity index an actor is resolved against.

    Two sources, consulted in order of what they entitle a claim to be:

      * the **Agent and Subagent Registry**, via `roles` — the Council's own
        record of its seats, matched on the exact registered name;
      * the **Institutional Node Taxonomy**, via `entity_registry` — 42 typed
        actors derived from registries the Foundation has ratified, which is what
        lets `LUMIAION`, `JERANIUM` and `Founder` resolve at all. They are names
        the Foundation uses constantly and that no Council seat holds.

    Both are exact. Neither does substring or fuzzy matching, because a string
    coincidence turned into an institutional attribution is indistinguishable
    from a real one once it is on screen.
    """
    # Keyed on the casefolded name. The Institutional Node Taxonomy already
    # matches case-insensitively, and a seat that answered to `CODEX` but not
    # `codex` would attribute the same actor at two different tiers depending on
    # how it happened to capitalise itself. Case is not semantic in a name;
    # exactness is about the whole string, not its casing.
    seats: dict[str, str] = {}

    def register(name: str, role_id: str) -> None:
        key = str(name or "").strip().casefold()
        if not key:
            return
        existing = seats.get(key)
        if existing and existing != role_id:
            # Two seats answering to one name is an identity collision the
            # registry has to resolve. Silently preferring either would
            # attribute work to whichever row happened to parse first.
            raise MemoryError_(
                f"The registry recognises {name!r} for both {existing} and {role_id}. "
                "One name cannot identify two seats — repair the Recognised names column."
            )
        seats[key] = role_id

    for role in roles:
        register(role.get("named_role") or "", role["id"])
        register(role["id"], role["id"])
        # Short names the registry recognises for the seat. An agent reports
        # itself as `CODEX`, not as `CODEX Engineering Lead`, and attribution
        # should not depend on the agent knowing its own full registry title.
        # Still exact: the registry states these names, this does not infer them.
        for recognised in role.get("recognised_names") or []:
            register(recognised, role["id"])
    return {"seats": seats, "entities": entity_registry}


def load_entity_registry(root: Path) -> dict[str, Any] | None:
    """The Institutional Node Taxonomy, or None when it cannot be read.

    Absence is survivable and reported: without it, the names the Foundation uses
    for itself do not resolve and the residue grows. That is a smaller failure
    than guessing.
    """
    try:
        module = _load_sibling("entity_registry.py", "alpha_memory_entity_registry")
    except (MemoryError_, OSError):
        return None
    try:
        return module.build(root)
    except (module.EntityError, OSError, KeyError, ValueError):
        # A root without the ratified registries — a test fixture, a partial
        # checkout — has no taxonomy to offer. Every actor then falls to the
        # residue, which is reported. Refusing to build the graph at all would
        # be a worse answer than building it with fewer attributions.
        return None


def _entity_tier(registry: dict[str, Any], entity_id: str, reference: str) -> str:
    """Whether `reference` is the entity's own name or merely an engine it cites."""
    module = sys.modules.get("alpha_memory_entity_registry")
    normalize = module.normalize if module else (lambda value: value.strip().lower())
    record = next((item for item in registry["entities"]
                   if item["entity_id"] == entity_id), None)
    if record is None:
        return "identity"
    key = normalize(reference)
    if key in {normalize(alias) for alias in record.get("aliases", [])}:
        return "identity"
    if key in {normalize(alias) for alias in record.get("secondary_aliases", [])}:
        return "engine"
    # Resolved through a derived form (a CF code, or a parenthetical stripped).
    # The taxonomy's own machinery got there, so it is an identity claim.
    return "identity"


def resolve_actor(actor: str, index: dict[str, Any]) -> dict[str, Any] | None:
    """Resolve an event's actor to an institutional identity, or decline.

    Returns a record carrying the id, the record that supports it, the tier, and
    how much that tier entitles the claim to weigh — or None, which is a real
    answer and the common one. `codex-bot` and `github-actions[bot]` are a GitHub
    login and a CI runner; neither is an institutional actor, and inventing one
    for them would be the fabrication this whole module is arranged to avoid.
    """
    name = (actor or "").strip()
    if not name:
        return None

    seats = index.get("seats") or {}
    seat_id = seats.get(name.casefold())
    if seat_id:
        return {
            "id": seat_id, "tier": "seat",
            "basis": "Agent and Subagent Registry — registered name for this seat",
            **RESOLUTION_TIERS["seat"],
        }

    if name in ACTOR_ALIASES:
        target = ACTOR_ALIASES[name]
        if target.casefold() in seats:
            return {
                "id": seats[target.casefold()], "tier": "seat",
                "basis": f"stated alias: {name} is {target}",
                **RESOLUTION_TIERS["seat"],
            }
        raise MemoryError_(
            f"ACTOR_ALIASES maps {name!r} to {target!r}, which is not in the registry. "
            "Repair or remove the alias rather than letting it resolve to nothing."
        )

    registry = index.get("entities")
    if registry:
        module = sys.modules.get("alpha_memory_entity_registry")
        if module is not None:
            found = module.resolve(registry, name)
            if found:
                tier = _entity_tier(registry, found, name)
                record = next((item for item in registry["entities"]
                               if item["entity_id"] == found), {})
                basis = (
                    f"{record.get('canonical_source', 'Institutional Node Taxonomy')} — "
                    + ("names this actor" if tier == "identity"
                       else f"cites {name} as an engine fulfilling this function")
                )
                return {"id": found, "tier": tier, "basis": basis,
                        **RESOLUTION_TIERS[tier]}
    return None


# --------------------------------------------------------------------------
# the graph
# --------------------------------------------------------------------------

def entity_node_id(event: dict[str, Any]) -> str:
    """A stable node id for an entity, namespaced by source.

    `PR-48` from GitHub and `PR-48` from some future provider are different
    things; namespacing keeps a later adapter from silently merging them.
    """
    return f"{event['source']}:{event['entity_type']}:{event['entity_id']}"


def actor_node_id(actor: str) -> str:
    return f"actor:{actor}"


def build_memory_graph(events: Iterable[dict[str, Any]],
                       roles: Iterable[dict[str, Any]] = (),
                       now: str | None = None,
                       entity_registry: dict[str, Any] | None = None) -> dict[str, Any]:
    """Turn the event ledger into nodes and typed, attributed edges.

    Four kinds of relationship come out, and every one of them is something the
    ledger witnessed rather than something this function decided:

      * **temporal** — two *different* entities observed one after the other
        inside one workflow. "The check ran after the pull request opened."
        An entity's own chronology is not an edge: a self-loop cannot be walked
        and tells a renderer nothing, so it lives on the node as `timeline`.
      * **causal** — B names A as its cause. Drawn between the *entities* the
        two events touch, so the graph shows that a push led to a CI failure
        rather than merely that two event records are linked.
      * **operational** — an actor acted on an entity. Witnessed, not inferred.
      * **structural** — an actor the registry does not know, joined to the
        graph only so it is reachable, and marked as carrying no claim.

    Nothing here writes. The ledger is read once and the graph is derived; call
    it again and it reflects the ledger at that instant.
    """
    ordered = ev.sort_events(events)
    role_index = build_role_index(roles, entity_registry)

    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, Any]] = []
    stamp = now or ae.now_iso()

    # -- nodes ----------------------------------------------------------
    by_entity: dict[str, list[dict[str, Any]]] = {}
    unresolved_actors: dict[str, int] = {}

    for event in ordered:
        node_id = entity_node_id(event)
        entry = nodes.setdefault(node_id, {
            "id": node_id,
            "kind": "entity",
            "entity_type": event["entity_type"],
            "entity_id": event["entity_id"],
            "source": event["source"],
            "label": event["entity_id"],
            "department": event["department"],
            "first_seen": event["occurred_at"],
            "last_seen": event["occurred_at"],
            "event_count": 0,
            # The entity's own chronology. On the node rather than as a
            # self-loop edge: "PR-48 changed three times" is a property of
            # PR-48, and a line from a node to itself is unwalkable.
            "timeline": [],
            "requires_founder": False,
            "latest_title": "",
            "latest_event_type": "",
            "deep_link": "",
            "severity": "info",
        })
        entry["last_seen"] = event["occurred_at"]
        entry["event_count"] += 1
        entry["timeline"].append({
            "occurred_at": event["occurred_at"],
            "event_type": event["event_type"],
            "actor": event["actor"],
            "severity": event["severity"],
            "title": event["title"],
            "event_id": event["event_id"],
        })
        entry["requires_founder"] = entry["requires_founder"] or event["requires_founder"]
        entry["latest_title"] = event["title"]
        entry["latest_event_type"] = event["event_type"]
        entry["deep_link"] = event["deep_link"] or entry["deep_link"]
        # The node carries the loudest severity it has ever seen, not the most
        # recent: a resolved CI failure is still why this entity mattered.
        if ev.SEVERITY_RANK[event["severity"]] > ev.SEVERITY_RANK[entry["severity"]]:
            entry["severity"] = event["severity"]
        by_entity.setdefault(node_id, []).append(event)

        actor = event["actor"]
        actor_id = actor_node_id(actor)
        resolution = resolve_actor(actor, role_index)
        actor_entry = nodes.setdefault(actor_id, {
            "id": actor_id,
            "kind": "actor",
            "label": actor,
            "source": event["source"],
            "department": event["department"],
            "role_id": resolution["id"] if resolution else None,
            "resolution_basis": resolution["basis"] if resolution else "",
            # Which record entitled the match, so an interface can weigh it. An
            # `engine` resolution is a citation, not an identity.
            "resolution_tier": resolution["tier"] if resolution else "",
            "resolved": resolution is not None,
            "event_count": 0,
            "first_seen": event["occurred_at"],
            "last_seen": event["occurred_at"],
        })
        actor_entry["event_count"] += 1
        actor_entry["last_seen"] = event["occurred_at"]
        actor_entry["_resolution"] = resolution
        if resolution is None:
            unresolved_actors[actor] = unresolved_actors.get(actor, 0) + 1

    # -- causal edges: between the entities two linked events touch ------
    by_event_id = {event["event_id"]: event for event in ordered}
    for event in ordered:
        cause = by_event_id.get(event.get("causation_id") or "")
        if cause is None:
            continue
        source_node, target_node = entity_node_id(cause), entity_node_id(event)
        if source_node == target_node:
            # Same entity: its `timeline` already records the sequence, and a
            # self-loop would be an unwalkable line repeating it.
            continue
        edges.append(ae.ledger_edge(
            source_node, target_node, "causal",
            authority=f"event ledger — {event['event_id']} names {cause['event_id']} as its cause",
            confidence=1.0,
            note=f"{cause['event_type']} caused {event['event_type']}",
            created_at=stamp,
        ))

    # -- temporal edges: what followed what, inside one workflow ---------
    # Scoped to a correlation group rather than drawn across the whole ledger.
    # Two unrelated things happening in sequence is a coincidence, not a
    # relationship; two things in one workflow happening in sequence is the order
    # the workflow ran, which the ledger genuinely witnessed.
    #
    # Two suppressions keep the picture from overstating itself:
    #
    #   * a pair already joined by a causal edge gets no temporal one, because
    #     causation is strictly stronger than sequence and drawing both would
    #     double the weight of one fact;
    #   * a pair is drawn once, in the direction it was first observed. A
    #     workflow that returns to an entity (opened, checked, then merged) would
    #     otherwise produce two arrows pointing at each other, which reads as a
    #     contradiction. The return visit is already legible in that entity's own
    #     `timeline`.
    causal_pairs = {frozenset((item["source"], item["target"])) for item in edges
                    if item["type"] == "causal"}
    drawn_pairs: set[frozenset[str]] = set()

    by_correlation: dict[str, list[dict[str, Any]]] = {}
    for event in ordered:
        by_correlation.setdefault(event["correlation_id"], []).append(event)

    for correlation_id, group in by_correlation.items():
        sequence: list[tuple[str, dict[str, Any]]] = []
        for event in group:
            node_id = entity_node_id(event)
            if not sequence or sequence[-1][0] != node_id:
                sequence.append((node_id, event))
        for (earlier_node, earlier), (later_node, later) in zip(sequence, sequence[1:]):
            pair = frozenset((earlier_node, later_node))
            if earlier_node == later_node or pair in causal_pairs or pair in drawn_pairs:
                continue
            drawn_pairs.add(pair)
            edges.append(ae.ledger_edge(
                earlier_node, later_node, "temporal",
                authority=(
                    f"event ledger — within {correlation_id}, {earlier['event_type']} "
                    f"was observed before {later['event_type']}"
                ),
                confidence=1.0,
                note=f"{earlier['occurred_at']} -> {later['occurred_at']}",
                created_at=stamp,
            ))
    # -- who acted on what ----------------------------------------------
    seen_action: set[tuple[str, str]] = set()
    for event in ordered:
        pair = (actor_node_id(event["actor"]), entity_node_id(event))
        if pair in seen_action:
            continue
        seen_action.add(pair)
        edges.append(ae.ledger_edge(
            pair[0], pair[1], "operational",
            authority=f"event ledger — {event['actor']} acted on {event['entity_id']}",
            confidence=1.0,
            note=event["event_type"],
            created_at=stamp,
        ))

    # -- unresolved actors, connected but making no claim ----------------
    # An actor the registry does not know still has to be reachable. A
    # `structural` edge to its Council seat would assert an attribution nobody
    # decided, so the node is instead left joined only by the operational edges
    # above — which are witnessed — and the residue is reported rather than
    # papered over.
    resolved_links = 0
    by_tier: dict[str, int] = {}
    for node in nodes.values():
        if node["kind"] != "actor":
            continue
        resolution = node.pop("_resolution", None)
        if resolution is None:
            continue
        resolved_links += 1
        by_tier[resolution["tier"]] = by_tier.get(resolution["tier"], 0) + 1
        # The edge inherits the tier's weight. An `engine` match is drawn as an
        # interpretation, because the taxonomy citing CODEX as the engine behind
        # CF-07 does not say that an actor called CODEX *is* CF-07 — engines move
        # between functions, and `alpha_edges` refuses a confident interpretation.
        edges.append(ae.ledger_edge(
            node["id"], resolution["id"], "operational",
            authority=resolution["basis"],
            confidence=resolution["confidence"],
            interpreted=resolution["interpreted"],
            note=("this actor holds that institutional identity"
                  if resolution["tier"] != "engine"
                  else "the taxonomy cites this name as an engine fulfilling that "
                       "function; engines move between functions"),
            created_at=stamp,
        ))

    for node in nodes.values():
        node.pop("_resolution", None)

    summary = ae.summarize(edges)
    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "generated_at": stamp,
        "read_only": True,
        "authority": "event ledger only; no registry relationship is asserted here",
        "nodes": sorted(nodes.values(), key=lambda node: (node["kind"], node["id"])),
        "edges": edges,
        "edge_summary": summary,
        "counts": {
            "events": len(ordered),
            "entities": sum(1 for node in nodes.values() if node["kind"] == "entity"),
            "actors": sum(1 for node in nodes.values() if node["kind"] == "actor"),
            "actors_resolved": resolved_links,
            "actors_unresolved": len(unresolved_actors),
            # Split by what entitled each match, so "resolved" is never read as
            # one uniform strength.
            "actors_by_tier": by_tier,
            "requires_founder": sum(1 for node in nodes.values()
                                    if node["kind"] == "entity" and node["requires_founder"]),
        },
        # The honest residue: who the Council does not recognize, and how often
        # they acted. An empty ledger makes this empty; a Council that never
        # reports its own work makes it long.
        "unresolved_actors": [
            {"actor": actor, "event_count": count}
            for actor, count in sorted(unresolved_actors.items(),
                                       key=lambda item: (-item[1], item[0]))
        ],
        "orphans": ae.orphans(edges, (node["id"] for node in nodes.values())),
    }


def thought_path(graph: dict[str, Any], start_id: str, depth: int = 3) -> dict[str, Any]:
    """Walk outward from one node, returning the reachable trail.

    This is the data behind the spatial view's `thoughtPath`: given a node, what
    can the Founder travel to, and along which kind of relationship. Breadth
    first, so the nearest relationships come first, and bounded because a
    thought path is a route rather than the whole graph.
    """
    by_id = {node["id"]: node for node in graph["nodes"]}
    if start_id not in by_id:
        raise MemoryError_(f"No node {start_id!r} in this graph.")
    adjacency: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    for item in graph["edges"]:
        if item["source"] == item["target"]:
            continue  # nothing to travel to
        adjacency.setdefault(item["source"], []).append((item["target"], item))
        adjacency.setdefault(item["target"], []).append((item["source"], item))

    seen = {start_id}
    frontier = [start_id]
    steps: list[dict[str, Any]] = []
    for level in range(1, max(0, depth) + 1):
        following: list[str] = []
        for node_id in frontier:
            for neighbour, item in adjacency.get(node_id, []):
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                following.append(neighbour)
                steps.append({
                    "depth": level,
                    "from": node_id,
                    "to": neighbour,
                    "via": item["type"],
                    "authority": item["authority"],
                    "interpreted": item["interpreted"],
                    "label": by_id[neighbour]["label"],
                })
        frontier = following
        if not frontier:
            break
    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "start": start_id,
        "label": by_id[start_id]["label"],
        "depth": depth,
        "steps": steps,
        "reachable": len(seen) - 1,
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def load_roles(root: Path) -> list[dict[str, Any]]:
    """The Council roles, or an empty list when the registry cannot be read.

    A missing registry means every actor is unresolved, which the graph reports
    honestly. It is not a reason to refuse to draw the ledger.
    """
    try:
        role_registry = _load_sibling("role_registry.py", "alpha_memory_role_registry")
        return role_registry.load_roles(root)["roles"]
    except (MemoryError_, OSError, KeyError, ValueError):
        return []


def render_report(graph: dict[str, Any]) -> str:
    """The graph as a terminal reading, shaped for a permanent note."""
    counts = graph["counts"]
    lines = [
        f"MEMORY GRAPH — {counts['events']} event(s) over {counts['entities']} entity(ies)",
        "",
        f"  authority   {graph['authority']}",
        f"  actors      {counts['actors']} ({counts['actors_resolved']} resolved, "
        f"{counts['actors_unresolved']} not)"
        + (f" — {', '.join(f'{n} by {tier}' for tier, n in sorted(counts['actors_by_tier'].items()))}"
           if counts.get("actors_by_tier") else ""),
        f"  attention   {counts['requires_founder']} entity(ies) awaiting the Founder",
        "",
    ]
    summary = graph["edge_summary"]
    lines.append("  " + ", ".join(
        f"{summary['counts'][kind]} {kind}" for kind in ae.EDGE_TYPES if summary["counts"][kind]
    ) or "  no edges")
    lines.append(f"  {summary['canonical']} of {summary['total']} edge(s) witnessed, "
                 f"{summary['interpreted']} interpreted")
    lines.append("")

    entities = [node for node in graph["nodes"] if node["kind"] == "entity"]
    if entities:
        lines.append("  ENTITIES")
        for node in sorted(entities, key=lambda n: n["last_seen"], reverse=True):
            mark = " *" if node["requires_founder"] else "  "
            lines.append(
                f"   {mark} {node['label']:<16} {node['entity_type']:<13} "
                f"{node['event_count']:>3} event(s)  {node['latest_event_type']}"
            )
        lines.append("")

    actors = [node for node in graph["nodes"] if node["kind"] == "actor"]
    resolved = [node for node in actors if node["resolved"]]
    if resolved:
        lines.append("  ATTRIBUTED ACTORS")
        for node in sorted(resolved, key=lambda n: (n["resolution_tier"], n["label"])):
            mark = "~" if node["resolution_tier"] == "engine" else " "
            lines.append(
                f"    {mark} {node['label']:<22} {node['role_id']:<22} "
                f"{node['resolution_tier']}"
            )
        if any(node["resolution_tier"] == "engine" for node in resolved):
            lines.append("")
            lines.append("  ~ resolved only as an engine the taxonomy cites for that function.")
            lines.append("    Engines move between functions, so this is a citation rather than")
            lines.append("    an identity, and its edge is drawn as an interpretation.")
        lines.append("")

    if graph["unresolved_actors"]:
        lines.append("  ACTORS NO RATIFIED REGISTRY NAMES")
        for row in graph["unresolved_actors"]:
            lines.append(f"      {row['actor']:<24} {row['event_count']:>3} event(s)")
        lines.append("")
        lines.append("  These acted on the Foundation and match neither a Council seat nor the")
        lines.append("  Institutional Node Taxonomy. A GitHub login and a CI runner are not")
        lines.append("  institutional actors, so attribution stops at the provider's name —")
        lines.append("  which is the honest state, not a defect to smooth over.")
    if graph["orphans"]:
        lines.append("")
        lines.append(f"  ORPHANED NODES: {', '.join(graph['orphans'])}")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ap.py memory", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT), help="Vault root, for the role registry.")
    parser.add_argument("--ledger", default=str(ev.DEFAULT_LEDGER), help="Event ledger (JSONL).")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("report", help="Read the memory graph in the terminal.")
    sub.add_parser("view", help="Print the memory graph as JSON.")

    path = sub.add_parser("path", help="Walk outward from one node.")
    path.add_argument("node_id", help="A node id, e.g. github:pull_request:PR-48.")
    path.add_argument("--depth", type=int, default=3)

    sub.add_parser("nodes", help="List node ids, for use with `path`.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()

    try:
        events = ev.EventLedger(args.ledger).events()
        graph = build_memory_graph(events, load_roles(root),
                                   entity_registry=load_entity_registry(root))

        if args.command == "view":
            print(json.dumps(graph, indent=2, ensure_ascii=False))
            return 0
        if args.command == "report":
            print(render_report(graph), end="")
            return 0
        if args.command == "nodes":
            for node in graph["nodes"]:
                print(f"{node['id']:<48} {node['kind']:<8} {node['label']}")
            return 0
        if args.command == "path":
            print(json.dumps(thought_path(graph, args.node_id, args.depth),
                             indent=2, ensure_ascii=False))
            return 0
    except (MemoryError_, ae.EdgeError, ev.EventError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
