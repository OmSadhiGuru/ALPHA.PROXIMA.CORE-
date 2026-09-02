#!/usr/bin/env python3
"""Analyze wiki-link and frontmatter dependency relationships in the vault."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import sys
from collections import defaultdict, deque
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
DEFAULT_REPORT = Path("08_SYSTEMS/Engineering Toolkit/Reports/Vault Dependency Report.md")


def load_vault_validator():
    spec = importlib.util.spec_from_file_location("vault_validator", TOOLKIT_DIR / "vault_validator.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load vault_validator.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = load_vault_validator()


def build_name_index(notes: list) -> dict[str, str]:
    index: dict[str, str] = {}
    for note in notes:
        for name in vault_validator.note_names(note):
            index.setdefault(name, note.relative_path)
    return index


def resolve(target: str, index: dict[str, str]) -> str | None:
    if target in index:
        return index[target]
    match = next((path for name, path in index.items() if name.endswith(f"/{target}")), None)
    return match


def graph(notes: list) -> tuple[dict[str, set[str]], list[tuple[str, str]]]:
    index = build_name_index(notes)
    edges: dict[str, set[str]] = defaultdict(set)
    broken: list[tuple[str, str]] = []
    for note in notes:
        text = vault_validator.strip_fenced_blocks(note.text)
        raw_targets = list(vault_validator.WIKI_LINK_RE.findall(text))
        deps = note.frontmatter.get("dependencies", [])
        if isinstance(deps, list):
            raw_targets.extend(str(dep).strip("[]") for dep in deps)
        for raw in raw_targets:
            target = vault_validator.normalize_link_target(raw)
            if vault_validator.should_skip_link_target(target):
                continue
            resolved = resolve(target, index)
            if resolved:
                edges[note.relative_path].add(resolved)
            else:
                broken.append((note.relative_path, target))
    return edges, broken


def find_cycles(edges: dict[str, set[str]], limit: int = 50) -> list[list[str]]:
    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(node: str) -> None:
        if len(cycles) >= limit:
            return
        if node in visiting:
            idx = stack.index(node)
            cycles.append(stack[idx:] + [node])
            return
        if node in visited:
            return
        visiting.add(node)
        stack.append(node)
        for target in edges.get(node, set()):
            visit(target)
        stack.pop()
        visiting.remove(node)
        visited.add(node)

    for node in sorted(edges):
        visit(node)
    return cycles


def clusters(notes: list, edges: dict[str, set[str]]) -> list[set[str]]:
    all_nodes = {note.relative_path for note in notes}
    undirected: dict[str, set[str]] = {node: set() for node in all_nodes}
    for source, targets in edges.items():
        for target in targets:
            undirected.setdefault(source, set()).add(target)
            undirected.setdefault(target, set()).add(source)
    seen: set[str] = set()
    result: list[set[str]] = []
    for node in sorted(all_nodes):
        if node in seen:
            continue
        group: set[str] = set()
        queue: deque[str] = deque([node])
        seen.add(node)
        while queue:
            current = queue.popleft()
            group.add(current)
            for nxt in undirected.get(current, set()):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        result.append(group)
    return sorted(result, key=len, reverse=True)


def render_report(root: Path, notes: list, edges: dict[str, set[str]], broken: list[tuple[str, str]]) -> str:
    today = dt.date.today().isoformat()
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    cycles = find_cycles(edges)
    groups = clusters(notes, edges)
    disconnected = [group for group in groups if len(group) == 1]
    lines = [
        "---",
        'title: "Vault Dependency Report"',
        "aliases: [\"Dependency Analyzer Report\"]",
        "tags: [systems, engineering, dependencies, graph, report, alpha-proxima]",
        f"created: {today}",
        f"updated: {today}",
        "status: draft",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 005 - Dependency Analyzer]]"]',
        'related_documents: ["[[Alpha Proxima Engineering Toolkit]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# Vault Dependency Report",
        "",
        "## Purpose",
        "",
        "Analyze wiki links and frontmatter dependencies for graph health.",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Notes analyzed: `{len(notes)}`",
        f"- Directed dependency edges: `{sum(len(value) for value in edges.values())}`",
        f"- Broken references: `{len(broken)}`",
        f"- Circular references found: `{len(cycles)}`",
        f"- Disconnected single-note clusters: `{len(disconnected)}`",
        f"- Connected clusters: `{len(groups)}`",
        "",
        "## Broken References",
        "",
        "| Source | Missing Target |",
        "|--------|----------------|",
    ]
    for source, target in broken[:200]:
        lines.append(f"| `{source}` | `[[{target}]]` |")
    lines.extend(["", "## Circular References", "", "| Cycle |", "|-------|"])
    for cycle in cycles[:50]:
        lines.append(f"| {' -> '.join(f'`{item}`' for item in cycle)} |")
    lines.extend(["", "## Largest Clusters", "", "| Size | Example Notes |", "|------|---------------|"])
    for group in groups[:20]:
        examples = "<br>".join(f"`{item}`" for item in sorted(group)[:5])
        lines.append(f"| `{len(group)}` | {examples} |")
    lines.extend(
        [
            "",
            "## Implementation Notes",
            "",
            "Circular references are not automatically errors. They identify dependency loops that may need human review.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Add graph export formats.",
            "- [ ] Add dependency severity rules.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 1.0.0 | {today} | [[CODEX]] | Dependency report generated |",
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
    edges, broken = graph(notes)
    output = Path(args.output).expanduser()
    if not output.is_absolute():
        output = root / output
    if output.exists() and not args.force:
        print(f"error: refusing to overwrite existing report: {output}", file=sys.stderr)
        return 4
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(root, notes, edges, broken), encoding="utf-8")
    print(f"Report written: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
