---
title: Typography Hierarchy
id: apx-design-typography-hierarchy
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, typography, headings]
related: [knowledge-design-system.md, document-layout-standard.md]
owner: Human Experience Lab (scope pending Founder ratification)
---

# Typography Hierarchy

## Purpose

Give every heading level a fixed purpose (Design Principle 3), so structure is predictable across every document in the system and machine-parseable by anything that reads heading level as meaning (search, indexing, future RAG chunking).

## Scope

Applies to every Markdown document produced under the Knowledge Design System. Plain Markdown only — no platform-specific heading syntax.

## Heading Levels

| Level | Purpose | Example |
|---|---|---|
| `#` H1 | Document title only. Exactly one per document. | `# Knowledge Design System` |
| `##` H2 | Major section (Purpose, Scope, Core Content, Version History — Vault Structure Convention's required sections where applicable; this repository's own README pattern otherwise) | `## Core Content` |
| `###` H3 | Subsection within a major section | `### Heading Levels` |
| `####` H4 | Named sub-item within a subsection (e.g., one callout type, one companion) | `#### Principle Callout` |
| `#####` H5 | Reserved for deeply nested reference material (e.g., a single field definition inside a template). Use sparingly — five levels deep is close to the limit of what remains scannable. |
| `######` H6 | Not used. If content requires six heading levels, the document should be split. |

## Body Text Conventions

- **Bold** marks a term being defined for the first time, or a constitutional/binding statement.
- *Italic* marks a name, title, or a word used in a special/technical sense.
- `Inline code` marks file paths, IDs, field names, and literal values.
- Plain prose is the default. Avoid unnecessary emphasis — over-use of bold defeats its own purpose (Design Principle 1: clarity, not decoration).

## Scan Rule

A reader skimming only the H2s and H3s of any document must be able to reconstruct its argument without reading body text. This is the practical test for Design Principle 6 (every document must be easy to scan).

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial typography hierarchy. |
