---
title: "Live Core Architecture v1"
aliases: ["Live Core", "AlphaEvent", "AlphaEvent v1", "Event Ledger", "Adapter Contract"]
tags: [systems, live, events, adapters, presence, notifications, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: active
version: "1.0.0"
authors: ["CLAUDE"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Architecture"
reasoning_engine: "Claude"
dependencies: ["[[Institutional Node Taxonomy v1]]", "[[Alpha Proxima App Architecture v1]]", "[[12 - Continuous Integration Standard]]"]
related_documents: ["[[Cognitive Function Registry]]", "[[Founder OS Architecture v1]]", "[[Knowledge Graph Architecture v1.0]]", "[[Office Registry]]"]
related_research_programs: []
---

# Live Core Architecture v1

## Purpose

Give the Foundation a single normal form for "something happened", so that institutional memory can acquire **time** without acquiring twelve provider vocabularies.

---

## Context

The Knowledge Graph describes structure: what exists, who owns it, what it references. It has no notion of *when*. Nothing in the Foundation can currently answer "what is CODEX doing right now" or "what happened to PR #50 between opening and merge" — not because the data is missing, but because there is no contract in which to express it.

Twelve integrations are intended. Without one normal form, provider vocabulary leaks into the Council, the Memory and the interface, and adding the twelfth means touching all three. The Foundation would acquire eleven good reasons never to add the twelfth.

---

## Architecture

```
provider payload
      │
      ▼
   adapter            ← the only place provider vocabulary exists
      │
      ▼
  validate            ← output is checked, never trusted
      │
      ▼
 normalize → AlphaEvent
      │
      ▼
  event ledger        ← append-only, durable
      │
      ├── activity        what has been happening
      ├── presence        what is happening now, and expires
      └── notifications   what reached the Founder, and what is unread
```

| Module | Owns |
|---|---|
| `alpha_event.py` | The contract: schema, validation, severity, idempotency |
| `event_adapters.py` | The provider membrane and the integration registry |
| `event_ledger.py` | Append-only storage and the three projections |

---

## The contract

### `actor_id` is an entity, never a name

An event produced by CODEX names `agent:cf-07`. This is enforced — a free-text actor is rejected. It is the join that makes an event navigable from the Council, and it is why [[Institutional Node Taxonomy v1]] had to exist first.

An event may have **no** actor: a CI run has no author. Absence is not the same as a bad value.

### Idempotency is structural

A webhook retried three times is one institutional fact. Identity derives from *what happened* — source, type, entity, and the provider's own delivery id where supplied — never from `received_at` or `event_id`, which differ per delivery.

The ledger enforces this itself rather than trusting upstream, because a retry is precisely the case where upstream is already not behaving as expected.

### Severity is a decision to interrupt someone

| Severity | Feed | Badge | Push | Immediate |
|---|:--:|:--:|:--:|:--:|
| `info` | ✓ | | | |
| `update` | ✓ | ✓ | | |
| `action` | ✓ | ✓ | ✓ | |
| `critical` | ✓ | ✓ | ✓ | ✓ |

`requires_founder` pushes at any severity. A `critical` event that claims *not* to require the Founder is rejected — that combination is almost always a silent mistake.

**The badge counts unread meaningful notifications, not event volume.** A hundred routine commits are a hundred feed items and zero badge. A badge that counts everything stops meaning anything and gets ignored — the same failure the coherence ceiling exists to avoid.

---

## The adapter membrane

**Never claim `connected` without verification.** A status is a claim about the world. An integration reporting `connected` while nothing is wired teaches the Founder to distrust every other status on the page. The registry *refuses* `connected` or `degraded` without evidence of a verified exchange, and refuses any non-`planned` status without an implementation.

| Status | Meaning |
|---|---|
| `connected` | Verified exchange, evidenced |
| `degraded` | Reachable but impaired; events may be missing |
| `disconnected` | Was connected, is not now |
| `planned` | Contract written, adapter not implemented |
| `blocked` | Prevented by a decision or a missing credential |

**All twelve integrations currently report `planned`. None has been verified.** GitHub becomes the first real adapter in Phase D.

**Adapters are pure.** `normalize()` takes a payload and returns events. It opens no socket, reads no credential, writes nothing. That is what makes the live layer testable with fixtures, offline, deterministically — and a test asserts no live-core module imports a network client.

---

## The ledger is append-only

An event happened. History is therefore not editable: if the interface finds it inconvenient, the interface changes, not the past.

Storage is **JSON Lines** — one event per line, newline-terminated, never rewritten. A format that appends by construction cannot be silently mutated by a careless writer, and stays readable with `tail` and `grep` long after this code is gone. A test asserts the module never opens the ledger for writing or truncation.

A corrupt line is **reported, never skipped**. A ledger that quietly drops what it cannot parse is worse than one that admits the gap.

The ledger is **operational state, not canon**. It lives at `13_OPERATIONS/Alpha Proxima App/live/event-ledger.jsonl`, is git-ignored, and the Markdown vault remains the Foundation's truth.

---

## Presence is not truth

Presence is a claim with an expiry. States: `offline`, `online`, `thinking`, `researching`, `coding`, `indexing`, `waiting`, `blocked`, `error`.

Every signal carries a TTL (default 90s), and the projection drops it at read time. **A crashed agent must never read as CODING forever** — an expired actor reports `offline` while retaining `claimed_state`, so a silent death is visible *as* a silent death rather than as work in progress.

Historical work lives in events. Current activity lives in presence. The two are never confused.

---

## Verification

| Check | Result |
|---|---|
| `test_live_core.py` | **51 passed** |
| End-to-end: append 3, retry same payload | 3 appended, then **0 appended / 3 duplicates** |
| Presence after TTL | `coding` → `offline`, `claimed_state` retained |
| Badge on 3 events (1 info, 1 update, 1 critical) | **2** — volume ignored |
| No network client in any live-core module | asserted |
| Ledger never opened for write/truncate | asserted |

Zero dependencies added. Standard library only.

---

## Boundaries

**The Core owns** schemas, validation, normalization, projections, read models and deterministic tests.

**External infrastructure owns** webhooks, network clients, Supabase, push providers, external authentication and provider SDKs.

This file is the contract that infrastructure must satisfy, not the place it runs.

---

## Future Improvements

1. **Phase C** — surface `activity`, `presence` and `notification_summary` through the existing `/api/v1/system-backbone` rather than a competing API.
2. **Phase D** — GitHub as the first real adapter, with the fifteen event types the directive names.
3. **Ledger compaction** for a multi-year ledger. Append-only does not mean unbounded; compaction must preserve history, not erase it.
4. **`EventNode`** in the Knowledge Graph, once events are produced at volume.

---

## Open Questions

- Should presence signals enter the same ledger as institutional events, or a separate ephemeral store? They currently share it, which keeps one contract but grows the ledger with data that expires in ninety seconds.
- Is 90 seconds the right default TTL for an agent that thinks for minutes at a time?
- Should `read_keys` (which notifications the Founder has seen) be Founder OS state, or operational state?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-29 | CLAUDE | AlphaEvent v1, adapter membrane with honest statuses, append-only ledger, activity/presence/notification projections |
