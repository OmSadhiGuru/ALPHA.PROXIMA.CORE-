---
title: "Galaxy Council Prototype — Concept Note"
aliases: []
tags: [systems, council, prototype, alpha-proxima]
updated: 2026-09-17
version: "0.1.0"
dependencies: ["[[Agent and Subagent Registry]]"]
related_documents: ["[[Tool 014 - Council Session Kernel]]"]
related_research_programs: []
status: draft
created: 2026-09-12
authors: ["CLAUDE"]
artifact_type: design-prototype-note
institutional_owner: "Alpha Proxima Foundation"
---

# Galaxy Council Prototype — Concept Note

An isolated visual prototype exploring a radial "galactic council" composition
for the sixteen registry roles, requested as an alternative to the dark
office-desk aesthetic of `office_spatial.py`. **This does not replace that
interface.** It lives at its own path, its own port, reads the same data,
writes nothing, and executes nothing.

- Code: `08_SYSTEMS/Engineering Toolkit/council_galaxy_prototype.py`
- Template: `13_OPERATIONS/AI Council/spatial/galaxy-prototype.template.html`
- Run: `python3 "08_SYSTEMS/Engineering Toolkit/council_galaxy_prototype.py" serve --port 8790`

## Composition

```
LUMIAION (center, white-gold)
  ↳ inner circle, r=3.4     — coordination seats
  ↳ council ring, r=6.8     — one seat per department (its lead)
      ↳ constellation, r=10, 12.8, …  — the rest of that department, behind its lead
  ↳ unassigned cluster, r=21 — roles with no department yet, held apart
```

Distances are composition, not object sizes — chosen so each tier has visible
breathing room at the default camera framing, adjusted twice after visual
review (the first pass crowded every label around the center; see Known
issues fixed, below).

## The transformation layer — real data, an explicit visual read

The registry has no "lead" flag and no "coordination seat" concept; both are
assigned by `classify_roles()` in `council_galaxy_prototype.py`, not asserted
as registry fact:

