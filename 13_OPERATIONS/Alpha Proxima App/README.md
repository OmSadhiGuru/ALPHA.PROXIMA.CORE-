---
title: "Alpha Proxima App README"
aliases: ["Alpha Proxima App README", "App Handbook", "App Continuation"]
tags: [operations, app, interface, readme, handbook, continuation, alpha-proxima]
created: 2026-09-01
updated: 2026-09-01
status: active
version: "1.1.0"
authors: ["CLAUDE"]
artifact_type: readme
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "Claude"
dependencies: ["[[Alpha Proxima App Architecture v1]]"]
related_documents: ["[[Founder OS README]]", "[[Founder Console]]", "[[Tool 013 - Alpha Proxima App]]", "[[Alpha Proxima Engineering Toolkit]]", "[[CN-001 Execution Tracker]]"]
related_research_programs: []
---

# Alpha Proxima App README

One interface for the whole Foundation. It **operates** and it **knows**.

For *why* it is built this way, read [[Alpha Proxima App Architecture v1]].

---

## Purpose

The Founder had a cockpit that knew about work ([[Founder Console]]) and a filesystem that held knowledge. Nothing connected them. This app is the single surface over both, and the first thing in the Foundation that can say how well its own knowledge connects.

---

## Context

### Open it

```bash
open "13_OPERATIONS/Alpha Proxima App/app/app.html"      # macOS
start "13_OPERATIONS\Alpha Proxima App\app\app.html"     # Windows
```

Self-contained — both halves are inlined at render time. No server, no network, no build step. On mobile, open it from the synced vault folder.

For a live view that re-reads state and re-indexes the vault on every request:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" app serve
# http://127.0.0.1:8788/            the app
# http://127.0.0.1:8788/api/app     composed read model  (the spatial/VR contract)
# http://127.0.0.1:8788/api/vault   vault index only
# http://127.0.0.1:8788/api/view    Founder OS read model only
```

Loopback only, no authentication. Do not expose it — `FD-002` is ratified.

### The two halves

| Half | Question | What it shows |
|---|---|---|
| **Operate** | What is happening now? | Mission of the Day, Top 3, Next Action, decisions awaiting you, blockers, execution, Council, systems, integrations |
| **Know** | What does the Foundation know? | 21 populated domains, search across all metadata, per-document connections both ways, coherence reporting |

Switch with the pill at the top, arrow keys, or the URL: `app.html#operate`, `app.html#know`.

### In the Know half

- **Click a domain** to filter to it. Click again to clear.
- **Search** matches titles, paths, tags, artifact types, owners, functions, and authors. Multiple words are ANDed.
- **Click a document** to see its metadata, everything it connects to, everything that references it, and any broken links it carries.
- **Click a connection** to travel to that document. This is how the knowledge graph is meant to be walked.
- **Open in Obsidian** opens the real note. The app routes to documents; it never holds copies of them.

---

## Core Content

### Layout

```
13_OPERATIONS/Alpha Proxima App/
├── README.md                             this file
├── Alpha Proxima App Architecture v1.md  the contracts and the reasoning
└── app/
    ├── app.template.html                 the interface (edit this to change the design)
    ├── app.html                          generated — do not edit
    └── vault-index.json                  generated — the knowledge read model
```

Implementation lives with the rest of the toolkit:

```
08_SYSTEMS/Engineering Toolkit/
├── alpha_app.py        index, read model, renderer, loopback server
└── test_alpha_app.py   34 tests
```

### Commands

```bash
AP='python3 "08_SYSTEMS/Engineering Toolkit/ap.py" app'

$AP show                      # both halves, in the terminal
$AP render                    # regenerate app.html and vault-index.json
$AP check                     # coherence defects against a ceiling of 0
$AP check --max-defects 422   # reconciled PR #7 corpus baseline; ratchet downward
$AP serve [--port 8788]       # loopback server
$AP index                     # the vault index as JSON
$AP view                      # the composed read model as JSON
```

