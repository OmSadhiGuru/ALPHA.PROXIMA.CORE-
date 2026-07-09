---
title: Approval Gates
id: apx-operations-cpos-approval-gates
department: LUMIAION
domain: operations
type: operations-gate
status: active
version: 1.0.0
created: 2026-07-09
updated: 2026-07-09
source: migration
tags: [operations, cpos, approval]
related: [DASHBOARD.md, BLOCKERS.md]
owner: "Operations Office (legacy-reference — not a ratified Constitutional Office; see repository hardening notes)"
---

# Approval Gates

Question answered: What decisions require Founder approval before work continues?

## Approval Boundary

Founder approval is required for:

- Strategy, positioning, or business model changes.
- Public brand, offer, launch, or publishing decisions.
- Long-term architecture decisions.
- Paid tools, subscriptions, vendors, or infrastructure costs.
- Legal, privacy, safety, or user-data risk.
- Irreversible migrations, deletions, or releases.

Founder approval is not required for:

- Queue movement inside approved scope.
- Research summaries.
- Draft options.
- Markdown cleanup.
- Technical implementation of approved tasks.
- Handoff and blocker maintenance.

## Open Approval Gates

| ID | Related Task ID | Requesting Department | Current Employee | Decision Needed | Options | Impact | Status | Founder Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AG-001 |  |  |  |  |  |  | Open |  |

Status values: Open, Approved, Rejected, Superseded.

## Handling Rule

When a task reaches an approval gate, mark that task Waiting Approval in its queue, open an entry here, and pull the next eligible Ready task. Do not stop production unless every queue is blocked by the same decision.

## Approval Log

| Date | ID | Decision | Notes |
| --- | --- | --- | --- |
|  |  |  |  |
