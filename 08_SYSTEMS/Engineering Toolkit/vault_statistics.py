#!/usr/bin/env python3
"""Generate an Engineering Dashboard Report for the Alpha Proxima Vault."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import sys
from collections import Counter
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
DEFAULT_REPORT = Path("08_SYSTEMS/Engineering Toolkit/Reports/Engineering Dashboard Report.md")


def load_vault_validator():
    spec = importlib.util.spec_from_file_location("vault_validator", TOOLKIT_DIR / "vault_validator.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load vault_validator.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = load_vault_validator()


def count_missing_metadata(notes: list) -> int:
    return sum(len(vault_validator.REQUIRED_FIELDS - set(note.frontmatter)) if note.has_frontmatter else len(vault_validator.REQUIRED_FIELDS) for note in notes)


def render_counter(title: str, counter: Counter[str]) -> list[str]:
    lines = [f"## {title}", "", "| Value | Count |", "|-------|-------|"]
    for value, count in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {value or 'unspecified'} | `{count}` |")
    lines.append("")
    return lines


def render_report(root: Path, notes: list, issues: list) -> str:
    today = dt.date.today().isoformat()
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    by_office = Counter(Path(note.relative_path).parts[0] if "/" in note.relative_path else "root" for note in notes)
    by_artifact = Counter(str(note.frontmatter.get("artifact_type", "")) for note in notes if note.has_frontmatter)
    by_status = Counter(str(note.frontmatter.get("status", "")) for note in notes if note.has_frontmatter)
    by_version = Counter(str(note.frontmatter.get("version", "")) for note in notes if note.has_frontmatter)
    orphan_count = sum(1 for issue in issues if issue.check == "missing_backlinks")
    programs = [note for note in notes if "research_program" in note.frontmatter or Path(note.relative_path).name.startswith("RP-")]
    charters = [note for note in notes if "Charter" in note.path.name]
    reports = [note for note in notes if str(note.frontmatter.get("artifact_type", "")) == "engineering-report" or "Report" in note.path.name]

    lines = [
        "---",
        'title: "Engineering Dashboard Report"',
        "aliases: [\"Vault Statistics\", \"Engineering Dashboard\"]",
        "tags: [systems, engineering, statistics, dashboard, report, alpha-proxima]",
        f"created: {today}",
        f"updated: {today}",
        "status: draft",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 004 - Vault Statistics Generator]]"]',
        'related_documents: ["[[Alpha Proxima Engineering Toolkit]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# Engineering Dashboard Report",
        "",
        "## Purpose",
        "",
        "Summarize vault structure, metadata coverage, and engineering health indicators.",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Total notes: `{len(notes)}`",
        f"- Missing metadata fields: `{count_missing_metadata(notes)}`",
        f"- Orphan documents: `{orphan_count}`",
        f"- Research program-related notes: `{len(programs)}`",
        f"- Charters: `{len(charters)}`",
        f"- Reports: `{len(reports)}`",
        "",
    ]
    lines.extend(render_counter("Notes by Office", by_office))
    lines.extend(render_counter("Notes by Artifact Type", by_artifact))
    lines.extend(render_counter("Active vs Archived", by_status))
    lines.extend(render_counter("Version Distribution", by_version))
    lines.extend(
        [
            "## Implementation Notes",
            "",
            "This dashboard is descriptive. It does not evaluate institutional quality or approve content.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Add trend history.",
            "- [ ] Add graph density metrics.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 1.0.0 | {today} | [[CODEX]] | Engineering dashboard report generated |",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root.")
    parser.add_argument("--output", default=str(DEFAULT_REPORT), help="Report output path.")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden/tool-managed folders.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing report.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    notes, issues = vault_validator.validate(root, args.include_hidden)
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = root / output
    if output.exists() and not args.force:
        print(f"error: refusing to overwrite existing report: {output}", file=sys.stderr)
        return 4
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(root, notes, issues), encoding="utf-8")
    print(f"Report written: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
