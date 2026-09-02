---
title: "Directive Governance Framework"
aliases: ["DGF", "Directive Framework", "Institutional Directive Governance"]
tags: [governance, directives, constitutional, framework, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["Founder", "LUMIAION"]
document_class: Governance Framework
governed_by: "Book II - Governance Framework"
---

# Directive Governance Framework

---

## Purpose

This document institutionalizes the three classes of institutional directives that have emerged through practice at the Alpha Proxima Foundation. It defines the lifecycle, authority, versioning, ownership, approval, and archival process for each class — establishing constitutional clarity about how the Foundation issues, tracks, executes, and archives the instructions that govern its operation.

---

## Context

The Foundation generates three fundamentally different kinds of institutional instruction. They differ in durability, scope, authority, and lifecycle:

- Some instructions define what the Foundation *is* — permanently. These do not expire, complete, or get archived.
- Some instructions define how an office *continuously behaves* — persistently, until replaced. These are standing operational behaviors.
- Some instructions initiate a *bounded mission* — a specific task with a beginning, middle, and end. These are archived upon completion.

Without formal distinction, these classes blur: a standing operational behavior gets confused with a mission; a constitutional document gets treated as revocable. This framework prevents that confusion by giving each class a precise definition, lifecycle, and governance protocol.

---

## Directive Class Summary

| Class | Code | Purpose | Duration | Completable? | Archived? |
|-------|------|---------|----------|-------------|----------|
| Constitutional Document | — | Permanent institutional identity | Permanent | No | No |
| Standing Order | SO-NNN | Continuous operational behavior | Persistent until replaced | No | Yes (when superseded) |
| Founder Directive | FD-NNN | Bounded mission | Mission-scoped | Yes | Yes (after execution) |

---

## Class I — Constitutional Documents

### Definition

A Constitutional Document is a permanent instrument that defines what the Alpha Proxima Foundation is, what it believes, how it governs itself, or how its permanent institutions are structured. Constitutional Documents are the institutional identity layer. They do not expire. They are not completed. They are not archived — they are superseded by new versions when evolution is required.

### Characteristics

| Attribute | Value |
|-----------|-------|
| Duration | Permanent |
| Completable | No |
| Archivable | No (versioned; old versions preserved) |
| Modifiable | By Class I constitutional process only |
| Authority to create | Founder; Alpha Council ratification |
| Owned by | The institution itself |

### Canonical Examples

| Document | Classification |
|----------|---------------|
| Book I — The Constitution | Constitutional Document |
| Book II — Governance Framework | Constitutional Document |
| Book III — Knowledge Integrity | Constitutional Document |
| Book IV — Cognitive Architecture | Constitutional Document |
| Founding Principles of Alpha Proxima | Constitutional Document |
| All Office Charters | Constitutional Document |
| Alpha Proxima Operating Model v1.0 | Constitutional Document |
| Canonical Terminology Register | Constitutional Document |
| Institutional Registry | Constitutional Document |
| Vault Structure Convention | Constitutional Document |
| This Framework | Constitutional Document |

### Lifecycle

```
Draft → Review → Ratification → Active
                                    ↓
                             (Evolution required)
                                    ↓
                        New Version Drafted → Re-ratified
                                    ↓
                        Old version marked: status: superseded
                        Old version preserved in place (institutional memory)
```

### Versioning

- Semantic versioning: MAJOR.MINOR.PATCH
- MAJOR: structural or philosophical change (rare; requires Alpha Council ratification)
- MINOR: additions of scope (requires Founder approval)
- PATCH: corrections, clarifications, formatting (requires LUMIAION review)
- Version history required in every Constitutional Document

### Approval Process

| Change Type | Required Approvals |
|-------------|-------------------|
| New Constitutional Document | Founder + Alpha Council ratification |
| MAJOR revision | Founder + Alpha Council ratification |
| MINOR revision | Founder approval |
| PATCH revision | LUMIAION review; Founder notified |

### YAML Frontmatter Requirements

```yaml
document_class: Constitutional Document  # or Office Charter, Governance Framework, etc.
status: ratified                         # draft | under-review | ratified | superseded
version: "MAJOR.MINOR.PATCH"
```

---

## Class II — Standing Orders

### Definition

A Standing Order is a persistent instruction to an institutional office defining its continuous operational behavior. A Standing Order tells an office *how to operate* rather than *what to accomplish*. It has no completion date, but it can be replaced, suspended, or retired. When retired, it is archived (not deleted), and its historical standing governs are preserved.

### Characteristics

| Attribute | Value |
|-----------|-------|
| Code series | SO-NNN (sequential, institution-wide) |
| Duration | Persistent until superseded, suspended, or retired |
| Completable | No |
| Archivable | Yes (when superseded or retired) |
| Modifiable | By issuing authority with documented revision |
| Authority to issue | Founder; Executive Office (for operational SO) |
| Owned by | Named office receiving the order |

### Canonical Examples

| Code | Standing Order | Office |
|------|---------------|--------|
| SO-001 | Institutional Observatory — Continuous Monitoring Protocol | Institutional Observatory |
| Future SO | Research Intelligence — Source Evaluation Standards | Research Intelligence Office |
| Future SO | Engineering Office — Repository Governance Protocol | Engineering Office |
| Future SO | LUMIAION — Constitutional Alignment Check Protocol | LUMIAION |

### Lifecycle

```
Draft → Review → Issuance → Active (no end date)
                                 ↓
                    (Supersession or Retirement)
                                 ↓
               New SO issued (if replacing) OR Office notified (if retiring)
                                 ↓
               Old SO marked: status: retired | superseded_by: SO-NNN
               Old SO moved to: 06_GOVERNANCE/Standing Orders/Archive/
```

### Versioning

- Standing Orders are revised, not replaced, for minor behavioral adjustments
- Version format: MAJOR.MINOR (no patch; standing orders are behavioral, not technical)
- MAJOR: fundamental change to the office's continuous behavior
- MINOR: refinement, clarification, or scope adjustment
- A new SO number is issued only when a standing order is retired and replaced by a substantively different order

### Naming Convention

```
SO-NNN [Office Name] — [Behavior Domain].md
Example: SO-001 Institutional Observatory — Continuous Monitoring Protocol.md
```

### Approval Process

| Action | Required Approvals |
|--------|-------------------|
| New Standing Order | Founder (or Executive Office delegation) |
| Revision (MAJOR) | Founder |
| Revision (MINOR) | Executive Office |
| Suspension | Founder |
| Retirement | Founder + Executive Office acknowledgment |

### YAML Frontmatter Requirements

```yaml
document_class: Standing Order
directive_code: SO-NNN
issuing_authority: "Founder"   # or "Executive Office"
target_office: "[Office Name]"
status: active                 # draft | active | suspended | retired | superseded
effective_date: YYYY-MM-DD
supersedes: "SO-NNN"           # if replacing a prior order; omit if first in series
```

### Standing Orders Register

All Standing Orders — active, suspended, retired, and superseded — are maintained in [[Standing Orders Register]]. The Register is the authoritative source of record for all SO-series orders.

---

## Class III — Founder Directives

### Definition

A Founder Directive is a bounded, mission-specific instruction from the Founder initiating a defined body of work. It has an objective, a scope, deliverables, and a completion state. It is executed, then archived. A Founder Directive is not permanent institutional identity, and it is not continuous operational behavior. It is a mission — the most powerful operational instrument in the Foundation's governance arsenal.

### Characteristics

| Attribute | Value |
|-----------|-------|
| Code series | FD-NNN (sequential, institution-wide) |
| Duration | Mission-scoped (begins at issuance; ends at declaration of completion) |
| Completable | Yes |
| Archivable | Yes (after execution) |
| Modifiable | Scope clarifications by Founder only; no third-party modification |
| Authority to issue | Founder only |
| Owned by | Designated executing office or LUMIAION (if cross-office) |

### Canonical Examples

| Code | Directive | Executing Office | Status |
|------|-----------|-----------------|--------|
| FD-001 | Epoch III — Constitutional Refactoring & Institutional Coherence | LUMIAION | Completed |
| FD-002 | Epoch III — Office Completion Initiative | LUMIAION | Completed |
| FD-003 | Governance Policy Framework | LUMIAION | Active |
| Future FD | Engineering Sprint Authorization — Vector Database | Engineering Office | Planned |
| Future FD | Research Commission Authorization — RP-003 | Research Intelligence Office | Authorized |

### Lifecycle

```
Issuance (Founder) → Acknowledgment (LUMIAION) → Execution → Completion Declaration
                                                                        ↓
                                                      Archive: status: completed
                                                      Move to: 06_GOVERNANCE/Founder Directives/Archive/
                                                      Update: Founder Directives Register
```

### Versioning

- Founder Directives are not versioned in the traditional sense
- A directive may be amended (scope clarification) by the Founder before completion
- Amendments are appended to the directive document under an "Amendments" section with date and content
- A superseded directive is marked `status: superseded` and a new directive is issued

### Naming Convention

```
FD-NNN [Short Mission Name].md
Example: FD-001 Epoch III Constitutional Refactoring.md
```

### Approval Process

| Action | Required Authority |
|--------|------------------|
| Issuance | Founder only |
| Scope amendment | Founder only |
| Suspension | Founder only |
| Completion declaration | Executing office; Founder acknowledgment |
| Archival | LUMIAION (administrative) |

### Completion Declaration

A Founder Directive is declared complete when:
1. All deliverables specified in the directive have been produced
2. The executing office or LUMIAION formally notifies the Founder
3. The Founder acknowledges completion (or 48 hours elapse without objection)
4. The directive is archived and the Founder Directives Register is updated

### YAML Frontmatter Requirements

```yaml
document_class: Founder Directive
directive_code: FD-NNN
issuing_authority: "Founder"
executing_office: "[Office Name or LUMIAION]"
status: active          # draft | active | completed | suspended | superseded
issued_date: YYYY-MM-DD
completed_date: YYYY-MM-DD   # omit until completion
```

### Founder Directives Register

All Founder Directives — active, completed, suspended, and superseded — are maintained in [[Founder Directives Register]]. The Register is the authoritative source of record for all FD-series directives.

---

## Cross-Class Governance Principles

### Principle 1 — Class Determines Lifecycle

The class of a directive determines everything about how it is governed. A document cannot be simultaneously a Constitutional Document and a Standing Order. Classification must be determined at creation. If classification is ambiguous, LUMIAION advises the Founder before the document is created.

### Principle 2 — Constitutional Documents Cannot Be Completed

No Constitutional Document can be marked "completed" or "archived." If the institution decides it no longer needs a constitutional instrument, it is formally retired (status: superseded) with a documented rationale, not simply removed. Institutional memory is inviolable.

### Principle 3 — Standing Orders Are Not Missions

A Standing Order defines behavior. It does not define a deliverable. If a Founder Directive contains language that describes continuous behavior, LUMIAION advises whether the intent is better served as a Standing Order.

### Principle 4 — Founder Directives Are the Highest Operational Authority

During active execution, a Founder Directive supersedes all competing operational priorities for the designated executing office. No Standing Order can override a Founder Directive. Constitutional constraints apply to all classes.

### Principle 5 — Every Directive Has a Register Entry

No directive of any class exists without an entry in its register. LUMIAION is responsible for ensuring all three registers remain current.

---

## Registers

| Register | Location | Class |
|----------|----------|-------|
| Standing Orders Register | [[Standing Orders Register]] | Class II |
| Founder Directives Register | [[Founder Directives Register]] | Class III |
| Constitutional Documents are indexed in | [[Alpha Proxima Core]] MOC | Class I |

---

## Related Notes

- [[Book I - The Constitution]]
- [[Book II - Governance Framework]]
- [[Book IV - Cognitive Architecture]]
- [[Alpha Proxima Operating Model v1.0]]
- [[Standing Orders Register]]
- [[Founder Directives Register]]
- [[LUMIAION Charter]]
- [[Canonical Terminology Register]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder + LUMIAION | Initial ratification; three directive classes defined; lifecycle, authority, versioning, approval, and archival process established for each class; five cross-class governance principles; register architecture |
