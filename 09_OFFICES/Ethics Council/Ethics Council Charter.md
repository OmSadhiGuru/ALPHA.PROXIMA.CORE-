---
title: "Ethics Council Charter"
aliases: ["Ethics Council", "Ethical Review Body", "Constitutional Ethics"]
tags: [governance, ethics, charter, constitutional, alpha-proxima, council]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Frederick Belizaire Gunville"]
---

# Ethics Council Charter

## Purpose

This Charter formally constitutes the Ethics Council of the Alpha Proxima Foundation and defines its mission, authority, membership, operating procedures, and relationships with all other institutional bodies.

The Ethics Council is referenced in [[Book I - The Constitution]] and [[Book II - Governance Framework]] but was not constituted at founding. This Charter closes that gap. The Ethics Council is the only governing body that holds independent constitutional authority — it cannot be instructed by any other council, including the Executive Council, in the exercise of its core function.

---

## Context

Every institution that wields significant power — over knowledge, over intelligence systems, over other people's decisions — requires an independent body whose only job is to ask: *is this right?* Not efficient. Not legal. Not popular. *Right.*

The Alpha Proxima Foundation wields power of a specific kind: it designs intelligence architectures, produces knowledge that influences decisions, deploys AI systems, and will eventually reach a broader community. Without an Ethics Council, there is no structural mechanism to prevent the accumulated drift of values over time — the slow substitution of convenience for principle that corrupts most institutions not through dramatic failure but through small, unremarkable exceptions.

The Ethics Council exists to make exceptions visible, costly, and reviewable.

---

## Core Content

### Mission

The Ethics Council exists to ensure that the Alpha Proxima Foundation acts in accordance with its constitutional principles — not occasionally, not when convenient, but systematically. It is the institutional conscience. Its authority is narrow, deep, and non-negotiable.

**In one sentence:** The Ethics Council ensures the Foundation never becomes what it was built to prevent.

---

### Constitutional Standing

| Attribute | Value |
|-----------|-------|
| Authority class | Constitutional oversight — independent |
| Scope | All Foundation activities; unlimited investigative authority |
| Reporting to | Founder directly; no other council may direct it |
| Voting weight | Veto power on constitutional violations |
| AI participation | Non-voting advisory role only (via LUMIAION) |
| Defined in | [[Book I - The Constitution]], Art. III; [[Book II - Governance Framework]], Art. V |

---

### Authority

The Ethics Council holds the following authorities, which may not be overridden by any council except the Founder acting through a Class I constitutional amendment:

**1. Pre-Action Review Authority**
The Ethics Council may review — and delay pending review — any Foundation action it determines may raise constitutional concerns. This is a right, not a requirement. The Council exercises it selectively.

**2. Veto Authority**
The Ethics Council may veto any action, decision, or publication that it determines violates [[Book I - The Constitution]]. A veto may be overridden only by the Founder via Class I amendment process — a high bar, by design.

**3. Investigative Authority**
The Ethics Council may investigate any past or present Foundation activity without requiring permission from any other body. It may access all Vault documents, ADR records, and institutional communications relevant to an investigation.

**4. Constitutional Interpretation Authority**
When a constitutional provision is ambiguous and bears on an ethical question, the Ethics Council's interpretation is advisory to the Founder. The Founder retains final interpretive authority but must record their reasoning if they deviate from the Ethics Council's interpretation.

**5. Amendment Proposal Authority**
The Ethics Council has the right to propose Class I constitutional amendments when it identifies provisions that, in practice, create ethical contradictions or gaps.

---

### Decision Scope

The Ethics Council reviews decisions, actions, and outputs in the following domains:

