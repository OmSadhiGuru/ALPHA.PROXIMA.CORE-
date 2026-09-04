---
title: "Truth Kernel — Weekly Execution Plan"
aliases: ["Truth Kernel Week", "Backend Upgrade Week 2026-09-03"]
tags: [operations, engineering, backend, knowledge-graph, weekly-plan, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: under_review
version: "1.0.0"
authors: ["CODEX"]
artifact_type: execution-plan
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Truth Kernel Node Contract v0.1]]", "[[Tool 010 - Node Registry Generator]]", "[[Tool 011 - Relationship Extractor]]", "[[Tool 014 - Truth Kernel]]"]
related_documents: ["[[Truth Kernel Weekly QA Report - 2026-09-03]]", "[[Graph Readiness Assessment]]", "[[Alpha Proxima App Architecture v1]]"]
related_research_programs: []
execution_window: "2026-09-03/2026-09-06"
approval_state: "Founder close decision pending"
---

# Truth Kernel — Weekly Execution Plan

## Weekly outcome

> A read-only Truth Kernel that scans the canonical Alpha Proxima Vault, generates stable knowledge-node records, preserves inferred relationships and validation defects, and exposes the result to Founder interfaces without modifying source notes.

## Execution rules

- Markdown remains canonical.
- Generated contracts are derived and replaceable.
- Unknowns and ambiguities remain visible.
- No autonomous writeback, mass metadata migration, graph database, or vector database.
- Completion requires reproducible evidence and a Founder close decision.

## Completed execution

### T1 — Canonical boundary

- [x] Canonical input is the repository Vault root.
- [x] Hidden/tool-managed directories and `Omi` local scaffolding are excluded.
- [x] Generated output defaults to `.alpha-proxima/generated/truth-kernel` and is excluded from scanning.

### T2 — Node Contract v0.1

- [x] Required fields and provenance defined.
- [x] Identity precedence defined.
- [x] Move, collision, provisional identity, and unknown-value behavior defined.
- [x] Project, decision/directive, office, research program, and unclassified examples recorded.

### T3 — Read-only Node Registry

- [x] Markdown and YAML scan implemented.
- [x] Durable identity fields preferred over title fallback.
- [x] Source SHA-256 and relative source paths preserved.
- [x] Runtime timestamps and absolute machine paths removed from machine output.
- [x] Two unchanged runs produce byte-identical registries.

### T4 — Extraction safety

- [x] Missing and malformed frontmatter tested.
- [x] Duplicate identity candidates tested.
- [x] Moved-path identity behavior tested.
- [x] Unreadable scan failure tested.
- [x] Source-note hashes remain unchanged after generation.

### T5 — Graph validation

- [x] Node, relationship, unresolved, type, owner, empty-note, and parsing findings produced.
- [x] Errors and warnings separated.
- [x] Source and contract fingerprints produced.
- [x] Reproduction command recorded in the generated report.

### T6 — Relationship preview

- [x] Body wikilinks become `REFERENCES`.
- [x] YAML dependencies become `REQUIRES` without duplicate weaker edges.
- [x] Provenance and confidence preserved.
- [x] Missing and ambiguous targets preserved without first-match guessing.

### T7 — Founder interface integration

- [x] Truth Kernel summary added to the Know interface.
- [x] Versioned read endpoints added for contract, nodes, relationships, validation, and health.
- [x] Interface and Kernel totals aligned to one canonical scan boundary.
- [x] Backend restart and endpoint responses verified.
- [x] Desktop and 390×844 mobile rendering verified with no console warnings or errors.

### T8 — Weekly QA

- [x] Founder OS tests passed.
- [x] Alpha Proxima App tests passed.
- [x] Truth Kernel tests passed.
- [x] Real-vault deterministic generation passed.
- [x] Source worktree remained unchanged by generated outputs.
- [x] Code, data, API, browser, and mobile evidence separated in [[Truth Kernel Weekly QA Report - 2026-09-03]].

## Founder close gate

- [ ] Founder reviews the QA report and interface proof.
- [ ] Founder chooses `accept`, `revise`, or `stop`.
- [ ] If accepted, preserve through a focused PR; do not merge automatically.
- [ ] Select exactly one next lane after closure.

## Completion conditions

- [x] Node Registry is reproducible.
- [x] Validation report is reproducible from the recorded command.
- [x] Source Markdown is proven unchanged by generation.
- [x] One Founder interface consumes and displays the derived summary.
- [ ] Founder records the close decision.

## Current status

**Execution:** COMPLETE
**Verification:** COMPLETE WITH DECLARED LIMITS
**Gate:** FOUNDER REVIEW
**Next action:** Founder records `accept`, `revise`, or `stop` after reviewing the QA report.
