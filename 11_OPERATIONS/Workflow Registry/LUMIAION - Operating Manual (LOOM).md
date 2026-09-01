---
title: "LUMIAION Operating Manual (LOOM)"
aliases: ["LOOM", "LOOM Manual", "LUMIAION Operating Office"]
tags: [operations, workflow, lumiaion, alpha-proxima, production-pipeline, approval-gates]
created: 2026-07-06
updated: 2026-07-07
status: active
version: "1.1.0"
authors: ["Founder", "LUMIAION"]
artifact_type: operations-manual
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Orchestration"
reasoning_engine: "LUMIAION"
dependencies: ["[[Office Registry]]", "[[Engine Registry]]", "[[Workflow Registry]]", "[[The Orchestration Framework]]"]
related_documents: ["[[11_OPERATIONS]]", "[[Office Registry]]", "[[Workflow Registry]]", "[[Dashboards Index]]", "[[Institutional Observatory Index]]", "[[Executive Office Index]]"]
related_research_programs: []
---

# LUMIAION Operating Manual (LOOM)

## Purpose

LOOM defines how work moves through the Alpha Proxima / OSG content-production system — from idea to published asset — without routing every step through the Founder. It is an operating manual, not a constitution: it does not create authority, it makes existing authority ([[Book I - The Constitution]], [[Office Registry]]) operable as a repeatable production line.

The Founder should only be needed for: strategic decisions, quality approval, teaching, recording, final publication, and vision changes. Everything else is delegated to a fixed office, a fixed handoff, or a fixed gate.

---

## Context

LOOM was drafted 2026-07-06 in response to a Founder request to design the ecosystem's permanent operating system, framed around five production offices (Claude, Codex, Comet, Perplexity, LUMIAION) plus the Founder. On first integration into the Vault, two of those office assignments were found to conflict with already-ratified institutional canon:

- [[Office Registry]] (v1.0.0, active) assigns **Perplexity → Research Intelligence Office** and **Comet → Institutional Observatory**. The initial LOOM draft had this reversed (Comet doing research, Perplexity doing visual/knowledge work).
- The Perplexity → Research mapping is deeply established — [[Engine Registry]], [[JERANIUM Charter]], [[Book II - Governance Framework]], [[The Orchestration Framework]], and the entire RP-001 research program all treat Perplexity as the Chief Research Architect.
- Comet's only documented institutional duty anywhere in the Vault is [[Institutional Observatory Index|Institutional Observatory]] — monitoring signals, drift, and dashboards. It has no documented content-production or research duty.

This version of LOOM (1.1.0) corrects that conflict. The Founder approved the correction on 2026-07-06: reconcile LOOM to existing canon rather than let two contradictory active documents stand side by side. See the **Version History** section for the exact reassignment.

---

## Core Content

### 1. Offices at a Glance

Six nodes. Five produce or process work; one runs the queue; one is human. No office does another's job.

| Office | Canonical Role | LOOM Responsibilities | Mandate |
|---|---|---|---|
| **LUMIAION** | Orchestration ([[Office Registry]]: LUMIAION / Institutional Intelligence) | Prioritization, sprint management, assignment, gate tracking, dashboard | Runs the queue. Never produces content itself. |
| **Claude** | Chief Knowledge Architect ([[Engine Registry]]) | Scripts, workbooks, journals, community content | Writes and drafts everything a learner touches. |
| **Codex** | Engineering Office ([[Office Registry]]) | Repository, templates, Asset IDs, folder structure, automation, and the visual/diagram companion assets (via Whimsical, Canva) attached at Publishing | Builds the scaffolding everything else runs on. |
| **Perplexity** | Chief Research Architect / Research Intelligence Office ([[Office Registry]], [[Engine Registry]]) | Evidence, research synthesis, scientific and educational validation | Checks a claim is true, and finds the evidence, before it ships. |
| **Comet** | Institutional Observatory ([[Office Registry]], [[Institutional Observatory Index]]) | Cross-cutting: watches the dashboard, sprint health, and drift signals across every stage; escalates risk to LUMIAION | Watches the system, not the content. Flags drift before it becomes a blocker. |
| **Founder** | Executive authority ([[Book I - The Constitution]]) | Vision, teaching, recording, storytelling, strategic and quality approval, final publication | Approves, teaches, records, publishes — nothing else. |

