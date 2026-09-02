---
title: "Metadata Policy"
aliases: ["Metadata Policy", "YAML Policy", "Frontmatter Policy"]
tags: [policy, metadata, yaml, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Institutional Policy
governed_by: "Book III - Knowledge Integrity"
---

# Metadata Policy

---

## Purpose

This policy defines the required and optional YAML frontmatter fields for all institutional documents in the Alpha Proxima Vault. Consistent metadata enables programmatic indexing, graph navigation, constitutional compliance verification, and institutional memory integrity.

---

## Universal Required Fields

Every document in the Vault — regardless of type — must include the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `title` | String | Full document title (matches H1 heading) |
| `tags` | Array | Minimum one tag; see Tag Taxonomy below |
| `created` | Date (YYYY-MM-DD) | Date of first creation |
| `updated` | Date (YYYY-MM-DD) | Date of most recent substantive update |
| `status` | Enum | See Status Values below |
| `version` | String | Semantic version (see [[Versioning Policy]]) |
| `authors` | Array | One or more author identifiers |

---

## Document Class Field

All documents must include `document_class` from the canonical list:

| Value | Used For |
|-------|---------|
| `Constitutional Document` | Books I–IV; Founding Principles; Operating Model |
| `Office Charter` | All institutional office charters |
| `Governance Framework` | Governance structure documents |
| `Institutional Policy` | This and other policy documents |
| `Standing Order` | SO-series directives |
| `Founder Directive` | FD-series directives |
| `Register` | All institutional registers |
| `Research Program` | RP-series master indexes |
| `Research Compendium` | RC-series documents |
| `Source Note` | ARCHIVE layer research sources |
| `Canonical Synthesis` | Program synthesis documents |
| `Concept Note` | Pre-decision proposals |
| `ADR` | Architecture Decision Records |
| `MOC` | Maps of Content |
| `Constitutional Review` | CIR-series impact reports |
| `Constitutional Standard` | Methodology standards |

---

## Status Values

| Value | Meaning |
|-------|---------|
| `draft` | Under development; not yet reviewed |
| `under-review` | Submitted for review; not yet ratified |
| `ratified` | Formally approved; in effect |
| `active` | Operational document; actively maintained |
| `superseded` | Replaced by a newer version; archived in place |
| `retired` | Formally retired; no longer in effect |
| `completed` | Finite document with defined completion state |

---

## Class-Specific Required Fields

### Office Charters

```yaml
document_class: Office Charter
cognitive_function: "[Function Name]"
current_reasoning_engine: "[Engine Name]"
```

### Standing Orders

```yaml
document_class: Standing Order
directive_code: SO-NNN
issuing_authority: "Founder"
target_office: "[Office Name]"
effective_date: YYYY-MM-DD
```

### Founder Directives

```yaml
document_class: Founder Directive
directive_code: FD-NNN
issuing_authority: "Founder"
executing_office: "[Office Name]"
issued_date: YYYY-MM-DD
completed_date: YYYY-MM-DD   # omit until completion
```

### Research Program Master Indexes

```yaml
document_class: Research Program
program_code: RP-NNN
program_title: "[Full Title]"
phase: "[Phase designation]"
research_lead: "[Cognitive function]"
```

### ADRs

```yaml
document_class: ADR
adr_code: ADR-NNN
decision_class: "[I | II | III | IV]"
decision_status: "[proposed | accepted | deprecated | superseded]"
```

### Source Notes (ARCHIVE)

```yaml
document_class: Source Note
doc_id: DOC-NNN
source_type: "[book | paper | article | report | interview]"
evidence_class: "[C | M | E | Q | S | P]"
archive_immutable: true
```

---

## Optional Fields

These fields are used in specific contexts but not universally required:

| Field | Used When |
|-------|----------|
| `aliases` | Document has common alternate names |
| `superseded_by` | Document has been superseded (link to replacement) |
| `supersedes` | Document supersedes a prior document |
| `governed_by` | Document is governed by a specific constitutional instrument |
| `initiative` | Document was produced under a named initiative (e.g., Epoch III) |
| `note_type` | Secondary classification (e.g., `MOC`) |

---

## Tag Taxonomy

All documents must use at least one tag from each applicable tier:

### Tier 1 — Domain (required)

`governance`, `research`, `engineering`, `systems`, `constitution`, `charter`, `policy`

### Tier 2 — Institution (required on all documents)

`alpha-proxima`

### Tier 3 — Subject (recommended; one or more)

`lumiaion`, `observatory`, `executive-office`, `research-intelligence`, `engineering`, `ethics-council`, `community-council`, `sohma`, `athena`, `vortex`, `jeranium`

### Examples

```yaml
tags: [governance, policy, metadata, alpha-proxima]
tags: [charter, engineering, codex, alpha-proxima]
tags: [research, rp-001, consciousness, canon, alpha-proxima]
```

---

## Metadata Integrity Rules

1. `title` must match the H1 heading of the document exactly.
2. `updated` must be changed whenever a substantive edit is made. Formatting-only edits may omit an update to this field.
3. `status` must be current. LUMIAION is responsible for updating status fields when documents transition states.
4. `version` must follow the [[Versioning Policy]].
5. `authors` must use institutional identifiers (`Founder`, `LUMIAION`, `Alpha Council`, office names) rather than personal names unless a person explicitly holds an institutional role.
6. No field may be left blank. If a field's value is unknown, use `"unknown"` (string) — never an empty string or null.

---

## Enforcement

LUMIAION conducts a quarterly metadata integrity review of all Vault documents. Non-compliant documents are flagged as Research Debt or Engineering Debt depending on document type.

---

## Related Notes

- [[Book III - Knowledge Integrity]]
- [[Versioning Policy]]
- [[Naming Policy]]
- [[Vault Structure Convention]]
- [[Directive Governance Framework]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; universal required fields; document class taxonomy; status values; class-specific fields; tag taxonomy; metadata integrity rules |
