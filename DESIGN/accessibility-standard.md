---
title: Accessibility Standard
id: apx-design-accessibility-standard
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, accessibility]
related: [knowledge-design-system.md, color-system.md, companion-color-map.md, pdf-ebook-style-guide.md]
owner: Human Experience Lab (scope pending Founder ratification)
---

# Accessibility Standard

## Purpose

Ensure the Knowledge Design System serves the Founder Covenant's principle that "knowledge belongs to humanity" without excluding readers by sensory ability, platform, or context — consistent with Design Principle 1 (clarity, not decoration) and Design Principle 7 (machine-readable).

## Requirements

1. **Color is never the only signal.** Every callout (`callout-standard.md`) and every functional color (`color-system.md`) carries a text label and, where used, an icon — never color alone. This also serves colorblind readers and print/greyscale contexts (`pdf-ebook-style-guide.md`).
2. **Contrast.** Any future themed implementation of `color-system.md` or `companion-color-map.md` must meet at minimum WCAG AA contrast for body text against its background. This standard does not set exact hex values (that is an implementation task) but binds any future implementation to this floor.
3. **Plain-language fallback.** Any symbolic or metaphor-heavy content (see `../EXPERIENCE/axiom-nexus-symbolic-interface.md`) must have a Neural Mode equivalent that conveys the same information without requiring familiarity with the symbolic framework — this is why Neural Mode is a constitutionally required alternative (Constitution Art. IX, §4), not optional polish.
4. **Alt text.** Any diagram, chakra map, or knowledge-graph visualization must ship with a text description sufficient for a screen-reader user to understand its content, not just its existence.
5. **Heading structure is semantic, not visual.** Per `typography-hierarchy.md`, heading levels are never skipped or chosen for visual size — this is required for screen readers and assistive navigation, not only for scan-ability.
6. **No information is locked behind a collapsed toggle by default**, per `toggle-structure-standard.md`'s exclusions — collapsing is a convenience, not a gate.

## Constraint

This standard does not yet cover: video/audio content accessibility (captioning, transcripts) for future course material, or specific assistive-technology testing. Both are flagged as gaps for the next design sprint, not addressed here.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial accessibility standard. Video/audio accessibility flagged as a gap. |
