---
title: Naming Conventions
id: apx-governance-naming
department: LUMIAION
domain: governance
type: standard
status: active
version: 1.0.0
created: 2026-07-07
updated: 2026-07-11
source: git
tags: [naming, standards, ids]
related: [documentation-standard.md, versioning-policy.md, ../ORGANIZATION/office-map.md]
owner: Knowledge Atlas Office
---

# Naming Conventions

## Files

Use lowercase kebab-case for durable knowledge files.

Examples:

- `project-spec.template.md`
- `source-index.md`
- `architecture-decision-record.template.md`

Use uppercase folder names only for top-level institutional domains.

## IDs

IDs must be stable and unique.

Format:

```text
apx-<domain>-<short-name>
```

Examples:

- `apx-governance-naming`
- `apx-index-master`
- `apx-agent-vortex`

## Tags

Tags use lowercase kebab-case.

Examples:

- `agent-profile`
- `institutional-memory`
- `notion-sync`
- `source-index`

## Departments

**Superseded 2026-07-11 — see `../ORGANIZATION/office-map.md` for the current model.** The original five-name list below conflated Office and Companion identity, which the ratified Companion System (`../DESIGN/companion-color-map.md`) and the fourteen-office structure now separate. Companion names (ATHENA, SOHMA, JERANIUM, GAIA, ORION, VORTEX) remain valid values for `related_companion`-type fields, but are **no longer the allowed value set for the `department:` frontmatter field** on new documents.

Allowed `department:` values going forward: `LUMIAION` (orchestration-attributed documents, unchanged), plus the fourteen offices named in `../ORGANIZATION/office-map.md` (e.g. `Office of Health`, `Office of Knowledge`, `Founder's Office`). Existing documents using the original five-name list are not retroactively changed by this update — see the Phase II Sprint 2 Conflict Review for their disposition.

Original list (historical, superseded):

- LUMIAION
- VORTEX
- JERANIUM
- SOHMA
- ATHENA

