---
title: "Metrics Registry"
aliases: ["Operations Metrics", "Institutional Metrics"]
tags: [operations, metrics, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: operations-registry
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Artifact Registry]]", "[[Operational Health Index]]"]
related_documents: ["[[11_OPERATIONS]]", "[[Dashboards Index]]", "[[Operational Health Index]]"]
related_research_programs: []
---

# Metrics Registry

## Purpose

Define operational metrics that help offices understand health, debt, growth, and continuity.

## Scope

Metrics are signals. They do not decide priorities by themselves.

## Dependencies

- [[Artifact Registry]]
- [[Operational Health Index]]
- [[Alpha Proxima Engineering Toolkit]]

## Version

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Status** | active |

## Author

[[CODEX]]

## Related Documents

- [[Dashboards Index]]
- [[Operational Health Index]]
- [[Review Cycles Registry]]

## Related Research Programs

- N/A

## Implementation Notes

Metrics should be computable from local files wherever possible.

## Future Improvements

- [ ] Add metric calculation scripts.
- [ ] Add metric history snapshots.

## Core Content

| Metric | Definition | Source | Review Cycle |
|--------|------------|--------|--------------|
| Vault notes | Count of Markdown notes | Vault scan | Weekly |
| Broken links | Wiki links without target | Vault Validator | Daily / weekly |
| Missing metadata | Required fields absent | YAML Validator | Weekly |
| Orphan notes | Notes without backlinks | Link scanner | Weekly |
| Research programs | Count and status of RP folders | `07_RESEARCH/` | Monthly |
| Engineering debt | Open validator warnings and tool TODOs | Toolkit reports | Weekly |
| Research debt | Missing research artifacts, open research questions | Research indexes | Monthly |
| Automation queue size | Count of automation candidates | [[Automation Queue Index]] | Weekly |
| Review queue size | Count of items awaiting review | [[Review Queue Index]] | Weekly |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial metrics registry |

