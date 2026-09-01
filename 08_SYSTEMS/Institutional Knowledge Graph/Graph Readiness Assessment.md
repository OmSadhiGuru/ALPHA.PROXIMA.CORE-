---
title: "Graph Readiness Assessment"
aliases: ["Institutional Graph Readiness Assessment", "Knowledge Graph Readiness"]
tags: [systems, engineering, knowledge-graph, assessment, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: draft
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-assessment
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Vault Dependency Report]]", "[[Engineering Dashboard Report]]", "[[Research Management Toolkit v1.0]]"]
related_documents: ["[[Knowledge Graph Architecture v1.0]]", "[[EP-001 Engineering Roadmap]]"]
related_research_programs: ["RP-001", "RP-002", "RP-003", "RP-004", "RP-005", "RP-006"]
---

# Graph Readiness Assessment

## Purpose

Assess how easily the current Alpha Proxima Vault can become an Institutional Knowledge Graph and identify engineering debt that should be resolved before graph extraction.

## Current Readiness Summary

| Area | Readiness | Notes |
|------|-----------|-------|
| Markdown documents | High | Human-readable source layer exists |
| YAML frontmatter | Medium | Many active documents now structured; legacy gaps remain |
| Wiki links | Medium | Rich links exist, but some are directory-like or unresolved |
| Research programs | Medium-High | RP-001 is mature; RP-002 through RP-006 are placeholders |
| Evidence registries | Medium | RP-001 has evidence registry; future RPs need scaffolds |
| Operations registries | Medium | Office, workflow, artifact, review cycle registries exist |
| Engineering tooling | Medium-High | Validators, dependency analyzer, research management tools exist |
| Stable identifiers | Low-Medium | IDs exist for some programs/artifacts but no graph-wide registry |
| Relationship typing | Low | Most relationships are wiki links, not typed graph edges |
| Provenance | Medium | Many documents have authors and dates; extraction provenance is not yet formalized |

## Existing Graph-Ready Assets

| Asset | Graph Use |
|-------|-----------|
| YAML frontmatter | Node properties |
| Wiki links | Candidate `REFERENCES` relationships |
| `dependencies` frontmatter | Candidate `REQUIRES` relationships |
| Research Program folders | `research_program` nodes and `PART_OF` structure |
| Evidence Registry | `evidence_claim` nodes |
| Research Graph concept notes | `concept` and `theory` nodes |
| Operations registries | `office`, `workflow`, `artifact`, and review-cycle nodes |
| Engineering Toolkit docs | `engineering_tool` nodes |
| Dependency Analyzer report | Relationship extraction baseline |

## Engineering Debt

| Debt | Impact | Recommendation |
|------|--------|----------------|
| Missing metadata fields | Weak node property coverage | Continue phased metadata migration |
| Root zero-byte `Vault.md` | Active validation error | Archive, remove, or convert in a focused cleanup sprint |
| Broken references | Unresolved relationship targets | Add folder-target handling or explicit index notes |
| Untyped wiki links | Low semantic precision | Build relationship extractor with review states |
| Duplicate template names | Ambiguous node labels | Introduce stable template IDs |
| No graph-wide node IDs | Fragile identity across file moves | Build Node Registry in ES-005 |
| No relationship registry | Hard to validate graph edges | Build Relationship Extractor in ES-006 |
| Evidence table parsing absent | Evidence claims not machine-actionable | Define claim row schema and extractor |

## Migration Phases

| Phase | Objective | Output |
|-------|-----------|--------|
| Phase 0 | Preserve Markdown as canonical human source | Existing vault remains source of truth |
| Phase 1 | Add stable node IDs to high-value documents | Node Registry |
| Phase 2 | Extract references, dependencies, and containment | Relationship Registry |
| Phase 3 | Validate missing targets, duplicate IDs, and orphan clusters | Graph Validation Report |
| Phase 4 | Add evidence-claim extraction from registries | Evidence Claim Registry |
| Phase 5 | Create Knowledge Graph Dashboard | Graph health, node counts, relationship counts |
| Phase 6 | Add optional database/export adapters | Neo4j, RDF, GraphRAG, JSONL |

## Readiness Estimate

The vault is ready for a Markdown-to-registry graph prototype. It is not yet ready for a production graph database.

Recommended next step: build a Node Registry generator that assigns stable IDs without changing document meaning.

## Implementation Notes

The Foundation should avoid premature graph database adoption. The most valuable near-term work is to make identities and relationships explicit while keeping Markdown readable.

## Future Improvements

- [ ] Add automated readiness scoring.
- [ ] Add graph extraction dry run.
- [ ] Add per-node-type migration checklist.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | [[CODEX]] | Initial graph readiness assessment |
