#!/usr/bin/env python3
"""Alpha Spatial — the first consumer of the System Backbone read contract.

`alpha_app.py` v1.4.0 introduced `GET /api/v1/system-backbone`: one normalized,
read-only view of every registered system, department, and Founder-attention
signal (`Alpha Proxima App Architecture v1` §7.2). This module is the first
thing that consumes it, and it establishes the shape every future spatial or
VR renderer must follow:

  * **It is a fourth consumer, never a second store.** It builds nothing that
    `alpha_app.build_system_backbone` does not already compute, and it caches
    nothing to disk. Every run reflects the Founder state at that instant.
  * **It writes nothing.** No `founder_os` mutation, no vault write, no cache
    file. Standard output only.
  * **`connected` is reported exactly as the state engine says it is.** A
    `planned` or `blocked` system is never presented as live. This is the same
    honesty guard `test_view_exposes_one_honest_system_backbone` locks in code;
    this module is bound by it too, not just the endpoint that emits it.

Two ways to obtain the contract, same shape either way:

  * **in-process (default)** -- imports `alpha_app` and calls
    `build_system_backbone` directly against local `founder-state.json` and
    the vault. No server required.
  * **`--live`** -- fetches `/api/v1/system-backbone` from a running
    `ap.py app serve` over loopback (127.0.0.1 only, per `FD-002`). Use this
    once a spatial renderer needs to point at the same running process a
    human is also looking at, rather than a second independent read.

`report` renders the contract as Markdown shaped for a permanent knowledge
note. `view` prints the raw JSON contract for a future renderer to consume.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import urllib.request
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent


class SpatialError(Exception):
    """Raised when the System Backbone contract cannot be built or fetched."""


def _load_sibling(filename: str, name: str):
    """Import a toolkit module by path, mirroring `alpha_app._load_sibling`."""
    path = (TOOLKIT_DIR / filename).resolve()
    if not path.exists():
        raise SpatialError(f"Required toolkit module not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SpatialError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# --------------------------------------------------------------------------
# obtaining the contract
# --------------------------------------------------------------------------

def build_backbone_in_process(root: Path, state_path: Path) -> dict[str, Any]:
    """Compute the contract locally: the same call `alpha_app` itself makes."""
    alpha_app = _load_sibling("alpha_app.py", "alpha_spatial_alpha_app")
    founder_os = alpha_app.founder_os
    truth_kernel = alpha_app.truth_kernel
    state = founder_os.load_state(state_path)
    kernel = truth_kernel.build(root)
    return alpha_app.build_system_backbone(state, kernel)


def fetch_backbone_live(port: int) -> dict[str, Any]:
    """Fetch the contract from a running `ap.py app serve`, loopback only."""
    url = f"http://127.0.0.1:{port}/api/v1/system-backbone"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:  # noqa: S310 - loopback only
            return json.loads(response.read().decode("utf-8"))
    except OSError as exc:
        raise SpatialError(
            f"Could not reach {url} — is `ap.py app serve` running? ({exc})"
        ) from exc


# --------------------------------------------------------------------------
# report rendering
# --------------------------------------------------------------------------

def _bool_mark(value: bool) -> str:
    return "yes" if value else "no"


def render_report(backbone: dict[str, Any]) -> str:
    """Render the contract as Markdown shaped to paste into a permanent note.

    Table order mirrors the contract's own field order, not an editorial
    choice -- so this report is a faithful transcription of the read model,
    never a second interpretation of it.
    """
    lines: list[str] = []
    counts = backbone["counts"]

    lines.append(f"Schema version: `{backbone['schema_version']}` · mode: `{backbone['mode']}`")
    lines.append("")
    lines.append(
        f"Canonical sources — operate: `{backbone['canonical_sources']['operate']}` · "
        f"know: `{backbone['canonical_sources']['know']}`"
    )
    lines.append("")

    lines.append(f"## Systems ({counts['systems']} registered, {counts['connected_systems']} connected)")
    lines.append("")
    lines.append("| ID | Name | Kind | Status | Connected | Planned capability | Notes |")
    lines.append("|---|---|---|---|---|---|---|")
    for system in backbone["systems"]:
        lines.append(
            f"| {system['id']} | {system['name']} | {system['kind']} | {system['status']} "
            f"| {_bool_mark(system['connected'])} | {system.get('planned_capability') or ''} "
            f"| {system.get('notes') or ''} |"
        )
    lines.append("")

    lines.append(f"## Departments ({counts['departments']})")
    lines.append("")
    lines.append("| ID | Name | Role | Status | Authority |")
    lines.append("|---|---|---|---|---|")
    for dept in backbone["departments"]:
        lines.append(
            f"| {dept['id']} | {dept['name']} | {dept['role']} | {dept['status']} | {dept['authority']} |"
        )
    lines.append("")

    lines.append(f"## Attention signals ({counts['attention_signals']})")
    lines.append("")
    if backbone["attention"]:
        lines.append("| ID | Kind | Severity | Title | Owner |")
        lines.append("|---|---|---|---|---|")
        for signal in backbone["attention"]:
            lines.append(
                f"| {signal['id']} | {signal['kind']} | {signal['severity']} "
                f"| {signal['title']} | {signal['owner']} |"
            )
    else:
        lines.append("None open.")
    lines.append("")

    lines.append("## Knowledge")
    lines.append("")
    lines.append(f"- Nodes: {counts['knowledge_nodes']}")
    lines.append(f"- Findings: {counts['knowledge_findings']}")
    lines.append(f"- Truth Kernel status: `{backbone['truth_kernel']['health']['status']}`")

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ap.py spatial", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT), help="Vault root to index.")
    parser.add_argument(
        "--state",
        default=None,
        help="Path to founder-state.json. Defaults to founder_os.DEFAULT_STATE.",
    )
    parser.add_argument("--live", action="store_true", help="Fetch from a running `ap.py app serve` instead of building in-process.")
    parser.add_argument("--port", type=int, default=8788, help="Port for --live (loopback only).")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("report", help="Render the System Backbone contract as Markdown.")
    sub.add_parser("view", help="Print the raw System Backbone contract as JSON.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()

    try:
        if args.live:
            backbone = fetch_backbone_live(args.port)
        else:
            founder_os = _load_sibling("founder_os.py", "alpha_spatial_founder_os")
            state_path = Path(args.state) if args.state else founder_os.DEFAULT_STATE
            backbone = build_backbone_in_process(root, state_path)

        if args.command == "view":
            print(json.dumps(backbone, indent=2, ensure_ascii=False))
            return 0

        if args.command == "report":
            print(render_report(backbone), end="")
            return 0
    except SpatialError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
