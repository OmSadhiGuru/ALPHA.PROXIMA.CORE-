---
title: "Founder OS README"
aliases: ["Founder OS README", "Founder Console Handbook", "Founder OS Continuation"]
tags: [operations, founder-os, console, handbook, continuation, alpha-proxima]
created: 2026-08-26
updated: 2026-08-26
status: active
version: "1.0.0"
authors: ["CODEX", "CLAUDE"]
artifact_type: readme
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Founder OS Architecture v1]]"]
related_documents: ["[[Founder Console]]", "[[Alpha Proxima Engineering Toolkit]]", "[[Founder Reboot Control Center]]"]
related_research_programs: []
---

# Founder OS README

One control plane for the Founder. State lives in this folder; the Console is generated from it.

For *why* it is built this way, read [[Founder OS Architecture v1]].

---

## Purpose

Founder OS gives Alpha Proxima a machine-readable Founder state with exactly one writer, and one calm surface that reads it. It replaces mental reconciliation across hand-kept dashboards with a single document that can be validated, versioned, and consumed by any future interface.

---

## Context

### Open the Console

```bash
open "11_OPERATIONS/Founder OS/console/console.html"      # macOS
start "11_OPERATIONS\Founder OS\console\console.html"     # Windows
```

The file is self-contained — state is embedded at render time. No server, no network, no build step. On mobile, open it from the synced vault folder.

For a live view that re-reads state on every request:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" founder serve
# http://127.0.0.1:8787/          Console
# http://127.0.0.1:8787/api/view  read model  (the future spatial/VR contract)
# http://127.0.0.1:8787/api/state raw state
```

The server binds `127.0.0.1` only and has no authentication. Do not expose it — see [[Founder OS Architecture v1]] §9.

In Obsidian, read [[Founder Console]]. It is generated and regenerated on every state change; edits there are overwritten.

---

## Core Content

### Layout

```
11_OPERATIONS/Founder OS/
├── README.md                       this file
├── Founder OS Architecture v1.md   the contract and the reasoning
├── Founder Console.md              generated Obsidian mirror — do not edit
├── state/
│   └── founder-state.json          canonical state — the only source of truth
└── console/
    ├── console.template.html       the page (edit this to change the design)
    └── console.html                generated — do not edit
```

Implementation lives with the rest of the toolkit:

```
08_SYSTEMS/Engineering Toolkit/
├── founder_os.py        state engine, CLI, renderer, loopback server
└── test_founder_os.py   39 tests
```

### Daily use

```bash
AP='python3 "08_SYSTEMS/Engineering Toolkit/ap.py" founder'

$AP show                                    # the four questions, in the terminal
$AP mission "Close RBT-001" --sprint RBT-001
$AP priority-add "Resolve the draft PRs" --why "CN-001 is blocked" --owner Founder
$AP next-action "Review PR #10" --owner Founder --priority PRI-001
$AP priority-status PRI-001 done
```

Routing and execution:

```bash
$AP task-add "Build the CN-001 relocation map" --owner CODEX \
    --why "Coherence precedes expansion" --by LUMIAION --gate G2
$AP task-state TSK-001 working
$AP task-state TSK-001 complete --output "[[CN-001 Relocation Map]]"
$AP agent-status AGT-003 working
$AP blocker-add "No OMI credential" --impact "Capture pipeline cannot ship" \
    --owner Founder --needs-founder
```

Founder decisions:

```bash
$AP decision-add "Adopt X" --context "..." --recommendation "..." \
    --option "A" --option "B" --consequence "..."
$AP decision-resolve FD-001 approved --note "Ratified 2026-08-26"
```

Maintenance:

```bash
$AP check                                   # validate state
$AP render                                  # regenerate console.html + the mirror
python3 "08_SYSTEMS/Engineering Toolkit/test_founder_os.py"
```

Every mutating command validates, saves, and re-renders both views. There is no separate build step to forget.

### Rules the system enforces for you

- **At most three open priorities.** A fourth is rejected. This is the cognitive-load requirement in code.
- **Every task carries `owner`, `requested_by`, and `why`.** Work that cannot say why it exists cannot be saved.
- **The Mission of the Day goes stale on its own** when its date is not today, and says so in the Console.
- **Closing a priority clears a Next Action bound to it,** so the Founder is never shown a stale instruction.
- **Integrations must declare an honest status** — `connected`, `not_connected`, `planned`, or `blocked`. Nothing may pretend to be wired up.

### Do not

- Edit `console.html` or `Founder Console.md` — both are generated.
- Edit `founder-state.json` by hand — use the CLI, which validates before writing.
- Expose the server beyond `127.0.0.1` — there is no authentication (`FD-002`).
- Commit credentials. Founder OS needs none and adds none.

---

## Continuation

The next session can resume from here without re-deriving anything.

**Verified state as of 2026-08-26**

- Console V1 is built, tested, and rendering. State holds 55 records seeded from repository evidence.
- The vertical slice — Mission → state → Console → editable → persisted → tested — is closed end to end.
- Vault validation is unchanged from its pre-session baseline: 5 errors, 479 warnings. Those belong to CN-001.

**Waiting on the Founder**

- `FD-001` Ratify Vault-native JSON as the state store.
- `FD-002` Keep the Console local-only.
- `FD-003` Authorize OMI credentials.
- Four decisions carried from [[Founder Reboot Control Center]] (coherence-first order; ARTEMIS/POSTMANIUM proposed; Secretary-General proposed; selective PR salvage).

**Next three actions**

1. Founder reviews [[Founder OS Architecture v1]] and resolves `FD-001`.
2. Resolve the four open draft PRs (#7, #8, #9, #10) so CN-001 can start.
3. Run the photo-to-social-post routing proof through Founder OS, recording each handoff as an `agent_run`.

**Not built, deliberately**

VR/spatial presentation, OMI ingestion, calendar or health adapters, automatic state commits, and multi-writer concurrency. Each is either behind a Founder decision or behind the routing proof.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-08-26 | CODEX / CLAUDE | Founder OS V1 handbook and continuation record |
