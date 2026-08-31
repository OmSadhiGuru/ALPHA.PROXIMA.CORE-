---
title: "Founder Console"
aliases: ["Founder Console", "Founder OS Console", "Console V1"]
tags: [operations, founder-os, console, dashboard, lumiaion, alpha-proxima]
created: 2026-08-26
updated: 2026-08-31
status: active
version: "1.0.0"
authors: ["LUMIAION", "CODEX"]
artifact_type: operations-dashboard
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Orchestration"
reasoning_engine: "LUMIAION"
dependencies: ["[[Founder OS Architecture v1]]", "[[LUMIAION - Operating Manual (LOOM)]]"]
related_documents: ["[[Founder Reboot Control Center]]", "[[Dashboards Index]]", "[[Workflow Registry]]"]
related_research_programs: []
---

# Founder Console

> [!warning] Generated file
> This note is rendered from `state/founder-state.json` by `ap.py founder render`. Edits here are overwritten. Change state with `ap.py founder <command>`.

_Rendered 2026-08-31T04:40:45+00:00 · schema 1.0.0_

## Today

**2026-08-26** — Establish one Founder cockpit: state, console, and a proven vertical slice ⚠️ **stale — set today's mission**

_Set by lumiaion · sprint RBT-001_

### Top 3 Priorities

| # | Priority | Why | Owner |
|---|---|---|---|
| 1 | Resolve the four open draft PRs (#7, #8, #9, #10) | CN-001 cannot proceed while canonical work is split across unmergeable branches. | Founder |
| 2 | Prove one end-to-end routing lane through LUMIAION | No new agent is authorized until one routing proof completes (Reboot Audit). | LUMIAION |

### Next Action

**Decide the disposition of PR #10 (CN-001) — resume, rebase, or close** — Founder

## Decisions Requiring Founder

| ID | Decision | Recommendation | Consequence of delay |
|---|---|---|---|
| FD-002 | Keep the Founder Console local-only | Keep local-only for V1. Treat hosting as a separate decision that must ship with authentication. | Low. Local-only is the safe default and blocks nothing today. |
| FD-003 | Authorize OMI credentials for the capture pipeline | Defer until the routing proof passes. Build the OMI adapter against the ContextItem contract only after one lane is proven. | Low for now. Voice-captured decisions keep landing outside Founder OS until it is built. |
| FD-004 | Accept repository-coherence-first recovery order | Accept | RBT-001 cannot close and no new agent can be authorized. |
| FD-005 | Treat ARTEMIS and POSTMANIUM as proposed until the routing proof passes | Accept | Agents risk becoming active purely because they were mentioned in conversation. |
| FD-006 | Treat Secretary-General as proposed until chartered | Accept | An unchartered role with unclear privacy boundaries stays informally active. |
| FD-007 | Salvage PR #7 and #8 selectively rather than merge wholesale | Accept | PR #7 (19 ahead / 84 behind) drifts further from main every week. |

## Execution

| ID | Task | State | Owner | Why |
|---|---|---|---|---|
| TSK-004 | Build the CN-001 relocation map from current main | BLOCKED | CODEX | Reboot Audit step 3: coherence must precede any expansion. |
| TSK-005 | Salvage PR #7 and #8 document by document | WAITING | LUMIAION | Reboot Audit forbids merging either wholesale; each document needs a class. |
| TSK-006 | Run the photo-to-social-post routing proof end to end | ASSIGNED | LUMIAION | First operational proof that Founder -> LUMIAION -> specialist -> Founder works. |

## Agents / Systems

| Agent | Role | Status | Authority |
|---|---|---|---|
| LUMIAION | Orchestration / Institutional Intelligence | ACTIVE | Class III/IV within delegated scope; AI seat, no vote |
| CLAUDE | Institutional Architecture / Chief Knowledge Architect | WORKING | Architecture recommendation and specification; no governance authority |
| CODEX | Engineering Office | WORKING | Implementation only; no governance authority |
| PERPLEXITY | Research Intelligence Office | IDLE | Research production and evidence gathering; not canonization |
| COMET | Institutional Observatory | IDLE | Observation and reporting; not decision authority |
| JERANIUM | Knowledge routing / manual semantic layer | IDLE | Retrieval and packaging; canonization requires LUMIAION |
| ATHENA | Health, performance, longevity department | IDLE | Domain analysis within charter |
| SOHMA | Consciousness, symbols, meaning department | IDLE | Domain analysis within charter |
| VORTEX | Finance, markets, business strategy department | IDLE | Domain analysis within charter |
| ARTEMIS | Proposed — not chartered | PROPOSED | None until ratified |
| POSTMANIUM | Proposed — not chartered | PROPOSED | None until ratified |
| SECRETARY-GENERAL | Proposed — charter, authority and privacy boundaries undefined | PROPOSED | None until chartered |

## Blockers

| ID | Blocker | Impact | Owner | Founder needed? |
|---|---|---|---|---|
| BLK-001 | Four draft PRs unresolved (#7, #8, #9, #10) | CN-001 coherence work cannot start; canonical content is split across branches. | Founder | Yes |
| BLK-002 | Semantic memory layer (Layer 3) does not exist | LUMIAION cannot search the full Vault in-session; context loading stays manual. | Founder | Yes |
| BLK-003 | No OMI adapter or credential in the repository | The OMI capture pipeline cannot be implemented or tested. | Founder | Yes |

## System Health

| Area | Status | Detail |
|---|---|---|
| Repository | OK | main at 4134c34; reboot control center merged via PR #11. |
| Vault validation | DEGRADED | 5 errors and 479 warnings outstanding across 297 notes (pre-existing baseline). |
| Open pull requests | DEGRADED | Four draft PRs open: #7, #8, #9, #10. None mergeable without salvage decisions. |
| Founder OS state | OK | State document validates; 39 engine tests pass. |
| Memory / context | DEGRADED | Layer 3 semantic memory unbuilt; context loading remains manual and selective. |
| Task queue | OK | Six work units tracked with owner, provenance, and state. |

## Integrations

| Integration | Status | Notes |
|---|---|---|
| Obsidian Vault | CONNECTED | The Vault is the Founder OS memory layer. Console state lives inside it. |
| GitHub | CONNECTED | State is git-versioned and pushed to OmSadhiGuru/ALPHA.PROXIMA.CORE-. History is the audit log. |
| OMI | NOT CONNECTED | No adapter or credential exists in this repository. An operating agent's own session tooling is not a Founder OS integration. |
| ChatGPT / Codex | NOT CONNECTED | Codex participates through commits and pull requests, not through a Founder OS API. |
| Google Calendar | NOT CONNECTED | No adapter or credential in this repository. |
| Semantic memory (vector index) | BLOCKED | Engine Registry lists the Chief Memory Architect role as unfilled. Blocks Layer 3 of the LUMIAION memory architecture. |
| Health / performance systems | PLANNED | ATHENA charter exists; no data source connected. |
| Financial systems | PLANNED | VORTEX charter exists; no data source connected. |
| Voice capture | PLANNED | No implementation. Depends on the same ContextItem contract as OMI. |
