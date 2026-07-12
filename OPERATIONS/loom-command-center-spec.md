---
title: LOOM Command Center Specification
id: apx-operations-loom-command-center-spec
department: LUMIAION
domain: operations
type: operations-standard
status: active
version: 1.0.0
created: 2026-07-11
updated: 2026-07-11
source: founder-request
tags: [operations, loom, founder-brief, command-center]
related: [../TEMPLATES/designed-founder-brief.template.md, CPOS/DASHBOARD.md, ../GOVERNANCE/change-control-workflow.md]
owner: LUMIAION
---

# LOOM Command Center Specification

## Purpose

Fix LOOM as the single Founder Command Center, and give it one reconciled field list — superseding the two prior, slightly different field lists this repository has accumulated (Sprint 1's Founder Ratification clarification 5, and this sprint's own restated requirements).

## Status

LOOM is designated the single Founder Command Center. All executive briefings converge into LOOM. Duplicate briefing systems (`../OPERATIONS/CPOS/DASHBOARD.md`, `../OPERATIONS/CPOS/CURRENT_SPRINT.md`, and any Vault-repository equivalent) **must eventually be migrated or retired** — not performed by this document, which only fixes the target spec they migrate toward.

## Reconciled Field List

This supersedes the field list in `../TEMPLATES/designed-founder-brief.template.md` — that template should be updated to match this list in a future implementation pass, not performed here.

1. Pending decisions.
2. Repository status.
3. Knowledge updates.
4. Research updates.
5. Health and personal tracking status.
6. Business status.
7. CRM and lead status.
8. Content and publishing status.
9. Active risks.
10. Blockers.
11. Opportunities.
12. Required Founder approvals.
13. Sprint progress.

## Field Provenance

| Field | Absorbs / Replaces |
|---|---|
| Pending decisions | Prior "Pending Decisions" (unchanged). |
| Repository status | Prior "Repository Updates" / "Institutional Health" (merged — repository consistency is the concrete signal institutional health was measuring). |
| Knowledge updates | Unchanged. |
| Research updates | Unchanged. |
| Health and personal tracking status | Prior "health/gym log status" — restored as its own field (this sprint's instruction explicitly lists it separately, reversing the prior sprint's interpretation that it should only be an input to another field). |
| Business status | Unchanged. |
| CRM and lead status | New — more specific than prior "Business Updates," reflecting Office of Enterprise's ratified CRM/lead jurisdiction (`../ORGANIZATION/office-map.md`). |
| Content and publishing status | Prior "Content Status" — expanded to name Office of Publishing explicitly. |
| Active risks | Unchanged. |
| Blockers | New as a distinct field — previously folded into "Risks"; CPOS already tracks Blockers separately (`CPOS/BLOCKERS.md`), so LOOM now mirrors that distinction. |
| Opportunities | Unchanged. |
| Required Founder approvals | Unchanged. |
| Sprint progress | New — ties LOOM to `CPOS/CURRENT_SPRINT.md`'s content without duplicating its full detail. |

## Relationship to CPOS

LOOM is the Founder-facing summary; CPOS is the underlying production system. LOOM's Sprint Progress, Blockers, and CRM/Business fields should be populated *from* CPOS's `DASHBOARD.md`, `BLOCKERS.md`, and `AI_ASSIGNMENTS.md` rather than maintained independently, once migration occurs.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-11 | Claude (Constitutional Secretary / Institutional Architect) | Initial LOOM Command Center Specification, reconciling two prior field lists into one, Phase II Sprint 2. Migration to `designed-founder-brief.template.md` and CPOS not yet performed. |
