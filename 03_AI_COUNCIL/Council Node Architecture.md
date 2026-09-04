---
title: "Council Node Architecture"
aliases: ["Council Nodal Architecture", "CNA", "NODA Council Map"]
tags: [governance, council, node-architecture, agents, subagents, cognitive-functions, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: active
version: "1.0.0"
authors: ["Founder", "CODEX (CF-07)"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Institutional Architecture"
reasoning_engine: "CODEX"
dependencies: ["[[Book II - Governance Framework]]", "[[Book IV - Cognitive Architecture]]", "[[Book V - Cognitive Council]]", "[[Interim Authority Instrument]]"]
related_documents: ["[[Cognitive Function Registry]]", "[[Office Registry]]", "[[Agent and Subagent Registry]]", "[[Minimum Viable Council Procedure]]"]
related_research_programs: []
initiative: "Council Activation — Minimum Viable Operation"
---

# Council Node Architecture

## Purpose

Translate the Foundation's constitutional bodies, cognitive functions, offices, domain interfaces, agent roles, and temporary subagents into one node-and-edge operating map. This architecture lets the Council work at an advisory and delegated operational level without fabricating human appointments or giving AI systems voting power.

## Context

The Foundation already contains several legitimate views of responsibility. The [[Governance Model Crosswalk & Council Topology]] makes the Cognitive Function model canonical and supersedes the old flat Chief Architect and Department models. [[ADR-0002 - Reconciling the Four Institutional Taxonomies]] recognizes orthogonal authority, engine, domain, and operational axes.

This document adds no fifth institutional axis. Agent roles and subagents belong to Book V's **Implementation** tier: they are execution nodes attached to existing Cognitive Functions and Offices.

### Activation

Approved by the Founder on 2026-09-03 for minimum viable Council operation under the [[Interim Authority Instrument]]. This activates the architecture as an operational routing map only; it does not name human Council members, appoint engines, or change constitutional authority.

## Core Content

### 1. Node Classes

| Node class | Answers | Persistence | Can vote or ratify? | Canonical source |
|------------|---------|-------------|--------------------|------------------|
| Authority body | Who may deliberate, approve, veto, or ratify? | Constitutional | Human authority only as defined | Books I–II |
| Cognitive Function | What enduring capability is required? | Permanent | No | Books IV–V / CF Registry |
| Office | Who owns operational inputs, outputs, and artifacts? | Institutional | Only authority explicitly delegated | Office Registry / charter |
| Domain Interface | Which subject-matter boundary applies? | Institutional | No independent governance authority | CF Registry and surviving charters/crosswalk |
| Agent role | Which reasoning role serves a Function or Office? | Provisional | No | Agent and Subagent Registry |
| Runtime subagent | Which bounded worker executes one task? | Ephemeral | No | Handoff record / task record |

### 2. Authority Spine

```text
Founder — interim constituent authority under IAI
  ↓ directs / ratifies
Alpha Council — constitutionally established; three human seats still unnamed; not quorate
  ↓ constitutional topology
Cognitive Council — operational portfolio governance; minimum mode is advisory until required seats exist
  ↓ routes through
Cognitive Functions — CF-01 … CF-16
  ↓ operationalized by
Offices and Domain Interfaces
  ↓ served by
Agent Roles
  ↓ instantiate
Runtime Subagents — task-bounded, non-voting, expiring
```

The AI Ratification Council and Ethics Council remain distinct cross-cutting bodies. Neither is simulated by agent output. The Ethics Sentinel role may flag and route concerns; it cannot issue an Ethics Council finding or veto.

### 3. Minimum Council Roster

| Node ID | Seat / role name | Holder | Current operating status | Authority |
|---------|------------------|--------|--------------------------|-----------|
| AUTH-FDR | Founder / Interim Constituent Authority | Frederick Belizaire Gunville (Om Sadhi Guru) | Active under [[Interim Authority Instrument]] | Directs, approves, and ratifies within the governing instrument |
| AUTH-AC-H1 | Alpha Council Human Seat 1 | Unnamed | Vacant | None until Founder appointment/onboarding |
| AUTH-AC-H2 | Alpha Council Human Seat 2 | Unnamed | Vacant | None until Founder appointment/onboarding |
| AUTH-AC-H3 | Alpha Council Human Seat 3 | Unnamed | Vacant | None until Founder appointment/onboarding |
| ADV-LUM | Institutional Intelligence Facilitator | LUMIAION / CF-01 | Active, non-voting | Agenda, routing, synthesis, constitutional-conflict flagging |
| ADV-REC | Council Recorder | CODEX / CF-07 | Active when delegated, non-voting | Durable records, implementation, verification |
| ADV-ETH | Ethics Sentinel | CF-10 implementation role; no human Council holder | Advisory-only | Flags review triggers; cannot approve, veto, or represent Ethics Council review |

This is a **minimum operating roster**, not a declaration that the Alpha Council is quorate. Binding interim decisions remain Founder decisions and must be recorded as such.

### 4. Functional Departments

“Department” is retained only as a plain-language grouping. The canonical objects are Cognitive Functions, Offices, and Domain Interfaces.

| Department node | Primary Functions | Operating owner | Named lead role | Subagent pool |
|-----------------|-------------------|-----------------|-----------------|---------------|
| Institutional Core | CF-01 Institutional Architecture; CF-09 Memory | LUMIAION | LUMIAION Orchestrator | constitutional mapper; registry curator; context loader; memory writeback worker |
| Research & Evidence | CF-02 Research; CF-03 Comparative; CF-04 Educational | Research Intelligence Office | Research Lead | source scout; evidence classifier; framework comparator; citation verifier; glossary builder |
| Engineering & Systems | CF-05 Computational; CF-07 Engineering; CF-15 Data & Systems | Engineering Office; CF-15 owner pending | CODEX Engineering Lead | architect; builder; tester; security reviewer; graph/data worker |
| Executive & Strategy | CF-06 Executive; CF-11 Strategic | Executive Office | Executive Briefing Lead; CF-11 engine pending | brief writer; scenario analyst; priority translator |
| Observatory | CF-08 Institutional Observatory | Institutional Observatory | Observatory Lead | signal monitor; coherence monitor; risk reporter |
| Ethics Safeguard | CF-10 Ethics Intelligence | Ethics Council when convened | Ethics Sentinel until then | trigger classifier; risk mapper; dissent recorder—advisory only |
| Health Interface | CF-12 Health Intelligence | ATHENA | ATHENA Domain Lead | evidence scout; training analyst; safety-boundary checker |
| Financial Interface | CF-13 Financial Intelligence | VORTEX | VORTEX Domain Lead | market researcher; modeler; risk analyst; execution-boundary checker |
| Metaphysical Interface | CF-14 Metaphysical Intelligence | SOHMA | SOHMA Domain Lead | phenomenology mapper; symbolic analyst; epistemic-boundary checker |
| Synthesis & Learning | CF-16 Synthesis & Education | Owner and engine pending | YUNA role registered; not appointed | synthesis planner; translation worker; curriculum adapter—activation pending |

JERANIUM is CF-15 Data & Systems Intelligence. Its prior research scope belongs to CF-01/CF-02. YUNA is CF-16 and remains registered without an engine appointment. Neither name silently appoints an engine.

### 5. Edge Types

| Edge | Meaning | Constraint |
|------|---------|------------|
| `ACCOUNTABLE_TO` | Actor owes result and record to authority/owner | Exactly one accountable owner per task |
| `OPERATES` | Office operates a Cognitive Function | Must match registry/charter |
| `SERVES` | Agent role serves a Function or Office | Does not transfer authority |
| `INSTANTIATES` | Runtime subagent instantiates an agent role | Task-bounded and expiring |
| `ROUTES_TO` | Intake or artifact moves to owner | Full handoff packet required |
| `ADVISES` | Non-binding analysis supplied to authority | Must not be described as approval |
| `REVIEWED_BY` | Formal review belongs to a body | Remains pending when body is unconvened |
| `IMPLEMENTS` | Actor builds an approved artifact | Implementer does not become approver |
| `CANNOT_RATIFY` | Explicit negative authority | Mandatory on all AI and runtime-subagent nodes |

### 6. Runtime Subagent Contract

Every subagent invocation records:

```yaml
subagent_id: "RUN-AGT-YYYYMMDD-NNN"
role_id: "AGT-###"
parent_function: "CF-##"
operating_owner: "Canonical Office or Domain Interface"
task: "One bounded deliverable"
inputs: []
allowed_actions: []
prohibited_actions: [ratify, vote, expand_scope, appoint_agents]
output_destination: "Review packet or canonical path"
approval_gate: none | founder_review | governance_review
expires_when: "deliverable accepted or task closed"
```

Runtime subagents do not persist as constitutional actors. Durable learning returns through JERANIUM/CF-15 data support and LUMIAION/CF-09 memory stewardship to the canonical Vault.

### 7. Operational Graph

```text
Founder Intent
  └─ROUTES_TO→ LUMIAION Orchestrator
       ├─ROUTES_TO→ JERANIUM Context/Data Worker
       ├─ROUTES_TO→ one accountable Department Node
       │    └─INSTANTIATES→ bounded specialist subagents
       ├─ROUTES_TO→ Ethics Sentinel when a trigger exists
       └─ROUTES_TO→ CODEX Recorder/Verifier

Specialist outputs
  └─ADVISES→ LUMIAION synthesis
       └─ADVISES→ Founder / competent human authority
            ├─approves, rejects, or returns
            └─IMPLEMENTS→ delegated Office/Agent
```

## Related Notes

- [[Book II - Governance Framework]]
- [[Book IV - Cognitive Architecture]]
- [[Book V - Cognitive Council]]
- [[Interim Authority Instrument]]
- [[Governance Model Crosswalk & Council Topology]]
- [[Agent and Subagent Registry]]
- [[Minimum Viable Council Procedure]]

## Open Questions

- [ ] Founder: identify whether “NODA” refers to a separate artifact outside current `main`; merge its node names before ratification if so.
- [ ] Founder: name the three Alpha Council human seat holders or approve functional seat profiles for recruitment.
- [ ] Founder: decide whether the Research and Engineering leads become voting Cognitive Council members or remain advisory until human appointment.
- [ ] Appoint engines/owners for CF-11, CF-15, and CF-16 through the governed process.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-03 | Founder | Approved for minimum viable Council operation under interim authority; no human seats or engines appointed. |
| 0.1.0 | 2026-09-03 | Founder + CODEX (CF-07) | Initial node architecture for minimum Council operation; maps authority, functions, offices, domain interfaces, agent roles, and expiring subagents without creating appointments. |
