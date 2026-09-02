---
title: "Relationship Taxonomy"
aliases: ["Institutional Knowledge Graph Relationship Taxonomy", "KG Relationship Types"]
tags: [systems, engineering, knowledge-graph, taxonomy, relationships, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Knowledge Graph Architecture v1.0]]", "[[Node Taxonomy]]"]
related_documents: ["[[Knowledge Graph Conventions]]"]
related_research_programs: []
---

# Relationship Taxonomy

## Purpose

Define approved relationship types for the Institutional Knowledge Graph v1.0.

## Relationship Rules

- Relationship types use uppercase snake case.
- Relationships are directional unless explicitly documented as symmetric.
- Every relationship must have provenance.
- Evidence-bearing relationships must link to an evidence source.
- Inferred relationships must be marked as inferred, never canonical.

## Core Relationship Types

| Relationship | Direction | Purpose |
|--------------|-----------|---------|
| `SUPPORTS` | Claim -> Claim/Theory/Synthesis | Indicates evidentiary or argumentative support |
| `CONTRADICTS` | Claim -> Claim/Theory/Synthesis | Indicates conflict or negative evidence |
| `EXTENDS` | Node -> Node | Adds scope or continuation |
| `DERIVED_FROM` | Node -> Source Node | Indicates origin or derivation |
| `REFERENCES` | Node -> Node | General citation or wiki-link reference |
| `PART_OF` | Component -> Whole | Membership or containment |
| `IMPLEMENTS` | Tool/Policy -> Standard/Architecture | Implementation relationship |
| `OWNED_BY` | Node -> Office/Function | Canonical ownership |
| `PRODUCED_BY` | Artifact -> Person/Organization/Engine | Creator or contributor |
| `SUPERSEDES` | New Node -> Old Node | Replacement relationship |
| `RELATED_TO` | Node -> Node | Weak relationship, usually symmetric |
| `REQUIRES` | Node -> Dependency | Dependency relationship |
| `VALIDATED_BY` | Node -> Validator/Review Artifact | Validation or review evidence |
| `CITED_BY` | Source -> Citing Node | Reverse citation convenience edge |

## Relationship Properties

| Property | Required | Purpose |
|----------|----------|---------|
| `relationship_id` | Yes | Stable edge identity |
| `relationship_type` | Yes | Type from this taxonomy |
| `source_node_id` | Yes | Source node |
| `target_node_id` | Yes | Target node |
| `provenance` | Yes | Origin of relationship |
| `status` | Yes | active, inferred, disputed, deprecated, archived |
| `evidence_node_id` | Conditional | Required for evidence-bearing claims |
| `confidence` | Conditional | Required for automated extraction |
| `created` | Yes | Creation date |
| `updated` | Yes | Update date |

## Relationship Interpretation

| Relationship | Canonical Use Constraint |
|--------------|--------------------------|
| `SUPPORTS` | Must cite evidence or review source |
| `CONTRADICTS` | Must cite evidence or review source |
| `DERIVED_FROM` | Must preserve source provenance |
| `OWNED_BY` | Must not be inferred when owner is ambiguous |
| `SUPERSEDES` | Must preserve old node rather than delete it |
| `RELATED_TO` | Should be avoided when a stronger relationship exists |
| `VALIDATED_BY` | Means structurally validated unless explicitly tied to review authority |

## Implementation Notes

Wiki links should initially map to `REFERENCES`. Frontmatter `dependencies` should initially map to `REQUIRES`. Research evidence table rows should map to `SUPPORTS`, `CONTRADICTS`, or `RELATED_TO` only after explicit evidence parsing or human review.

## Future Improvements

- [ ] Add relationship extraction confidence scoring.
- [ ] Add inverse relationship generation rules.
- [ ] Add allowed source-target type matrix.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial Institutional Knowledge Graph relationship taxonomy |
