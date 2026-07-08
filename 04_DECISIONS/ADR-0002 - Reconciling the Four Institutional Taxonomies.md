---
title: "ADR-0002 - Reconciling the Four Institutional Taxonomies"
aliases: ["ADR-0002", "Four Taxonomies Reconciliation", "Role Axis Reconciliation"]
tags: [adr, governance, architecture, alpha-proxima, lumiaion, taxonomy]
created: 2026-07-07
updated: 2026-07-07
status: proposed
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
decision_class: "Class II"
ratified_by: null
ratification_date: null
supersedes: null
superseded_by: null
---

# ADR-0002 — Reconciling the Four Institutional Taxonomies

## Header

| Field | Value |
|-------|-------|
| **ADR Number** | 0002 |
| **Title** | Reconciling the Four Institutional Taxonomies |
| **Date** | 2026-07-07 |
| **Status** | `Proposed` |
| **Decision Class** | Class II — Institutional |
| **Proposed By** | LUMIAION (drafted during compilation of [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]]) |
| **Ratified By** | Pending — Founder |
| **Ratification Date** | Pending |
| **Supersedes** | N/A |
| **Superseded By** | N/A |

---

## Problem Statement

The vault currently contains four separate documents, each of which enumerates "who does what" in the Foundation, using different names, different groupings, and different numbers of entries:

1. **Constitutional Councils** ([[Book II - Governance Framework]], Article III) — Founder, Executive Council, AI Council, Research Council, Engineering Council, Ethics Council, Community Council. Governs *voting authority*.
2. **Chief Architect Roles** ([[AI Council Registry]], [[Engine Registry]]) — Chief Systems / Knowledge / Science / Research / Deep Investigation / Engineering / Memory Architect, plus LUMIAION's Constitutional Intelligence Core seat. Governs *which AI engine is currently assigned to which permanent cognitive function*.
3. **Domain Departments** ([[SOHMA Charter]], [[ATHENA Charter]], [[VORTEX Charter]], [[JERANIUM Charter]]) — SOHMA, ATHENA, VORTEX, JERANIUM. Governs *subject-matter jurisdiction*.
4. **Production Offices** ([[Office Registry]]) — LUMIAION, Institutional Architecture, Engineering Office, Research Intelligence Office, Institutional Observatory, Executive Office, Future Office. Governs *operational workflow function* (inputs/outputs/artifacts).

A fifth, narrower instance of the same pattern was found and corrected in [[LUMIAION - Operating Manual (LOOM)]] v1.1.0, where Comet and Perplexity's production-office assignments initially contradicted the Office Registry and were reconciled prior to filing.

Read individually, each document is internally consistent. Read side by side, a contributor cannot tell whether "Research" names a Council, a Chief Architect, a Department, or an Office — or whether these are four names for one thing that has drifted, or four genuinely different things. This ambiguity is a structural risk: a future contributor or AI agent could resolve it by inventing a fifth taxonomy (as the original LOOM draft did) rather than recognizing that one already governs the case in point.

---

## Context and Constraints

**What is not in question:** none of the four documents is factually wrong within its own scope. Each was ratified or authored for a distinct purpose, and each remains the sole authority for that purpose per [[Foundational Architecture]] and the "Single Source of Truth" objective this ADR serves.

**What is in question:** whether the vault has an explicit, named statement that these four lists are orthogonal axes rather than competing definitions. No such statement currently exists. Its absence is what allowed the LOOM drift to occur once, and nothing currently prevents it from recurring in the next department, workflow, or office document a contributor drafts.

**Known adjacent gap, not resolved by this ADR:** [[Research Council]] is explicitly a `status: placeholder` document — referenced as an active authority by [[Research Governance Protocol]] and others, but not yet constituted. This is already tracked by `[[CN-0001 - Constitutional Alignment Gap Report]]` in `05_PROPOSALS/` and is left to that proposal rather than duplicated here.

---

## Decision

The four taxonomies are hereby recognized as four orthogonal axes describing the same set of institutional activities from four different questions, not four competing definitions requiring merger:

| Axis | Question It Answers | Canonical Document | Governs |
|---|---|---|---|
| Authority | Who can vote to ratify this? | [[Book II - Governance Framework]] | Decision Classes I–IV routing |
| Engine | Which AI currently fulfills this cognitive function? | [[AI Council Registry]], [[Engine Registry]] | Engine selection, replacement, dependency risk |
| Domain | What subject matter does this concern? | [[SOHMA Charter]], [[ATHENA Charter]], [[VORTEX Charter]], [[JERANIUM Charter]] | Jurisdiction and boundary disputes |
| Function | What operational role does this play in getting work done? | [[Office Registry]] | Inputs, outputs, handoffs, review cycles |

