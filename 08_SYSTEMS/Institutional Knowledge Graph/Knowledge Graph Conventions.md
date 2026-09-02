---
title: "Knowledge Graph Conventions"
aliases: ["Institutional Knowledge Graph Conventions", "KG Conventions"]
tags: [systems, engineering, knowledge-graph, conventions, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Knowledge Graph Architecture v1.0]]", "[[Node Taxonomy]]", "[[Relationship Taxonomy]]"]
related_documents: ["[[Graph Readiness Assessment]]", "[[EP-001 Engineering Roadmap]]"]
related_research_programs: []
---

# Knowledge Graph Conventions

## Purpose

Define operational conventions for naming, identifiers, relationships, version control, merge strategy, conflict handling, and deprecation in the Institutional Knowledge Graph.

## Naming

Human-readable names should remain clear and stable. Machine names should be deterministic.

| Object | Human Name | Machine Name |
|--------|------------|--------------|
| Node type | Research Program | `research_program` |
| Relationship type | DERIVED_FROM | `DERIVED_FROM` |
| Property | Canonical Owner | `canonical_owner` |
| Node ID | RP-001 | `apkg:research_program:rp-001` |

## Identifiers

Node identifiers use:

```text
apkg:<node_type>:<stable_slug>
```

Relationship identifiers use:

```text
apkg:rel:<relationship_type>:<source_slug>:<target_slug>
```

If duplicate relationships exist between the same nodes, append a short evidence or sequence suffix.

## Relationship Rules

1. Use the strongest accurate relationship type.
2. Use `RELATED_TO` only when a stronger relationship is not justified.
3. Treat wiki links as `REFERENCES` until reviewed or parsed with a stronger rule.
4. Treat frontmatter `dependencies` as `REQUIRES`.
5. Treat file containment as `PART_OF`.
6. Treat evidence table source references as candidate evidence relationships, not automatically canonical relationships.
7. Never infer `OWNED_BY` from folder location alone when ownership is ambiguous.

## Version Control

Graph records should be generated into reviewable files before any database import.

Recommended progression:

1. Markdown source
2. Extracted node registry
3. Extracted relationship registry
4. Validation report
5. Optional database import

Version control belongs at every stage.

## Merge Strategy

When two graph nodes appear to represent the same entity:

| Condition | Strategy |
|-----------|----------|
| Same stable ID | Merge properties after conflict check |
| Same title, different type | Do not merge automatically |
| Same alias, different owner | Flag for review |
| Same source path | Prefer current source path |
| Duplicate concept notes | Create merge recommendation, not automatic merge |

## Conflict Handling

Conflicts should be represented, not erased.

| Conflict Type | Handling |
|---------------|----------|
| Conflicting evidence claims | Use `CONTRADICTS` or disputed status |
| Ownership conflict | Mark `ownership_status: disputed` |
| Version conflict | Preserve both versions and use `SUPERSEDES` only after review |
| Relationship ambiguity | Keep as `REFERENCES` until classified |
| Canonical conflict | Route to governance or research review |

## Deprecation

Deprecated nodes and relationships remain addressable.

Deprecation requirements:

- `status: deprecated`
- `deprecated_date`
- `deprecated_reason`
- Optional `superseded_by`
- Link to decision or migration report

No graph object should disappear without a trace.

## Implementation Notes

These conventions are designed for Markdown-first graph evolution. They can later map to JSON, property graph databases, RDF triples, vector indexes, or GraphRAG systems.

## Future Improvements

- [ ] Add generated ID examples for every node type.
- [ ] Add source-to-relationship extraction rules.
- [ ] Add conflict report template.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial Institutional Knowledge Graph conventions |
