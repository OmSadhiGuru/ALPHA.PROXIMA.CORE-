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
    {
        "query": "path:09_OFFICES/LUMIAION OR file:LUMIAION",
        "color": {"a": 1, "rgb": 0x7C3AED},
    },
    {
        "query": 'path:"09_OFFICES/Executive Office"',
        "color": {"a": 1, "rgb": 0xD97706},
    },
    {
        "query": 'path:"09_OFFICES/Research Intelligence Office"',
        "color": {"a": 1, "rgb": 0x059669},
    },
    {
        "query": 'path:"09_OFFICES/Engineering Office"',
        "color": {"a": 1, "rgb": 0xEA580C},
    },
    {
        "query": 'path:"09_OFFICES/Institutional Observatory"',
        "color": {"a": 1, "rgb": 0x0891B2},
    },
    {
        "query": 'file:"Ethics Council Charter"',
        "color": {"a": 1, "rgb": 0xBE123C},
    },
    {
        "query": 'file:"SOHMA Charter"',
        "color": {"a": 1, "rgb": 0x9333EA},
    },
    {
        "query": 'file:"ATHENA Charter"',
        "color": {"a": 1, "rgb": 0x1D4ED8},
    },
    {
        "query": 'file:"VORTEX Charter"',
        "color": {"a": 1, "rgb": 0x65A30D},
    },
    {
        "query": 'file:"JERANIUM Charter"',
        "color": {"a": 1, "rgb": 0x0F766E},
    },
    {
        "query": "path:00_CONSTITUTION",
        "color": {"a": 1, "rgb": 0xF59E0B},
    },
    {
        "query": "path:07_RESEARCH",
        "color": {"a": 1, "rgb": 0x16A34A},
    },
    {
        "query": "path:06_GOVERNANCE",
        "color": {"a": 1, "rgb": 0x0369A1},
    },
    {
        "query": "path:08_SYSTEMS",
        "color": {"a": 1, "rgb": 0xC2410C},
    },
    {
        "query": "path:03_AI_COUNCIL",
        "color": {"a": 1, "rgb": 0x0D9488},
    },
    {
        "query": "path:04_DECISIONS",
        "color": {"a": 1, "rgb": 0xE11D48},
    },
    {
        "query": "path:01_VISION OR path:02_STRATEGY",
        "color": {"a": 1, "rgb": 0xC026D3},
    },
    {
        "query": "path:10_TEMPLATES",
        "color": {"a": 1, "rgb": 0x64748B},
    },
    {
        "query": "path:99_ARCHIVE",
        "color": {"a": 1, "rgb": 0x57534E},
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
