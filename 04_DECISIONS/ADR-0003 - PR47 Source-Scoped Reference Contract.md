---
title: "ADR-0003 - PR47 Source-Scoped Reference Contract"
aliases: ["ADR-0003", "PR47 Reference Contract", "Historical Run Preservation Contract"]
tags: [adr, governance, engineering, identity, state, alpha-proxima]
created: 2026-09-22
updated: 2026-09-22
status: accepted
version: "1.0.0"
authors: ["Founder", "CODEX"]
document_class: ADR
adr_code: ADR-0003
decision_class: "Class II"
decision_status: accepted
ratified_by: "Founder under the Interim Authority Instrument"
ratification_date: 2026-09-22
supersedes: null
superseded_by: null
related_documents: ["[[PR47 Identity and State Safety Review]]", "[[Agent and Subagent Registry]]", "[[Validation Debt Policy]]", "[[Interim Authority Instrument]]"]
artifact_type: "architecture decision record"
dependencies: ["[[PR47 Identity and State Safety Review]]", "[[Interim Authority Instrument]]"]
institutional_owner: "Alpha Proxima Foundation"
related_research_programs: []
---

# ADR-0003 — PR47 Source-Scoped Reference Contract

## Decision

The Founder ratifies the bounded recommendation in [[PR47 Identity and State Safety Review]]:

1. Historical Founder records keep their original roster references unchanged.
2. Any future cross-store identity reference must include its source namespace and source revision.
3. A future approved crosswalk, if needed, belongs in one governance-owned record from which read models are derived. It must not create a second mutable state store.
4. An absent or unapproved mapping remains unresolved and cannot authorize an appointment, a state migration, an execution, or an identity rewrite.

This decision is in force under the [[Interim Authority Instrument]]. It establishes a reference-safety boundary; it does not appoint an agent, amend Founder or Council state, or alter any historical run.

## Scope of ratification

The following are ratified only as constraints:

| Subject | Ratified constraint |
|---|---|
| `RUN-001` | Its recorded Founder `AGT-006` / JERANIUM reference and route remain historical evidence. It must not be reinterpreted as Council `AGT-006` Executive Briefing Lead. |
| Shared `AGT-*` strings | Equal strings across Founder OS and the Council registry are not proof of identity. |
| Future integrations | Source namespace and revision are required before any join or migration. |
| Derived interfaces | Office, Galaxy and read models may display source-scoped references but may not create or mutate canonical identity truth. |

## Explicitly not ratified

This ADR does **not** approve any candidate correspondence in the PR #47 review, including LUMIAION, CODEX, PERPLEXITY, COMET, ATHENA, SOHMA, VORTEX, CLAUDE or JERANIUM. It also does not:

- change the canonical [[Agent and Subagent Registry]];
- modify `founder-state.json`, `council-state.json`, roles, departments or appointments;
- decide any of the 16 governance-dependent validation errors;
- create a new agent, identity node, state schema or runtime mapping;
- authorize live model execution or promote Galaxy beyond its read-only prototype role.

The candidate mappings and debt dispositions remain review material in [[PR47 Identity and State Safety Review]]. They require separate, explicit Founder decisions before implementation.

## Consequences

The atomic JSON publication implementation merged through PR #47 remains the existing technical safeguard for complete-file visibility. It is not a transaction lock, a concurrency policy, or a cross-store mapping mechanism. Any concurrency or migration work must be proposed and reviewed separately against this ADR.

The repository architecture remains:

```text
Canonical institutional truth
  -> source-scoped parser and state
  -> derived read model
  -> Office / Galaxy visualization
```

## Ratification record

| Field | Record |
|---|---|
| Date | 2026-09-22 |
| Authority | Founder under the Interim Authority Instrument |
| Decision | Approve PR #47's source-scoped reference and historical-run preservation contract only |
| Evidence | Explicit Founder instruction: “lets fix PR #46 #47 and ratified #47 so everything align and follow the system architechture” |

## Review trigger

Review this ADR before any identity migration, cross-store join, roster rename, state-schema change, or concurrent writer design. A proposed mapping alone is insufficient.

## Version history

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-09-22 | Founder / CODEX | Founder ratification of the bounded PR #47 reference-safety contract. |
