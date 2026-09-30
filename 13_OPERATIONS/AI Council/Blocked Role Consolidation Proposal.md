---
title: "Blocked Role Consolidation Proposal"
aliases: ["Blocked Role Coverage", "AGT-011 AGT-015 AGT-016 Consolidation"]
tags: [operations, council, agents, governance, proposal]
created: 2026-09-30
updated: 2026-09-30
status: draft
version: "0.1.0"
authors: ["Founder", "CODEX"]
artifact_type: governance-proposal
institutional_owner: "Alpha Proxima Foundation"
dependencies: ["[[Agent and Subagent Registry]]", "[[Founder Intent Routing Procedure]]"]
related_documents: ["[[Galaxy Council Prototype — Concept Note]]", "[[Council Node Architecture]]"]
related_research_programs: []
---

# Blocked Role Consolidation Proposal

## Purpose

Reduce duplicated planning capacity while preserving the historical identities
and non-executable status of AGT-011, AGT-015, and AGT-016. This proposal does
not appoint an engine, activate a role, change Founder State, or merge Council
and Founder identifiers.

## Current condition

| Council ID | Blocked role | Why it is blocked |
|---|---|---|
| AGT-011 | Strategic Intelligence Lead | Implementation is unappointed. |
| AGT-015 | JERANIUM Data & Systems Lead | Owner and implementation are unappointed. |
| AGT-016 | YUNA Synthesis & Learning Lead | Owner and implementation are unappointed. |

These IDs are Council registry identities. They are not interchangeable with
same-looking IDs or names in Founder State. In particular, a historical
Founder-State JERANIUM record must not appoint, activate, or satisfy Council
AGT-015.

## Recommended operational coverage

| Blocked capacity | Existing accountable role | Bounded coverage | Boundary |
|---|---|---|---|
| AGT-011 strategic intelligence | AGT-006 Executive Briefing Lead | Executive briefs and scenario framing | AGT-006 does not become AGT-011 or receive strategic decision authority. |
| AGT-015 data and systems | AGT-007 CODEX Engineering Lead | Technical data validation and systems implementation | AGT-007 may act only through an approved engineering brief; AGT-015 remains blocked. |
| AGT-016 synthesis and learning | AGT-001 LUMIAION Orchestrator | Cross-office synthesis and routing of learning outputs | AGT-001 coordinates; learning artifacts remain bounded and do not create a YUNA appointment. |

The relevant specialist can be requested as a bounded subagent under the
existing accountable role. That preserves one accountable role per task and
does not create a fourth permanent identity.

## What consolidation means

1. New Council tasks must use AGT-006, AGT-007, or AGT-001 for these three
   scopes.
2. AGT-011, AGT-015, and AGT-016 remain in the registry as `blocked` so prior
   records, Galaxy, and the entity registry retain their source identity.
3. Galaxy continues to show AGT-015 and AGT-016 as unassigned. It does not
   visually assign them to an office or treat coverage as an appointment.
4. No task, output, or run may claim that AGT-011, AGT-015, or AGT-016
   executed work while blocked.

## Founder decision required

The Founder may ratify this operational coverage model. A later separate
decision is still required to appoint, retire, rename, or activate any of the
three blocked roles. Those changes are intentionally outside this proposal.

## Verification

- The Council Kernel must continue to reject AGT-011, AGT-015, and AGT-016 as
  owners or execution roles.
- The Role Registry must continue to report three blocked roles.
- The Galaxy must render the two owner-pending roles as unassigned and must
  not fabricate a department or agent.
