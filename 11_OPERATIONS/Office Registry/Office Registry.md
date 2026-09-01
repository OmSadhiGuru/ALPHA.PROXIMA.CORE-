---
title: "Office Registry"
aliases: ["Institutional Office Registry", "Foundation Office Registry"]
tags: [operations, office-registry, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: operations-registry
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[The Orchestration Framework]]", "[[Institutional Relationship Map]]"]
related_documents: ["[[11_OPERATIONS]]", "[[AI Council Operations Registry]]", "[[Artifact Registry]]"]
related_research_programs: []
---

# Office Registry

## Purpose

Define the current offices of the Alpha Proxima Foundation in operational terms so contributors can understand who receives what, who produces what, and where Engineering support belongs.

---

## Scope

This registry describes offices as operating units. It does not create or redefine constitutional authority.

---

## Dependencies

- [[The Orchestration Framework]]
- [[Institutional Relationship Map]]
- [[AI Council Registry]]
- [[Engine Registry]]

---

## Version

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | active |
| **Last Updated** | 2026-07-02 |

---

## Author

[[CODEX]]

---

## Related Documents

- [[11_OPERATIONS]]
- [[AI Council Operations Registry]]
- [[Workflow Registry]]
- [[Artifact Registry]]

---

## Related Research Programs

- N/A

---

## Implementation Notes

Fields in this registry support routing and automation. Authority remains defined by constitutional and governance documents.

---

## Future Improvements

- [ ] Add office-level service-level expectations.
- [ ] Add office-specific intake forms.
- [ ] Add automation hooks after workflow tooling exists.

---

## Core Content

| Office | Purpose | Authority | Inputs | Outputs | Artifacts Produced | Review Cycle | Dependencies | Responsible Cognitive Function | Preferred Reasoning Engine | Engineering Support |
|--------|---------|-----------|--------|---------|--------------------|--------------|--------------|--------------------------------|----------------------------|--------------------|
| LUMIAION / Institutional Intelligence | Orchestrate institutional continuity, memory, routing, and synthesis | Orchestration and constitutional alignment within defined architecture | Founder requests, office outputs, open questions, review packets | Routed work, synthesis, continuity notes, operational coordination | Orchestration summaries, routing decisions, memory writebacks | Daily and weekly | [[LUMIAION Charter]], [[The Orchestration Framework]] | Orchestration | LUMIAION | Context loading, note generation, validation, dashboards |
| Institutional Architecture | Define and evolve institutional architecture through approved process | Architecture recommendation and specification, subject to governance | Future proposals, operational gaps, research signals, governance constraints | Architecture specifications, proposals, ADR-ready material | Architecture specs, relationship maps, protocols | Monthly and quarterly | [[Foundational Architecture]], [[Future Expansion Protocol]] | Architecture | Claude | Diagramming, versioning, consistency validation |
| Engineering Office | Build tools, automation, standards, validation, and local-first infrastructure | Implementation only; no governance authority | Approved architecture, engineering debt, validation reports, automation requests | Tools, reports, scripts, templates, infrastructure | Engineering standards, validators, CLIs, implementation notes | Daily and weekly | [[ALPHA PROXIMA ENGINEERING HANDBOOK]], [[Alpha Proxima Engineering Toolkit]] | Implementation | CODEX | Primary office |
| Research Intelligence Office | Produce and package external evidence and research materials | Research production and evidence gathering; not canonization | Research commissions, questions, source requests | Research packages, source notes, evidence packets | Research packages, source registries, evidence summaries | Per commission and monthly | [[Research Governance Protocol]], [[Research Council]] | Research | Perplexity Compute | Research package generators, source registries |
| Institutional Observatory | Monitor signals, patterns, risks, drift, and system health | Observation and reporting; not decision authority | Metrics, vault state, external signals, office reports | Observation reports, alerts, trend summaries | Observatory reports, drift logs, metrics snapshots | Daily and weekly | [[Metrics Registry]], [[Operational Health Index]] | Observation | Comet | Dashboards, metrics, graph health, automation monitors |
| Executive Office | Founder-level prioritization and institutional direction | Founder authority as defined by Constitution | Review packets, proposals, escalations, strategic questions | Priorities, approvals, direction, delegation | Executive notes, priority lists, decision requests | Daily, weekly, quarterly | [[Book I - The Constitution]], [[ADR-0001 - The Founding Decision]] | Executive | Founder / LUMIAION support | Brief generation, queue management |
| Future Office | Preserve future proposals until mature | Preservation and review routing; no automatic approval | Ideas, recommendations, feature requests, technology watch items | Routed proposals, archive rationale, review queue | Future proposals, watch items, review queue entries | Monthly and quarterly | [[09_FUTURE]], [[Future Expansion Protocol]] | Evolution | LUMIAION / CODEX support | Proposal templates, queue reports |

---

## Open Questions

- [ ] Should the Institutional Observatory receive a formal charter?
- [ ] Should Engineering Office be represented under `03_AI_COUNCIL` or only operationally here?
- [ ] Should each office have a dedicated intake queue?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial office registry |

