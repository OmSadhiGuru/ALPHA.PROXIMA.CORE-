#!/usr/bin/env python3
"""Galaxy Council prototype -- an isolated spatial composition, read-only.

This is a DESIGN PROTOTYPE, not a replacement for `office_spatial.py`. It
renders to its own output file, its own template, and its own port -- the
existing Council 3D Office (`ap.py office ...`) is untouched by anything in
this module.

## What this is

A radial composition of the same sixteen registry roles, arranged as:

  center            LUMIAION itself (AGT-001) -- the Foundation's HQ.
  inner circle      coordination seats close to LUMIAION.
  council ring      one seat per department, its actual lead.
  constellations    the rest of each department's roles, behind its lead.
  unassigned        roles whose registry owner is "Owner pending" -- no real
                    department exists for them yet, so they are held apart
                    rather than forced into a fabricated one.

## The transformation layer (§9 of the brief this was built from)

The registry has no "lead" flag and no "coordination seat" concept -- both
are visual roles this module assigns, not facts the registry states. That
assignment is `classify_roles()` below, and it is deliberately explicit and
narrow:

  * A department's lead is whichever of its roles is first in registry
    order unless LEAD_OVERRIDES selects another member of that owner group.
    This is a judgment call, not derived data -- documented here and
    in the companion concept note, not asserted as registry fact.
  * Every role keeps its own `id`; nothing is invented, merged, or renamed.
  * A "coordination seat" with no real occupant is emitted as
    `{"proposed": true, "desk": None}` -- never a fabricated agent.

## What this does NOT do

  * It does not execute anything. There is no `POST` handler in this
    module's `serve()`, matching `office_spatial.py`.
  * It does not call an LLM to preview the "propose an intention to
    LUMIAION" flow -- that flow is a static, clearly-labeled demonstration
    in the template, not a live request.
  * It does not touch `council-state.json`, `founder-state.json`, or the
    registry document. Read-only, like every sibling module.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
PROTOTYPE_DIR = VAULT_ROOT / "13_OPERATIONS" / "AI Council" / "spatial"
DEFAULT_TEMPLATE = PROTOTYPE_DIR / "galaxy-prototype.template.html"
DEFAULT_OUTPUT = PROTOTYPE_DIR / "galaxy-prototype.html"

VIEW_PLACEHOLDER = "/*__GALAXY_VIEW__*/null"

# Coordination-seat functions the brief asked for, confronted against the
# registry: only AGT-009 (Memory Steward, owner LUMIAION) is a real occupant
# of this kind of seat today. The rest are named functions with no titulaire
# -- proposed placeholders, not agents.
PROPOSED_COORDINATION_SEATS = [
    "Clarify Founder intent before it is routed",
    "Distribute and track work across the Council",
    "Check incoming data quality",
    "Prepare syntheses for LUMIAION's review",
]

# The transformation layer: which role is a department's council-seat lead.
# Judgment calls, explicit and narrow -- see the module docstring. Any
# owner not listed here falls back to "first role in registry order for
# that owner."
LEAD_OVERRIDES = {
    "Research Intelligence Office": "AGT-002",   # Research Lead, not the other two "*Lead" titles
    "Engineering Office": "AGT-007",              # CODEX Engineering Lead, not the Computational Specialist
    "Executive Office": "AGT-006",                # Executive Briefing Lead is available; AGT-011 is blocked
}


class PrototypeError(Exception):
    """Raised when the prototype view cannot be built or rendered."""


def _load_sibling(filename: str, name: str):
    path = (TOOLKIT_DIR / filename).resolve()
    if not path.exists():
        raise PrototypeError(f"Required toolkit module not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise PrototypeError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


office_spatial = _load_sibling("office_spatial.py", "galaxy_prototype_office_spatial")
role_registry = office_spatial.role_registry
alpha_app = office_spatial.alpha_app
# The relationship taxonomy, shared with the memory graph so both views mean the
# same thing by a line.
alpha_edges = _load_sibling("alpha_edges.py", "galaxy_alpha_edges")
check_reachability_gate = alpha_app.check_reachability_gate
LOOPBACK_HOSTS = alpha_app.LOOPBACK_HOSTS


# --------------------------------------------------------------------------
# the transformation layer
# --------------------------------------------------------------------------

def classify_roles(office_view: dict[str, Any]) -> dict[str, Any]:
    """Turn the flat 16-role registry into the radial composition.

    Reuses `office_spatial.build_office_view`'s desks (registry roles joined
    to live assignment status) as input -- one source of truth, two
    presentations.
    """
    desks_by_id = {d["id"]: d for d in office_view["desks"]}

    if "AGT-001" not in desks_by_id:
        raise PrototypeError("Galaxy requires canonical AGT-001; no substitute center is invented.")
    center = desks_by_id["AGT-001"]

    # Membership follows the current registry, including newly added roles.
    # A removed or reassigned Memory Steward must not be fabricated or duplicated.
    inner_circle: list[dict[str, Any]] = [
        {"proposed": False, "desk": desk, "function": desk["named_role"]}
        for desk in office_view["desks"]
        if desk["id"] != center["id"] and desk["operating_owner"] == "LUMIAION"
    ]
    for function in PROPOSED_COORDINATION_SEATS:
        inner_circle.append({"proposed": True, "desk": None, "function": function})

    by_owner: dict[str, list[dict[str, Any]]] = {}
    for owner in office_view["registry"]["owners"]:
        by_owner[owner["owner"]] = [desks_by_id[rid] for rid in owner["role_ids"]
                                    if rid != center["id"]]

    council: list[dict[str, Any]] = []
    unassigned: list[dict[str, Any]] = []
    for owner_name, members in by_owner.items():
        if owner_name == "LUMIAION" or not members:
            continue  # Center and current LUMIAION-owned roles are already placed.
        if owner_name == "Owner pending":
            unassigned.extend(members)
            continue
        lead_id = LEAD_OVERRIDES.get(owner_name)
        if lead_id and lead_id in {m["id"] for m in members}:
            lead = desks_by_id[lead_id]
        else:
            lead = members[0]
        constellation = [m for m in members if m["id"] != lead["id"]]
        council.append({
            "owner": owner_name,
            "lead": lead,
            "constellation": constellation,
        })

    return {
        "center": center,
        "inner_circle": inner_circle,
        "council": council,
        "unassigned": unassigned,
        "subagent_profiles": office_view["registry"]["subagent_profiles"],
    }


# --------------------------------------------------------------------------
# the edge taxonomy
# --------------------------------------------------------------------------
# Defined in `alpha_edges`, shared with the memory graph. Both views must mean
# the same thing by a line, or the Founder learns two visual languages.
#
# This view reads the role registry, so it builds through `registry_edge`, which
# refuses `causal` and `temporal` outright: a registry witnesses structure, not
# occurrence. Only the event ledger can say one thing caused another.
EDGE_TYPES = alpha_edges.EDGE_TYPES


def edge(source_id: str, target_id: str, edge_type: str, **fields: Any) -> dict[str, Any]:
    """A registry-authorized edge, with this module's error type on failure."""
    try:
        return alpha_edges.registry_edge(source_id, target_id, edge_type, **fields)
    except alpha_edges.EdgeError as exc:
        raise PrototypeError(str(exc)) from exc


