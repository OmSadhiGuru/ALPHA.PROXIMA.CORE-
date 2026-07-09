---
title: Obsidian Style Guide
id: apx-design-obsidian-style-guide
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, obsidian]
related: [knowledge-design-system.md, callout-standard.md, toggle-structure-standard.md]
owner: Office of Intelligence Infrastructure (scope pending Founder ratification)
---

# Obsidian Style Guide

## Purpose

Isolate every Obsidian-specific formatting convention in one place, so GitHub markdown readability is never silently compromised elsewhere in the system (Design Principle 8, cross-platform constraint in `knowledge-design-system.md`).

## Obsidian-Specific Elements in Use

| Element | Syntax | GitHub Fallback |
|---|---|---|
| Callouts | `> [!type] Title` | Renders as a plain blockquote — label is still readable as text. |
| Wiki-links | `[[Document Title]]` | Renders as literal bracketed text on GitHub — still human-readable, not broken, but not clickable. |
| Aliases | `[[Document Title\|Display Text]]` | Same as above. |
| Collapsible headings | Native, no syntax | No effect on GitHub — heading simply displays normally, which is the desired fallback. |
| Tags | `#tag` inline, or frontmatter `tags:` | Frontmatter form preferred for machine-readability; inline `#tag` renders as plain text on GitHub. |
| Graph View colors | `.obsidian/graph.json`, see the Vault's `Graph View Color System` for precedent | Not applicable to this repository directly; noted for future reconciliation if this repository adopts its own graph view. |

## Rule

No document may rely on an Obsidian-only feature to convey information that would be lost on GitHub. Every use above degrades to plain, still-meaningful text. If a future Obsidian feature cannot degrade this way, it must not be adopted without an explicit exception recorded here.

## Companion / Callout Color Rendering

Obsidian callout colors are set via CSS snippet, not per-document. A single shared snippet implementing `color-system.md` and `companion-color-map.md` should be maintained once (not yet built — see Sprint output, Recommended Next Sprint) rather than styled inline per document.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial Obsidian style guide, isolating platform-specific formatting. |
