---
title: "Artifact Registry"
aliases: ["Institutional Artifact Registry", "Foundation Artifact Catalog"]
tags: [operations, artifacts, registry, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: operations-registry
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Office Registry]]", "[[Workflow Registry]]", "[[Vault Structure Convention]]"]
related_documents: ["[[11_OPERATIONS]]", "[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_research_programs: []
---

# Artifact Registry

## Purpose

Catalog institutional artifact types so contributors know what each artifact is for, who owns it, how it is approved, where it belongs, and how it evolves.

---

## Scope

This registry covers institutional, research, governance, engineering, operations, and future-evolution artifacts.

---

## Dependencies

- [[Vault Structure Convention]]
- [[02 - YAML Frontmatter Standard]]
- [[04 - File Naming Convention]]

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
- [[Office Registry]]
- [[Workflow Registry]]
- [[Review Cycles Registry]]

---

## Related Research Programs

- N/A

---

## Implementation Notes

Storage locations reflect current architecture. If architecture changes, this registry should be updated rather than silently drifting.

---

## Future Improvements

- [ ] Add artifact IDs.
- [ ] Add artifact creation templates.
- [ ] Add validation schemas per artifact type.

---

## Core Content

| Artifact | Purpose | Owner | Approval Authority | Lifecycle | Storage Location | Versioning Rules |
|----------|---------|-------|--------------------|-----------|------------------|------------------|
| Constitution | Supreme institutional law | Governance Authority | Founder / constitutional process | draft -> ratified -> amended -> archived | `00_CONSTITUTION/` | Major amendments require governance record |
| Law | Binding institutional rule below Constitution | Governance Authority | Relevant governance process | draft -> review -> ratified -> superseded | `00_CONSTITUTION/` or approved governance area | Semantic versioning plus decision record |
| ADR | Durable decision record | Relevant decision owner | Decision authority by class | proposed -> accepted -> superseded -> archived | `04_DECISIONS/` | Sequential ID, immutable rationale |
| Concept Note | Structured proposal before decision | Proposal author / receiving council | Receiving council or Founder | draft -> under_review -> approved_for_adr/rejected/withdrawn | `05_PROPOSALS/` | Semantic versioning while active |
| Research Commission | Request for research work | Research Office / commissioning office | Research governance process | draft -> commissioned -> converted -> archived | `09_FUTURE/Research Commissions/` or future research intake | Commission ID |
| Research Package | Delivered research evidence package | Research Intelligence Office | Research review process | intake -> review -> integrated -> archived | `07_RESEARCH/` | Research program versioning |
| Canonical Synthesis | Integrated research synthesis | Research Office | Research Council or approved authority | draft -> under_review -> canonical -> revised | `07_RESEARCH/RP-XXX/` | Version history required |
| Engineering Standard | Reusable engineering rule | Engineering Office | Engineering Office within architecture boundary | draft -> active -> deprecated -> superseded | `08_SYSTEMS/Engineering Standards/` | Semantic versioning |
| Future Proposal | Preserved future idea | Future Office | Routing authority by destination | draft -> review_queue -> routed -> archived | `09_FUTURE/` | Future ID and version |
| Strategic Review | Strategy and priority review | Executive Office / Strategy | Founder or relevant office | draft -> reviewed -> actioned -> archived | `02_STRATEGY/` or `11_OPERATIONS/` | Review period versioning |
| Operational Procedure | Repeatable operating process | Operations Layer | Relevant office owner | draft -> active -> revised -> archived | `11_OPERATIONS/Operational Procedures/` | Semantic versioning |
| Implementation Note | Technical implementation record | Engineering Office | Engineering owner | draft -> active -> superseded -> archived | `08_SYSTEMS/Implementation Notes/` or relevant systems area | Semantic versioning |
| Engineering Report | Generated engineering status report | Engineering Office | Report-only; no approval authority | generated -> reviewed -> archived | `08_SYSTEMS/Engineering Toolkit/Reports/` | Timestamped or dated |
| Operational Health Report | Health and risk summary | Institutional Observatory / Engineering | Report-only unless escalated | generated -> reviewed -> routed -> archived | `11_OPERATIONS/Operational Health/` | Dated reports |

---

## Open Questions

- [ ] Should generated reports be archived by date automatically?
- [ ] Should artifact schemas live beside this registry?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial artifact registry |

