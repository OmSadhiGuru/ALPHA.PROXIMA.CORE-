---
title: "ADR Template"
aliases: ["Architecture Decision Record Template", "Decision Record Template", "ADR"]
tags: [template, governance, decision-record, adr, process]
created: 2026-07-01
updated: 2026-07-01
status: active
version: "1.0.0"
authors: ["Alpha Council"]
template_type: ADR
---

# ADR Template — Architecture Decision Record

## Purpose

This template is the standard format for all Architecture Decision Records (ADRs) within [[Alpha Proxima Core]]. ADRs are the primary mechanism for capturing consequential decisions — why they were made, what alternatives were considered, and what the expected consequences are.

All Class I, II, and III decisions (as defined in [[Book I - The Constitution]], Article IV) must produce an ADR before they are considered ratified.

**To use this template:** Copy the file, rename it to `ADR-XXXX - [Short Title].md`, and place it in the appropriate folder (e.g. `04_DECISIONS/`).

---

## Context

ADRs were adopted as the standard decision record format for Alpha Proxima Core based on the widely-used practice in software architecture. They provide:
- A durable, queryable record of *why* decisions were made (not just *what* was decided)
- A basis for revisiting decisions when context changes
- Accountability and attribution for consequential choices
- A foundation for [[LUMIAION]]'s institutional memory

See also: [[Institutional Registry]] for the authority levels governing each decision class.

---

## Core Content

---

> **TEMPLATE BEGINS BELOW THIS LINE**
> *Delete everything above this line in your actual ADR. Fill in every section. Do not leave sections blank — write "N/A" with a brief explanation if a section truly does not apply.*

---

# ADR-XXXX — [Short Descriptive Title]

## Header

| Field | Value |
|-------|-------|
| **ADR Number** | XXXX |
| **Title** | [Short Descriptive Title] |
| **Date** | YYYY-MM-DD |
| **Status** | `Proposed` / `Accepted` / `Rejected` / `Deprecated` / `Superseded by ADR-XXXX` |
| **Decision Class** | Class I / II / III / IV (see [[Book I - The Constitution]], Article IV) |
| **Proposed By** | [[Name or Role]] |
| **Ratified By** | [[Alpha Council]] / [Working Group Name] / [Delegate Name] |
| **Ratification Date** | YYYY-MM-DD |
| **Supersedes** | ADR-XXXX or N/A |
| **Superseded By** | ADR-XXXX or N/A |

---

## Problem Statement

*In 2–5 sentences: What is the problem, tension, or opportunity this decision addresses? What happens if no decision is made? Be specific — vague problem statements produce vague decisions.*

---

## Context and Constraints

*What background does a reader need to understand why this decision is non-trivial? Include:*
- *The current state of relevant systems or processes*
- *External constraints (technical, resource, timeline, regulatory)*
- *Internal constraints (existing decisions, principles from [[Book I - The Constitution]])*
- *Who is affected by this decision and how*

---

## Decision

*State the decision clearly and directly. Start with: "We will..." or "Alpha Proxima Core will..."*

*This section should be unambiguous. Someone reading only this section should understand what was decided.*

---

## Rationale

*Explain why this decision was made. What factors were weighted? What principle from [[Book I - The Constitution]] guided the choice? This is the most important section — a decision without rationale is not a decision record, it is just a log.*

---

## Alternatives Considered

*List every meaningful alternative that was evaluated before settling on the decision above.*

### Alternative 1 — [Name]

**Description:** [What would this option do?]  
**Pros:** [Why was it considered?]  
**Cons / Reasons Rejected:** [Why was it not chosen?]

### Alternative 2 — [Name]

**Description:**  
**Pros:**  
**Cons / Reasons Rejected:**

### Alternative 3 — [Name] *(add as many as apply)*

**Description:**  
**Pros:**  
**Cons / Reasons Rejected:**

---

## Consequences

### Positive Consequences
- [What becomes easier, better, or more aligned with our principles?]

### Negative Consequences / Trade-offs
- [What becomes harder, more constrained, or less optimal as a result?]

### Risks
- [What could go wrong? What assumptions could prove false?]

### Mitigations
- [For each risk above, what is the plan if it materialises?]

---

## Implementation Notes

*What needs to happen for this decision to take effect? List concrete next steps, owners, and timelines if known. Cross-link to relevant notes or working documents.*

- [ ] [Action item 1] — Owner: [[Name]] — Due: YYYY-MM-DD
- [ ] [Action item 2] — Owner: [[Name]] — Due: YYYY-MM-DD

---

## Dissent

*Record any formal dissent from Council members or participants. Dissent is not failure — it is institutional memory. Format: "[[Name]] dissented on [date] on the grounds that [reason]."*

*If no dissent: write "No formal dissent recorded."*

---

## Review

*When should this decision be revisited? What event or condition would trigger a review?*

**Scheduled Review Date:** YYYY-MM-DD or [Event-triggered, e.g. "After first quarterly review of LUMIAION scope"]  
**Review Owner:** [[Name or Role]]

---

## Related Notes

- [[Book I - The Constitution]]
- [[Institutional Registry]]
- [[Concept Note Template]]
- [Link to Concept Note that preceded this ADR, if applicable]
- [Link to other related ADRs]

---

## Open Questions

*Questions that were not resolved before ratification but should be tracked.*

- [ ] [Question 1]
- [ ] [Question 2]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | [[Name]] | Initial draft |
| 1.1 | YYYY-MM-DD | [[Name]] | [What changed and why] |

---

> **TEMPLATE ENDS ABOVE THIS LINE**

---

## Related Notes

- [[Book I - The Constitution]]
- [[Institutional Registry]]
- [[Concept Note Template]]
- [[Alpha Council]]
- [[LUMIAION]]

---

## Open Questions

- [ ] Should ADRs be numbered sequentially across all decision classes, or should each class have its own numbering sequence (e.g. `ADR-I-001`, `ADR-III-007`)?
- [ ] Where should ADRs be stored? Proposal: `04_DECISIONS/` folder, but this needs to be formalised in the Vault Structure Convention.
- [ ] Should [[LUMIAION]] be permitted to mark an ADR as `Accepted` for Class IV decisions autonomously, or must a human always ratify?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-01 | [[Alpha Council]] | Initial template established |
