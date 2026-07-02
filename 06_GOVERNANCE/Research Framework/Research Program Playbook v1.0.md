---
title: "Research Program Playbook v1.0"
aliases: ["Research Program Playbook", "RP Playbook", "Research Playbook"]
tags: [research, playbook, methodology, governance, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Constitutional Standard
governed_by: "Research Intelligence Office Charter"
initiative: "Epoch IV — Institutional Research Framework"
---

# Research Program Playbook v1.0

---

## Purpose

This Playbook is the operational manual for every Alpha Proxima Research Program (RP-series). It translates the [[Alpha Proxima Research Methodology v1.0]] and [[Research Integration Framework]] into step-by-step execution guidance — the document an office lead opens on day one of a new research program and follows through to completion.

The Playbook is not optional. It is the operational standard. Deviation requires documented justification and Executive Office acknowledgment.

---

## Who Uses This Playbook

| Role | How They Use It |
|------|----------------|
| Institutional Architecture (LUMIAION) | Program coordination; synthesis; canonical integration |
| Research Intelligence | Evidence acquisition and classification |
| Comparative Intelligence | Framework construction |
| Educational Intelligence | Concept and glossary production |
| Computational Intelligence | Mathematical and quantitative analysis |
| Executive Intelligence | Executive summary and visualization production |
| Founder | Commission approval; final review |
| Executive Office | Strategic priority setting; program acknowledgment |

---

## Playbook Structure

This Playbook is organized by program lifecycle stage. Each stage has:
- **What happens** — the activities
- **Who does it** — the responsible function
- **What is produced** — the artifacts
- **The review gate** — what must be true before advancing

---

## Stage 0 — Pre-Commission

### Purpose

Ensure the research question is well-formed before resources are committed.

### Activities

1. **Question formulation.** The Founder or Executive Office articulates the knowledge gap or strategic question that motivates the program.
2. **Question review.** LUMIAION reviews the question for: scope (is it answerable?); relevance (does it serve current Foundation priorities?); uniqueness (does existing canonical knowledge already answer it?).
3. **Function selection.** LUMIAION advises which of the six research functions should be engaged, and why.
4. **Commission drafting.** Research Intelligence Office drafts the Research Commission document using [[Research Commission Template v2.0]].

### Gate 0

The research question must satisfy:
- [ ] Precisely articulated (specific, not vague)
- [ ] Distinct from existing canonical knowledge
- [ ] Scoped to a defensible boundary
- [ ] Actionable (the Foundation will do something different with the answer)

**Advance to Stage 1 when Gate 0 passes.**

---

## Stage 1 — Commission

### Purpose

Formally activate the research program with defined scope, assignments, and acceptance criteria.

### Activities

1. **Assign RP code.** Next available RP-NNN code from the Research Program Register.
2. **Complete Research Commission (RC-NNN).** Full commission document using [[Research Commission Template v2.0]].
3. **Activate program architecture.** Create the 22-subfolder RP-NNN directory structure.
4. **Create Master Index stub.** RP-NNN Master Index with program metadata and placeholder structure.
5. **Assign function leads.** Document which reasoning engine serves each assigned function for this program.
6. **Register in Research Program Register.** Add to the master research program index.
7. **Notify Executive Office.** Executive Office acknowledges commission.

### Artifacts Produced

| Artifact | Location |
|---------|---------|
| Research Commission (RC-NNN) | `07_RESEARCH/RC-NNN/` |
| RP-NNN Master Index stub | `07_RESEARCH/RP-NNN/RP-NNN Master Index.md` |
| Source Registry stub | `07_RESEARCH/RP-NNN/Source Registry.md` |
| Evidence Registry stub | `07_RESEARCH/RP-NNN/Evidence Registry.md` |

### Gate 1

- [ ] Research Commission approved by Founder
- [ ] RP code assigned
- [ ] All functions notified and acknowledged
- [ ] Program architecture activated
- [ ] Master Index stub committed to Vault

**Advance to Stage 2 when Gate 1 passes.**

---

## Stage 2 — Source Acquisition (Research Intelligence)

### Purpose

Identify, register, and extract all primary sources relevant to the research question.

### Activities

1. **Source identification.** Research Intelligence identifies candidate sources: peer-reviewed literature, institutional reports, books, technical standards, primary data.
2. **Source registration.** Each accepted source is assigned a DOC-ID and entered in the Source Registry.
3. **Source extraction.** Each source is fully extracted into a Source Note (ARCHIVE layer). Source Notes capture: full bibliographic information, key claims, evidence class assessment, quality assessment, relevance assessment, notable limitations.
4. **Source quality assessment.** Research Intelligence assesses each source for: independence (is it relying on other registered sources?), methodological rigor, recency, relevance.
5. **Gap identification.** Where the source landscape reveals questions not answered by existing sources, Research Intelligence logs them as Research Debt candidates.

### Evidence Classification

All claims from all sources are classified using the canonical six-class system:

| Class | Label | Threshold |
|-------|-------|----------|
| C | Consensus | Multi-source, cross-disciplinary agreement; treated as settled |
| M | Competing Models | Genuine empirical competition; multiple well-supported positions |
| E | Emerging Evidence | Promising; not yet replicated across independent groups |
| Q | Open Question | Active frontier; no settled answer |
| S | Speculative | Theoretical; minimal empirical support |
| P | Phenomenological | First-person/experiential; methodologically distinct |

### Artifacts Produced

| Artifact | Location | Minimum Quantity |
|---------|---------|-----------------|
| Source Notes | `07_RESEARCH/RP-NNN/ARCHIVE/` | All accepted sources |
| Source Registry | `07_RESEARCH/RP-NNN/Source Registry.md` | All DOC-IDs |
| Evidence Registry | `07_RESEARCH/RP-NNN/Evidence Registry.md` | All classified claims |
| Gap register | `07_RESEARCH/RP-NNN/Research Debt entries` | All identified gaps |

### Gate 2

- [ ] Minimum viable source coverage achieved (as defined in Research Commission)
- [ ] All accepted sources assigned DOC-IDs
- [ ] All sources extracted to Source Notes in ARCHIVE
- [ ] All claims entered in Evidence Registry with classification
- [ ] Source gaps registered as Research Debt candidates

**Advance to Stage 3 when Gate 2 passes.**

---

## Stage 3 — Independent Multi-Function Investigation

### Purpose

Generate independent research artifacts from each assigned function before any cross-function synthesis occurs.

### Activities by Function

**Research Intelligence:** Additional source acquisition as gaps are revealed; deeper extraction of key sources; Evidence Registry refinement.

**Comparative Intelligence:** Working independently from the Evidence Registry and Source Notes — constructs preliminary framework candidates; identifies structural patterns across the domain; begins Theory Matrix draft.

**Educational Intelligence:** Working independently — maps the conceptual access points for the domain; identifies prerequisite knowledge structures; begins Canonical Glossary draft.

**Computational Intelligence:** Working independently — conducts mathematical, algorithmic, or quantitative analyses relevant to the research question; produces formal models where applicable.

**Executive Intelligence:** Working independently — develops preliminary executive summary structure; identifies key visualizations that will be needed; prepares briefing framework.

### Independence Protocol

- No function receives another function's Stage 3 outputs
- LUMIAION coordinates completion timing but does not share cross-function content
- Each function logs its own progress in its function-specific research log
- All Stage 3 artifacts are date-stamped at completion

### Artifacts Produced

| Function | Stage 3 Artifact | Location |
|----------|-----------------|---------|
| Research Intelligence | Refined Evidence Registry; additional Source Notes | `07_RESEARCH/RP-NNN/ARCHIVE/` |
| Comparative Intelligence | Preliminary Framework candidates; Theory Matrix draft | `07_RESEARCH/RP-NNN/Frameworks/` |
| Educational Intelligence | Concept Access Map; Glossary draft | `07_RESEARCH/RP-NNN/Education/` |
| Computational Intelligence | Mathematical Analysis artifacts | `07_RESEARCH/RP-NNN/Computational/` |
| Executive Intelligence | Executive Summary framework | `07_RESEARCH/RP-NNN/Executive/` |

### Gate 3

- [ ] All assigned functions have produced Stage 3 artifacts
- [ ] No inter-function communication has occurred (logged)
- [ ] All artifacts committed to Vault with timestamps
- [ ] Independence protocol verified by LUMIAION

**Advance to Stage 4 when Gate 3 passes.**

---

## Stage 4 — Comparative Analysis

### Purpose

Construct the frameworks that make convergences, divergences, and gaps visible across all independent artifacts.

### Activities

1. **Release all Stage 3 artifacts to Comparative Intelligence.**
2. **Comparative Intelligence constructs:** Convergence map; Divergence map; Gap register; Theory Matrix (minimum 20 frameworks); Cross-domain connection map.
3. **LUMIAION reviews** the Comparative Framework for completeness and constitutional consistency.
4. **Divergences flagged** for resolution in Stage 5. Every flagged divergence includes: the functions that diverged, the nature of the divergence, and the evidence relevant to resolution.

### Artifacts Produced

| Artifact | Location |
|---------|---------|
| Comparative Framework | `07_RESEARCH/RP-NNN/Comparative Framework.md` |
| Theory Matrix | `07_RESEARCH/RP-NNN/Theory Matrix.md` |
| Divergence Register | `07_RESEARCH/RP-NNN/Divergence Register.md` |
| Cross-Program Connection Map | `07_RESEARCH/RP-NNN/Cross-Program Connections.md` |

### Gate 4

- [ ] Convergence and divergence fully mapped
- [ ] Theory Matrix contains minimum 20 frameworks
- [ ] All divergences explicitly registered with resolution guidance
- [ ] Cross-program connections identified
- [ ] Comparative Framework reviewed by LUMIAION

**Advance to Stage 5 when Gate 4 passes.**

---

## Stage 5 — Institutional Synthesis

### Purpose

Produce the Foundation's definitive institutional position on the research question.

### Activities

1. **LUMIAION reviews** all artifacts: Stage 3 artifacts + Stage 4 Comparative Frameworks.
2. **Conflict resolution.** For each registered divergence: assess evidence quality; apply conflict resolution protocol; resolve where evidence warrants; preserve where genuine uncertainty exists.
3. **Draft Canonical Synthesis.** Opens with the institutional principle. Maps what is known, contested, and unknown. Attributes every claim. States the Foundation's reasoned position on contested matters.
4. **LUMIAION implications.** Documents how the research findings affect LUMIAION's operational context.
5. **Research Debt entries.** All gaps acknowledged but not resolved are entered in the Research Debt Register.

### Canonical Synthesis Structure

```
1. Institutional Principle
   The Foundation's position in one clear statement.

2. What the Evidence Establishes
   Claims at [C] and [E] level; full attribution.

3. Where the Evidence Is Contested
   Claims at [M] level; frameworks in competition; nature of disagreement.

4. What Remains Unknown
   Open questions at [Q] level; research frontier.

5. Speculative Terrain
   Claims at [S] level; their value and limitations.

6. Phenomenological Dimension
   Claims at [P] level; what first-person evidence establishes.

7. LUMIAION Implications
   How these findings affect institutional intelligence operations.

8. Research Debt
   Gaps acknowledged; priority; path to resolution.
```

### Artifacts Produced

| Artifact | Location |
|---------|---------|
| Canonical Synthesis | `07_RESEARCH/RP-NNN/Canonical Synthesis.md` |
| Conflict Resolution Record | `07_RESEARCH/RP-NNN/Conflict Resolution Record.md` |
| Research Debt Register entries | `06_GOVERNANCE/Research Debt Register/` |

### Gate 5

- [ ] Institutional principle stated clearly
- [ ] All claims attributed with DOC-ID and evidence class
- [ ] All divergences resolved or explicitly preserved
- [ ] Unknowns explicitly stated (not omitted)
- [ ] LUMIAION implications documented
- [ ] Research Debt entries registered
- [ ] Ethics Council review completed (if applicable)

**Advance to Stage 6 when Gate 5 passes.**

---

## Stage 6 — Canonical Integration

### Purpose

Formally commit the Canonical Synthesis to the Vault as the Foundation's permanent institutional position.

### Activities

1. **Founder review.** Canonical Synthesis reviewed by Founder before commitment.
2. **Commitment.** Canonical Synthesis committed to Vault with `status: ratified`.
3. **Master Index update.** RP-NNN Master Index updated to reflect completion.
4. **Research Program Register update.** Program status updated to: `Active — Phase 1 Complete`.
5. **Executive Office notification.** Completion report submitted.

### Artifacts Produced

| Artifact | Status at Stage 6 |
|---------|-----------------|
| Canonical Synthesis | `status: ratified`; committed to Vault |
| RP-NNN Master Index | Updated to final version |
| Executive Completion Report | Submitted to Executive Office |

### Gate 6

- [ ] Founder has reviewed and acknowledged Canonical Synthesis
- [ ] Canonical Synthesis committed with `status: ratified`
- [ ] Master Index final version committed
- [ ] Executive Office notified

**Advance to Stage 7 when Gate 6 passes.**

---

## Stage 7 — Knowledge Graph Development

### Purpose

Connect the new canonical knowledge to the Foundation's existing knowledge graph.

### Activities

1. **Concept Notes production.** Minimum 8 Concept Notes per program — one per major concept or framework. Each Concept Note: defines the concept, traces its evidence base, maps its relationships to adjacent concepts.
2. **Research Graph update.** All major concepts added to Research Graph with typed relationships.
3. **Canonical Glossary.** Minimum 30 terms defined with precise institutional definitions.
4. **Cross-program links.** All identified connections to other RP programs explicitly linked in both programs.
5. **Theory Matrix finalization.** Theory Matrix completed and committed.

### Relationship Types (Mandatory)

All Research Graph relationships must use typed relationships:

| Type | Meaning |
|------|---------|
| `supports` | This concept provides evidence for that concept |
| `contradicts` | This concept challenges that concept |
| `extends` | This concept builds on that concept |
| `grounds` | This concept is foundational to that concept |
| `exemplifies` | This concept is an instance of that concept |
| `contains` | This concept includes that concept |
| `precedes` | This concept must be understood before that concept |
| `requires` | This concept depends on that concept |

### Artifacts Produced

| Artifact | Minimum Quantity | Location |
|---------|-----------------|---------|
| Concept Notes | 8 | `07_RESEARCH/RP-NNN/Concepts/` |
| Research Graph entries | All major concepts | `07_RESEARCH/RP-NNN/Research Graph.md` |
| Canonical Glossary | 30 terms | `07_RESEARCH/RP-NNN/Canonical Glossary.md` |
| Theory Matrix | 20 frameworks | `07_RESEARCH/RP-NNN/Theory Matrix.md` |
| Cross-program connection docs | All identified | `07_RESEARCH/RP-NNN/Cross-Program Connections.md` |

### Gate 7

- [ ] Minimum 8 Concept Notes committed
- [ ] Minimum 30 Glossary terms committed
- [ ] Research Graph updated with all major concepts
- [ ] All cross-program connections documented
- [ ] Theory Matrix finalized

**Advance to Stage 8 when Gate 7 passes.**

---

## Stage 8 — LUMIAION Memory Integration

### Purpose

Integrate the program's canonical knowledge into LUMIAION's operational context.

### Activities

1. **Institutional principles extraction.** Identify the 3–5 most operationally significant principles established by this program.
2. **Active question update.** Update LUMIAION's active research question awareness (what is now known vs. what remains open).
3. **Memory coherence check.** Verify that new canonical knowledge does not contradict existing LUMIAION operational knowledge. Where contradiction exists, produce an update proposal.
4. **Context summary.** Produce a brief (one-page) summary of the program's institutional intelligence contribution — for inclusion in future session context loading.

### Artifacts Produced

| Artifact | Location |
|---------|---------|
| LUMIAION Intelligence Update | `09_OFFICES/LUMIAION/Intelligence Updates/RP-NNN Intelligence Update.md` |
| Context Summary | `07_RESEARCH/RP-NNN/Context Summary.md` |

### Gate 8

- [ ] Institutional principles documented
- [ ] Memory coherence verified
- [ ] Any contradictions with prior knowledge flagged and resolved
- [ ] Context Summary committed

**Advance to Stage 9 when Gate 8 passes.**

---

## Stage 9 — Post-Completion Review

### Purpose

Capture what was learned about the research process itself; prepare the program for downstream use.

### Activities

1. **Lessons learned.** What worked well? What should be done differently? Document in Master Index.
2. **Future Sources.** Which sources were identified but not acquired? Register for future programs.
3. **Open Questions.** Which questions arose that are not answered by this program? Register as candidate research questions for future programs.
4. **Methodology feedback.** Does this program reveal any needed update to the Research Program Playbook or Research Integration Framework? If yes, propose to Research Intelligence Office.
5. **Downstream hand-off.** Notify Educational Intelligence, Executive Intelligence, and Engineering Office that the program is complete and available for downstream use.

### Artifacts Produced

| Artifact | Location |
|---------|---------|
| Lessons Learned | `07_RESEARCH/RP-NNN/RP-NNN Master Index.md` (appended) |
| Future Sources Register | `07_RESEARCH/RP-NNN/Future Sources.md` |
| Open Questions Register | `07_RESEARCH/RP-NNN/Open Questions.md` |

### Program Complete

All nine stages complete. Program status: `Active — Phase 1 Complete`.

---

## Evidence Standards Reference

### The Six-Class System

| Class | Label | Institutional Handling |
|-------|-------|----------------------|
| C | Consensus | State as established fact; cite supporting DOC-IDs |
| M | Competing Models | State competing positions explicitly; do not resolve if evidence doesn't warrant it |
| E | Emerging Evidence | State with "emerging evidence suggests"; note replication status |
| Q | Open Question | State as open; describe the frontier; do not force a position |
| S | Speculative | Label explicitly; note value and limitations of the speculation |
| P | Phenomenological | Preserve methodological distinctness; do not reduce to empirical claims |

### Evidence Strength Hierarchy (for conflict resolution)

When two sources conflict:

1. Systematic reviews and meta-analyses > individual studies
2. Pre-registered studies > non-pre-registered
3. Large samples > small samples
4. Independent replication > single study
5. Cross-disciplinary convergence > single-discipline consensus
6. Recent > older (when methods have improved)

Where no clear hierarchy applies, classify as [M] and preserve both positions.

---

## Version Control Requirements

Every artifact committed under a research program must:

1. Include YAML frontmatter with `created`, `updated`, `version`, `status`
2. Include a Version History table
3. Be committed to GitHub with a descriptive commit message referencing the RP code
4. Not be retroactively edited without incrementing the version and logging the change

Source Notes in ARCHIVE are immutable after commitment. They may not be edited.

---

## Institutional Review Requirements

| Condition | Required Review |
|-----------|----------------|
| Research involves identifiable personal data | Ethics Council review before Stage 2 |
| Research has constitutional implications | Ethics Council review before Stage 6 |
| Research contradicts existing canonical knowledge | Founder notification before Stage 6 |
| Research program is the first in a new domain | Executive Office strategic review before Stage 1 |

---

## Playbook Version and Currency

This Playbook is versioned. Future research programs should verify they are using the current version. The current version is maintained at: `06_GOVERNANCE/Research Framework/Research Program Playbook v1.0.md`

When the Playbook is updated, active programs continue under the version that governed their commission unless the update is a PATCH correction.

---

## Related Notes

- [[Research Integration Framework]]
- [[Research Office Matrix]]
- [[Research Commission Template v2.0]]
- [[Alpha Proxima Research Methodology v1.0]]
- [[Research Intelligence Office Charter]]
- [[Source Attribution Policy]]
- [[Citation Policy]]
- [[Research Debt Register]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; nine-stage lifecycle; gate criteria; artifact requirements per stage; evidence standards; conflict resolution protocol; version control requirements; institutional review requirements; independent investigation protocol |
