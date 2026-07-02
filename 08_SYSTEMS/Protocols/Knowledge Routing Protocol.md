---
title: "Knowledge Routing Protocol"
aliases: ["Knowledge Routing", "KRP", "Information Flow Protocol"]
tags: [protocol, knowledge, routing, systems, infrastructure, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["Founder", "Alpha Proxima Foundation"]
---

# Knowledge Routing Protocol

## Purpose

This Protocol defines how knowledge moves within the Alpha Proxima Foundation — between systems, between departments, between sessions, and between AI engines. It answers: *when knowledge is created, where does it go, how does it get there, and who is responsible?*

---

## Context

Knowledge routing is the infrastructure problem beneath every knowledge management problem. Great knowledge systems fail not because the knowledge is absent but because it never reaches the place it was needed.

Alpha Proxima's architecture spans multiple systems ([[Obsidian Vault]], GitHub, future vector databases, future local infrastructure), multiple AI engines, and multiple departments. Without a clear routing protocol, knowledge created in one context never finds the decision being made in another.

This Protocol is enforced operationally by [[LUMIAION Charter|LUMIAION]] and [[JERANIUM Charter|JERANIUM]]. It is governed by the Engineering Council and approved by the Chief Knowledge Architect.

---

## Core Content

### The Four Knowledge Flows

All knowledge movement within Alpha Proxima falls into one of four flows:

---

**Flow 1 — Creation → Vault**

*Every significant knowledge creation event ends with a Vault note.*

| Event | Responsible Party | Vault Destination |
|-------|------------------|-------------------|
| Multi-department synthesis | LUMIAION | Appropriate domain folder |
| Research finding | JERANIUM | `07_RESEARCH/` |
| Decision rationale | Founder / LUMIAION | `04_DECISIONS/` (as ADR) |
| Proposal | Any participant | `05_PROPOSALS/` (as Concept Note) |
| Project output | Project lead | `06_PROJECTS/[Project Name]/` |
| System change | Engineering Council | `08_SYSTEMS/` |

*Knowledge that does not reach the Vault is not institutional knowledge. It is lost.*

---

**Flow 2 — Vault → Session Context**

*Before beginning any substantive work session, relevant Vault content is provided as context.*

LUMIAION is responsible for identifying and surfacing the relevant Vault notes at the beginning of each session. This is what substitutes for persistent memory across sessions.

**Standard context package for a working session:**

| Content | Source |
|---------|--------|
| This session's domain (health? finance? research?) | Founder instruction |
| Relevant department charter | `03_AI_COUNCIL/Departments/` |
| Relevant ADRs and decisions | `04_DECISIONS/` |
| Relevant project notes | `06_PROJECTS/` |
| Constitutional provisions if governance is involved | `00_CONSTITUTION/` |
| Open questions from prior sessions in this domain | Vault search |

This package is assembled by LUMIAION at session start and discarded at session end. The Vault is the persistent record; the session is the working surface.

---

**Flow 3 — Department → LUMIAION → Synthesis**

*Inter-department knowledge flows through LUMIAION only.*

As defined in [[Communication Protocol]], departments do not exchange knowledge directly. JERANIUM may provide research directly to specialist departments as an operational exception, but final synthesis always routes through LUMIAION.

This ensures:
- No knowledge is presented to the Founder without synthesis
- Conflicting department outputs are surfaced and resolved before the Founder receives them
- The synthesis layer preserves institutional coherence

---

**Flow 4 — Vault → Future Systems**

*As Alpha Proxima's infrastructure evolves, the Vault feeds future systems.*

| Future System | What it Receives from Vault | When |
|--------------|----------------------------|------|
| Vector Database | All canonicalised Vault notes, chunked and embedded for semantic search | Phase 2 |
| Home Server | Full Vault mirror + private infrastructure | Phase 3 |
| LUMIAION local memory | Session-persistent context derived from Vault | Phase 2–3 |

**Design principle:** The Vault is always the source of truth. Future systems are derived views of the Vault, not replacements for it. Any system that cannot be reconstructed from the Vault is a dependency risk.

---

### Knowledge Routing Rules

**Rule 1 — Single Source of Truth**
Every piece of institutional knowledge has exactly one canonical home in the Vault. Links from other notes point to it; they do not duplicate it.

**Rule 2 — Freshness Responsibility**
When a Vault note becomes outdated, JERANIUM flags it. The responsible department or LUMIAION updates it. Outdated notes that cannot be updated are archived in `99_ARCHIVE/`, not deleted.

**Rule 3 — Pull Before Creating**
Before creating a new Vault note, check whether a note already exists for this content. JERANIUM is responsible for maintaining awareness of what already exists. Duplication degrades the knowledge graph.

**Rule 4 — Link on Creation**
Every new Vault note must link to at least one existing note. Isolated notes are a routing failure — they cannot be found through the knowledge graph.

**Rule 5 — Route Research Requests to JERANIUM**
Any request that requires searching, synthesising, or retrieving external knowledge routes to [[JERANIUM Charter|JERANIUM]] first. JERANIUM then provides the knowledge base from which specialists operate.

**Rule 6 — Constitutional Knowledge Routes to LUMIAION**
Any question involving governance, constitutional interpretation, or institutional process routes to LUMIAION directly, regardless of domain overlap.

---

### Information Architecture

```
External World
      ↓ (via JERANIUM research, department inputs, Founder observation)
Raw Information
      ↓ (evaluation, quality assessment, synthesis)
Institutional Knowledge
      ↓ (committed to Vault with proper metadata, links, structure)
Canonical Vault Note
      ↓ (available as session context, searchable, linkable)
Active Working Memory (session)
      ↓ (synthesised by LUMIAION, delivered to Founder)
Decision or Action
      ↓ (documented as ADR or logged)
Decision Record (Vault)
```

The cycle is complete when a decision is documented. Undocumented decisions are knowledge that has escaped the system.

---

### Synchronisation Philosophy

Alpha Proxima currently operates with one canonical knowledge store: the Obsidian Vault, version-controlled in GitHub.

**Synchronisation principles:**
- The Vault is always the master; all other systems derive from it
- GitHub is the engineering memory; it tracks *changes* to the Vault over time
- No knowledge is created directly in GitHub — it flows through the Vault
- Future systems (Notion Mission Control, Vector Database) receive knowledge from the Vault, not from each other

**Synchronisation frequency:**
- Vault → GitHub: On every meaningful note creation or edit (via Obsidian Git)
- Vault → Future Vector Database: Triggered on Vault commit; batch sync acceptable
- Vault → Session context: At start of each working session

---

## Related Notes

- [[Knowledge Ownership Protocol]]
- [[Decision Routing Protocol]]
- [[Communication Protocol]]
- [[LUMIAION Charter]]
- [[JERANIUM Charter]]
- [[Foundational Architecture]]
- [[Book II - Governance Framework]]

---

## Open Questions

- [ ] What is the minimum size/significance threshold for creating a Vault note versus leaving knowledge in session?
- [ ] How should LUMIAION handle knowledge created in a session that the Founder explicitly does not want committed to the Vault?
- [ ] When the Vector Database is built (Phase 2), should the Vault remain the canonical source or can the Vector DB become co-canonical?
- [ ] Should there be a scheduled "knowledge review" session — JERANIUM auditing the Vault for freshness and completeness?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder | Initial protocol established |