Paths are overridable with `--root`, `--state`, `--template`, `--app`, and `--index`. They are **global options and precede the subcommand** — `app --app out.html render`, not `app render --app out.html`, which argparse rejects. This matches `ap.py founder`.

### Regenerating

The app does **not** re-render itself when Founder OS state changes, because indexing 363 notes on every `task-state` call costs time no reader benefits from. Run `render` when you want the file refreshed, or use `serve` for a view that is always current:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" founder task-state TSK-004 working
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" app render
```

### What the app enforces

- **It writes nothing.** Founder state is written only by `ap.py founder`; notes are written only by their authors. A test asserts no mutation call exists in the module.
- **It never copies note bodies.** The index holds metadata and relationships. A test asserts no note text reaches an index entry.
- **It makes no network call.** A test asserts the template contains no URL, `fetch`, `XMLHttpRequest`, `WebSocket`, `<link>`, or `@import`.
- **Broken links are reported, never dropped.** A link to a document that does not exist is a coherence defect.
- **Links inside code are not relationships** — fenced blocks and inline backticks alike. A link quoted in a standard is documentation *about* links, not an edge.

### Do not

- Edit `app.html` or `vault-index.json` — both are generated. Edit `app.template.html`.
- Expose the server beyond `127.0.0.1` — there is no authentication (`FD-002`).
- **Raise `--max-defects` to excuse new defects inside the indexed corpus.** The ceiling ratchets down. The only permitted reset is a Founder-ratified corpus expansion with both baselines recorded, as occurred when PR #7 added previously unindexed constitutional and research material.

---

## Continuation

The next session can resume from here without re-deriving anything.

**Verified state after PR #7 reconciliation**

- App V1 is built, tested, and rendering. 34 app tests pass; Founder OS's 45 pass unchanged.
- Verified in headless Chromium at 330 px, 485 px, 768 px, and 1280 px: no horizontal overflow, no JavaScript errors, all 19 interactive assertions passing.
- The app is registered as `ap.py app`. Four pre-existing files were modified, all of them registrations or cross-references: `ap.py` (one registry line), [[Alpha Proxima Engineering Toolkit]] (Tool 013 and two CLI rows), and the Founder OS [[Founder OS README|README]] and [[Founder OS Architecture v1|architecture]] (links back to this app).
- The Founder-ratified hierarchy is enacted: `11_PROJECTS`, `12_PEOPLE`, and `13_OPERATIONS`. Generated and personal Obsidian state is excluded from version control.

**What the app measured, that nobody had before**

| Signal | Value |
|---|---|
| Institutional documents | 363 |
| Connected | 312 (86.0%) |
| Orphans | 51 |
| Missing frontmatter | 18 |
| Broken links | 349 |
| Empty documents | 4 |
| Coherence defects | 422 |
| Folders outside the canonical hierarchy | 7, holding 77 documents |

**All of this belongs to CN-001, not to the app.** The app's job is to keep it visible; [[CN-001 Execution Tracker]] owns the repair.

**Waiting on the Founder**

- What canonical number, if any, should replace the uncanonical `09_FUTURE` namespace now that `09_OFFICES` owns reservation `09`?
- Should coherence defects become Founder OS `blockers`, so repair enters the operating half rather than living only in a report?
- Does the Foundation commit to a connectedness target, or is 90.8% an acceptable floor?

**Next three actions**

1. Take the domain map to CN-001 and decide placement for the seven loose folders.
2. Lower `--max-defects` in the same commit as each repaired batch.
3. Regenerate or formally retire the 2026-07-03 graph registries, which the app's index now supersedes operationally.

**Not built, deliberately**

A visual graph (a 363-node hairball is decorative, not navigable — the per-document connection list answers the real question better), editing from the interface (a second writer is a Founder decision, not an enhancement), automatic re-render on state change, and any hosted deployment.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-01 | CLAUDE | First App handbook: the two halves, commands, enforced rules, and the coherence baseline |
| 1.1.0 | 2026-09-02 | Founder / CODEX | PR #7 reconciliation: enact `11_PROJECTS`, `12_PEOPLE`, `13_OPERATIONS`; refresh generated index and the expanded-corpus baseline |