| Domain | Review Trigger | Review Type |
|--------|---------------|-------------|
| Research publication | Before any research becomes canonical | Pre-publication review |
| Software and automation deployment | Before deployment of any automated system | Pre-deployment review |
| AI deployment and engine changes | Before any AI engine is granted new authority | Pre-authority review |
| Institutional partnerships | Before any formal partnership is ratified | Pre-partnership review |
| Knowledge canonisation | When research makes claims with significant real-world implications | Evidence integrity review |
| Constitutional amendments | All Class I proposals | Mandatory review |
| Conflict of interest | When any participant's personal interests may influence institutional decisions | Triggered investigation |
| Community-facing communications | Any public statement made in the Foundation's name | Advisory review |

---

### Membership

**Composition:** 3–5 independent human members  
**AI participation:** LUMIAION holds a permanent non-voting advisory seat  
**Chair:** Elected by members; one-year term; renewable once  
**Quorum:** Majority of members  
**Vote to veto:** Majority of members  
**Vote to override veto (Council only):** Not possible — only Founder via Class I process

**Independence requirements:**
- No member may simultaneously hold a seat on the Executive Council, AI Council, or any other governing body
- No member may have a direct financial interest in Foundation activities under their review
- Members serve three-year staggered terms to prevent wholesale replacement

**Founding members:** *To be named — see Open Questions*

---

### Selection Criteria

Members of the Ethics Council are selected by the Founder, in consultation with the Executive Council, based on:

| Criterion | Description |
|-----------|-------------|
| Ethical reasoning depth | Demonstrated capacity for structured ethical reasoning, not just ethical instinct |
| Domain breadth | Familiarity with at least two of: technology ethics, bioethics, epistemology, governance, philosophy |
| Independence | No significant personal or financial relationship with Foundation activities |
| Epistemic humility | Track record of changing positions when evidence changes |
| Constitutional alignment | Alignment with the Founding Principles in [[Book I - The Constitution]], Art. II |
| Communication quality | Ability to communicate ethical judgments clearly and without condescension |

Members need not be philosophers. They must be honest thinkers.

---

### Operating Procedures

**1. Standing Review**
The Ethics Council conducts a standing quarterly review of all ADRs, publications, and significant actions from the prior quarter. This is the default operating mode — not crisis response.

**2. Triggered Review**
Any Foundation participant — human or AI — may trigger an Ethics Council review by submitting a written concern to the Chair. LUMIAION is obligated to trigger a review when it detects a potential constitutional conflict.

**3. Pre-Action Review**
When a domain requires pre-action review (see Decision Scope table), the responsible party submits the proposed action to the Ethics Council with sufficient lead time for review (minimum 7 days for routine matters; minimum 14 days for constitutional matters).

**4. Investigation**
When the Ethics Council opens a formal investigation, it notifies the Founder and the relevant parties. Investigations are documented. Outcomes are published in `04_DECISIONS/` as Ethics Council Findings, not ADRs.

**5. Deliberation Record**
All Ethics Council deliberations are documented in the Vault. The record includes: what was reviewed, who participated, what positions were held, what the outcome was, and whether any member dissented from the majority position. Dissent is always recorded.

**6. Veto Exercise**
A veto is issued in writing, citing the specific constitutional provision violated and the reasoning. The vetoed party has 7 days to respond. The Ethics Council may withdraw the veto if the response resolves the concern. If the veto stands, the Founder receives both positions and must either accept the veto or initiate a Class I amendment to override it.

---

### Ethical Review Protocols by Domain

#### Research Review Protocol
Before any research produced under the Alpha Proxima Research Program becomes canonical:

1. Source attribution complete and verifiable
2. Evidence classification applied (Consensus / Competing Models / Open Questions / Emerging Evidence / Speculative Hypotheses)
3. Conflicting evidence preserved — not merged into false consensus
4. Claims do not exceed what the evidence supports
5. Methodology is documented and evaluable
6. Limitations are stated explicitly

**LUMIAION's role:** Performs initial check against these criteria; routes to Ethics Council if any criterion is not met.

#### Software and Automation Review Protocol
Before any automated system is deployed that acts on behalf of the Foundation:

