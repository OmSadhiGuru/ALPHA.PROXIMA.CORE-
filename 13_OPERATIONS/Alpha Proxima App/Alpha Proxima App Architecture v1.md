---
title: "Alpha Proxima App Architecture v1"
aliases: ["Alpha Proxima App", "App Architecture", "Alpha Proxima App Architecture", "The App"]
tags: [operations, app, interface, architecture, founder-os, knowledge-graph, lumiaion, alpha-proxima]
created: 2026-09-01
updated: 2026-09-01
status: active
version: "1.0.0"
authors: ["CLAUDE"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Architecture"
reasoning_engine: "Claude"
dependencies: ["[[Founder OS Architecture v1]]", "[[Knowledge Graph Architecture v1.0]]", "[[03 - Folder Naming Convention]]", "[[02 - YAML Frontmatter Standard]]"]
related_documents: ["[[Alpha Proxima App README]]", "[[Founder Console]]", "[[Founder OS README]]", "[[Tool 013 - Alpha Proxima App]]", "[[Alpha Proxima Engineering Toolkit]]", "[[Book III - Knowledge Integrity]]", "[[CN-001 Execution Tracker]]"]
related_research_programs: []
---

# Alpha Proxima App Architecture v1

## Purpose

Specify the Foundation's single application interface: one surface from which the Founder can both **operate** the institution and **read** what it knows, without switching tools or reconciling two mental models.

It is deliberately narrow. It covers what was built and verified on 2026-09-01, the contracts it introduces, and what it refuses to do. It does not amend the Constitution, activate an office, ratify a decision, or alter a single institutional note.

---

## Mission

Give Alpha Proxima an interface that will still make sense when its storage, its rendering technology, and its authors have all been replaced.

The design test applied to every decision below: **would this still be readable, navigable, and repairable in one hundred years by someone who has never met its authors?** A folder of Markdown with an index that regenerates itself passes. A hosted application with a proprietary database and an expired certificate does not.

---

## Definitions

| Term | Meaning |
|---|---|
| **Half** | One of the app's two top-level modes: `operate` or `know`. Not a page — a way of asking. |
| **Read model** | A derived, presentation-facing structure. Interfaces consume it; they never touch storage. |
| **Vault index** | A compact record per note: metadata and relationships, never note bodies. |
| **Entry** | One indexed document. |
| **Edge** | A resolved link from one entry to another. |
| **Unresolved link** | A wiki-link whose target does not exist. A coherence defect, not a broken string to discard. |
| **Orphan** | A document with no edges in either direction. A violation of the Library Rule. |
| **Coherence defect** | Any of: orphan, missing frontmatter, unresolved link, empty document. |
| **Ceiling** | The number of coherence defects the Foundation currently tolerates. It ratchets down, never up. |

---

## Context

### 1. What existed before

Founder OS V1 ([[Founder OS Architecture v1]]) established a machine-readable Founder state with exactly one writer, and rendered a read-only Console from it. That solved the *operating* half.

The *knowing* half had no interface at all. The Foundation's institutional documents — 272 at the time of writing — were reachable only by opening Obsidian and navigating folders by hand. Two registries existed — [[Tool 010 - Node Registry Generator]] and [[Tool 011 - Relationship Extractor]] — but they were generated once on 2026-07-03 against a different machine's vault path, are 1.9 MB combined, and nothing consumed them.

So the Founder held two separate models: a cockpit that knew about work, and a filesystem that held knowledge. Nothing connected them.

### 2. The finding that shaped this design

Indexing the vault produced a measurement nobody had:

| Signal | Value |
|---|---|
| Institutional documents | 272 |
| Documents that connect to something | 247 (90.8%) |
| **Orphans — connected to nothing** | **25** |
| **Documents with no YAML frontmatter** | **16** |
| **Links pointing at documents that do not exist** | **198** |
| **Empty documents** | **4** |
| **Top-level folders outside the canonical hierarchy** | **7** |

[[Book III - Knowledge Integrity]] and the Library Rule both require that knowledge connect. Until now that requirement had no number attached to it, so it could not be verified, tracked, or closed. It was an aspiration.

The V1 scan exposed seven uncanonical folders and two number collisions. The Founder subsequently ratified `11_PROJECTS`, `12_PEOPLE`, and `13_OPERATIONS`, resolving the project, people, and operations collisions. `09_FUTURE` remains visible but uncanonical because `09_OFFICES` owns reservation `09`; resolving that remaining namespace requires a separate Founder decision. Legacy and adjacent workstreams remain visible rather than silently hidden.

**The app does not repair any of this.** Repair is CN-001's, which owns the taxonomy ([[CN-001 Execution Tracker]]). The app's contribution is to make the gap continuously visible instead of periodically rediscovered.

---

## Architecture

### 3. The composition

```
founder-state.json ──► founder_os.build_view() ──┐
   (one writer,                                  │
    validated)                                   ├──► build_app_view() ──► app.html
                                                 │      (read model)       (generated)
272 vault notes ────► build_vault_index() ───────┘                    └──► vault-index.json
   (authored by                                                              (generated)
    their owners)
```

Two sources of truth, each with exactly one writer, composed into one read model. The app is a **third consumer**, not a third store.

### 4. The two halves

The split is not navigational convenience. It reflects what an institution actually is: something that acts, and something that remembers.

| Half | Question | Source | Answers |
|---|---|---|---|
| **Operate** | What is happening now? | `founder-state.json` | Mission of the Day, Top 3, Next Action, decisions awaiting the Founder, blockers, execution, Council status, systems, integrations |
| **Know** | What does the Foundation know? | The vault | 14 constitutional domains, full-text search over metadata, per-document connections in both directions, coherence reporting |

Each domain in the Know half carries the question it answers — *Constitution: what may not be violated; Research: what is being investigated* — because a folder name is a label, and a question is an explanation. Labels decay when their authors leave; questions do not.

### 5. Two rules that keep this a presentation layer

Both are enforced by tests, not by discipline.

**It writes nothing.** `alpha_app.py` imports `founder_os` for its read model and never calls a mutation. `test_the_app_never_writes_state` asserts that no `founder_os.save_state`, `set_mission`, `add_task`, `add_priority`, or `resolve_decision` call appears in the module's source. The single-writer property Founder OS established is preserved exactly.

**It never copies vault content.** The index stores a document's *metadata and relationships*, never its body. `test_entry_carries_metadata_but_never_the_body` asserts no note text reaches an index entry. This matters more than it appears: an index that embedded note bodies would become a second, silently-stale copy of the Foundation's canon — precisely the reconciliation problem Founder OS was built to remove. Instead, the app **routes** to each document (`obsidian://` and a relative file link). A document's text lives in exactly one place: the document.

### 6. Relationships

An edge is recorded when a link resolves to a real document. Three details are deliberate:

- **Frontmatter links count.** A `dependencies:` or `related_documents:` entry is as real a relationship as a body wiki-link. [[02 - YAML Frontmatter Standard]] made those fields load-bearing; the graph honours them.
- **Code is excluded — fenced blocks and inline spans alike.** A wiki-link quoted inside backticks in a standard or a template is documentation *about* links, not a link. Counting it would both inflate connectedness with fiction and report phantom broken references; enabling this in V1 removed 10 false defects.
- **Unresolved links are kept, not dropped.** A link to a document that does not exist is a coherence defect and is reported as one. Silently discarding it would hide the 198 broken references the Foundation currently carries.

Backlinks are **derived, never stored**. Storing both directions of an edge writes the same fact twice and invites the two copies to disagree. Consumers invert `links`; the app does this in the browser at render time.

### 7. Coherence as a ratchet

`ap.py app check` fails when defects exceed an agreed ceiling:

```bash
ap.py app check                     # ceiling 0 — the destination
ap.py app check --max-defects 243   # today's honest baseline
```

The ceiling exists because a gate that can never pass is not a gate — it is noise that teams learn to ignore. A ceiling that only ever decreases turns 243 defects from a permanent embarrassment into a tracked, closable number. **It must never be raised.** Raising it is how institutions quietly ratify their own decay.

The ceiling is not stored in the repository. It is passed explicitly by whoever runs the check, so lowering it is a visible act in a command or a workflow, never a silent edit to a config file.

### 8. Presentation

One self-contained HTML file with the read model inlined at render time. No build step, no framework, no bundler, no external font, no network call, no analytics. It opens by double-click on Mac, PC, and phone from the synced vault, and renders identically from the loopback server.

The palette and type scale are inherited from Founder Console V1 without modification: one Foundation, one visual language. Teal marks the institution; **gold is reserved exclusively for what requires the Founder** and is never used decoratively. A Founder who learns that gold means *you* can scan the interface in one pass.

Deliberately absent: burndown charts, velocity, activity feeds, engagement metrics, and any number that does not name a repair or change a Founder action. The four coherence counts are the only metrics in the application, and each one names a specific document to fix.

### 9. Security and privacy

| Property | State |
|---|---|
| Credentials in the repository | None. None added. |
| Network calls from the app | None. Asserted by `test_the_app_makes_no_network_call`. |
| Server binding | `127.0.0.1` only, port 8788. Not reachable off-host. |
| Authentication | **Not implemented, and not required at loopback scope.** |
| Third-party dependencies | None. Python standard library and vanilla JavaScript. |
| Personal data | Only the Founder's name and role, already present in the vault. |

`FD-002` is ratified: the Founder's surfaces stay local-only, and any hosted deployment must ship authentication first. This app was built to that constraint rather than around it, and no amendment was required.

The one injection surface — a note title or tag reaching the inlined JSON — is closed by escaping `</` before inlining, asserted by `test_render_escapes_closing_script_tags`. All DOM text is set through `textContent`; the app never assigns `innerHTML`.

### 10. The presentation boundary holds

`GET /api/app` returns the composed read model. A future spatial, voice, or accessibility layer consumes that document and needs to know nothing about how state is stored or how the vault is laid out.

The chakra mapping recorded in [[Founder OS Architecture v1]] §7 remains a **presentation mapping only**. No entity, field, or endpoint in this module references it. The two halves are `operate` and `know`; a spatial layer may map them onto that model, and nothing here will know it did.

---

## Dependencies

| Dependency | Nature |
|---|---|
| Python 3 standard library | Runtime. Nothing else. |
| `founder_os.py` | Read model for the Operate half. Imported, never mutated. |
| `vault_validator.py` | Markdown discovery and frontmatter parsing. Shared, not reimplemented. |
| `founder-state.json` | Canonical Founder state. Read-only to this module. |
| The vault's Markdown notes | Canonical knowledge. Read-only to this module. |
| A browser | Any browser from the last decade. No specific engine. |

---

## Related Documents

- [[Founder OS Architecture v1]] — the state contract this app reads
- [[Alpha Proxima App README]] — how to run it
- [[Tool 013 - Alpha Proxima App]] — toolkit registration and CLI reference
- [[Knowledge Graph Architecture v1.0]] — the graph model this index is an operational subset of
- [[Book III - Knowledge Integrity]] — the constitutional basis for coherence reporting
- [[03 - Folder Naming Convention]] — the hierarchy the domain map measures against
- [[CN-001 Execution Tracker]] — owner of every repair this app reports

---

## Examples

```bash
AP='python3 "08_SYSTEMS/Engineering Toolkit/ap.py" app'

$AP show      # both halves, in the terminal
$AP render    # regenerate app.html and vault-index.json
$AP check     # coherence defects against a ceiling
$AP serve     # http://127.0.0.1:8788/
open "13_OPERATIONS/Alpha Proxima App/app/app.html"
```

---

## Verification

Performed 2026-09-01 on `main` at `99c081e`.

| Check | Method | Result |
|---|---|---|
| App engine tests | `test_alpha_app.py` | 34 passed |
| Founder OS regression | `test_founder_os.py` | 45 passed, unchanged |
| Renders from `file://` | headless Chromium | 272 entries, 19 domains, 0 JS errors |
| Interactive paths | scripted probe: half switch, search, entry select, link traversal, domain filter, coherence panel | 19 assertions passed at 485 px, 768 px, 1280 px |
| True mobile width | 330 px viewport | no horizontal overflow; no overflowing element |
| Vault validation | `ap.py validate` | unchanged from baseline — this work introduced no error and fixed none |

No institutional note was created, modified, moved, or deleted by the app. The only pre-existing file changed by this work is `ap.py`, which gained one registry line.

---

## Future Improvements

1. **Regenerate the stale graph registries.** [[Tool 010 - Node Registry Generator]] and [[Tool 011 - Relationship Extractor]] still carry 2026-07-03 output against another machine's path. The app's index supersedes them operationally; the registries should either be regenerated or formally retired.
2. **A visual graph.** The index carries every edge needed to draw one. It was omitted from V1 because a force-directed diagram of 272 nodes is decorative, not navigable — the per-document connection list answers "how does this connect?" better than a hairball does.
3. **Lower the ceiling as CN-001 closes.** Each repaired batch should lower `--max-defects` in the same commit, so the number is never left behind.
4. **A `write` half, behind a Founder decision.** The app is read-only by design. Editing state from the interface means a second writer and is a decision (`FD-001` revisit), not an enhancement.
5. **Domain questions for uncanonical folders.** The seven loose folders currently read "Not yet placed in the canonical hierarchy." When CN-001 places them, each earns a real question.

---

## Open Questions

- Should `ap.py app render` run automatically whenever Founder OS state changes, or stay an explicit act? Founder OS re-renders its Console on every mutation; the app does not, because indexing 272 notes on every `task-state` call is a cost with no reader.
- Do the seven uncanonical folders get relocated, chartered in place, or archived? Three of them (`OSG_LAUNCH`, `OSG_BUSINESS`, `ALPHA PROXIMA`) hold 70 documents between them. This is CN-001's decision, and the largest single lever on the connectedness number.
- Should coherence defects become Founder OS `blockers` automatically, so repair work enters the operating half instead of living only in a report?
- Is 90.8% connectedness acceptable as a long-term floor, or does the Foundation commit to a target?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-01 | CLAUDE | First Alpha Proxima App architecture: the two halves, the vault index contract, coherence as a ratchet, and the presentation boundary |
