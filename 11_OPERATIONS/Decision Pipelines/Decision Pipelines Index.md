---
title: "Decision Pipelines Index"
aliases: ["Decision Pipelines"]
tags: [operations, decisions, pipelines, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: operations-index
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Decision Routing Protocol]]", "[[Artifact Registry]]"]
related_documents: ["[[11_OPERATIONS]]", "[[Decision Routing Protocol]]", "[[Workflow Registry]]"]
related_research_programs: []
---

# Decision Pipelines Index

## Purpose

Describe how operational work moves toward decisions without Engineering making the decision.

## Scope

Covers pipeline visibility, artifact movement, and review readiness.

## Dependencies

- [[Decision Routing Protocol]]
- [[Artifact Registry]]

## Version

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | active |

## Author

[[CODEX]]

## Related Documents

- [[Workflow Registry]]
- [[Artifact Registry]]
- [[ADR Template]]
- [[Concept Note Template]]

## Related Research Programs

- N/A

## Implementation Notes

Pipelines make readiness visible. They do not approve progression.

## Future Improvements

- [ ] Add pipeline state fields.
- [ ] Add dashboard cards for blocked decisions.

## Core Content

| Pipeline | Intake Artifact | Decision Artifact | Review Authority | Engineering Role |
|----------|-----------------|-------------------|------------------|------------------|
| Concept to ADR | Concept Note | ADR | Relevant governance authority | Scaffold, validate, link |
| Future Proposal to Route | Future Proposal | Research Commission, Architecture Proposal, Implementation Note, ADR, or Archive Rationale | Relevant receiving office | Generate migration scaffolds |
| Research to Canon | Research Package | Canonical Synthesis | Research Council or approved authority | Structure, validate, export |
| Architecture to Implementation | Architecture Proposal or ADR | Implementation Note / Tool | Architecture and relevant authority | Build and test |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial decision pipelines index |

