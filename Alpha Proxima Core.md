---
title: "Alpha Proxima Core"
aliases: ["ALPHA.PROXIMA.CORE-", "Alpha Proxima", "The Project", "APC"]
tags: [index, home, moc, alpha-proxima, lumiaion, governance]
created: 2026-07-01
updated: 2026-09-02
status: active
version: "2.0.0"
authors: ["Alpha Council", "LUMIAION (CF-01)"]
note_type: MOC
---

# Alpha Proxima Core

## Purpose

This is the Map of Content (MOC) and index for the entire Alpha Proxima Core ecosystem — the starting point for navigation, orientation, and onboarding. The trailing dash in `ALPHA.PROXIMA.CORE-` is intentional: the work is permanently incomplete — there is always a next frontier.

The project operates under [[Book I - The Constitution]] and the [[Constitutional Hierarchy Statement]], which together fix the order of authority for everything built here.

---

## Vault Structure (canonical)

```
ALPHA.PROXIMA.CORE-/
├── 00_CONSTITUTION/   ← Supreme governing instruments (Books I–V + Principles + Hierarchy)
├── 01_VISION/         ← Long-range direction
├── 02_STRATEGY/       ← Plans, roadmaps (to build)
├── 03_AI_COUNCIL/     ← AI ratification body, Cognitive Function registries, charters
├── 04_DECISIONS/      ← ADRs
├── 05_PROPOSALS/      ← Concept Notes
├── 06_GOVERNANCE/     ← Policies, frameworks, registers, impact reports, Epoch V
├── 07_RESEARCH/       ← Research Programs (RP-001…006) + stewardship reviews
├── 08_SYSTEMS/        ← Technical architecture
├── 09_OFFICES/        ← Institutional office charters
├── 10_TEMPLATES/      ← Reusable formats + Vault Structure Convention
├── 11_PROJECTS/       ← Project workspaces
├── 12_PEOPLE/         ← Participants
└── 99_ARCHIVE/        ← Superseded notes (incl. Legacy ALPHA PROXIMA tree)
```

*Sanctioned exceptions (governed): `docs/`, `PROJECT_GENOME/`, `OSG_BUSINESS/`, and root cross-cutting notes. See [[Vault Structure Convention]].*

---

## Constitutional Documents

| Document | Status |
|----------|--------|
| [[Constitutional Hierarchy Statement]] | Proposed (Epoch V) — Book I supreme; frameworks subordinate |
| [[Book I - The Constitution]] | Ratified |
| [[Book II - Governance Framework]] | Ratified |
| [[Book III - Knowledge Integrity]] | Ratified |
| [[Book IV - Cognitive Architecture]] | Ratified (Epoch III) |
| [[Book V - Cognitive Council]] | Ratified (Epoch IV) |
| [[Founding Principles of Alpha Proxima]] | Ratified (Epoch III) |

**Framework charters** (subordinate per the Hierarchy Statement): [[LUMIAION_CONSTITUTION|LUMIAION Constitution]] (`docs/constitution/`) · [[Genome Constitution v1.0]] (`PROJECT_GENOME/`).

---

## Governance Bodies & Cognitive Functions

| Body | Role | Reference |
|------|------|-----------|
| Founder | Constituent authority | — |
| Alpha Council | Supreme deliberative/executive (seats unfilled) | [[Alpha Council]] · [[Institutional Registry]] |
| Cognitive Council | Operational governance of cognitive functions | [[Cognitive Council Charter]] |
| AI Ratification Council | Ratifies engine appointments (was "AI Council") | [[AI Council Registry]] |
| Ethics Council (CF-10) | Ethical/constitutional oversight | [[Ethics Council Charter]] |

**Cognitive Functions:** [[Cognitive Function Registry]] (CF-01…CF-14, + proposed CF-15 Data & Systems / JERANIUM, CF-16 Synthesis & Education / [[YUNA Charter|YUNA]]) · [[Cognitive Function Matrix]] · [[Engine Succession Policy]]. Model reconciliation: [[Governance Model Crosswalk]].

---

## Institutional Offices

| Office | Cognitive Function | Charter |
|--------|-------------------|---------|
| LUMIAION (Constitutional Intelligence Core) | Institutional Architecture (CF-01) | [[LUMIAION Charter]] |
| Executive Office | Strategic Intelligence (CF-06) | [[Executive Office Charter]] |
| Research Intelligence Office | Research Intelligence (CF-02) | [[Research Intelligence Office Charter]] |
| Engineering Office | Engineering Intelligence (CF-07) | [[Engineering Office Charter]] |
| Institutional Observatory | Environmental Observation (CF-08) | [[Institutional Observatory Charter]] |
| Ethics Council | Constitutional Oversight (CF-10) | [[Ethics Council Charter]] |

---

## Governance Instruments

