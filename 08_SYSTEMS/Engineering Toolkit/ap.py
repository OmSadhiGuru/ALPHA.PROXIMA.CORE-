#!/usr/bin/env python3
"""Unified Alpha Proxima Engineering CLI."""

from __future__ import annotations

import argparse
import sys
import types
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
COMMANDS = {
    "validate": ("vault_validator.py", "Run the Vault Validator"),
    "yaml": ("yaml_validator.py", "Run the YAML Validator"),
    "stats": ("vault_statistics.py", "Generate the Engineering Dashboard Report"),
    "migrate": ("metadata_migrator.py", "Plan or apply metadata migration"),
    "report": ("vault_statistics.py", "Alias for stats"),
    "office-check": ("office_integrity_checker.py", "Generate the Office Integrity Report"),
    "research-check": ("research_integrity_checker.py", "Generate the Research Integrity Report"),
    "dependency-map": ("dependency_analyzer.py", "Generate the Vault Dependency Report"),
    "research-management": ("research_management.py", "Generate the Research Management Toolkit dashboard and index"),
    "graph-colors": ("apply_graph_colors.py", "Apply official Obsidian Graph View color groups"),
    "founder": ("founder_os.py", "Founder OS state engine and Founder Console V1"),
    "council": ("council_kernel.py", "Minimum Viable Council session kernel"),
    "app": ("alpha_app.py", "Alpha Proxima App — the Foundation's operate and know halves"),
    "events": ("alpha_events.py", "AlphaEvent v1 contract, validation, and the append-only event ledger"),
    "adapters": ("alpha_adapters.py", "Provider adapters and the honest adapter registry"),
    "context": ("alpha_context.py", "ContextItem v1 — the capture contract for Omi and Pocket AI"),
    "ingress": ("alpha_ingress.py", "Signed webhook receiver — the layer's only write path"),
    "memory": ("alpha_memory.py", "Memory graph — the event ledger as a navigable temporal structure"),
    "live": ("alpha_live.py", "Live Integration Layer projections — activity, presence, notifications, badge"),
    "spatial": ("alpha_spatial.py", "System Backbone contract as Markdown or JSON — first consumer of /api/v1/system-backbone"),
    "role-registry": ("role_registry.py", "Parse the Agent and Subagent Registry as JSON"),
    "entities": ("entity_registry.py", "Canonical identity for actors that are not documents"),
    "office": ("office_spatial.py", "3D office visualization — Council roles as a spatial read model"),
    "node-registry": ("../Institutional Knowledge Graph/Tools/node_registry.py", "Generate the Institutional Knowledge Graph node registry"),
    "relationship-extract": ("../Institutional Knowledge Graph/Tools/relationship_extractor.py", "Generate the Institutional Knowledge Graph relationship registry"),
    "retrieve": ("alpha_retrieval.py", "Vault retrieval — lexical and structural, not semantic (narrows BLK-002)"),
    "truth-kernel": ("../Institutional Knowledge Graph/Tools/truth_kernel.py", "Build the read-only Truth Kernel contract and validation report"),
}


def load_tool(filename: str):
    path = (TOOLKIT_DIR / filename).resolve()
    module = types.ModuleType(path.stem)
    module.__file__ = str(path)
    sys.modules[path.stem] = module
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), module.__dict__)
    return module


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=sorted(COMMANDS), help="Toolkit command to run.")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments passed to the selected command.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    filename, _ = COMMANDS[args.command]
    module = load_tool(filename)
    return int(module.main(args.args))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
