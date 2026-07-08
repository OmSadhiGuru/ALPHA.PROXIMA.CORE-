#!/usr/bin/env python3
"""Validate required YAML frontmatter keys in ALPHAPROXIMA Markdown files."""

from pathlib import Path
import sys
from typing import Dict, Optional

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_KEYS = [
    "title",
    "id",
    "department",
    "domain",
    "type",
    "status",
    "version",
    "created",
    "updated",
    "source",
    "tags",
    "related",
    "owner",
]


def frontmatter(text: str) -> Optional[Dict[str, str]]:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data: Dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors = []
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        metadata = frontmatter(text)
        if metadata is None:
            errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
            continue
        missing = [key for key in REQUIRED_KEYS if key not in metadata]
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing keys {', '.join(missing)}")

    if errors:
        print("Metadata validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Metadata validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
