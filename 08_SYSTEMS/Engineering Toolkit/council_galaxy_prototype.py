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
    order among those literally titled "*Lead*" (or the office's own
    domain-lead role for single-role offices). Ties are broken by registry
    order. This is a judgment call, not derived data -- documented here and
    in the companion concept note, not asserted as registry fact.
  * Every role keeps its own `id`; nothing is invented, merged, or renamed.
  * A "coordination seat" with no real occupant is emitted as
    `{"proposed": true, "role_id": None}` -- never a fabricated agent.

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

    center = desks_by_id["AGT-001"]

    inner_circle: list[dict[str, Any]] = [{
        "proposed": False,
        "desk": desks_by_id["AGT-009"],
        "function": "Holds context and writeback for LUMIAION",
    }]
    for function in PROPOSED_COORDINATION_SEATS:
        inner_circle.append({"proposed": True, "desk": None, "function": function})

    by_owner: dict[str, list[dict[str, Any]]] = {}
    for owner in office_view["registry"]["owners"]:
        by_owner[owner["owner"]] = [desks_by_id[rid] for rid in owner["role_ids"]]

    council: list[dict[str, Any]] = []
    unassigned: list[dict[str, Any]] = []
    for owner_name, members in by_owner.items():
        if owner_name == "LUMIAION":
            continue  # AGT-001 is the center; AGT-009 is already in the inner circle
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


def build_galaxy_view(root: Path = VAULT_ROOT, council_state_path: Path | None = None) -> dict[str, Any]:
    office_view = office_spatial.build_office_view(root, council_state_path)
    return {
        "schema_version": "1.0.0-prototype",
        "generated_at": role_registry.now_iso(),
        "galaxy": classify_roles(office_view),
        "brain": office_view["brain"],
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
                else:
                    self._json({"error": "not found"}, 404)
            except (PrototypeError, role_registry.RegistryError, OSError) as exc:
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
            written = write_output(build_galaxy_view(root, state_path), template_path, Path(args.output))
            print(f"wrote {written}")
            return 0
        if args.command == "serve":
            token = args.token or _os.environ.get("ALPHA_APP_TOKEN")
            return serve(root, template_path, args.port, host=args.host, token=token,
                        council_state_path=state_path)
    except (PrototypeError, role_registry.RegistryError, alpha_app.AppError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
