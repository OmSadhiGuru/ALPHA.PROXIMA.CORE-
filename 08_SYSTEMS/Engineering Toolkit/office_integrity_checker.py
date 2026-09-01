#!/usr/bin/env python3
"""Check whether institutional offices have expected operational components."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import sys
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
DEFAULT_REPORT = Path("08_SYSTEMS/Engineering Toolkit/Reports/Office Integrity Report.md")
REQUIRED_COMPONENTS = ["charter", "authority", "owner", "relationships", "standing orders", "active"]


def load_vault_validator():
    spec = importlib.util.spec_from_file_location("vault_validator", TOOLKIT_DIR / "vault_validator.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load vault_validator.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = load_vault_validator()


def office_candidates(root: Path, notes: list) -> dict[str, list]:
    candidates: dict[str, list] = {}
    for note in notes:
        path = Path(note.relative_path)
        if path.parts[:1] == ("11_OPERATIONS",) and len(path.parts) >= 2:
            office = path.parts[1]
            if office not in {"README.md"}:
                candidates.setdefault(office, []).append(note)
        if "Office" in note.path.name or "Council" in note.path.name or "Charter" in note.path.name:
            owner = path.parts[0] if path.parts else "root"
            candidates.setdefault(owner, []).append(note)
    return dict(sorted(candidates.items()))


def component_status(notes: list) -> dict[str, bool]:
    text = "\n".join(note.text.lower() for note in notes)
    names = " ".join(note.path.name.lower() for note in notes)
    return {
        "charter": "charter" in text or "charter" in names,
        "authority": "authority" in text,
        "owner": "owner" in text or "institutional_owner" in text,
        "relationships": "relationships" in text or "dependencies" in text,
        "standing orders": "standing orders" in text,
        "active": "status: active" in text or "active status" in text,
    }


def render_report(root: Path, offices: dict[str, list]) -> str:
    today = dt.date.today().isoformat()
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    rows: list[tuple[str, dict[str, bool]]] = [(office, component_status(notes)) for office, notes in offices.items()]
    missing_total = sum(1 for _, status in rows for value in status.values() if not value)
    lines = [
        "---",
        'title: "Office Integrity Report"',
        "aliases: [\"Office Integrity Checker Report\"]",
        "tags: [systems, engineering, operations, offices, integrity, report, alpha-proxima]",
        f"created: {today}",
        f"updated: {today}",
        "status: draft",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 006 - Office Integrity Checker]]"]',
        'related_documents: ["[[Office Registry]]", "[[Alpha Proxima Engineering Toolkit]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# Office Integrity Report",
        "",
        "## Purpose",
        "",
        "Verify whether office-related areas expose the operational components needed for maintainable institutional work.",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Office candidates checked: `{len(rows)}`",
        f"- Missing components: `{missing_total}`",
        "",
        "## Office Checks",
        "",
        "| Office | Charter | Authority | Owner | Relationships | Standing Orders | Active Status |",
        "|--------|---------|-----------|-------|---------------|-----------------|---------------|",
    ]
    for office, status in rows:
        values = ["yes" if status[item] else "missing" for item in REQUIRED_COMPONENTS]
        lines.append(f"| {office} | " + " | ".join(values) + " |")
    lines.extend(
        [
            "",
            "## Implementation Notes",
            "",
            "This checker reports missing operational components. It does not create offices or define authority.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Use a formal Office Registry schema.",
            "- [ ] Add per-office standing order templates.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 1.0.0 | {today} | [[CODEX]] | Office integrity report generated |",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".")
    parser.add_argument("--output", default=str(DEFAULT_REPORT))
    parser.add_argument("--include-hidden", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    notes = vault_validator.load_notes(root, args.include_hidden)
    offices = office_candidates(root, notes)
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = root / output
    if output.exists() and not args.force:
        print(f"error: refusing to overwrite existing report: {output}", file=sys.stderr)
        return 4
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(root, offices), encoding="utf-8")
    print(f"Report written: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
