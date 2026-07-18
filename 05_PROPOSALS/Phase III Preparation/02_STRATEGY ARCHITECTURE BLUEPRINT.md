---
title: "02_STRATEGY Architecture Blueprint"
aliases: ["Strategy Bridge Blueprint", "Strategy Architecture"]
tags: [proposal, planning, strategy, architecture, alpha-proxima, preparation]
created: 2026-07-18
updated: 2026-07-18
status: draft
version: "0.1.0"
authors: ["Claude Code — Vault Architect"]
artifact_type: architecture-blueprint
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Strategy"
reasoning_engine: "LUMIAION"
dependencies: ["[[Alpha Proxima — 10 Year Vision]]", "[[Book I - The Constitution]]"]
related_documents: ["[[PHASE III INSTITUTIONAL READINESS MAP]]", "[[ALPHA PROXIMA META-LAYER DECISION MEMO]]"]
related_research_programs: []
---

# 02_STRATEGY Architecture Blueprint

> **Structure, not content.** This defines the *scaffold* the future strategy will occupy. It writes no strategy. It does not create the files yet — building the skeleton is YELLOW-gated on the meta-layer decision (to avoid a duplicate command layer).

## Grounding Evidence

- `01_VISION/Alpha Proxima — 10 Year Vision.md` — **exists** (the only populated vision doc).
- `02_STRATEGY/` — **empty** except `.gitkeep`. This is the missing middle layer.
- `06_PROJECTS/` — **empty** except `.gitkeep`. No active project workspaces.
- `OSG_LAUNCH/08_ROADMAP/30 Day Implementation Roadmap.md` — an execution-tier roadmap already exists, **disconnected** from any strategy layer.
- `11_OPERATIONS/` — mature cadence (Weekly/Monthly/Quarterly/Annual, Review Cycles, Dashboards) — the execution end already works.

**Diagnosis:** Alpha Proxima has a **vision** (top) and an **operational cadence** (bottom) but **no bridge** connecting them. Projects can't prove strategic alignment because there is no strategy to align to.

---

## The Eleven-Level Cascade (anti-duplication design)

Each level answers one question at one time-horizon and **references** — never restates — the level above. The core rule: **a level stores only the delta it introduces.**

| Level | Horizon | Question it answers | Home | Owner | Review cadence | Status semantics |
|-------|---------|---------------------|------|-------|----------------|------------------|
| L1 Direction | 15 yr | *Why do we exist / where ultimately* | `01_VISION/` (extend) | Founder | Annual | enduring / amended |
| L2 Position | 10 yr | *What we will have become* | `01_VISION/` (exists) | Founder | Annual | active / superseded |
| L3 Strategic State | 5 yr | *What state proves progress* | `02_STRATEGY/` | Founder + Exec | Annual | active / retired |
| L4 Capability Objectives | 3 yr | *What capabilities we must build* | `02_STRATEGY/` | Exec Council | Semi-annual | active / met / retired |
| L5 Institutional Outcomes | 1 yr | *What outcomes this year* | `02_STRATEGY/` | Exec Council | Quarterly | active / met / missed |
| L6 Priorities | 6 mo | *What we focus on now* | `02_STRATEGY/` | Exec Council | Quarterly | active / done |
| L7 Quarterly Portfolios | 3 mo | *Which projects this quarter* | `11_OPERATIONS/Quarterly Reviews` (exists) | Exec Council | Quarterly | planned/active/closed |
| L8 Active Projects | weeks–mo | *What is being built* | `06_PROJECTS/` | Project owner | Weekly | active/blocked/done |
| L9 Milestones | per project | *Proof points* | inside each project | Project owner | Weekly | pending/hit/slipped |
| L10 Weekly Execution | 1 wk | *This week's moves* | `11_OPERATIONS/Weekly Operations` (exists) | Delegates | Weekly | rolling |
| L11 Daily Focus | 1 day | *Today* | `11_OPERATIONS/Daily Operations` (exists) | Delegates | Daily | rolling |

**Non-duplication mechanism:** L3–L6 live as **distinct notes in `02_STRATEGY/`**, each linking *up* (parent objective) and *down* (child items). No level copies its parent's text; it links to it. L7/L10/L11 already exist in `11_OPERATIONS` — the blueprint **connects to them, does not recreate them.**

