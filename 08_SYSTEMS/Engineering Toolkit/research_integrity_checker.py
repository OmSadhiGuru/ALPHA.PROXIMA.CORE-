#!/usr/bin/env python3
"""Check research program folders for expected structural components."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import re
import sys
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
DEFAULT_REPORT = Path("08_SYSTEMS/Engineering Toolkit/Reports/Research Integrity Report.md")
COMPONENTS = {
    "master_index": "Master Index",
    "canonical_synthesis": "Canonical Synthesis",
    "evidence_registry": "Evidence Registry",
    "source_notes": "Source Note",
    "source_registry": "Source Registry",
}


def load_vault_validator():
    spec = importlib.util.spec_from_file_location("vault_validator", TOOLKIT_DIR / "vault_validator.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load vault_validator.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = load_vault_validator()


def program_dirs(root: Path) -> list[Path]:
    research_root = root / "07_RESEARCH"
    if not research_root.exists():
        return []
    return sorted(path for path in research_root.iterdir() if path.is_dir() and re.fullmatch(r"RP-\d{3}", path.name))


def program_status(program: Path) -> dict[str, bool]:
    files = list(program.rglob("*.md"))
    names = "\n".join(path.name for path in files)
    text = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in files)
    return {
        "master_index": any("Master Index" in path.name for path in files),
        "canonical_synthesis": "Canonical Synthesis" in names,
        "evidence_registry": "Evidence Registry" in names,
        "source_notes": "Source Note" in names,
        "source_registry": "Source Registry" in names,
        "cross_links": "[[" in text,
    }


def render_report(root: Path, programs: list[Path]) -> str:
    today = dt.date.today().isoformat()
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    rows = [(program.name, program_status(program)) for program in programs]
    missing_total = sum(1 for _, status in rows for key in COMPONENTS if not status[key])
    lines = [
        "---",
        'title: "Research Integrity Report"',
        "aliases: [\"Research Integrity Checker Report\"]",
        "tags: [systems, engineering, research, integrity, report, alpha-proxima]",
        f"created: {today}",
        f"updated: {today}",
        "status: draft",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 007 - Research Integrity Checker]]"]',
        'related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Research Governance Protocol]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# Research Integrity Report",
        "",
        "## Purpose",
        "",
        "Check research program folders for required structural artifacts and cross-linking signals.",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Research programs checked: `{len(rows)}`",
        f"- Missing core components: `{missing_total}`",
        "",
        "## Program Checks",
        "",
        "| Program | Master Index | Canonical Synthesis | Evidence Registry | Source Notes | Source Registry | Cross Links |",
        "|---------|--------------|---------------------|-------------------|--------------|-----------------|-------------|",
    ]
    for program, status in rows:
        values = ["yes" if status[key] else "missing" for key in ["master_index", "canonical_synthesis", "evidence_registry", "source_notes", "source_registry", "cross_links"]]
        lines.append(f"| {program} | " + " | ".join(values) + " |")
    lines.extend(
        [
            "",
            "## Implementation Notes",
            "",
            "This checker verifies research infrastructure. It does not evaluate scientific validity.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Add research phase-specific schemas.",
            "- [ ] Add source-to-claim traceability scoring.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 1.0.0 | {today} | [[CODEX]] | Research integrity report generated |",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".")
    parser.add_argument("--output", default=str(DEFAULT_REPORT))
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = root / output
    if output.exists() and not args.force:
        print(f"error: refusing to overwrite existing report: {output}", file=sys.stderr)
        return 4
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(root, program_dirs(root)), encoding="utf-8")
    print(f"Report written: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
