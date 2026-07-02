---
title: "03 - Folder Naming Convention"
aliases: ["Folder Standard", "Vault Hierarchy Standard"]
tags: [systems, engineering, standards, folders, vault, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-03"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Vault Structure Convention]]"]
related_documents: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_research_programs: []
---

# 03 - Folder Naming Convention

## Purpose

Define a stable vault hierarchy that supports long-term navigation, governance, research, engineering, education, automation, and archival memory without depending on temporary technologies.

---

## Scope

Applies to top-level vault folders and all major subfolders created for durable institutional work.

---

## Rules

- Preserve the existing numbered top-level hierarchy unless changed through governance.
- Use two-digit numeric prefixes for top-level domains.
- Use title case for human-facing folder names.
- Use stable institutional categories instead of vendor or tool names.
- Use `Assets/` for local media attached to a document family.
- Use `Automation/` for executable or workflow-supporting utilities.
- Use `Archive/` or the canonical `99_ARCHIVE/` for retired material.
- Do not bury active canonical documents more than three levels deep without a navigation index.
- Every new durable folder should have either an index note or an obvious parent document.

### Current Canonical Top-Level Folders

| Folder | Purpose |
|--------|---------|
| `00_CONSTITUTION/` | Supreme governing documents |
| `01_VISION/` | Long-range vision and values |
| `02_STRATEGY/` | Plans, roadmaps, priorities |
| `03_AI_COUNCIL/` | AI Council and department records |
| `04_DECISIONS/` | ADRs and durable decisions |
| `05_PROPOSALS/` | Concept notes and proposals |
| `06_PROJECTS/` | Active project workspaces |
| `07_RESEARCH/` | Research programs and evidence work |
| `08_SYSTEMS/` | Technical systems, protocols, standards, automation |
| `09_PEOPLE/` | People, roles, and entities |
| `10_TEMPLATES/` | Reusable templates |
| `99_ARCHIVE/` | Superseded or retired material |

### Recommended Durable Subfolders

| Parent | Subfolder | Use |
|--------|-----------|-----|
| `08_SYSTEMS/` | `Engineering Standards/` | Engineering handbook and standards |
| `08_SYSTEMS/` | `Automation/` | Local scripts and workflow utilities |
| `08_SYSTEMS/` | `Protocols/` | Operational protocols |
| `08_SYSTEMS/` | `Implementation Notes/` | Technical implementation records |
| `07_RESEARCH/` | `RP-XXX/` | Research program workspace |
| Any document family | `Assets/` | Images, diagrams, attachments |

---

## Examples

Good:

```text
08_SYSTEMS/Engineering Standards/
08_SYSTEMS/Automation/
07_RESEARCH/RP-001/
06_PROJECTS/Vault Automation/
```

Avoid:

```text
Claude Scripts/
New Stuff/
Temp Docs/
Random Research/
```

---

## Best Practices

- Create folders when they reduce search and maintenance burden.
- Keep standards, protocols, and implementation notes separate.
- Use local indexes for folders that contain more than ten durable notes.
- Archive instead of deleting.
- Keep temporary work outside canonical folders until it is ready to become a durable artifact.

---

## Common Mistakes

- Naming folders after current tools instead of stable functions.
- Creating duplicate homes for the same artifact type.
- Using folder depth as a substitute for frontmatter and links.
- Keeping obsolete work in active folders without status metadata.
- Creating isolated folders without backlinks.

---

## Future Evolution

This standard may recommend new top-level folders for education, public knowledge products, or engineering if the vault outgrows the current hierarchy. Such changes should be proposed through governance because they affect institutional architecture.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial folder naming convention |

---

## Related Standards

- [[01 - Markdown Style Guide]]
- [[02 - YAML Frontmatter Standard]]
- [[04 - File Naming Convention]]
- [[09 - Git Standard]]
- [[10 - Template Standard]]

