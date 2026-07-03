---
title: "EP-001 Engineering Roadmap"
aliases: ["Institutional Knowledge Graph Roadmap", "Knowledge Graph Engineering Roadmap"]
tags: [systems, engineering, knowledge-graph, roadmap, ep-001, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-roadmap
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Knowledge Graph Architecture v1.0]]", "[[Graph Readiness Assessment]]"]
related_documents: ["[[Engineering Program EP-001 - Institutional Knowledge Graph]]"]
related_research_programs: []
---

# EP-001 Engineering Roadmap

## Purpose

Break the Institutional Knowledge Graph program into future Engineering Sprints.

## Roadmap

| Sprint | Name | Objective | Primary Output |
|--------|------|-----------|----------------|
| ES-005 | Node Registry | Generate stable graph node IDs from Markdown and YAML | Node Registry v1.0 |
| ES-006 | Relationship Extractor | Extract candidate relationships from wiki links, dependencies, folders, and tables | Relationship Registry v1.0 |
| ES-007 | Graph Builder | Build an intermediate graph export from node and relationship registries | Graph Export v1.0 |
| ES-008 | Graph Validator | Validate IDs, missing targets, relationship rules, cycles, and provenance | Graph Validation Report |
| ES-009 | Knowledge Graph Dashboard | Display graph health, node coverage, relationship density, evidence linkage, and orphan clusters | Knowledge Graph Dashboard |
| ES-010 | Future Graph Connector | Prepare optional adapters for Neo4j, RDF, GraphRAG, vector stores, or local LLM retrieval | Connector Architecture |

## Sprint Detail

### ES-005 - Node Registry

Create a registry of graph nodes from:

- YAML frontmatter
- Research program folders
- Operations registries
- Engineering Toolkit documents
- Research Management Toolkit documents

Do not change source documents by default. Produce a preview first.

### ES-006 - Relationship Extractor

Extract candidate relationships from:

- Wiki links
- Frontmatter dependencies
- Folder containment
- Research evidence tables
- Office/workflow/artifact registries

Relationships must carry extraction provenance and review status.

### ES-007 - Graph Builder

Build a technology-neutral export format:

- `nodes.jsonl`
- `relationships.jsonl`
- Markdown summary report

No production database required.

### ES-008 - Graph Validator

Validate:

- Duplicate node IDs
- Missing relationship targets
- Invalid relationship types
- Missing provenance
- Unsupported node types
- Evidence relationships without evidence
- Deprecated nodes still used as active targets

### ES-009 - Knowledge Graph Dashboard

Generate:

- Node counts by type
- Relationship counts by type
- Evidence linkage coverage
- Canonical ownership coverage
- Orphan/disconnected clusters
- Graph readiness trend

### ES-010 - Future Graph Connector

Design optional connector adapters after registries are stable:

- Neo4j
- RDF
- SQLite
- JSONL
- GraphRAG
- Local LLM retrieval
- Vector database overlays

## Quality Gates

| Gate | Requirement |
|------|-------------|
| Node IDs | Stable and deterministic |
| Relationships | Typed and provenance-backed |
| Evidence | Linked to source artifacts |
| Ownership | Explicit or marked unknown |
| Exports | Reproducible locally |
| Automation | Draft by default |
| Governance | No automated canonical decisions |

## Implementation Notes

EP-001 should progress from registries to exports to connectors. Do not begin with a graph database.

## Future Improvements

- [ ] Add time estimates and dependencies for each sprint.
- [ ] Add acceptance criteria templates.
- [ ] Add test fixtures from RP-001.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial EP-001 multi-sprint engineering roadmap |
