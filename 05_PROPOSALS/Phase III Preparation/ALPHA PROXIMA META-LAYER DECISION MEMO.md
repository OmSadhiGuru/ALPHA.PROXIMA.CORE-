---
title: "Alpha Proxima Meta-Layer Decision Memo"
aliases: ["Meta-Layer Decision Memo", "ALPHA PROXIMA Root Decision"]
tags: [proposal, planning, meta-layer, governance, alpha-proxima, preparation]
created: 2026-07-18
updated: 2026-07-18
status: draft
version: "0.1.0"
authors: ["Claude Code — Vault Architect"]
artifact_type: decision-memo
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Orchestration"
reasoning_engine: "LUMIAION"
dependencies: ["[[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]]"]
related_documents: ["[[PHASE III INSTITUTIONAL READINESS MAP]]", "[[02_STRATEGY ARCHITECTURE BLUEPRINT]]", "[[ALPHA PROXIMA VAULT HEALTH REGISTER]]"]
related_research_programs: []
---

# Alpha Proxima Meta-Layer Decision Memo

> **Recommendation, not implementation.** No placeholder is populated, moved, or deleted by this memo. It classifies what exists and recommends a canonical purpose for Founder decision.

## Grounding Evidence

`ALPHA PROXIMA/` (root, outside numbered structure): **28 md files, 20 placeholders, 0 active.** Two sub-structures:

1. **Top-level command stubs:** `NOTION COMMAND CENTER.md`, `OBSIDIAN VAULT.md` (both `status: placeholder`).
2. **Legacy build tree** `ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/`:
   - `building milestone/phase 1…5/` — legacy phase notes (e.g. `PHASE 3 - INTELLIGENCE.md` is `status: archived`, tagged `legacy`). Contains COST TIERS, ROUTING RULES, MEMORY RULES, MVP SPECIFICATION, HOSTING OPTIONS, AUTOMATION PLAN, etc.
   - `Building achitecture/ALPHA PROXIMA ROLES/AI COUNCIL/{Claude.ai, ChatGPT, Gemini, Perplexity, DeepSeek, Google Notebook LLM}/` + `ARCHITECTURE MAP.md`, `AI COUNCIL.md` (placeholders).

**Key facts:**
- This tree **predates** the numbered canonical structure (`00_`–`11_`). Its content is largely **superseded** by ratified canon: e.g. AI Council roles now live in `03_AI_COUNCIL` + [[Engine Registry]]; routing rules in `08_SYSTEMS/Protocols/Knowledge Routing Protocol`; MVP/architecture in `08_SYSTEMS/Foundational Architecture`.
- It is **coloured "Alpha Proxima Bronze" (Rule 25)** in the graph — currently rendering ~28 stub nodes around the brain, **diluting graph readability** (the exact problem the color audit fought).
- `NOTION COMMAND CENTER` overlaps conceptually with the canonical [[ALPHAPROXIMA Enterprise Knowledge Architecture v1.0]] (the real master reference).

---

## Five Candidate Models (mandate list)

