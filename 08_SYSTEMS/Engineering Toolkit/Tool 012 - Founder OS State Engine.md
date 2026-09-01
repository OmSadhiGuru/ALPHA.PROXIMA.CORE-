---
title: "Tool 012 - Founder OS State Engine"
aliases: ["Founder OS State Engine", "founder_os", "Engineering Toolkit Tool 012", "ap founder"]
tags: [systems, engineering, toolkit, founder-os, console, state, alpha-proxima]
created: 2026-08-26
updated: 2026-09-01
status: active
version: "1.1.0"
authors: ["CODEX"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["Python 3 standard library", "[[Tool 008 - Engineering CLI]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Founder OS Architecture v1]]", "[[Founder OS README]]", "[[Founder Console]]"]
related_research_programs: []
---

# Tool 012 - Founder OS State Engine

## Purpose

Own the canonical Founder state document and generate every view of it. This module is the **only** writer of `11_OPERATIONS/Founder OS/state/founder-state.json`; the Console page and the Obsidian mirror are generated artifacts.

## Context

Before this tool, Founder state existed only as hand-maintained Markdown tables that nothing could validate or query. The state engine gives that state a schema, enforced invariants, provenance, and a read model that any presentation layer — terminal, browser, or a future spatial interface — can consume without the domain model changing.

Standard library only, consistent with the rest of the toolkit.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" founder <command> [options]
```

| Command | Effect |
|---|---|
| `init` | Create an empty state document. |
| `show` | Print the Founder Console summary to the terminal. |
| `check` | Validate state; report structural notes. |
| `render` | Regenerate `console.html` and [[Founder Console]]. |
| `serve [--port]` | Serve the Console and its read model on `127.0.0.1`. |
| `state` / `view` | Print raw state / the Console read model as JSON. |
| `mission <text>` | Set the Mission of the Day. |
| `priority-add <title>` | Add a Top 3 priority (rejected when three are already open). |
| `priority-status <id> <status>` | `open` \| `done` \| `dropped`. |
| `next-action <title>` | Set the single Next Action. |
| `decision-add` / `decision-resolve` | Queue and resolve Founder decisions. |
| `task-add` / `task-state` | Create work units and move them between states. |
| `agent-status <id> <status>` | Set an agent's operational status. |
| `health-set <id> <status>` | Update a system-health signal (`--detail`, `--source`). |
| `blocker-add` / `blocker-resolve` | Record and clear blockers. |

Paths are overridable with `--state`, `--template`, `--console`, and `--mirror`; the defaults resolve inside the Vault.

## Behaviour

- Every mutating command validates, saves, and re-renders both views — there is no separate build step.
- Invalid input fails with a one-line message and exit code 1, never a traceback.
- Enforced invariants: at most three open priorities; mandatory `owner` / `requested_by` / `why` on every task; closed-loop referential integrity between the Next Action and its priority.
- `serve` binds loopback only and provides no authentication — see [[Founder OS Architecture v1]] §9 before changing that.

## HTTP Endpoints

| Route | Returns |
|---|---|
| `/` | The rendered Console. |
| `/api/view` | The read model. This is the contract a future spatial or voice interface consumes. |
| `/api/state` | The raw state document. |

## Tests

```bash
python3 "08_SYSTEMS/Engineering Toolkit/test_founder_os.py"
```

44 tests covering the state lifecycle, every enforced invariant, the decision and task state machines, rendering (including `</script>` escaping in embedded state), the CLI vertical slice, and the validity of the state document committed to the Vault.

Every mutating subcommand is exercised through `main()` rather than by calling its function directly, and one structural test asserts that no subcommand reuses a global option's argparse dest. Both exist because `task-state` shipped broken in v1.0.0: its `state` positional shared a dest with the global `--state`, so the task state overwrote the state-file path. Tests that call the mutators directly cannot catch that class of defect.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-09-01 | [[CODEX]] | Added `health-set`: system-health signals were displayed but unreachable from the CLI, so they could only go stale |
| 1.0.1 | 2026-08-31 | [[CODEX]] | Fixed `task-state` argparse dest collision with the global `--state`; added CLI-level and structural regression tests |
| 1.0.0 | 2026-08-26 | CODEX | Initial Founder OS state engine, Console renderer, and loopback server |