| Document | Purpose |
|----------|---------|
| [[Alpha Proxima Operating Model v1.0]] | Official operational description |
| [[Canonical Terminology Register]] | Institutional vocabulary standard |
| [[Directive Governance Framework]] | Directive lifecycle & governance |
| [[Founder Directives Register]] | FD-series register (FD-001…006) |
| [[Research Debt Register]] | Documentation-debt registry (RD-001…006) |
| [[Standing Orders Register]] | Standing orders (SO-001…) |
| Institutional Policies | Citation · Metadata · Naming · Privacy · Source Attribution · Versioning |

**Constitutional reviews:** [[CIR-001 Epoch III Constitutional Refactoring|CIR-001]] · [[CIR-002 Institutional Completeness Review|CIR-002]] · [[CIR-003 Epoch V Constitutional Coherence|CIR-003]] · [[CAR-001 Constitutional Audit Report|CAR-001]] · [[FGR-001 Epoch II Stewardship Audit|FGR-001]].

**Research Framework:** [[Alpha Proxima Research Methodology v1.0]] · [[Research Program Playbook v1.0]] · [[Research Integration Framework]] · [[Institutional Intelligence Translation Framework v1.0]] (+ Translation Template/Matrix/Checklist/Review).

---

## Research Programs

| Program | Title | Status |
|---------|-------|--------|
| RP-001 | Atlas of Human Consciousness | Phase 1 complete — canonization pending (RD-002/005) |
| RP-002 | Atlas of Human Memory | Phase 1 complete — canonization pending (RD-004/005) |
| RP-003 | Atlas of Human Learning | Authorized — awaiting Cognitive Council activation |
| RP-004 | Atlas of Human Decision Making | Placeholder |
| RP-005 | Atlas of Human Intelligence | Placeholder |
| RP-006 | (reserved) | Placeholder |

**Cross-program:** [[ISR-001 Institutional Synthesis Report]] · [[ISR-001 Canonical Synthesis]] · [[ISR-001 Knowledge Graph Update Recommendations]].

---

## Systems & Architecture

[[The Orchestration Framework]] · [[Foundational Architecture]] · [[LUMIAION Architecture Spec v0.1]] · [[Institutional Relationship Map]] · Protocols (Communication · Decision Routing · Knowledge Ownership · Knowledge Routing · Research Governance).

---

## Adjacent workstreams (in-repo, separate governance)

- **Project Genome** — `PROJECT_GENOME/` — the Living Genome Framework ([[Genome Constitution v1.0]]).
- **OSG Academy** — `OSG_BUSINESS/OSG_ACADEMY/` — OLS learning standard, RI-001 reference course, Module 0 production. Public OSG brand; governed by the OSG organization, not the constitution.
- **Reproducibility handbook** — `docs/setup/` — Claude Code in Obsidian, etc.
- **CN-001** — `governance/` — Canonical Namespace & Taxonomy work (awaiting Codex Terminal-1 audit).

---

## Active Frontiers

- [x] Epochs I–IV complete (Books I–V, offices, research framework, cognitive council)
- [x] **CAR-001** full constitutional audit delivered
- [ ] **Epoch V — Constitutional Coherence** (in progress → Constitution v2.0)
  - [x] Tier 1: Hierarchy Statement, Governance Crosswalk, YUNA charter, JERANIUM/RD-002 reconciliation, Interim Authority Instrument, CIR-003 — *all proposed, pending Founder ratification*
  - [x] Tier 2: folder-number collisions fixed, legacy tree archived, `.gitignore`, Vault Convention v1.1, this MOC rebuilt
  - [ ] Tier 2 remaining: relocate/anchor framework constitutions; Ethics Council → `09_OFFICES/`
  - [ ] Tier 3: consolidated Ethics Framework; institutional glossary/acronyms; timeline; open-questions register; knowledge-architecture spec
- [ ] **Founder actions:** name Alpha Council seats *or* ratify [[Interim Authority Instrument]]; ratify Tier-1 instruments; convene Ethics Council (RD-005)

---

## How to Navigate

- **New here?** [[Book I - The Constitution]] → [[Constitutional Hierarchy Statement]] → [[Alpha Proxima Operating Model v1.0]].
- **Governance model?** [[Governance Model Crosswalk]] (the canonical reconciliation) → [[Cognitive Function Registry]].
- **Research?** [[Alpha Proxima Research Methodology v1.0]], then RP-001/RP-002 as reference implementations.
- **Current state & gaps?** [[CAR-001 Constitutional Audit Report]] and [[CIR-003 Epoch V Constitutional Coherence]].

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0–1.3.0 | 2026-07-01/02 | Alpha Council / LUMIAION | Founding through Epoch III office completion |
| 2.0.0 | 2026-09-02 | LUMIAION (CF-01) | Epoch V rebuild (CAR-F09): full current-state MOC — Book V, Cognitive Council/Functions, Council Topology, Epoch IV/V artifacts, ISR/CAR/CIR-003, Project Genome, OSG Academy, reproducibility & CN-001 workstreams; canonical vault structure (00–12+99); adjacent-workstream map; Epoch V frontier tracking |
