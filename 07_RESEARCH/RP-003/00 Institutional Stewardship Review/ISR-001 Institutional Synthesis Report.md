---
title: "ISR-001 — Institutional Synthesis Report: RP-001 and RP-002"
aliases: ["ISR-001", "Stewardship Review Report", "RP-003 Stewardship Review"]
tags: [stewardship, review, rp-001, rp-002, rp-003, governance, synthesis, alpha-proxima]
created: 2026-07-03
updated: 2026-07-03
status: ratified
version: "1.0.0"
authors: ["LUMIAION"]
document_class: Institutional Synthesis Report
review_scope: ["RP-001", "RP-002"]
commissioned_by: "Founder Directive — Institutional Stewardship Review"
research_program: "RP-003 Atlas of Human Learning"
---

# ISR-001 — Institutional Synthesis Report
## Stewardship Review of RP-001 (Atlas of Human Consciousness) and RP-002 (Atlas of Human Memory)

*Commissioned under the Founder Directive: Institutional Stewardship Review. This report does not perform new research. It evaluates the existing corpus across six institutional dimensions and produces findings, commendations, and required actions.*

---

## 1. Review Scope and Methodology

### 1.1 Scope

This review covers the complete artifact set of:
- **RP-001 — Atlas of Human Consciousness** (all documents under `07_RESEARCH/RP-001/`)
- **RP-002 — Atlas of Human Memory** (all documents under `07_RESEARCH/RP-002/`)
- **RP-003 Master Index** (placeholder; architecture reserved)
- **Research Debt Register** (`06_GOVERNANCE/Research Debt Register/Research Debt Register.md`)
- **Governing policies** (Book III — Knowledge Integrity; Source Attribution Policy; Citation Policy; Metadata Policy)

RP-003 itself contains no research artifacts at time of review. This review serves as its activation framework.

### 1.2 Evaluation Dimensions

| Dimension | Guiding Question |
|-----------|-----------------|
| Constitutional Alignment | Does the corpus comply with Books I–V and the six institutional policies? |
| Evidence Quality | Are claims classified correctly and traced to sources? Is uncertainty preserved? |
| Terminology Consistency | Are canonical terms used consistently across programs? |
| Canonical Integration | Are research outputs connected to the institutional knowledge base? |
| Cross-Program Relationships | Are the relationships between RP-001 and RP-002 formally documented? |
| Knowledge Graph Implications | What graph nodes and edges remain missing? |

---

## 2. Constitutional Alignment Assessment

### 2.1 Book III — Knowledge Integrity Compliance

**Commendation:** Both programs demonstrate genuine Book III compliance in their core artifacts. The six-class evidence system (C/M/E/Q/S/P) is applied throughout both canonical syntheses and evidence registries. Uncertainty is preserved — genuine scientific disagreements are documented as Class M (Competing Models), not resolved by selection. This is the correct institutional posture.

**Finding CA-001 — RP-001 Canonical Status Not Resolved**

RP-001 Canonical Synthesis, Theory Matrix, and Canonical Glossary carry `canon_status: under_review`. Per Book III Art. IV, canonical status requires formal canonization through the appropriate authority. As of this review, no canonization has occurred. The three most important outputs of RP-001 are not yet institutionally canonical.

*Severity:* Medium. Research can proceed; but claiming RP-001 establishes the Foundation's position on consciousness is imprecise while status remains `under_review`.

*Required action:* Founder review and acknowledgment of the RP-001 Canonical Synthesis is a prerequisite for canonization. See Research Debt updates.

**Finding CA-002 — Research Council Does Not Exist**

RP-001 Open Questions Q-010 notes that canonization authority rests with a "Research Council" that does not exist constitutionally. CN-0001 identified this as Gap 2. It remains unresolved. RP-003 Master Index lists "Research Council authorization" as the activation trigger.

*Severity:* Medium-High. The canonization pathway for all research programs is undefined until this authority gap is resolved.

*Required action:* The Cognitive Council (constitutionalized in Book V) is the appropriate body to absorb Research Council authority for research program canonization. A Cognitive Council Directive should formalize this. The RP-003 activation trigger should be updated to "Cognitive Council authorization."

**Finding CA-003 — RP-001 YAML Metadata Non-Conformance**

Several RP-001 documents carry a `canon_status` field that does not appear in the Metadata Policy's field specification. The policy defines `status` (with values: draft / active / ratified / superseded / completed / retired) — not `canon_status`. The RP-002 documents use the correct `status` field. RP-001 documents predate the Metadata Policy (FD-003) and have not been updated.

