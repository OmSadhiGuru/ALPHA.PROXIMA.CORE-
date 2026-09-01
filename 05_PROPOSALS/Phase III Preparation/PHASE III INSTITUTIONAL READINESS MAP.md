---
title: "Phase III Institutional Readiness Map"
aliases: ["Phase III Readiness Map", "Parallel Preparation Dependency Map"]
tags: [proposal, planning, phase-iii, readiness, dependency-map, alpha-proxima, preparation]
created: 2026-07-18
updated: 2026-07-18
status: draft
version: "0.1.0"
authors: ["Claude Code — Vault Architect"]
artifact_type: readiness-dependency-map
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Orchestration"
reasoning_engine: "LUMIAION"
dependencies: ["[[CN-0001 - Constitutional Alignment Gap Report]]", "[[Book II - Governance Framework]]"]
related_documents: ["[[CN-0001 COUNCIL CLOSURE IMPLEMENTATION PLAN]]", "[[08_SYSTEMS DRAFT TRIAGE REGISTER]]", "[[ALPHA PROXIMA META-LAYER DECISION MEMO]]", "[[02_STRATEGY ARCHITECTURE BLUEPRINT]]", "[[ALPHA PROXIMA VAULT HEALTH REGISTER]]"]
related_research_programs: []
---

# Phase III Institutional Readiness Map

> **Preparation-only artifact.** This document maps dependencies and gates. It does not authorise, implement, ratify, or merge anything. It is the master index for the five preparation packages produced under the Parallel Architecture Preparation Mandate.

## Purpose

Provide a single dependency map that shows what can safely move now while the active technical gate closes, what must wait for a named prerequisite, and what is prohibited until constitutional ratification. Every item is classified GREEN / YELLOW / RED.

---

## Critical Terminology Discovery (must resolve before RED work)

| Term (as used in mandate) | Vault evidence | Interpretation | Status |
|---|---|---|---|
| **CNS-001** ("active technical gate, final closure") | **No literal string `CNS-001` exists anywhere in the vault.** | Most likely the Founder's shorthand for the **CN-0001 Constitutional Alignment Gap Report** (`05_PROPOSALS/`, status `active`, "gaps being closed"). | ⚠️ **Unresolved — Founder must confirm** |
| **CNS-002** | No literal string exists. | Presumed the *next* Concept Note / constitutional step after the gap closure. | ⚠️ Inference only |
| **AxiomNexus** | Appears **once**, as "Axiom Nexus" — a product-line concept with ID scheme `AXN-###` in [[LUMIAION - Operating Manual (LOOM)]] line 233. | A product/pipeline concept, **not** an existing interface or constitutional body. | ⚠️ Inference only |
| **Phase III** | "Phase 3 - Intelligence" exists but is `status: archived` legacy under `ALPHA PROXIMA/…/building milestone/phase 3/`. | The mandate's "Phase III" is a *new forward phase*, unrelated to the archived legacy note of the same name. | ⚠️ Naming collision — see Vault Health Register |

**Consequence:** All RED-gated work below is gated on "CNS-001 ratification." Until the Founder confirms that CNS-001 = CN-0001 (or names the actual artifact), the gate itself is ambiguous. **This is the first Founder decision required.** Everything GREEN proceeds regardless.

---

## Dependency Map

Legend: **BB** = blocked by · **UB** = unblocks · complexity S/M/L/XL

