---
title: Partner Access Model
id: apx-governance-partner-access-model
department: LUMIAION
domain: governance
type: policy
status: active
version: 1.0.0
created: 2026-07-11
updated: 2026-07-11
source: founder-request
tags: [governance, partners, contributors, access]
related: [institutional-authority-model.md, ../TEMPLATES/guest-contribution-node.template.md]
owner: "Founder's Office (scope pending Founder ratification)"
---

# Partner Access Model

## Purpose

Define access, onboarding, authority, and removal procedure for every contributor tier. This is the first version of this model actually filed in this repository — a Partnership Charter covering similar ground was drafted separately but is not filed here (pending source); this document does not depend on it and should be treated as the operative version for this repository going forward.

## Tiers

| Tier | Access Level | Onboarding | Decision Authority | Repository Access | Confidentiality | Permitted Contributions | Approval Required | Removal/Suspension |
|---|---|---|---|---|---|---|---|---|
| **Executive Council** | Broad, not unrestricted | Founder-conducted | Governance input, strategic review | Read all; write within Founder-assigned scope | Full institutional NDA-equivalent expected | Governance review, strategic input | Founder | Founder, for cause |
| **Constitutional Partners** | Scoped to partnered Office(s) | Formal onboarding per `../TEMPLATES/guest-contribution-node.template.md` pattern, extended | Standing input within partnered Office | Read/write within partnered Office's folders | Institutional NDA-equivalent for partnered domain | Ongoing work within partnered Office | LUMIAION or Founder, per `approval-authority-matrix.md` | Founder or LUMIAION, for cause |
| **Core Contributors** | Scoped to assigned Office(s) or project(s) | Formal onboarding, standards briefing | None beyond assigned scope | Read/write within assignment | Confidentiality for assigned domain | Ongoing operational work | Per `approval-authority-matrix.md`, by decision type | LUMIAION, for cause |
| **Guest Contributors** | **Scoped access only** — the narrowest working tier | Guest Contribution Node (below) | None | Read scoped materials; write to scoped deliverable only | Confidentiality for the scoped task | Single scoped task | Gate defined in the Guest Contribution Node | Automatic at task close, or earlier for cause |
| **Community Contributors** | Public-facing (OSGMETAPHYSICS) only | Public-tier onboarding, not institutional | None | No institutional repository access | Standard public terms | Public engagement, feedback, community content | Not applicable — public tier | Standard community moderation |

## Principles

1. No tier below Founder receives unrestricted authority.
2. Every tier requires completed onboarding before participation.
3. Authority is exercised only within assigned scope — a Core Contributor to the Office of Health has no standing in the Office of Enterprise absent separate scoping.

## The Guest Contribution Node

Every Guest Contributor receives, before any task begins:

1. Vision summary.
2. Mission.
3. Architecture map (`../ORGANIZATION/office-map.md`, `../ORGANIZATION/repository-ownership-map.md`).
4. Current roadmap (`../OPERATIONS/CPOS/ROADMAP.md`).
5. Coding or writing standards (`../DESIGN/`, `../GOVERNANCE/documentation-standard.md`).
6. Scoped task.
7. Acceptance criteria.
8. Approval gate (per `approval-authority-matrix.md`).
9. Handoff procedure (`../TEMPLATES/worker-handoff.template.md`).

**No guest receives unrestricted access by default.** Template: `../TEMPLATES/guest-contribution-node.template.md`.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-11 | Claude (Constitutional Secretary / Institutional Architect) | Initial Partner Access Model, Phase II Sprint 2 — first filed version of this ground, superseding pending-source status for this specific content. |
