---
title: Research Note Standard
id: apx-design-research-note-standard
department: LUMIAION
domain: design
type: design-standard
status: active
version: 1.0.0
created: 2026-07-08
updated: 2026-07-08
source: founder-request
tags: [design-system, research, study-standard, evidence]
related: [knowledge-design-system.md, document-layout-standard.md, callout-standard.md, ../TEMPLATES/designed-study-note.template.md]
owner: Office of Research (scope pending Founder ratification)
---

# Research / Study Standard

## Purpose

Define the fixed structure for every future study note, and enforce a hard separation between five registers of claim that must never be blended (Constitution Art. XI; Design Principle 4).

## Required Fields, in Order

1. **Research Question** — what is being asked, framed with a `[!research-question]` callout.
2. **Hypothesis** — the tentative answer, explicitly marked as unconfirmed.
3. **Context** — why this question matters now, and what prior work it builds on.
4. **Evidence Type** — which of the seven Intellectual Honesty categories the study primarily produces.
5. **Method** — how the observation or data was obtained.
6. **Observation** — what was directly seen, measured, or reported.
7. **Data** — structured results, where applicable.
8. **Interpretation** — what the observer believes the data means, explicitly separated from Observation.
9. **Limitations** — what the study cannot establish.
10. **Risks** — any risk the study or its subject matter introduces, including risk of misuse if published.
11. **Ethical Concerns** — flagged with `[!ethics-review-required]` where applicable (Constitution Art. XIV).
12. **Founder Reflection** — the Founder's own synthesis, marked `[!reflection]`, kept distinct from Interpretation.
13. **Next Experiment** — what follow-up, if any, is proposed.
14. **Related Knowledge Objects** — linked list.
15. **Publication Potential** — whether this study is a `[!public-content-candidate]`, and what would need to happen before it could be.

## The Five-Register Separation

Every study note must keep these five registers visually and structurally distinct — never merged into one undifferentiated narrative:

| Register | Definition | Marker |
|---|---|---|
| Personal observation | What the Founder or a contributor directly noticed, without interpretation | Plain Observation field |
| Experiential report | A first-person account of an effect or experience | `[!reflection]` |
| Scientific evidence | Data obtained by a method that could, in principle, be reproduced by someone else | `[!evidence]`, tagged Empirical or Clinical |
| Symbolic interpretation | Meaning assigned through a traditional, mythological, or symbolic framework (Constitution Art. V implementing text — see Office of Consciousness) | `[!evidence]`, tagged Symbolic, or `[!reflection]` if unattributed to a framework |
| Speculation | An idea offered without evidentiary support, explicitly named as such | `[!evidence]`, tagged Speculative |

No study note may present content from one register using the visual marker of another. A symbolic interpretation dressed as scientific evidence is a defect in the document, not a stylistic choice.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-08 | Claude (Constitutional Secretary / Repository Architect) | Initial research/study standard, fifteen fields, five-register separation. |
