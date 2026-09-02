---
title: "Tool 011 - Relationship Extractor"
aliases: ["Relationship Extractor", "Institutional Knowledge Graph Relationship Extractor", "ES-006 Relationship Extractor"]
tags: [systems, engineering, knowledge-graph, relationships, automation, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Tool 010 - Node Registry Generator]]", "[[Relationship Taxonomy]]"]
related_documents: ["[[Engineering Program EP-001 - Institutional Knowledge Graph]]", "[[Knowledge Graph Architecture v1.0]]", "[[Node Taxonomy]]", "[[Relationship Taxonomy]]", "[[Tool 008 - Engineering CLI]]"]
related_research_programs: []
---

# Tool 011 - Relationship Extractor

## Purpose

The Relationship Extractor scans the Alpha Proxima Vault and generates a machine-readable registry of candidate relationships between graph nodes.

This tool is the second practical bridge between Markdown institutional memory and the future Institutional Knowledge Graph.

## Scope

The extractor reads:

- `node_registry.json`
- Markdown wiki links
- YAML `related_documents`
- YAML `dependencies`
- YAML `related_research_programs`
- YAML ownership and author fields
- Folder structure
- Filename conventions

The extractor does not modify notes and does not create canonical institutional claims.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" relationship-extract --vault . --force
```

Direct tool invocation is also supported:

```bash
python3 "08_SYSTEMS/Institutional Knowledge Graph/Tools/relationship_extractor.py" --vault . --force
```

## Outputs

| Output | Purpose |
|--------|---------|
| `relationship_registry.json` | Machine-readable relationship registry |
| `Relationship Registry Report.md` | Human-readable engineering report |

## Relationship Candidates

The extractor can produce the following relationship candidates:

- `REFERENCES`
- `RELATED_TO`
- `DEPENDS_ON`
- `PART_OF`
- `PRODUCED_BY`
- `OWNED_BY`
- `SUPPORTS`
- `EXTENDS`
- `SUPERSEDES`
- `IMPLEMENTS`
- `REQUIRES`

## Relationship Sources

Every relationship records a base `relationship_source`:

| Source | Meaning |
|--------|---------|
| `wiki_link` | Relationship came from a Markdown wiki link |
| `yaml_field` | Relationship came from YAML frontmatter |
| `folder_inference` | Relationship came from folder placement |
| `filename_inference` | Relationship came from a filename or title convention |

When useful, `source_detail` records the exact field or inference rule, such as `dependencies`, `related_documents`, or `evidence_candidate`.

## Confidence Rules

| Confidence Range | Meaning |
|------------------|---------|
| `0.8+` | Strong internal metadata match |
| `0.6-0.79` | Reasonable inferred match |
| `0.4-0.59` | Low-confidence structural or semantic candidate |
| `<0.4` | Unresolved or weak candidate |

Low-confidence relationships require human review before downstream graph use.

## Usage Examples

Generate the relationship registry:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" relationship-extract --vault . --force
```

Use a custom node registry:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" relationship-extract --vault . --node-registry "08_SYSTEMS/Institutional Knowledge Graph/Tools/node_registry.json" --force
```

Write to a custom output path:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" relationship-extract --vault . --output "/tmp/relationship_registry.json" --report "/tmp/Relationship Registry Report.md" --force
```

## Implementation Notes

The extractor treats resolved internal links as graph relationship candidates. Unresolved links are preserved separately so future cleanup work can repair missing targets, ambiguous names, or external dependency references.

YAML `dependencies` produce `REQUIRES` when the dependency resolves to an internal node. Unresolved dependency strings are preserved as `DEPENDS_ON` candidates because they often describe external systems, tools, or standards that may later become explicit nodes.

## Future Improvements

- [ ] Add configurable relationship extraction rules.
- [ ] Add inverse relationship generation.
- [ ] Add source-target validation rules.
- [ ] Add JSON Schema validation for relationship registry output.
- [ ] Add graph export formats for future GraphRAG or graph database connectors.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial ES-006 Relationship Extractor |

