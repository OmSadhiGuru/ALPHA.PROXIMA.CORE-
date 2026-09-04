#!/usr/bin/env python3
"""Build the read-only Alpha Proxima Truth Kernel contract."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


TOOL_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = Path(".alpha-proxima/generated/truth-kernel")


def load_tool(filename: str, name: str):
    path = TOOL_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load Truth Kernel component: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


node_registry = load_tool("node_registry.py", "truth_kernel_node_registry")
relationship_extractor = load_tool("relationship_extractor.py", "truth_kernel_relationship_extractor")


def finding(severity: str, code: str, path: str, message: str) -> dict[str, str]:
    return {"severity": severity, "code": code, "path": path, "message": message}


def validate(nodes: list[dict[str, Any]], unresolved: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    ids = Counter(str(node["node_id"]) for node in nodes)
    for node in nodes:
        path = str(node["source_path"])
        if ids[str(node["node_id"])] > 1:
            findings.append(finding("error", "duplicate_node_id", path, str(node["node_id"])))
        if node["node_type"] == "unknown":
            findings.append(finding("warning", "unknown_node_type", path, "No confident node type rule matched."))
        if not node.get("canonical_owner"):
            findings.append(finding("warning", "missing_owner", path, "No canonical owner is declared."))
        if not node.get("has_yaml"):
            findings.append(finding("warning", "missing_frontmatter", path, "Markdown note has no frontmatter."))
        if node.get("word_count") == 0:
            findings.append(finding("error", "empty_note", path, "Markdown note body is empty."))
        for item in node.get("validation_findings", []):
            findings.append(finding(str(item["severity"]), str(item["code"]), path, str(item["message"])))

    for rel in unresolved:
        source_kind = str(rel.get("relationship_source", ""))
        resolution = str(rel.get("resolution_status", "missing"))
        severity = "error" if source_kind == "wiki_link" and resolution == "missing" else "warning"
        findings.append(finding(
            severity,
            f"{resolution}_relationship",
            str(rel.get("source_path", "")),
            f"{rel.get('relationship_type')} target: {rel.get('target_raw')}",
        ))

    order = {"error": 0, "warning": 1, "info": 2}
    return sorted(findings, key=lambda item: (order.get(item["severity"], 9), item["code"], item["path"], item["message"]))


def build(root: Path) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Vault root not found: {root}")
    nodes = node_registry.build_nodes(root, include_hidden=False)
    relationships, unresolved = relationship_extractor.extract_relationships(nodes)
    findings = validate(nodes, unresolved)
    severities = Counter(item["severity"] for item in findings)
    node_types = Counter(str(node["node_type"]) for node in nodes)
    relationship_types = Counter(str(rel["relationship_type"]) for rel in relationships)
    source_fingerprint = node_registry.registry_payload(root, nodes)["source_fingerprint"]
    contract = {
        "schema_version": "1.0.0",
        "mode": "read_only",
        "canonical_source": "obsidian_markdown",
        "source": {
            "root": ".",
            "fingerprint": source_fingerprint,
            "note_count": len(nodes),
        },
        "health": {
            "status": "attention" if severities.get("error", 0) else "ready",
            "counts": {
                "errors": severities.get("error", 0),
                "warnings": severities.get("warning", 0),
                "findings": len(findings),
            },
        },
        "counts": {
            "nodes": len(nodes),
            "relationships": len(relationships),
            "unresolved_relationships": len(unresolved),
            "node_types": dict(sorted(node_types.items())),
            "relationship_types": dict(sorted(relationship_types.items())),
        },
        "nodes": nodes,
        "relationships": relationships,
        "unresolved_relationships": unresolved,
        "validation": {"findings": findings},
    }
    canonical = json.dumps(contract, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    contract["contract_fingerprint"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return contract


def summary(contract: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": contract["schema_version"],
        "mode": contract["mode"],
        "source": contract["source"],
        "health": contract["health"],
        "counts": contract["counts"],
        "contract_fingerprint": contract["contract_fingerprint"],
    }


def render_report(contract: dict[str, Any]) -> str:
    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    counts = contract["counts"]
    health = contract["health"]
    lines = [
        "---",
        'title: "Truth Kernel Graph Validation Report"',
        'tags: [systems, engineering, truth-kernel, validation, alpha-proxima]',
        f"created: {dt.date.today().isoformat()}",
        f"updated: {dt.date.today().isoformat()}",
        "status: draft",
        'version: "1.0.0"',
        'authors: ["CODEX"]',
        "artifact_type: engineering-report",
        'institutional_owner: "Alpha Proxima Foundation"',
        'dependencies: ["[[Truth Kernel Node Contract v0.1]]", "[[Tool 010 - Node Registry Generator]]", "[[Tool 011 - Relationship Extractor]]"]',
        "---", "", "# Truth Kernel Graph Validation Report", "",
        "## Verification boundary", "",
        "This report describes a derived, read-only scan. Findings are not canonical decisions and source notes were not modified by the generator.", "",
        "## Summary", "",
        f"- Generated: `{now}`",
        f"- Source fingerprint: `{contract['source']['fingerprint']}`",
        f"- Contract fingerprint: `{contract['contract_fingerprint']}`",
        f"- Nodes: `{counts['nodes']}`",
        f"- Relationships: `{counts['relationships']}`",
        f"- Unresolved relationships: `{counts['unresolved_relationships']}`",
        f"- Errors: `{health['counts']['errors']}`",
        f"- Warnings: `{health['counts']['warnings']}`",
        f"- Health: `{health['status']}`", "",
        "## Findings", "",
        "| Severity | Code | Source path | Message |",
        "|---|---|---|---|",
    ]
    for item in contract["validation"]["findings"][:300]:
        message = str(item["message"]).replace("|", "\\|")
        lines.append(f"| {item['severity']} | `{item['code']}` | `{item['path']}` | {message} |")
    lines.extend([
        "", "## Reproduction", "",
        "```bash",
        'python3 "08_SYSTEMS/Engineering Toolkit/ap.py" truth-kernel --vault . --output-dir /tmp/alpha-proxima-truth-kernel --force',
        "```", "",
        "The machine-readable outputs are deterministic: two runs over unchanged source content must be byte-identical.",
    ])
    return "\n".join(lines) + "\n"


def write(path: Path, payload: str, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"error: refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(payload, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Canonical Vault root.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Derived output directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing derived outputs.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.vault).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser()
    if not output_dir.is_absolute():
        output_dir = root / output_dir
    contract = build(root)
    nodes = contract["nodes"]
    relationships = contract["relationships"]
    unresolved = contract["unresolved_relationships"]
    write(output_dir / "node_registry.json", json.dumps(node_registry.registry_payload(root, nodes), indent=2, ensure_ascii=False, sort_keys=True) + "\n", args.force)
    write(output_dir / "relationship_registry.json", json.dumps(relationship_extractor.payload(root, Path("node_registry.json"), relationships, unresolved), indent=2, ensure_ascii=False, sort_keys=True) + "\n", args.force)
    write(output_dir / "truth-kernel.json", json.dumps(contract, indent=2, ensure_ascii=False, sort_keys=True) + "\n", args.force)
    write(output_dir / "Graph Validation Report.md", render_report(contract), args.force)
    print(f"Truth Kernel written: {output_dir / 'truth-kernel.json'}")
    print(f"Nodes: {contract['counts']['nodes']}")
    print(f"Relationships: {contract['counts']['relationships']}")
    print(f"Findings: {contract['health']['counts']['findings']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
