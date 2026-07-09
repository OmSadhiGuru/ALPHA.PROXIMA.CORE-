---
title: Document Layout Standard
id: apx-design-document-layout-standard
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, layout, document-grammar]
related: [knowledge-design-system.md, typography-hierarchy.md, callout-standard.md, research-note-standard.md]
owner: Human Experience Lab (scope pending Founder ratification)
---

# Document Layout Standard

## Purpose

Define the visual grammar every designed knowledge document uses, field by field, so structure is predictable regardless of subject matter (Design Principle 3, 6, 7).

## Fields, in Order

1. **Title** — H1, exactly one, matches frontmatter `title`.
2. **Subtitle** — one italic line beneath the title, optional, states the document's angle in under twelve words.
3. **Metadata block** — the YAML frontmatter (id, department, domain, type, status, version, created, updated, source, tags, related, owner) per this repository's existing schema. Not restated in the body.
4. **Summary** — two to four sentences, states what the document claims before any argument is made. Never buried.
5. **Key Principle** — a `[!principle]` callout (`callout-standard.md`) stating the one idea the document exists to convey.
6. **Evidence Classification** — an `[!evidence]` callout tagging the document's central claim(s) with its Constitution Art. XI category (Empirical, Clinical, Historical, Philosophical, Symbolic, Experiential, Speculative).
7. **Founder Synthesis** — where applicable, a `[!reflection]` or `[!founder-decision]` callout recording the Founder's own interpretation, distinct from raw evidence.
8. **Exercises** — practical, actionable steps for the reader, using `[!practice]` callouts.
9. **Warnings** — `[!warning]` or `[!medical-safety-note]` callouts as applicable, placed immediately adjacent to the content they qualify, never deferred to the end of the document.
10. **Research Notes** — links to or excerpts from supporting `research-note-standard.md` documents.
11. **Practical Applications** — `[!application]` callouts connecting the Key Principle to real use.
12. **Related Concepts** — a linked list, not prose, of related knowledge objects.
13. **Companion Ownership** — which Companion (if any) this document is attributed to or fronted by, per `companion-color-map.md`.
14. **Tags** — mirrors frontmatter `tags`, restated only if the document is long enough that a reader would not scroll back to the top to check.
15. **Version History** — required table, every knowledge document ends with one.
16. **Approval Status** — current review state: `draft`, `internal-reviewed`, `ethics-reviewed`, `public-approved`, or `archived`. Distinct from frontmatter `status`, which tracks lifecycle; Approval Status tracks review outcome specifically for content bound for OSGMETAPHYSICS.

## Rule

Not every field is required in every document type — a short internal note does not need Exercises or Practical Applications. Which fields are mandatory for which document type is defined per-template in `TEMPLATES/designed-*.md`, not here. This file defines what each field *means* when present; the templates define which are *required*.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial document layout standard, sixteen fields. |
