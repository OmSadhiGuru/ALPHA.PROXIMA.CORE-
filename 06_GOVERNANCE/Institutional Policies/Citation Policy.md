---
title: "Citation Policy"
aliases: ["Citation Policy", "Reference Policy", "Citation Format"]
tags: [policy, citation, research, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Institutional Policy
governed_by: "Book III - Knowledge Integrity"
---

# Citation Policy

---

## Purpose

This policy defines how citations are formatted in Alpha Proxima Foundation documents. Consistent citation format ensures that every source referenced can be located, verified, and evaluated by any current or future reader.

This policy governs format. The [[Source Attribution Policy]] governs what must be cited and how sources are classified.

---

## Citation System

Alpha Proxima uses a **hybrid institutional citation system** that prioritizes:

1. **Traceability** — every citation must allow the reader to find the original source
2. **Clarity** — citations must be readable inline without requiring a separate bibliography to understand
3. **Classification** — every empirical citation must carry an evidence class marker

---

## Inline Citation Format

The standard inline citation format is:

```
[DOC-ID] [Evidence Class]
```

Used immediately after the claim:

```
The hippocampus plays a critical role in the consolidation of episodic memories from 
short-term to long-term storage. [DOC-004] [C]
```

For claims supported by multiple sources:

```
The default mode network is consistently activated during self-referential processing, 
mind-wandering, and future planning. [DOC-003, DOC-007, DOC-012] [C]
```

For claims with contested evidence:

```
Sleep may serve a role in synaptic homeostasis through active downscaling. [DOC-009] [M]
```

---

## Full Reference Format

When a document includes a formal References or Bibliography section, each entry follows this format:

### Books

```
[DOC-ID] Last, First. (Year). *Title of Book*. Publisher.
```

Example:
```
[DOC-004] Squire, Larry R. & Kandel, Eric R. (1999). *Memory: From Mind to Molecules*. Scientific American Library.
```

### Academic Papers

```
[DOC-ID] Last, First, & Last, First. (Year). Title of paper. *Journal Name*, Volume(Issue), Pages. DOI or URL.
```

Example:
```
[DOC-009] Tononi, Giulio, & Cirelli, Chiara. (2014). Sleep and the price of plasticity. *Neuron*, 81(1), 12–34. https://doi.org/10.1016/j.neuron.2013.12.025
```

### Reports and Institutional Documents

```
[DOC-ID] Organization Name. (Year). *Title of Report*. Publisher. URL.
```

### Articles and Web Sources

```
[DOC-ID] Last, First. (Year, Month Day). Title of article. *Publication*. URL. Accessed: YYYY-MM-DD.
```

### Primary Sources and Interviews

```
[DOC-ID] Last, First. (Year). *Description of Primary Source*. Context or repository.
```

---

## Internal Foundation Document Citations

When citing another Foundation document within a Foundation document, use Obsidian internal links:

```
As established in [[Book III - Knowledge Integrity]], the Archive Immutability Principle...
```

For formal references in a structured context:

```
Alpha Proxima Foundation. (2026). *Book III — Knowledge Integrity*. 
Alpha Proxima Vault. [[Book III - Knowledge Integrity]]
```

Internal document citations do not require DOC-IDs. They use Obsidian wikilinks.

---

## Evidence Class in Citations

The evidence class marker always follows the DOC-ID citation. It is not optional for empirical claims:

| Correct | Incorrect |
|---------|----------|
| `[DOC-003] [C]` | `[DOC-003]` (missing class) |
| `[DOC-007] [M]` | `DOC-007 [M]` (missing brackets) |
| `[DOC-009, DOC-012] [E]` | `[DOC-009] + [DOC-012]` (wrong format) |

When multiple sources support a claim and they have different evidence classes, use the most conservative (lowest confidence) class for the inline marker and document the disagreement in the Evidence Registry.

---

## Bibliography Placement

Formal bibliographies appear at the end of the document under:

```markdown
## Sources

[DOC-001] ...
[DOC-002] ...
```

In research program documents, the Source Registry serves as the formal bibliography. Individual synthesis chapters reference DOC-IDs without repeating the full bibliographic entry.

---

## What Does Not Require a Citation

The following do not require DOC-ID citations:

- Institutional positions established in Foundation constitutional documents (link to the document instead)
- Mathematical truisms and logical definitions
- Conceptual frameworks that are being introduced (the introduction itself is the source)
- Definitions provided within the same document

---

## Related Notes

- [[Book III - Knowledge Integrity]]
- [[Source Attribution Policy]]
- [[Alpha Proxima Research Methodology v1.0]]
- [[Research Intelligence Office Charter]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; hybrid citation system; inline format; full reference formats by source type; internal document citations; evidence class in citations; bibliography placement; non-citation items |