def build_edges(galaxy: dict[str, Any]) -> list[dict[str, Any]]:
    """Every relationship in the composition, typed and attributed.

    Two rules govern this function, and they pull in opposite directions:

      * **No visible node is orphaned.** A seat with no line looks like an
        accident of layout rather than a role nobody has claimed.
      * **No relationship is invented.** The registry does not say that
        LUMIAION owns the Engineering Office, and this function must not say so
        either.

    They are reconciled by the `structural` type: an unowned or
    visually-positioned node is connected for navigability with an edge that
    states, in its own data, that it carries no institutional claim. The
    renderer draws those differently, and `test_council_galaxy_prototype`
    asserts that it must.
    """
    center = galaxy["center"]["id"]
    edges: list[dict[str, Any]] = []

    # The Vault is the memory layer LUMIAION reads from. This one is canonical.
    edges.append(edge(
        "VAULT", center, "semantic",
        authority="founder-state INT-001 — the Vault is the Founder OS memory layer",
        confidence=1.0, direction="bidirectional",
    ))

    # Registry fact: these roles report to LUMIAION as their operating owner.
    for seat in galaxy["inner_circle"]:
        if seat["proposed"] or not seat.get("desk"):
            continue
        edges.append(edge(
            center, seat["desk"]["id"], "operational",
            authority="Agent and Subagent Registry — operating owner",
            confidence=1.0,
        ))

    for constellation in galaxy["council"]:
        lead_id = constellation["lead"]["id"]
        owner = constellation["owner"]
        # Navigation only. The registry names the office, not a reporting line
        # from LUMIAION to it, and the choice of which role is its visual lead
        # is made in this module.
        edges.append(edge(
            center, lead_id, "structural",
            authority="galaxy composition — radial layout",
            confidence=0.0, interpreted=True,
            note=f"{owner} is placed on the council ring; no reporting line is asserted.",
        ))
        for member in constellation["constellation"]:
            # Shared registry ownership is a fact; drawing it through the lead
            # rather than as a group is this module's arrangement.
            edges.append(edge(
                lead_id, member["id"], "operational",
                authority=f"Agent and Subagent Registry — both roles owned by {owner}",
                confidence=0.6, interpreted=True,
                note="Shared owner is registry fact; routing through the visual lead is not.",
            ))

    # Roles with no owner. Connected so they are reachable, and marked so the
    # absence of a real department is visible rather than papered over.
    for role in galaxy["unassigned"]:
        edges.append(edge(
            center, role["id"], "structural",
            authority="galaxy composition — holding cluster for unowned roles",
            confidence=0.0, interpreted=True,
            note="Registry owner is pending. This line exists only so the seat is reachable.",
        ))

    return edges


