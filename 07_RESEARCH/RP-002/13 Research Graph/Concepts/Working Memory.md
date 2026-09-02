---
title: "Concept — Working Memory"
aliases: ["Working Memory", "Short-Term Memory"]
tags: [concept, rp-002, working-memory, memory, cognitive-science, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
research_program: "RP-002 Atlas of Human Memory"
---

# Concept Note — Working Memory

---

## Canonical Definition

**Working memory** is a temporary, capacity-limited system for actively maintaining and manipulating information in service of current cognitive goals [C-009]. It is the interface between perception and long-term memory — only information held in working memory has opportunity for encoding into long-term memory. Attention is the gate.

---

## Architecture (Baddeley Model)

| Component | Function | Neural Substrate |
|-----------|---------|-----------------|
| **Central Executive** | Attentional control, task switching, inhibition | dlPFC + FPCN |
| **Phonological Loop** | Verbal/auditory information maintenance | Left perisylvian cortex |
| **Visuospatial Sketchpad** | Visual/spatial information maintenance | Right parietal / occipital |
| **Episodic Buffer** | Integration of phonological and visuospatial with LTM | Hippocampus + PFC |

---

## Capacity

Classical estimate: 7 ± 2 items (Miller, 1956). Modern estimate: ~4 chunks (Cowan, 2001). The relevant unit is the "chunk" — a meaningful unit bound by prior knowledge. Expert chess players "see" board positions, not individual pieces.

**Theta-gamma coupling hypothesis [E-005]:** Capacity may be mechanistically constrained by the number of gamma cycles (30-100 Hz) that can be phase-amplitude coupled within each theta cycle (4-8 Hz). This would make the ~4-item limit a direct consequence of oscillatory architecture.

---

## Working Memory vs. Long-Term Memory

| Feature | Working Memory | Long-Term Memory |
|---------|--------------|-----------------|
| Capacity | ~4 chunks | Effectively unlimited |
| Duration | Seconds (without rehearsal) | Years to decades |
| Access | Immediately available | Requires retrieval |
| Neural substrate | PFC + FPCN | MTL + distributed neocortex |
| Manipulation | Active, flexible | Retrieved, reconstructed |

---

## AI Analogue

The context window in large language models is the closest analogue to working memory: capacity-limited, session-scoped, immediately accessible, lost at reset. Like biological working memory, the context window is the interface — only information in the context window can be processed and potentially written to external memory.

---

## Related Concepts

- [[Memory]] — memory overview
- [[Hippocampus]] — episodic buffer; encoding from WM to LTM
- [[Pattern Separation and Completion]] — how WM contents are distinguished and completed

---

## Evidence Classification

C-009, E-005 — see [[12 Evidence Registry/RP-002 Evidence Registry]]
