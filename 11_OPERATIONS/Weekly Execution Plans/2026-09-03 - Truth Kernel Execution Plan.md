---
title: "Truth Kernel — Weekly Execution Plan"
aliases: ["Truth Kernel Week", "Backend Upgrade Week 2026-09-03"]
tags: [operations, engineering, backend, knowledge-graph, weekly-plan, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: draft
version: "0.1.0"
authors: ["CODEX"]
artifact_type: execution-plan
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Graph Readiness Assessment]]", "[[Knowledge Graph Architecture v1.0]]", "[[LUMIAION - Operating Manual (LOOM)]]"]
related_documents: ["[[Engineering Program EP-001 - Institutional Knowledge Graph]]", "[[Node Taxonomy]]", "[[Relationship Taxonomy]]"]
execution_window: "2026-09-03/2026-09-06"
approval_state: "Founder confirmation required at weekly close"
---

# Truth Kernel — Weekly Execution Plan

## Weekly outcome

By Sunday 2026-09-06, produce and verify one narrow backend upgrade:

> A read-only Truth Kernel that can scan the canonical Alpha Proxima Vault, generate stable knowledge-node records, and report validation defects without modifying source notes.

This week does **not** include autonomous Vault writeback, a vector database, production authentication, multi-agent orchestration, or a graph database.

## Execution rules

- Markdown in the Alpha Proxima Vault remains canonical.
- All generated registries and reports are derived and replaceable.
- The initial lane is read-only against source notes.
- Unknown or ambiguous metadata is reported, not invented.
- No mass frontmatter migration.
- A checkbox is completed only when its confirmation evidence exists.
- Founder approval is required before moving from read-only extraction to canonical writeback.

## Confirmed starting point

- [x] **Execution window confirmed** — Thursday 2026-09-03 through Sunday 2026-09-06.
  - Evidence: system date checked on 2026-09-03 EDT.
- [x] **Institutional next step confirmed** — the current readiness assessment recommends a Node Registry generator before adopting a production graph database.
  - Evidence: [[Graph Readiness Assessment]].
- [x] **Minimum node contract confirmed** — stable ID, type, title, status, version, source path, owner, dates, and provenance are already specified.
  - Evidence: [[Knowledge Graph Architecture v1.0]].
- [x] **Weekly plan created** — this document defines scope, evidence, and confirmation gates.
  - Evidence: this file.

## Thursday — Truth and scope lock

### T1. Confirm the canonical input boundary

- [x] Record the exact canonical Vault root used by the generator.
- [x] Record the canonical Git checkout and current branch; full working-tree cleanliness remains explicitly unconfirmed.
- [x] Identify duplicate or competing Alpha Proxima roots without modifying them.
- [x] Define excluded folders and generated-output folders.

**Deliverable:** `Truth Kernel Baseline Report`  
**Confirmation:** report contains absolute paths, scan boundary, exclusions, timestamp, and explicit unresolved ambiguities.  
**Gate:** no generator implementation until the read boundary is explicit.

**Result:** CONFIRMED WITH DECLARED LIMITS — see [[2026-09-03 - Truth Kernel Baseline Report]].

### T2. Freeze the v0 node contract

- [ ] Map existing Vault metadata to the required node properties.
- [ ] Define deterministic `apkg:<node_type>:<stable_slug>` generation.
- [ ] Define collision behavior without editing source documents.
- [ ] Define provenance and validation-status fields.
- [ ] Define machine-readable output schema.

**Deliverable:** `Truth Kernel Node Contract v0.1`  
**Confirmation:** schema examples cover a project, decision, office, research program, and unclassified note.

## Friday — Read-only Node Registry

### T3. Implement the extractor

- [ ] Scan Markdown files inside the confirmed boundary.
- [ ] Parse YAML frontmatter without modifying notes.
- [ ] Generate deterministic node IDs.
- [ ] Preserve source paths and provenance.
- [ ] Represent unknown values as `null` or validation findings.
- [ ] Write output only to a dedicated generated-data location.

**Deliverable:** Node Registry generator plus generated JSONL or SQLite registry.  
**Confirmation:** two identical runs against unchanged input produce an identical registry.

### T4. Add extraction safety tests

- [ ] Verify the generator does not alter source Markdown.
- [ ] Test missing frontmatter.
- [ ] Test duplicate titles and duplicate candidate IDs.
- [ ] Test moved-path behavior.
- [ ] Test malformed YAML and unreadable files.

