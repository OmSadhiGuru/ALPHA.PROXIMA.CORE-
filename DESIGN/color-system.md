---
title: Color System
id: apx-design-color-system
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, color, semantics]
related: [knowledge-design-system.md, companion-color-map.md, callout-standard.md]
owner: Human Experience Lab (scope pending Founder ratification)
---

# Color System

## Purpose

Define functional (non-companion) color meaning across Alpha Proxima surfaces. Companion identity color is defined separately in `companion-color-map.md` — this file governs everything else: status, evidence, callouts, approval state.

## Scope

Applies to callout colors (detailed per-type in `callout-standard.md`), status badges, evidence-classification indicators, and any future UI chrome that is not a Companion's personal identity.

## Principle

Every color must have meaning (Design Principle 2). No color is chosen for decoration. A color's meaning must be identical everywhere it appears — a status green means the same thing in a knowledge object, a course module, and a dashboard.

## Functional Palette

| Function | Color | Meaning |
|---|---|---|
| Verified / Approved | Green | Content has passed required review (Ethics & Evidence Council where applicable) |
| Draft / Pending | Amber | Not yet reviewed or ratified |
| Contradiction / Conflict | Red | Two sources or claims disagree; requires resolution before canonization |
| Speculative | Violet-grey | Explicitly unproven; see Intellectual Honesty categories, Constitution Art. XI |
| Founder Decision | Gold | Marks Founder-authored or Founder-ratified content specifically |
| Archived / Superseded | Slate | Preserved but no longer active guidance |
| Public Content Candidate | Teal | Flagged as suitable for OSGMETAPHYSICS publication, pending Ethics & Evidence Council review |

## Relationship to Evidence Classification

Constitution Article XI's seven categories (Empirical, Clinical, Historical, Philosophical, Symbolic, Experiential, Speculative) are a classification, not a color set. This file assigns display treatment to that classification in `callout-standard.md`'s Evidence callout and `document-layout-standard.md`'s Evidence Classification field — it does not alter the classification itself.

## Constraint

Functional colors must remain distinguishable from all seven Companion colors (`companion-color-map.md`) so a reader is never uncertain whether a color marks a Companion's identity or a document's status. Verified/Approved (Green) is intentionally distinct from Emerald Green (GAIA) — implementers must use a visibly different shade, not the same hex value, and this must be validated before any theme ships.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial functional color system. |