def edge_summary(edges: list[dict[str, Any]]) -> dict[str, Any]:
    """Counts per type, plus how much of the graph is interpretation."""
    return alpha_edges.summarize(edges)


# What the committed render says instead of live data. `galaxy-prototype.html`
# is a generated artifact in the Foundation's permanent record, and presence is
# machine-local telemetry that expires in three minutes -- baking one into the
# other would commit a moment of one developer's afternoon as though it were
# institutional state, and would show a stale badge to anyone who opened the
# file later. The served page fetches the real thing from its own origin.
# The memory graph is derived from the event ledger, which is machine-local
# runtime state. It is omitted from a static render for exactly the reason
# presence is: a committed artifact must not preserve one afternoon's activity
# as though it were structure.
MEMORY_OMITTED = {
    "available": False,
    "reason": "Rendered without the memory graph. Serve this page to read the event ledger.",
    "nodes": [],
    "edges": [],
    "edge_summary": {"counts": {kind: 0 for kind in alpha_edges.EDGE_TYPES},
                     "total": 0, "interpreted": 0, "canonical": 0},
    "counts": {"events": 0, "entities": 0, "actors": 0,
               "actors_resolved": 0, "actors_unresolved": 0, "requires_founder": 0},
    "unresolved_actors": [],
}


LIVE_OMITTED = {
    "available": False,
    "reason": "Rendered without live state. Presence and activity are read when this page is served.",
    "realtime": {
        "mode": "unconfigured",
        "detail": "This is a static render. Serve it with `ap.py galaxy-prototype serve` for live activity.",
        "canonical_readable": True,
        "presence_trustworthy": False,
    },
    "presence": [],
    "activity": [],
    "badge": 0,
}


