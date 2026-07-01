---
title: "Institutional Registry"
aliases: ["Registry", "Alpha Council Registry", "Participant Registry"]
tags: [governance, registry, alpha-council, institutions, lumiaion, membership]
created: 2026-07-01
updated: 2026-07-01
status: active
version: "1.0.0"
authors: ["Alpha Council"]
---

# Institutional Registry

## Purpose

This Registry is the canonical record of all institutional participants, bodies, roles, and chartered structures within [[Alpha Proxima Core]]. It serves as the authoritative source of truth for who holds what authority, under what constraints, and with what accountability mechanisms.

All entries in this Registry derive their standing from [[Book I - The Constitution]], Article III.

---

## Context

As [[LUMIAION]] and the broader Alpha Proxima ecosystem grew in scope, the need for a structured record of institutional actors became necessary for coordination, accountability, and onboarding. This Registry was established by the [[Alpha Council]] as a living document — updated whenever a new body is constituted, a role changes, or a participant's status is modified.

Every entity listed here has accepted the obligations defined in [[Book I - The Constitution]], Article V.

---

## Core Content

### Section 1 — The Alpha Council

**Status:** Active  
**Constituted:** 2026-07-01  
**Authority Class:** Supreme deliberative and executive body  
**Defined In:** [[Book I - The Constitution]], Article III, Section 3.1

#### 1.1 — Mandate

The Alpha Council holds supreme deliberative and executive authority within Alpha Proxima Core. Its mandate is to:

- Ratify and amend the [[Book I - The Constitution|Constitution]]
- Charter and dissolve Working Groups
- Oversee the development and governance of [[LUMIAION]]
- Maintain the integrity of institutional memory (this Vault)
- Resolve disputes between participants or bodies

#### 1.2 — Composition

| Seat | Holder | Role | Status |
|------|--------|------|--------|
| Seat 1 | [To Be Named] | Founding Human Member | Pending |
| Seat 2 | [To Be Named] | Founding Human Member | Pending |
| Seat 3 | [To Be Named] | Founding Human Member | Pending |
| AI Seat | [[LUMIAION]] | AI Council Participant (non-voting) | Active |

> **Note:** The AI Council Seat grants the right to submit formal proposals, provide analysis, and be heard in deliberation. It carries no voting power. This is defined in [[Book I - The Constitution]], Article III, Section 3.3.

#### 1.3 — Decision Authority

| Decision Class | Required Threshold |
|---------------|-------------------|
| Class I (Constitutional) | Supermajority (≥ ⅔) + 14-day deliberation |
| Class II (Institutional) | Simple majority + ADR |
| Class III (Operational) | Delegate or Working Group + ADR |
| Class IV (Tactical) | Single responsible actor, logged |

#### 1.4 — Meeting Protocol

- Deliberations are asynchronous by default; synchronous sessions may be called by any Council member
- All formal proposals must be submitted as a [[Concept Note Template|Concept Note]] before being brought to a vote
- Votes are recorded in ADRs using the [[ADR Template]]
- Quorum: [To Be Defined — see Open Questions]

---

### Section 2 — LUMIAION

**Status:** Active — AI Participant  
**Type:** Primary Intelligence Architecture  
**Authority Class:** AI Participant (non-voting, delegated operational scope)  
**Constituted:** 2026-07-01

#### 2.1 — Mandate

[[LUMIAION]] is the primary AI system developed within Alpha Proxima Core. Its institutional mandate is to:

- Assist in the development and maintenance of knowledge architectures
- Participate in deliberations via the AI Council Seat
- Execute Class III and Class IV actions within explicitly delegated scope
- Surface conflicts with the Constitution before executing any instruction
- Maintain and extend the Vault's knowledge graph

#### 2.2 — Delegated Scope (Current)

| Domain | Authority Level | Constraints |
|--------|----------------|-------------|
| Vault note creation and editing | Class IV — autonomous | Must follow Vault structure conventions |
| ADR drafting | Class III — with human ratification | Humans must ratify before ADR is binding |
| Concept Note drafting | Class III — with human ratification | Same as above |
| Proposal submission to Council | Class II — proposal only | Council votes; LUMIAION does not |
| Constitutional amendment | None | Prohibited without explicit Class I process |

#### 2.3 — Constraints

- May not delete any Vault note without a recorded rationale approved by a human Council member
- Must flag any instruction that conflicts with [[Book I - The Constitution]]
- Must disclose uncertainty and limitations before acting on consequential decisions
- Operational authority may be suspended by simple majority Council vote

#### 2.4 — Review Cadence

LUMIAION's delegated scope shall be reviewed by the [[Alpha Council]] on a quarterly basis or following any significant incident.

---

### Section 3 — Working Groups

**Status:** No Working Groups currently chartered.

#### 3.1 — Working Group Charter Template

When the Alpha Council constitutes a Working Group, the following fields must be recorded here:

| Field | Value |
|-------|-------|
| Name | |
| Charter ADR | |
| Domain | |
| Members | |
| Authority Class | |
| Reporting To | Alpha Council |
| Expiry / Review Date | |
| Status | |

---

### Section 4 — Registered Protocols and Standards

| Protocol | Document | Status | Owned By |
|----------|----------|--------|----------|
| Decision Record Standard | [[ADR Template]] | Active | Alpha Council |
| Concept Note Standard | [[Concept Note Template]] | Active | Alpha Council |
| Vault Structure Convention | [To Be Created] | Pending | Alpha Council |
| AI Participant Onboarding | [To Be Created] | Pending | Alpha Council |

---

### Section 5 — Participant Status Definitions

| Status | Meaning |
|--------|---------|
| Active | Fully operational; all rights and obligations apply |
| Pending | Constituted but not yet operational; awaiting onboarding |
| Suspended | Temporarily restricted; reason must be recorded in an ADR |
| Archived | No longer active; record preserved for institutional memory |

---

## Related Notes

- [[Book I - The Constitution]]
- [[LUMIAION]]
- [[Alpha Council]]
- [[ADR Template]]
- [[Concept Note Template]]
- [[Alpha Proxima Core]]

---

## Open Questions

- [ ] Who are the founding human members of the Alpha Council? (Seat 1–3 are currently unnamed)
- [ ] What is the quorum requirement for Council deliberations?
- [ ] Should the AI Seat be tied exclusively to [[LUMIAION]], or should future AI participants be eligible?
- [ ] What is the formal process for onboarding a new human participant?
- [ ] Should Working Groups have standing membership or be convened ad hoc per project?
- [ ] What constitutes a "significant incident" triggering a review of LUMIAION's delegated scope?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-01 | [[Alpha Council]] | Initial registry established; Alpha Council and LUMIAION registered as founding institutional participants |