**Deliverable:** automated test suite and test report.  
**Confirmation:** all safety tests pass; any skipped test is documented.

## Saturday — Validation and relationships preview

### T5. Generate the Graph Validation Report

- [ ] Count scanned files, generated nodes, unknown types, and missing owners.
- [ ] Detect duplicate IDs.
- [ ] Detect unresolved wikilinks.
- [ ] Detect zero-byte Markdown files.
- [ ] Detect malformed metadata.
- [ ] Separate errors, warnings, and informational findings.

**Deliverable:** timestamped Graph Validation Report.  
**Confirmation:** every total can be reproduced by the command recorded in the report.

### T6. Produce a non-canonical relationship preview

- [ ] Extract candidate `REFERENCES` edges from wikilinks.
- [ ] Extract candidate `REQUIRES` edges from `dependencies`.
- [ ] Add source, extraction method, and confidence to every edge.
- [ ] Keep unresolved and ambiguous edges visible for review.

**Deliverable:** Relationship Registry preview.  
**Confirmation:** sampled relationships resolve back to their exact source notes; no relationship is silently promoted to canonical truth.

## Sunday — Integration proof and Founder close

### T7. Expose the Truth Kernel through a read-only interface

- [ ] Define a versioned read contract for nodes, relationships, validation, and health.
- [ ] Connect one existing Founder interface view to generated data.
- [ ] Ensure the interface displays provenance and source-path access.
- [ ] Confirm empty, loading, stale, and error states.

**Deliverable:** working read-only integration proof.  
**Confirmation:** interface data matches registry totals and survives a backend restart.

### T8. Complete weekly QA

- [ ] Run the full extractor and tests from a clean command sequence.
- [ ] Confirm source Markdown remains unchanged by extraction.
- [ ] Record performance and registry totals.
- [ ] Record all defects and deferred work.
- [ ] Separate code verification, data verification, browser verification, and mobile verification.

**Deliverable:** `Truth Kernel Weekly QA Report — 2026-09-06`.  
**Confirmation:** evidence paths and exact commands are present; untested claims are labelled unverified.

### T9. Founder confirmation gate

- [ ] Founder reviews the QA report and integration proof.
- [ ] Founder chooses: accept, revise, or stop.
- [ ] If accepted, preserve the proven state in Git without merging or enacting broader architecture automatically.
- [ ] Select exactly one next lane: relationship hardening, hybrid search, or gated writeback preview.

**Weekly achievement is confirmed only when:**

- [ ] Node Registry is reproducible.
- [ ] Validation report is reproducible.
- [ ] Source Markdown is proven unchanged by the extractor.
- [ ] One interface reads the derived registry successfully.
- [ ] Founder records an explicit close decision.

## Deferred backlog — not part of this week

- [ ] Hybrid lexical, graph, and semantic search.
- [ ] Local/private embeddings and vector index.
- [ ] Structured operational state and G0–G7 state machine.
- [ ] Gated writeback with diff preview, approval, audit, and rollback.
- [ ] LUMIAION intent routing and department context isolation.
- [ ] Persistent session memory and re-entry briefs.
- [ ] Authenticated private mobile access.
- [ ] Observability, queues, recovery drills, and cost telemetry.
- [ ] Private Alpha Proxima server and local-model adapters.
- [ ] Optional Neo4j, RDF, GraphRAG, or external graph exports.

## End-of-week evidence table

| Evidence | Status | Location | Confirmation |
|---|---|---|---|
| Baseline Report | Confirmed with declared limits | [[2026-09-03 - Truth Kernel Baseline Report]] | Exact roots, boundaries, exclusions, and unresolved checks recorded |
| Node Contract v0.1 | Pending | TBD | Required examples validated |
| Node Registry | Pending | TBD | Deterministic rerun confirmed |
| Automated Tests | Pending | TBD | Safety suite passes |
| Graph Validation Report | Pending | TBD | Totals reproducible |
| Relationship Preview | Pending | TBD | Sample provenance verified |
| Interface Integration | Pending | TBD | Registry totals match UI |
| Weekly QA Report | Pending | TBD | Verification boundaries explicit |
| Founder Close Decision | Pending | TBD | Accept, revise, or stop recorded |

## Final weekly status

**Current status:** IN PROGRESS  
**Current gate:** Node Contract v0.1  
**Next executable action:** freeze the deterministic node identity and output schema.  
**Founder action required now:** none; review is required at the Sunday close gate.