def build_live_section() -> dict[str, Any]:
    """The Live Integration Layer's projections, or an honest statement of absence.

    Wrapped in its own function with its own failure path because the galaxy is
    a view of the *registry*, which exists, and the live layer is a view of
    *activity*, which may not. A missing ledger must dim the presence dots, not
    take down the scene.
    """
    try:
        alpha_events = _load_sibling("alpha_events.py", "galaxy_alpha_events")
        alpha_adapters = _load_sibling("alpha_adapters.py", "galaxy_alpha_adapters")
        alpha_live = _load_sibling("alpha_live.py", "galaxy_alpha_live")
        ledger = alpha_events.EventLedger()
        store = alpha_live.LiveStore()
        registry = alpha_adapters.AdapterRegistry()
        view = alpha_live.build_live_view(ledger, store, registry, limit=25)
    except (PrototypeError, OSError, KeyError, ValueError) as exc:
        return {
            "available": False,
            "reason": str(exc),
            # Stated rather than implied by an empty feed: an interface that
            # cannot tell "nothing happened" from "I cannot see" is lying.
            "realtime": {"mode": "unavailable", "detail": f"Live layer unavailable: {exc}",
                         "canonical_readable": True, "presence_trustworthy": False},
            "presence": [], "activity": [], "badge": 0,
        }
    return {
        "available": True,
        "reason": "",
        "realtime": view["realtime"],
        "presence": view["presence"]["presence"],
        "activity": view["activity"]["activities"],
        "badge": view["badge"]["badge"],
        "integration_counts": view["integrations"]["counts"],
    }


def build_memory_section(root: Path) -> dict[str, Any]:
    """The event ledger as a graph, or an honest statement of absence.

    Separate from `build_live_section` because they answer different questions
    and fail independently: live activity is "what is happening", the memory
    graph is "what happened and what it led to". A ledger that cannot be read
    must dim the memory field, not the presence dots, and neither may take down
    the registry view — which exists whether or not anything has ever happened.
    """
    try:
        alpha_events = _load_sibling("alpha_events.py", "galaxy_alpha_events_mem")
        alpha_memory = _load_sibling("alpha_memory.py", "galaxy_alpha_memory")
        events = alpha_events.EventLedger().events()
        roles = role_registry.load_roles(root)["roles"]
        graph = alpha_memory.build_memory_graph(events, roles)
    except (PrototypeError, role_registry.RegistryError, OSError, KeyError, ValueError) as exc:
        return dict(MEMORY_OMITTED, available=False, reason=f"Memory graph unavailable: {exc}")
    return {
        "available": True,
        "reason": "",
        "nodes": graph["nodes"],
        "edges": graph["edges"],
        "edge_summary": graph["edge_summary"],
        "counts": graph["counts"],
        "unresolved_actors": graph["unresolved_actors"],
    }


def build_galaxy_view(root: Path = VAULT_ROOT, council_state_path: Path | None = None,
                      include_live: bool = True) -> dict[str, Any]:
    office_view = office_spatial.build_office_view(root, council_state_path)
    galaxy = classify_roles(office_view)
    edges = build_edges(galaxy)
    return {
        "schema_version": "1.1.0-prototype",
        "read_only": True,
        "classification_authority": "visual interpretation only; not institutional authority",
        "generated_at": role_registry.now_iso(),
        "galaxy": galaxy,
        # Edges are data, not drawing calls, so their taxonomy can be tested and
        # so a renderer cannot quietly upgrade an inference into a canonical line.
        "edges": edges,
        "edge_summary": edge_summary(edges),
        "brain": office_view["brain"],
        # Activity, presence and the badge — the Council as an observable space
        # rather than a diagram. Honest about its own absence.
        "live": build_live_section() if include_live else dict(LIVE_OMITTED),
        # What happened, joined to who exists. Ledger-authorized edges only:
        # the registry edges above and these are built through different
        # constructors precisely so neither can claim the other's authority.
        "memory": build_memory_section(root) if include_live else dict(MEMORY_OMITTED),
        # The full session/assignment ledger (council_kernel.build_view), not
        # just counts -- feeds the "Council Sessions" logistics panel, which
        # is a second read of the same data the per-desk assignment fields
        # already carry, not a new source of truth.
        "council": office_view["council"],
    }


# --------------------------------------------------------------------------
# renderer (mirrors alpha_app.render_app / office_spatial.render_app)
# --------------------------------------------------------------------------

