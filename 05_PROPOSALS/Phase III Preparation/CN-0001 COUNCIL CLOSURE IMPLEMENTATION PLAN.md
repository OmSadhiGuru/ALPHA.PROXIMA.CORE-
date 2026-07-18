---
title: "CN-0001 Council Closure Implementation Plan"
aliases: ["Council Closure Package", "Council Closure Plan"]
tags: [proposal, planning, governance, councils, cn-0001, alpha-proxima, preparation]
created: 2026-07-18
updated: 2026-07-18
status: draft
version: "0.1.0"
authors: ["Claude Code — Vault Architect"]
artifact_type: implementation-plan
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Governance"
reasoning_engine: "LUMIAION"
dependencies: ["[[CN-0001 - Constitutional Alignment Gap Report]]", "[[Ethics Council Charter]]", "[[Book II - Governance Framework]]"]
related_documents: ["[[PHASE III INSTITUTIONAL READINESS MAP]]", "[[Research Governance Protocol]]", "[[Foundational Architecture]]"]
related_research_programs: []
---

# CN-0001 Council Closure Implementation Plan

> **Preparation-only.** This plan drafts the *authority surfaces* for four councils and the order/dependencies for closing them. It ratifies nothing. Charter drafting proceeds only on Founder go; ratification is a separate RED-gated step.

## Grounding Evidence

- [[CN-0001 - Constitutional Alignment Gap Report]]: Gap 2 Research Council (**High** — RP-001 active), Gap 3 Engineering Council (**Medium**), Gap 4 Education Council (**Low, deferred**), Gap 5 Community Council (**Low, deferred**).
- [[Book II - Governance Framework]] Art. V constitutes **Research, Engineering, Ethics, Community** councils — **Education Council is absent from the Constitution.**
- [[Ethics Council Charter]] (ratified 2026-07-02) is the proven structural template and already names each future council's intended review surface (its "Relationships with Other Bodies" table).
- `03_AI_COUNCIL/Research Council.md` already exists as a **placeholder** (status `placeholder`) — it is amended, not created.

## ⚠️ Blocking Constitutional Finding

**Education Council has no constitutional basis.** Book II Art. V lists only Research, Engineering, Ethics, Community. Education Council appears only in derived documents (Ethics Charter relationship table; CN-0001 Gap 4). **It cannot be "closed" as a gap — it must first be *constituted* via a Class I amendment, or explicitly declined.** This is a Founder decision, not an architecture decision.

---

## Recommended Creation Order (evaluated, not assumed)

| Order | Council | Rationale | Gate |
|-------|---------|-----------|------|
| **1st** | **Research Council** | Highest urgency: RP-001 is *active* and canonisation authority currently has no home. Amends an existing placeholder. Clearest domain surface (epistemic standards). | After CNS-001 |
| **2nd** | **Engineering Council** | Medium urgency: infra decisions (incl. this color-system work) are being made under *de facto* Chief Engineering Architect authority with no formal oversight. Needed before Phase III technical architecture. | After CNS-001; before Phase III tech work |
| **3rd** | **Community Council** | Low urgency but **constitutionally grounded** (Art. V). Draft now as "ratify-ready, activate-later"; no current community function to govern. | After 1st & 2nd; activation deferred |
| **4th** | **Education Council** | **Blocked**: not in Constitution. Requires Class I amendment *or* formal decline. Prepare authority surface only; do not draft a ratifiable charter until grounded. | Class I amendment first |

**Why not parallel:** Research and Engineering councils share review boundaries with Ethics (pre-publication vs pre-deployment) and with each other (research tooling is both). Sequencing prevents overlapping authority claims being ratified simultaneously.

---

## Dependencies Between Councils

- **Research ↔ Engineering:** Research tooling (Research Management Toolkit) sits in `08_SYSTEMS` — governed by Engineering, *used* by Research. Boundary must be written once, referenced twice.
- **All ↔ Ethics:** Ethics holds pre-action review over all four (already defined in Ethics Charter). New charters must *reference*, not *redefine*, Ethics authority.
- **All ↔ AI Council:** Class III AI-related matters require AI Council concurrence (Book II Art. VI).
- **Research → JERANIUM:** Research Council governs JERANIUM (Book II Art. V line 152). Engineering → does **not** govern departments; owns infrastructure.

