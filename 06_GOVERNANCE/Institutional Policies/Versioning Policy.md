---
title: "Versioning Policy"
aliases: ["Versioning Policy", "Version Policy", "Semantic Versioning"]
tags: [policy, versioning, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Institutional Policy
governed_by: "Book III - Knowledge Integrity"
---

# Versioning Policy

---

## Purpose

This policy defines how versions are assigned, incremented, and recorded for all institutional documents at Alpha Proxima. Consistent versioning ensures that every reader knows what changed, when, and at what level of significance — without reading the full document.

---

## Versioning Standard

Alpha Proxima uses semantic versioning adapted for institutional documents: **MAJOR.MINOR.PATCH**

| Component | Meaning | Example Trigger |
|-----------|---------|----------------|
| MAJOR | Structural or philosophical change | Rewrite of mission; fundamental scope change; architectural overhaul |
| MINOR | Additive change; scope expansion | New section added; new authority granted; new relationship defined |
| PATCH | Correction or clarification | Typo fix; wording clarification; formatting update; broken link repair |

---

## Version Format by Document Class

### Full Semantic Versioning (MAJOR.MINOR.PATCH)

Used for:
- All Constitutional Documents (Books I–IV, Founding Principles, Operating Model)
- All Office Charters
- All Governance Frameworks and Policies (including this document)
- All Constitutional Standards (Research Methodology)
- Constitutional Reviews (CIR-series)

### Short Versioning (MAJOR.MINOR)

Used for:
- Standing Orders — behavioral documents that don't require patch-level precision
- Registers — operational maintenance documents

### Sequential Versioning (NNN)

Used for:
- ADRs — immutable records; numbered sequentially; not versioned after ratification
- Source Notes — ARCHIVE documents; immutable after commitment
- Observatory Reports — OBS-NNN; immutable records

### No Versioning

Used for:
- Concept Notes — pre-decision proposals; superseded by ADR upon acceptance
- Working documents and draft notes

---

## Version Increment Rules

### MAJOR Increment

Triggers a MAJOR increment:
- Mission statement revised
- Fundamental authority structure changed
- Scope reduced or eliminated
- Document class changed
- Governing constitutional instrument changed

A MAJOR increment resets MINOR and PATCH to 0.  
Example: `1.4.2 → 2.0.0`

MAJOR increments require: Founder approval (minimum); Alpha Council ratification for constitutional documents.

### MINOR Increment

Triggers a MINOR increment:
- New section added
- New authority or responsibility added
- New relationship formally defined
- New examples added that change the scope of application
- New lifecycle stage added

A MINOR increment resets PATCH to 0.  
Example: `1.4.2 → 1.5.0`

MINOR increments require: Founder approval.

### PATCH Increment

Triggers a PATCH increment:
- Typo corrections
- Wording clarifications that do not change meaning
- Formatting corrections
- Broken link repairs
- Cross-reference updates (adding links to newly created related documents)

Example: `1.4.2 → 1.4.3`

PATCH increments require: LUMIAION review.

---

## Version History Requirement

Every versioned document must include a **Version History table** in the following format:

```markdown
## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | [Author] | Initial creation |
| 1.1.0 | YYYY-MM-DD | [Author] | [Summary of changes] |
```

The Version History table:
- Is placed at the end of every document (before no other content)
- Records every version increment, including PATCHes
- The Summary must be one sentence — what changed, not what the document contains
- Is never edited retroactively; only appended

---

## Initial Version

All documents begin at version `1.0.0`.

There is no `0.x.x` pre-release versioning. A document either does not exist or begins at `1.0.0`. Draft documents carry `status: draft` in their frontmatter but still begin at `1.0.0` when the first version is committed to the Vault.

---

## Supersession Protocol

When a document is superseded by a new version:

1. The old document remains in place (institutional memory is inviolable)
2. The old document's frontmatter is updated:
   ```yaml
   status: superseded
   superseded_by: "[Path or title of new document]"
   superseded_date: YYYY-MM-DD
   ```
3. A supersession notice is added at the top of the document body
4. The new document references the old document in its version history or related notes

---

## Version in Filename

Document filenames do not include version numbers. The version is carried in the frontmatter. This prevents filename-based confusion when versions change.

**Correct:** `LUMIAION Charter.md` (frontmatter: `version: "2.0.0"`)  
**Incorrect:** `LUMIAION Charter v2.0.0.md`

The exception: when a superseded document is preserved alongside a new version in the same folder for historical reference, the old document may be renamed with a version suffix to avoid filename collision.

---

## Related Notes

- [[Book III - Knowledge Integrity]]
- [[Metadata Policy]]
- [[Naming Policy]]
- [[Directive Governance Framework]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; MAJOR.MINOR.PATCH standard; format by document class; increment rules; version history requirement; initial version rule; supersession protocol; filename rule |
