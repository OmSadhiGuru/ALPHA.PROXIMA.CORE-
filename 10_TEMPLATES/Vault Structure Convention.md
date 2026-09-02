---
title: "Vault Structure Convention"
aliases: ["Vault Convention", "Folder Structure", "Note Standards", "VSC"]
tags: [convention, vault, structure, obsidian, standards, template]
created: 2026-07-01
updated: 2026-09-02
status: active
version: "1.2.0"
authors: ["Alpha Council", "LUMIAION (CF-01)"]
---

# Vault Structure Convention

## Purpose

This document defines the canonical folder structure, naming conventions, metadata standards, and note architecture for the [[Alpha Proxima Core]] Obsidian Vault. All notes created in this vault — by humans or [[LUMIAION]] — must conform to these conventions.

Consistency here is what makes the knowledge graph navigable, the git history legible, and the institutional memory durable.

---

## Context

As the vault grows, ad-hoc structure creates drift — notes that can't be found, links that break, metadata that becomes meaningless. This convention was established to prevent that. It was ratified by the [[Alpha Council]] as a Class II institutional decision.

This document is itself a standard, not a template. To create a new note *use* the appropriate template from `10_TEMPLATES/`. To understand *where* to put it and *how* to name it, read this document.

---

## Core Content

### Folder Structure

```
ALPHA.PROXIMA.CORE-/
│
├── 00_CONSTITUTION/       ← Supreme governing documents only
│                            Never more than 5 files. Changes require Class I ADR.
│
├── 01_VISION/             ← Long-range direction, mission, values
│                            Single authoritative vision document + supporting notes
│
├── 02_STRATEGY/           ← Plans, roadmaps, OKRs, priorities
│                            Time-bounded; archive when superseded
│
├── 03_AI_COUNCIL/         ← Governance bodies, the Alpha Council, LUMIAION registry
│                            Institutional notes, not project notes
│
├── 04_DECISIONS/          ← All ADRs (Architecture Decision Records)
│                            Named: ADR-XXXX - Title.md
│                            Never deleted; superseded ADRs marked in frontmatter
│
├── 05_PROPOSALS/          ← Concept Notes awaiting or undergoing deliberation
│                            Named: CN-XXXX - Title.md
│                            Moved to 99_ARCHIVE after outcome is recorded
│
├── 06_GOVERNANCE/         ← Policies, frameworks, registers, impact reports
│                            Institutional governance instruments
│
├── 07_RESEARCH/           ← Research programs (RP-###) + explorations
│                            Looser structure; tag heavily
│
├── 08_SYSTEMS/            ← Technical architecture and infrastructure
│                            System maps, API references, infrastructure decisions
│
├── 09_OFFICES/            ← Institutional office charters
│                            One subfolder per office
│
├── 10_TEMPLATES/          ← Reusable note formats
│                            Never modify a template without an ADR
│
├── 11_PROJECTS/           ← Active project workspaces
│                            One subfolder per project: 11_PROJECTS/Project Name/
│
├── 12_PEOPLE/             ← Participant profiles and roles
│                            One note per person/entity
│
├── 13_OPERATIONS/         ← Operational nervous system of the Foundation
│                            Founder OS, workflows, registries, reviews, and metrics
│
└── 99_ARCHIVE/            ← Superseded, retired, or closed notes
                             Never delete; archive instead
```

**Number reservation table (canonical — resolves CAR-F07 folder-number collisions):**

| # | Folder | # | Folder |
|---|--------|---|--------|
| 00 | CONSTITUTION | 07 | RESEARCH |
| 01 | VISION | 08 | SYSTEMS |
| 02 | STRATEGY | 09 | OFFICES |
| 03 | AI_COUNCIL | 10 | TEMPLATES |
| 04 | DECISIONS | 11 | PROJECTS |
| 05 | PROPOSALS | 12 | PEOPLE |
| 06 | GOVERNANCE | 13 | OPERATIONS |
|    |            | 99 | ARCHIVE |

*Each number maps to exactly one folder. The Epoch III–IV additions `06_GOVERNANCE` and `09_OFFICES` kept their numbers (they are populated); the original `06_PROJECTS` → `11_PROJECTS` and `09_PEOPLE` → `12_PEOPLE` were renumbered (Epoch V) to remove the collisions.*

**Sanctioned structural exceptions (resolves CAR-F08):**

- **Root-level cross-cutting notes** — `[[Alpha Proxima Core]]` (MOC), `[[LUMIAION]]`, `[[Alpha Council]]`, `README.md`.
- **`docs/`** — engineering-facing documentation served outside the numbered knowledge structure (e.g. `docs/constitution/`, `docs/setup/`). A software convention, deliberately sanctioned.
- **`PROJECT_GENOME/`** — top-level project directory for the Living Genome Framework.
- **`OSG_BUSINESS/`** — the OSG (public brand) business/academy workstream.

