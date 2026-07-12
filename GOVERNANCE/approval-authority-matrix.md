---
title: Approval Authority Matrix
id: apx-governance-approval-authority-matrix
department: LUMIAION
domain: governance
type: policy
status: active
version: 1.0.0
created: 2026-07-11
updated: 2026-07-11
source: founder-request
tags: [governance, approval, ethics, canonical-approval]
related: [approval-policy.md, ../OPERATIONS/canonical-approval-record.md, ../OPERATIONS/CPOS/APPROVAL_GATES.md, ../INGESTION/ingestion-approval-gates.md, ../TEMPLATES/approval-record.template.md]
owner: "Ethics & Evidence Council (not yet seated) / LUMIAION"
---

# Approval Authority Matrix

## Purpose

Reconcile every approval mechanism currently in this repository — `approval-policy.md` (general), `../OPERATIONS/CPOS/APPROVAL_GATES.md` (production queue), `../INGESTION/ingestion-approval-gates.md` (ingestion pipeline) — into **one canonical approval model**. This document is that model. The other three remain in force for their specific contexts but now point here for the shared vocabulary and record format.

## Two Separate Status Fields — Not to Be Confused

This repository has, until now, used `status:` (frontmatter) inconsistently alongside an emerging `approval_status:` concept. This matrix fixes both, as two genuinely different fields:

| Field | Governs | Canonical Source | Values |
|---|---|---|---|
| `status:` | A document's own lifecycle | `../GOVERNANCE/versioning-policy.md` (already ratified, unchanged by this document) | `draft`, `active`, `review`, `approved`, `superseded`, `archived` |
| `approval_status:` | Whether a specific decision or piece of content has cleared the approval it requires | This document (new) | `draft`, `pending-review`, `internally-reviewed`, `founder-approved`, `ethics-reviewed`, `public-approved`, `superseded`, `archived`, `rejected` |

A document can be `status: active` (it's the current version of this file) while its content is `approval_status: pending-review` (nobody has signed off on the decision it records yet). These are not redundant — do not collapse them.

## Canonical Approval Model

Every approval, regardless of which subsystem raised it (CPOS gate, ingestion gate, governance decision, publication request), is recorded with these fields:

1. Decision ID.
2. Subject (what is being approved).
3. Requester.
4. Approving authority.
5. Date.
6. Scope (what the approval covers, and what it does not).
7. Status (`approval_status`, from the vocabulary above).
8. Conditions (if approved with conditions, state them).
9. Linked files (every document the decision affects).
10. Revision impact (what changes if this approval is later revised or superseded).

Template: `../TEMPLATES/approval-record.template.md`. Log location: `../OPERATIONS/canonical-approval-record.md`.

## Authority by Decision Type

| Decision Type | Approving Authority | Source |
|---|---|---|
| Strategy, positioning, business model | Founder | `approval-policy.md` |
| Public brand, offer, launch, publishing | Founder | `approval-policy.md` |
| Long-term architecture | Founder | `approval-policy.md` |
| Paid tools, vendors, infrastructure cost | Founder | `approval-policy.md` |
| Legal, privacy, safety, user-data risk | Founder | `approval-policy.md` |
| Irreversible migration, deletion, release | Founder | `approval-policy.md` |
| Health, wellness, education, complementary-practice content, pre-publication | Ethics & Evidence Council (not yet seated — see Standing Gap) | `../INGESTION/ingestion-approval-gates.md` Gate 3, Gate 6 |
| Production queue movement inside approved scope | No approval required | `../OPERATIONS/CPOS/APPROVAL_GATES.md` |
| Technical implementation of already-approved work | No approval required (Codex verifies, does not re-approve) | `ai-worker-jurisdiction.md` |
| Documentation formatting, metadata correction, index update | No approval required | `approval-policy.md` |

## Standing Gap

The Ethics & Evidence Council has no seated members. Any decision routed to it under this matrix stops and waits — it is not satisfied by Founder approval alone, and it is not skipped. This is unchanged from `../INGESTION/ingestion-approval-gates.md` and is repeated here because this matrix is now the canonical reference point.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-11 | Claude (Constitutional Secretary / Institutional Architect) | Initial Approval Authority Matrix, reconciling three prior approval mechanisms into one model, Phase II Sprint 2. |
