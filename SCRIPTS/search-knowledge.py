#!/usr/bin/env python3
"""Search ALPHAPROXIMA Markdown files by text, metadata, or path."""

from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Search ALPHAPROXIMA Markdown knowledge files.")
    parser.add_argument("query", help="Case-insensitive search query")
    parser.add_argument("--path", default="", help="Optional path fragment filter")
    args = parser.parse_args()

    query = args.query.lower()
    path_filter = args.path.lower()
    matches = []

    for path in sorted(ROOT.rglob("*.md")):
        rel = str(path.relative_to(ROOT))
        if path_filter and path_filter not in rel.lower():
            continue
        text = path.read_text(encoding="utf-8")
        if query in text.lower() or query in rel.lower():
            matches.append(rel)

    for match in matches:
        print(match)

    if not matches:
        print("No matches found.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

