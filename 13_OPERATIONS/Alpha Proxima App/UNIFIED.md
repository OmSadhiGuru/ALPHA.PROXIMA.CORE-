---
title: "Alpha Proxima Unified Interface"
aliases: ["Unified Interface"]
tags: [operations, app, interface, founder-os]
created: 2026-09-24
updated: 2026-09-29
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: implementation-guide
institutional_owner: "Engineering Office"
dependencies: ["[[Alpha Proxima App Architecture v1]]"]
related_documents: ["[[Founder OS Architecture v1]]"]
related_research_programs: []
---

# One Vault, one interface

The unified service uses an explicit `--root` for **all** notes and Founder/Council state.
Code and built assets can live in a separate deployment; they are not a data source.

Run `python3 -B "08_SYSTEMS/Engineering Toolkit/unified_app.py" --root /path/to/vault`.
Open `http://127.0.0.1:8788/`. The Universe, Memory, capture, project tracking and
Council share this origin. `#know` remains an alias for Memory. `/galaxy` opens the
Council in the shared shell. `/classic` retains the detailed read-only interface.

An optional `--remote-config /path/to/config.json` reuses an existing private
`host`, `port` and `token`. Every remote resource requires authentication.
The existing URL token is exchanged for an HttpOnly, SameSite session cookie.
No secrets belong in this repository. `--redirect-port 5173` redirects the former
standalone development entry to the shared app. All listeners share one Memory
instance and one authoring lock.

## Authoring and tracking

- Explicit submission creates `14_FUTURE/Founder Ideas/Capture-<request-id>.md`.
- Captures are `intake` records. They do not ratify decisions, alter Council
  authority, run agents, or mutate Founder/Council JSON state.
- Notes, ideas, tasks and projects share this authoring endpoint. Task/project
  checkboxes are Markdown checkboxes in the same document.
- Only captured tasks/projects can be updated here. Existing institutional
  documents remain read-only. A submitted content hash rejects stale edits.
- Atomic create-without-replacement makes retries idempotent. Project publication
  is atomic; it checks the current bytes again before replacement. Obsidian is an
  external writer and does not participate in this process's lock, so this is not
  a general multi-writer transaction protocol.

## Loading and availability

The HTML shell does not wait for indexing. The memory snapshot is derived in the
background and refreshed at most once per 20 seconds, without overlapping builds.
New captures are inserted immediately into the shared read index. Files that
macOS identifies as iCloud placeholders are listed as unavailable and are never
silently represented as fully indexed. Download those files on the host Mac to
make their contents available. `knowledge_complete` and `unavailable_notes` expose
this boundary. The live service still requires the Mac and private network to be
available; this is a responsive web app, not a native/offline iOS package.

## Build and verification

The `universe` folder preserves the existing auric-body Orbit → Surface → Inward
visualization, adapted to `/api/v1/app`. Build it with `npm run build`; deploy
`universe/dist/client` along with the Python service and templates. These build
outputs are ignored by Git. The capture/project shell is `app/unified.html`.

Run Toolkit unittest discovery, Truth Kernel tests, `npm run build` and
`npm run test:sites`. `test_unified_app.py` tests authoring, retries, stale updates,
path confinement and request authentication on disposable data. Rendered QA must
also exercise capture → read → track → reload → spatial lookup → source note, plus
the Council panel and narrow touch layouts. A build alone is not mobile QA.
