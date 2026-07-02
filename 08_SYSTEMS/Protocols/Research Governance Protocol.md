---
title: "Research Governance Protocol"
aliases: ["Research Governance", "RGP", "Research Protocol"]
tags: [protocol, research, governance, evidence, knowledge, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["Frederick Belizaire Gunville", "LUMIAION"]
---

# Research Governance Protocol

## Purpose

This Protocol defines how research enters the Alpha Proxima Foundation, how evidence is evaluated, how confidence levels are assigned, how contradictory evidence is preserved, how revisions occur, how publications become canonical, and how failed hypotheses remain historically documented.

This Protocol is subordinate to [[Book III - Knowledge Integrity]] and governed by the [[Research Council]] in coordination with the [[Ethics Council Charter|Ethics Council]].

---

## Context

Research without governance is accumulation without discernment. The Alpha Proxima Foundation's knowledge base must be both comprehensive and trustworthy — a high bar requiring that every piece of knowledge entering the system passes through a defined quality and integrity process.

The first formal research program — [[RP-001 Master Index|RP-001 Atlas of Human Consciousness]] — made this Protocol necessary. As external contributors (Perplexity, Gemini, SanaLab) produce research for the Foundation, a clear process for receiving, evaluating, and integrating that research is essential.

---

## Core Content

### The Research Lifecycle

All research in Alpha Proxima passes through five stages:

```
Stage 1: INTAKE
      ↓ Research arrives from external or internal source
Stage 2: EVALUATION
      ↓ Evidence classified; sources evaluated; quality assessed
Stage 3: INTEGRATION
      ↓ Integrated into Vault with proper structure and attribution
Stage 4: ETHICS REVIEW
      ↓ Ethics Council reviews before canonisation
Stage 5: CANONISATION
      ↓ Formally enters canonical knowledge base; linked into graph
      ↓
(Ongoing) REVISION
      ↓ Updated as new evidence emerges
(Terminal) ARCHIVE
        Preserved as historical record when superseded
```

---

### Stage 1 — Research Intake

**Who initiates:** Any Foundation participant; external contributors; automated research pipelines.

**What arrives:** Research may arrive as:
- External AI outputs (Perplexity, Gemini, SanaLab contributions)
- Published academic papers, books, or reports
- Original research conducted by Foundation participants
- Phenomenological reports from the Founder's direct experience

**Intake requirements:**
Every piece of incoming research must arrive with or be given:

| Field | Required? | Notes |
|-------|-----------|-------|
| Source identification | Mandatory | Who or what produced it |
| Date of production | Mandatory | When it was produced |
| Domain classification | Mandatory | Which department's domain |
| Research Program assignment | If applicable | e.g. RP-001 |
| Initial quality flag | Mandatory | High / Medium / Low / Unknown |

**JERANIUM's role:** Receives all incoming research, applies initial classification, checks for existing Vault content on the same topic, and flags conflicts before evaluation begins.

---

### Stage 2 — Evidence Evaluation

**Who evaluates:** [[JERANIUM Charter|JERANIUM]] (initial); relevant department (domain review); [[Ethics Council Charter|Ethics Council]] (integrity review).

**Evidence Classification:**
All claims within the research are classified using the six-class taxonomy from [[Book III - Knowledge Integrity]], Article II:

| Class | Label | Criteria |
|-------|-------|----------|
| C | Consensus | Strong independent agreement; replicated |
| M | Competing Models | Multiple well-developed frameworks; genuine competition |
| Q | Open Questions | Tractable question; insufficient evidence for conclusion |
| E | Emerging Evidence | New; not yet replicated; promising but preliminary |
| S | Speculative Hypotheses | Coherent; minimal or no empirical support |
| P | Phenomenological | First-person subjective report; valid within its domain |

**Source Quality Assessment:**
Sources are evaluated on:

| Criterion | Assessment |
|-----------|------------|
| Independence | Is the source independent of other sources making the same claim? |
| Methodology | Is the methodology documented and sound? |
| Replication | Has the finding been independently replicated? |
| Peer review | Has it been subject to expert evaluation? |
| Recency | Is it current? When is recency material? |
| Potential bias | Does the source have interests that might influence the findings? |

**Conflict Detection:**
JERANIUM checks new research against existing Vault content. When conflicts are detected:
- If the conflict is minor: noted in the new note's Open Questions
- If the conflict is significant: a Comparative Framework note is produced (see [[RP-001 Comparative Framework]] for the model)
- If the conflict suggests existing Vault content is incorrect: revision process is triggered

---

### Stage 3 — Research Integration

**Who integrates:** LUMIAION (structural); JERANIUM (content); relevant department (domain accuracy).

**Integration requirements:**
Every research note committed to the Vault must include:

```yaml
---
research_id: RP-XXX-NNN
research_program: "RP-XXX [Program Name]"
evidence_class: C / M / Q / E / S / P
source_quality: High / Medium / Low
sources: ["Source 1", "Source 2"]
contributor: "Perplexity / Gemini / SanaLab / Internal"
intake_date: YYYY-MM-DD
canon_status: intake / under_review / canonical / archived
---
```

**Structural requirements:**
All research notes follow this structure (see [[Research Note Template]]):
1. Research ID and Program
2. Purpose
3. Source Information
4. Definitions (all technical terms defined)
5. Core Findings (with evidence classification on each claim)
6. Evidence Classification Summary
7. Source Quality Assessment
8. Conflicting Evidence (preserved, not resolved)
9. Related Documents
10. Related Research
11. Related Laws or Institutional Rules
12. Related ADRs
13. Future Experiments
14. Open Questions
15. Version History

---

### Stage 4 — Ethics Review

**Who reviews:** [[Ethics Council Charter|Ethics Council]] (mandatory for all research before canonisation).

**Review scope:**
- Source attribution complete and verifiable
- Evidence classification accurately applied
- Conflicting evidence preserved
- Claims do not exceed what evidence supports
- Methodology documented
- Limitations stated
- No conflict of interest undisclosed

**Review outcomes:**
- **Approved:** Research proceeds to canonisation
- **Approved with conditions:** Specific revisions required before canonisation; JERANIUM implements; re-review if conditions are significant
- **Deferred:** Additional evidence or clarification needed; research remains at `canon_status: under_review`
- **Rejected:** Research does not meet Knowledge Integrity standards; documented and archived as `canon_status: intake_rejected` with full rationale

---

### Stage 5 — Canonisation

**Who canonises:** Research Council (authority); LUMIAION (implementation).

**Canonisation act:**
- `canon_status` updated to `canonical`
- Note linked into all relevant knowledge graph nodes
- Research Program Master Index updated
- Source Registry updated
- Any relevant Theory Matrix or Comparative Framework updated

**Canonical research is:**
- The Foundation's authoritative position on the covered topic at the time of canonisation
- Subject to revision when new evidence emerges (see Revision Protocol below)
- Citable in all subsequent Foundation work

---

### Revision Protocol

**Trigger:** New evidence, new analysis, or identification of error in canonical research.

**Minor revision** (corrections, additions, clarification):
- JERANIUM or LUMIAION may implement
- Version History updated
- `updated` date updated in frontmatter
- No re-canonisation required

**Major revision** (change to core claims, reclassification, significant addition):
1. Concept Note submitted documenting the proposed revision and justification
2. Research Council reviews (7 days minimum)
3. Ethics Council review if revision has significant implications
4. Revision implemented by JERANIUM
5. Version History updated with explicit changelog
6. Prior version archived if substantially different

---

### Failed Hypothesis Protocol

When a hypothesis tested by the Foundation is disconfirmed:

1. A note titled `[Hypothesis Name] — Disconfirmed` is created in the relevant research folder
2. The note documents: the hypothesis, the testing method, the disconfirming evidence, the conclusion, and what was learned from the failure
3. `status: archived` and `outcome: disconfirmed` in frontmatter
4. The note is linked from the Research Program's Open Questions and from any canonical notes that previously referenced the hypothesis as promising
5. The note is **never deleted**

Disconfirmed hypotheses are institutional knowledge. The path to understanding passes through them.

---

### Publication Protocol

When Foundation research is published externally:

1. Internal canonisation must be complete before external publication
2. Ethics Council publication review completed (see [[Ethics Council Charter]])
3. All claims in the publication correspond to canonical Vault content
4. Any deviation between the publication and the Vault is documented and justified
5. A publication record note is created in `06_PROJECTS/` or the relevant research folder linking to the external publication
6. The publication's canonical status is tracked: if the external publication is later revised or retracted, the Vault is updated accordingly

---

### Research Program Registry

All formal Alpha Proxima Research Programs are registered here:

| ID | Program | Status | Lead | Contributors | Canon Date |
|----|---------|--------|------|-------------|------------|
| RP-001 | Atlas of Human Consciousness | Active — Intake | JERANIUM | Perplexity, Gemini, SanaLab | Pending |

---

## Related Notes

- [[Book III - Knowledge Integrity]]
- [[Ethics Council Charter]]
- [[JERANIUM Charter]]
- [[RP-001 Master Index]]
- [[Research Note Template]]
- [[Knowledge Routing Protocol]]
- [[Knowledge Ownership Protocol]]

---

## Open Questions

- [ ] Who formally constitutes the Research Council, and what are their qualifications?
- [ ] Should there be a time limit on how long research can remain in `under_review` status before it must be either canonised or rejected?
- [ ] How should the Foundation handle research produced by AI systems (Perplexity, Gemini) that arrives without explicit methodology documentation?
- [ ] Should external contributors (SanaLab, etc.) be granted access to the Vault to contribute directly, or should their contributions always be mediated through JERANIUM?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Frederick Belizaire Gunville / LUMIAION | Initial protocol established; triggered by RP-001 initiation |
