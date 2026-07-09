---
title: CPOS
id: apx-operations-cpos-readme
department: LUMIAION
domain: operations
type: readme
status: active
version: 1.0.0
created: 2026-07-09
updated: 2026-07-09
source: migration
tags: [operations, cpos, readme]
related: [../README.md, DASHBOARD.md, CURRENT_SPRINT.md]
owner: "Operations Office (legacy-reference — not a ratified Constitutional Office; see repository hardening notes)"
---

# CPOS

## Purpose

CPOS is a Markdown-native production operating framework: a set of linked queue files that let any department (see Office Vocabulary Conflict, below) find its next eligible task without manual coordination. Migrated from `Desktop/LUMIAION/OSG Operating Office/` into this repository by Codex (Production Queue, task PRD-001) and hardened for repository readiness in Sprint 1.5.

## Scope

Sixteen files, each answering exactly one question about the production flow:

| File | Question It Answers |
|---|---|
| `DASHBOARD.md` | What does the Founder need to know today? |
| `CURRENT_SPRINT.md` | What production cycle is active right now? |
| `AI_ASSIGNMENTS.md` | Which permanent department owns each current assignment? |
| `BACKLOG.md` | What approved or potential work exists before it enters a production queue? |
| `RESEARCH_QUEUE.md` | What needs evidence, context, or source gathering next? |
| `BLUEPRINT_QUEUE.md` | What needs to be designed before production starts? |
| `PRODUCTION_QUEUE.md` | What is ready to be built, edited, written, or packaged now? |
| `REVIEW_QUEUE.md` | What completed work needs quality review before publishing or knowledge capture? |
| `PUBLISHING_QUEUE.md` | What is ready to package, release, or present? |
| `FEEDBACK_QUEUE.md` | What feedback must be processed into next work? |
| `KNOWLEDGE_QUEUE.md` | What needs to be captured into reusable organizational knowledge? |
| `IMPROVEMENT_QUEUE.md` | What should be improved so production flows better next cycle? |
| `BLOCKERS.md` | What is preventing production flow right now? |
| `APPROVAL_GATES.md` | What decisions require Founder approval before work continues? |
| `HANDOFF_LOG.md` | What structured production handoffs have occurred? |
| `ROADMAP.md` | What production horizons guide queue priority? |

## Office Vocabulary Conflict — Not Resolved by This Hardening Pass

CPOS content uses an eight-office vocabulary (Executive, Learning, Engineering, Research, Knowledge Atlas, Review, Publishing, Operations Office) staffed by named engines (LUMIAION, Claude, Codex, Comet, Perplexity). This does not match the Founder-ratified Companion/Office structure from Sprint 1 (Office of Health, Office of Consciousness, Office of Knowledge, Office of Research, Office of Enterprise, Office of Education, Office of Community, Office of Nature Systems, Office of Publishing, Office of Intelligence Infrastructure, Innovation Lab, Human Experience Lab; Companions ATHENA/SOHMA/JERANIUM/GAIA/ORION/VORTEX), nor the earlier Vault Office Registry. Per this hardening sprint's instruction not to change Founder-ratified architecture, **CPOS's internal office vocabulary was left as-is** rather than rewritten to match. This is recorded as an unresolved Founder decision (see Sprint 1.5 output).

## Relationship to LOOM and the Founder Command Center

A separate Vault-based system (LOOM) is independently designated a Founder Command Center / Daily Executive Brief. CPOS's `DASHBOARD.md` performs an overlapping function inside this repository. Whether CPOS is subordinate to, parallel to, or the intended replacement for LOOM is not decided here.

## Design System Conformance

CPOS files do not yet use the Knowledge Design System (`../../DESIGN/`) — no callouts, no companion color attribution, no `document-layout-standard.md` fields. This is expected: CPOS predates Sprint 1 and was migrated, not authored against it. Bringing CPOS into conformance is recommended as a future sprint, not performed here.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-09 | Claude (Constitutional Secretary / Repository Architect) | Initial CPOS README, Sprint 1.5 Repository Hardening. |
