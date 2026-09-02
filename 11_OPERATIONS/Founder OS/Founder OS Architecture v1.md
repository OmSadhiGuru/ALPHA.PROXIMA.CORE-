---
title: "Founder OS Architecture v1"
aliases: ["Founder OS", "Founder OS Architecture", "Founder Console V1 Architecture"]
tags: [operations, founder-os, architecture, console, lumiaion, orchestration, alpha-proxima]
created: 2026-08-26
updated: 2026-09-01
status: active
version: "1.2.0"
authors: ["CLAUDE", "CODEX", "LUMIAION"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Architecture"
reasoning_engine: "Claude"
dependencies: ["[[Repository Reboot Audit - 2026-08-23]]", "[[Founder Reboot Control Center]]", "[[LUMIAION Architecture Spec v0.1]]", "[[LUMIAION - Operating Manual (LOOM)]]"]
related_documents: ["[[Founder Console]]", "[[The Orchestration Framework]]", "[[Office Registry]]", "[[Engine Registry]]", "[[Alpha Proxima Engineering Toolkit]]", "[[Alpha Proxima App Architecture v1]]"]
related_research_programs: []
---

# Founder OS Architecture v1

## Purpose

This document specifies the first operational control plane of Alpha Proxima: the state contract, orchestration contract, and presentation boundary that let the Founder direct work from one surface instead of routing information between systems by hand.

It is deliberately narrow. It covers what was built and verified on 2026-08-26, what was found in the repository, and what remains a decision. It does not amend the Constitution, activate an office, or authorize a merge.

---

## Context

### 1. What the repository actually is

The single most consequential finding of this session, and the one that shaped every decision below:

**`ALPHA.PROXIMA.CORE-` is an Obsidian Markdown vault with a small Python toolkit. It is not an application.**

Verified by inspection on 2026-08-26 at `main` = `4134c34`:

| Evidence | Count / state |
|---|---|
| Markdown notes | 297 |
| Python modules | 13 (Engineering Toolkit + Knowledge Graph tools) |
| `package.json`, `requirements.txt`, lockfiles | **None** |
| Web application, framework, or bundler | **None** |
| HTTP API or server | **None** |
| Database or state store | **None** |
| Test suite (pre-session) | **None** |
| CI workflow | **None** |
| Third-party Python dependency | **None** — the toolkit is standard library only |

The vault carries substantial institutional canon: Books I–III of the Constitution, the LUMIAION charter and architecture spec, the LOOM operating manual, ATHENA / SOHMA / VORTEX / JERANIUM department charters, office and engine registries, six research programs, and an Engineering Toolkit with nine documented tools behind one `ap.py` CLI.

What it did not carry was any executable representation of Founder state. Every dashboard in `11_OPERATIONS/` is a hand-maintained Markdown table. Nothing reads them; nothing validates them; nothing can be queried by a second interface.

### 2. Component classification

Per the mission's instruction to integrate rather than reboot:

| Component | Class | Reasoning |
|---|---|---|
| `00_CONSTITUTION/`, `03_AI_COUNCIL/`, governance instruments | **KEEP** | Canonical. Founder OS consumes these; it never redefines them. |
| `08_SYSTEMS/Engineering Toolkit/` + `ap.py` | **EXTEND** | The existing implementation surface. Founder OS ships as a new subcommand, not a new tool family. |
| `11_OPERATIONS/Dashboards/Founder Reboot Control Center` | **KEEP** | Remains the RBT-001 sprint record. Founder OS carries its four pending decisions into the live queue rather than duplicating the document. |
| `11_OPERATIONS/Reboot/Repository Reboot Audit` | **KEEP** | Its findings are the seed data for the Console's blockers and health signals. |
| Hand-maintained Markdown dashboards | **REFACTOR** (deferred) | Superseded in function by generated views, but not touched this session. Migration belongs to CN-001. |
| `ALPHA PROXIMA/` legacy root, `Sans titre*.md`, `Vault.md` | **ARCHIVE** (deferred) | The Reboot Audit forbids relocation before CN-001 produces a migration map. Untouched. |
| ARTEMIS, POSTMANIUM, Secretary-General | **BLOCKED** | No canonical charter on `main`. Registered as `proposed`; carry no authority. |
| PRs #7, #8, #9, #10 | **BLOCKED** | Four open drafts. Founder decisions required before salvage. |
| Layer 3 semantic memory | **BLOCKED** | Chief Memory Architect role unfilled in the Engine Registry. |

Nothing was deleted, relocated, or renamed. The only pre-existing file modified is `ap.py`, which gained one registry line.

---

## Core Content

### 3. The architecture delta

```
BEFORE                                  AFTER
──────                                  ─────
Founder                                 Founder
   │  reads 6 hand-kept dashboards         │  reads 1 Console
   │  reconciles them mentally             │
   ▼                                       ▼
Markdown tables                         founder-state.json   ← one writer, validated
   │  no schema                            │  schema + provenance + git history
   │  no validation                        │
   │  no consumer                          ├──► Console V1 (HTML, generated)
   ▼                                       ├──► Obsidian mirror (Markdown, generated)
Nothing reads them                         ├──► /api/view  (loopback HTTP)
                                           └──► future spatial / voice / VR layer
```

The delta is not a new interface. It is the introduction of **a machine-readable Founder state with exactly one writer**, from which every interface is derived.

### 4. The central decision: state lives in the Vault

Founder OS needed persistence. The options were:

1. **Vault-native JSON** — one git-versioned document inside the repository.
2. **A hosted database** plus a web application.
3. **Continue with Markdown tables** and accept manual reconciliation.

Option 2 was rejected for V1, and the rejection is on the record as a Founder decision (`FD-001`) rather than an assumption. Its costs against this repository's reality are concrete: a new runtime, a dependency tree, hosting, credentials, an authentication system, and a second source of truth competing with the Vault the Founder already reads daily. None of that reduces the coordination the Founder personally performs — the test every Founder OS decision must pass.

Option 1 was chosen because it is the only option where the storage layer is *already* the Founder's working environment:

- The Vault is LUMIAION's declared memory between sessions ([[LUMIAION Architecture Spec v0.1]] §3). State belongs in memory.
- Git history is the audit log. Every mission, decision, and status change is a diff with an author and a timestamp — provenance for free.
- Obsidian Git already syncs the vault to the Founder's devices. State reaches Mac, PC, and phone with no new infrastructure.
- No credentials, no hosted service, no attack surface. Private by default, per mission §13.
- Zero dependencies. The toolkit's standard-library-only property is preserved exactly.

The honest cost: JSON is not concurrently writable, and two agents editing state simultaneously would produce a git conflict. That is acceptable while LUMIAION is the single orchestrator, and it is the trigger condition for revisiting `FD-001` — not a defect to paper over.

### 5. The state contract

One document, `state/founder-state.json`, written **only** by `ap.py founder`. Markdown and HTML views are generated and carry a "generated file" banner; they are never edited by hand, which removes the reconciliation problem rather than managing it.

Entities implemented, matching mission §7:

| Entity | Shape | Purpose |
|---|---|---|
| `founder` | object | Identity and role. |
| `daily_mission` | object \| null | Date, mission, `set_by`, `set_at`, `sprint_id`. Goes stale automatically when its date is not today. |
| `priorities` | list | **Capped at three open items by the schema.** Rank, why, owner, project, status. |
| `next_action` | object \| null | Exactly one. Optionally bound to a priority; cleared automatically when that priority closes. |
| `decisions` | list | Context, recommendation, options, consequence of delay, status. |
| `tasks` | list | States: `assigned`, `working`, `waiting`, `blocked`, `review`, `complete`. |
| `agents` | list | Role, office, engine, status, authority. |
| `agent_runs` | list | Execution records against an agent and task. |
| `blockers` | list | Impact, owner, `needs_founder`, and what they block. |
| `context_items` | list | Where a fact came from — the ingestion contract future inputs write into. |
| `results` | list | What a task produced, and where it lives. |
| `projects` | list | What work serves. |
| `integrations` | list | `connected` \| `not_connected` \| `planned` \| `blocked`. |
| `system_health` | list | `ok` \| `degraded` \| `unknown` \| `failing`, with the source of the signal. |

Two constraints are enforced in code rather than left to discipline, because both are load-bearing for the mission's cognitive-load requirement:

- **The Top 3 is a hard cap.** A fourth open priority is rejected. A twenty-item board cannot form.
- **Provenance is mandatory.** Every task must carry `owner`, `requested_by`, and `why`; every decision must carry its consequence of delay. A work item that cannot say why it exists cannot be saved.

Every record additionally answers: who owns it, what project it serves, what state it is in, what it produced, and whether the Founder is required.

### 6. The orchestration contract

The mission's target loop, mapped onto entities that now exist:

| Stage | Contract |
|---|---|
| FOUNDER | Intent enters as a `daily_mission`, `priority`, or `task`. |
| LUMIAION | Classifies and assigns `owner`; sets `state = assigned`. |
| CONTEXT COLLECTION | Sources write `context_items` with `source` and `ref`. |
| ROUTING | `owner` names the office; `gate` names the LOOM gate (G0–G7). |
| SPECIALIST / TOOL | Execution recorded as an `agent_run`; `state = working`. |
| RESULT | Output recorded as a `result` with a `ref`; `state = review`. |
| LUMIAION SYNTHESIS | Result summarized; blockers raised. |
| FOUNDER DECISION | Anything needing the Founder becomes a `decision` or a `needs_founder` blocker — it never hides inside a task. |
| MEMORY / STATE UPDATE | The state document is written and committed. Git history is institutional memory. |

This is a data contract, not a scheduler. Asynchronous workers are supported later by design: `agent_runs` already models start, end, status, and output, so a worker can append a run record without the contract changing.

The Console surfaces LOOM gates on work units rather than inventing a parallel workflow. LOOM remains the authority on how work moves.

### 7. Presentation boundary

The domain model contains no metaphor. Console V1 reads a derived read model (`build_view`) rather than raw state, so a later 2D, 3D, VR, voice, or accessibility interface consumes the same structure without the backend changing.

The chakra / energy-field mapping described in the mission brief (Crown → Vision, Third Eye → Intelligence, Throat → Routing, Heart → Relationships, Solar Plexus → Execution, Sacral → Creation, Root → Stability) is recorded here as a **presentation mapping only**. No entity, field, or endpoint references it. A future spatial layer may map `priorities`, `decisions`, and `agents` onto that model; nothing in Founder OS will know it did.

`GET /api/view` on loopback is the interface contract a Meta Quest client would consume. It exists today.

**The boundary has since been exercised.** [[Alpha Proxima App Architecture v1]] (2026-09-01) composes `build_view` with a vault index into a second, independent interface without changing one line of this state contract. That is the evidence the presentation boundary is real rather than asserted.

### 8. Console V1 — what it shows and what it refuses to show

The Console is a decision interface, not an analytics dashboard. It answers four questions in one screen:

1. **What matters today?** → Mission of the Day, Top 3, all above the fold.
2. **What is happening?** → Execution, with state pills.
3. **What needs me?** → Decisions and `needs_founder` blockers, in the accent colour reserved for Founder attention.
4. **What happens next?** → Next Action, given its own emphasized panel.

Everything else is progressively disclosed behind a `context` or `provenance` toggle: decision options, consequence of delay, task provenance, blocker linkage. Nothing is dumped.

Deliberately absent: burndown charts, velocity, counts-as-metrics, agent conversation logs, and any number that does not change a Founder action.

The page is one self-contained HTML file with the state inlined at render time. It has no network calls, no external fonts, no analytics, and no build step. It opens by double-click on Mac, PC, and mobile, and renders identically from the loopback server. Verified responsive from 345 px to 1280 px with zero horizontal overflow.

### 9. Security and privacy

| Property | State |
|---|---|
| Credentials in the repository | None. None added. |
| Network calls from the Console | None. The page reads no remote resource. |
| Server binding | `127.0.0.1` only. Not reachable off-host. |
| Authentication | **Not implemented, and not required at loopback scope.** |
| Personal data | Only the Founder's name and role, already present in the vault. |

The absence of authentication is a deliberate consequence of the loopback boundary, not an oversight. **Any hosted deployment must ship an authentication system first** — this repository has none, and exposing Founder state publicly is an explicit autonomy boundary. Recorded as `FD-002`, **ratified 2026-09-01**.

### 10. Extension points for future inputs

Future sources write `context_items` and, where they imply work, `tasks` or `decisions`. That is the whole contract; no source-specific coupling enters the model.

The OMI pipeline in mission §11 maps onto it directly:

```
OMI recording → transcript → ingestion → LUMIAION classification
   → decisions / tasks / commitments / ideas / knowledge / people
   → deduplication → routing → Founder OS → memory
```

**No OMI code was written and no OMI credential exists in this repository.** Provisioning one crosses the new-secrets autonomy boundary, so it is queued as `FD-003` rather than assumed. The integration reports `not_connected`, which is the honest status per mission §10.

The same applies to Google Calendar, ChatGPT/Codex, health, and financial systems: contracts exist, adapters do not, and every one of them reports its true status in the Console.

---

## Verification

| Check | Command | Result |
|---|---|---|
| Engine tests | `python3 "08_SYSTEMS/Engineering Toolkit/test_founder_os.py"` | 44 passed, 0 skipped |
| State validity | `ap.py founder check` | OK — 55 records, 0 notes |
| Vault validation | `ap.py validate` | 5 errors / 479 warnings — unchanged from the pre-session baseline |
| Browser render | headless Chromium, 345 px and 1280 px | renders; no horizontal overflow |

The vault validator's pre-existing 5 errors and 479 warnings were **not** introduced by this work and were **not** fixed by it; repairing them belongs to CN-001, which owns the taxonomy.

---

## Open Questions

- ~~Does the Founder accept Vault-native JSON as the state store?~~ **Resolved 2026-08-31: ratified (`FD-001` approved).** Revisit only when concurrent multi-writer access is genuinely required.
- ~~Should the Console remain local-only?~~ **Resolved 2026-09-01: local-only ratified (`FD-002` approved).** Hosting is a separate decision that must ship authentication first.
- When should OMI credentials be authorized? (`FD-003`)
- Should the hand-maintained Markdown dashboards in `11_OPERATIONS/` be generated from state, and does that belong to CN-001?
- Does the Founder want Founder OS state committed automatically at session end, or only on explicit instruction?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.2.0 | 2026-09-01 | CLAUDE / CODEX | FD-002 ratified (Console stays local-only); state corrected after the #8/#9/#10 merges |
| 1.1.0 | 2026-08-31 | CLAUDE / CODEX / LUMIAION | FD-001 ratified: Vault-native JSON is the state store. Recorded the `task-state` defect and its regression tests |
| 1.0.0 | 2026-08-26 | CLAUDE / CODEX / LUMIAION | First Founder OS architecture: repository audit, state contract, orchestration contract, presentation boundary, Console V1 |
