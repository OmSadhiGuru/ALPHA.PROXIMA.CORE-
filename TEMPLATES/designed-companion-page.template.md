---
title: Designed Companion Page Template
id: apx-template-designed-companion-page
department: LUMIAION
domain: templates
type: template
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-09
source: founder-request
tags: [template, designed-companion-page, companions]
related: [../DESIGN/companion-color-map.md, ../EXPERIENCE/companion-portal-system.md]
owner: "Human Experience Lab (scope pending Founder ratification)"
---

# Designed Companion Page Template

Use this template to document a Companion (`../DESIGN/companion-color-map.md`). Copy the block below as the new page's live frontmatter, then fill in every field.

```yaml
---
title: " — Companion Page"
id: apx-companion-
department: LUMIAION
domain: experience
type: designed-companion-page
status: draft
version: 0.1.0
created:
updated:
source: founder-request
channel:  # Crown | Third Eye | Throat | Heart | Solar Plexus | Sacral | Root
color:    # per ../DESIGN/companion-color-map.md
fronts:   # Constitutional Office, or "Executive Specialist under LUMIAION"
tags: [companion-page]
related: [../DESIGN/companion-color-map.md, ../EXPERIENCE/companion-portal-system.md]
owner:
---
```

# Companion Name

*One-line description of this Companion's domain, per `../DESIGN/companion-color-map.md`*

## Identity

- **Channel:**
- **Color:**
- **Fronts:** — this Companion has no authority of its own beyond what its fronted Office or Specialist holds. One Companion may front more than one Office only where the Founder has explicitly ratified it (see `../DESIGN/companion-color-map.md`, Status Note, and `../EXPERIENCE/companion-portal-system.md`, Multi-Office Portals).

## Domain

Restate the domain from `../DESIGN/companion-color-map.md` in this Companion's voice.

## Voice and Tone

Not yet specified — personality, voice, and interface behavior are defined per-Companion. The constitutional package's Companion Charter, which would otherwise be the source for open items on a given Companion, is **not yet filed in this repository** (pending source) — do not link to it as if it exists here.

## Accessed Through

Portal mechanism — see `../EXPERIENCE/companion-portal-system.md`. Symbolic Mode routes through this Companion's portal; Neural Mode and Professional Mode may access the fronted Office directly (`../EXPERIENCE/experience-modes.md`).

## Content Boundaries

> [!warning]
> Any domain-specific limit — e.g., Office of Health's constitutional limit ("does not diagnose, prescribe, or substitute for licensed medical care"), restated here if this Companion fronts that Office.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | | | |

## Template Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial template, Sprint 1. |
| 1.0.1 | 2026-07-09 | Claude (Constitutional Secretary / Repository Architect) | Sprint 1.5 hardening: placeholder YAML moved from live frontmatter to body block; status normalized to `active`; removed a link to the constitutional package's Companion Charter, which is not filed in this repository, and marked it pending source instead; updated the Neural/Professional Mode reference to reflect the now-ratified routing rule. |
