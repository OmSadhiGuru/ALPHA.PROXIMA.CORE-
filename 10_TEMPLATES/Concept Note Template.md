---
title: "Concept Note Template"
aliases: ["Concept Note", "Proposal Template", "CN Template"]
tags: [template, governance, proposal, concept-note, process]
created: 2026-07-01
updated: 2026-07-01
status: active
version: "1.0.0"
authors: ["Alpha Council"]
template_type: Concept Note
---

# Concept Note Template

## Purpose

This template is the standard format for all Concept Notes within [[Alpha Proxima Core]]. A Concept Note is a structured proposal submitted to the [[Alpha Council]] or a Working Group before a formal decision is made. It is the entry point to the governance process.

All Class I and Class II decisions (as defined in [[Book I - The Constitution]], Article IV) must be preceded by a Concept Note. Concept Notes are encouraged — but not required — for Class III decisions.

**A Concept Note is not a decision.** It opens deliberation. The decision is recorded in an [[ADR Template|ADR]].

**To use this template:** Copy the file, rename it to `CN-XXXX - [Short Title].md`, and place it in the appropriate folder (e.g. `05_PROPOSALS/`).

---

## Context

Concept Notes were adopted to separate the *proposal* phase from the *decision* phase of governance. This ensures that:
- Ideas are stress-tested before they become binding decisions
- All participants have time to respond before a vote is called
- The deliberation record is preserved independently of the outcome
- [[LUMIAION]] and human participants can contribute to shaping proposals before ratification

A well-written Concept Note dramatically improves the quality of the ADR that follows.

---

## Core Content

---

> **TEMPLATE BEGINS BELOW THIS LINE**
> *Delete everything above this line in your actual Concept Note. Fill in every section. Do not leave sections blank — write "N/A" with a brief explanation if a section truly does not apply.*

---

# CN-XXXX — [Short Descriptive Title]

## Header

| Field | Value |
|-------|-------|
| **CN Number** | XXXX |
| **Title** | [Short Descriptive Title] |
| **Date Submitted** | YYYY-MM-DD |
| **Status** | `Draft` / `Under Review` / `Approved for ADR` / `Rejected` / `Withdrawn` |
| **Submitted By** | [[Name or Role]] |
| **Submitted To** | [[Alpha Council]] / [Working Group Name] |
| **Decision Class Anticipated** | Class I / II / III (see [[Book I - The Constitution]], Article IV) |
| **Review Deadline** | YYYY-MM-DD *(minimum 14 days for Class I; 7 days recommended for Class II)* |
| **Linked ADR** | ADR-XXXX or "Not yet created" |

---

## Executive Summary

*In 3–5 sentences: What are you proposing and why does it matter? A reader who only reads this section should understand the essence of the proposal and its significance to [[Alpha Proxima Core]].*

---

## Problem or Opportunity

*What gap, tension, failure mode, or opportunity is this proposal responding to? Be concrete. Reference existing notes, systems, or decisions where relevant.*

*If this is a response to a known problem, link to any prior discussion or related ADR.*

---

## Proposed Approach

*Describe what you are proposing in enough detail that participants can evaluate it. This does not need to be fully specified — Concept Notes are proposals, not implementations — but it must be specific enough to deliberate on.*

Include:
- What would change or be created
- Who would be responsible
- What resources or time would be required (if known)
- How this aligns with the principles in [[Book I - The Constitution]], Article II

---

## Fit with Founding Principles

*Map the proposal explicitly to the Founding Principles in [[Book I - The Constitution]], Article II. Which principles does it advance? Does it create any tension with any principle? How is that tension resolved?*

| Principle | How This Proposal Relates |
|-----------|--------------------------|
| Openness | |
| Human-AI Complementarity | |
| Epistemic Humility | |
| Durable Memory | |
| Accountability | |
| Proportionality | |

---

## Alternatives

*What other approaches were considered before arriving at this proposal? Even brief alternatives help reviewers understand the choice space.*

### Alternative A — [Name or "Do Nothing"]
[Brief description and reason for not proposing this]

### Alternative B — [Name]
[Brief description and reason for not proposing this]

---

## Anticipated Consequences

### If Approved
- [What becomes possible or better?]
- [What commitments or changes does approval trigger?]

### If Rejected
- [What remains unresolved?]
- [Is there a fallback?]

### Risks
- [What could go wrong if this is adopted?]

---

## Questions for Deliberation

*List the specific questions you want reviewers to engage with. What aspects of the proposal are uncertain or contested? This is where you invite pushback.*

1. [Question 1]
2. [Question 2]
3. [Question 3]

---

## Deliberation Log

*Record responses, concerns, and commentary from participants during the review period. This log becomes part of the institutional record regardless of outcome.*

| Date | Participant | Comment / Response |
|------|-------------|-------------------|
| YYYY-MM-DD | [[Name]] | [Comment] |

---

## Outcome

*Completed after the review period ends.*

**Decision:** `Approved for ADR` / `Rejected` / `Withdrawn` / `Deferred`  
**Date of Decision:** YYYY-MM-DD  
**Decided By:** [[Alpha Council]] / [Name]  
**Rationale:** [Brief summary of why the proposal was approved or not]  
**Linked ADR:** [[ADR-XXXX - Title]] or N/A  

---

## Related Notes

- [[Book I - The Constitution]]
- [[Institutional Registry]]
- [[ADR Template]]
- [[Alpha Council]]
- [[LUMIAION]]
- [Any other notes directly relevant to this proposal]

---

## Open Questions *(unresolved at time of submission)*

- [ ] [Question that was not resolved before submission]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | [[Name]] | Initial draft submitted |
| 1.1 | YYYY-MM-DD | [[Name]] | [What changed and why] |

---

> **TEMPLATE ENDS ABOVE THIS LINE**

---

## Related Notes

- [[Book I - The Constitution]]
- [[Institutional Registry]]
- [[ADR Template]]
- [[Alpha Council]]
- [[LUMIAION]]

---

## Open Questions

- [ ] Where should Concept Notes be stored? Proposal: `05_PROPOSALS/` folder — needs formalising in the Vault Structure Convention.
- [ ] Should [[LUMIAION]] be permitted to submit Concept Notes autonomously, or must a human co-sign every proposal?
- [ ] Should there be a lighter-weight "quick proposal" format for Class III items that don't warrant a full Concept Note?
- [ ] What happens to a Concept Note if the submitter withdraws it — is the deliberation log still preserved?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-01 | [[Alpha Council]] | Initial template established |
