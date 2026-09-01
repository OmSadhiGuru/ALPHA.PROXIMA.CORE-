#!/usr/bin/env python3
"""Apply Alpha Proxima Obsidian Graph View color groups."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path


WARNING = "Close Obsidian before running this script. Obsidian may overwrite graph.json while open."
DEFAULT_GRAPH = Path(".obsidian/graph.json")

OFFICIAL_COLOR_GROUPS = [
    # Rule 1: LUMIAION - Central orchestration intelligence
    {
        "query": "file:LUMIAION",
        "color": {"a": 1, "rgb": 0x7C3AED},
    },
    # Rule 2: Executive Office (FIXED: 09_OFFICES → 11_OPERATIONS)
    {
        "query": 'path:"11_OPERATIONS/Executive Office"',
        "color": {"a": 1, "rgb": 0xD97706},
    },
    # Rule 3: Research Council (FIXED: 09_OFFICES → 03_AI_COUNCIL)
    {
        "query": 'path:"03_AI_COUNCIL/Research Council"',
        "color": {"a": 1, "rgb": 0x059669},
    },
    # Rule 4: Engineering Systems (FIXED: 09_OFFICES → 08_SYSTEMS)
    {
        "query": 'path:"08_SYSTEMS/Engineering Toolkit" OR path:"08_SYSTEMS/Engineering Standards"',
        "color": {"a": 1, "rgb": 0xEA580C},
    },
    # Rule 5: Institutional Observatory (FIXED: 09_OFFICES → 11_OPERATIONS)
    {
        "query": 'path:"11_OPERATIONS/Institutional Observatory"',
        "color": {"a": 1, "rgb": 0x0891B2},
    },
    # Rule 6: Ethics Council Charter
    {
        "query": 'file:"Ethics Council Charter"',
        "color": {"a": 1, "rgb": 0xBE123C},
    },
    # Rule 7: SOHMA Charter
    {
        "query": 'file:"SOHMA Charter"',
        "color": {"a": 1, "rgb": 0x9333EA},
    },
    # Rule 8: ATHENA Charter
    {
        "query": 'file:"ATHENA Charter"',
        "color": {"a": 1, "rgb": 0x1D4ED8},
    },
    # Rule 9: VORTEX Charter
    {
        "query": 'file:"VORTEX Charter"',
        "color": {"a": 1, "rgb": 0x65A30D},
    },
    # Rule 10: JERANIUM Charter
    {
        "query": 'file:"JERANIUM Charter"',
        "color": {"a": 1, "rgb": 0x0F766E},
    },
    # Rule 11: Constitutional Authority
    {
        "query": "path:00_CONSTITUTION",
        "color": {"a": 1, "rgb": 0xF59E0B},
    },
    # Rule 12: Research Programs
    {
        "query": "path:07_RESEARCH",
        "color": {"a": 1, "rgb": 0x16A34A},
    },
    # Rule 13: Governance Bodies
    {
        "query": "path:06_GOVERNANCE",
        "color": {"a": 1, "rgb": 0x0369A1},
    },
    # Rule 14: Systems Architecture (catch-all for 08_SYSTEMS)
    {
        "query": "path:08_SYSTEMS",
        "color": {"a": 1, "rgb": 0xC2410C},
    },
    # Rule 15: AI Council (catch-all for 03_AI_COUNCIL)
    {
        "query": "path:03_AI_COUNCIL",
        "color": {"a": 1, "rgb": 0x0D9488},
    },
    # Rule 16: Decisions & ADRs
    {
        "query": "path:04_DECISIONS",
        "color": {"a": 1, "rgb": 0xE11D48},
    },
    # Rule 17: Vision & Strategy
    {
        "query": "path:01_VISION OR path:02_STRATEGY",
        "color": {"a": 1, "rgb": 0xC026D3},
    },
    # Rule 18: Templates & Scaffolds
    {
        "query": "path:10_TEMPLATES",
        "color": {"a": 1, "rgb": 0x64748B},
    },
    # Rule 19: Archive & Deprecated
    {
        "query": "path:99_ARCHIVE",
        "color": {"a": 1, "rgb": 0x57534E},
    },
    # Rule 20: Proposals (NEW - v1.1.0 audit)
    {
        "query": "path:05_PROPOSALS",
        "color": {"a": 1, "rgb": 0x4F46E5},
    },
    # Rule 21: Active Projects (NEW - v1.1.0 audit)
    {
        "query": "path:06_PROJECTS",
        "color": {"a": 1, "rgb": 0x0EA5E9},
    },
    # Rule 22: Future & Technology Watch (NEW - v1.1.0 audit)
    {
        "query": "path:09_FUTURE",
        "color": {"a": 1, "rgb": 0xEC4899},
    },
    # Rule 23: People & Roles (NEW - v1.1.0 audit)
    {
        "query": "path:09_PEOPLE",
        "color": {"a": 1, "rgb": 0x92400E},
    },
    # Rule 24: Operations (catch-all for 11_OPERATIONS) (NEW - v1.1.0 audit)
    {
        "query": "path:11_OPERATIONS",
        "color": {"a": 1, "rgb": 0x1E293B},
    },
    # Rule 25: Alpha Proxima Meta (NEW - v1.1.0 audit)
    {
        "query": 'path:"ALPHA PROXIMA"',
        "color": {"a": 1, "rgb": 0xA16207},
    },
    # Rule 26: OSG Launch Initiative (NEW - v1.1.0 audit)
    {
        "query": "path:OSG_LAUNCH",
        "color": {"a": 1, "rgb": 0x14532D},
    },
]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root. Defaults to current working directory.")
    parser.add_argument("--graph-file", default=str(DEFAULT_GRAPH), help="Path to graph.json relative to vault or absolute.")
    parser.add_argument("--dry-run", action="store_true", help="Preview the update without writing files.")
    return parser.parse_args(argv)


def graph_path(root: Path, raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = root / path
    return path


def backup_path(path: Path) -> Path:
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    return path.with_name(f"graph.backup-{timestamp}.json")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    path = graph_path(root, args.graph_file)

    print(f"Warning: {WARNING}")

    if not path.exists():
        print(f"error: graph configuration not found: {path}", file=sys.stderr)
        return 2

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        print(f"error: graph configuration should be a JSON object: {path}", file=sys.stderr)
        return 2

    updated = dict(data)
    updated["colorGroups"] = OFFICIAL_COLOR_GROUPS

    if args.dry_run:
        print(f"Dry run: would update {path}")
        print(f"Official color groups: {len(OFFICIAL_COLOR_GROUPS)}")
        return 0

    backup = backup_path(path)
    shutil.copy2(path, backup)
    path.write_text(json.dumps(updated, indent=2) + "\n", encoding="utf-8")

    print("Alpha Proxima graph color groups applied successfully.")
    print(f"Graph configuration updated: {path}")
    print(f"Backup written: {backup}")
    print(f"Color groups written: {len(OFFICIAL_COLOR_GROUPS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
