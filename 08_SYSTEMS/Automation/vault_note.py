#!/usr/bin/env python3
"""Create Alpha Proxima vault notes from approved templates."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

NOTE_TYPES = {
    "implementation": {
        "template": ROOT / "10_TEMPLATES" / "Implementation Note Template.md",
        "default_folder": ROOT / "08_SYSTEMS" / "Implementation Notes",
        "implementation_type": "technical",
    }
}


def slug_title(title: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|#^[\\]]+', "", title).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        raise ValueError("Title cannot be empty after filename cleanup.")
    return f"{cleaned}.md"


def extract_template_body(template_path: Path) -> str:
    text = template_path.read_text(encoding="utf-8")
    begin = "TEMPLATE BEGINS BELOW THIS LINE"
    end = "TEMPLATE ENDS ABOVE THIS LINE"
    if begin not in text or end not in text:
        raise ValueError(f"Template markers missing in {template_path}")
    lines = text.splitlines()
    start = next(index for index, line in enumerate(lines) if begin in line)
    stop = next(index for index, line in enumerate(lines) if end in line)
    body_lines = lines[start + 1 : stop]
    frontmatter_start = next(
        (
            index
            for index, line in enumerate(body_lines[:-1])
            if line.strip() == "---" and body_lines[index + 1].startswith("title:")
        ),
        None,
    )
    if frontmatter_start is None:
        raise ValueError(f"Generated note frontmatter missing in {template_path}")
    return "\n".join(body_lines[frontmatter_start:]).strip() + "\n"


def bullet_block(values: list[str], fallback: str) -> str:
    if not values:
        return fallback
    return "\n".join(f"- {value}" for value in values)


def build_note(args: argparse.Namespace) -> str:
    config = NOTE_TYPES[args.note_type]
    today = dt.date.today().isoformat()
    replacements = {
        "{{TITLE}}": args.title,
        "{{DATE}}": today,
        "{{AUTHOR}}": args.author,
        "{{IMPLEMENTATION_TYPE}}": args.implementation_type or config["implementation_type"],
        "{{PURPOSE}}": args.purpose,
        "{{DEPENDENCIES}}": bullet_block(args.dependency, "- N/A - no external dependency identified at draft time."),
        "{{RELATED_DOCUMENTS}}": bullet_block(args.related_document, "- [[Vault Structure Convention]]"),
        "{{RELATED_RESEARCH_PROGRAMS}}": bullet_block(args.related_research_program, "- N/A"),
        "{{IMPLEMENTATION_NOTES}}": args.implementation_notes,
        "{{FUTURE_IMPROVEMENTS}}": bullet_block(args.future_improvement, "- [ ] Review after first implementation pass."),
    }
    note = extract_template_body(config["template"])
    for token, value in replacements.items():
        note = note.replace(token, value)
    return note


def target_path(args: argparse.Namespace) -> Path:
    if args.output:
        output = Path(args.output)
        return output if output.is_absolute() else ROOT / output
    return NOTE_TYPES[args.note_type]["default_folder"] / slug_title(args.title)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note_type", choices=sorted(NOTE_TYPES))
    parser.add_argument("title")
    parser.add_argument("--author", default="CODEX")
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--implementation-type", default=None)
    parser.add_argument("--implementation-notes", default="[Describe the implementation approach, files, commands, and maintenance expectations.]")
    parser.add_argument("--dependency", action="append", default=[])
    parser.add_argument("--related-document", action="append", default=[])
    parser.add_argument("--related-research-program", action="append", default=[])
    parser.add_argument("--future-improvement", action="append", default=[])
    parser.add_argument("--output", help="Optional path relative to the vault root, or an absolute path.")
    parser.add_argument("--force", action="store_true", help="Overwrite the target file if it already exists.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    destination = target_path(args)
    if destination.exists() and not args.force:
        print(f"Refusing to overwrite existing file: {destination}", file=sys.stderr)
        return 1
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(build_note(args), encoding="utf-8")
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
