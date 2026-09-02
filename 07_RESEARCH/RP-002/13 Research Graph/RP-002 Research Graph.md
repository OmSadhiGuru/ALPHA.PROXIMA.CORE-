---
title: "RP-002 Research Graph"
aliases: ["RP-002 Graph", "Memory Knowledge Graph", "Atlas of Human Memory Graph"]
tags: [research, rp-002, memory, graph, knowledge-map, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["LUMIAION"]
research_program: "RP-002 Atlas of Human Memory"
---

# RP-002 — Research Graph

---

## Purpose

This document maps the conceptual structure of RP-002 — how the major domains, frameworks, and concepts relate to each other. It is a navigational and analytical tool: it shows where the program has coverage, where gaps remain, and how any new concept note or research finding should connect to existing knowledge.

---

## Domain Map

RP-002 covers memory across five levels of analysis, each supported by concept notes and evidence:

```
┌──────────────────────────────────────────────────────────────────────┐
│                    ATLAS OF HUMAN MEMORY — RP-002                    │
└────────────────────────┬─────────────────────────────────────────────┘
                         │
     ┌───────────────────┼──────────────────────────┐
     │                   │                          │
     ▼                   ▼                          ▼
┌──────────────┐  ┌─────────────────┐  ┌───────────────────────────┐
│  MOLECULAR / │  │  SYSTEMS /      │  │  HUMAN / CULTURAL /       │
│  CELLULAR    │  │  COGNITIVE      │  │  INSTITUTIONAL            │
└──────┬───────┘  └────────┬────────┘  └──────────────┬────────────┘
       │                   │                           │
  LTP/Plasticity      Hippocampus              Collective Memory
  Reconsolidation     Pattern Sep/Comp          Trauma Memory
  Engram              Working Memory            Contemplative Memory
                      Memory (overview)
```

---

## Concept Note Index

| Concept | Domain | Key Evidence | File |
|---------|--------|-------------|------|
| Memory | Overview / Cross-domain | C-001, C-004–C-006, C-008, C-010 | [[Concepts/Memory]] |
| Hippocampus | Cellular / Systems | C-003, C-007, M-001, E-003 | [[Concepts/Hippocampus]] |
| LTP / Synaptic Plasticity | Molecular / Cellular | C-002, M-003, E-002, S-003 | [[Concepts/LTP - Synaptic Plasticity]] |
| Reconsolidation | Molecular / Therapeutic | C-001, C-008, Q-004, S-005 | [[Concepts/Reconsolidation]] |
| Working Memory | Cognitive / Systems | C-009, E-005 | [[Concepts/Working Memory]] |
| Engram | Molecular / Open Frontier | Q-001 | [[Concepts/Engram]] |
| Pattern Separation and Completion | Circuit / Computational | C-007, E-003, M-004 | [[Concepts/Pattern Separation and Completion]] |
| Collective Memory | Cultural / Institutional | C-010, DOC-B anthropology | [[Concepts/Collective Memory]] |
| Trauma Memory | Clinical / Therapeutic | C-006, Q-004, P-002 | [[Concepts/Trauma Memory]] |
| Contemplative Memory | Phenomenological / Speculative | E-004, P-001, S-005 | [[Concepts/Contemplative Memory]] |

---

## Concept Relationship Map

Key relationships between concept notes — how they connect in the knowledge graph:

```
Memory (overview) ←──────────── all concepts link here
    │
    ├── Molecular Level
    │       ├── LTP / Synaptic Plasticity ──→ Hippocampus
    │       │       └── Engram (what LTP encodes)
    │       └── Reconsolidation ──→ LTP (restabilization mechanism)
    │               └── Trauma Memory (reconsolidation disrupted)
    │               └── Contemplative Memory (reconsolidation facilitation?)
    │
    ├── Circuit Level
    │       └── Hippocampus ──→ Pattern Separation and Completion
    │               └── Engram (hippocampus as engram site)
    │               └── Working Memory (episodic buffer)
    │
    ├── Cognitive Level
    │       └── Working Memory ──→ Memory (gateway to LTM)
    │
    └── Cultural / Institutional Level
            └── Collective Memory ──→ Memory (social constitution)
                    └── Trauma Memory (collective trauma)
                    └── Contemplative Memory (deconditioning tradition)
```

---

## Coverage Assessment

### Well-Covered Domains

- Molecular neuroscience (LTP, reconsolidation, engram)
- Hippocampal circuit computation (trisynaptic, pattern separation/completion)
- Cognitive psychology (working memory, declarative memory systems)
- Interdisciplinary breadth (10 disciplines via DOC-B)

### Partial Coverage

- Oscillatory dynamics (covered in Canonical Synthesis and LTP note; no dedicated concept note)
- Glial coupling / tripartite synapse (covered in Evidence Registry; no dedicated concept note)
- AI memory architecture (covered in Canonical Synthesis Ch. 9; no dedicated concept note — candidate for RP-002 Phase 2)

### Coverage Gaps

- No concept note for: Theta-Gamma Coupling; Glial Coupling; Sleep and Consolidation; AI Memory Architecture; Adult Neurogenesis; Schema Integration
- These gaps are candidates for Phase 2 concept note development

---

## Cross-Program Connections

RP-002 connects to other Alpha Proxima programs at these nodes:

| Connection | RP-002 Concept | Connected Program |
|-----------|---------------|-----------------|
| Working memory ↔ Global Workspace | Working Memory | [[07_RESEARCH/RP-001/13 Research Graph/Concepts/Global Neuronal Workspace Theory]] |
| Episodic memory ↔ consciousness | Memory, Hippocampus | [[07_RESEARCH/RP-001/13 Research Graph/Concepts/Consciousness]] |
| Default Mode Network ↔ autobiographical memory | Collective Memory (self-constitution) | [[07_RESEARCH/RP-001/13 Research Graph/Concepts/Default Mode Network]] |
| Reconsolidation ↔ predictive processing | Reconsolidation | [[07_RESEARCH/RP-001/13 Research Graph/Concepts/Predictive Processing]] |
| AI memory types | Working Memory, Collective Memory | [[08_SYSTEMS/The Orchestration Framework]] |

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | LUMIAION | Initial Research Graph; 10 concept notes mapped; domain structure and cross-program connections established |
