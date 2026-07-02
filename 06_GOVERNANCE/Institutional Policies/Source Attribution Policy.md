---
title: "Source Attribution Policy"
aliases: ["Source Attribution Policy", "Attribution Policy", "Source Policy"]
tags: [policy, attribution, research, sources, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Institutional Policy
governed_by: "Book III - Knowledge Integrity"
---

# Source Attribution Policy

---

## Purpose

This policy defines how the Alpha Proxima Foundation attributes sources across all institutional documents. Attribution is not a formality — it is an epistemic commitment. When the Foundation makes a claim, every reader must be able to trace that claim to its origin, evaluate its quality, and understand exactly how much confidence to place in it.

Unattributed claims are not institutional knowledge. They are opinion.

---

## Governing Principle

**No claim without attribution. No attribution without classification.**

Every factual or empirical claim in a Foundation document must:
1. Be traceable to at least one source with a DOC-ID in the Source Registry
2. Carry an evidence class marker (C/M/E/Q/S/P) that reflects the quality of the underlying evidence
3. Be honest about what is known, what is contested, and what is unknown

---

## Source Registration

Every external source used in Foundation research must be registered:

1. Assigned a **DOC-ID** (DOC-NNN, sequential within a research program)
2. Entered in the **Source Registry** of the relevant research program
3. Assigned an **evidence class** at extraction time
4. Extracted into a **Source Note** in the ARCHIVE layer

No source may be cited in a Foundation document without a registered DOC-ID. This is not optional.

---

## Evidence Classification System

The six-class system is the canonical institutional standard. Every claim is classified at the time it enters the Foundation's knowledge base:

| Class | Label | Definition |
|-------|-------|-----------|
| C | Consensus | Multi-source, cross-disciplinary agreement; the claim is treated as settled by the relevant scientific community |
| M | Competing Models | Genuine empirical competition; multiple well-supported frameworks; the debate is substantive |
| E | Emerging Evidence | Promising but not yet replicated across independent groups; treat with interest, not confidence |
| Q | Open Question | Active research frontier; no settled answer; the honest position is uncertainty |
| S | Speculative | Theoretical; minimal empirical support; legitimate conjecture, not evidence |
| P | Phenomenological | First-person or experiential data; methodologically distinct from third-person empirical claims |

These classes are not evaluative rankings. A [P] claim is not weaker than a [C] claim — they are different in kind. Phenomenological claims are not reducible to empirical claims. Speculative claims may be important even without empirical support.

---

## In-Document Attribution Requirements

### Research Documents (Canonical Syntheses, Concept Notes, Synthesis Chapters)

Every empirical claim must carry:

```
[Claim text]. [DOC-ID] [Evidence Class]
Example: Default Mode Network activity shows characteristic deactivation during external attention tasks. [DOC-003] [C]
```

### Governance Documents

Governance documents (charters, frameworks, policies) do not require DOC-ID attribution — they express institutional positions, not empirical claims. However:

- When a governance document references an external authority (e.g., a regulatory standard, a published framework), it must name the source inline.
- When a governance document makes an empirical claim (e.g., citing a statistic), that claim must follow the standard attribution format.

### Internal Cross-References

When one Foundation document references another Foundation document, use Obsidian internal links:

```
[[Document Title]]
[[Folder/Document Title|Display Text]]
```

Internal cross-references are not source citations. They are navigation. A claim that derives from another Foundation document still requires the original external source attribution unless the claim originated within the Foundation.

---

## Attribution Format for Source Notes

Source Notes in the ARCHIVE layer follow this format for the document header:

```yaml
doc_id: DOC-NNN
source_type: [book | paper | article | report | interview | dataset | primary]
author: "[Last, First]"
year: YYYY
title: "[Full Title]"
publisher: "[Publisher or Journal]"
url: "[URL if available]"
access_date: YYYY-MM-DD
evidence_class: [C | M | E | Q | S | P]
archive_immutable: true
```

---

## Conflicting Sources

When two registered sources make conflicting claims:

1. Both claims are recorded in the Evidence Registry
2. Neither claim is suppressed or merged
3. The evidence class for the conflicting area is set to [M] (Competing Models) or [Q] (Open Question) as appropriate
4. The Canonical Synthesis explicitly acknowledges the conflict and the Foundation's reasoned institutional position

**False consensus is an epistemic violation.** If the evidence is genuinely divided, the synthesis must say so.

---

## LUMIAION-Generated Content

Content produced by LUMIAION (synthesis, institutional analysis, governance documents) is attributed to `LUMIAION` as author in the document frontmatter. This content:

- Does not require DOC-ID attribution when it expresses institutional position
- Does require DOC-ID attribution when it makes empirical claims derived from external sources
- Must clearly distinguish between "LUMIAION's institutional synthesis" and "the underlying evidence"

LUMIAION does not introduce external knowledge claims without routing them through the appropriate research process first.

---

## External AI-Generated Content

External AI-generated content (content produced by reasoning engines outside of a formal Foundation research process) may not be treated as a source. It may not receive a DOC-ID. It may not appear in the Evidence Registry. If an AI-generated insight is valuable, it must be validated through a Source Verification Pass before it enters institutional memory.

This rule exists because AI models synthesize and generate — they do not observe. Treating AI output as evidence collapses the distinction between knowledge and confabulation.

---

## Related Notes

- [[Book III - Knowledge Integrity]]
- [[Citation Policy]]
- [[Alpha Proxima Research Methodology v1.0]]
- [[Research Intelligence Office Charter]]
- [[Metadata Policy]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; governing principle; source registration; evidence classification system; in-document attribution requirements; Source Note format; conflicting source protocol; LUMIAION content attribution; AI content exclusion |
