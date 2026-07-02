---
title: "Foundational Architecture"
aliases: ["Foundational Architecture", "Knowledge Infrastructure", "Execution Infrastructure", "Technical Architecture"]
tags: [systems, architecture, infrastructure, knowledge, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["Founder", "Alpha Proxima Foundation"]
---

# Foundational Architecture

## Purpose

This document describes the complete technical and knowledge infrastructure of the Alpha Proxima Foundation — what systems exist, what role each plays, how information flows between them, and how the architecture evolves toward institutional sovereignty.

This is the Engineering Council's primary reference document. It is updated whenever a material infrastructure change is made via a Class III ADR.

---

## Context

Architecture is the set of decisions that are expensive to reverse. Alpha Proxima's architecture must therefore be designed with the long view: not for current convenience, but for a 20-year trajectory toward a Foundation that is independent of any single vendor, provider, or technology generation.

The design principle that governs every architectural decision: **no single point of failure may be allowed in the knowledge or intelligence layer**. Providers will change. Models will be deprecated. Services will be acquired. The institution must survive all of it.

---

## Core Content

### Current Architecture — Phase 1

```
┌─────────────────────────────────────────────────────────┐
│                  FOUNDER / ALPHA PROXIMA                │
└─────────────────────────────────────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │   LUMIAION  │  Constitutional Intelligence Core
                    │  (Claude)   │  Orchestration + Memory
                    └──────┬──────┘
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     [SOHMA]          [ATHENA]         [VORTEX]
  (Consciousness)     (Health)         (Finance)
          └────────────────┼────────────────┘
                           ▼
                      [JERANIUM]
                      (Research)
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   ┌─────────────┐  ┌────────────┐  ┌─────────────┐
   │ Obsidian    │  │   GitHub   │  │  AI Provider│
   │   Vault     │  │   Repo     │  │    APIs     │
   │(Canonical   │  │(Engineering│  │(Claude,GPT, │
   │ Knowledge)  │  │  Memory)   │  │Gemini, etc.)│
   └─────────────┘  └────────────┘  └─────────────┘
```

---

### System Registry — Current

---

#### System 1 — Obsidian Vault
**Role:** Canonical Knowledge Store  
**Status:** Active  
**Owner:** Chief Knowledge Architect (Anthropic Claude / LUMIAION)  
**Location:** `/Users/Fred/Documents/Obsidian Vault` (local Mac) + GitHub mirror  
**Technology:** Obsidian (Markdown-based knowledge management)

**What it holds:**
- All constitutional documents
- All institutional charters and registries
- All ADRs and Concept Notes
- All research, project, and systems documentation
- The knowledge graph connecting all of the above

**Design principles:**
- Plain Markdown only — no proprietary formats, no vendor lock-in
- Every note is human-readable without any software
- Git-versioned — every change is tracked and reversible
- Cross-linked — knowledge is connected, not siloed

**Failure mode:** If Obsidian as a product were discontinued, the Vault survives as a folder of `.md` files readable by any text editor. This is by design.

---

#### System 2 — GitHub Repository
**Role:** Engineering Memory  
**Status:** Active  
**Owner:** Chief Engineering Architect (DeepSeek)  
**Repository:** `omsadhiguru/alpha.proxima.core-`  
**Technology:** Git / GitHub

**What it holds:**
- Version history of every Vault change
- Engineering infrastructure code (future: APIs, automation, integrations)
- CI/CD pipelines (future)
- Change record for institutional memory evolution

**Design principles:**
- The Vault is the content; GitHub is the version control
- Nothing is created directly in GitHub — it mirrors Vault changes
- Branch protection for `main` — all changes go through pull request process for significant commits
- Public by default for constitutional and charter documents; private for strategic and financial content

**Sync mechanism:** Obsidian Git plugin (local Mac → GitHub on commit)

---

#### System 3 — AI Provider APIs
**Role:** Intelligence Execution Layer  
**Status:** Active  
**Owner:** AI Council (each engine owned by its Chief Architect role)  
**Technology:** Multiple provider APIs (see [[Engine Registry]])

**What it holds:**
- No persistent knowledge (by design — this is why the Vault exists)
- Active reasoning capability
- Tool use and function calling capability (for future integrations)

**Design principles:**
- Providers are interchangeable — the role persists when the engine changes
- No institutional knowledge is stored inside a provider — it always flows to the Vault
- Redundancy: multiple providers ensure no single provider failure disables the Foundation
- Data minimisation: share only what the engine needs for the current task

**Failure mode:** If any provider API goes down, other providers can cover most functions. If all external providers fail, the Vault and its knowledge remain intact.

---

### Future Architecture — Phase 2 (Target: 1–3 Years)

```
┌─────────────────────────────────────────────────────────┐
│                  FOUNDER / ALPHA PROXIMA                │
└─────────────────────────────────────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │   LUMIAION  │  + Persistent Cross-Session Memory
                    │  (Claude +  │  via Vector Database
                    │Local Memory)│
                    └──────┬──────┘
                           │
   ┌────────────┬───────────┼───────────┬────────────┐
   ▼            ▼           ▼           ▼            ▼
[SOHMA]    [ATHENA]    [VORTEX]    [JERANIUM]   [Chief Memory
                                                 Architect]
                                                      │
                                              ┌───────▼────────┐
                                              │ Vector Database│
                                              │(Semantic Memory│
                                              │  + Retrieval)  │
                                              └───────┬────────┘
                                                      │
   ┌──────────────────────────────────────────────────┘
   ▼
┌─────────────┐  ┌────────────┐  ┌──────────────┐  ┌──────────┐
│ Obsidian    │  │   GitHub   │  │   Notion     │  │  Future  │
│   Vault     │  │   Repo     │  │(Mission Ctrl)│  │   APIs   │
└─────────────┘  └────────────┘  └──────────────┘  └──────────┘
```

**Phase 2 additions:**
- **Vector Database** — semantic search across full institutional memory; persistent context for LUMIAION
- **Notion Mission Control** — operational project management, separate from canonical knowledge (Vault) and engineering memory (GitHub)
- **Future APIs** — institutional connectivity layer; programmatic access to Alpha Proxima intelligence

---

### Future Architecture — Phase 3 (Target: 3–7 Years)

```
┌─────────────────────────────────────────────────────────┐
│                    ALPHA PROXIMA FOUNDATION             │
└─────────────────────────────────────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │   LUMIAION  │  Running on Private Infrastructure
                    │  (Local +   │  External providers: supplementary only
                    │  External)  │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    [Private Compute]  [Local Models]  [External APIs]
    (Home Server)     (Open-Weight)    (Supplementary)
           │
   ┌───────┴────────┐
   │  Full Knowledge│
   │  Infrastructure│
   │  (Vault + Vector│
   │  DB + Archive) │
   └────────────────┘
```

**Phase 3 characteristics:**
- LUMIAION runs primarily on private, locally-operated infrastructure
- External AI providers are supplementary, not primary
- Full memory sovereignty — no institutional knowledge leaves the Foundation's infrastructure without governance approval
- Chief Memory Architect role fully operational

---

### Information Flow Summary

| Flow | From | To | Trigger | Responsible |
|------|------|----|---------|-------------|
| Knowledge creation | Any session | Obsidian Vault | Significant insight or decision | LUMIAION / JERANIUM |
| Version control | Obsidian Vault | GitHub | On Vault commit | Obsidian Git plugin |
| Session context | Obsidian Vault | AI session | Session start | LUMIAION |
| Research retrieval | External world | JERANIUM → Vault | Research request | JERANIUM |
| Department synthesis | All departments | LUMIAION → Founder | Per [[Communication Protocol]] | LUMIAION |
| Semantic index (Phase 2) | Obsidian Vault | Vector Database | On Vault commit | Chief Memory Architect |

---

### Ownership Philosophy

| Layer | Owner | Principle |
|-------|-------|-----------|
| Knowledge content | Alpha Proxima Foundation | See [[Knowledge Ownership Protocol]] |
| Vault structure | Chief Knowledge Architect | Governed by [[Vault Structure Convention]] |
| GitHub repository | Chief Engineering Architect | Engineering Council authority |
| AI engines | No one — they are tools | Engines are accountable; they are not owners |
| Infrastructure (Phase 3) | Alpha Proxima Foundation | Complete sovereignty target |

---

## Related Notes

- [[Knowledge Routing Protocol]]
- [[Knowledge Ownership Protocol]]
- [[Communication Protocol]]
- [[Decision Routing Protocol]]
- [[Engine Registry]]
- [[AI Council Registry]]
- [[Future Expansion Protocol]]
- [[Vault Structure Convention]]
- [[Book II - Governance Framework]]

---

## Open Questions

- [ ] When should Phase 2 (Vector Database) development begin? What milestone triggers it?
- [ ] What hardware specifications are appropriate for the Phase 3 home server?
- [ ] Should Notion Mission Control (Phase 2) be a separate Obsidian vault or a third-party tool?
- [ ] How should the Foundation handle a situation where a critical provider API undergoes unexpected pricing changes or access restrictions?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | Founder | Initial architecture documented; Phase 1 current state; Phase 2 and 3 roadmap established |
