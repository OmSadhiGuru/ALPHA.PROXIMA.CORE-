---
title: "Tool 013 - Alpha Proxima App"
aliases: ["Alpha Proxima App Tool", "alpha_app", "Engineering Toolkit Tool 013", "ap app"]
tags: [systems, engineering, toolkit, app, interface, knowledge-graph, coherence, alpha-proxima]
created: 2026-09-01
updated: 2026-09-01
status: active
version: "1.0.0"
authors: ["CLAUDE"]
artifact_type: implementation-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "Claude"
dependencies: ["Python 3 standard library", "[[Tool 008 - Engineering CLI]]", "[[Tool 012 - Founder OS State Engine]]", "[[Tool 001 - Vault Validator]]"]
related_documents: ["[[Alpha Proxima Engineering Toolkit]]", "[[Alpha Proxima App Architecture v1]]", "[[Alpha Proxima App README]]", "[[Founder Console]]", "[[Tool 010 - Node Registry Generator]]", "[[Tool 011 - Relationship Extractor]]", "[[12 - Continuous Integration Standard]]"]
related_research_programs: []
---

# Tool 013 - Alpha Proxima App

## Purpose

Compose the Foundation's two halves — what it **operates** and what it **knows** — into one interface, and report how well its knowledge actually connects.

This module is a **presentation layer only**. It writes nothing and copies nothing. Founder state remains written solely by [[Tool 012 - Founder OS State Engine]]; institutional notes remain written solely by their authors.

## Context

Before this tool, the Founder held two disconnected models: a cockpit that knew about work ([[Founder Console]]) and a filesystem that held knowledge. The app joins them behind one read model, and in doing so produces the Foundation's first measurement of its own coherence.

It reuses rather than reimplements: `vault_validator` supplies Markdown discovery and frontmatter parsing, `founder_os` supplies the operating read model. Standard library only, consistent with the rest of the toolkit.

## CLI Interface

```bash
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" app <command> [options]
```

| Command | Effect |
|---|---|
| `show` | Print both halves to the terminal. |
| `render` | Regenerate `app.html` and `vault-index.json`. |
| `check [--max-defects N]` | Report coherence defects against a ceiling; exit 1 above it. |
| `serve [--port]` | Serve the app and its read model on `127.0.0.1` (default 8788). |
| `index` | Print the vault index as JSON. |
| `view` | Print the composed read model as JSON. |

Paths are overridable with `--root`, `--state`, `--template`, `--app`, and `--index`; the defaults resolve inside the Vault.

## HTTP Contract

Loopback only. No authentication, per ratified `FD-002`.

| Route | Returns |
|---|---|
| `/` | The rendered app. |
| `/api/app` | The composed read model — the contract a future spatial, voice, or accessible layer consumes. |
| `/api/vault` | The vault index alone. |
| `/api/view` | The Founder OS read model alone. |
| `/api/state` | Raw Founder state. |

## Behaviour

- **Never writes.** No `founder_os` mutation is called; a test asserts none appears in the module's source.
- **Never copies note bodies.** The index carries metadata and relationships only; a test asserts no note text reaches an entry.
- **Never calls the network.** A test asserts the template contains no URL, `fetch`, `XMLHttpRequest`, `WebSocket`, `<link>`, or `@import`.
- **Frontmatter links count as relationships**, alongside body wiki-links.
- **Links resolve the way Obsidian resolves them** — a bare `[[Note]]` by title or filename, a qualified `[[folder/Note]]` against any path ending at that suffix. A link that works in Obsidian is never reported as a defect; a trailing slash stays unresolved, because a folder is not a document.
- **Links inside code do not** — fenced blocks and inline backticks alike — so a standard that quotes a link cannot inflate connectedness or report a phantom broken reference.
- **Backlinks are derived, never stored** — the same fact is never written down twice.
- **Unresolved links are reported, not discarded**; a link to a nonexistent document is a coherence defect.
- Invalid input fails with a one-line message and a non-zero exit code, never a traceback.

## Coherence Ratchet

`check` fails when defects exceed `--max-defects` (default 0). The ceiling exists so the gate can pass today and tighten over time; **it must only ever be lowered.** It is passed explicitly rather than stored, so every change to it is visible in a command or workflow rather than buried in configuration.

The ratchet runs on every change via [[12 - Continuous Integration Standard|Foundation Integrity]], which declares the ceiling as `COHERENCE_CEILING`.

Baseline recorded 2026-09-02: **135 defects** across 366 documents — 21 orphans, 18 missing frontmatter, 92 broken links, 4 empty. All belong to CN-001, which owns the taxonomy.

This supersedes a 422 figure set earlier the same day, which was an artefact of the resolver ignoring path-qualified links rather than a condition of the vault. See [[12 - Continuous Integration Standard]], *Check the instrument before raising the tolerance*.

## Relationship to Tools 010 and 011

[[Tool 010 - Node Registry Generator]] and [[Tool 011 - Relationship Extractor]] build the full institutional knowledge graph, with node typing, confidence scoring, and stable `apkg:` identifiers. Their registries were last generated 2026-07-03 against a different machine's vault path and total 1.9 MB.

This tool builds a **lean operational subset** — regenerated on every render, sized to inline into a page — for interface use. It does not replace them. Where the registries are the archival graph, this index is the working one.

## Verification

| Check | Result |
|---|---|
| `test_alpha_app.py` | 40 passed |
| `test_founder_os.py` | 45 passed, unchanged |
| Headless Chromium, 330–1280 px | renders; 0 JS errors; no horizontal overflow; 19 interactive assertions passed |

## Related Documents

- [[Alpha Proxima App Architecture v1]] — the contracts and the reasoning
- [[Alpha Proxima App README]] — how to run it
- [[Tool 012 - Founder OS State Engine]] — the state this app reads
- [[Tool 001 - Vault Validator]] — the shared parsing foundation
- [[Alpha Proxima Engineering Toolkit]] — the toolkit index

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-01 | CLAUDE | First registration: two-half composition, vault index, coherence ratchet, loopback contract |
