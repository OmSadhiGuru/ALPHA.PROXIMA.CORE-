#!/usr/bin/env python3
"""The Foundation's one relationship taxonomy.

Two views now draw lines between nodes: the Council galaxy, which reads the role
registry, and the memory graph, which reads the event ledger. They must mean the
same thing by a line, or the Founder learns two visual languages and trusts the
wrong one.

So the taxonomy lives here rather than in either view. This module owns the six
edge types, the builder that stamps provenance onto every edge, and the summary
that says how much of a graph is interpretation. It reads nothing and writes
nothing — it has no registry, no ledger, and no state.

## The six types, and why the distinctions are load-bearing

    semantic     Canonical. The Foundation states this relationship in a
                 document or a record. The strongest claim a line can make.
    operational  A registry or a ledger states it: ownership, assignment,
                 an actor having acted on a thing.
    causal       One event caused another. Only the event ledger can create
                 these, because only it witnesses causation.
    temporal     The same entity, observed at two instants. Also ledger-only.
    structural   Navigation only. Carries no institutional claim whatsoever —
                 it exists so a node is reachable, and it says so.
    inferred     A view assigned it. Never canonical, always marked.

`interpreted` is orthogonal to the type and matters more than it: it is true
whenever any part of an edge was decided by the view rather than read from a
record. A renderer keys its visual grammar off that flag, so an inference cannot
look like canon whatever else it claims to be.

Standard library only.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

EDGE_TYPES = ("semantic", "operational", "causal", "temporal", "structural", "inferred")

# The types only the event ledger may produce. A view that reads a registry and
# emits one of these is claiming to have witnessed something it cannot have.
LEDGER_ONLY_TYPES = ("causal", "temporal")

DIRECTIONS = ("directed", "bidirectional")


class EdgeError(Exception):
    """Raised when an edge cannot be built as described."""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def edge(source_id: str, target_id: str, edge_type: str, *, authority: str,
         confidence: float, direction: str = "directed",
         interpreted: bool = False, note: str = "",
         created_at: str | None = None) -> dict[str, Any]:
    """One typed edge, carrying where it came from and how much to trust it.

    `authority` names the document or record that supports the edge, so a viewer
    can go and check it. An edge with no authority is a guess wearing a type, so
    it is refused.

    `confidence` is not a probability. It is how much of the edge came from a
    record: 1.0 means a record states it outright, 0.0 means the line exists
    only so a node is reachable.
    """
    if edge_type not in EDGE_TYPES:
        raise EdgeError(f"Unknown edge type {edge_type!r}. One of: {', '.join(EDGE_TYPES)}.")
    if direction not in DIRECTIONS:
        raise EdgeError(f"Unknown direction {direction!r}. One of: {', '.join(DIRECTIONS)}.")
    if not isinstance(confidence, (int, float)) or isinstance(confidence, bool):
        raise EdgeError(f"Edge confidence must be a number, got {confidence!r}.")
    if not 0.0 <= confidence <= 1.0:
        raise EdgeError(f"Edge confidence must be between 0 and 1, got {confidence!r}.")
    if not authority or not authority.strip():
        raise EdgeError(
            f"Edge {source_id} -> {target_id} has no authority. An edge nobody can "
            "check is a guess, not a relationship."
        )
    if not source_id or not target_id:
        raise EdgeError("An edge needs both a source and a target.")
    # A full-confidence edge that a view decided for itself is the exact
    # confusion this taxonomy exists to prevent: it would render as canon.
    if interpreted and confidence >= 1.0:
        raise EdgeError(
            f"Edge {source_id} -> {target_id} is marked interpreted but claims full "
            "confidence. An inference cannot be certain; lower the confidence or drop "
            "the interpretation."
        )
    return {
        "source": source_id,
        "target": target_id,
        "type": edge_type,
        "authority": authority,
        "confidence": round(float(confidence), 2),
        "direction": direction,
        "interpreted": bool(interpreted),
        "note": note,
        "created_at": created_at or now_iso(),
    }


def ledger_edge(source_id: str, target_id: str, edge_type: str, **fields: Any) -> dict[str, Any]:
    """An edge the event ledger witnessed. Refuses a type it cannot have seen.

    Used by the memory graph so that a `causal` or `temporal` claim is
    structurally tied to the one source able to support it.
    """
    if edge_type not in LEDGER_ONLY_TYPES + ("operational", "structural"):
        raise EdgeError(
            f"The event ledger does not witness {edge_type!r} relationships. "
            f"It may state: {', '.join(LEDGER_ONLY_TYPES + ('operational', 'structural'))}."
        )
    return edge(source_id, target_id, edge_type, **fields)


def registry_edge(source_id: str, target_id: str, edge_type: str, **fields: Any) -> dict[str, Any]:
    """An edge a registry or document states. Refuses the ledger-only types.

    This is the guard that keeps the Council view honest: reading the role
    registry cannot tell you that one event caused another, so a view built from
    it may not say so.
    """
    if edge_type in LEDGER_ONLY_TYPES:
        raise EdgeError(
            f"{edge_type!r} edges may only come from the event ledger; a registry "
            "witnesses structure, not occurrence."
        )
    return edge(source_id, target_id, edge_type, **fields)


def summarize(edges: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Counts per type, plus how much of the graph is interpretation.

    The `interpreted` / `canonical` split is the number a legend shows, so a
    viewer can see at a glance how much of what they are looking at the
    Foundation actually asserts.
    """
    rows = list(edges)
    counts = {edge_type: 0 for edge_type in EDGE_TYPES}
    for item in rows:
        counts[item["type"]] += 1
    return {
        "counts": counts,
        "total": len(rows),
        "interpreted": sum(1 for item in rows if item["interpreted"]),
        "canonical": sum(1 for item in rows if not item["interpreted"]),
    }


def orphans(edges: Iterable[dict[str, Any]], node_ids: Iterable[str]) -> list[str]:
    """Node ids no edge touches.

    A node with no line looks like a layout accident rather than a thing nobody
    has connected. Both views assert this is empty, and reconcile it with
    `structural` edges rather than by hiding the node.
    """
    touched: set[str] = set()
    for item in edges:
        touched.add(item["source"])
        touched.add(item["target"])
    return sorted(set(node_ids) - touched)