These exceptions are governed by, and subordinate to, the numbered structure and the [[Constitutional Hierarchy Statement]]; they are not ungoverned.

---

### File Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| ADR | `ADR-XXXX - Short Title.md` | `ADR-0001 - Adopt Obsidian as Primary Vault.md` |
| Concept Note | `CN-XXXX - Short Title.md` | `CN-0001 - Expand LUMIAION Scope.md` |
| Project note | `Project Name - Note Title.md` | `LUMIAION - Architecture Overview.md` |
| General note | `Descriptive Title.md` | `Knowledge Graph Principles.md` |
| Person/entity | `Full Name.md` | `Frederick Belizaire.md` |

**Rules:**
- No underscores in note titles (use spaces; Obsidian handles them)
- No dates in filenames (use frontmatter `created` field)
- Title case for all note titles
- ADR and CN numbers are zero-padded to 4 digits

---

### Required Frontmatter

Every note must include this frontmatter block:

```yaml
---
title: "Note Title"
aliases: ["Alternative Name", "Abbreviation"]
tags: [tag1, tag2, tag3]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft | active | archived | superseded
version: "X.Y.Z"
authors: ["[[Name]]"]
---
```

**Tag conventions:**
- Use kebab-case for multi-word tags: `alpha-proxima`, `decision-record`
- Always include the primary domain tag: `governance`, `research`, `systems`, etc.
- Always tag with the relevant institution if applicable: `alpha-council`, `lumiaion`

---

### Required Note Sections

Every note must contain these six sections in this order:

1. **Purpose** — Why does this note exist? What question does it answer?
2. **Context** — What background does a reader need? What created the need for this note?
3. **Core Content** — The substance of the note
4. **Related Notes** — Wikilinks to connected notes
5. **Open Questions** — Unresolved issues, tracked as checkboxes
6. **Version History** — A table of changes

---

### Wikilink Standards

- Always use `[[Note Title]]` — the exact title as it appears in the note's `title` frontmatter
- Use aliases when the display text should differ: `[[ADR Template|ADR]]`
- Never use bare URLs inside notes where a wikilink would serve — external references go in the Context or Related Notes section
- Every note should link to at least one other note — isolated notes are a smell

---

### Status Definitions

| Status | Meaning |
|--------|---------|
| `draft` | Being written; not yet ready for use or deliberation |
| `active` | Current and authoritative |
| `archived` | Superseded but preserved; do not update |
| `superseded` | Replaced by a newer version; frontmatter should link to successor |

---

### Version Numbering

Use semantic versioning:
- **Major (X)** — structural or substantive change to the content
- **Minor (Y)** — additions or expansions that don't change existing content
- **Patch (Z)** — corrections, typos, clarifications

Templates start at `1.0.0`. Living documents (like this one) increment as updated.

---

### What Not to Do

- Do not create notes without frontmatter
- Do not leave notes without at least one wikilink
- Do not delete notes — archive them in `99_ARCHIVE/` with a note explaining why
- Do not use folder structure to replace tagging — use both
- Do not create a note for something that should be a section in an existing note

---

## Related Notes

- [[Alpha Proxima Core]]
- [[Alpha Council]]
- [[LUMIAION]]
- [[Book I - The Constitution]]
- [[Institutional Registry]]
- [[ADR Template]]
- [[Concept Note Template]]

---

## Open Questions

- [ ] Should there be a `00_INDEX/` folder for MOC and navigation notes, separate from root-level notes?
- [ ] What is the maximum recommended depth for subfolders within a project folder (`11_PROJECTS/`)?
- [ ] Should templates themselves be versioned in git with their own changelog, separate from the vault convention?
- [ ] Do we need a separate convention document for how [[LUMIAION]] should name and structure its own operational logs?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-01 | [[Alpha Council]] | Initial convention established |
| 1.1.0 | 2026-09-02 | LUMIAION (CF-01) | Epoch V Tier 2: number reservation table added (resolves CAR-F07 — `06_PROJECTS`→`11_PROJECTS`, `09_PEOPLE`→`12_PEOPLE`; GOVERNANCE/OFFICES keep their numbers); sanctioned `docs/`, `PROJECT_GENOME/`, `OSG_BUSINESS/` as governed structural exceptions (resolves CAR-F08) |
| 1.2.0 | 2026-09-02 | Founder / CODEX | Founder-ratified reconciliation: reserve `13_OPERATIONS`; preserve `11_PROJECTS` and `12_PEOPLE`; remove the post-Epoch-V `11` collision introduced by the Operations layer |
