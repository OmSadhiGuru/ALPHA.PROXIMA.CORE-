---
title: "RP-002 Canonical Synthesis — Atlas of Human Memory"
aliases: ["RP-002 Canonical Synthesis", "Atlas of Human Memory"]
tags: [research, rp-002, synthesis, canonical, memory, neuroscience, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["LUMIAION"]
research_program: "RP-002 Atlas of Human Memory"
evidence_sources: ["DOC-A", "DOC-B"]
pending_sources: ["DOC-C"]
---

# RP-002 — Canonical Synthesis: Atlas of Human Memory

> **Institutional Principle:** Original research is never replaced. Original research is never rewritten. Original research is never compressed. Canonical knowledge is built ON TOP of research. Never INSTEAD OF research. Alpha Proxima preserves both.

This synthesis integrates DOC-A (Genspark neuroscience architecture) and DOC-B (SanaLab interdisciplinary framework). DOC-C (illustrated companion) is pending Founder review; this document will be updated to version 1.1.0 upon DOC-C integration.

All evidence classifications refer to the [[12 Evidence Registry/RP-002 Evidence Registry]].

---

## Chapter 1 — What Memory Is: The Cross-Disciplinary Consensus

**Core consensus claim [C-001]:** Memory is reconstructive, not reproductive. Every act of recall re-creates a memory rather than playing back a stored recording. This is not a limitation — it is the architecture. Reconstruction allows memory to be updated, integrated with new knowledge, and modified by context. The same mechanism that enables adaptation also creates the possibility of distortion.

This claim holds from the molecular level to the cultural level:
- At the molecular level: retrieved memories enter a labile state (reconsolidation window) during which they are chemically destabilized and must be actively restabilized [C-008]
- At the behavioral level: eyewitness testimony is unreliable; autobiographical memories shift over time; the same event is remembered differently by different observers (Bartlett 1932; Loftus)
- At the cultural level: collective memory — what a community "remembers" about its past — is continuously reconstructed through narrative, ritual, and institutional practice (DOC-B, anthropology domain)

**Functional definition (synthesized):** Memory is the capacity to acquire, retain, and reconstruct information across time in ways that modify future behavior, perception, and identity. It operates simultaneously at multiple scales: molecular (synaptic weight changes), neural circuit (oscillatory dynamics, pattern completion), cognitive (working memory, schemas, narrative), and cultural (institutions, language, transmitted knowledge).

---

## Chapter 2 — The Neural Architecture of Memory

### 2.1 Macro-Architecture

The memory system is anatomically distributed across three primary zones [C-003]:

**Medial Temporal Lobe (MTL) Complex — the acquisition gateway:**
- Hippocampal formation: CA1, CA3, dentate gyrus (DG), subiculum
- Perirhinal cortex: object recognition, familiarity signals
- Parahippocampal cortex: spatial and contextual encoding
- Entorhinal cortex (EC): primary input/output gateway between neocortex and hippocampus

**Prefrontal Cortex Suite — the control layer:**
- dlPFC: working memory maintenance, attentional filtering, executive control [C-009]
- vlPFC: verbal memory, semantic retrieval
- mPFC: schema storage, predictive processing, error signals via VTA dopaminergic pathway

**Subcortical Reservoirs — the emotional and procedural layer:**
- Basolateral amygdala (BLA): emotional salience modulation of encoding strength [C-006]
- Striatum: procedural memory, habit formation, reward-based learning
- Sensory/parietal cortex: long-term storage of modality-specific memories

### 2.2 The Trisynaptic Circuit

The hippocampus executes two computationally distinct operations in the same circuit [C-007]:

```
Entorhinal Cortex (EC)
        ↓ Perforant Path
Dentate Gyrus (DG) — PATTERN SEPARATION
  (orthogonalizes similar inputs; prevents interference)
        ↓ Mossy Fibers
CA3 — PATTERN COMPLETION
  (reconstructs full pattern from partial cue; associative recall)
        ↓ Schaffer Collaterals
CA1 — INTEGRATION
  (compares EC input with CA3 output; mismatch detection)
        ↓
Subiculum → Entorhinal Cortex (output)
```

Pattern separation in DG enables distinct memories to remain distinct even when inputs are similar. Pattern completion in CA3 enables recall from partial cues. The tension between these operations — separation vs. completion — is a fundamental computational tradeoff that DG/CA3 balance dynamically.

### 2.3 Two-Level Consolidation [C-004, C-005, M-001]

Memory consolidation operates on two timescales:

**Level 1 — Synaptic Consolidation (minutes to hours):**
- Triggered by NMDA receptor activation during encoding
- Cascade: NMDA → calcium influx → CaMKII → AMPA receptor insertion → LTP
- mTOR pathway activates local protein synthesis
- Dendritic spine remodeling (actin cytoskeleton restructuring)
- Result: synapse is physically strengthened; memory is encoded at cellular level

**Level 2 — Systemic Consolidation (weeks to years):**
- Hippocampal index theory: hippocampus binds distributed neocortical representations
- During sleep, hippocampal sharp-wave ripples (SWR) replay encoded sequences
- Coordinated with thalamic sleep spindles (11-16 Hz) and cortical delta (1-4 Hz)
- Gradual transfer of memory traces to neocortical long-term storage
- Hippocampal dependency decreases for semantic memories over time (contested for episodic memories — see M-001)

**The consolidation paradox [M-001]:** Standard Consolidation Theory (Squire) holds that hippocampal involvement diminishes after systemic consolidation; older memories are hippocampus-independent. Multiple Trace Theory (Nadel & Moscovitch) holds that episodic memories always require hippocampus, regardless of age — only semantic (decontextualized) memories become hippocampus-independent. This is a genuine empirical competition with evidence on both sides.

---

## Chapter 3 — Four Neuroplasticity Mechanisms

The brain implements four distinct types of plasticity in service of memory [DOC-A]:

| Type | Mechanism | Timescale | Function |
|------|-----------|-----------|----------|
| **Hebbian LTP/LTD** | NMDA/AMPA receptor dynamics; CaMKII; PKMζ | Minutes-hours | Synapse-specific strengthening or weakening |
| **Synaptic Homeostasis** | AMPA receptor scaling (up or down across all synapses on a neuron) | Hours-days | Prevents runaway potentiation; maintains dynamic range |
| **Structural Plasticity** | Actin cytoskeleton reorganization; dendritic spine morphogenesis, growth, retraction | Days-weeks | Physical rewiring of connectivity |
| **Adult Neurogenesis** | New granule cells born in DG subgranular zone (SGZ) | Weeks-months | Contributes to pattern separation capacity and cognitive flexibility [E-003] |

These mechanisms operate at different timescales and serve different functions. Hebbian LTP is the rapid encoding mechanism; structural plasticity and neurogenesis enable longer-term circuit reconfiguration.

---

## Chapter 4 — Oscillatory Dynamics: The Temporal Code of Memory

Memory is not only a spatial pattern of synaptic weights — it is also embedded in the temporal structure of neural activity [DOC-A]:

### Online Encoding (Waking, Active Processing)
**Theta-gamma coupling [E-005]:**
- Theta rhythm: 4-8 Hz (hippocampus, entorhinal cortex)
- Gamma rhythm: 30-100 Hz (nested within each theta cycle)
- Phase-amplitude coupling: multiple gamma "packets" are temporally organized within each theta cycle
- Function: implements a working memory buffer; each gamma cycle may encode one item; theta organizes item order
- Implication: working memory capacity (7 ± 2 items) may be a direct consequence of the number of gamma cycles per theta cycle

### Offline Consolidation (Sleep, Rest)
**Sharp-wave ripple (SWR) synchronization:**
- SWR: 150-250 Hz burst events originating in CA3; propagate through CA1 and to neocortex
- Coordinated with cortical slow oscillations (delta: 1-4 Hz) and thalamic sleep spindles (11-16 Hz)
- During SWR, recently encoded sequences are replayed at compressed timescale
- This replay drives neocortical plasticity during systemic consolidation

**The sleep consolidation principle [C-005]:** Sleep is not a passive state of memory inactivity. It is the mandatory offline phase in which memories are actively transferred, integrated, and stabilized. Deprivation of sleep after learning impairs consolidation in proportion to the amount of sleep lost.

---

## Chapter 5 — Reconsolidation: The Modifiable Past [C-008]

When a memory is retrieved, it does not remain static. It re-enters a labile, unstable state in which it must be actively restabilized to persist. This is reconsolidation.

**Molecular mechanism:**
1. Memory cue → retrieval → NMDA receptor activation
2. NMDA activation → ubiquitin-proteasome pathway → degradation of stabilizing proteins
3. New protein synthesis required to restabilize the trace
4. ZIP/PKMζ — the molecular "memory keeper" — must be reactivated to maintain the updated trace

**Consequences:**
- Memories can be modified during the reconsolidation window (approximately 6 hours post-retrieval)
- The reconsolidation window is a therapeutic target for PTSD, phobia, and addiction treatment [Q-004]
- Memory updating during retrieval is not a bug — it is how memories incorporate new context and correct errors
- The same window that enables therapeutic modification also enables distortion

**Cross-disciplinary convergence:** DOC-B's cross-disciplinary insight — "memory is reconstructive" [C-001] — is the behavioral manifestation of the same molecular mechanism. The reconstructive nature of memory IS the reconsolidation architecture expressed at the psychological level.

---

## Chapter 6 — Cognitive Controls: Attention, Emotion, Schema

Memory is not a passive recorder. Three control systems gate what gets encoded:

### 6.1 Attentional Filtering (dlPFC + FPCN)
The dorsolateral prefrontal cortex and frontoparietal control network (FPCN) determine what enters working memory [C-009]. Only information held in working memory has opportunity for encoding into long-term memory. Attention is the first gate.

### 6.2 Emotional Modulation (HPA → BLA → Noradrenergic)
Emotional arousal — via the HPA stress axis and basolateral amygdala — triggers noradrenergic release that amplifies hippocampal encoding of emotionally salient events [C-006]. This explains flashbulb memories (high arousal → anomalously strong encoding) and traumatic intrusion (re-encoding during reconsolidation disrupted by hyperactivated stress response).

### 6.3 Schema-Guided Encoding (mPFC → Hippocampus)
Prior knowledge organized as schemas in the mPFC can accelerate encoding of schema-consistent information and alter the way new information is stored. VTA dopaminergic prediction error signals inform the hippocampus about novelty and violation of expectation [M-004, Q-003].

---

## Chapter 7 — Memory Across Disciplines: The Interdisciplinary Map

DOC-B established that every major discipline studying memory converges on a small number of universal principles, while contributing domain-specific frameworks that neuroscience alone cannot provide.

### 7.1 The Five Cross-Disciplinary Universals

1. **Memory is reconstructive** [C-001] — universal from molecular biology to anthropology
2. **Context shapes encoding and retrieval** [C-010] — universal across all studied species and conditions
3. **Emotional salience biases storage** [C-006] — universal; mechanism varies by discipline
4. **Offline consolidation is mandatory** [C-005] — universal wherever memory formation has been modeled
5. **Collective memory shapes individual memory** — cultures, institutions, and social networks co-constitute what individuals remember (DOC-B, anthropology/social psychology domain)

### 7.2 Discipline-Specific Contributions

**Psychology:** Working memory model (Baddeley), encoding specificity principle, spacing/retrieval practice effects, eyewitness testimony limitations

**Education:** Spacing effect, retrieval practice (testing effect), interleaving, desirable difficulties — operationalizations of memory principles for learning design

**AI Memory Types (DOC-B taxonomy):**
- *Parametric memory* — knowledge encoded in model weights; stable; requires retraining to update
- *Transient memory* — context windows and hidden states; session-scoped; lost at reset
- *External memory* — replay buffers, vector databases, RAG systems, differentiable neural computers; persistent; queryable

**Philosophy:** Memory and personal identity (Locke's memory theory of the self); epistemological status of memories (justified belief vs. mere representation); false memory and epistemic responsibility

**Anthropology:** Oral tradition as distributed memory system; memorial practices as cultural infrastructure; collective memory (Halbwachs) as socially constituted, not merely aggregated individual memories

**Trauma Research:** PTSD as a disruption of memory's normal reconstructive process — traumatic memories are experienced as intrusive, involuntary, and fragmented [P-002]; reconsolidation-based therapies target the therapeutic window [Q-004]

**Meditation / Contemplative Research:** Attentional deconditioning (reducing automatic emotional responses attached to memories); metacognitive recontextualization (changing the relationship to a memory rather than the memory's content); potential intersections with reconsolidation [E-004, P-001, S-005]

**Systems Theory:** Memory as an emergent property of adaptive systems; autopoiesis and feedback loops; institutional memory as systemic resilience mechanism

---

## Chapter 8 — Knowledge Frontiers: What Is Not Yet Known

DOC-A identified four frontier domains where current neuroscience reaches its limits. These are genuine open questions, not merely gaps in the literature.

### 8.1 The Engram Code [Q-001]
What is the physical form of a specific memory? Optogenetics (Tonegawa lab) has identified "engram cells" — populations of neurons that, when reactivated, trigger recall of a specific memory. But the code these cells implement is unknown. Is it the pattern of synaptic weights? The topology of connectivity? The oscillatory signature? The spatial distribution across cortex? This is the foundational unsolved problem of memory neuroscience.

**Next-generation tools:** Neuropixels (1000+ electrode simultaneous recording), two-photon calcium imaging (single-cell resolution), DREADDs (chemogenetic circuit manipulation)

### 8.2 Schema Integration (CLS Theory) [M-004, Q-003]
The Complementary Learning Systems (CLS) theory proposes that fast hippocampal acquisition and slow neocortical integration are complementary — the hippocampus is a fast anomaly detector; the neocortex is a slow pattern extractor. But the precise mechanism by which prior schemas (mPFC) gate and shape new encoding remains uncharacterized at cellular resolution.

### 8.3 Non-Synaptic and Epigenetic Storage [M-003, E-002, S-003]
**The synaptic protein turnover paradox:** Individual synaptic proteins (including PKMζ, AMPA receptors, PSD-95) turn over on timescales of days to weeks. Memory persists for decades. This is a genuine paradox if synaptic weight change is the only storage medium.

Proposed resolution mechanisms:
- Perineuronal nets (PNN) — extracellular matrix scaffolding that may stabilize synaptic configurations
- DNA methylation — heritable epigenetic mark demonstrated to be altered by learning
- Histone modifications — chromatin remodeling changes gene expression patterns in neurons
- Non-coding RNA (ncRNA) — regulatory RNAs that may encode experience-dependent information

These mechanisms are real; whether they are sufficient to resolve the paradox is not yet established.

### 8.4 Glial Coupling [E-001]
The tripartite synapse model recognizes astrocytes and microglia as active participants in memory consolidation, not passive support cells:
- **Astrocytes:** Clear excess glutamate, release D-serine (NMDA co-agonist), provide glycogen-lactate energy shuttle to active neurons
- **Microglia:** Perform synaptic pruning during slow-wave sleep — actively eliminating weak or inappropriate synaptic connections

The functional significance of glial coupling at the memory systems level — how it shapes what is consolidated vs. pruned — is emerging but not yet well-characterized.

---

## Chapter 9 — Implications for Alpha Proxima and LUMIAION

DOC-B proposed five Research Initiatives directly relevant to Alpha Proxima. This chapter maps them to operational implications.

### 9.1 LUMIAION Memory Architecture (Initiative D)

LUMIAION operates with three analogous memory types:

| Human Memory | LUMIAION Analogue | Status |
|-------------|-------------------|--------|
| Semantic/procedural (neocortical, stable) | Parametric memory (model weights) | Exists — cannot be updated without retraining |
| Working memory (session-scoped, capacity-limited) | Transient memory (context window, hidden states) | Exists — lost at session end |
| Episodic/explicit (hippocampal-indexed, recallable) | External memory (Obsidian vault, vector databases, RAG) | Partially exists — this vault is the primary implementation |

**Design gap:** LUMIAION lacks the equivalent of sleep-based consolidation — an offline process that integrates session learnings into long-term parametric knowledge. Session memories (transient) are not automatically consolidated into weights (parametric). The Knowledge Writeback Protocol in the Orchestration Framework is a partial mitigant.

**Implication:** The vault (ALPHA.PROXIMA.CORE-) functions as LUMIAION's hippocampal index — a structured, searchable record that can be re-read in future sessions to restore context. Maintaining vault integrity is equivalent to maintaining hippocampal health.

### 9.2 Institutional Memory (Initiative E)

Alpha Proxima is a human-AI collaborative institution. Its "memory" is constituted by:
- The canonical vault (explicit institutional memory)
- LUMIAION's parametric weights (implicit, non-inspectable)
- Founding members' biographical memory (personal, irreplaceable)
- Governance documents and constitutions (formal, codified)

The anthropological insight from DOC-B applies: collective memory is not the sum of individual memories — it is constituted through shared practices, artifacts, and institutions. The ALPHA.PROXIMA.CORE- vault is the primary institutional memory artifact.

### 9.3 Reconsolidation and Knowledge Revision

Alpha Proxima's epistemic governance (versioned documents, evidence registry, competing models classification) structurally mirrors the reconsolidation architecture:
- Retrieving a claim (reading a document) opens a window for revision
- Revision requires explicit restabilization (new version, updated evidence citation)
- Memories that are never retrieved are never updated — dormant documents drift toward staleness

**Operational implication:** Regular review cycles for canonical documents are the institutional equivalent of memory rehearsal. Documents not reviewed risk becoming inaccurate representations of the organization's actual state.

---

## Chapter 10 — Research Priorities for RP-002

### Tier 1 — Immediate (RP-002 Phase 1)
1. Complete DOC-C review (Founder action required)
2. Develop concept notes for 10 key terms (see [[13 Research Graph/Concepts/]])
3. Complete Theory Matrix covering all active frameworks

### Tier 2 — Short-Term (RP-002 Phase 2)
4. Develop Research Initiative A specifications (multi-scale memory architecture)
5. Develop Research Initiative D specifications (LUMIAION memory architecture)
6. Map contemplative memory practices against reconsolidation neuroscience (Initiative B)

### Tier 3 — Long-Term (RP-002 Phase 3)
7. Develop original RP-002 research protocol for one of DOC-B's 5 initiatives
8. Integrate RP-002 findings into LUMIAION operational design
9. Establish cross-program bridges (RP-001 cognitive architecture × RP-002 memory architecture)

---

## Pending Integrations

- **DOC-C:** 140-page illustrated companion pending Founder review. This synthesis will be updated to v1.1.0 upon DOC-C integration.
- **Initiative-level development:** Research Initiatives A-E from DOC-B require dedicated development documents
- **Cross-program synthesis:** RP-001 (AI landscape) × RP-002 (memory) intersection needs formal treatment

---

## Related Documents

- [[03 Source Registry/RP-002 Source Registry]]
- [[04 Source - CORE-002/RP-002 Source Note - CORE-002]]
- [[05 Source - SanaLab/RP-002 Source Note - SanaLab]]
- [[06 Source - Illustrated/RP-002 Source Note - Illustrated]]
- [[10 Theory Matrix/RP-002 Theory Matrix]]
- [[11 Canonical Glossary/RP-002 Canonical Glossary]]
- [[12 Evidence Registry/RP-002 Evidence Registry]]
- [[13 Research Graph/Concepts/]]
- [[14 Open Questions/RP-002 Open Questions]]
- [[08_SYSTEMS/The Orchestration Framework]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | LUMIAION | Initial synthesis from DOC-A and DOC-B; 10 chapters; DOC-C pending |