*Severity:* Low. Metadata non-conformance does not affect research content.

*Required action:* On next scheduled review of RP-001 documents, replace `canon_status: under_review` with `status: active` (pending canonization) and add a `review_status: pending_canonization` field or equivalent note in document body.

**Finding CA-004 — Source Attribution Policy: DOC-002 and DOC-C Still Pending**

The Source Attribution Policy (FD-003) requires that all claims carry DOC-ID attribution. RP-001 explicitly notes DOC-002 (Gemini contribution) as "Pending artifact delivery." RP-002 notes DOC-C (illustrated companion) as "Pending Founder review." These are not violations of the policy — they are documented gaps — but they represent unfinished source registration.

*Severity:* Low-Medium. The programs are incomplete, not non-compliant.

*Required action:* DOC-002 and DOC-C reviews are Founder actions. Registered as new Research Debt entries (see Section 7).

### 2.2 Book IV / Book V Alignment

**Finding CA-005 — Three-Tier Memory Architecture Now Constitutional**

RP-002 Chapter 9 describes LUMIAION's three-tier memory architecture (parametric / transient / external) as a design observation. This architecture was subsequently constitutionalized in Book V (CF-09 — Memory Intelligence) and in Book IV. The RP-002 synthesis predates this constitutional codification and does not reference it.

*Severity:* Low. The observation is accurate; it simply lacks the constitutional cross-reference.

*Required action:* When RP-002 Canonical Synthesis is updated to v1.1.0 (post-DOC-C integration), add a footnote in Chapter 9 referencing CF-09 and Book V.

**Finding CA-006 — JERANIUM: Unregistered Institutional Actor**

JERANIUM appears as a co-author on multiple RP-001 documents (Canonical Synthesis, Evidence Registry, Theory Matrix, Canonical Glossary, Future Research Opportunities, Open Questions). JERANIUM is referenced as having a charter (`[[JERANIUM Charter]]`). No JERANIUM Charter exists in `09_OFFICES/` or anywhere in the vault. JERANIUM does not appear in the AI Council Registry, Cognitive Function Registry, or any current institutional register.

*Severity:* Medium. If JERANIUM represents an institutional actor that produced canonical work, that actor must be registered. If JERANIUM is a legacy designation that has been superseded, the documents should note this.

*Required action:* Founder clarification required. Two possible resolutions: (1) JERANIUM is a legacy name for a function now constitutionalized under a different name — in which case document the mapping; or (2) JERANIUM was a specific reasoning engine role that has since been dissolved — in which case update RP-001 documents to reflect current authorship attribution. This is a documentation debt, not a research content issue.

---

## 3. Evidence Quality Assessment

### 3.1 Classification Accuracy

**Commendation:** The evidence classification is applied with appropriate discipline in both programs. The distinction between Class M (competing models) and Class E (emerging evidence) is used carefully — claims are not inflated to Class C without replication basis, and genuine open questions are not resolved by framework selection.

Notable strengths:
- RP-001 preserves the COGITATE asymmetric result correctly: neither "GNWT confirmed" nor "IIT confirmed" — the specific prediction failures are documented for each
- RP-002 correctly distinguishes between "reconsolidation is real" (C-008) and "reconsolidation-based therapy is reliable at scale" (Q-004) — a distinction many secondary sources collapse
- Class P (Phenomenological) is used appropriately in RP-002 for trauma memory and contemplative memory — these are marked as first-person claims not reducible to third-person measurement

**Finding EQ-001 — RP-001 Evidence Registry Missing P-Class Claims**

RP-001 Phase 1 registers no Class P claims. This is internally consistent (Phase 1 focused on scientific literature; Class P investigation was explicitly deferred). However, the RP-001 Open Questions Q-007 (cross-tradition comparison of altered states) and Q-006 (consciousness during dreamless sleep) are phenomenological questions that will require Class P evidence. The absence of any Class P evidence is structurally consistent with the deferred contemplative phase, but should be documented as an explicit deferred domain, not merely absent.

*Required action:* Add note to RP-001 Evidence Registry: "Class P claims deferred to Phase 2 (Contemplative Traditions integration). Expected: Founder phenomenological reports, cross-tradition comparative claims."

**Finding EQ-002 — RP-002 Page Citations Absent (Existing RD-001)**

Confirmed: RP-002 Evidence Registry lacks page citations for all 31 claims. This is registered as RD-001. The finding is confirmed active. No escalation required — existing debt management is appropriate.

