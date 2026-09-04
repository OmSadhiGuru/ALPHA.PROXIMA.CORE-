---
title: "Knowledge Architecture Specification"
aliases: ["Institutional Knowledge Architecture Specification", "KAS"]
tags: [systems, knowledge-architecture, knowledge-graph, research, epoch-v, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: draft
version: "0.1.0"
authors: ["CODEX (CF-07)"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
dependencies: ["[[Book III - Knowledge Integrity]]", "[[Knowledge Graph Architecture v1.0]]", "[[Genome Constitution v1.0]]", "[[Vault Structure Convention]]"]
related_documents: ["[[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]]", "[[Node Taxonomy]]", "[[Relationship Taxonomy]]", "[[Knowledge Graph Conventions]]"]
related_research_programs: ["[[RP-001 Master Index]]", "[[RP-002 Master Index]]"]
initiative: "Epoch V — Constitutional Coherence"
resolves: ["CAR-001 Deliverable 6", "CAR-001 Deliverable 7", "Epoch V Tier 3 knowledge architecture"]
---

# Knowledge Architecture Specification

## Purpose

This specification unifies the institutional research lifecycle, Book III evidence classes, the typed Institutional Knowledge Graph, and the Living Genome cell/organ model into one Markdown-first architecture. It extends the [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]]; it does not replace that master reference or silently alter its source taxonomies.

## Context

CAR-001 identified two parallel but compatible knowledge architectures: the Foundation's research and graph system, and Project Genome's cell/organ/evolution model. Their shared commitments—explicit epistemic status, typed relationships, provenance, revision history, and human review—allow a single lifecycle and crosswalk without collapsing institutional knowledge into personal knowledge.

## Core Content

### 1. Architectural Layers

| Layer | Canonical object | Function |
|-------|------------------|----------|
| Source | observation, document, dataset, conversation, experience | Preserved input with provenance and access boundary |
| Claim | evidence claim or Knowledge Cell | Smallest reviewable assertion with epistemic status, source, timestamps, and owner |
| Relationship | typed edge or Genome Connection | Directional, provenance-bearing connection between objects |
| Synthesis | research package, canonical synthesis, cluster | Evidence-aware integration that preserves disagreement |
| Domain | research program, Knowledge Organ, knowledge system | Functionally coherent body of knowledge with a steward and review cadence |
| Decision/Application | ADR, protocol, project use, Genome Decision Layer | Traceable use of knowledge in action |
| History | Git/version record, supersession edge, Genome Mutation, timeline | Durable account of how content, status, and relationships changed |

Institutional and personal objects may share schemas and relationship types, but they retain separate ownership and access domains.

### 2. Canonical Crosswalk

| Living Genome term | Institutional graph equivalent | Rule |
|--------------------|--------------------------------|------|
| Knowledge Cell | `evidence_claim`, `concept`, `principle`, `experience`, or another approved node type | A Cell is graph-ready only when it has epistemic status, provenance, timestamps, and at least one typed relationship |
| Genome Node | Registered graph node | Stable ID and source path required |
| Genome Connection | Typed relationship | Use the strongest approved relationship; provenance required |
| Cluster | Query- or proximity-derived grouping | Non-canonical until reviewed and assigned purpose/ownership |
| Knowledge Organ | Governed domain subgraph or research program | Must have defined boundary, steward, entry criteria, and review cadence |
| Knowledge System | Cross-domain subgraph | Explicit dependencies; no ownership inferred from folder location |
| Genome Mutation | Revision, reclassification, merge, branch, retraction, or supersession event | Preserve prior state and rationale; never silently overwrite |
| Evolution Timeline | Version history plus event index | Reconstructible from durable records |

This crosswalk does not make a person's Living Genome part of the institutional canon. Promotion across that boundary requires consent, provenance, redaction where needed, and the applicable research/canonisation review.

### 3. Minimum Knowledge Object Contract

Every graph-participating knowledge object must have:

- a stable human title and machine-resolvable identity;
- object or node type from the approved taxonomy;
- accountable owner or steward;
- source and provenance;
- creation, update, and last-review timestamps;
- lifecycle status and semantic version;
- Book III epistemic class when the object makes or contains a claim;
- at least one typed relationship, or an explicit `unintegrated` state;
- access/sensitivity classification when personal, restricted, or security-relevant; and
- a revision or supersession trail when changed materially.

The base frontmatter in the [[Vault Structure Convention]] remains authoritative. New fields should be proposed through the governed schema process before bulk migration; this draft defines requirements, not an unreviewed repository-wide rewrite.

### 4. Evidence and Relationship Semantics

Book III classes remain the canonical epistemic vocabulary: C (consensus), M (competing models), Q (open question), E (emerging evidence), S (speculative hypothesis), and P (phenomenological report). Classification applies to claims, not automatically to entire documents.

The [[Relationship Taxonomy]] governs machine-facing edges. The research vocabulary (`grounds`, `extends`, `instantiates`, `competes_with`, `contradicts`, `requires`, `supports`, `exemplifies`, `precedes`, `contains`) maps to the approved graph vocabulary only through explicit reviewed rules. Until mapped, preserve the source term and represent the edge as a reviewed `REFERENCES` or candidate relationship; do not fabricate semantic certainty.

### 5. Knowledge Lifecycle

1. **Capture** — preserve the source, responsible actor, time, and consent/access boundary.
2. **Structure** — identify claims and objects; assign provisional types and epistemic classes.
3. **Connect** — add typed, directional, provenance-bearing relationships.
4. **Validate** — check required metadata, link targets, source accessibility, classification, and contradiction preservation.
5. **Review** — accountable human or council reviews according to stakes and canonisation rules.
6. **Canonise** — approved synthesis enters the institutional canon with decision/review evidence.
7. **Apply** — decisions and projects link back to the knowledge used and record deviations.
8. **Evolve** — revise, supersede, branch, merge, retract, or archive while preserving prior states.

Automated extraction and validators may report structural conformance. They do not canonise knowledge or replace epistemic and ethical review.

### 6. Quality Controls

| Control | Minimum signal |
|---------|----------------|
| Provenance completeness | Claims trace to an accessible source or are explicitly marked unverified |
| Epistemic completeness | Evidence-bearing claims have a Book III class |
| Relationship integrity | Targets resolve; type and provenance are recorded |
| Contradiction retention | Competing evidence remains discoverable and is not averaged into false consensus |
| Review currency | `last_reviewed` and next-review trigger are visible for governed knowledge |
| Orphan visibility | Unintegrated objects are reported, not silently discarded |
| Change traceability | Material revisions link prior state, rationale, and responsible actor |
| Boundary integrity | Personal/restricted knowledge is not promoted or published without authority and consent |

### 7. Ownership and Governance

- [[Book III - Knowledge Integrity]] governs evidence and canonisation.
- The Research Council role governs institutional research review; where that body is not operationally constituted, approval must not be implied.
- JERANIUM / CF-15 may operate data and graph infrastructure within delegated scope; it does not decide truth or canonisation.
- LUMIAION / CF-01 maintains architectural coherence and routing.
- The Engineering Office maintains schemas, extractors, validators, and migration safety.
- The Ethics Council reviews triggered high-stakes, personal-data, deployment, and constitutional concerns.
- The Founder and ratified councils retain the authority defined by the constitutional hierarchy.

### 8. Implementation Sequence

1. Ratify this conceptual crosswalk and select canonical field names.
2. Add schema fields through the Vault Structure Convention's governed change process.
3. Update node and relationship extractors with backward-compatible parsing.
4. Generate a migration report before changing existing notes.
5. Prove one vertical lane from source → claim → relationship → review → application → history.
6. Expand only after the lane passes structural, epistemic, privacy, and recovery checks.

## Related Notes

- [[Book III - Knowledge Integrity]]
- [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]]
- [[Knowledge Graph Architecture v1.0]]
- [[Node Taxonomy]]
- [[Relationship Taxonomy]]
- [[Knowledge Graph Conventions]]
- [[Genome Constitution v1.0]]

## Open Questions

- [ ] Ratify the exact crosswalk between the research relationship vocabulary and the Institutional Knowledge Graph taxonomy.
- [ ] Define the access/sensitivity vocabulary before ingesting personal Living Genome material.
- [ ] Select a single proven vertical lane for implementation and migration testing.
- [ ] Determine whether the cross-program graph master index (M-09) is generated from the registries or maintained as a reviewed note.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-09-03 | CODEX (CF-07) | Initial ontology-unification draft for Epoch V Tier 3; no schema migration or canonisation implied. |