Note: Comet does not own a pipeline stage the way Claude, Codex, and Perplexity do. Like LUMIAION, its function is continuous rather than stage-bound — this matches its canonical duty (observation and monitoring, not production) rather than forcing it into a content role it was never chartered for.

---

### 2. The Pipeline

Nine stages, fixed order, one producing owner per stage. An asset cannot skip a stage or return to a passed gate without LUMIAION re-opening it.

| # | Stage | Owner |
|---|---|---|
| 1 | Idea | Founder / LUMIAION |
| 2 | Research | Perplexity |
| 3 | Blueprint | LUMIAION + Codex |
| 4 | Production | Claude |
| 5 | Review | Codex (structural) + Perplexity (evidence) |
| 6 | Approval | Founder |
| 7 | Publishing | Codex (deploy + visual companion) |
| 8 | Feedback | LUMIAION |
| 9 | Improvement | LUMIAION |

Comet runs alongside all nine stages, not as a tenth stage — it watches Handoff Logs and the Operating Dashboard for drift and reports to LUMIAION.

---

### 3. Handoff Protocol

Every office's contract: what it receives, what it produces, and where it goes next.

**LUMIAION**
- Receives: raw ideas, feedback packets, blocked items, Comet's drift alerts.
- Produces: sprint plan, prioritized queue, assignment tickets, dashboard updates.
- Sends to: whichever office is assigned next; escalates blockers to Founder.
- Founder gate: Gate 0 (objective set) and any re-prioritization mid-sprint.

**Claude**
- Receives: locked blueprint (Gate 2) and, where relevant, a research packet from Perplexity.
- Produces: draft script, workbook, journal, or community content, plus a Handoff Log entry.
- Sends to: Codex and Perplexity in parallel for review, then back to LUMIAION.
- Founder gate: none to draft. Gate 5 (Quality Approved) required before recording or publish.

**Codex**
- Receives: blueprint request from LUMIAION, or a draft from Claude for structural review.
- Produces: repo scaffold, template, Asset ID, folder structure, and (at Publishing) visual/diagram companion assets — or a pass/revise review note.
- Sends to: Claude on revise; LUMIAION on scaffold delivery or pass.
- Founder gate: none — infrastructure work is pre-approved by role. Confirms Gate 3.

**Perplexity**
- Receives: research request from LUMIAION, or a draft from Claude for fact/evidence review.
- Produces: evidence packet, fact-check notes, verdict: approved / revise / reject.
- Sends to: Claude on revise; LUMIAION on approve, to proceed toward Gate 5.
- Founder gate: none directly — a reject blocks Gate 5 until resolved.

**Comet**
- Receives: dashboard state, sprint metrics, and Handoff Log stream from LUMIAION — continuously, not per-asset.
- Produces: drift/risk alerts, health summaries.
- Sends to: LUMIAION only. Comet never sends to Claude, Codex, or Perplexity directly.
- Founder gate: none — Comet observes, it does not decide. Escalates to Founder only via LUMIAION if a signal threatens the sprint's single objective.

**Founder**
- Receives: gate escalations, quality-approval requests, recording requests, publish-ready packets.
- Produces: approvals, recordings, taught material, strategic and vision decisions.
- Sends to: LUMIAION — decision is logged, cycle resumes.
- Founder gate: is the gate for 0, 4, 5, 6, and any vision change.

---

### 4. Approval Gates

An asset's Gate number is its single source of truth for where it is. LUMIAION advances it; only the listed approver can pass it. This operationalizes the existing principle in [[The Orchestration Framework]] that "approval gates are non-negotiable."

