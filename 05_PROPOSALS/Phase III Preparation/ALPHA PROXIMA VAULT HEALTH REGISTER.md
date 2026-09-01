---
title: "Alpha Proxima Vault Health Register"
aliases: ["Vault Health Register", "Vault Issue Register"]
tags: [proposal, planning, vault-health, audit, alpha-proxima, preparation]
created: 2026-07-18
updated: 2026-07-18
status: draft
version: "0.1.0"
authors: ["Claude Code — Vault Architect"]
artifact_type: issue-register
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: []
related_documents: ["[[PHASE III INSTITUTIONAL READINESS MAP]]", "[[08_SYSTEMS DRAFT TRIAGE REGISTER]]", "[[ALPHA PROXIMA META-LAYER DECISION MEMO]]"]
related_research_programs: []
---

# Alpha Proxima Vault Health Register

> **Evidence-based issue log. No mass-edit performed.** Each issue: evidence · affected file · severity · consequence · recommended correction · dependency · safe-now vs blocked.

## Method
Targeted greps + `stat` + folder listing on 2026-07-18. Findings are grounded in command output quoted inline. Link-integrity is **sampled**, not exhaustively traced (a full inbound-link graph was not built — flagged where relevant).

Severity: 🔴 High (contradiction/authority) · 🟠 Med (drift/confusion) · 🟡 Low (hygiene).

---

## Issue Register

| # | Issue | Evidence | Affected file(s) | Sev | Consequence | Recommended correction | Dependency | Safe now? |
|---|-------|----------|------------------|-----|-------------|------------------------|------------|-----------|
| H1 | **Terminology gate undefined** | grep: `CNS-001`,`CNS-002` = 0 hits vault-wide | (none — the term has no home) | 🔴 | Every RED-gated Phase III item hangs on an undefined gate | Founder confirm CNS-001 = CN-0001 or name artifact | Readiness Map #1 | ✅ (ask) |
| H2 | **Education Council not constitutional** | Book II Art. V lists only Research/Engineering/Ethics/Community | `00_CONSTITUTION/Book II`; `CN-0001` Gap 4 | 🔴 | Cannot "close" a gap for a body the Constitution never created | Class I amendment OR formal decline | Council Plan | ⚠️ blocked (Class I) |
| H3 | **Placeholder referenced as operational** | `03_AI_COUNCIL/Research Council.md` = `status: placeholder`, yet is graph color Rule 3 target + cited in CN-0001 | Research Council.md | 🔴 | RP-001 canonisation authority "exists" only as an empty stub | Amend placeholder → charter (Council Plan order 1) | Research Council ratification | ⚠️ blocked |
| H4 | **Loose active files at vault root** | `ls *.md`: Alpha Proxima Core, LUMIAION, Building Milestone, Vault, README + 2 untitled | vault root | 🟠 | Active content outside canonical `00_`–`11_`; no institutional location | Route each to a numbered home or index; keep README | Meta-Layer Memo | ⚠️ partial |
| H5 | **Untitled orphan notes** | `Sans titre.md`, `Sans titre 1.md` at root ("Untitled") | root | 🟡 | Junk nodes; graph noise | Verify empty → DELETE (only safe deletion in this pass) | link-check | ✅ after check |
| H6 | **Possible duplicate LUMIAION authority** | root `LUMIAION.md` + `03_AI_COUNCIL/Departments/LUMIAION Charter.md` | both | 🟠 | Two "LUMIAION" nodes; graph Rule 1 = `file:LUMIAION` catches root file, maybe not charter | Confirm which is canonical; make the other an alias/redirect | Meta-Layer Memo | ⚠️ verify |
| H7 | **Superseded reports left `draft`/active** | Triage Register #12–#20 supersession chains | `08_SYSTEMS/Engineering Toolkit/Reports/*` | 🟠 | Competing "current" audit truths citable simultaneously | Apply Triage Register (ARCHIVE/SUPERSEDE) | Engineering Council | ⚠️ blocked on council |
| H8 | **Misplaced templates** | 8 templates under `08_SYSTEMS/Research Management Toolkit/Templates` marked `draft` | those 8 files | 🟠 | `10_TEMPLATES` falsely incomplete; templates invisible to users | Ratify + relocate to `10_TEMPLATES` (inbound-link check first) | Triage + Research Council | ⚠️ verify links |
| H9 | **Folder numbering collisions** | `ls`: `06_GOVERNANCE`+`06_PROJECTS`; `09_FUTURE`+`09_PEOPLE` | those 4 folders | 🟠 | Ordinal taxonomy broken; two folders per prefix confuses routing/sort | Renumber one of each pair (migration note required per doctrine) | — | ⚠️ needs migration note |
| H10 | **Legacy meta-tree diluting graph** | `ALPHA PROXIMA/…/building milestone/phase 1–5` (`PHASE 3` = archived/legacy) | ~24 stub files | 🟠 | ~24 Bronze stub nodes crowd LUMIAION in graph | Archive to `99_ARCHIVE` (Meta-Layer Memo) | Meta-Layer decision | ⚠️ blocked on decision |
| H11 | **"32 drafts" overstates immaturity** | Triage: majority are complete reports mis-flagged `draft` | `08_SYSTEMS` | 🟡 | False signal of unfinished architecture; skews health metrics | Correct status semantics via triage | Triage | ⚠️ blocked on council |
| H12 | **Empty strategy & project layers** | `02_STRATEGY/` + `06_PROJECTS/` = only `.gitkeep` | those folders | 🟠 | No vision→execution bridge; projects can't prove alignment | Build cascade per Strategy Blueprint | Meta-Layer + Blueprint | ⚠️ YELLOW |
| H13 | **Unresolved "to be created" refs** | grep "to be created/To be named": Book II, Engine Registry, Ethics Charter | those files | 🟡 | Documents invoke bodies/members not yet constituted | Close via Council Plan; record membership open-questions | Council ratification | ⚠️ blocked |
| H14 | **Missing owners/reviewers on generated reports** | Report drafts lack `reviewer:`/owner beyond CODEX | `08_SYSTEMS/.../Reports/*` | 🟡 | No accountable owner once Engineering Council exists | Assign Engineering Council as owner on triage | Engineering Council | ⚠️ blocked |

