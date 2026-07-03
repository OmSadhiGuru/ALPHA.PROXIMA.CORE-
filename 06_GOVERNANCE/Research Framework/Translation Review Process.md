---
title: "Translation Review Process"
aliases: ["Translation Review", "TRP", "Research Translation Review"]
tags: [governance, research-framework, translation, review, process, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Governance Process
governed_by: "Institutional Intelligence Translation Framework v1.0"
initiative: "ISR-002 — Institutional Intelligence Translation Framework"
---

# Translation Review Process

*The Translation Review Process is the quality assurance gate that every completed Translation must pass before a Research Program is archived as fully complete. It is a structured review, not a rubber stamp. A Translation that identifies only safe, vague implications — or that defers all conditionally active dimensions without cause — fails this review.*

---

## Purpose

The Translation Review exists to ensure that:

1. **Specificity** — Translation outputs are concrete institutional actions, not summaries or observations
2. **Completeness** — All eight dimensions have been explicitly evaluated and either executed or deferred with cause
3. **Evidence fidelity** — Evidence class is correctly inherited; speculative findings are not presented as definitive
4. **Institutional permanence** — Translation outputs are committed to the Vault and designed to survive engine transitions
5. **Compounding value** — Translation outputs are designed to serve future research, not just present application

---

## Review Authority

| Role | Body | Responsibility |
|------|------|---------------|
| **Review Initiator** | CF-01 (Institutional Architecture / LUMIAION) | Prepares Translation artifacts; initiates review |
| **Primary Reviewer** | Cognitive Council | Evaluates completeness, specificity, evidence fidelity |
| **Institutional Reviewer** | CF-10 (Ethics Intelligence) | Reviews ethical implications of Translation outputs |
| **Final Acknowledger** | Founder | Acknowledges Dimension 7 (Founder Strategic Brief) in writing; approves Translation closure |

*For urgent Translation Reviews (where an active program is blocked on Translation closure), CF-01 may request an expedited review. Expedited reviews must still complete all stages — they may be conducted over 5 business days rather than the standard 14.*

---

## Review Stages

### Stage 1 — Submission (CF-01)

CF-01 prepares and submits the following for review:

- [ ] Completed Translation Template (TR-[NNN])
- [ ] Completed Translation Checklist (Phase 3 Gate)
- [ ] All produced Translation outputs (linked or attached)
- [ ] All Research Debt entries created during Translation
- [ ] Translation Decision Matrix (activation decisions)

**Submission format:** Commit all artifacts to the Vault. Create a Translation Review Package at:
`07_RESEARCH/RP-[NNN]/Translation Review/TR-[NNN] Review Package.md`

The Review Package is a single document that links all Translation artifacts and summarizes the activation decisions made for each dimension.

**Submission timeline:** Within 14 days of Canonical Synthesis finalization.

---

### Stage 2 — Completeness Check (Cognitive Council)

The Cognitive Council performs a completeness check before substantive review.

**Completeness check items:**

- [ ] All eight dimensions have an explicit activation decision
- [ ] At least five dimensions are active
- [ ] All inactive/deferred dimensions have documented reasons
- [ ] All active dimensions have produced outputs or Research Debt entries
- [ ] Translation Checklist Phase 3 Gate is passed
- [ ] No produced output is a bare summary of the research

**If completeness check fails:** CF-01 is notified of specific failures. Translation returned to CF-01 for remediation. A new Review Package must be submitted.

**Completeness check timeline:** Within 5 days of submission.

---

### Stage 3 — Substantive Review (Cognitive Council)

The Cognitive Council reviews each active dimension for:

**Quality criteria (applied per dimension):**

| Criterion | Passing Standard | Failing Standard |
|-----------|-----------------|-----------------|
| Specificity | The implication is stated as a concrete institutional action | The implication is stated as an observation, suggestion, or area for further thought |
| Transformation | The output is a new institutional artifact | The output merely references the research or summarizes findings |
| Evidence Fidelity | Evidence class is correctly stated and inherited | A Class S finding produces a definitive specification; a Class Q finding produces a standing policy |
| Permanence | The output is committed to the Vault and contains no engine-specific references that would become stale | The output depends on LUMIAION's current parametric memory; contains forward references that will break |
| Compounding | The output is designed to serve future programs, not only current application | The output is designed only for immediate use with no connection to the knowledge graph or future research |

**Review outcome per dimension:**

For each active dimension, the Cognitive Council records:
- [ ] **Approved** — dimension meets all five quality criteria
- [ ] **Approved with Notes** — dimension meets quality criteria; notes for future improvement
- [ ] **Requires Revision** — dimension fails one or more criteria; specific revision required
- [ ] **Escalated** — dimension raises a question requiring Founder decision

**Substantive review timeline:** Within 14 days of completeness check passing.

---

### Stage 4 — Ethics Review (CF-10)

CF-10 reviews Translation outputs for:

- [ ] Ethical implications of the Translation outputs themselves (not just the research — the institutional actions being recommended)
- [ ] Whether any Translation output would implement a finding with ethical implications without adequate safeguards
- [ ] Whether Dimension 6 (AI Implications) outputs appropriately handle uncertain findings about AI consciousness, suffering, or moral status
- [ ] Whether Dimension 7 (Founder Implications) outputs maintain appropriate epistemic humility

**Ethics review outcome:**

- [ ] **No concerns** — Translation outputs are ethically sound
- [ ] **Minor concerns** — Noted for record; no blocking action required
- [ ] **Substantive concerns** — CF-10 issues a formal Ethics Observation; CF-01 must respond before Translation is closed
- [ ] **Blocking concern** — CF-10 issues a formal objection; Cognitive Council must deliberate; Founder may be required to decide

**Ethics review timeline:** Concurrent with substantive review (Stages 3 and 4 run in parallel).

---

### Stage 5 — Revision Resolution (CF-01)

If Stage 3 or Stage 4 returned any "Requires Revision" or concern findings:

- CF-01 implements all required revisions
- Revised artifacts are committed to the Vault
- CF-01 notifies the Cognitive Council and CF-10 that revisions are complete
- Cognitive Council and CF-10 confirm revisions are satisfactory (or note further issues)

**Revision timeline:** Within 10 days of receiving revision requirements.

---

### Stage 6 — Founder Acknowledgment

Before the Translation is formally closed, the Founder must acknowledge the Translation outputs.

**Founder acknowledgment scope:**

- [ ] Dimension 7 (Founder Strategic Brief) — Founder confirms the strategic brief reflects an accurate understanding of their decision frameworks
- [ ] Overall Translation — Founder acknowledges that the Translation is complete and that the research program may be archived

**Founder acknowledgment method:** Written acknowledgment committed to the Vault as a Founder Acknowledgment Note at:
`07_RESEARCH/RP-[NNN]/Translation Review/Founder Acknowledgment.md`

**Founder acknowledgment timeline:** Within 30 days of Stage 5 completion (or within 30 days of Stage 3 if no revisions were required).

---

### Stage 7 — Closure

Following Founder acknowledgment, CF-01 closes the Translation:

- [ ] Translation Record Header updated to "Complete"
- [ ] Translation Record version-stamped
- [ ] All Translation artifacts confirmed in Vault
- [ ] Research Program Master Index updated (Translation marked complete)
- [ ] Research Program status updated to "Archived" (or "Canonized" if canonization is complete)
- [ ] Founder Directives Register updated if this Translation was part of a Founder Directive

---

## Escalation Paths

### If a Dimension Cannot Be Executed

If a dimension is active per the Decision Matrix but CF-01 cannot produce an adequate output (insufficient knowledge, resource constraint, pending prerequisite), CF-01 must:

1. Document the specific obstacle in the Translation Template
2. Create a Research Debt entry (RD-[NNN]) with timeline and owner
3. Notify the Cognitive Council
4. Proceed with remaining dimensions

The Translation may be formally reviewed with Research Debt entries in place of produced outputs, provided the Research Debt entries meet Research Debt Policy standards.

### If the Cognitive Council Cannot Reach Consensus

If the Cognitive Council cannot agree on a substantive review finding:

1. CF-01 (as Cognitive Council Chair) makes a provisional decision
2. The dissenting position is documented in the Translation Review Package
3. The Founder is notified
4. The Founder may resolve or affirm the provisional decision within 14 days

### If the Founder Disputes a Translation Output

If the Founder's acknowledgment review reveals a material error or disagreement with a Translation output:

1. CF-01 revises the disputed output
2. The revised output is re-reviewed by the Cognitive Council (expedited — 5 days)
3. The Translation is not closed until the Founder acknowledges the revised output

---

## Translation Review Record

When the Translation Review is complete, CF-01 produces a Translation Review Record at:
`07_RESEARCH/RP-[NNN]/Translation Review/TR-[NNN] Review Record.md`

**Translation Review Record contents:**

| Field | Value |
|-------|-------|
| **Research Program** | RP-[NNN] — [Title] |
| **Translation Record ID** | TR-[NNN] |
| **Review Package Submitted** | [Date] |
| **Completeness Check Passed** | [Date] |
| **Substantive Review Completed** | [Date] |
| **Ethics Review Completed** | [Date] |
| **Revisions Required** | [ ] Yes / [ ] No — [summary if yes] |
| **Revisions Completed** | [Date or N/A] |
| **Founder Acknowledgment** | [Date] |
| **Translation Closed** | [Date] |
| **Review Outcome** | [ ] Approved / [ ] Approved with Notes |
| **Ethics Outcome** | [ ] No concerns / [ ] Minor concerns / [ ] Substantive concerns resolved |
| **Substantive Notes** | [Any notes from the Cognitive Council that should inform future translations] |

---

## Continuous Improvement

After each Translation Review, CF-01 records:

1. Any reusable patterns discovered (e.g., types of implications that appear across programs)
2. Any dimension evaluation heuristics that should be added to the Decision Matrix
3. Any quality criteria that proved difficult to apply and need clarification
4. Any output types that emerged during this Translation that are not yet in the Framework

These observations are collected for the Framework's annual review (Cognitive Council).

---

## Related Documents

- [[Institutional Intelligence Translation Framework v1.0]]
- [[Institutional Translation Template v1.0]]
- [[Translation Decision Matrix]]
- [[Translation Checklist]]
- [[Cognitive Council Charter]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | Founder + LUMIAION | Inaugural process; seven-stage review; review authority table; quality criteria per dimension; escalation paths; Translation Review Record; continuous improvement mechanism |