1. Scope of automation is explicitly defined
2. Human override is built in — no fully autonomous action without defined override
3. Failure modes are documented
4. Data handling is constitutional (see [[Knowledge Ownership Protocol]])
5. Ethics Council has reviewed the delegation of authority

#### AI Deployment Review Protocol
Before any AI engine is granted new institutional authority (new role, expanded scope, new access):

1. The role is defined in [[AI Council Registry]] — engine is filling a permanent role, not creating a new one
2. Constitutional alignment check completed (see [[LUMIAION Architecture Spec v0.1]], Section 9)
3. Data sovereignty implications assessed
4. Ethics Council has reviewed the proposed authority level

#### Publication Review Protocol
Before any knowledge is published externally in the Foundation's name:

1. Claims are accurately described — not overstated, not understated
2. Sources are attributed
3. Uncertainty is disclosed
4. The publication does not misrepresent the Foundation's positions or capabilities
5. Ethics Council advisory review completed (blocking only if constitutional violation detected)

#### Partnership Review Protocol
Before any formal institutional partnership is ratified:

1. Partner's values are compatible with [[Book I - The Constitution]] Founding Principles
2. No conflict of interest exists between the partnership and the Foundation's mission
3. Knowledge ownership implications are assessed under [[Knowledge Ownership Protocol]]
4. Ethics Council has reviewed and has no constitutional objection

---

### Constitutional Amendment Procedures for Ethical Conflicts

When the Ethics Council identifies a constitutional provision that, in practice, creates ethical contradictions:

1. Ethics Council Chair submits a formal **Ethics Council Finding** to the Founder
2. The Finding documents: the provision, the conflict, the evidence, and the proposed resolution
3. The Founder has 30 days to respond
4. If the Founder agrees: a Concept Note is submitted for the Class I amendment process
5. If the Founder disagrees: the Finding is archived with the disagreement recorded; the Ethics Council may resubmit after 90 days if conditions change
6. The Ethics Council may not initiate a constitutional amendment unilaterally — it can only propose and advocate

---

### Relationships with Other Bodies

| Body | Relationship | Ethics Council Authority |
|------|-------------|-------------------------|
| Founder | Reports to; may advise against but not override | Founder is final authority; Ethics Council is constitutional conscience |
| Executive Council | Independent from; reviews Executive decisions for constitutional alignment | May veto Executive decisions that violate Constitution |
| AI Council | Oversees AI authority grants and engine deployments | Pre-authority review required for new AI authority |
| Research Council | Reviews research for integrity before canonisation | Pre-publication review; may block on integrity grounds |
| Engineering Council | Reviews automated systems before deployment | Pre-deployment review; may block on constitutional grounds |
| Education Council | Advisory review of community-facing content | Advisory only unless constitutional violation detected |
| Community Council | Advisory review of partnership and external relations | Pre-partnership review; may block on values-alignment grounds |
| LUMIAION | LUMIAION is obligated to trigger Ethics Council review when it detects conflicts | LUMIAION is a reporter and advisor, not a reviewer; the Ethics Council reviews |

---

## Related Notes

- [[Book I - The Constitution]]
- [[Book II - Governance Framework]]
- [[Institutional Registry]]
- [[Research Governance Protocol]]
- [[Knowledge Integrity]]
- [[LUMIAION Charter]]
- [[ADR Template]]
- [[Concept Note Template]]

---

## Open Questions

- [ ] Who are the founding members of the Ethics Council? This is the most critical unfilled position in the governance system.
- [ ] Should the Ethics Council publish an annual public report on the Foundation's ethical posture?
- [ ] What is the process for removing an Ethics Council member who is not fulfilling their responsibilities?
- [ ] Should the Ethics Council have the authority to trigger a constitutional convention — a structured process for reviewing the entire Constitution — after a significant number of years?
- [ ] How should the Ethics Council handle situations where the Founder's personal values have evolved in ways that create tension with the founding documents?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Frederick Belizaire Gunville | Initial charter ratified; Ethics Council formally constituted (members pending) |
