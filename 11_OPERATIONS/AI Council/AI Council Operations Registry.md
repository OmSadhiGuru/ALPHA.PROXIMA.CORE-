---
title: "AI Council Operations Registry"
aliases: ["Reasoning Office Registry", "AI Operations Registry"]
tags: [operations, ai-council, reasoning-engines, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: operations-registry
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[AI Council Registry]]", "[[Engine Registry]]", "[[Office Registry]]"]
related_documents: ["[[11_OPERATIONS]]", "[[AI Council Registry]]", "[[Engine Registry]]", "[[CODEX]]"]
related_research_programs: []
---

# AI Council Operations Registry

## Purpose

Document current reasoning offices and preferred engines so new reasoning engines can be added without restructuring the Foundation.

---

## Scope

This registry is operational. It does not replace charters, engine registry records, or governance authority.

---

## Dependencies

- [[AI Council Registry]]
- [[Engine Registry]]
- [[Office Registry]]

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

- [[AI Council Registry]]
- [[Engine Registry]]
- [[LUMIAION Charter]]
- [[CODEX]]

---

## Related Research Programs

- N/A

---

## Implementation Notes

Adding a future office should require adding a row and linking its charter or profile, not restructuring the operations layer.

---

## Future Improvements

- [ ] Add invocation patterns for each reasoning office.
- [ ] Add context loading checklists.
- [ ] Add engine handoff templates.

---

## Core Content

| Reasoning Office | Preferred Engine | Institutional Role | Inputs | Outputs | Operational Boundary | Engineering Support |
|------------------|------------------|--------------------|--------|---------|----------------------|--------------------|
| LUMIAION | LUMIAION | Institutional Intelligence and orchestration | Founder intent, office reports, vault context | Routing, synthesis, continuity, memory writeback | Orchestrates; does not replace governance | Context loaders, routing scaffolds, review packets |
| Institutional Architecture | Claude | Institutional Architecture | Architecture gaps, proposals, protocols, review findings | Architecture specs, architecture proposals, protocol updates | Proposes architecture; governance approves where required | Diffing, diagrams, spec templates |
| Engineering Office | Codex | Implementation | Approved architecture, engineering tasks, validation reports | Tools, scripts, templates, reports, automation | Builds; does not decide | Primary implementation environment |
| Research Intelligence Office | Perplexity Compute | Research Intelligence | Research commissions, source questions, evidence needs | Research packages, source reports, evidence summaries | Produces evidence; does not canonize | Research package generators, export tools |
| Institutional Observatory | Comet | Observation and monitoring | Metrics, vault signals, external signals, drift patterns | Observatory reports, alerts, health summaries | Observes; does not decide | Dashboards, metrics pipelines |
| Future Office Slots | Future engines | Future cognitive functions | TBD | TBD | Must be defined before engine adoption | Profile templates, registry updates |

---

## Open Questions

- [ ] Should each reasoning office have a formal operating checklist?
- [ ] Should future engines be registered before first use or after trial use?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial AI Council operations registry |

