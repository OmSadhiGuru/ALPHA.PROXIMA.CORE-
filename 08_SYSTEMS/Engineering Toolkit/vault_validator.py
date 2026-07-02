#!/usr/bin/env python3
"""Validate Alpha Proxima Obsidian Vault engineering standards."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_REPORT = Path("08_SYSTEMS/Engineering Toolkit/Reports/Vault Validation Report.md")
HIDDEN_DIRS = {".git", ".obsidian", ".smart-env", ".claude", ".claudian"}
REQUIRED_FIELDS = {
    "title",
    "aliases",
    "tags",
    "created",
    "updated",
    "status",
    "version",
    "authors",
    "artifact_type",
    "institutional_owner",
    "dependencies",
    "related_documents",
    "related_research_programs",
}
STATUS_VALUES = {"draft", "active", "under_review", "deprecated", "superseded", "archived"}
LIST_FIELDS = {"aliases", "tags", "authors", "dependencies", "related_documents", "related_research_programs"}
WIKI_LINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
FENCED_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
PLACEHOLDER_TARGETS = {"Author", "Founder", "Name", "Name or Role", "Note Title", "Target", "ADR-XXXX - Title"}


@dataclass(frozen=True)
class Issue:
    severity: str
    check: str
    path: str
    message: str


@dataclass
class Note:
    path: Path
    relative_path: str
    text: str
    body: str
    frontmatter: dict[str, object]
    frontmatter_errors: list[str]
    has_frontmatter: bool


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def iter_files(root: Path, include_hidden: bool) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if not include_hidden and any(part in HIDDEN_DIRS or part.startswith(".") for part in path.relative_to(root).parts):
            continue
        yield path


def markdown_files(root: Path, include_hidden: bool) -> list[Path]:
    return sorted(path for path in iter_files(root, include_hidden) if path.suffix.lower() == ".md")


def parse_scalar(value: str) -> object:
    value = value.strip()
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"').strip("'") for item in inner.split(",")]
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[bool, dict[str, object], str, list[str]]:
    if not text.startswith("---\n"):
        return False, {}, text, []

    lines = text.splitlines()
    closing_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return True, {}, "", ["frontmatter opening delimiter has no closing delimiter"]

    raw_lines = lines[1:closing_index]
    body = "\n".join(lines[closing_index + 1 :])
    data: dict[str, object] = {}
    errors: list[str] = []
    current_list_key: str | None = None

    for line_number, line in enumerate(raw_lines, start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if current_list_key and line.startswith("  - "):
            current_value = data.setdefault(current_list_key, [])
            if isinstance(current_value, list):
                current_value.append(parse_scalar(line[4:]))
            else:
                errors.append(f"line {line_number}: list item found for non-list field {current_list_key}")
            continue
        current_list_key = None
        if ":" not in line:
            errors.append(f"line {line_number}: unsupported YAML line")
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if not re.fullmatch(r"[a-z][a-z0-9_]*", key):
            errors.append(f"line {line_number}: field name should use lowercase snake_case: {key}")
        if key in data:
            errors.append(f"line {line_number}: duplicate field: {key}")
        if raw_value == "":
            data[key] = []
            current_list_key = key
        else:
            data[key] = parse_scalar(raw_value)

    return True, data, body, errors


def load_notes(root: Path, include_hidden: bool) -> list[Note]:
    notes: list[Note] = []
    for path in markdown_files(root, include_hidden):
        text = path.read_text(encoding="utf-8", errors="replace")
        has_frontmatter, frontmatter, body, errors = parse_frontmatter(text)
        notes.append(
            Note(
                path=path,
                relative_path=relative(path, root),
                text=text,
                body=body,
                frontmatter=frontmatter,
                frontmatter_errors=errors,
                has_frontmatter=has_frontmatter,
            )
        )
    return notes


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.split("|", 1)[0].rstrip("\\").split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target


def should_skip_link_target(target: str) -> bool:
    return (
        not target
        or "{{" in target
        or "}}" in target
        or "XXX" in target
        or "XXXX" in target
        or target in PLACEHOLDER_TARGETS
    )


def note_names(note: Note) -> set[str]:
    names = {note.path.stem, note.relative_path[:-3]}
    title = note.frontmatter.get("title")
    if isinstance(title, str) and title:
        names.add(title)
    return names


def strip_fenced_blocks(text: str) -> str:
    return FENCED_BLOCK_RE.sub("", text)


def target_exists(root: Path, note: Note, target: str, known_targets: set[str]) -> bool:
    if target in known_targets:
        return True
    if any(name.endswith(f"/{target}") for name in known_targets):
        return True

    candidates = [
        root / target,
        root / f"{target}.md",
        root / f"{target}.canvas",
        note.path.parent / target,
        note.path.parent / f"{target}.md",
        note.path.parent / f"{target}.canvas",
    ]
    return any(candidate.exists() for candidate in candidates)


def validate_frontmatter(notes: list[Note]) -> list[Issue]:
    issues: list[Issue] = []
    for note in notes:
        if not note.has_frontmatter:
            issues.append(Issue("error", "missing_yaml", note.relative_path, "Markdown note does not start with YAML frontmatter."))
            continue
        for error in note.frontmatter_errors:
            issues.append(Issue("error", "invalid_frontmatter", note.relative_path, error))
        for field in sorted(REQUIRED_FIELDS - set(note.frontmatter)):
            issues.append(Issue("warning", "missing_required_metadata", note.relative_path, f"Missing required frontmatter field: {field}"))
        status = note.frontmatter.get("status")
        if isinstance(status, str) and status not in STATUS_VALUES:
            issues.append(Issue("warning", "invalid_frontmatter", note.relative_path, f"Invalid status value: {status}"))
        for field in sorted(LIST_FIELDS & set(note.frontmatter)):
            if not isinstance(note.frontmatter[field], list):
                issues.append(Issue("warning", "invalid_frontmatter", note.relative_path, f"Field should be a list: {field}"))
    return issues


def validate_links(root: Path, notes: list[Note]) -> list[Issue]:
    issues: list[Issue] = []
    known_targets: set[str] = set()
    incoming: Counter[str] = Counter()
    path_by_name: dict[str, str] = {}

    for note in notes:
        for name in note_names(note):
            known_targets.add(name)
            path_by_name.setdefault(name, note.relative_path)

    for note in notes:
        searchable_text = strip_fenced_blocks(note.text)
        for raw_target in WIKI_LINK_RE.findall(searchable_text):
            target = normalize_link_target(raw_target)
            if should_skip_link_target(target):
                continue
            if not target_exists(root, note, target, known_targets):
                issues.append(Issue("error", "broken_wiki_link", note.relative_path, f"Missing wiki link target: [[{target}]]"))
                continue
            resolved_path = path_by_name.get(target)
            if not resolved_path:
                matching_name = next((name for name in known_targets if name.endswith(f"/{target}")), None)
                resolved_path = path_by_name.get(matching_name or "")
            if resolved_path:
                incoming[resolved_path] += 1

    for note in notes:
        if incoming[note.relative_path] == 0 and note.path.name not in {"README.md"}:
            issues.append(Issue("info", "missing_backlinks", note.relative_path, "No incoming wiki links found."))
    return issues


def validate_duplicate_filenames(root: Path, include_hidden: bool) -> list[Issue]:
    by_name: dict[str, list[str]] = defaultdict(list)
    for path in iter_files(root, include_hidden):
        by_name[path.name].append(relative(path, root))

    issues: list[Issue] = []
    for filename, paths in sorted(by_name.items()):
        if len(paths) > 1:
            for path in paths:
                issues.append(Issue("warning", "duplicate_filename", path, f"Duplicate filename appears in {len(paths)} locations: {filename}"))
    return issues


def validate_folder_placement(notes: list[Note]) -> list[Issue]:
    issues: list[Issue] = []
    for note in notes:
        path = note.relative_path
        name = note.path.name
        if name.startswith("ADR-") and not path.startswith("04_DECISIONS/"):
            issues.append(Issue("warning", "incorrect_folder_placement", path, "ADR files should live under 04_DECISIONS/."))
        if name.startswith("CN-") and not path.startswith("05_PROPOSALS/"):
            issues.append(Issue("warning", "incorrect_folder_placement", path, "Concept Notes should live under 05_PROPOSALS/."))
        if re.match(r"RP-\d{3}", name) and not path.startswith("07_RESEARCH/"):
            issues.append(Issue("warning", "incorrect_folder_placement", path, "Research program files should live under 07_RESEARCH/."))
        if name.endswith(" Template.md") and not (path.startswith("10_TEMPLATES/") or path.startswith("09_FUTURE/Templates/")):
            issues.append(Issue("warning", "incorrect_folder_placement", path, "Templates should live under 10_TEMPLATES/ or an approved office-local Templates/ folder."))
        if name.endswith(" Protocol.md") and not path.startswith("08_SYSTEMS/Protocols/"):
            issues.append(Issue("warning", "incorrect_folder_placement", path, "Protocols should live under 08_SYSTEMS/Protocols/."))
    return issues


def summarize_issues(issues: list[Issue]) -> dict[str, int]:
    summary = {"critical": 0, "error": 0, "warning": 0, "info": 0}
    for issue in issues:
        summary[issue.severity] = summary.get(issue.severity, 0) + 1
    return summary


def render_markdown_report(root: Path, notes: list[Note], issues: list[Issue]) -> str:
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    summary = summarize_issues(issues)
    by_check: dict[str, list[Issue]] = defaultdict(list)
    for issue in sorted(issues, key=lambda item: (item.check, item.path, item.message)):
        by_check[issue.check].append(issue)

    lines = [
        "---",
        'title: "Vault Validation Report"',
        "aliases: []",
        "tags: [systems, engineering, validation, report, alpha-proxima]",
        f"created: {dt.date.today().isoformat()}",
        f"updated: {dt.date.today().isoformat()}",
        "status: draft",
        'version: "0.1.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 001 - Vault Validator]]"]',
        'related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# Vault Validation Report",
        "",
        "## Purpose",
        "",
        "Report engineering quality issues detected by [[Tool 001 - Vault Validator]].",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Markdown notes scanned: `{len(notes)}`",
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
            for issue in check_issues:
                message = issue.message.replace("|", "\\|")
                lines.append(f"| {issue.severity} | `{issue.path}` | {message} |")
            lines.append("")

    lines.extend(
        [
            "## Implementation Notes",
            "",
            "This report is diagnostic. It does not approve, reject, move, or modify institutional documents.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Add baseline support for legacy validation debt.",
            "- [ ] Add JSON output for downstream automation.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 0.1.0 | {dt.date.today().isoformat()} | [[CODEX]] | Validation report generated |",
        ]
    )
    return "\n".join(lines) + "\n"


def validate(root: Path, include_hidden: bool) -> tuple[list[Note], list[Issue]]:
    notes = load_notes(root, include_hidden)
    issues: list[Issue] = []
    issues.extend(validate_frontmatter(notes))
    issues.extend(validate_links(root, notes))
    issues.extend(validate_duplicate_filenames(root, include_hidden))
    issues.extend(validate_folder_placement(notes))
    return notes, issues


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root. Defaults to current working directory.")
    parser.add_argument("--output", default=str(DEFAULT_REPORT), help="Markdown validation report output path.")
    parser.add_argument("--format", choices=["markdown"], default="markdown", help="Report format.")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden folders.")
    parser.add_argument("--fail-on", choices=["warning", "error"], help="Exit with code 1 when issues exist at or above this level.")
    parser.add_argument("--force", action="store_true", help="Overwrite the output report if it already exists.")
    return parser.parse_args(argv)


def should_fail(issues: list[Issue], fail_on: str | None) -> bool:
    if not fail_on:
        return False
    threshold = {"warning": 1, "error": 2}
    severity_rank = {"info": 0, "warning": 1, "error": 2, "critical": 3}
    return any(severity_rank[issue.severity] >= threshold[fail_on] for issue in issues)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"error: vault path is not a directory: {root}", file=sys.stderr)
        return 2

    notes, issues = validate(root, args.include_hidden)
    report = render_markdown_report(root, notes, issues)
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = root / output
    if output.exists() and not args.force:
        print(f"error: refusing to overwrite existing report: {output}", file=sys.stderr)
        print("hint: choose a different --output path or pass --force after reviewing the existing report.", file=sys.stderr)
        return 4
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    summary = summarize_issues(issues)
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