| # | Model | Fit assessment |
|---|-------|----------------|
| 1 | Canonical institutional command layer | ⚠️ Would **duplicate** the already-canonical AEKA master reference + `11_OPERATIONS` command surfaces. Risk of two command truths. |
| 2 | Future AxiomNexus control-plane docs | Premature — AxiomNexus is undefined (one AXN-### mention). Reserving the space is fine; populating is RED. |
| 3 | Index-only navigation layer | ✅ Low-risk, high-value: a thin, human-facing "front door" that links *into* canonical folders without holding authority. |
| 4 | Deprecated duplicate structure | ✅ Accurate for the **legacy build tree** specifically — it is a superseded duplicate. |
| 5 | Hybrid | ✅ **Recommended:** thin index/front-door (Model 3) at top + **archive the legacy build tree** (Model 4) + **reserve** a clearly-marked future AxiomNexus space (Model 2, empty). |

### ✅ Recommendation: **Hybrid (3 + 4 + reserved-2)**
- Keep `ALPHA PROXIMA/` as an **index-only front door** (Model 3): human-readable entry that links to `00_`–`11_` canon. It holds **navigation, never authority**.
- **Archive** `ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/` legacy build tree → `99_ARCHIVE/` (Model 4). It is superseded duplicate history.
- **Reserve** (do not populate) a future AxiomNexus control-plane location, explicitly marked "empty until CNS-002/AxiomNexus is constitutionally grounded" (Model 2).

---

## Per-Placeholder Classification

Vocabulary: REQUIRED · REDUNDANT · MISPLACED · FUTURE · DEPRECATE

| Placeholder / group | Class | Rationale |
|---------------------|-------|-----------|
| `NOTION COMMAND CENTER.md` | **REDUNDANT** | Overlaps canonical AEKA master reference; keep as *index link* to Notion, strip any authority claim |
| `OBSIDIAN VAULT.md` | **REQUIRED** (as index) | Legitimate front-door node → becomes the index-only entry point |
| `…/ALPHA PROXIMA ROLES/AI COUNCIL/*` (6 engine folders) | **DEPRECATE** | Superseded by `03_AI_COUNCIL` + [[Engine Registry]] |
| `…/ARCHITECTURE MAP.md`, `AI COUNCIL.md` | **DEPRECATE** | Superseded by Foundational Architecture + AI Council Registry |
| `…/building milestone/phase 1–5/*` | **DEPRECATE** | Legacy; `PHASE 3` already `archived`. Move whole tree to `99_ARCHIVE` |
| `…/phase 2/{CONCEPT NOTE, SOURCE NOTE, NAMING RULES, TAG TAXONOMY} ` | **MISPLACED** | If any is the *only* copy of a live convention, relocate to `10_TEMPLATES`/`08_SYSTEMS` before archiving parent (verify first) |
| `…/phase 4/{MVP SPECIFICATION, HOSTING OPTIONS, AUTOMATION PLAN, GITHUB REPO STRUCTURE}` | **FUTURE** vs **DEPRECATE** | Check against canonical `08_SYSTEMS` equivalents; keep only if it holds unique forward content, else DEPRECATE |
| Reserved AxiomNexus space | **FUTURE** | Create empty, clearly gated; do not populate |

> Every "relocate before archive" row requires an **inbound-link check first** (coordinate with Vault Health Register) so archiving doesn't break live links.

## Recommendation Detail

- **Canonical purpose:** A navigation index and (future) reserved control-plane shell. **Never** a second authority layer.
- **Folder boundaries:** `ALPHA PROXIMA/` = links + reserved shells only. Authority stays in `00_`–`11_`.
- **What belongs there:** vault front-door index, external-tool links (Notion), reserved AxiomNexus placeholder.
- **What must NEVER belong there:** ratified charters, canonical protocols, research artifacts, decisions — anything with authority. Those live in numbered canon.
- **Which placeholders to implement:** only `OBSIDIAN VAULT.md` (as index) + a new reserved AxiomNexus shell.
- **Which to archive:** the entire legacy `ALPHA.PROXIMA.FOUNDATION/` tree.
- **Naming conventions:** front-door notes ALL-CAPS acceptable as index labels; reserved shells prefixed `_RESERVED - `.
- **Indexing behavior:** index links out; nothing links *to* it as a source of truth.
- **Maintenance authority:** LUMIAION maintains the index; Engineering Council owns archival mechanics.

## Graph-Readability Note
Archiving the legacy tree removes ~24 stub nodes currently rendering "Alpha Proxima Bronze" around LUMIAION — directly improving the graph the earlier color passes were protecting. (They'd re-color to Archive Stone, Rule 19.)

## Founder Decision Points
1. Approve **Hybrid** model (or pick 1–5).
2. Approve archiving the legacy `ALPHA.PROXIMA.FOUNDATION/` tree to `99_ARCHIVE`.
3. Confirm whether a reserved AxiomNexus shell should be created now (empty) or deferred entirely.

## Fact / Inference / Recommendation / Open Question
- **Fact:** 28 files, 20 placeholders, 0 active; legacy tree superseded by numbered canon; NOTION COMMAND CENTER overlaps AEKA.
- **Inference:** legacy phase notes are pre-canon history, not live architecture.
- **Recommendation:** Hybrid — index front-door + archive legacy + reserve AxiomNexus shell.
- **Open question:** Are any `phase 2/4` convention notes the *sole* copy of a live rule? (must link-check before archiving).

## Version History
| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-18 | Claude Code — Vault Architect | Classified meta-layer; recommended Hybrid (index + archive legacy + reserve AxiomNexus). No population. |
