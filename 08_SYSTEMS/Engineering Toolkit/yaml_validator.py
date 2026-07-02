#!/usr/bin/env python3
"""Validate Alpha Proxima Markdown YAML frontmatter."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
DEFAULT_REPORT = Path("08_SYSTEMS/Engineering Toolkit/Reports/YAML Validation Report.md")
DATE_FIELDS = {"created", "updated", "review_date"}
DEPRECATED_FIELDS = {
    "author": "authors",
    "created_by": "authors",
    "owner": "institutional_owner",
    "related_notes": "related_documents",
    "related_research": "related_research_programs",
}
OPTIONAL_FIELDS = {
    "standard_id",
    "template_type",
    "implementation_type",
    "research_id",
    "research_program",
    "evidence_class",
    "source_quality",
    "cognitive_function",
    "reasoning_engine",
    "review_owner",
    "review_date",
    "supersedes",
    "superseded_by",
    "future_id",
    "future_version",
    "origin",
    "priority",
    "affected_institutes",
    "affected_systems",
}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class YamlIssue:
    severity: str
    check: str
    path: str
    message: str


def load_vault_validator():
    module_path = TOOLKIT_DIR / "vault_validator.py"
    spec = importlib.util.spec_from_file_location("vault_validator", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load shared validator module: {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = load_vault_validator()


def issue(severity: str, check: str, path: str, message: str) -> YamlIssue:
    return YamlIssue(severity, check, path, message)


def first_h1(body: str) -> str | None:
    match = H1_RE.search(body)
    return match.group(1).strip() if match else None


def validate_note(note) -> list[YamlIssue]:
    issues: list[YamlIssue] = []
    if not note.has_frontmatter:
        return [issue("error", "missing_yaml", note.relative_path, "Markdown note does not start with YAML frontmatter.")]

    for error in note.frontmatter_errors:
        issues.append(issue("error", "invalid_frontmatter", note.relative_path, error))

    fields = set(note.frontmatter)
    for field in sorted(vault_validator.REQUIRED_FIELDS - fields):
        issues.append(issue("warning", "missing_required_metadata", note.relative_path, f"Missing required field: {field}"))

    known_fields = vault_validator.REQUIRED_FIELDS | OPTIONAL_FIELDS | set(DEPRECATED_FIELDS)
    for field in sorted(fields):
        if field in DEPRECATED_FIELDS:
            issues.append(issue("warning", "deprecated_field", note.relative_path, f"Deprecated field `{field}`; use `{DEPRECATED_FIELDS[field]}`."))
        elif field not in known_fields:
            issues.append(issue("info", "unknown_field", note.relative_path, f"Field is not defined in the current standard: {field}"))

    status = note.frontmatter.get("status")
    if isinstance(status, str) and status not in vault_validator.STATUS_VALUES:
        issues.append(issue("warning", "invalid_status", note.relative_path, f"Invalid status value: {status}"))

    version = note.frontmatter.get("version")
    if isinstance(version, str):
        if not SEMVER_RE.fullmatch(version):
            issues.append(issue("warning", "invalid_version", note.relative_path, f"Version should use semantic versioning: {version}"))
    elif version is not None:
        issues.append(issue("warning", "invalid_version", note.relative_path, "Version should be a quoted semantic version string."))

    for field in sorted(DATE_FIELDS & fields):
        value = note.frontmatter[field]
        if isinstance(value, str) and not DATE_RE.fullmatch(value):
            issues.append(issue("warning", "invalid_date", note.relative_path, f"{field} should be YYYY-MM-DD: {value}"))

    for field in sorted(vault_validator.LIST_FIELDS & fields):
        if not isinstance(note.frontmatter[field], list):
            issues.append(issue("warning", "invalid_list_field", note.relative_path, f"Field should be a list: {field}"))

    title = note.frontmatter.get("title")
    h1 = first_h1(note.body)
    if isinstance(title, str) and h1 and "{{" not in title and title != h1:
        issues.append(issue("info", "title_mismatch", note.relative_path, f"Frontmatter title `{title}` does not match H1 `{h1}`."))

    return issues


def summarize(issues: list[YamlIssue]) -> dict[str, int]:
    summary = {"critical": 0, "error": 0, "warning": 0, "info": 0}
    for item in issues:
        summary[item.severity] = summary.get(item.severity, 0) + 1
    return summary


def render_report(root: Path, note_count: int, issues: list[YamlIssue]) -> str:
    today = dt.date.today().isoformat()
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    summary = summarize(issues)
    by_check: dict[str, list[YamlIssue]] = defaultdict(list)
    for item in sorted(issues, key=lambda value: (value.check, value.path, value.message)):
        by_check[item.check].append(item)

    lines = [
        "---",
        'title: "YAML Validation Report"',
        "aliases: []",
        "tags: [systems, engineering, validation, yaml, report, alpha-proxima]",
        f"created: {today}",
        f"updated: {today}",
        "status: draft",
        'version: "0.1.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 002 - YAML Validator]]"]',
        'related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[02 - YAML Frontmatter Standard]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# YAML Validation Report",
        "",
        "## Purpose",
        "",
        "Report frontmatter quality issues detected by [[Tool 002 - YAML Validator]].",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Markdown notes scanned: `{note_count}`",
        f"- Critical: `{summary['critical']}`",
        f"- Errors: `{summary['error']}`",
        f"- Warnings: `{summary['warning']}`",
        f"- Info: `{summary['info']}`",
        "",
        "## Validation Results",
        "",
    ]

    if not issues:
        lines.extend(["No issues detected.", ""])
    else:
        for check, check_issues in sorted(by_check.items()):
            lines.extend([f"### {check}", "", "| Severity | Path | Message |", "|----------|------|---------|"])
            for item in check_issues:
                message = item.message.replace("|", "\\|")
                lines.append(f"| {item.severity} | `{item.path}` | {message} |")
            lines.append("")

    lines.extend(
        [
            "## Implementation Notes",
            "",
            "This report is diagnostic. It does not approve, reject, move, or modify institutional documents.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Add per-artifact schemas.",
            "- [ ] Add JSON output for automation.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 0.1.0 | {today} | [[CODEX]] | YAML validation report generated |",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root. Defaults to current working directory.")
    parser.add_argument("--output", default=str(DEFAULT_REPORT), help="Markdown validation report output path.")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden folders.")
    parser.add_argument("--fail-on", choices=["warning", "error"], help="Exit with code 1 when issues exist at or above this level.")
    parser.add_argument("--force", action="store_true", help="Overwrite the output report if it already exists.")
    return parser.parse_args(argv)


def should_fail(issues: list[YamlIssue], fail_on: str | None) -> bool:
    if not fail_on:
        return False
    threshold = {"warning": 1, "error": 2}
    severity_rank = {"info": 0, "warning": 1, "error": 2, "critical": 3}
    return any(severity_rank[item.severity] >= threshold[fail_on] for item in issues)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"error: vault path is not a directory: {root}", file=sys.stderr)
        return 2

    notes = vault_validator.load_notes(root, args.include_hidden)
    issues = [item for note in notes for item in validate_note(note)]
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = root / output
    if output.exists() and not args.force:
        print(f"error: refusing to overwrite existing report: {output}", file=sys.stderr)
        print("hint: choose a different --output path or pass --force after reviewing the existing report.", file=sys.stderr)
        return 4

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(root, len(notes), issues), encoding="utf-8")
    summary = summarize(issues)
    print(f"Report written: {output}")
    print(
        "Issues: "
        f"{summary['critical']} critical, "
        f"{summary['error']} errors, "
        f"{summary['warning']} warnings, "
        f"{summary['info']} info"
    )
    return 1 if should_fail(issues, args.fail_on) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