---

## Required Documents (to be created later, YELLOW-gated)

| Document | Level | Purpose |
|----------|-------|---------|
| `02_STRATEGY/Strategy Bridge Index.md` | all | Single entry point; renders the cascade |
| `02_STRATEGY/L3 - Five-Year Strategic State.md` | L3 | Named target states |
| `02_STRATEGY/L4 - Three-Year Capability Objectives.md` | L4 | Capability roadmap |
| `02_STRATEGY/L5 - Annual Institutional Outcomes.md` | L5 | Yearly outcomes |
| `02_STRATEGY/L6 - Six-Month Priorities.md` | L6 | Current priorities |
| `06_PROJECTS/_Project Template.md` | L8/L9 | Every project proves alignment (see below) |

## Required Databases / Indexes

- **Strategy Cascade Index** (Dataview) — one query rendering L1→L11 with status roll-up.
- **Alignment Ledger** — each `06_PROJECTS` note carries `parent_objective:` (a link to its L4/L5 parent). A Dataview query lists any project with a missing/broken `parent_objective` → **strategic-drift detector**.
- **Retirement Log** — objectives marked `retired` with date + reason; nothing is deleted, only retired.

## Ownership & Review Cadence
- **Founder:** L1–L3 (direction/position/strategic state).
- **Executive Council:** L4–L7 (the operational strategy band).
- **Delegates/Project owners:** L8–L11.
- Cadence already has homes in `11_OPERATIONS/Review Cycles` — the blueprint plugs strategy reviews into the existing cadence rather than inventing a parallel one.

## Status Semantics (uniform)
`active` · `met` · `missed` · `retired` · `superseded`. **No objective is deleted** — it is `retired` (with reason) or `superseded` (with successor link). This preserves institutional memory (Book III principle).

## Dependency Model
- Downward: each level's items must name a parent one level up (`parent_objective`).
- A project with no parent objective = **drift signal** (surfaced by Alignment Ledger).
- An objective with no children after one review cycle = **stalled** (surfaced by index).

## How Strategic Drift Is Detected
1. **Orphan projects:** `06_PROJECTS` note lacking a valid `parent_objective` link.
2. **Stalled objectives:** L4/L5 note with zero active children.
3. **Expired outcomes:** L5 past its year still `active`.
LUMIAION runs these three Dataview checks on the quarterly cadence and reports exceptions.

## How LUMIAION Reads & Uses the Structure
- LUMIAION treats the Strategy Bridge Index as the **canonical alignment map**: when routing a new idea/project, it attaches the nearest L4/L5 parent, or flags "no strategic home."
- LUMIAION's drift report feeds the Executive Council quarterly review.

## How Projects Prove Strategic Alignment
Every `06_PROJECTS` note's frontmatter carries `parent_objective:` + a one-line "alignment claim." A project **cannot enter `active`** without a valid parent link (enforced by review, later by validator). This is the concrete bridge the vault currently lacks.

## How Obsolete Objectives Are Retired
`retired` status + `retired_reason` + `retired_date`; children reassigned or also retired; entry added to Retirement Log. Never deleted.

## ⚠️ Dependency on Meta-Layer Decision
The `ALPHA PROXIMA/` meta-layer contains placeholder command/index notes. **If** the Founder makes that the command layer, the Strategy Bridge Index must live *there* or explicitly delegate to `02_STRATEGY/`. **Do not build the skeleton until the Meta-Layer Decision Memo is resolved** — otherwise two competing command surfaces appear.

## Fact / Inference / Recommendation / Open Question
- **Fact:** `02_STRATEGY` and `06_PROJECTS` are empty; vision and cadence exist and are disconnected.
- **Inference:** OSG 30-day roadmap is an orphan L7/L8 artifact with no strategic parent.
- **Recommendation:** Build the 11-level cascade as links-not-copies; enforce `parent_objective` on projects.
- **Open question:** Does strategy index live in `02_STRATEGY/` or the `ALPHA PROXIMA/` command layer? (gated on Meta-Layer Memo).

## Version History
| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-18 | Claude Code — Vault Architect | 11-level cascade scaffold; drift detectors; anti-duplication link model. Structure only. |
