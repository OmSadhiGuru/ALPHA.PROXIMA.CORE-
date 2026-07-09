---
title: Knowledge Design System
id: apx-design-knowledge-design-system
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, knowledge-design, readability, alphaproxima]
related: [color-system.md, typography-hierarchy.md, callout-standard.md, toggle-structure-standard.md, companion-color-map.md, document-layout-standard.md, research-note-standard.md, pdf-ebook-style-guide.md, obsidian-style-guide.md, accessibility-standard.md]
owner: Human Experience Lab (scope pending Founder ratification — see Constitutional package)
---

# Knowledge Design System

## Purpose

Define how Alpha Proxima, Axiom Nexus, and OSGMETAPHYSICS knowledge should look, feel, be structured, colored, categorized, and read — across Obsidian, GitHub markdown, Notion, PDFs/eBooks, courses, public education, internal research, AI ingestion, and future UI/UX. This document is the index and statement of intent; each concern below has its own standard file.

## Scope

Covers every knowledge object, folder, node, study, protocol, companion page, and future product surface built from ALPHAPROXIMA content. Does not cover raw source material (Article X, Knowledge Principle) — raw sources are never redesigned, only the objects derived from them.

## Design Principles

1. The design must increase clarity, not decoration.
2. Every color must have meaning.
3. Every heading level must have a purpose.
4. Every callout must communicate function.
5. Every companion must have a consistent visual identity.
6. Every document must be easy to scan.
7. Every document must remain machine-readable.
8. Beauty must never destroy searchability.
9. Markdown must remain clean.
10. The system must support future CSS/theme implementation.

These ten principles are binding on every file in `DESIGN/`, `EXPERIENCE/`, and every `designed-*` template. A proposed design choice that cannot be justified against at least one principle should not be adopted.

## System Map

| Concern | File |
|---|---|
| Semantic/functional color (non-companion) | `color-system.md` |
| Heading levels and body text | `typography-hierarchy.md` |
| Reusable callout types | `callout-standard.md` |
| Collapsible/toggle sections (Obsidian) | `toggle-structure-standard.md` |
| Companion chakra/color identity | `companion-color-map.md` |
| Document visual grammar (title through approval status) | `document-layout-standard.md` |
| Research/study note structure | `research-note-standard.md` |
| PDF/eBook translation of this system | `pdf-ebook-style-guide.md` |
| Obsidian-specific formatting, isolated from GitHub core | `obsidian-style-guide.md` |
| Accessibility requirements | `accessibility-standard.md` |
| Symbolic interface (Axiom Nexus) | `../EXPERIENCE/axiom-nexus-symbolic-interface.md` |
| Neural interface (Alpha Proxima) | `../EXPERIENCE/alpha-proxima-neural-interface.md` |
| Experience mode definitions | `../EXPERIENCE/experience-modes.md` |
| Companion portal access | `../EXPERIENCE/companion-portal-system.md` |

## Cross-Platform Constraint

Every standard in this system must degrade gracefully: a document styled for Obsidian must still be fully readable as plain GitHub markdown, and a document readable on GitHub must still convert cleanly to PDF/eBook. Where a platform-specific feature (e.g., Obsidian callouts, toggles) is used, `obsidian-style-guide.md` isolates it so its absence elsewhere does not break comprehension — this operationalizes Design Principle 8.

## Relationship to Governance

This system implements Constitution Article IX (Experience Layer) and the Design Principles above; it does not alter Constitutional Offices, Companions' institutional standing, or any ratified doctrine. Visual identity may change without constitutional amendment (Constitution Art. VIII, §4); the Offices and Specialists a Companion fronts may not.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial Knowledge Design System index. |
