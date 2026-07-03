#!/usr/bin/env python3
"""Extract candidate relationships for the Institutional Knowledge Graph."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


TOOL_DIR = Path(__file__).resolve().parent
DEFAULT_NODE_REGISTRY = Path("08_SYSTEMS/Institutional Knowledge Graph/Tools/node_registry.json")
DEFAULT_OUTPUT = Path("08_SYSTEMS/Institutional Knowledge Graph/Tools/relationship_registry.json")
DEFAULT_REPORT = Path("08_SYSTEMS/Institutional Knowledge Graph/Tools/Relationship Registry Report.md")


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def stable_relationship_id(source_id: str, rel_type: str, target: str, source_kind: str, source_detail: str | None) -> str:
    digest = hashlib.sha1(f"{source_id}|{rel_type}|{target}|{source_kind}|{source_detail or ''}".encode("utf-8")).hexdigest()[:10]
    return f"apkg:rel:{rel_type.lower()}:{digest}"


def normalize_link(raw: str) -> str:
    value = raw.strip()
    if value.startswith("[[") and value.endswith("]]"):
        value = value[2:-2]
    value = value.split("|", 1)[0].split("#", 1)[0].strip()
    if value.endswith(".md"):
        value = value[:-3]
    return value


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if value in (None, ""):
        return []
    return [str(value)]


class NodeLookup:
    def __init__(self, nodes: list[dict[str, Any]]):
        self.nodes = nodes
        self.by_id = {node["node_id"]: node for node in nodes}
        self.by_key: dict[str, dict[str, Any]] = {}
        for node in nodes:
            self.add(node["source_path"], node)
            self.add(str(Path(node["source_path"]).with_suffix("")), node)
            self.add(Path(node["source_path"]).stem, node)
            self.add(str(node.get("title", "")), node)
            for alias in as_list(node.get("yaml", {}).get("aliases")):
                self.add(alias, node)

    def add(self, key: str, node: dict[str, Any]) -> None:
        key = key.strip()
        if not key:
            return
        self.by_key.setdefault(key, node)
        self.by_key.setdefault(key.lower(), node)

    def resolve(self, raw_target: str) -> dict[str, Any] | None:
        target = normalize_link(raw_target)
        if not target:
            return None
        if target in self.by_key:
            return self.by_key[target]
        if target.lower() in self.by_key:
            return self.by_key[target.lower()]
        target_name = Path(target).name
        if target_name in self.by_key:
            return self.by_key[target_name]
        matches = [node for key, node in self.by_key.items() if key.endswith(f"/{target}") or key.endswith(f"/{target_name}")]
        return matches[0] if matches else None


def relationship(
    source: dict[str, Any],
    rel_type: str,
    target_node: dict[str, Any] | None,
    target_raw: str,
    source_kind: str,
    confidence: float,
    status: str = "inferred",
    evidence: str | None = None,
    source_detail: str | None = None,
) -> dict[str, Any]:
    target_id = target_node["node_id"] if target_node else None
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    return {
        "relationship_id": stable_relationship_id(source["node_id"], rel_type, target_id or target_raw, source_kind, source_detail),
        "relationship_type": rel_type,
        "source_node_id": source["node_id"],
        "source_path": source["source_path"],
        "target_node_id": target_id,
        "target_path": target_node.get("source_path") if target_node else None,
        "target_raw": target_raw,
        "status": status,
        "confidence": confidence,
        "relationship_source": source_kind,
        "source_detail": source_detail,
        "evidence": evidence,
        "created": now,
        "updated": now,
    }


def add_unique(relationships: list[dict[str, Any]], seen: set[str], rel: dict[str, Any]) -> None:
    if rel["relationship_id"] in seen:
        return
    seen.add(rel["relationship_id"])
    relationships.append(rel)


def extract_relationships(nodes: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    lookup = NodeLookup(nodes)
    relationships: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    seen: set[str] = set()

    for node in nodes:
        for link in node.get("wiki_links", []):
            target = lookup.resolve(link)
            rel = relationship(node, "REFERENCES", target, link, "wiki_link", 0.75 if target else 0.2)
            if target:
                add_unique(relationships, seen, rel)
            else:
                unresolved.append(rel)

        for target_raw in as_list(node.get("related_documents")):
            target = lookup.resolve(target_raw)
            rel = relationship(node, "RELATED_TO", target, target_raw, "yaml_field", 0.8 if target else 0.25, source_detail="related_documents")
            if target:
                add_unique(relationships, seen, rel)
            else:
                unresolved.append(rel)

        for target_raw in as_list(node.get("yaml", {}).get("dependencies")):
            target = lookup.resolve(target_raw)
            rel_type = "REQUIRES" if target else "DEPENDS_ON"
            rel = relationship(node, rel_type, target, target_raw, "yaml_field", 0.85 if target else 0.25, source_detail="dependencies")
            if target:
                add_unique(relationships, seen, rel)
            else:
                unresolved.append(rel)

        for program in as_list(node.get("related_research_programs")):
            target = lookup.resolve(program)
            rel = relationship(node, "RELATED_TO", target, program, "yaml_field", 0.7 if target else 0.2, source_detail="related_research_programs")
            if target:
                add_unique(relationships, seen, rel)
            else:
                unresolved.append(rel)

        owner = node.get("institutional_owner")
        if owner:
            target = lookup.resolve(str(owner))
            rel = relationship(node, "OWNED_BY", target, str(owner), "yaml_field", 0.65 if target else 0.2, source_detail="institutional_owner")
            if target:
                add_unique(relationships, seen, rel)
            else:
                unresolved.append(rel)

        for author in as_list(node.get("yaml", {}).get("authors")):
            target = lookup.resolve(author)
            rel = relationship(node, "PRODUCED_BY", target, author, "yaml_field", 0.7 if target else 0.2, source_detail="authors")
            if target:
                add_unique(relationships, seen, rel)
            else:
                unresolved.append(rel)

        source_path = Path(node["source_path"])
        parts = source_path.parts
        for depth in range(1, len(parts)):
            parent_path = "/".join(parts[:depth])
            parent = lookup.resolve(parent_path)
            if parent and parent["node_id"] != node["node_id"]:
                add_unique(relationships, seen, relationship(node, "PART_OF", parent, parent_path, "folder_inference", 0.55))
                break

        title = str(node.get("title", ""))
        if "Template" in title and node["node_type"] == "standard":
            target = lookup.resolve("10 - Template Standard")
            if target:
                add_unique(relationships, seen, relationship(node, "IMPLEMENTS", target, "10 - Template Standard", "filename_inference", 0.6))
        if "Version History" in title:
            master = lookup.resolve(str(source_path.parent.parent / f"{source_path.parts[1]} Master Index")) if len(source_path.parts) > 2 else None
            if master:
                add_unique(relationships, seen, relationship(node, "EXTENDS", master, master["source_path"], "filename_inference", 0.45))
        supersedes = as_list(node.get("yaml", {}).get("supersedes"))
        for target_raw in supersedes:
            target = lookup.resolve(target_raw)
            rel = relationship(node, "SUPERSEDES", target, target_raw, "yaml_field", 0.8 if target else 0.25, source_detail="supersedes")
            if target:
                add_unique(relationships, seen, rel)
            else:
                unresolved.append(rel)

        if node["node_type"] == "evidence_claim":
            for link in node.get("wiki_links", []):
                target = lookup.resolve(link)
                if target and target["node_type"] in {"canonical_synthesis", "research_artifact", "theory", "concept"}:
                    add_unique(relationships, seen, relationship(node, "SUPPORTS", target, link, "wiki_link", 0.45, evidence=node["source_path"], source_detail="evidence_candidate"))

    return relationships, unresolved


def payload(root: Path, node_registry_path: Path, relationships: list[dict[str, Any]], unresolved: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "registry_version": "1.0.0",
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "vault": str(root),
        "node_registry": str(node_registry_path),
        "relationship_count": len(relationships),
        "unresolved_count": len(unresolved),
        "principle": "Nodes are memory objects. Relationships are the beginning of institutional reasoning.",
        "relationships": relationships,
        "unresolved": unresolved,
    }


def render_report(root: Path, relationships: list[dict[str, Any]], unresolved: list[dict[str, Any]]) -> str:
    today = dt.date.today().isoformat()
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    by_type = Counter(rel["relationship_type"] for rel in relationships)
    unresolved_by_type = Counter(rel["relationship_type"] for rel in unresolved)
    by_source = Counter(rel["relationship_source"] for rel in relationships)
    low_confidence = [rel for rel in relationships if rel["confidence"] < 0.6]
    lines = [
        "---",
        'title: "Relationship Registry Report"',
        "aliases: [\"Institutional Knowledge Graph Relationship Registry Report\"]",
        "tags: [systems, engineering, knowledge-graph, relationships, report, alpha-proxima]",
        f"created: {today}",
        f"updated: {today}",
        "status: draft",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'cognitive_function: "Implementation"',
        'reasoning_engine: "CODEX"',
        'dependencies: ["[[Tool 011 - Relationship Extractor]]", "[[Relationship Taxonomy]]", "[[Tool 010 - Node Registry Generator]]"]',
        'related_documents: ["[[Engineering Program EP-001 - Institutional Knowledge Graph]]", "[[Relationship Taxonomy]]", "[[Node Registry Report]]"]',
        "related_research_programs: []",
        "---",
        "",
        "# Relationship Registry Report",
        "",
        "## Purpose",
        "",
        "Summarize candidate graph relationships extracted by [[Tool 011 - Relationship Extractor]].",
        "",
        "## Summary",
        "",
        f"- Vault: `{root}`",
        f"- Generated: `{now}`",
        f"- Total relationships discovered: `{len(relationships)}`",
        f"- Low-confidence relationships: `{len(low_confidence)}`",
        f"- Broken or unresolved links: `{len(unresolved)}`",
        "",
        "## Relationships by Type",
        "",
        "| Relationship Type | Count |",
        "|-------------------|-------|",
    ]
    for rel_type, count in sorted(by_type.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{rel_type}` | `{count}` |")
    lines.extend(["", "## Relationships by Source", "", "| Source | Count |", "|--------|-------|"])
    for source, count in sorted(by_source.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{source}` | `{count}` |")
    lines.extend(["", "## Low-Confidence Relationships", "", "| Type | Source Path | Target | Confidence | Relationship Source |", "|------|-------------|--------|------------|---------------------|"])
    for rel in low_confidence[:100]:
        lines.append(f"| `{rel['relationship_type']}` | `{rel['source_path']}` | `{rel['target_path'] or rel['target_raw']}` | `{rel['confidence']}` | `{rel['relationship_source']}` |")
    lines.extend(["", "## Unresolved by Type", "", "| Relationship Type | Count |", "|-------------------|-------|"])
    for rel_type, count in sorted(unresolved_by_type.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{rel_type}` | `{count}` |")
    lines.extend(["", "## Broken or Unresolved Links", "", "| Type | Source Path | Target | Relationship Source | Source Detail |", "|------|-------------|--------|---------------------|---------------|"])
    for rel in unresolved[:150]:
        lines.append(f"| `{rel['relationship_type']}` | `{rel['source_path']}` | `{rel['target_raw']}` | `{rel['relationship_source']}` | `{rel.get('source_detail') or ''}` |")
    lines.extend(
        [
            "",
            "## High-Value Cleanup Recommendations",
            "",
            "- Add or correct notes for frequently unresolved dependency targets.",
            "- Convert directory-like wiki links into explicit index note links.",
            "- Add stable node IDs after Node Registry review.",
            "- Review low-confidence `PART_OF`, `SUPPORTS`, and ownership relationships before downstream use.",
            "",
            "## Recommendations for ES-007",
            "",
            "- Build a graph builder that joins `node_registry.json` and `relationship_registry.json`.",
            "- Export graph data to a technology-neutral JSONL format.",
            "- Add graph validation for missing targets, duplicate relationship IDs, and invalid type pairs.",
            "- Keep all generated relationships in draft/inferred state until reviewed.",
            "",
            "## Implementation Notes",
            "",
            "This report is generated from a read-only scan. Relationships are candidates for institutional graph construction, not canonical claims.",
            "",
            "## Future Improvements",
            "",
            "- [ ] Add configurable relationship rules.",
            "- [ ] Add inverse relationship generation.",
            "- [ ] Add relationship type source-target validation matrix.",
            "",
            "## Version History",
            "",
            "| Version | Date | Author | Summary |",
            "|---------|------|--------|---------|",
            f"| 1.0.0 | {today} | [[CODEX]] | Relationship registry report generated |",
        ]
    )
    return "\n".join(lines) + "\n"


def resolve(root: Path, raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = root / path
    return path


def write_text(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"error: refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root. Defaults to current working directory.")
    parser.add_argument("--node-registry", default=str(DEFAULT_NODE_REGISTRY), help="Input node registry JSON path.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Relationship registry JSON output path.")
    parser.add_argument("--report", default=str(DEFAULT_REPORT), help="Markdown report output path.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    node_registry_path = resolve(root, args.node_registry)
    registry = json.loads(node_registry_path.read_text(encoding="utf-8"))
    nodes = registry.get("nodes", [])
    relationships, unresolved = extract_relationships(nodes)
    output = resolve(root, args.output)
    report = resolve(root, args.report)
    write_text(output, json.dumps(payload(root, node_registry_path, relationships, unresolved), indent=2, ensure_ascii=False) + "\n", args.force)
    write_text(report, render_report(root, relationships, unresolved), args.force)
    print(f"Relationship registry written: {output}")
    print(f"Relationship registry report written: {report}")
    print(f"Relationships discovered: {len(relationships)}")
    print(f"Unresolved relationships: {len(unresolved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
