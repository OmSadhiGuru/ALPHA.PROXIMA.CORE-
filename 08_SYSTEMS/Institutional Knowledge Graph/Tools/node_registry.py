#!/usr/bin/env python3
"""Generate the Alpha Proxima Institutional Knowledge Graph node registry."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


TOOL_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT = Path("08_SYSTEMS/Institutional Knowledge Graph/Tools/node_registry.json")
DEFAULT_REPORT = Path("08_SYSTEMS/Institutional Knowledge Graph/Tools/Node Registry Report.md")
VAULT_VALIDATOR_PATH = TOOL_DIR.parents[1] / "Engineering Toolkit" / "vault_validator.py"

ARTIFACT_TYPE_MAP = {
    "archive-record": "research_artifact",
    "canonical-synthesis": "canonical_synthesis",
    "canonical-synthesis-template": "canonical_synthesis",
    "charter": "charter",
    "constitution": "policy",
    "constitutional-book": "policy",
    "council-placeholder": "office",
    "engineering-architecture": "standard",
    "engineering-assessment": "standard",
    "engineering-program": "standard",
    "engineering-report": "engineering_tool",
    "engineering-roadmap": "standard",
    "engineering-standard": "standard",
    "evidence-registry": "evidence_claim",
    "evidence-registry-template": "evidence_claim",
    "future-index": "future_research",
    "future-research-template": "future_research",
    "governance-framework": "policy",
    "implementation-note": "engineering_tool",
    "institutional-office": "office",
    "open-questions-template": "open_question",
    "operations-index": "standing_order",
    "operations-registry": "office",
    "person-profile": "person",
    "protocol": "policy",
    "research-artifact-template": "research_artifact",
    "research-commission-template": "research_commission",
    "research-dashboard": "standard",
    "research-diagram": "standard",
    "research-index": "standard",
    "research-program-index": "research_program",
    "research-program-template": "research_program",
    "research-timeline-template": "standard",
    "template": "standard",
    "visual-system-standard": "standard",
    "readme": "standard",
    "version-history": "standard",
}


def load_vault_validator():
    spec = importlib.util.spec_from_file_location("vault_validator", VAULT_VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load shared validator module: {VAULT_VALIDATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = load_vault_validator()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def node_id(node_type: str, path: str, title: str) -> str:
    stable = slugify(title or Path(path).stem)
    digest = hashlib.sha1(path.encode("utf-8")).hexdigest()[:8]
    return f"apkg:{node_type}:{stable}-{digest}"


def first_h1(body: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    return match.group(1).strip() if match else None


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if value in (None, ""):
        return []
    return [str(value)]


def infer_node_type(note) -> tuple[str, float, list[str]]:
    path = note.relative_path
    name = note.path.name
    stem = note.path.stem
    artifact_type = str(note.frontmatter.get("artifact_type", "")).strip()
    reasons: list[str] = []

    if artifact_type in ARTIFACT_TYPE_MAP:
        reasons.append(f"artifact_type:{artifact_type}")
        return ARTIFACT_TYPE_MAP[artifact_type], 0.9, reasons

    if name.endswith(" Charter.md"):
        return "charter", 0.85, ["filename:charter"]
    if path.startswith("07_RESEARCH/") and re.match(r"RP-\d{3} Master Index", name):
        return "research_program", 0.9, ["folder:07_RESEARCH", "filename:master_index"]
    if "Canonical Synthesis" in name:
        return "canonical_synthesis", 0.85, ["filename:canonical_synthesis"]
    if "Evidence Registry" in name:
        return "evidence_claim", 0.75, ["filename:evidence_registry"]
    if "Open Questions" in name:
        return "open_question", 0.75, ["filename:open_questions"]
    if "Future Research" in name or "Future Sources" in name:
        return "future_research", 0.7, ["filename:future_research"]
    if "Source Note" in name or path.startswith("07_RESEARCH/") and "/ARCHIVE/" in path:
        return "research_artifact", 0.75, ["folder:research_source_or_archive"]
    if "/13 Research Graph/Concepts/" in path:
        if any(token in stem.lower() for token in ["theory", "processing", "inference", "panpsychism", "illusionism"]):
            return "theory", 0.65, ["folder:research_graph_concepts", "filename:theory_signal"]
        return "concept", 0.65, ["folder:research_graph_concepts"]
    if path.startswith("09_PEOPLE/"):
        return "person", 0.8, ["folder:09_PEOPLE"]
    if path.startswith("08_SYSTEMS/Engineering Toolkit/Tool "):
        return "engineering_tool", 0.85, ["folder:engineering_toolkit", "filename:tool"]
    if path.startswith("08_SYSTEMS/Engineering Standards/"):
        return "standard", 0.85, ["folder:engineering_standards"]
    if path.startswith("11_OPERATIONS/Office Registry/"):
        return "office", 0.75, ["folder:office_registry"]
    if path.startswith("08_SYSTEMS/Protocols/"):
        return "policy", 0.75, ["folder:protocols"]
    if path.startswith("05_PROPOSALS/") or "Founder" in name:
        return "founder_directive", 0.55, ["folder:proposals_or_founder_signal"]

    return "unknown", 0.0, ["no_confident_rule"]


def wiki_links(note) -> list[str]:
    text = vault_validator.strip_fenced_blocks(note.text)
    links: list[str] = []
    for raw in vault_validator.WIKI_LINK_RE.findall(text):
        target = vault_validator.normalize_link_target(raw)
        if target and not vault_validator.should_skip_link_target(target):
            links.append(target)
    return sorted(set(links))


def make_node(note) -> dict[str, Any]:
    title = note.frontmatter.get("title")
    if not isinstance(title, str) or not title:
        title = first_h1(note.body) or note.path.stem
    node_type, confidence, reasons = infer_node_type(note)
    return {
        "node_id": node_id(node_type, note.relative_path, title),
        "node_type": node_type,
        "node_type_confidence": confidence,
        "node_type_reasons": reasons,
        "source_path": note.relative_path,
        "title": title,
        "yaml": note.frontmatter,
        "has_yaml": note.has_frontmatter,
        "frontmatter_errors": note.frontmatter_errors,
        "artifact_type": note.frontmatter.get("artifact_type"),
        "institutional_owner": note.frontmatter.get("institutional_owner"),
        "cognitive_function": note.frontmatter.get("cognitive_function"),
        "related_documents": as_list(note.frontmatter.get("related_documents")),
        "related_research_programs": as_list(note.frontmatter.get("related_research_programs")),
        "wiki_links": wiki_links(note),
        "tags": as_list(note.frontmatter.get("tags")),
        "status": note.frontmatter.get("status"),
        "version": note.frontmatter.get("version"),
        "provenance": {
            "source": "markdown_scan",
            "generated_by": "node_registry.py",
            "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        },
    }


def registry_payload(root: Path, nodes: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "registry_version": "1.0.0",
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "vault": str(root),
        "node_count": len(nodes),
        "principle": "The Node Registry is the first bridge between Markdown memory and LUMIAION's future institutional graph.",
        "nodes": nodes,
    }


def render_report(root: Path, nodes: list[dict[str, Any]]) -> str:
    today = dt.date.today().isoformat()
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    by_type = Counter(str(node["node_type"]) for node in nodes)
    missing_yaml = [node for node in nodes if not node["has_yaml"]]
    unknown = [node for node in nodes if node["node_type"] == "unknown"]
    cleanup = [node for node in nodes if not node["has_yaml"] or node["node_type"] == "unknown" or not node.get("artifact_type")]
    lines = [
        "---",
        'title: "Node Registry Report"',
        "aliases: [\"Institutional Knowledge Graph Node Registry Report\"]",
        "tags: [systems, engineering, knowledge-graph, node-registry, report, alpha-proxima]",
        f"created: {today}",
        f"updated: {today}",
        "status: draft",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 010 - Node Registry Generator]]", "[[Node Taxonomy]]"]',
        'related_documents: ["[[Engineering Program EP-001 - Institutional Knowledge Graph]]", "[[Knowledge Graph Architecture v1.0]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# Node Registry Report",
        "",
        "## Purpose",
        "",
        "Summarize graph node candidates discovered by [[Tool 010 - Node Registry Generator]].",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Total nodes discovered: `{len(nodes)}`",
        f"- Unknown node types: `{len(unknown)}`",
        f"- Missing YAML: `{len(missing_yaml)}`",
        f"- High-value cleanup candidates: `{len(cleanup)}`",
        "",
        "## Nodes by Type",
        "",
        "| Node Type | Count |",
        "|-----------|-------|",
    ]
    for node_type, count in sorted(by_type.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{node_type}` | `{count}` |")
    lines.extend(["", "## Unknown Node Types", "", "| Source Path | Title | Reason |", "|-------------|-------|--------|"])
    for node in unknown[:100]:
        title = str(node["title"]).replace("|", "\\|")
        reasons = ", ".join(node["node_type_reasons"])
        lines.append(f"| `{node['source_path']}` | {title} | {reasons} |")
    lines.extend(["", "## Missing YAML", "", "| Source Path | Title |", "|-------------|-------|"])
    for node in missing_yaml[:100]:
        title = str(node["title"]).replace("|", "\\|")
        lines.append(f"| `{node['source_path']}` | {title} |")
    lines.extend(["", "## High-Value Cleanup Candidates", "", "| Source Path | Issue |", "|-------------|-------|"])
    for node in cleanup[:100]:
        issues = []
        if not node["has_yaml"]:
            issues.append("missing YAML")
        if node["node_type"] == "unknown":
            issues.append("unknown node type")
        if not node.get("artifact_type"):
            issues.append("missing artifact_type")
        lines.append(f"| `{node['source_path']}` | {', '.join(issues)} |")
    lines.extend(
        [
            "",
            "## Recommendations for ES-006",
            "",
            "- Build the Relationship Extractor using this registry as the node lookup table.",
            "- Convert wiki links into candidate `REFERENCES` relationships.",
            "- Convert YAML `dependencies` into candidate `REQUIRES` relationships.",
            "- Preserve extraction confidence and provenance on every relationship.",
            "- Do not promote inferred relationships to canonical status without review.",
            "",
            "## Implementation Notes",
            "",
            "This report is generated from a read-only Markdown scan. It does not modify notes or create canonical claims.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Add configurable node inference rules.",
            "- [ ] Add schema validation against [[Node Taxonomy]].",
            "- [ ] Add stable ID override support in YAML.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 1.0.0 | {today} | [[CODEX]] | Node registry report generated |",
        ]
    )
    return "\n".join(lines) + "\n"


def write_text(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"error: refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root. Defaults to current working directory.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="JSON registry output path.")
    parser.add_argument("--report", default=str(DEFAULT_REPORT), help="Markdown report output path.")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden/tool-managed folders.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing registry/report.")
    return parser.parse_args(argv)


def resolve_output(root: Path, raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = root / path
    return path


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    notes = vault_validator.load_notes(root, args.include_hidden)
    nodes = [make_node(note) for note in notes]
    output = resolve_output(root, args.output)
    report = resolve_output(root, args.report)
    write_text(output, json.dumps(registry_payload(root, nodes), indent=2, ensure_ascii=False) + "\n", args.force)
    write_text(report, render_report(root, nodes), args.force)
    print(f"Node registry written: {output}")
    print(f"Node registry report written: {report}")
    print(f"Nodes discovered: {len(nodes)}")
    print(f"Unknown node types: {sum(1 for node in nodes if node['node_type'] == 'unknown')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
