---
title: "Tool 010 - Node Registry Generator"
aliases: ["Node Registry Generator", "Institutional Knowledge Graph Node Registry Tool"]
tags: [systems, engineering, knowledge-graph, node-registry, tool, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Knowledge Graph Architecture v1.0]]", "[[Node Taxonomy]]", "[[Tool 008 - Engineering CLI]]"]
related_documents: ["[[Engineering Program EP-001 - Institutional Knowledge Graph]]", "[[Node Registry Report]]", "[[node_registry.json]]"]
related_research_programs: []
---

# Tool 010 - Node Registry Generator

## Purpose

Generate the first machine-readable node registry for the Institutional Knowledge Graph.

The Node Registry is the first bridge between Markdown memory and LUMIAION's future institutional graph.

## Scope

The generator scans Markdown files and extracts graph node candidates. It does not modify notes, create canonical claims, or infer beyond reasonable confidence.

## Extracted Fields

- File path
- Title
- YAML fields
- Artifact type
- Institutional owner
- Cognitive function
- Related documents
- Related research programs
- Wiki links
- Tags
- Status
- Version
- Node type candidate

## Node Type Inference

Node type candidates are inferred from:

- `artifact_type`
- Folder location
- Filename patterns
- Known conventions from [[Node Taxonomy]]

If the generator is uncertain, it marks `node_type` as `unknown`.

## CLI Interface

```bash
python3 "08_SYSTEMS/Institutional Knowledge Graph/Tools/node_registry.py" --vault . --force
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" node-registry --vault . --force
```

Options:

| Option | Purpose |
|--------|---------|
| `--vault PATH` | Vault root. Defaults to current working directory. |
| `--output PATH` | JSON registry output path. |
| `--report PATH` | Markdown report output path. |
| `--include-hidden` | Include hidden/tool-managed folders. |
| `--force` | Overwrite existing output files. |

## Outputs

| Output | Purpose |
|--------|---------|
| `node_registry.json` | Machine-readable node registry |
| `Node Registry Report.md` | Human-readable summary and cleanup recommendations |

## Implementation Notes

The generator reuses the Engineering Toolkit Markdown and YAML parser to keep graph extraction aligned with vault validation.

Node IDs are deterministic and include a path-derived hash so early registry generation remains stable while avoiding collisions.

## Future Improvements

- [ ] Add YAML `node_id` override support.
- [ ] Add configurable inference rule files.
- [ ] Add schema validation against [[Node Taxonomy]].
- [ ] Feed registry into ES-006 Relationship Extractor.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial Node Registry Generator for ES-005 |
