---
title: "RP-002 Theory Matrix"
aliases: ["RP-002 Theory Matrix"]
tags: [research, rp-002, theory-matrix, memory, frameworks, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["LUMIAION"]
research_program: "RP-002 Atlas of Human Memory"
---

# RP-002 — Theory Matrix

---

## Overview

This matrix maps all major theoretical frameworks identified across the RP-002 source set. Each framework is classified by domain, level of empirical support, and relationship to competing frameworks.

**Evidence classification codes:** C = Consensus · M = Competing Models · E = Emerging · Q = Open Question · S = Speculative

---

## Neuroscience Frameworks

| Framework | Proponents | Core Claim | Evidence Class | Competes With |
|-----------|-----------|-----------|----------------|---------------|
| **Hebbian Learning / LTP** | Hebb (1949); Bliss & Lømo (1973) | Neurons that fire together wire together; LTP is the cellular substrate of memory | C | Non-synaptic storage models |
| **Standard Consolidation Theory (SCT)** | Squire, Alvarez | Hippocampus required only during consolidation; memories eventually transfer to hippocampus-independent neocortical storage | M | Multiple Trace Theory |
| **Multiple Trace Theory (MTT)** | Nadel, Moscovitch (1997) | Hippocampus required for episodic memory regardless of age; only semantic memories become hippocampus-independent | M | Standard Consolidation Theory |
| **Complementary Learning Systems (CLS)** | McClelland, McNaughton, O'Reilly | Hippocampus = fast anomaly detector; neocortex = slow pattern extractor; integration via sleep replay | M | Direct schema encoding models |
| **Reconsolidation Theory** | Nader, Schafe, LeDoux (2000) | Retrieved memories enter labile state requiring protein synthesis to restabilize; defines therapeutic modification window | C | Classic consolidation (one-time event) |
| **Theta-Gamma Coupling (temporal coding)** | Lisman, Jensen; Buzsáki | Working memory items are encoded in gamma cycles nested within theta rhythm; theta organizes temporal order | E | Rate-code models of working memory |
| **Trisynaptic Circuit Model** | Ramón y Cajal; modern electrophysiology | DG (pattern separation) → CA3 (pattern completion) → CA1 (integration) → Subiculum is the hippocampal computation | C | — |
| **Synaptic Homeostasis Hypothesis (SHY)** | Tononi, Cirelli | Sleep downscales synaptic potentiation accumulated during waking; SWS is the renormalization phase | M | Replay/consolidation view of sleep |
| **Epigenetic Memory Storage** | Bhaskaran, Bhatt; multiple | DNA methylation, histone modifications, ncRNA encode experience-dependent changes persisting beyond protein turnover | E | Synaptic-only storage models |
| **Tripartite Synapse / Glial Memory** | Araque; Bhatt; multiple | Astrocytes and microglia are active participants in synaptic plasticity and consolidation | E | Neuron-only synapse models |
| **Adult Neurogenesis (DG)** | Altman, Gross; Bhaskaran | New granule cells born in DG subgranular zone contribute to pattern separation and cognitive flexibility | E | Static circuit models |

---

## Cognitive Psychology Frameworks

| Framework | Proponents | Core Claim | Evidence Class | Competes With |
|-----------|-----------|-----------|----------------|---------------|
| **Working Memory Model** | Baddeley & Hitch (1974) | WM has 3 components: phonological loop, visuospatial sketchpad, central executive; limited capacity | C | Unitary short-term memory models |
| **Levels of Processing** | Craik & Lockhart (1972) | Deeper semantic processing produces stronger encoding; encoding is not binary storage | C | Dual-store (STM/LTM) models |
| **Encoding Specificity** | Tulving & Thomson (1973) | Retrieval cues must match encoding context; memory is context-dependent | C | — |
| **Episodic vs. Semantic Memory** | Tulving (1972) | Episodic (autobiographical, contextual) and semantic (factual, decontextualized) are dissociable memory systems | C | Unitary declarative memory |
| **Constructive Memory / Schema Theory** | Bartlett (1932); Bransford & Johnson | Memory is reconstructive; schemas (organized prior knowledge) shape encoding and distort recall | C | Copy-fidelity / tape-recorder models |

---

## Educational Frameworks

| Framework | Proponents | Core Claim | Evidence Class |
|-----------|-----------|-----------|----------------|
| **Spacing Effect** | Ebbinghaus (1885); Cepeda et al. | Distributed practice produces stronger long-term retention than massed practice | C |
| **Testing Effect (Retrieval Practice)** | Roediger & Karpicke (2006) | Retrieval practice produces stronger retention than re-study; testing is learning | C |
| **Interleaving** | Taylor & Rohrer | Interleaving of topics during study (vs. blocking) improves long-term discrimination | C |
| **Desirable Difficulties** | Bjork (1994) | Conditions that slow learning may improve long-term retention (spacing, interleaving, generation) | C |

---

## Artificial Intelligence Frameworks

| Framework | Proponents | Core Claim | Evidence Class |
|-----------|-----------|-----------|----------------|
| **Parametric Memory** | Rumelhart, McClelland; LeCun et al. | Knowledge encoded in model weights through training; stable but requires retraining to update | C (AI) |
| **Experience Replay** | Lin (1992); Mnih et al. (DQN) | Storing and replaying past experiences improves learning stability; explicit analogy to SWR consolidation | C (AI) |
| **Retrieval-Augmented Generation (RAG)** | Lewis et al. (2020) | External knowledge retrieved at inference time; extends effective memory beyond parametric limits | C (AI) |
| **Differentiable Neural Computer (DNC)** | Graves et al. (2016) | Differentiable external memory with read/write heads; explicit external memory architecture | E (AI) |
| **Continual / Lifelong Learning** | Kirkpatrick et al. (EWC) | Preventing catastrophic forgetting in neural networks via selective weight protection | E (AI) |

---

## Anthropological / Social Frameworks

| Framework | Proponents | Core Claim | Evidence Class |
|-----------|-----------|-----------|----------------|
| **Collective Memory** | Halbwachs (1925) | Memory is socially constituted; individuals remember within group frameworks; collective memory is irreducible to individual memories | C (sociology) |
| **Oral Tradition as Distributed Memory** | Ong (1982); Vansina | Pre-literate cultures implement distributed memory through oral performance and formulaic structure | C (anthropology) |
| **Sites of Memory (Lieux de mémoire)** | Nora (1984) | Memory is externalized into material sites, monuments, and artifacts when living tradition fades | C (history) |

---

## Contemplative / Trauma Frameworks

| Framework | Proponents | Core Claim | Evidence Class |
|-----------|-----------|-----------|----------------|
| **Attentional Deconditioning** | Buddhist scholarship; Kabat-Zinn | Mindfulness practice deconditions automatic emotional responses attached to memories | P, E |
| **PTSD as Memory Pathology** | van der Kolk; Brewin | PTSD involves disrupted reconsolidation — traumatic memories re-encoded without narrative integration | C (clinical) |
| **Reconsolidation-Based Therapy** | Nader; Ecker (Coherence Therapy) | Deliberately reactivating traumatic memories in safe context to open reconsolidation window for therapeutic modification | Q |

---

## Theory Relationship Map

```
MOLECULAR LEVEL
  LTP (Hebb) ←→ Reconsolidation ←→ Epigenetic Storage
       ↓
CIRCUIT LEVEL  
  Trisynaptic Circuit → CLS Theory → SCT vs. MTT
       ↓
COGNITIVE LEVEL
  Working Memory Model → Schema Theory (Bartlett) → Encoding Specificity
       ↓
SYSTEMS LEVEL
  Sleep consolidation (SHY vs. Replay view)
       ↓
CULTURAL LEVEL
  Collective Memory (Halbwachs) → Oral Tradition → Sites of Memory
       ↓
AI LEVEL
  Parametric → Transient → External Memory → RAG → DNC
```

---

## Competing Model Summary

| Competition | Frameworks | Empirical Resolution Status |
|------------|-----------|---------------------------|
| How long does hippocampus matter? | SCT vs. MTT | Unresolved — evidence on both sides |
| What does sleep do to memory? | SHY (downscaling) vs. Replay (consolidation) | Partial — both may be true for different phases |
| Where is memory stored long-term? | Synaptic-only vs. Epigenetic + Synaptic | Unresolved — epigenetic mechanisms real; sufficiency unknown |
| How does prior knowledge shape encoding? | CLS (two-stage) vs. Direct schema encoding | Emerging — not yet resolved at circuit level |

---

## Related Documents

- [[12 Evidence Registry/RP-002 Evidence Registry]]
- [[09 Canonical Synthesis/RP-002 Canonical Synthesis]]
- [[11 Canonical Glossary/RP-002 Canonical Glossary]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | LUMIAION | Initial matrix; 30 frameworks across 6 domains; DOC-C pending |