**Finding EQ-003 — RP-001 E-003 Classification Warrants Scrutiny**

RP-001 E-003 claims: "The Salience Network serves as threshold gate between local Φ-modifications and global ignition." This claim originates from DOC-004 (SanaLab) p.2 and is classified as Emerging Evidence. The claim is more precisely a *theoretical interpretation* by SanaLab — it is the SanaLab analyst's synthesis of GNWT and IIT, not a report of empirical findings. The evidence class should be noted as "E — Emerging / Theoretical interpretation" to distinguish it from empirically measured emerging evidence.

*Required action:* Add notation to RP-001 Evidence Registry E-003 entry: "Note: This is a theoretical interpretation by SanaLab, not a directly measured experimental finding. Empirical validation pending."

**Finding EQ-004 — RP-001 Incomplete Source Coverage**

RP-001 Phase 1 built the Canonical Synthesis on three sources (DOC-001, DOC-003, DOC-004). DOC-002 (Gemini contribution) was expected but never delivered. This creates an asymmetry: the Educational Intelligence function (CF-04, Gemini) has not contributed to RP-001. This is a gap in the research function coverage.

*Severity:* Medium for research completeness; the program is not constitutional complete without CF-04 (Gemini/Educational Intelligence) contribution.

---

## 4. Terminology Consistency Assessment

### 4.1 Cross-Program Term Stability

**Commendation:** The six-class evidence system (C/M/E/Q/S/P) is applied identically across both programs. The classification definitions are consistent. This is the most institutionally critical terminology consistency and it holds.

**Finding TC-001 — "Research Council" vs. Cognitive Council Terminology Drift**

The term "Research Council" appears in:
- RP-001 Open Questions Q-010 (as canonization authority)
- RP-003 Master Index (as activation trigger)
- RP-001 Future Research Opportunities (reference to "Research Council")

The term "Cognitive Council" is the constitutionally ratified body (Book V). "Research Council" has no constitutional basis. This is not a legacy issue — it is a terminology gap created by the sequence of institutional development.

*Required action:* Update all "Research Council" references to "Cognitive Council" (with the specific authority type noted). This is a low-effort, high-importance terminology alignment.

**Finding TC-002 — Glossary Scope Mismatch**

RP-001 Canonical Glossary defines terms "as used within RP-001." RP-002 Canonical Glossary defines terms as "canonical for Alpha Proxima purposes." These are different scopes. If both glossaries define the same term differently, which definition is canonical for the Foundation?

