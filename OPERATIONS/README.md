---
title: Operations Folder
id: apx-operations-readme
department: LUMIAION
domain: operations
type: readme
status: active
version: 1.0.0
created: 2026-07-09
updated: 2026-07-09
source: migration
tags: [operations, readme]
related: [CPOS/README.md, ../README.md, ../GOVERNANCE/constitution.md]
owner: "Operations Office (legacy-reference — not a ratified Constitutional Office; see repository hardening notes)"
---

# OPERATIONS

## Purpose

Hold the operational layer of ALPHAPROXIMA — the day-to-day production, queue, and briefing system, as distinct from `GOVERNANCE/` (doctrine) and `KNOWLEDGE/` (durable content).

## Scope

Currently contains one subsystem: `CPOS/` (see `CPOS/README.md`). This folder was created during Sprint 1.5 Repository Hardening to give the migrated `OSG Operating Office/` content a proper home inside the canonical repository.

## Relationship to the Constitutional Package

A separate constitutional package (Founder Covenant, Constitution v1.0, Organizational Charter, and related charters) was drafted and Founder-reviewed but **is not yet filed as a file in this repository** — it exists outside `ALPHAPROXIMA/` pending a filing decision. Where this folder's content would naturally cite that package (e.g., the Founder Command Center concept in Constitution Art. XIII), it is marked **pending source** rather than linked, per repository hardening instruction. `GOVERNANCE/constitution.md`, which does exist in this repository, is linked above where relevant.

## External Systems Referenced by Operations

The following are external to this repository. Operations files may refer to them, but none is stored here:

| System | Status | Note |
|---|---|---|
| **LOOM** | External — lives in a separate Vault repository | Also described there as a Founder Command Center / Daily Executive Brief mechanism. Its relationship to `CPOS/` (this folder) is unresolved — see `CPOS/README.md`, Open Items. |
| **Google Drive** | External — raw source archive | Governed by `../AUTOMATIONS/drive-sync-spec.md`. Not touched by anything in this folder. |
| **Notion** | External — not yet integrated | Referenced as a future workspace surface in `../README.md`; no live connection exists. |
| **OSGMETAPHYSICS** | External — the public-facing layer | Per the (unfiled) Constitution Art. V, OSGMETAPHYSICS is the public bridge this institution expresses through; pending source for the formal citation. |

## Related Folders

- `CPOS/` — the current production/queue/dashboard system.
- `../GOVERNANCE/` — doctrine this layer operates under.
- `../DESIGN/`, `../EXPERIENCE/` — the Knowledge Design System, which CPOS content should eventually conform to (not yet applied — see Recommended Next Sprint in the Sprint 1.5 output).

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-09 | Claude (Constitutional Secretary / Repository Architect) | Initial OPERATIONS README, Sprint 1.5 Repository Hardening. |