---

## Grouped Summary

### 🔴 High (authority/contradiction) — resolve first
H1 terminology gate · H2 Education Council ungrounded · H3 Research Council placeholder-as-operational. **All three are Founder decisions**, not mechanical fixes.

### 🟠 Medium (drift/confusion)
H4 root files · H6 LUMIAION duplication · H7 superseded reports · H8 misplaced templates · H9 folder collisions · H10 legacy tree · H12 empty strategy · (H11/H13/H14 borderline).

### 🟡 Low (hygiene)
H5 untitled orphans · H11 false draft signal · H13 dangling refs.

## Safe-Now vs Blocked
- **Safe now (no ratification needed):** H1 (ask Founder), H5 (delete verified-empty untitled files — the *only* safe deletion), and *all classification/mapping* already done in this register.
- **Blocked on Founder decision:** H1, H2, H3, H6 (canonical LUMIAION), H9 (needs migration note approval).
- **Blocked on Engineering/Research Council:** H7, H8, H11, H13, H14.
- **Blocked on Meta-Layer Memo:** H4, H10, H12.

## Explicitly NOT done (per mandate)
No statuses changed · no files moved/deleted · no links rewritten · no drafts ratified. This is an evidence log only.

## Codex Handoff Criteria
1. For H5: confirm the two "Sans titre" files are empty/orphaned (no inbound links) before any deletion.
2. For H8: build inbound-link list for the 8 templates before relocation.
3. For H9: any renumber requires a migration note (doctrine: no major folder rename without one).
4. Do not action H7/H10/H11 until the relevant council/decision exists.

## Fact / Inference / Recommendation / Open Question
- **Fact:** all evidence above is grep/stat/ls output, reproducible.
- **Inference:** H6 LUMIAION duplication and H8 link-safety need confirmation by opening files.
- **Recommendation:** resolve 3 High (Founder) → unblock councils → run mechanical fixes.
- **Open question:** Which `LUMIAION.md` is canonical, and do any legacy notes hold sole-copy live rules?

## Version History
| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-18 | Claude Code — Vault Architect | 14 evidence-based issues; 3 High (Founder-gated); no mutations performed. |