**Rule going forward:** any new document that assigns "who does X" must state which axis it is populating, and must not introduce a fifth axis without an ADR. A single real-world entity (e.g. LUMIAION, or the Claude engine) can and does appear on more than one axis simultaneously — that is expected, not a conflict, provided each appearance is doing the job of its own axis.

This reconciliation is recorded here, in [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]] (Section 0, Canonical Dependency Map), and cross-referenced from [[Institutional Relationship Map]].

---

## Rationale

**Why an ADR instead of silently editing the four source documents?** Per the Founder's explicit instruction governing this work: existing canon remains authoritative for its own domain, and genuine inconsistencies are recorded as decisions rather than resolved by quietly rewriting a ratified document. None of the four documents is being changed by this ADR — only their relationship to each other is being named.

**Why now?** The LOOM incident (v1.0.0 to v1.1.0) demonstrated the failure mode concretely: a fifth, unauthorized taxonomy was drafted before anyone checked the other four. The Enterprise Knowledge Architecture consolidation is the first document explicitly designed to prevent recurrence, so this is the correct moment to name the rule it depends on.

---

## Alternatives Considered

### Alternative 1 — Merge the four lists into one canonical office/role table
**Pros:** A single table would be simpler to scan.
**Cons / Reasons Rejected:** The four lists answer different questions for different audiences (a Founder voting on a Class I decision does not need Perplexity's evidence-classification duties in the same table as engine dependency-risk ratings). Merging would lose information and would require rewriting four ratified documents for a cosmetic gain. Rejected.

### Alternative 2 — Deprecate the Office Registry / Production Offices axis in favor of the Chief Architect Roles axis
**Pros:** Reduces from four axes to three.
**Cons / Reasons Rejected:** The two axes are not redundant — Chief Architect Roles track engine assignment and replacement risk; Office Registry tracks day-to-day handoffs, artifacts, and review cadence. [[LUMIAION - Operating Manual (LOOM)]] depends specifically on the Office Registry axis and would need to be rebuilt against a coarser one. Rejected.

### Alternative 3 — Do nothing; treat the ambiguity as tolerable
**Cons / Reasons Rejected:** Already demonstrated to fail once (LOOM v1.0.0). Rejected.

---

## Consequences

### Positive Consequences
- Future documents assigning responsibility can state their axis explicitly and avoid inventing a fifth.
- The LOOM-style drift becomes checkable in one step: "which axis does this new assignment belong to, and does it match that axis's canonical document?"

### Negative Consequences / Trade-offs
- Contributors must now learn four axes instead of assuming one flat list of "departments."

### Risks
- **Axis creep** — a future document could still invent a fifth axis without reading this ADR. Mitigation below.

### Mitigations
- [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]] cites this ADR directly in its Canonical Dependency Map and Governance System sections, so the rule is discoverable from the top-level architecture document, not only from `04_DECISIONS/`.

---

## Implementation Notes

- [ ] Add a short cross-reference to this ADR in [[Institutional Relationship Map]] — **Owner: LUMIAION** — Priority: Medium
- [ ] Resolve the [[Research Council]] placeholder gap via `[[CN-0001 - Constitutional Alignment Gap Report]]` (tracked separately, not blocked by this ADR) — **Owner: Founder / Alpha Council**

---

## Dissent

None recorded — proposed and pending Founder review.

---

## Review

**Scheduled Review Date:** Alongside the next Department Charter or Office Registry revision, whichever comes first.
**Review Owner:** Founder + LUMIAION.
**Review scope:** Has any new document violated the axis rule since ratification?

---

## Related Notes

- [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]]
- [[Book II - Governance Framework]]
- [[AI Council Registry]]
- [[Engine Registry]]
- [[Office Registry]]
- [[SOHMA Charter]]
- [[ATHENA Charter]]
- [[VORTEX Charter]]
- [[JERANIUM Charter]]
- [[LUMIAION - Operating Manual (LOOM)]]
- [[CN-0001 - Constitutional Alignment Gap Report]]

---

## Open Questions

- [ ] Should this axis rule itself be promoted into [[Book II - Governance Framework]] as a standing article, rather than living only as an ADR?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-07 | Founder / LUMIAION | Proposed during compilation of the Enterprise Knowledge Architecture consolidation |