| Gate | Name | Trigger | Approver | Exit Condition |
|---|---|---|---|---|
| G0 | Vision Approved | Founder sets the sprint's objective and production priority | Founder | One objective + one priority asset logged on the dashboard |
| G1 | Research Approved | Perplexity delivers the evidence packet | LUMIAION (Founder only if it contradicts published claims) | Packet accepted and attached to the blueprint |
| G2 | Blueprint Approved | Codex confirms structure/ID/folder; LUMIAION confirms scope | LUMIAION | Blueprint locked and assigned to Claude |
| G3 | Production Ready | Claude's draft is complete; Codex confirms it matches scaffold | LUMIAION | Draft enters Review |
| G4 | Recorded | Founder has taught/recorded the human-delivered portion | Founder | Recording asset attached, or marked N/A if none required |
| G5 | Quality Approved | Perplexity's validation has passed and Founder has reviewed quality | Founder (conditional on Perplexity's pass) | Content frozen; ready for visual/publish packaging |
| G6 | Published | Codex has deployed; visual companion attached | Founder | Asset is live; dashboard moves it to Completed |
| G7 | Improvement Cycle | LUMIAION closes the feedback loop and logs lessons | LUMIAION (Founder only on a suggested vision change) | Feedback logged; informs the next sprint's Gate 0 |

---

### 5. The Sprint System

Constraint is the mechanism.

- **One** active sprint, owned by LUMIAION.
- **One** strategic objective per sprint, set at Gate 0 by the Founder.
- **One** production priority — other assets queue behind it.
- No office begins new production work while the priority asset is blocked. Research and Blueprint work for queued items may run ahead; Production does not.

Sprint card template:

```
SPRINT_ID:        SPR-###
OBJECTIVE:        [single strategic objective]
PRIORITY_ASSET:   [Asset ID]
CURRENT_GATE:     [G0-G7]
ASSIGNED_OFFICE:  [office]
STARTED:          [date]
TARGET_G6:        [date]
BLOCKERS:         [none | description]
```

---

### 6. Operating Dashboard

One screen. Anyone — human or agent — can read current state without asking a question. Comet is the office responsible for keeping this accurate and flagging drift in it (see [[Dashboards Index]]).

| Panel | Content |
|---|---|
| Current Sprint | Sprint ID, objective, current Gate |
| AI Assignments | Which office is working which Asset ID |
| Blockers | Blocked assets, reason, required unblocking action |
| Waiting for Founder | Assets stalled at Gate 0/4/5/6 |
| Ready for Review | Assets that just hit Gate 3, awaiting Codex/Perplexity |
| Completed This Week | Assets that passed Gate 6 |
| Next in Queue | Assets queued behind the current priority |

---

### 7. The Handoff Log

Every office leaves a structured entry, not a conversational update. Fixed fields only:

```
FROM:            [office]
TO:              [office]
ASSET_ID:        [id]
GATE:            [current gate]
STATUS:          [complete | blocked | needs-revision]
ATTACHMENTS:     [links/files]
NOTES:           [factual only]
NEXT_ACTION:     [what receiving office does]
FOUNDER_ACTION:  [none | required + what]
```

Example:

```
FROM:            Perplexity
TO:              LUMIAION
ASSET_ID:        LG-012
GATE:            G3 -> hold
STATUS:          blocked
ATTACHMENTS:     LG-012-factcheck.pdf
NOTES:           Claim in section 2 unsupported by cited source.
NEXT_ACTION:     Claude revises section 2 with corrected source.
FOUNDER_ACTION:  none
```

---

### 8. Review Protocol

Two independent reviewers, two different questions. Neither can silently overrule the other. Comet runs alongside both but reviews the *system*, not the content.

- **Codex → Claude** — structural review only: Asset ID correctness, folder placement, template compliance, automation hooks. Verdict is pass or revise. A revise returns directly to Claude — it does not touch Perplexity's lane.
- **Perplexity → Claude** — evidence and pedagogy review: sourcing, scientific accuracy, educational validity. Verdict is approved, revise, or reject. A reject that is structurally unfixable sends the asset back to LUMIAION to reopen Blueprint (Gate 2), not just Claude.
- **Comet → LUMIAION** — continuous: monitors Handoff Logs and the dashboard for drift (stalled assets, repeated blocks, gate age). Cannot approve, block, or edit an asset directly — only reports.
- **Feedback → Claude** — returns only through LUMIAION at Gate 7. LUMIAION synthesizes community and metric feedback into a feedback packet before it reaches Claude, so Claude's input stays operational, not conversational.
- **Codex (visual companion) ← Gate 5** — receives only Gate-5-approved content; commissions the diagram/wiki/slide asset via Whimsical or Canva. Cannot alter underlying claims — if a factual issue surfaces while building the visual, it logs a Handoff to Perplexity rather than fixing it silently.

