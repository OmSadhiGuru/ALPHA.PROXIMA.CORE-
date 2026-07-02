---
title: "Naming Policy"
aliases: ["Naming Policy", "File Naming Policy", "Document Naming Convention"]
tags: [policy, naming, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Institutional Policy
governed_by: "Book III - Knowledge Integrity"
---

# Naming Policy

---

## Purpose

This policy defines the naming conventions for all files, folders, and documents in the Alpha Proxima Vault and GitHub repository. Consistent naming enables navigation, prevents collision, and makes the knowledge graph legible without requiring memorization.

---

## Core Naming Principles

1. **Names are stable.** Once a document is committed to the Vault, its filename is not changed except in rare, formally justified circumstances. Renaming destroys links.
2. **Names describe content, not status.** A file named `LUMIAION Charter.md` — not `LUMIAION Charter (Current).md` or `LUMIAION Charter v2.md`. Status belongs in frontmatter.
3. **Names use Title Case.** Filenames use Title Case for document names. Folders use the numbered prefix convention (see below).
4. **No special characters except hyphens and en-dashes.** Avoid underscores in document names (they are used in folder names only for the prefix system). Never use slashes, colons, question marks, or ampersands in filenames.

---

## Folder Naming Convention

Top-level folders follow the numbered prefix convention:

```
NN_FOLDER_NAME/
```

Where `NN` is a two-digit number and `FOLDER_NAME` is SCREAMING_SNAKE_CASE.

### Canonical Top-Level Folders

| Folder | Purpose |
|--------|---------|
| `00_CONSTITUTION/` | Supreme governing documents |
| `01_VISION/` | Long-range direction and principles |
| `02_STRATEGY/` | Plans, roadmaps, priorities |
| `03_AI_COUNCIL/` | Governance bodies and registry |
| `04_DECISIONS/` | All ADRs |
| `05_PROPOSALS/` | Concept Notes awaiting deliberation |
| `06_GOVERNANCE/` | Governance documents and policies |
| `06_PROJECTS/` | Active project workspaces |
| `07_RESEARCH/` | Research programs |
| `08_SYSTEMS/` | Technical architecture and infrastructure |
| `09_OFFICES/` | Institutional office documents |
| `09_PEOPLE/` | Participant profiles and roles |
| `10_TEMPLATES/` | Reusable note formats |
| `99_ARCHIVE/` | Superseded or retired notes |

Subfolders within these folders use Title Case without numeric prefixes, unless a specific program numbering scheme applies (e.g., `RP-001/`, `EP-001/`).

---

## Document Naming Convention

### General Documents

```
[Document Title].md
```

Title Case. Spaces between words. No version number in filename.

**Examples:**
- `LUMIAION Charter.md`
- `Founding Principles of Alpha Proxima.md`
- `Alpha Proxima Operating Model v1.0.md` ← exception: when "v1.0" is part of the canonical title

**Note on "v1.0" in titles:** Avoid including version numbers in document titles. The exception is when the version is part of the canonical proper name of the document (e.g., "Operating Model v1.0" is the proper name, not a versioned filename).

### Coded Series Documents

Documents with formal codes follow the pattern:

```
[CODE]-[NNN] [Short Title].md
```

| Series | Pattern | Example |
|--------|---------|---------|
| ADR | `ADR-NNN [Title].md` | `ADR-001 Obsidian as Primary Vault.md` |
| CIR | `CIR-NNN [Title].md` | `CIR-001 Epoch III Constitutional Refactoring.md` |
| SO | `SO-NNN [Office] — [Domain].md` | `SO-001 Institutional Observatory — Continuous Monitoring Protocol.md` |
| FD | `FD-NNN [Mission Name].md` | `FD-001 Epoch III Constitutional Refactoring.md` |
| OBS | `OBS-NNN [Short Title].md` | `OBS-001 GPT-5 Release Capability Assessment.md` |
| RD | `RD-NNN [Short Title].md` | `RD-001 RP-002 Evidence Registry Page Citations.md` |

### Research Program Structure

```
07_RESEARCH/RP-NNN/
├── RP-NNN Master Index.md
├── ARCHIVE/
│   └── DOC-NNN [Author Year Title].md
├── Evidence Registry.md
├── Canonical Synthesis.md
└── [Other structured subfolders]
```

Research program files use the program code as prefix: `RP-001 Master Index.md`

Source Notes in ARCHIVE follow: `DOC-NNN [Author Last Name Year Short Title].md`  
Example: `DOC-001 Dehaene 2014 Consciousness and the Brain.md`

---

## Template Naming

Templates are named descriptively and stored in `10_TEMPLATES/`:

```
[Document Type] Template.md
```

Examples:
- `ADR Template.md`
- `Concept Note Template.md`
- `Research Program Template.md`

---

## Prohibited Naming Patterns

| Pattern | Why Prohibited |
|---------|---------------|
| `Draft - [Title].md` | Status belongs in frontmatter, not filename |
| `[Title] (OLD).md` | Superseded status belongs in frontmatter |
| `[Title] FINAL.md` | "Final" is not a meaningful status |
| `[Title]_v2.md` | Version belongs in frontmatter |
| `Copy of [Title].md` | Never commit copies; use links |
| `Untitled.md` | Every document must have a title |

---

## Renaming Protocol

When a document must be renamed (rare; justified only by correction of a genuine naming error):

1. Create the new file at the new name
2. Update all internal Obsidian links to point to the new name
3. Mark the old file with a redirect notice and `status: superseded`
4. Update the GitHub repository to reflect the rename
5. Document the rename in LUMIAION's activity log

**Do not delete the old file.** Redirect notices preserve navigation.

---

## Related Notes

- [[Book III - Knowledge Integrity]]
- [[Metadata Policy]]
- [[Versioning Policy]]
- [[Vault Structure Convention]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; core naming principles; folder convention; document convention; coded series patterns; research program structure; prohibited patterns; renaming protocol |