## Risks of Overlap

| Risk | Between | Mitigation |
|------|---------|------------|
| Double-governance of research tooling | Research vs Engineering | Explicit "owns infrastructure / owns epistemic standard" split |
| Pre-publication vs integrity review duplication | Research vs Ethics | Research = standards *authorship*; Ethics = constitutional *veto*. Not the same act. |
| Protocol-approval collision | Engineering vs AI Council | Engineering owns routing protocols; AI Council concurs on AI-specific clauses |
| Activating deferred councils prematurely | Community/Education | Draft as "ratify-ready, activate-later"; membership stays empty |

---

## Per-Council Authority Surfaces (domain-specific — NOT Ethics clones)

### 1. Research Council
- **Constitutional basis:** Book II Art. V; Book III Knowledge Integrity; [[Research Governance Protocol]].
- **Mission:** Guarantee that knowledge entering the canonical vault meets institutional epistemic standards.
- **Scope:** All research artifacts (RP-###), evidence classification, canonisation gate.
- **Authority:** Approve/reject canonisation; set epistemic standards; govern JERANIUM.
- **Explicit NON-authority:** No infrastructure control; no constitutional veto (that is Ethics); no engine selection (AI Council).
- **Membership model:** Small generalist-epistemologist panel + domain reviewers co-opted per program; JERANIUM non-voting advisory.
- **Quorum/decision:** Majority; canonisation requires recorded evidence-class sign-off.
- **Escalation:** → Ethics (integrity violation) → Executive (resource) → Founder (Class I).
- **↔ LUMIAION:** LUMIAION performs first-pass integrity check, routes to Council.
- **↔ Departments:** Governs JERANIUM; advises SOHMA/ATHENA/VORTEX on research outputs.
- **↔ Founder:** Class II charter; Founder concurs.
- **Inputs/outputs:** In: research artifacts, source registries. Out: canonisation decisions, epistemic standards, Research Council Findings.
- **Evidence/review standard:** Book III evidence classes (Consensus/Competing/Open/Emerging/Speculative).
- **COI controls:** Author cannot approve own canonisation; co-opted reviewers declare interests.
- **Records:** Canonisation Decisions in `04_DECISIONS/`; standards in `06_GOVERNANCE/`.
- **Ratification reqs:** Class II; Executive concurrence; Ethics review.
- **Dependencies:** RP-001 live; placeholder to amend.
- **Unresolved:** Generalist panel vs per-domain experts? (CN-0001 open question, unresolved).
- **Acceptance criteria:** Canonisation gate defined; JERANIUM governance line explicit; no overlap with Ethics veto; placeholder amended not duplicated.

### 2. Engineering Council
- **Constitutional basis:** Book II Art. V; [[Foundational Architecture]].
- **Mission:** Own and safeguard all technical infrastructure and its evolution.
- **Scope:** Knowledge + execution infrastructure; routing protocols; systems standards; the 08_SYSTEMS estate.
- **Authority:** Approve infra changes; approve changes to Knowledge/Decision Routing Protocols; own engineering standards.
- **Explicit NON-authority:** No authority over knowledge *content* (Research); no constitutional veto (Ethics); no department jurisdiction.
- **Membership model:** Chief Engineering Architect (chair) + technical reviewers; Codex as implementation/review agent (non-voting).
- **Quorum/decision:** Majority; infra changes require reviewed change record.
- **Escalation:** → Ethics (deployment risk) → Executive → Founder.
- **↔ LUMIAION:** LUMIAION consumes infra; does not govern it.
- **↔ Departments:** Serves all; governs none.
- **↔ Founder:** Class II charter.
- **Inputs/outputs:** In: change proposals, audit reports (the 08_SYSTEMS drafts!). Out: infra decisions, engineering standards, deployment approvals.
- **Evidence/review standard:** Engineering Standards ES-##; audit reports; test/verification records.
- **COI controls:** Implementer ≠ approver for own change.
- **Records:** Engineering decisions in `04_DECISIONS/`; standards in `06_GOVERNANCE/` or `08_SYSTEMS/Engineering Standards`.
- **Ratification reqs:** Class II; Ethics pre-deployment review referenced.
- **Dependencies:** **Consumes the 08_SYSTEMS Draft Triage Register** — this council would be the natural owner of that triage.
- **Unresolved:** Quorum size (Book II open question).
- **Acceptance criteria:** Infra ownership explicit; routing-protocol authority stated; boundary with Research tooling written; consumes triage register.

### 3. Community Council (ratify-ready, activate-later)
- **Constitutional basis:** Book II Art. V; [[Future Expansion Protocol]].
- **Mission:** Govern external relationships, partnerships, and future community expansion.
- **Scope:** Partnerships, external comms, community expansion.
- **Authority:** Define Future Expansion Protocol; approve partnerships (with Ethics values-review).
- **Explicit NON-authority:** **No authority over internal governance** (Book II Art. V line 168, verbatim).
- **Membership model:** Empty until a community function exists; charter defines seats, activation deferred.
- **Quorum/decision:** Defined but dormant.
- **Escalation:** → Ethics (values) → Executive → Founder.
- **↔ LUMIAION / Departments / Founder:** Advisory; Class II charter.
- **Inputs/outputs:** In: partnership proposals. Out: partnership decisions, expansion protocol.
- **Evidence/review standard:** Values-alignment with Book I Founding Principles.
- **COI controls:** Partnership beneficiaries recuse.
- **Records:** Partnership decisions in `04_DECISIONS/`.
- **Ratification reqs:** Class II; charter may ratify with membership empty.
- **Unresolved:** Nomination/ratification of members (Book II open question).
- **Acceptance criteria:** Charter ratify-ready; activation explicitly deferred; internal-governance exclusion preserved.

### 4. Education Council (BLOCKED — surface only)
- **Constitutional basis:** ⚠️ **NONE.** Absent from Book II Art. V. Referenced only in Ethics Charter + CN-0001.
- **Required first step:** Class I amendment to add Education Council to Book II, **OR** formal decline recorded in CN-0001.
- **Provisional mission (if grounded):** Govern curriculum, pedagogy, and learner-facing knowledge (natural tie to OSG Academy / OSG_LAUNCH/10_ACADEMY).
- **Non-authority:** No canonisation authority (Research); no infra (Engineering).
- **Acceptance criteria:** Do **not** produce a ratifiable charter until constitutionally grounded. Produce the amendment proposal OR the decline note.

---

## Exact Files Likely to Require Creation or Amendment

| Action | File | Type |
|--------|------|------|
| AMEND (placeholder → charter) | `03_AI_COUNCIL/Research Council.md` | existing placeholder |
| CREATE | `03_AI_COUNCIL/Engineering Council Charter.md` | new (mirror Ethics location) |
| CREATE (ratify-ready) | `03_AI_COUNCIL/Community Council Charter.md` | new |
| AMEND or DECLINE | `05_PROPOSALS/CN-0001 …` (add resolution records) | **RED — do not touch until gate confirmed** |
| CONDITIONAL | `00_CONSTITUTION/Book II …` (add Education Council) | **Class I — Founder only** |
| CREATE | `09_PEOPLE/Frederick Belizaire Gunville.md` (Gap 6, low priority) | new |

## Codex Review Criteria

1. Each charter has a **distinct** authority surface (no Ethics-clone language).
2. No new charter redefines Ethics/AI Council authority — references only.
3. Research↔Engineering tooling boundary is written exactly once.
4. Community Council preserves "no internal governance" verbatim.
5. Education Council produces **no** ratifiable artifact absent constitutional grounding.
6. Research Council **amends** the placeholder (no duplicate node → protects graph color Rule 3).

## Founder Decision Points

1. **Confirm CNS-001 = CN-0001** (or name the real gate).
2. **Education Council:** amend Constitution to add it, or formally decline (CN-0001 recommended defer).
3. **Creation order** approval (recommended: Research → Engineering → Community → Education-pending).
4. **Research Council composition** (generalist panel vs domain experts) — unresolved since 2026-07-02.

## Version History
| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-18 | Claude Code — Vault Architect | Domain-specific authority surfaces; evaluated order; Education Council constitutional gap flagged. |