| # | Item | BB | UB | Owner | Reviewer | Cplx | Decision authority | Evidence required | Start condition | Completion condition |
|---|------|----|----|-------|----------|------|--------------------|-------------------|-----------------|----------------------|
| 1 | **CNS-001 closure** (= CN-0001?) | Founder disambiguation | Councils, CNS-002 | Founder / LUMIAION | Ethics Council | M | Founder (Class I/II) | Gap report resolution record | Founder confirms scope | Founder marks CN-0001 gaps resolved |
| 2 | **Council gap closure** (Research, Engineering, ±Education, ±Community) | #1 | Research canonisation, infra governance | Executive Council | Ethics Council | L | Executive Council concur + Founder (Class II) | Charters drafted + reviewed | #1 ratified | 4 charters ratified |
| 3 | **08_SYSTEMS draft triage** | none (GREEN) | Phase III clean base | Chief Eng. Architect | Codex | M | Specialist council (Class III) | Triage register (this package) | Now | All 32 drafts dispositioned |
| 4 | **Strategy bridge** | none for *structure* (GREEN); content needs #1 | Project alignment proofs | Executive Council | LUMIAION | L | Executive Council | Blueprint (this package) | Now (structure) | Blueprint approved; skeleton built |
| 5 | **Meta-layer decision** | none (GREEN) | Command-plane clarity | Founder / LUMIAION | Codex | S | Founder | Decision memo (this package) | Now | Founder picks model 1–5 |
| 6 | **CNS-002 prerequisites** | #1, #2 | AxiomNexus constitutional work | LUMIAION | Ethics Council | L | Founder | Confirmed CNS-001 outcome | #1 + #2 done | Prereqs enumerated & met |
| 7 | **AxiomNexus constitutional work** | #6 | Interface build | Executive + Ethics | Ethics Council | XL | Founder (Class I) | CNS-002 ratified | #6 done | Constitutional basis ratified |
| 8 | **UX blueprint** | #7 (constitutional envelope) | Founder MVP | Eng. Council | Codex | L | Eng. Council | Ratified constraints | #7 defines envelope | Blueprint approved |
| 9 | **Technical architecture** | #3, #7 | Founder MVP | Eng. Council | Codex | XL | Eng. Council | Clean systems base + constraints | #3 + #7 done | Architecture spec ratified |
| 10 | **Founder MVP** | #8, #9 | — | Founder / Codex | Ethics + Eng. | XL | Founder | All above | #8 + #9 done | MVP demonstrated |

---

## Traffic-Light Classification

### 🟢 GREEN — Safe to prepare now (research, mapping, classification, proposals, acceptance criteria)

- **Council Closure Package** — draft the four council charters + implementation plan (Workstream 1). *Drafting only; no ratification.*
- **08_SYSTEMS Draft Triage Register** — classify all 32 drafts (Workstream 2). *Classification only; no status changes.*
- **Meta-Layer Decision Memo** — classify placeholders, recommend a model (Workstream 3). *No population.*
- **Strategy Architecture Blueprint** — design the empty scaffold levels (Workstream 4). *Structure only; no strategy content.*
- **Vault Health Register** — evidence-based issue log (Workstream 6). *No mass-edit.*
- **CNS-001 disambiguation question** to Founder.

### 🟡 YELLOW — May begin only after a named prerequisite

| Work | Named prerequisite |
|------|--------------------|
| Convert any council charter draft → ratified | #1 CNS-001 confirmed + Executive Council concurrence |
| Apply any 08_SYSTEMS triage recommendation (archive/merge/delete) | Chief Engineering Architect sign-off + Codex review |
| Build the strategy bridge skeleton files | #5 meta-layer model chosen (avoids duplicate command layers) |
| Populate `03_AI_COUNCIL/Research Council.md` placeholder | #2 Research Council Charter ratified |
| Enumerate CNS-002 prerequisites in detail | #1 ratified |

### 🔴 RED — Prohibited until CNS-001 ratified (hard stop)

- Any modification to CNS-001 / CN-0001 content.
- Declaring CNS-001 closed.
- Implementing CNS-002.
- Building the AxiomNexus interface.
- Activating (constituting membership of) any council.
- Converting drafts to `ratified`.
- Ratifying any constitutional (Book) document.
- Production integration / MVP construction.

---

## Contradiction Watch (halt trigger)

Per the mandate's ordering rule, a later workstream must halt if an earlier one changes its assumptions. Two live contradictions could do so:

1. **CNS-001 ↔ CN-0001 identity** (unresolved) — if the Founder says these are *different* artifacts, Workstream 1's gate assumption changes.
2. **Education Council constitutional grounding** — Book II Art. V lists only Research, Engineering, Ethics, Community. **Education Council is NOT in the Constitution** (see Council Closure Plan). If confirmed, Workstream 1 cannot "close" an Education Council gap without a Class I amendment first.

---

## Fact / Inference / Recommendation / Open Question

- **Observed fact:** CNS-001/CNS-002/AxiomNexus-as-interface do not exist as vault artifacts; CN-0001 does and is active. Book II Art. V omits Education Council.
- **Inference:** CNS-001 ≈ CN-0001; "Phase III" is a new forward phase distinct from the archived legacy note.
- **Recommendation:** Confirm terminology before any YELLOW/RED work; run all six GREEN packages in parallel now.
- **Open question:** Is CNS-001 identical to CN-0001, or a separate technical gate the Founder is tracking outside the vault?

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-18 | Claude Code — Vault Architect | Initial readiness map; GREEN/YELLOW/RED classification; terminology discovery flagged. |