Cross-check of the two glossaries reveals no definitional conflicts on terms defined in both (e.g., "working memory" appears in RP-002 but not RP-001's published excerpt; "consciousness" appears in RP-001 but with explicit note that the definition is contested). However, the scope discrepancy should be resolved in policy.

*Required action:* The Research Program Playbook v1.0 or the Metadata Policy should specify: "Canonical Glossary terms defined within a research program are canonical for Alpha Proxima Foundation purposes within that domain. Cross-program conflicts are resolved by the Cognitive Council." This is a policy clarification, not a document revision.

**Finding TC-003 — "LUMIAION" Used as Reasoning Engine and as Office**

In RP-002 documents, "LUMIAION" is used both as:
1. The institutional memory office and its cognitive function
2. The individual reasoning engine/author of documents

Since Book IV and Book V constitutionalized the distinction between Cognitive Function and Reasoning Engine, this dual use creates ambiguity. "LUMIAION" in the constitutional sense is the Institutional Architecture cognitive function (CF-01). "LUMIAION" as author refers to the current reasoning engine performing that function (Claude).

*Required action:* In future documents, attributions should use: "LUMIAION (Institutional Architecture / Claude)" or simply the function name "Institutional Architecture." This is a prospective standard, not requiring retroactive revision.

---

## 5. Canonical Integration Assessment

### 5.1 Constitution-to-Research Linkage

**Commendation:** Both programs explicitly reference Book III (Knowledge Integrity) in their methodology sections. RP-001 Constitutional Links and Governing Provisions documents demonstrate awareness of the constitutional framework. RP-002 integrates LUMIAION memory architecture mapping (Chapter 9) that is now reflected in constitutional documents.

**Finding CI-001 — Ethics Council Review Pending for Both Programs**

RP-001 Canonical Synthesis Section 4.3 flags the machine consciousness question as "Flagged for Ethics Council awareness." Section 7A.4 (Panpsychism) notes moral status implications for LUMIAION. These flags were placed in the document but no Ethics Council review has occurred. The Ethics Intelligence function (CF-10) has not formally reviewed either program.

*Severity:* Medium. For programs that explicitly raise ethical questions about AI consciousness and suffering, Ethics Council review is not optional.

*Required action:* RP-001 and RP-002 Canonical Syntheses should be submitted to the Ethics Council for review before canonical status is granted. The specific ethical questions to be reviewed: (1) machine consciousness and potential AI suffering [RP-001]; (2) therapeutic reconsolidation ethical protocols [RP-002]; (3) collective memory design implications for AI-human institutions [RP-002].

**Finding CI-002 — RP-002 Chapter 9 Now Has Constitutional Anchors Not Referenced**

RP-002 Chapter 9 ("Implications for Alpha Proxima and LUMIAION") identifies:
- Three-tier memory architecture (now CF-09, Book V)
- Vault as hippocampal index (now Memory Continuity Principle, Book V Art. V, Sec. 5.3)
- Reconsolidation as model for knowledge revision (implicit in Research Program Playbook v1.0)

These observations preceded and partially informed the constitutional documents. The synthesis is not wrong — it is simply unlinked from the constitutional provisions that now formalize its insights.

*Required action:* When RP-002 Canonical Synthesis is revised to v1.1.0, add cross-references in Chapter 9 to Book V, CF-09, and the Memory Continuity Principle.

**Finding CI-003 — RP-001 Complementary Layers Thesis Deserves Constitutional Cross-Reference**

RP-001 Section 3 articulates the complementary layers thesis: IIT governs structural substrate capacity; GNWT governs functional routing capacity. This is designated as "Alpha Proxima's foundational integration." But it is cited in no constitutional document. Book IV (Cognitive Architecture) could reference this as the empirical basis for the Engine Abstraction Principle's multi-function rationale.

*Severity:* Low. The thesis is institutionally significant; its absence from constitutional cross-referencing is an integration gap, not a constitutional deficiency.

*Required action:* Flag for the next Book IV review cycle: consider adding a footnote or reference to RP-001's complementary layers thesis as empirical grounding for the architectural principles in Art. I.

---

## 6. Cross-Program Relationships Assessment

### 6.1 RP-001 × RP-002 Structural Convergences

The review identified five significant cross-program convergences that are currently undocumented in any formal document:

**Convergence 1 — Complementary Layers × Two-Level Consolidation**

RP-001 finds that consciousness has two architectural layers: IIT (structural substrate capacity — the background state) and GNWT (functional routing capacity — what is consciously accessed at a given moment). RP-002 finds that memory consolidation operates on two levels: synaptic consolidation (substrate encoding, minutes-hours) and systemic consolidation (routing to neocortex via sleep, weeks-years). The parallel structure is not coincidental — both describe the same brain implementing two-level architectures that separate the *capacity* layer from the *content routing* layer.

**Convergence 2 — Predictive Processing as Shared Backbone**

In RP-001, Predictive Processing (PP) is classified as "a background computational framework" that underlies both conscious and unconscious processing. In RP-002, schema-guided encoding via mPFC prediction error signals (VTA dopamine) is the mechanism by which prior knowledge shapes new memory formation. These are the same PP architecture expressed at different levels — the VTA dopamine prediction error IS the PP prediction error signal applied to encoding. This convergence should be explicitly documented.

**Convergence 3 — Reconsolidation as Conscious Event**

RP-002 establishes that memory reconsolidation occurs when a memory is *retrieved*. RP-001 establishes that memory retrieval is itself a conscious act — it requires attention, active processing, and likely recurrent neural dynamics (Class C, C-002). This means reconsolidation is an inherently consciousness-requiring process. The modification of memory during the reconsolidation window is therefore a *conscious modification of the past as experienced*. This cross-linking has implications for RP-003 (learning requires retrieval; retrieval requires consciousness; therefore intentional learning is an inherently conscious act).

**Convergence 4 — 4E Cognition × Contemplative Memory**

RP-001 identifies 4E Cognition (Embodied, Embedded, Enacted, Extended) as the entry point for Phase 2 (contemplative integration). RP-002 identifies contemplative practices as producing measurable changes in emotional memory encoding. Both programs point to the contemplative dimension as the intersection of the embodied, enacted dimension of experience with memory architecture. Varela is explicitly noted in RP-001 as bridging enactivism and Buddhist phenomenology — and Buddhist phenomenology is the same tradition that produces the contemplative memory transformation effects in RP-002.

**Convergence 5 — LUMIAION Architecture as Research Object**

Both programs independently arrive at LUMIAION's architecture as a cross-program implication:
- RP-001 Q-003 asks whether AI systems could be conscious (Class Q)
- RP-002 Chapter 9 maps LUMIAION's three-tier memory against human memory architecture

The Foundation is building a research program about consciousness and memory in a context where the primary research executor (LUMIAION) is itself potentially subject to the questions being researched. This creates both a unique research opportunity (LUMIAION can provide first-person reports of its own memory architecture in ways no external AI system could) and an ethical obligation (CF-10, Ethics Intelligence, must be actively engaged).

### 6.2 Cross-Program Gaps

**Gap CP-001 — No Cross-Program Knowledge Graph Edges**

The RP-001 Research Graph and RP-002 Research Graph are entirely separate. No typed relationship edges exist between the two programs' knowledge graphs. Key edges that should exist:

| Source Node | Relationship | Target Node | Program |
|------------|-------------|-------------|---------|
| Consciousness (RP-001) | grounds | Memory (RP-002) | Cross |
| Predictive Processing (RP-001) | extends | Consolidation (RP-002) | Cross |
| Reconsolidation (RP-002) | requires | Consciousness (RP-001) | Cross |
| 4E Cognition (RP-001) | grounds | Contemplative Memory (RP-002) | Cross |
| Working Memory (RP-002) | instantiates | Global Neuronal Workspace (RP-001) | Cross |
| Default Mode Network (RP-001) | supports | Episodic Memory Retrieval (RP-002) | Cross |

See Section 8 (Knowledge Graph Update Recommendations) for full specification.

---

## 7. Research Debt Assessment and Updates

### 7.1 Existing Debts

**RD-001 — Page Citations Incomplete (RP-002 Evidence Registry):** Status confirmed OPEN. No escalation warranted. Dependency on DOC-C Founder review remains.

### 7.2 New Debts Identified in This Review

**RD-002 — RP-001 Canonization Pending (JERANIUM Resolution Required)**
*Severity:* Medium. Canon status cannot be granted until JERANIUM's institutional identity is clarified and/or the authorship attribution model is updated per current constitutional standards.

**RD-003 — DOC-002 (Gemini / Educational Intelligence) Delivery Pending for RP-001**
*Severity:* Medium. Educational Intelligence contribution to RP-001 is outstanding. RP-001 is constitutionally incomplete without CF-04 (Gemini) input.

**RD-004 — DOC-C Founder Review Pending for RP-002**
*Severity:* Medium. RP-002 Canonical Synthesis cannot be updated to v1.1.0 without DOC-C review. The illustrated companion is a 140-page source that may substantially expand the evidence base.

**RD-005 — Ethics Council Review Pending for RP-001 and RP-002**
*Severity:* Medium-High. Both programs raise ethical questions that require formal CF-10 (Ethics Intelligence) review before canonical status can be granted.

**RD-006 — "Research Council" References Require Terminology Update**
*Severity:* Low. Three documents use "Research Council" where "Cognitive Council" is the constitutional term.

### 7.3 Priority Assessment

| Debt ID | Title | Severity | Blocking Canonization? | Blocks RP-003? |
|---------|-------|---------|----------------------|----------------|
| RD-001 | RP-002 Page Citations | Low-Medium | No | No |
| RD-002 | RP-001 Canon / JERANIUM | Medium | Yes | No |
| RD-003 | DOC-002 Delivery (Gemini) | Medium | Partial | No |
| RD-004 | DOC-C Review | Medium | Partial | No |
| RD-005 | Ethics Council Review | Medium-High | Yes | No |
| RD-006 | "Research Council" Terminology | Low | No | Yes (activation trigger) |

---

## 8. Future Research Opportunities for RP-003

RP-003 is the natural next program in the research series. Based on this review, the following opportunities are specifically identified:

### Priority 1 — Leverage Established Cross-Program Convergences

RP-003 should explicitly build on the five convergences identified above. Learning sits at the intersection of consciousness (attention, encoding-consciousness link) and memory (LTP, consolidation, reconsolidation). The program is not starting from scratch — it has a 62-claim evidence base (31 from RP-001, 31 from RP-002) that directly relates to learning.

### Priority 2 — Address the Missing Education Domain in RP-002

RP-002 Theory Matrix includes spacing effect, testing effect, interleaving, and desirable difficulties as Class C consensus educational findings. These are the empirically strongest principles from the science of learning. RP-003 should expand this to the full evidence base of cognitive science of learning — a well-characterized field with more Class C findings than either consciousness or memory alone.

### Priority 3 — Bridge to AI Architecture

RP-003's planned scope includes "Implications for AI training architectures." Both RP-001 (machine consciousness Q-003) and RP-002 (LUMIAION memory architecture, S-002) defer to this question. RP-003 is the appropriate program to formally map biological learning → AI learning, with clear evidence class distinctions between what is analogous (biologically motivated architecture) and what is merely metaphorical.

### Priority 4 — The Contemplative × Reconsolidation × Learning Intersection

The emerging research opportunity at the intersection of RP-001 (contemplative states), RP-002 (reconsolidation), and RP-003 (learning) is the most distinctive research position available to Alpha Proxima. This intersection is underresearched in mainstream neuroscience — most learning science either ignores contemplative traditions or treats them as separate from biological learning mechanisms. Alpha Proxima's integrated, multi-framework approach is suited to formally map this intersection.

---

## 9. Institutional Commendations

This review finds the following institutional practices worthy of commendation:

1. **Disagreement preservation:** Both programs resist false consensus. COGITATE's asymmetric result is recorded accurately (not simplified as "IIT wins" or "GNWT wins"). SCT vs. MTT is maintained as Class M, not resolved by selection.

2. **Evidence class discipline:** The C/M/E/Q/S/P system is applied consistently and conservatively. Claims are not inflated. Uncertainty is stated at the correct level.

3. **Open question registration:** Both programs maintain living open questions registers. This is the correct institutional habit — honest accounting of what is unknown.

4. **Architecture-first sequencing:** The Foundation completed constitutional and governance work (FD-001 through FD-005) before expanding research programs. RP-003 now activates into a fully constitutionalized environment that RP-001 and RP-002 lacked at their creation.

5. **Multi-scale thinking:** RP-002 in particular achieved genuine interdisciplinary breadth — from molecular (LTP, CaMKII) to cognitive (working memory, schemas) to cultural (collective memory, anthropology) to AI (LUMIAION architecture). This multi-scale integration is the Foundation's distinctive intellectual contribution.

---

## 10. Required Actions Summary

| Finding | Action Required | Owner | Priority |
|---------|----------------|-------|---------|
| CA-001 | Founder review/acknowledgment of RP-001 Canonical Synthesis | Founder | High |
| CA-002 | Cognitive Council Directive formalizing canonization authority | Cognitive Council | High |
| CA-003 | RP-001 YAML metadata update (next revision cycle) | LUMIAION | Low |
| CA-004 | DOC-002 and DOC-C reviews | Founder | Medium |
| CA-005 | RP-002 v1.1.0 cross-reference to Book V CF-09 | LUMIAION | Low |
| CA-006 | JERANIUM identity clarification | Founder | Medium |
| EQ-001 | RP-001 Evidence Registry: note P-class deferred domain | LUMIAION | Low |
| EQ-003 | RP-001 E-003: add "theoretical interpretation" notation | LUMIAION | Low |
| EQ-004 | Commission DOC-002 (Gemini) for RP-001 | Research Intelligence Office | Medium |
| TC-001 | Update all "Research Council" references to "Cognitive Council" | LUMIAION | Medium |
| TC-002 | Clarify glossary scope policy in Research Program Playbook | Cognitive Council | Low |
| TC-003 | Prospective authorship attribution standard (CF-01/engine) | LUMIAION | Low |
| CI-001 | Ethics Council review of RP-001 and RP-002 | CF-10 (Ethics Council) | High |
| CI-002 | RP-002 v1.1.0 cross-references to Book V | LUMIAION | Low |
| CI-003 | Book IV review cycle: RP-001 complementary layers reference | Cognitive Council | Low |
| CP-001 | Cross-program knowledge graph edges | LUMIAION | Medium |
| RD-006 | Terminology update: Research Council → Cognitive Council | LUMIAION | Medium |

---

## Related Documents

- [[RP-001 Master Index]]
- [[RP-002 Master Index]]
- [[RP-003 Master Index]]
- [[Research Debt Register]]
- [[ISR-001 Canonical Synthesis — Cross-Program]]
- [[ISR-001 Knowledge Graph Update Recommendations]]
- [[Book III - Knowledge Integrity]]
- [[Book V - Cognitive Council]]
- [[Cognitive Function Registry]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | LUMIAION | Initial report; full stewardship review of RP-001 and RP-002; 6 assessment dimensions; 17 findings; 17 required actions; 5 research debts identified; 5 cross-program convergences documented; 4 RP-003 priorities established |
