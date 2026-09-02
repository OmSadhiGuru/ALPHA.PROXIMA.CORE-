#!/usr/bin/env python3
"""Generate Research Management Toolkit dashboards and indexes."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import re
import sys
from dataclasses import dataclass
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = Path("08_SYSTEMS/Research Management Toolkit")
PROGRAM_RE = re.compile(r"RP-\d{3}")


def load_vault_validator():
    spec = importlib.util.spec_from_file_location("vault_validator", TOOLKIT_DIR / "vault_validator.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load vault_validator.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = load_vault_validator()


@dataclass(frozen=True)
class ResearchProgram:
    program_id: str
    title: str
    status: str
    path: str
    master_index: str
    canonical_synthesis: str | None
    evidence_registry: str | None
    knowledge_graph: str | None
    open_questions: str | None
    future_research: str | None


def first_note_with(root: Path, program_dir: Path, text: str) -> str | None:
    matches = sorted(path for path in program_dir.rglob("*.md") if text in path.name)
    return matches[0].relative_to(root).as_posix() if matches else None


def program_title(note) -> str:
    title = note.frontmatter.get("research_program") or note.frontmatter.get("title") or note.path.stem
    return str(title)


def discover_programs(root: Path) -> list[ResearchProgram]:
    research_root = root / "07_RESEARCH"
    if not research_root.exists():
        return []
    notes_by_path = {note.relative_path: note for note in vault_validator.load_notes(root, False)}
    programs: list[ResearchProgram] = []
    for program_dir in sorted(path for path in research_root.iterdir() if path.is_dir() and PROGRAM_RE.fullmatch(path.name)):
        master_path = first_note_with(root, program_dir, "Master Index")
        note = notes_by_path.get(master_path) if master_path else None
        status = str(note.frontmatter.get("status", "unknown")) if note else "unknown"
        title = program_title(note) if note else program_dir.name
        programs.append(
            ResearchProgram(
                program_id=program_dir.name,
                title=title,
                status=status,
                path=program_dir.relative_to(root).as_posix(),
                master_index=master_path or "",
                canonical_synthesis=first_note_with(root, program_dir, "Canonical Synthesis"),
                evidence_registry=first_note_with(root, program_dir, "Evidence Registry"),
                knowledge_graph=first_note_with(root, program_dir, "Research Graph"),
                open_questions=first_note_with(root, program_dir, "Open Questions"),
                future_research=first_note_with(root, program_dir, "Future Research"),
            )
        )
    return programs


def wiki(path: str | None, label: str | None = None) -> str:
    if not path:
        return "Missing"
    stem = Path(path).with_suffix("").as_posix()
    return f"[[{stem}|{label or Path(path).stem}]]"


def status_bucket(program: ResearchProgram) -> str:
    status = program.status.lower()
    if status in {"active", "intake", "under_review"}:
        return "active"
    if status in {"accepted", "ratified", "completed", "archived"}:
        return "completed"
    if status in {"planned", "placeholder", "pending_delivery"}:
        return "planned"
    return "unknown"


def frontmatter(title: str, aliases: list[str], tags: list[str], artifact_type: str, related: list[str]) -> list[str]:
    today = dt.date.today().isoformat()
    return [
        "---",
        f'title: "{title}"',
        "aliases: [" + ", ".join(f'"{item}"' for item in aliases) + "]",
        "tags: [" + ", ".join(tags) + "]",
        f"created: {today}",
        f"updated: {today}",
        "status: active",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        f"artifact_type: {artifact_type}",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Research Governance Protocol]]", "[[Book III - Knowledge Integrity]]"]',
        "related_documents: [" + ", ".join(f'"[[{item}]]"' for item in related) + "]",
        "related_research_programs: []",
        "---",
        "",
    ]


def render_dashboard(programs: list[ResearchProgram]) -> str:
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    active = [item for item in programs if status_bucket(item) == "active"]
    completed = [item for item in programs if status_bucket(item) == "completed"]
    awaiting_synthesis = [item for item in programs if not item.canonical_synthesis]
    awaiting_review = [item for item in programs if item.status in {"under_review", "active"}]
    awaiting_institutionalization = [item for item in programs if item.canonical_synthesis and item.status != "ratified"]
    evidence_missing = [item for item in programs if not item.evidence_registry]
    lines = frontmatter(
        "Research Dashboard",
        ["Research Program Dashboard"],
        ["systems", "research", "dashboard", "alpha-proxima"],
        "research-dashboard",
        ["Research Index", "Research Lifecycle Diagram"],
    )
    lines.extend(
        [
            "# Research Dashboard",
            "",
            "## Purpose",
            "",
            "Provide an operational view of Alpha Proxima research programs without deciding research content.",
            "",
            "## Summary",
            "",
            f"- Generated: `{now}`",
            f"- Active Research Programs: `{len(active)}`",
            f"- Completed Programs: `{len(completed)}`",
            f"- Research Debt Items: `{len(awaiting_synthesis) + len(evidence_missing)}`",
            f"- Programs Awaiting Synthesis: `{len(awaiting_synthesis)}`",
            f"- Programs Awaiting Review: `{len(awaiting_review)}`",
            f"- Programs Awaiting Institutionalization: `{len(awaiting_institutionalization)}`",
            "",
            "## Active Research Programs",
            "",
            "| Program | Status | Master Index | Evidence Status |",
            "|---------|--------|--------------|-----------------|",
        ]
    )
    for program in active:
        evidence = "Present" if program.evidence_registry else "Missing"
        lines.append(f"| {program.program_id} - {program.title} | {program.status} | {wiki(program.master_index)} | {evidence} |")
    lines.extend(["", "## Completed Programs", "", "| Program | Status | Master Index |", "|---------|--------|--------------|"])
    for program in completed:
        lines.append(f"| {program.program_id} - {program.title} | {program.status} | {wiki(program.master_index)} |")
    lines.extend(["", "## Research Debt", "", "| Program | Debt | Recommended Engineering Action |", "|---------|------|-------------------------------|"])
    for program in programs:
        debts = []
        if not program.canonical_synthesis:
            debts.append("Missing canonical synthesis")
        if not program.evidence_registry:
            debts.append("Missing evidence registry")
        if not program.knowledge_graph:
            debts.append("Missing knowledge graph")
        if debts:
            lines.append(f"| {program.program_id} | {', '.join(debts)} | Generate or commission missing scaffold after authorization |")
    lines.extend(["", "## Evidence Status", "", "| Program | Evidence Registry |", "|---------|-------------------|"])
    for program in programs:
        lines.append(f"| {program.program_id} | {wiki(program.evidence_registry, 'Evidence Registry')} |")
    lines.extend(["", "## Programs Awaiting Synthesis", "", "| Program | Master Index |", "|---------|--------------|"])
    for program in awaiting_synthesis:
        lines.append(f"| {program.program_id} | {wiki(program.master_index)} |")
    lines.extend(["", "## Programs Awaiting Review", "", "| Program | Status |", "|---------|--------|"])
    for program in awaiting_review:
        lines.append(f"| {program.program_id} | {program.status} |")
    lines.extend(["", "## Programs Awaiting Institutionalization", "", "| Program | Canonical Synthesis |", "|---------|---------------------|"])
    for program in awaiting_institutionalization:
        lines.append(f"| {program.program_id} | {wiki(program.canonical_synthesis, 'Canonical Synthesis')} |")
    lines.extend(common_tail("Research dashboard generated."))
    return "\n".join(lines) + "\n"


def render_index(programs: list[ResearchProgram]) -> str:
    lines = frontmatter(
        "Research Index",
        ["Research Program Index"],
        ["systems", "research", "index", "alpha-proxima"],
        "research-index",
        ["Research Dashboard", "Research Lifecycle Diagram"],
    )
    lines.extend(
        [
            "# Research Index",
            "",
            "## Purpose",
            "",
            "Automatically link research programs to their core research management artifacts.",
            "",
            "## Program Index",
            "",
            "| Program | Commission | Artifacts | Canonical Synthesis | Evidence Registry | Knowledge Graph | Related Programs |",
            "|---------|------------|-----------|---------------------|-------------------|-----------------|------------------|",
        ]
    )
    for program in programs:
        lines.append(
            f"| {wiki(program.master_index, program.program_id)} | Missing | {program.path} | "
            f"{wiki(program.canonical_synthesis, 'Synthesis')} | {wiki(program.evidence_registry, 'Evidence')} | "
            f"{wiki(program.knowledge_graph, 'Graph')} | {', '.join(program_id for program_id in related_programs(program, programs)) or 'None listed'} |"
        )
    lines.extend(common_tail("Research index generated."))
    return "\n".join(lines) + "\n"


def related_programs(program: ResearchProgram, programs: list[ResearchProgram]) -> list[str]:
    return [item.program_id for item in programs if item.program_id != program.program_id and item.program_id in program.title]


def render_lifecycle() -> str:
    lines = frontmatter(
        "Research Lifecycle Diagram",
        ["Research Lifecycle"],
        ["systems", "research", "lifecycle", "diagram", "alpha-proxima"],
        "research-diagram",
        ["Research Dashboard", "Research Index"],
    )
    lines.extend(
        [
            "# Research Lifecycle Diagram",
            "",
            "## Purpose",
            "",
            "Describe the operational lifecycle that turns research questions into durable institutional memory and downstream applications.",
            "",
            "## Lifecycle",
            "",
            "```mermaid",
            "flowchart TD",
            '    A["Research Question"] --> B["Commission"]',
            '    B --> C["Independent Research"]',
            '    C --> D["Comparative Review"]',
            '    D --> E["Canonical Synthesis"]',
            '    E --> F["Knowledge Graph"]',
            '    F --> G["Institutional Memory"]',
            '    G --> H["Education"]',
            '    H --> I["Products"]',
            "```",
            "",
            "## Implementation Notes",
            "",
            "Engineering maintains the lifecycle infrastructure. Research Intelligence and governance determine research quality, review, and institutional adoption.",
        ]
    )
    lines.extend(common_tail("Research lifecycle diagram created."))
    return "\n".join(lines) + "\n"


def common_tail(summary: str) -> list[str]:
    today = dt.date.today().isoformat()
    return [
        "",
        "## Future Improvements",
        "",
        "- [ ] Add JSON data export for dashboards.",
        "- [ ] Add research program creation automation.",
        "- [ ] Add research debt trend history.",
        "",
        "## Version History",
        "",
        "| Version | Date | Author | Summary |",
        "|---------|------|--------|---------|",
        f"| 1.0.0 | {today} | [[CODEX]] | {summary} |",
    ]


def write(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"error: refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Research Management Toolkit output directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite generated dashboard/index/diagram.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser()
    if not output_dir.is_absolute():
        output_dir = root / output_dir
    programs = discover_programs(root)
    write(output_dir / "Research Dashboard.md", render_dashboard(programs), args.force)
    write(output_dir / "Research Index.md", render_index(programs), args.force)
    write(output_dir / "Research Lifecycle Diagram.md", render_lifecycle(), args.force)
    print(f"Research management files generated in: {output_dir}")
    print(f"Programs indexed: {len(programs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
