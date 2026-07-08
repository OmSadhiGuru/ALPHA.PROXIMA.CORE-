#!/usr/bin/env python3
"""Build a Markdown index preview from ALPHAPROXIMA frontmatter."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()
    return metadata


def main() -> int:
    rows = []
    for path in sorted(ROOT.rglob("*.md")):
        metadata = parse_metadata(path)
        if not metadata:
            continue
        rows.append(
            [
                metadata.get("id", ""),
                metadata.get("title", ""),
                str(path.relative_to(ROOT)),
                metadata.get("department", ""),
                metadata.get("type", ""),
                metadata.get("status", ""),
            ]
        )

    print("---")
    print("title: Master Index")
    print("id: apx-index-master")
    print("department: LUMIAION")
    print("domain: indexing")
    print("type: index")
    print("status: active")
    print("version: 1.1.0")
    print("created: 2026-07-07")
    print("updated: 2026-07-07")
    print("source: generated")
    print("tags: [index, master, retrieval, generated]")
    print("related: [department-index.md, tag-index.md, status-index.md]")
    print("owner: Knowledge Atlas Office")
    print("---")
    print()
    print("# Master Index")
    print()
    print("Generated from Markdown frontmatter by `SCRIPTS/build-index.py`.")
    print()
    print("| ID | Title | Path | Department | Type | Status |")
    print("| --- | --- | --- | --- | --- | --- |")
    for row in rows:
        print("| " + " | ".join(row) + " |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
