---
title: "02 - YAML Frontmatter Standard"
aliases: ["Frontmatter Standard", "Metadata Standard"]
tags: [systems, engineering, standards, yaml, metadata, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.1.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-02"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Vault Structure Convention]]"]
related_research_programs: []
---

# 02 - YAML Frontmatter Standard

## Purpose

Define consistent YAML frontmatter so the vault can support search, graph navigation, automation, validation, and future indexing without brittle assumptions.

---

## Scope

Applies to every Markdown note in the vault and to generated Markdown artifacts unless a more specific approved template overrides a field.

---

## Rules

- Every note must start with YAML frontmatter.
- Use lowercase snake_case field names.
- Use ISO dates: `YYYY-MM-DD`.
- Use semantic versions in quotes: `"1.0.0"`.
- Use lists for fields that may contain multiple values.
- Use wikilinks in `related_documents` when the target is an internal note.
- Use controlled status values.
- Do not store secrets, private keys, access tokens, or sensitive credentials in frontmatter.

### Required Fields

| Field | Type | Rule |
|-------|------|------|
| title | string | Must match the H1 unless the file is a template containing placeholders |
| aliases | list | Use `[]` when none exist |
| tags | list | Use kebab-case tags |
| created | date | Initial creation date |
| updated | date | Last meaningful update date |
| status | string | Controlled value |
| version | string | Semantic version |
| authors | list | People, roles, or reasoning engines |
| artifact_type | string | Document category |
| institutional_owner | string | Owning institution, council, department, or role |
| dependencies | list | Required notes, tools, standards, systems, or packages |
| related_documents | list | Internal documents directly connected to this artifact |
| related_research_programs | list | Research programs connected to the artifact, or `[]` |

### Optional Fields

| Field | Use |
|-------|-----|
| standard_id | Engineering standard identifier |
| template_type | Template classification |
| implementation_type | Technical implementation classification |
| research_id | Research note identifier |
| research_program | Research program identifier |
| evidence_class | Knowledge integrity classification |
| source_quality | High, Medium, Low |
| cognitive_function | Implementation, Governance, Research, Strategy, or other approved function |
| reasoning_engine | Reasoning engine that produced or materially updated the note |
| review_owner | Role responsible for review |
| review_date | Scheduled review date |
| supersedes | Replaced artifact |
| superseded_by | Successor artifact |

### Status Values

| Status | Meaning |
|--------|---------|
| draft | Being written |
| accepted | Approved decision record or accepted technical outcome |
| active | Current and usable |
| archived | Preserved, not maintained |
| deprecated | Still present but discouraged |
| draft | Being written |
| intake | Captured but not yet reviewed |
| pending_delivery | Awaiting source delivery or external input |
| placeholder | Reserved scaffold with incomplete content |
| planned | Intended but not active |
| ratified | Formally approved by the relevant authority |
| superseded | Replaced by a newer artifact |
| under_review | Awaiting review |

---

## Examples

```yaml
---
title: "Vault Note Generator"
aliases: ["Obsidian Note Generator"]
tags: [systems, automation, obsidian, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "0.1.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Implementation Note Template]]"]
related_documents: ["[[Vault Structure Convention]]"]
related_research_programs: []
---
```

---

## Best Practices

- Keep frontmatter descriptive, not exhaustive.
- Add fields only when they will support retrieval, validation, or maintenance.
- Prefer stable institutional terms over current vendor names.
- Keep `dependencies` honest; if a note cannot be used without something, list it.
- Update `updated` and `version` together for meaningful changes.

---

## Common Mistakes

- Mixing `author`, `authors`, `created_by`, and `owner` inconsistently.
- Using free-form status values such as `done`, `final`, or `approved` without definition.
- Adding URLs where a stable internal note should exist.
- Listing every vaguely related document instead of direct dependencies.
- Using technology names as institutional ownership.

---

## Future Evolution

Future versions may add machine-readable validation schemas. If validation becomes automated, failures should block generated artifacts but should not retroactively alter governance status.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | [[CODEX]] | Expanded controlled status values to cover existing institutional document states |
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial YAML frontmatter standard |

---

## Related Standards

- [[01 - Markdown Style Guide]]
- [[03 - Folder Naming Convention]]
- [[04 - File Naming Convention]]
- [[07 - Automation Standard]]
- [[10 - Template Standard]]
