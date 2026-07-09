---
title: Designed Knowledge Object Template
id: apx-template-designed-knowledge-object
department: LUMIAION
domain: templates
type: template
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-09
source: founder-request
tags: [template, designed-knowledge-object, knowledge-design-system]
related: [../DESIGN/document-layout-standard.md, ../DESIGN/callout-standard.md, ../DESIGN/companion-color-map.md]
owner: "Human Experience Lab (scope pending Founder ratification)"
---

# Designed Knowledge Object Template

Use this template for knowledge objects styled per the Knowledge Design System (`../DESIGN/document-layout-standard.md`). Copy the block below as the new document's live frontmatter, then fill in every field — none of the values below are real metadata, they are placeholders.

```yaml
---
title:
id: apx-knowledge-
department:
domain:
type: designed-knowledge-object
status: draft
version: 0.1.0
created:
updated:
source:
category:        # Empirical | Clinical | Historical | Philosophical | Symbolic | Experiential | Speculative
companion:       # see ../DESIGN/companion-color-map.md, if any
approval_status: # draft | internal-reviewed | ethics-reviewed | public-approved | archived
tags: [knowledge-object]
related: []
owner:
---
```

# Title

*Subtitle — one line, under twelve words*

## Summary

Two to four sentences. What this document claims, before any argument is made.

> [!principle] Key Principle
> The one idea this document exists to convey.

> [!evidence] Evidence Classification
> Category: (from the field above). One sentence on the basis for this classification.

> [!reflection] Founder Synthesis
> Optional. The Founder's own interpretation, kept distinct from raw evidence.

## Exercises

> [!practice] Exercise title
> Actionable instruction.

## Warnings

> [!warning] (or [!medical-safety-note] if health-related)
> Caveat or limitation, placed here adjacent to the content it qualifies.

## Research Notes

- Link to supporting research-note-standard document(s), if any.

## Practical Applications

> [!application] Context
> How the Key Principle translates into practical use.

## Related Concepts

- Linked list of related knowledge objects — not prose.

## Companion Ownership

Which Companion, if any, this document is attributed to or fronted by.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | | | |

## Template Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial template, Sprint 1. |
| 1.0.1 | 2026-07-09 | Claude (Constitutional Secretary / Repository Architect) | Sprint 1.5 hardening: moved placeholder YAML out of live frontmatter into a body-level fenced block, per repository metadata standard (`../GOVERNANCE/documentation-standard.md`) and the pattern established in `knowledge-object.template.md`. Status normalized to `active` (the template itself is in active use; `draft` now describes only the fenced placeholder block's own status field). |
