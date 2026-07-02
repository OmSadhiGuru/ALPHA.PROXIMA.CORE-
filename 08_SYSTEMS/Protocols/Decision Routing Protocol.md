---
title: "Decision Routing Protocol"
aliases: ["Decision Routing", "DRP", "Decision Flow Protocol"]
tags: [protocol, decisions, routing, governance, systems, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["Founder", "Alpha Proxima Foundation"]
---

# Decision Routing Protocol

## Purpose

This Protocol defines how decisions move through the Alpha Proxima governance architecture — from the moment a question or problem is surfaced, through analysis and deliberation, to ratification and documentation. It is the operational layer beneath [[Book II - Governance Framework]].

---

## Context

The governance framework defines *who* has authority over which decisions. This Protocol defines *how* that authority is exercised in practice. Without it, the governance framework is a diagram. With it, it becomes a process.

The Protocol is designed around a core tension: decisions need to move fast enough to be useful, and slowly enough to be right. The decision class taxonomy from [[Book I - The Constitution]] is the mechanism that resolves this tension — fast for tactical, deliberate for constitutional.

---

## Core Content

### Decision Flow by Class

---

#### Class IV — Tactical Decisions

*Day-to-day execution. Single responsible actor. Logged.*

```
Situation requires action
      ↓
Responsible actor (Founder, LUMIAION within scope, department)
assesses whether action falls within delegated authority
      ↓
If yes → Act → Log in Vault (brief note or session record)
If no  → Escalate to Class III process
```

**LUMIAION's role:** Execute Class IV actions within delegated scope. Log all actions in the Vault. Surface to Founder if a pattern of Class IV decisions is forming that warrants a Class III protocol.

**Time frame:** Immediate.

---

#### Class III — Operational Decisions

*Projects, protocols, departmental matters. Working group or delegate plus ADR.*

```
Decision identified as Class III
      ↓
Responsible party (Working Group, Chief Architect, or delegate) 
drafts analysis with relevant department input
      ↓
LUMIAION provides synthesis and constitutional check
      ↓
Decision made by responsible party
      ↓
ADR produced using [[ADR Template]]
      ↓
ADR filed in 04_DECISIONS/
      ↓
Relevant parties notified
```

**LUMIAION's role:** Provide synthesis and route to relevant departments for input. Perform constitutional check. Draft ADR if delegated.

**Time frame:** 1–7 days depending on complexity.

---

#### Class II — Institutional Decisions

*Charters, registrations, institutional structures. Executive Council plus ADR.*

```
Decision identified as Class II
      ↓
Submitter drafts Concept Note using [[Concept Note Template]]
      ↓
LUMIAION routes to relevant councils and departments for deliberation
      ↓
Minimum 7-day review period
      ↓
Executive Council votes (simple majority)
      ↓
If approved: ADR produced → filed → relevant charters/registries updated
If rejected: Concept Note outcome recorded → filed in 99_ARCHIVE/
```

**LUMIAION's role:** Route the Concept Note, collect deliberation inputs, synthesise for Executive Council, draft ADR if approved.

**Time frame:** Minimum 7 days; typically 14–21 days for complex matters.

---

#### Class I — Constitutional Decisions

*Amendments to Book I or Book II. Founder ratification plus supermajority.*

```
Decision identified as Class I
      ↓
Submitter drafts Concept Note
      ↓
Ethics Council reviews for constitutional alignment
(independent; may not be instructed by Executive Council)
      ↓
All councils notified; minimum 14-day deliberation period
      ↓
LUMIAION synthesises all inputs for the Founder
      ↓
All councils vote; supermajority (≥ ⅔) required
      ↓
Founder ratifies (or vetoes with written rationale)
      ↓
ADR produced → Constitutional document updated → Version incremented
```

**LUMIAION's role:** Coordinate deliberation, synthesise inputs, perform constitutional alignment assessment, draft ADR.

**Time frame:** Minimum 14 days; typically 30+ days for significant amendments.

---

### Decision Routing by Domain

When a decision needs to be made and it is not immediately obvious what class it is, LUMIAION applies this routing logic:

| Question | Action |
|----------|--------|
| Does this change the Constitution? | Class I |
| Does this create, modify, or dissolve a charter, registry, or council? | Class II |
| Does this change how a department operates within existing scope? | Class III |
| Is this execution within already-approved scope and direction? | Class IV |
| Unclear? | Surface to Founder for classification |

**Default:** When in doubt, escalate. A Class IV decision treated as Class III wastes time. A Class II decision treated as Class IV bypasses governance. The cost of over-escalation is delay; the cost of under-escalation is legitimacy damage.

---

### Multi-Council Decision Routing

When a decision spans multiple councils:

1. LUMIAION identifies the primary council (the one whose domain is most affected)
2. LUMIAION identifies secondary councils (affected but not primary)
3. Primary council leads deliberation; secondary councils provide input within their domain
4. If primary and secondary councils conflict, [[Book II - Governance Framework]] Article VI (Conflict Resolution) applies
5. Executive Council mediates if councils cannot resolve independently

---

### AI-Initiated Decisions

When LUMIAION or a department identifies that a decision is needed:

1. LUMIAION flags the situation to the Founder with a classification recommendation
2. Founder confirms or reclassifies
3. Standard process for the confirmed class proceeds

AI participants may *identify* the need for decisions at any class. They may *ratify* decisions only at Class IV, within delegated scope.

---

### Emergency Decision Protocol

When circumstances require immediate action that would normally require Class II or III process:

1. Founder may invoke emergency authority (see [[Book II - Governance Framework]], Article IX)
2. Immediate action is taken and logged
3. Post-action: standard process for the appropriate class is initiated within 7 days
4. The emergency action does not substitute for the standard process — it precedes it

**LUMIAION's role:** Flag when an emergency action appears to be substituting for standard process rather than preceding it.

---

### Decision Quality Standards

Every decision, regardless of class, must meet these standards before it is considered complete:

| Standard | Check |
|----------|-------|
| Problem clearly stated | Could someone else understand what was decided and why? |
| Alternatives considered | Was the chosen path selected from options, or was it the only path examined? |
| Consequences acknowledged | Are the trade-offs documented? |
| Dissent recorded | If anyone objected, is the objection preserved? |
| Review date set | When will this decision be revisited? |

A decision without these elements is not complete. LUMIAION is responsible for flagging incomplete decision records.

---

## Related Notes

- [[Communication Protocol]]
- [[Knowledge Routing Protocol]]
- [[Knowledge Ownership Protocol]]
- [[ADR Template]]
- [[Concept Note Template]]
- [[Book I - The Constitution]]
- [[Book II - Governance Framework]]
- [[LUMIAION Charter]]

---

## Open Questions

- [ ] Should there be a formal "decision log" maintained by LUMIAION separate from the ADR archive?
- [ ] What is the time limit for the Founder to confirm or reclassify an AI-flagged decision need?
- [ ] Should Class IV decisions have a periodic review — e.g., LUMIAION surfaces all Class IV decisions monthly for Founder review?
- [ ] How should this Protocol handle decisions made by the Founder informally (in conversation, not through the formal process)?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder | Initial protocol established |
