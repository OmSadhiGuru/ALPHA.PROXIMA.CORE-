---
title: Production Queue
id: apx-operations-cpos-production-queue
department: LUMIAION
domain: operations
type: operations-queue
status: active
version: 1.0.0
created: 2026-07-09
updated: 2026-07-09
source: migration
tags: [operations, cpos, production]
related: [BLUEPRINT_QUEUE.md, REVIEW_QUEUE.md]
owner: "Operations Office (legacy-reference — not a ratified Constitutional Office; see repository hardening notes)"
---

# Production Queue

Question answered: What is ready to be built, edited, written, or packaged now?

## Entry Criteria

- The task has a clear blueprint, acceptance criteria, or obvious operational need.
- Dependencies are available or explicitly marked.

## Exit Criteria

- The artifact is complete enough for review.
- Git status, files changed, and verification are recorded in handoff.

## Queue

| Priority | Status | Task ID | Work Item | Owner Department | Current Employee | Dependencies | Approval Required | Next Department | Estimated Effort | Linked Documents |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | Review | PRD-001 | Refactor OSG Operating Office into CPOS v1.0 Markdown operating framework | Operations Office | Codex | Founder request | No | Review Office | M | `OPERATIONS/CPOS/` |
| P1 | Ready | PRD-002 | Add missing cross-links between CPOS dashboard, queues, gates, blockers, and handoffs | Engineering Office | Codex | PRD-001 | No | Review Office | S | `OPERATIONS/CPOS/` |
| P2 | Ready | PRD-003 | Prepare lightweight verification notes for existing Flask routes and modules | Engineering Office | Codex |  | No | Review Office | S | `main.py` |
