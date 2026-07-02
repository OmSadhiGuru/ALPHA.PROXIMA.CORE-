---
title: "RP-001 Source Registry"
aliases: ["RP-001 Sources", "Consciousness Source Registry"]
tags: [research, rp-001, sources, registry, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["LUMIAION", "JERANIUM"]
research_program: "RP-001 Atlas of Human Consciousness"
---

# RP-001 — Source Registry

---

## Purpose

This registry tracks every source that contributes to the Atlas of Human Consciousness. It records source identity, type, quality assessment, and which research notes cite it. It is the authoritative attribution record for RP-001.

Per [[Book III - Knowledge Integrity]], Art. I, Sec. 1.5: every claim that derives from an external source must be attributed to that source. This registry is how RP-001 fulfils that obligation at the program level.

---

## Source Quality Criteria

All sources are assessed on the following criteria per [[Research Governance Protocol]], Stage 2:

| Criterion | Description |
|-----------|-------------|
| **Independence** | Is this source independent of other sources making the same claim? |
| **Methodology** | Is the methodology documented and sound? |
| **Replication** | Has the finding been independently replicated? |
| **Peer review** | Has it been subject to expert evaluation? |
| **Recency** | Is it current? When is recency material for this domain? |
| **Potential bias** | Does the source have interests that might influence findings? |

**Quality ratings:** High / Medium / Low / Unknown

---

## External Contributor Registry

These are the AI and institutional contributors delivering research to RP-001.

| Contributor | Type | Quality Profile | Notes |
|-------------|------|-----------------|-------|
| Perplexity | AI Research Tool | Medium (methodology rarely documented; sources cited) | Best used for literature surveys and finding primary sources; not for novel synthesis |
| Gemini | AI Research Tool | Medium (strong breadth; synthesis quality varies) | Best used for framework comparison and cross-domain synthesis |
| SanaLab | Research Partner | To be assessed on first delivery | Quality will be assessed per-contribution |
| JERANIUM | Internal AI | High within defined role | Responsible for integration, classification, conflict detection; not a primary research source |
| Frederick Belizaire Gunville | Founder / Phenomenologist | High (Class P) | Phenomenological reports from direct practice; classified as Class P per [[Book III - Knowledge Integrity]], Art. II |

---

## Academic and Published Sources

*Sources will be registered here as they are cited in research notes.*

| Source ID | Title / Author | Type | Year | Quality | Cites in |
|-----------|---------------|------|------|---------|----------|
| SRC-001 | *(first source to be registered)* | | | | |

---

## Source Registration Protocol

When a new source is cited in any RP-001 research note:

1. Check if the source is already registered in this table
2. If not registered: add a new row with all fields populated
3. Add the Source ID to the research note's `sources` frontmatter field
4. If the source's quality is not yet assessed: flag as `Unknown` and note that assessment is pending

**Source ID format:** `SRC-NNN` (sequential, independent of research note numbering)

---

## Known Source Limitations by Contributor

### AI-Generated Sources (Perplexity, Gemini)

Per [[Research Governance Protocol]], Open Questions, Item 3: AI-generated research arrives without explicit methodology documentation. The following limitations apply to all AI-contributed research in this program:

- Training cutoff dates may mean AI outputs lack awareness of very recent findings
- AI outputs may synthesise across sources in ways that obscure individual source quality
- AI outputs may reflect biases in training data (e.g., overrepresentation of Western academic frameworks in consciousness research)
- AI outputs cannot be verified for accuracy without checking against primary sources

**JERANIUM's responsibility:** Flag any AI-contributed research note that makes claims without traceable primary sources. Such claims are assigned Class E (Emerging Evidence) or lower until primary sources are identified.

### Phenomenological Sources (Founder's Reports)

Class P reports from the Founder are epistemically valid within their domain — first-person subjective experience — but are not generalisable as objective empirical claims without additional evidence. They are registered here as a distinct source type and clearly labelled in all research notes.

---

## Related Documents

- [[RP-001 Master Index]]
- [[Research Governance Protocol]]
- [[Book III - Knowledge Integrity]]
- [[Research Note Template]]
- [[JERANIUM Charter]]

---

## Open Questions

- [ ] Should primary academic sources (published papers, books) have a separate quality assessment process from AI-contributed summaries of those sources?
- [ ] Who is responsible for verifying that AI-contributed citations are accurate? JERANIUM or a human reviewer?
- [ ] Should SanaLab contributions arrive through JERANIUM (mediated) or directly into the Source Registry (direct)?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | LUMIAION / JERANIUM | Registry created; no sources yet registered; contributor profiles established |
