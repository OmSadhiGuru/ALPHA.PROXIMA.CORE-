---
title: "Governance Model Crosswalk & Council Topology"
aliases: ["Governance Crosswalk", "Model Crosswalk", "Council Topology"]
tags: [governance, crosswalk, cognitive-functions, councils, epoch-v, alpha-proxima]
created: 2026-09-01
updated: 2026-09-01
status: proposed — pending Founder ratification
version: "0.1.0"
authors: ["LUMIAION (CF-01)"]
document_class: Governance Reconciliation
initiative: "Epoch V — Constitutional Coherence"
resolves: ["CAR-F01", "CAR-F14", "M-02", "M-04"]
---

# Governance Model Crosswalk & Council Topology

*Epoch V · Resolves CAR-F01 (three parallel, contradictory AI-governance models) and CAR-F14 (three overlapping council names), and delivers Missing-Documents M-02 and M-04. Establishes the **Cognitive Function model as canonical**, maps the two legacy models onto it, and fixes the scope of each council. Proposed by CF-01; **pending Founder ratification.***

---

## Part A — The canonical model

Per **Book IV (Cognitive Architecture)** and **Book V (Cognitive Council)**, the **Cognitive Function model (CF-01 … CF-14)** is the single canonical model. The two earlier models are **superseded** and retained only as historical records:

- **Chief Architects model** (Epoch I, `AI Council Registry`) — *superseded*.
- **Departments model** (Epoch I–II, `03_AI_COUNCIL/Departments/`) — *superseded*.

"Superseded" means: no longer authoritative for current operation; not deleted; each legacy document gains a banner pointing to this crosswalk.

---

## Part B — Crosswalk (legacy → canonical)

| Legacy: Chief Architect | Legacy: Department | → Canonical Cognitive Function | Current engine (per CF Registry) |
|-------------------------|--------------------|-------------------------------|----------------------------------|
| Chief Systems Architect | — | CF-01 Institutional Architecture (orchestration aspect) | Claude |
| Chief Knowledge Architect | (LUMIAION coord.) | CF-01 Institutional Architecture | Claude |
| Chief Research Architect | JERANIUM (research/synthesis) | CF-02 Research Intelligence | Perplexity |
| Chief Science Architect | ATHENA (science aspect) | CF-03 Comparative Intelligence / CF-12 Health | SanaLab / ATHENA Office |
| — (Educational) | — | CF-04 Educational Intelligence | Gemini |
| Chief Deep Investigation Architect | — | CF-06 Executive Intelligence (investigation aspect) | Genspark |
| Chief Engineering Architect | — | CF-07 Engineering Intelligence | Codex / DeepSeek |
| Chief Memory Architect (unfilled) | — | CF-09 Memory Intelligence | LUMIAION multi-engine |
| — | SOHMA (symbolic/contemplative) | CF-14 Metaphysical Intelligence | SOHMA Office |
| — | VORTEX (finance) | CF-13 Financial Intelligence | VORTEX Office |
| — | JERANIUM (data/analytics) | **CF-15 Data & Systems Intelligence** *(new — see Part C)* | To be appointed |

*Note: some legacy roles split across more than one CF because the canonical model separates functions the old models had bundled. The CF Registry remains the authoritative per-function record.*

---

## Part C — JERANIUM reconciliation (resolves CAR-F03 / RD-002)

JERANIUM was **doubly defined**: the Departments charter cast it as *Knowledge & Institutional Intelligence* (research, pattern detection, knowledge-graph health); the LUMIAION Constitution cast it as *data orchestration, analytics, system optimization*. Reconciliation:

- JERANIUM's **research / knowledge-synthesis** functions are **absorbed by CF-02 (Research Intelligence)** and **CF-01 (Institutional Architecture)** — where they already live in the canonical model.
- JERANIUM's **distinctive** remaining function — **data orchestration, analytics, system optimization** (the LUMIAION Constitution definition) — is registered as a new cognitive function: **CF-15 — Data & Systems Intelligence** (infrastructure class, engine to be appointed).
- The Departments `JERANIUM Charter` is marked **superseded**; RP-001's JERANIUM co-authorship is re-attributed to CF-02/CF-01 as historical contribution.

This closes the true state of **RD-002** (which incorrectly claimed no JERANIUM charter existed): the problem was contradiction, not absence, and it is resolved by assignment to CF-15 + supersession of the legacy charter.

---

## Part D — Council Topology (resolves CAR-F14 / M-04)

Three council names operate; their scopes are now distinct and their escalation order fixed:

| Council | Scope | Authority | Escalates to |
|---------|-------|-----------|--------------|
| **Cognitive Council** (Book V) | Operational governance of the cognitive-function portfolio (CF-01…CF-15): appointments-in-principle, engine succession, function lifecycle | Operational | AI Council (for ratification) |
| **AI Council** → renamed **AI Ratification Council** | Constitutional ratification of engine appointments and AI-architecture changes | Ratifying | Alpha Council / Founder |
| **Alpha Council** (Book I) | Supreme deliberative/executive body; constitutional amendments; supreme disputes | Supreme | Founder (constituent) |
| **Ethics Council** (CF-10) | Ethical/constitutional oversight across all of the above | Oversight (cross-cutting) | Alpha Council / Founder |

**Escalation order:** Cognitive Council → AI Ratification Council → Alpha Council → Founder. The Ethics Council may inject at any level. The folder `03_AI_COUNCIL/` is renamed in intent to hold the AI Ratification Council + the Cognitive Function registries; the **Cognitive Council** is the live operational body.

This removes the AI Council / Cognitive Council authority overlap: **Cognitive Council operates; AI Ratification Council ratifies; Alpha Council/Founder holds supremacy.**

---

## Part E — Enactment checklist (Epoch V)

- [ ] Add "superseded — see Governance Model Crosswalk" banner to `AI Council Registry` and each `Departments/*` charter.
- [ ] Amend the **Cognitive Function Registry** to add **CF-15 Data & Systems Intelligence** (JERANIUM) and update the JERANIUM entry.
- [ ] Create/relocate the **Ethics Council** to `09_OFFICES/Ethics Council/` (CAR-F11).
- [ ] Update **RD-002** to resolved-pending-registry-amendment.
- [ ] Reflect the Council Topology in Book II (or a linked governance note).

---

## Status

**Proposed — pending Founder ratification** (Alpha Council seats unfilled, CAR-F04). The crosswalk is a reconciliation *proposal*; supersession of the legacy models becomes binding on ratification.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-09-01 | LUMIAION (CF-01) | Canonical = Cognitive Function model; legacy Chief Architects + Departments superseded; full crosswalk; JERANIUM reconciled to new CF-15 + CF-02/01 (resolves RD-002); Council Topology with fixed escalation order. Pending Founder ratification. |