def render_app(view: dict, template_path: Path) -> str:
    if not template_path.exists():
        raise PrototypeError(f"Prototype template not found: {template_path}")
    template = template_path.read_text(encoding="utf-8")
    if VIEW_PLACEHOLDER not in template:
        raise PrototypeError(f"Prototype template is missing the {VIEW_PLACEHOLDER} placeholder.")
    payload = json.dumps(view, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("</", "<\\/")
    return template.replace(VIEW_PLACEHOLDER, payload)


def write_output(view: dict, template_path: Path, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_app(view, template_path), encoding="utf-8")
    return output_path


# --------------------------------------------------------------------------
# localhost server -- read-only, isolated port, same reachability gate
# --------------------------------------------------------------------------

def serve(root: Path, template_path: Path, port: int = 8790,
          host: str = "127.0.0.1", token: str | None = None,
          council_state_path: Path | None = None) -> int:
    check_reachability_gate(host, port, token)

    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlsplit, parse_qs
    import hmac

    class Handler(BaseHTTPRequestHandler):
        def _send(self, body: bytes, content_type: str, status: int = 200) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, payload: Any, status: int = 200) -> None:
            self._send(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"),
                       "application/json; charset=utf-8", status)

        def _authorized(self, parsed) -> bool:
            if not token:
                return True
            header = self.headers.get("Authorization", "")
            presented = header[7:] if header.startswith("Bearer ") else ""
            if not presented:
                presented = parse_qs(parsed.query).get("token", [""])[0]
            return hmac.compare_digest(presented, token)

        def do_GET(self) -> None:  # noqa: N802
            parsed = urlsplit(self.path)
            self.path = parsed.path
            if not self._authorized(parsed):
                self._json({"error": "unauthorized"}, 401)
                return
            try:
                if self.path in ("/", "/index.html", "/galaxy-prototype.html"):
                    view = build_galaxy_view(root, council_state_path)
                    self._send(render_app(view, template_path).encode("utf-8"),
                               "text/html; charset=utf-8")
                elif self.path == "/api/galaxy":
                    self._json(build_galaxy_view(root, council_state_path))
                elif self.path == "/api/v1/memory":
                    self._json(build_memory_section(root))
                elif self.path == "/api/v1/live":
                    # Same-origin, so the scene can refresh presence without a
                    # cross-origin request to the app's port. Read-only, like
                    # every other route in this module.
                    self._json(build_live_section())
                else:
                    self._json({"error": "not found"}, 404)
            except (PrototypeError, role_registry.RegistryError, office_spatial.council_kernel.StateError, OSError) as exc:
                self._json({"error": str(exc)}, 500)

        def log_message(self, *args) -> None:
            pass

    server = HTTPServer((host, port), Handler)
    print(f"Galaxy prototype: http://{host}:{port}/{'?token=' + token if token else ''}")
    print("Loopback only. Ctrl-C to stop." if host in LOOPBACK_HOSTS
          else "Token-gated. Ctrl-C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    import argparse
    import os as _os

    parser = argparse.ArgumentParser(prog="ap.py galaxy-prototype", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT))
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--state", default=None)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("view", help="Print the classified galaxy view as JSON.")
    sub.add_parser("render", help="Regenerate galaxy-prototype.html.")
    serve_cmd = sub.add_parser("serve", help="Serve the prototype (default port 8790).")
    serve_cmd.add_argument("--port", type=int, default=8790)
    serve_cmd.add_argument("--host", default="127.0.0.1")
    serve_cmd.add_argument("--token", default=None)
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    template_path = Path(args.template)
    state_path = Path(args.state) if args.state else None

    try:
        if args.command == "view":
            print(json.dumps(build_galaxy_view(root, state_path), indent=2, ensure_ascii=False))
            return 0
        if args.command == "render":
            # Deliberately without live state -- see LIVE_OMITTED.
            written = write_output(build_galaxy_view(root, state_path, include_live=False),
                                   template_path, Path(args.output))
            print(f"wrote {written}")
            return 0
        if args.command == "serve":
            token = args.token or _os.environ.get("ALPHA_APP_TOKEN")
            return serve(root, template_path, args.port, host=args.host, token=token,
                        council_state_path=state_path)
    except (PrototypeError, role_registry.RegistryError, office_spatial.council_kernel.StateError, alpha_app.AppError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
