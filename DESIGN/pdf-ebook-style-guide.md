---
title: PDF / eBook Style Guide
id: apx-design-pdf-ebook-style-guide
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, pdf, ebook, publishing]
related: [knowledge-design-system.md, document-layout-standard.md, color-system.md, callout-standard.md]
owner: Office of Publishing (scope pending Founder ratification)
---

# PDF / eBook Style Guide

## Purpose

Define how the Knowledge Design System translates into fixed, printable output — PDFs, eBooks, and course booklets — for OSGMETAPHYSICS's free, affordable, and paid tiers (Constitution Art. V; Founder Covenant §1).

## Translation Rules

| Markdown/Obsidian Element | PDF/eBook Treatment |
|---|---|
| Callouts (`callout-standard.md`) | Rendered as bordered boxes using the callout's assigned color at reduced saturation (print-safe), with the icon suggestion rendered as a small glyph, not emoji. |
| Companion color (`companion-color-map.md`) | Used for chapter accents and Companion-attributed sections only — never as full-page background, to preserve print legibility and ink cost. |
| Toggles (`toggle-structure-standard.md`) | Do not exist in fixed output. Collapsed content must be expanded; nothing may be hidden in a PDF. |
| Wiki-links | Rendered as plain text with a footnote or endnote reference, never a raw `[[bracket]]`. |
| Frontmatter | Not printed. A human-readable title/author/version block replaces it on the document's first page. |
| Version History table | Retained, placed at the end matter, not the front. |

## Accessibility in Print

Follows `accessibility-standard.md` wherever print permits — sufficient color contrast, no meaning conveyed by color alone (every callout also carries a text label and icon), and a plain-text fallback available for every diagram.

## Free / Affordable / Paid Tier Consistency

All three access tiers (Constitution Art. II) use the same design system. A free PDF and a paid course booklet differ in depth and packaging, never in visual grammar — a reader moving from free to paid content should recognize the system immediately.

## Constraint

This guide does not define a specific typeface, page size, or binding — those are production decisions for the Office of Publishing once scoped, made *within* this system, not instead of it.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial PDF/eBook style guide. |