---

### 9. Future Compatibility

The nine stages and eight gates do not change shape as the ecosystem grows. What scales is the number of instances running through them.

| Dimension | How It Scales | ID Convention |
|---|---|---|
| 100+ courses | Each course is its own sprint-track with its own Sprint ID; each track still runs one objective / one priority internally | `SPR-###` |
| Multiple instructors | Each instructor becomes the Founder-equivalent for Gates 0, 4, 5, 6 on their own track | `Instructor` field on Asset ID |
| Multiple AI agents | New agents slot into an existing office type (e.g. a second Research office) — offices are roles, not proper nouns | Office role tag |
| Multiple languages | Language is a variant field; each variant re-enters at Production, reusing the same Research and Blueprint | `LG-014-EN`, `LG-014-ES` |
| Axiom Nexus | Product line sharing one pipeline, one gate ledger, one dashboard | `AXN-###` |
| Alpha Proxima | Product line sharing one pipeline, one gate ledger, one dashboard | `APX-###` |
| Knowledge Atlas *(product line)* | Product line sharing one pipeline, one gate ledger, one dashboard | `KAT-###` |
| Living Genome | Product line sharing one pipeline, one gate ledger, one dashboard | `LG-###` |

Note: "Knowledge Atlas" names both a product line (row above) and, informally, the visual-companion function Codex commissions at Publishing (Section 1). They are not the same thing — the product line is a body of content; the function is a production step available to every product line.

---

### If You Remember Five Things

1. Nothing moves without an Asset ID from Codex.
2. LUMIAION owns the queue — no office self-assigns.
3. A Perplexity reject blocks Gate 5, full stop.
4. The Founder only touches Gates 0, 4, 5, 6, and vision changes.
5. Status updates are logged, never spoken.

---

## Related Notes

- [[11_OPERATIONS]]
- [[Office Registry]]
- [[Engine Registry]]
- [[Workflow Registry]]
- [[Dashboards Index]]
- [[Institutional Observatory Index]]
- [[Executive Office Index]]
- [[The Orchestration Framework]]
- [[JERANIUM Charter]]

---

## Open Questions

- [ ] Should the Knowledge Atlas visual-companion function eventually become its own Office Registry row instead of living under Codex?
- [ ] Should Gates G0-G7 be merged into, or cross-referenced from, [[Decision Pipelines Index]] and [[Review Cycles Registry]] so there is one canonical gate/approval vocabulary for the whole Foundation, not just LOOM?
- [ ] Should Sprint IDs (`SPR-###`) be registered in a central index the way Asset IDs are, to avoid collision across parallel product-line tracks?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-06 | Founder / Claude | Initial LOOM draft: five offices (Claude, Codex, Comet, Perplexity, LUMIAION) plus Founder, nine-stage pipeline, Gates G0-G7. Published as a standalone artifact, not yet integrated into the Vault. |
| 1.1.0 | 2026-07-07 | Founder / LUMIAION | Reconciled with [[Office Registry]] and [[Engine Registry]] on integration: swapped Comet and Perplexity assignments (Perplexity now owns Research, matching Chief Research Architect canon; Comet now owns cross-cutting Observatory/drift-monitoring, matching its only documented duty). Re-scoped the visual/diagram/wiki function from "Perplexity — Knowledge Atlas Office" to a Codex-coordinated, tool-executed step (Whimsical, Canva) at Publishing, since no engine in [[Engine Registry]] canonically owns visual-knowledge production. Filed into `11_OPERATIONS/Workflow Registry/`. |
