---
title: "Minimum Viable Council Procedure"
aliases: ["MVC Procedure", "MVC Protocol", "Interim Council Operating Protocol", "Minimum Council Protocol"]
tags: [operations, council, interim-authority, agents, deliberation, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: active
version: "1.0.0"
authors: ["Founder", "CODEX (CF-07)"]
artifact_type: operational-procedure
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Institutional Architecture"
reasoning_engine: "CODEX"
dependencies: ["[[Interim Authority Instrument]]", "[[Council Node Architecture]]", "[[Founder Intent Routing Procedure]]"]
related_documents: ["[[Agent and Subagent Registry]]", "[[Alpha Council]]", "[[Cognitive Council Charter]]"]
related_research_programs: []
---

# Minimum Viable Council Procedure

## Purpose

Allow structured Council-level work to begin before the Alpha Council's three human seats and the Ethics Council membership are filled. The protocol creates an advisory and delegated execution loop around the Founder; it does not declare either Council quorate.

## Context

The [[Interim Authority Instrument]] makes the Founder the interim constituent authority and explicitly forbids pretending that the Alpha Council already exists as a voting body. The Foundation nevertheless needs a repeatable way to gather independent analysis, preserve dissent, make Founder decisions, and route approved execution.

### Activation

Approved by the Founder on 2026-09-03 and activated under the [[Interim Authority Instrument]]. The first activation record is [[MVC-001 Council Activation Record]]. This procedure remains limited to advisory and delegated work until human seats are filled and the interim instrument sunsets.

## Core Content

### 1. Operating Mode

The minimum viable Council is:

- **Founder** — sole interim human decision and ratification authority;
- **LUMIAION Orchestrator** — non-voting facilitator, router, and synthesizer;
- **Council Recorder (CODEX)** — non-voting record and verification role when delegated;
- **relevant Agent Leads** — non-voting advisors selected by domain;
- **Ethics Sentinel** — non-voting trigger and risk classifier, never a substitute for the Ethics Council.

No session under this protocol counts as a quorate Alpha Council, Cognitive Council, AI Ratification Council, or Ethics Council meeting.

### 2. Permitted Outputs

| Output | Effect |
|--------|--------|
| Advisory opinion | Non-binding analysis for Founder review |
| Council synthesis | Reconciled options, evidence, dissent, and recommendation |
| Founder interim decision | Binding only within the Founder's valid interim authority and exact recorded scope |
| Class I/II proposal | Draft only until explicit Founder ratification and required process |
| Delegated Class III/IV task | Executable within recorded authority and approval gates |
| Ethics trigger notice | Pauses/routes review where required; not an Ethics finding |

### 3. Session Flow

1. **Open** — assign `MVC-YYYYMMDD-NNN`; preserve the Founder's exact intent.
2. **Classify** — identify decision class, authority, risk, domain, and review gates.
3. **Map nodes** — select one accountable Agent Lead and only necessary advisors/subagents.
4. **Investigate** — advisors work independently when comparison or dissent matters.
5. **Challenge** — one assigned reviewer tests assumptions, scope, evidence, and failure modes.
6. **Synthesize** — LUMIAION returns options, recommendation, dissent, and one next action.
7. **Decide** — Founder approves, rejects, revises, ratifies, or defers in explicit language.
8. **Execute** — approved Class III/IV work routes to the accountable Office/Agent.
9. **Record** — CODEX or delegated Recorder writes the exact decision and evidence.
10. **Write back** — Memory Steward preserves durable context; unresolved items enter the Open Questions Register.

### 4. Session Record

```yaml
session_id: "MVC-YYYYMMDD-NNN"
founder_intent: "Exact request"
decision_class: "I | II | III | IV"
interim_authority_basis: "Interim Authority Instrument section, or none"
facilitator: "AGT-001 LUMIAION Orchestrator"
accountable_role: "AGT-###"
advisors: []
subagent_runs: []
ethics_trigger: "none | advisory | formal-review-required"
dissent: []
recommendation: "Non-binding recommendation"
founder_decision: "Exact words, or pending"
execution_owner: "Canonical Office/Agent, or none"
writeback: []
state: "open | investigating | founder-review | approved | executing | complete | blocked"
next_action: "One executable action"
```

### 5. Stop Conditions

The session stops and returns to the Founder when:

- a human seat appointment, engine appointment, or scope expansion is required;
- an Ethics Council review is constitutionally required but unavailable;
- authority is ambiguous or conflicting;
- personal, health, financial, legal, publication, credential, or destructive action exceeds delegation; or
- advisors cannot preserve a material disagreement in one honest decision surface.

### 6. Activation and Sunset

This protocol becomes operational only after explicit Founder approval of its exact version or commit. It sunsets or is amended when the Interim Authority Instrument expires after at least two human Alpha Council seats are filled and the first quorate session occurs.

## Related Notes

- [[Interim Authority Instrument]]
- [[Council Node Architecture]]
- [[Agent and Subagent Registry]]
- [[Founder Intent Routing Procedure]]
- [[Institutional Open Questions Register]]

## Open Questions

- [ ] What is the standard response time for a minimum viable Council session?
- [ ] Which sessions require an independent challenger by default?
- [ ] Where should MVC session records live after activation?

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-03 | Founder | Approved and activated under the Interim Authority Instrument for advisory and delegated Council work. |
| 0.1.0 | 2026-09-03 | Founder + CODEX (CF-07) | Initial minimum operating protocol under Founder interim authority; advisory and delegated work only until human seats are filled. |
