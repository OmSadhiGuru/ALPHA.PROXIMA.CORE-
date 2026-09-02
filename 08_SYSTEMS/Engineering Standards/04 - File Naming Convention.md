---
title: "04 - File Naming Convention"
aliases: ["Filename Standard", "Document Naming Standard"]
tags: [systems, engineering, standards, filenames, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-04"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Vault Structure Convention]]"]
related_documents: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_research_programs: []
---

# 04 - File Naming Convention

## Purpose

Define file names that are readable to humans, searchable in Obsidian, stable in Git, and predictable for future automation.

---

## Scope

Applies to Markdown notes, scripts, templates, protocols, automation files, research artifacts, and engineering documentation.

---

## Rules

- Use human-readable names for Markdown documents.
- Use title case for Markdown note names.
- Use spaces in Obsidian note names; do not use underscores for human-facing notes.
- Use lowercase snake_case for executable code files.
- Do not put dates in filenames unless the artifact is inherently date-based.
- Use zero-padded numeric identifiers for sequenced institutional artifacts.
- Use version suffixes only when multiple versions must coexist as files.
- Keep names stable after linking; rename only when the old name is misleading.

### Naming Patterns

| Artifact | Pattern | Example |
|----------|---------|---------|
| ADR | `ADR-XXXX - Short Title.md` | `ADR-0001 - The Founding Decision.md` |
| Concept Note | `CN-XXXX - Short Title.md` | `CN-0001 - Constitutional Alignment Gap Report.md` |
| Engineering Standard | `NN - Standard Name.md` | `05 - Python Development Standard.md` |
| Protocol | `Protocol Name.md` | `Knowledge Routing Protocol.md` |
| Template | `Artifact Type Template.md` | `Implementation Note Template.md` |
| Research Program Index | `RP-XXX Master Index.md` | `RP-001 Master Index.md` |
| Research Note | `RP-XXX Short Title.md` or approved program pattern | `RP-001 Source Registry.md` |
| Python Script | `lowercase_snake_case.py` | `vault_note.py` |
| CLI Package | `lowercase-kebab-command` | `vault-note` |
| Asset | `descriptive-kebab-name.ext` | `system-context-diagram.png` |

---

## Examples

Good:

```text
08_SYSTEMS/Engineering Standards/05 - Python Development Standard.md
10_TEMPLATES/Implementation Note Template.md
08_SYSTEMS/Automation/vault_note.py
07_RESEARCH/RP-001/RP-001 Master Index.md
```

Avoid:

```text
pythonStandardFinal.md
notes_new.md
2026-07-02-random.md
ClaudeAutomationV2.md
```

---

## Best Practices

- Name files for the reader who finds them in search results.
- Put the most important identifier first for sequenced artifacts.
- Keep filenames shorter than the document title when the title is long.
- Use frontmatter for dates, authors, status, and version.
- Match the H1 to the filename unless a template requires placeholders.

---

## Common Mistakes

- Adding `final`, `latest`, or `new` to filenames.
- Mixing code naming conventions with note naming conventions.
- Renaming widely linked notes without updating links.
- Encoding governance status in the filename instead of frontmatter.
- Creating names that only make sense to the original author.

---

## Future Evolution

Future versions may define naming rules for datasets, embeddings, generated exports, release artifacts, and packaged workflows. Those rules should remain compatible with local filesystems and GitHub.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial file naming convention |

---

## Related Standards

- [[01 - Markdown Style Guide]]
- [[02 - YAML Frontmatter Standard]]
- [[03 - Folder Naming Convention]]
- [[05 - Python Development Standard]]
- [[06 - CLI Standard]]

