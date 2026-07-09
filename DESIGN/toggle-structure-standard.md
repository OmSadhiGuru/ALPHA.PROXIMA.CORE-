---
title: Toggle Structure Standard
id: apx-design-toggle-structure-standard
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, obsidian, toggles, collapsible]
related: [knowledge-design-system.md, obsidian-style-guide.md, document-layout-standard.md]
owner: Human Experience Lab (scope pending Founder ratification)
---

# Toggle Structure Standard

## Purpose

Define when and how collapsible/toggle sections are used, so long documents remain scannable without hiding information a GitHub reader would otherwise see in full (Design Principle 6 and 8).

## Format Rule

Obsidian's native collapsible heading behavior (any heading can be collapsed in the Obsidian UI without special syntax) is the default toggle mechanism — it requires no markup and therefore does not break GitHub rendering, satisfying the cross-platform constraint. Do not use HTML `<details>`/`<summary>` tags unless a specific need (e.g., a long raw data table) is identified, since they render inconsistently across GitHub, Obsidian, and PDF export.

## When to Use a Toggle-Friendly Structure

- Long reference tables (e.g., a full companion list, a full callout list) that a reader scans by heading, not by reading top to bottom.
- Supplementary detail that supports but is not required to follow the main argument (e.g., raw data inside a study note — see `research-note-standard.md`).
- Version History and Secretary's/Author's Notes sections, which are reference material, not argument.

## When Not to Use a Toggle-Friendly Structure

- Purpose, Scope, and Core Content sections — these must always be visible by default, since collapsing them defeats the scan rule in `typography-hierarchy.md`.
- Any Ethics Review Required or Medical Safety Note callout (`callout-standard.md`) — safety-relevant content must never be hidden behind a fold.
- Constitutional or governance text — nothing binding should be collapsible by default.

## Nesting Limit

A toggle-friendly heading should not itself contain another toggle-friendly heading more than one level deep. If a document needs deeper nesting than that, it should be split into linked documents instead (consistent with `typography-hierarchy.md`'s H6 rule).

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial toggle structure standard. |
