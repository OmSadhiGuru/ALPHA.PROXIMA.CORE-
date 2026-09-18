#!/usr/bin/env python3
"""3D office — a read-only spatial view over the Council role registry.

Composes `role_registry.load_roles()` (the sixteen named agent roles) with
`council_kernel`'s session/assignment state into one desk-per-role read
model, and renders it into a self-contained isometric scene.

Two rules carried over from `alpha_app.py`, unchanged:

  * **It writes nothing.** No `council_kernel.save`, `record_output`,
    `execute_assignment`, or `assign` call appears anywhere in this module.
    Triggering a real run stays a CLI act (`ap.py council run ...`); the page
    only ever shows the exact command to copy.
  * **Authentication ships before reachability.** `serve()` reuses
    `alpha_app.check_reachability_gate` rather than reimplementing it, so a
    non-loopback bind is refused without a token from day one, exactly like
    the main app.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
OFFICE_DIR = VAULT_ROOT / "13_OPERATIONS" / "AI Council" / "spatial"
DEFAULT_TEMPLATE = OFFICE_DIR / "office.template.html"
DEFAULT_OUTPUT = OFFICE_DIR / "office.html"

VIEW_PLACEHOLDER = "/*__OFFICE_VIEW__*/null"


class OfficeError(Exception):
    """Raised when the office view cannot be built or rendered."""


def _load_sibling(filename: str, name: str):
    """Import a toolkit module by path, mirroring `alpha_app._load_sibling`."""
    path = (TOOLKIT_DIR / filename).resolve()
    if not path.exists():
        raise OfficeError(f"Required toolkit module not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise OfficeError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


role_registry = _load_sibling("role_registry.py", "office_spatial_role_registry")
council_kernel = _load_sibling("council_kernel.py", "office_spatial_council_kernel")
alpha_app = _load_sibling("alpha_app.py", "office_spatial_alpha_app")

check_reachability_gate = alpha_app.check_reachability_gate
LOOPBACK_HOSTS = alpha_app.LOOPBACK_HOSTS


# --------------------------------------------------------------------------
# the composed read model
# --------------------------------------------------------------------------

def _active_assignment(state: dict, role_id: str) -> dict[str, Any] | None:
    """The most recently opened, not-yet-complete assignment for this role, if any."""
    candidates = []
    for item in state["sessions"]:
        for run in item["assignments"]:
            if run["role"] == role_id and run["status"] != "complete":
                candidates.append({
                    "session_id": item["session_id"],
                    "run_id": run["id"],
                    "deliverable": run["deliverable"],
                    "status": run["status"],
                    "created_at": run["created_at"],
                })
    if not candidates:
        return None
    return sorted(candidates, key=lambda c: c["created_at"], reverse=True)[0]


def _recent_outputs(state: dict, role_id: str, limit: int = 3) -> list[dict[str, Any]]:
    completed = []
    for item in state["sessions"]:
        for run in item["assignments"]:
            if run["role"] == role_id and run["status"] == "complete":
                completed.append({
                    "session_id": item["session_id"],
                    "run_id": run["id"],
                    "deliverable": run["deliverable"],
                    "output": run["output"],
                    "completed_at": run.get("completed_at"),
                })
    completed.sort(key=lambda c: c.get("completed_at") or "", reverse=True)
    return completed[:limit]


def _brain_summary(root: Path) -> dict[str, Any]:
    """A light read of the Alpha Proxima vault, for the central Brain node.

    Reuses `alpha_app`'s own vault index and Truth Kernel builders (already
    loaded as a sibling for the reachability gate) rather than re-parsing the
    vault a second way. Only a compact summary is returned -- never the full
    entries list -- so the office view stays a light poll, not a second copy
    of `alpha_app`'s own index.
    """
    vault_index = alpha_app.build_vault_index(root)
    coherence = vault_index["coherence"]
    kernel = alpha_app.truth_kernel.build(root)
    kernel_summary = alpha_app.truth_kernel.summary(kernel)
    return {
        "note_count": vault_index["note_count"],
        "domain_count": len(vault_index["domains"]),
        "connectedness": coherence["connectedness"],
        "coherence_defects": sum(coherence["counts"].values()),
        "knowledge_nodes": kernel_summary["counts"]["nodes"],
        "knowledge_findings": kernel_summary["health"]["counts"]["findings"],
        "health_status": kernel_summary["health"]["status"],
    }


def build_office_view(root: Path = VAULT_ROOT, council_state_path: Path | None = None) -> dict[str, Any]:
    """The application's read model: the registry's roles, joined to live Council state."""
    registry = role_registry.load_roles(root)
    state_path = council_state_path or (root / "13_OPERATIONS" / "AI Council" / "state" / "council-state.json")
    state = council_kernel.load(state_path)
    sessions_view = council_kernel.build_view(state)

    desks = []
    for record in registry["roles"]:
        desks.append({
            **record,
            "active_assignment": _active_assignment(state, record["id"]),
            "recent_outputs": _recent_outputs(state, record["id"]),
        })

    return {
        "schema_version": "1.0.0",
        "generated_at": role_registry.now_iso(),
        "registry": registry,
        "council": sessions_view,
        "desks": desks,
        "brain": _brain_summary(root),
    }


# --------------------------------------------------------------------------
# renderer (mirrors alpha_app.render_app exactly)
# --------------------------------------------------------------------------

def render_app(view: dict, template_path: Path) -> str:
    """Inline the read model so the page works from `file://` with no server."""
    if not template_path.exists():
        raise OfficeError(f"Office template not found: {template_path}")
    template = template_path.read_text(encoding="utf-8")
    if VIEW_PLACEHOLDER not in template:
        raise OfficeError(f"Office template is missing the {VIEW_PLACEHOLDER} placeholder.")
    payload = json.dumps(view, ensure_ascii=False, separators=(",", ":"))
    # Prevent an embedded </script> inside data from terminating the tag early.
    payload = payload.replace("</", "<\\/")
    return template.replace(VIEW_PLACEHOLDER, payload)


def write_output(view: dict, template_path: Path, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_app(view, template_path), encoding="utf-8")
    return output_path


# --------------------------------------------------------------------------
# localhost server -- read-only, same reachability gate as alpha_app
# --------------------------------------------------------------------------

def serve(root: Path, template_path: Path, port: int = 8789,
          host: str = "127.0.0.1", token: str | None = None,
          council_state_path: Path | None = None) -> int:
    """Serve the office view. See `alpha_app.serve` for the security model this mirrors.

    Also serves the Galaxy Council prototype (`/galaxy`, `/api/galaxy`) on
    this same port/token, so the Founder has one URL for both views instead
    of two separate servers. Loaded lazily, function-local: importing this
    at module level would make `office_spatial` and `council_galaxy_prototype`
    load each other at import time (each is the other's sibling dependency),
    which is harmless once but wasteful on every import of either module for
    reasons that have nothing to do with serving.
    """
    check_reachability_gate(host, port, token)
    galaxy_prototype = _load_sibling("council_galaxy_prototype.py", "office_serve_galaxy_prototype")

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

        def do_GET(self) -> None:  # noqa: N802 - stdlib naming
            parsed = urlsplit(self.path)
            self.path = parsed.path
            if not self._authorized(parsed):
                self._json({"error": "unauthorized"}, 401)
                return
            try:
                if self.path in ("/", "/index.html", "/office.html"):
                    view = build_office_view(root, council_state_path)
                    self._send(render_app(view, template_path).encode("utf-8"),
                               "text/html; charset=utf-8")
                elif self.path in ("/api/office", "/api/v1/office"):
                    self._json(build_office_view(root, council_state_path))
                elif self.path == "/api/v1/roles":
                    registry = role_registry.load_roles(root)
                    self._json({"schema_version": "1.0.0", "roles": registry["roles"],
                               "owners": registry["owners"]})
                elif self.path == "/api/v1/sessions":
                    state = council_kernel.load(council_state_path or (root / "13_OPERATIONS" / "AI Council" / "state" / "council-state.json"))
                    self._json(council_kernel.build_view(state))
                elif self.path in ("/galaxy", "/galaxy.html", "/galaxy-prototype.html"):
                    view = galaxy_prototype.build_galaxy_view(root, council_state_path)
                    self._send(galaxy_prototype.render_app(view, galaxy_prototype.DEFAULT_TEMPLATE).encode("utf-8"),
                               "text/html; charset=utf-8")
                elif self.path == "/api/galaxy":
                    self._json(galaxy_prototype.build_galaxy_view(root, council_state_path))
                else:
                    self._json({"error": "not found"}, 404)
            except (OfficeError, role_registry.RegistryError, council_kernel.StateError,
                    galaxy_prototype.PrototypeError, OSError) as exc:
                self._json({"error": str(exc)}, 500)

        def log_message(self, *args) -> None:  # keep the terminal calm
            pass

    server = HTTPServer((host, port), Handler)
    print(f"3D Office: http://{host}:{port}/{'?token=' + token if token else ''}")
    print(f"Read model: http://{host}:{port}/api/office")
    print("Loopback only. Ctrl-C to stop." if host in LOOPBACK_HOSTS
          else "Token-gated — every request must present it. Ctrl-C to stop.")
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

def build_parser():
    import argparse
    import os as _os

    parser = argparse.ArgumentParser(prog="ap.py office", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT), help="Vault root to read.")
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="Office template path.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Rendered office.html output.")
    parser.add_argument("--state", default=None, help="Path to council-state.json.")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("view", help="Print the composed office view as JSON.")
    sub.add_parser("render", help="Regenerate office.html from office.template.html.")
    serve_cmd = sub.add_parser("serve", help="Serve the office view.")
    serve_cmd.add_argument("--port", type=int, default=8789)
    serve_cmd.add_argument("--host", default="127.0.0.1",
                           help="Bind address. Anything but 127.0.0.1/localhost requires "
                                "--token or ALPHA_APP_TOKEN.")
    serve_cmd.add_argument("--token", default=None,
                           help="Shared token every request must present. Falls back to $ALPHA_APP_TOKEN.")
    return parser, _os


def main(argv: list[str] | None = None) -> int:
    parser, _os = build_parser()
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    template_path = Path(args.template)
    state_path = Path(args.state) if args.state else None

    try:
        if args.command == "view":
            print(json.dumps(build_office_view(root, state_path), indent=2, ensure_ascii=False))
            return 0
        if args.command == "render":
            written = write_output(build_office_view(root, state_path), template_path, Path(args.output))
            print(f"wrote {written}")
            return 0
        if args.command == "serve":
            token = args.token or _os.environ.get("ALPHA_APP_TOKEN")
            return serve(root, template_path, args.port, host=args.host, token=token,
                        council_state_path=state_path)
    except (OfficeError, role_registry.RegistryError, council_kernel.StateError, alpha_app.AppError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
