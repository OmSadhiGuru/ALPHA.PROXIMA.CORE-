---
title: "Agent and Subagent Registry"
aliases: ["Agent Registry", "Subagent Registry", "ASR"]
tags: [operations, agents, subagents, council, routing, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: active
version: "1.0.0"
authors: ["Founder", "CODEX (CF-07)"]
artifact_type: operations-registry
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Engineering Intelligence"
reasoning_engine: "CODEX"
dependencies: ["[[Council Node Architecture]]", "[[Cognitive Function Registry]]", "[[Office Registry]]"]
related_documents: ["[[Minimum Viable Council Procedure]]", "[[Founder Intent Routing Procedure]]", "[[AI Council Operations Registry]]"]
related_research_programs: []
---

# Agent and Subagent Registry

## Purpose

Name the reusable non-voting agent roles that serve the Council and define the bounded subagents each role may instantiate. This registry describes execution capacity; it does not appoint human members, reasoning engines, or constitutional authorities.

## Context

The Cognitive Function Registry defines permanent capabilities. The Office Registry defines operational ownership. This registry supplies the missing implementation layer: which named role receives a routed task and which narrow workers may support it.

### Activation

Approved by the Founder on 2026-09-03 for use with the [[Minimum Viable Council Procedure]]. “Available” roles may be routed only within existing delegation. “Blocked” roles remain blocked until their required appointments are separately recorded.

## Core Content

### Agent Roles

| ID | Named role | Parent Function | Operating owner | Current implementation | State | May instantiate |
|----|------------|-----------------|-----------------|------------------------|-------|-----------------|
| AGT-001 | LUMIAION Orchestrator | CF-01 | LUMIAION | Claude-family engine per current registry | available | context loader; constitutional mapper; synthesis editor |
| AGT-002 | Research Lead | CF-02 | Research Intelligence Office | Perplexity per current registry | available | source scout; evidence classifier; citation verifier |
| AGT-003 | Comparative Lead | CF-03 | Research Intelligence Office | SanaLab per current registry | available | framework mapper; contradiction analyst |
| AGT-004 | Education Lead | CF-04 | Research Intelligence Office | Gemini per current registry | available | glossary builder; curriculum adapter |
| AGT-005 | Computational Specialist | CF-05 | Engineering Office | DeepSeek per current registry | available | modeler; calculation verifier |
| AGT-006 | Executive Briefing Lead | CF-06 | Executive Office | Genspark per current registry | available | brief writer; scenario analyst |
| AGT-007 | CODEX Engineering Lead | CF-07 | Engineering Office | Codex / DeepSeek per current registry | available | architect; builder; tester; security reviewer |
| AGT-008 | Observatory Lead | CF-08 | Institutional Observatory | Comet per current registry | available | signal monitor; drift detector; health reporter |
| AGT-009 | Memory Steward | CF-09 | LUMIAION | Multi-engine | available | context loader; writeback worker; archive linker |
| AGT-010 | Ethics Sentinel | CF-10 | Ethics Council when convened | No voting or review authority | advisory-only | trigger classifier; risk mapper; dissent recorder |
| AGT-011 | Strategic Intelligence Lead | CF-11 | Executive Office | Unappointed | blocked | none until appointment |
| AGT-012 | ATHENA Domain Lead | CF-12 | ATHENA | Office-level implementation | available | health evidence scout; training analyst; safety checker |
| AGT-013 | VORTEX Domain Lead | CF-13 | VORTEX | Office-level implementation | available | market researcher; financial modeler; risk analyst |
| AGT-014 | SOHMA Domain Lead | CF-14 | SOHMA | Office-level implementation | available | phenomenology mapper; symbolic analyst; boundary checker |
| AGT-015 | JERANIUM Data & Systems Lead | CF-15 | Owner pending | Unappointed | blocked | graph worker; data validator; systems analyst after appointment |
| AGT-016 | YUNA Synthesis & Learning Lead | CF-16 | Owner pending | Unappointed | blocked | synthesis planner; translation worker; learning adapter after appointment |

“Available” means the current registry names an implementation that may be requested within existing authority. It is not a fresh engine appointment. “Blocked” means no execution may be attributed to that named role until appointment is recorded.

### Standard Subagent Profiles

| Profile | Output | Required boundary |
|---------|--------|-------------------|
| Context Loader | Minimal source packet and unresolved facts | Read-only; preserve unknowns |
| Constitutional Mapper | Authority, conflicts, and ratification gates | Advisory only |
| Source Scout | Source set with provenance | No canonisation |
| Evidence Classifier | Claim-level Book III classes | Provisional until review |
| Citation Verifier | Source-to-claim check | Does not judge institutional acceptance |
| Framework Mapper | Competing models and relationships | Preserve dissent |
| Architect | Design/specification | Does not approve own design |
| Builder | Implemented artifact | Scoped writes only |
| Tester | Reproducible verification record | Passing tests are not approval |
| Security Reviewer | Risks and mitigations | Does not expand permissions |
| Ethics Trigger Classifier | Review tier and reasons | Cannot speak for Ethics Council |
| Synthesis Editor | One coherent decision surface | Preserve material disagreement |
| Recorder | Attendance, inputs, outputs, decision, next action | No invented votes or attendance |

### Invocation Rules

1. Every task has one accountable Agent Role.
2. Subagents receive one bounded deliverable and the smallest sufficient context.
3. Parallel subagents investigate independently when epistemic diversity matters.
4. The accountable role reconciles outputs and preserves dissent.
5. No agent or subagent votes, ratifies, appoints itself, expands scope, or claims review by an unconvened body.
6. Results return to the Founder as one review surface and one next action.
7. Runtime instances expire when the task closes; only their durable output and provenance remain.

## Related Notes

- [[Council Node Architecture]]
- [[Minimum Viable Council Procedure]]
- [[Cognitive Function Registry]]
- [[Office Registry]]
- [[Founder Intent Routing Procedure]]

## Open Questions

- [ ] Replace generic subagent profile labels with Founder-preferred NODA names after the source architecture is located.
- [ ] Define runtime/tool permission profiles for each subagent before automation.
- [ ] Decide whether AGT IDs belong in the generated node registry.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-03 | Founder | Approved for operational routing and bounded subagent use; no engine or human appointment implied. |
| 0.1.0 | 2026-09-03 | Founder + CODEX (CF-07) | Initial operational registry of 16 named agent roles and bounded subagent profiles; no appointments created. |