| Council seat (department) | Lead (this prototype's call) | Constellation |
|---|---|---|
| Research Intelligence Office | Research Lead (AGT-002) | Comparative Lead, Education Lead |
| Engineering Office | CODEX Engineering Lead (AGT-007) | Computational Specialist |
| Executive Office | Executive Briefing Lead (AGT-006, available) | Strategic Intelligence Lead (AGT-011, **blocked**) |
| Institutional Observatory | Observatory Lead | *(none — single-role office)* |
| Ethics Council when convened | Ethics Sentinel (**advisory-only**, styled distinctly) | *(none)* |
| ATHENA / VORTEX / SOHMA | their Domain Lead | *(none — single-role offices)* |

Two roles are not on the council ring at all: **JERANIUM Data & Systems Lead**
and **YUNA Synthesis & Learning Lead** are both `operating_owner: "Owner
pending"` in the registry — no real department exists for them, so they sit
in a visually separate, dashed "unassigned" cluster rather than being forced
into a fabricated department.

The inner circle has one real occupant — **Memory Steward** (AGT-009, the
only other role whose owner is LUMIAION) — and four **proposed, unfilled**
seats matching functions the brief asked for (clarify intent, distribute
work, check data quality, prepare syntheses). Nothing was invented to fill
them; they render dashed and unlabeled-by-default, exactly as unappointed.

All sixteen roles are accounted for exactly once: 1 center + 1 inner + 8
leads + 4 constellation + 2 unassigned = 16.

## Role-by-role clarification for the PR #45 integration

PR #45 did not appoint agents or create constitutional offices. It integrated
the parser and read-only Council/Office/Galaxy views for the roles already
approved in the [[Agent and Subagent Registry]]. The registry remains the
authority for names, owners, implementations, states, and permitted subagents.
The Galaxy grouping and lead selection remain presentation choices.

| ID | Role | Accountable contribution | Authority and hard limit |
|---|---|---|---|
| AGT-001 | LUMIAION Orchestrator | Loads context, checks constitutional routing, coordinates specialists, and prepares synthesis. | Coordinates within delegated scope; does not replace specialist judgment, vote, ratify, or make the Founder decision. |
| AGT-002 | Research Lead | Builds sourced research sets and supervises evidence classification and citation checks. | May research and recommend; does not canonise findings or decide institutional acceptance. |
| AGT-003 | Comparative Lead | Maps competing frameworks, contradictions, and material disagreement. | Preserves alternatives; does not select doctrine or erase dissent. |
| AGT-004 | Education Lead | Turns approved knowledge into glossaries, explanations, and learning structures. | Adapts presentation; does not change the underlying institutional claim. |
| AGT-005 | Computational Specialist | Produces calculations, models, and independent quantitative verification. | Verifies computation; does not approve policy or expand an assignment. |
| AGT-006 | Executive Briefing Lead | Produces executive briefs and bounded scenario analysis for Founder review. | Briefs and advises; does not issue executive decisions. This Council ID must not be joined to a Founder-state ID by string alone. |
| AGT-007 | CODEX Engineering Lead | Designs, implements, tests, and security-reviews bounded engineering work. | Writes within the approved technical scope; does not approve its own work, change governance, or infer authority from passing tests. |
| AGT-008 | Observatory Lead | Monitors signals, detects drift, and reports institutional or system health. | Observes and reports; does not mutate canonical state or direct departments. |
| AGT-009 | Memory Steward | Prepares context, links archives, and performs bounded knowledge writeback. | Stewardship follows provenance and review rules; it does not declare imported material canonical. |
| AGT-010 | Ethics Sentinel | Classifies ethics triggers, maps risk, and records dissent when the Ethics Council is relevant. | Advisory-only; cannot vote, decide, or speak for an unconvened Ethics Council. |
| AGT-011 | Strategic Intelligence Lead | Intended to provide strategic intelligence under the Executive Office. | Blocked and unappointed; no work may be attributed to this role until an appointment is recorded. |
| AGT-012 | ATHENA Domain Lead | Provides health evidence, training analysis, and safety checks. | Domain advice only; the Founder retains decisions and external professional authority is not implied. |
| AGT-013 | VORTEX Domain Lead | Provides market research, financial modelling, and risk analysis. | Intelligence and advice only; no trading, capital movement, or regulated authority is implied. |
| AGT-014 | SOHMA Domain Lead | Maps phenomenology, symbols, meaning, and relevant epistemic boundaries. | Interprets within its charter; does not convert symbolic interpretation into institutional fact. |
| AGT-015 | JERANIUM Data & Systems Lead | Intended to support graph work, data validation, and systems analysis. | Blocked, unappointed, and owner-pending; the Galaxy must keep it unassigned and must not equate it with a Founder-state identity. |
| AGT-016 | YUNA Synthesis & Learning Lead | Intended to support synthesis planning, translation, and learning adaptation. | Blocked, unappointed, and owner-pending; no department or execution may be fabricated for it. |

Every listed role is non-voting. A subagent is a temporary bounded worker, not
another permanent agent identity. It inherits the accountable role's scope,
returns a defined deliverable, and expires when the task closes. Proposed inner
coordination seats remain functions without occupants until separately approved.

## What's real vs. demonstration

- **Real**: every role's name, department, current implementation, state
  (available/blocked/advisory-only), `may_instantiate` list, and — when one
  exists — its live Council assignment/status (including `executing`, if a
  `council run` is in flight while the page is open).
- **Demonstration, clearly labeled**: clicking LUMIAION opens an "intention"
  textarea; submitting it shows a static, hardcoded mock proposal card
  under a visible "DEMONSTRATION — no real routing or execution happens
  here" banner. No prompt is sent anywhere. No session is opened.
- **Not connected**: there is no way to trigger a `council run` from this
  page. The agent detail panel shows the exact CLI command to copy instead.

## Known issues found and fixed during review

1. A CSS specificity bug (`.label.dim{opacity:.55}` beating `.label{opacity:0}`
   regardless of a `.shown` toggle class) made constellation-member labels
   visible in the overview when they should have been hidden. Fixed by
   switching the show/hide mechanism to `display` (which the `.dim` opacity
   rule can't override) instead of `opacity`.
2. The first render showed every inner-circle seat's function label at all
   times, crowding the core into unreadable overlap — the brief's own spec
   says the overview should show only LUMIAION and department names. Fixed
   by making inner-circle (and unassigned) labels reveal on hover/pointer
   proximity instead of always-on.
3. The naive "first role in registry order per owner" lead-selection rule
   picked the wrong lead for Engineering Office (Computational Specialist
   instead of CODEX Engineering Lead). Fixed with an explicit
   `LEAD_OVERRIDES` map, documented in the module itself as a judgment call.

## Historical prototype-session verification (not replayed by PR #46)

Department fly-to navigation, breadcrumb, Escape/back-to-council, hover
label reveal, search by name and by skill, agent detail panel with real
registry + live-assignment data, the LUMIAION demonstration dialogue, the
16-item accessible keyboard list, WebGL-fallback code path (not exercised —
this machine has WebGL), no console errors, no write calls anywhere in the
new module, no production state file touched.

## Proposed for later (not built this session)

- A persistent top-down camera toggle (used ad hoc via console for review
  screenshots, not exposed as a UI control yet).
- Touch/tap equivalent for the hover-reveal labels (today's reveal is
  pointer-proximity based; a phone would need tap-to-reveal instead).
- Performance: `council_galaxy_prototype.py` recomputes the full vault index
  and Truth Kernel graph on every request (~3s/load on this machine, same
  cost `office_spatial.py` already has) — fine for a single reviewer, not
  for anything higher-traffic.
- The actual CLI-to-page execution bridge described in the original brief's
  §10 (queueing, submission IDs, permission checks) — intentionally not
  built; this session only verified that no such path exists yet.
