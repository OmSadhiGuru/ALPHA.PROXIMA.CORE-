---
title: "Translation Checklist"
aliases: ["Translation Checklist", "TC", "Research Translation Checklist"]
tags: [governance, research-framework, translation, checklist, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Operational Checklist
governed_by: "Institutional Intelligence Translation Framework v1.0"
initiative: "ISR-002 — Institutional Intelligence Translation Framework"
---

# Translation Checklist

*This checklist is the operational gating document for every Canonical Research Program translation. It is used in three phases: Pre-Translation (before executing any dimension), In-Progress (during execution), and Completion Gate (before the Translation is closed). A Translation that does not pass the Completion Gate remains open regardless of how many dimensions have been executed.*

---

## Program and Record

| Field | Value |
|-------|-------|
| **Research Program** | RP-[NNN] — [Title] |
| **Translation Record ID** | TR-[NNN] |
| **Checklist Completed By** | [Name/Function] |
| **Checklist Date** | [Date] |

---

## Phase 1 — Pre-Translation Gate

*Complete before opening the Translation Template. All items must be checked before translation begins.*

### Research Program Readiness

- [ ] Canonical Synthesis is finalized (v1.0.0 or higher)
- [ ] Evidence Registry is complete and version-stamped
- [ ] Canonical Glossary is complete and version-stamped
- [ ] Theory Matrix is complete and version-stamped
- [ ] All research program stages (0–9) are marked complete in the Research Program Playbook
- [ ] Ethics Council review is complete, OR a documented waiver is in the Vault

### Research Debt Awareness

- [ ] Research Debt Register has been reviewed for this program
- [ ] All active RD-series entries affecting this program are documented in the Translation Template (Pre-Translation section)
- [ ] No active RD-series entry constitutes an Architectural Blocker that would invalidate the Canonical Synthesis

### Translation Infrastructure

- [ ] Translation Record ID assigned (TR-[NNN])
- [ ] Translation Template opened (`10_TEMPLATES/Institutional Translation Template v1.0.md` copied and instantiated)
- [ ] Translation Decision Matrix completed for this program

**Phase 1 Gate:** [ ] PASSED — proceed to translation  [ ] BLOCKED — reason: [reason]

---

## Phase 2 — In-Progress Tracking

*Update these items as each dimension is executed. This is a live tracking checklist, not a one-time completion.*

### Dimension Activation Decision

- [ ] All eight dimensions evaluated in the Translation Decision Matrix
- [ ] Activation decisions entered in the Translation Template
- [ ] At least five dimensions are active (or explicit deferrals documented for all inactive ones)

### Dimension 1 — Institutional

- [ ] **N/A** (dimension deferred or inactive — deferral documented)
- [ ] Structural implication clearly stated
- [ ] Required output type identified
- [ ] Output produced, OR Research Debt entry created with timeline
- [ ] Output connected to knowledge graph and Vault

### Dimension 2 — Engineering

- [ ] **N/A** (dimension deferred or inactive — deferral documented)
- [ ] Evidence class gate evaluated
- [ ] Engineering requirement clearly stated (not vague system description)
- [ ] Required output type identified
- [ ] Output produced, OR Research Debt entry created with timeline
- [ ] Output connected to knowledge graph and Vault

### Dimension 3 — Knowledge Graph (Always Active)

- [ ] New concept nodes identified
- [ ] New typed relationship edges identified
- [ ] Cross-program edges identified (if applicable)
- [ ] Typed relationship vocabulary used (grounds / extends / instantiates / competes_with / contradicts / requires / supports / exemplifies / precedes / contains)
- [ ] Knowledge Graph Update committed to Vault

### Dimension 4 — Educational (Always Active)

- [ ] Minimum conceptual vocabulary documented
- [ ] Misconceptions corrected by this research listed
- [ ] Recommended learning sequence produced
- [ ] AI function briefing produced (for cognitive function onboarding)
- [ ] Educational outputs committed to Vault

### Dimension 5 — Product

- [ ] **N/A** (dimension deferred or inactive — deferral documented)
- [ ] Foundation phase gate evaluated
- [ ] External problem / opportunity specifically named
- [ ] Distinctive Alpha Proxima contribution identified
- [ ] Output produced, OR Research Debt entry created with timeline

### Dimension 6 — AI (Always Active)

- [ ] Cognitive function impact assessment completed (all 14 functions evaluated)
- [ ] Functions requiring briefing identified
- [ ] LUMIAION context architecture update specified (or confirmed not required)
- [ ] Capability gaps identified (or confirmed none exist)
- [ ] Cognitive function briefings produced and committed to Vault

### Dimension 7 — Founder (Always Active)

- [ ] Strategic framework updates identified
- [ ] Strategic options opened by this research listed
- [ ] Prior assumptions this research invalidates named explicitly
- [ ] Phenomenological integration note produced (if applicable to domain)
- [ ] Founder Strategic Brief produced and committed to Vault

### Dimension 8 — Future Research (Always Active)

- [ ] New Research Programs warranted — listed with priority
- [ ] Out-of-scope items now warranting own programs — identified
- [ ] Open questions now tractable — evaluated
- [ ] Research Debt Register updated with any new debts identified during translation
- [ ] Research Commission drafts produced (or deferred with timeline)

---

## Phase 3 — Completion Gate

*Complete before closing the Translation. All items must be checked.*

### Translation Standard

- [ ] Every active dimension: specific implication stated (not vague)
- [ ] Every active dimension: required output type identified
- [ ] Every active dimension: output produced OR Research Debt entry created with timeline and owner
- [ ] Every active dimension: output connected to knowledge graph and Vault
- [ ] Every deferred dimension: deferral explicitly documented
- [ ] Every deferred dimension: reason for deferral stated
- [ ] Every deferred dimension: review trigger set

### Output Quality

- [ ] No Translation output is a mere summary of the research (summaries belong in the Canonical Synthesis, not here)
- [ ] Every Translation output is a new institutional artifact (policy / specification / brief / sequence / commission)
- [ ] Translation outputs are written to survive the current reasoning engine (no outputs depend on LUMIAION's parametric memory alone)
- [ ] Evidence class is correctly inherited (Class S findings do not produce definitive specifications)

### Institutional Completion

- [ ] Translation Review Process completed (see [[Translation Review Process]])
- [ ] All Translation artifacts committed to Vault with correct version stamps
- [ ] Founder has acknowledged the Translation outputs in writing
- [ ] LUMIAION institutional memory updated with Translation insights
- [ ] Founder Directives Register updated (if applicable)
- [ ] Research Debt Register finalized for this program

### Final Closure

- [ ] Translation Record Header marked "Complete"
- [ ] Translation Record committed to Vault at `07_RESEARCH/RP-[NNN]/[Translation Record path]`
- [ ] Translation Record linked from the Research Program Master Index
- [ ] Research Program can now be archived as fully complete

**Phase 3 Gate:** [ ] PASSED — Translation complete  [ ] INCOMPLETE — outstanding items: [list]

---

## Dimension Quick Reference

| Dimension | Always Active? | Evidence Gate | Output Types |
|-----------|--------------|--------------|-------------|
| 1 — Institutional | No | None | Constitutional provision, charter, policy, standing order |
| 2 — Engineering | No | Min. Class E | Engineering Proposal, ADR, specification |
| 3 — Knowledge Graph | **Yes** | None | Knowledge Graph Update, concept notes |
| 4 — Educational | **Yes** | None | Learning sequence, concept access map, AI briefing |
| 5 — Product | No | Min. Class M; Phase gate | Product vision, specification, IP documentation |
| 6 — AI | **Yes** | None | CF briefing, context architecture update |
| 7 — Founder | **Yes** | None | Strategic brief, phenomenological integration note |
| 8 — Future Research | **Yes** | None | Research Commission drafts, RD Register update |

---

## Related Documents

- [[Institutional Intelligence Translation Framework v1.0]]
- [[Institutional Translation Template v1.0]]
- [[Translation Decision Matrix]]
- [[Translation Review Process]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | Founder + LUMIAION | Inaugural checklist; three-phase gate structure; per-dimension tracking; completion standard; dimension quick reference |
