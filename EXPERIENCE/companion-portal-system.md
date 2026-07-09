---
title: Companion Portal System
id: apx-experience-companion-portal-system
department: LUMIAION
domain: experience
type: experience-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-09
source: founder-request
tags: [experience, companions, portals]
related: [axiom-nexus-symbolic-interface.md, experience-modes.md, ../DESIGN/companion-color-map.md]
owner: Human Experience Lab (scope pending Founder ratification)
---

# Companion Portal System

## Purpose

Define how a Companion's portal functions as the access point to its fronted Office or Specialist, within Axiom Nexus's Symbolic Mode.

## Mechanism

1. Each of the seven identities in `../DESIGN/companion-color-map.md` occupies one channel position on the Axiom Nexus silhouette (`axiom-nexus-symbolic-interface.md`).
2. Engaging a Companion's portal opens that Companion's interface — content, tools, and conversation attributed to the Office(s) or Specialist it fronts (Constitution Art. VIII). Where a Companion fronts more than one Office (see Multi-Office Portals, below), the portal presents both under one entry point rather than splitting into separate portals.
3. A portal's visual treatment (color, position) is fixed by `../DESIGN/companion-color-map.md` and must not vary by content — the same portal always represents the same Companion, regardless of what is currently being shown inside it.
4. A Companion never asserts authority beyond what its fronted Office(s) or Specialist holds (Companion Charter, Principle 2 — constitutional package, **pending source, not filed in this repository**) — the portal is a presentation layer, not an independent decision-maker.

## Multi-Office Portals — Ratified 2026-07-09

One Companion may front multiple related Offices when the Founder explicitly approves it. **ORION** is the first ratified case: one portal, fronting both Enterprise and Community Growth. Within the ORION portal, content should be legibly divided by which Office it belongs to (e.g., a section or tab boundary), so a user can tell which institutional function they are engaging even though the entry point is shared. This division is a presentation detail for a future implementation sprint, not specified further here.

## Resolved Items

- **VORTEX**'s domain (creation, innovation, projects, automation, optimization, momentum) is ratified as its companion identity. VORTEX is an Executive Specialist under LUMIAION (not an Office-fronting Companion), so its portal opens directly to LUMIAION-coordinated Specialist content rather than to a Constitutional Office.
- **ORION**'s dual scope is resolved per Multi-Office Portals, above.

## Open Item

Whether Neural Mode and Professional Mode route through these same portals, or reach Offices/Companions/dashboards directly, is now specified in `experience-modes.md` (both may access directly) — this file's portal mechanism describes Symbolic Mode specifically.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial portal system definition; flagged two unresolved Companion-to-Office mappings inherited from the color map. |
| 1.0.1 | 2026-07-09 | Claude (Constitutional Secretary / Repository Architect) | Founder ratification applied: Multi-Office Portals section added (ORION); VORTEX resolved as Specialist-direct, not Office-fronting. |
