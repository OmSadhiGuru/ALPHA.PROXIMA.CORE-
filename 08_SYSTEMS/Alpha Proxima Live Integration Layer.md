---
title: "Alpha Proxima Live Integration Layer"
aliases: ["Live Integration Layer", "AlphaEvent Architecture", "Alpha Event Bus"]
tags: [systems, architecture, live-integration, events, adapters, notifications, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: draft
version: "1.0.0"
authors: ["Claude — Chief Knowledge Architect"]
artifact_type: architecture-specification
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "Claude"
dependencies: ["[[Alpha Proxima App Architecture v1]]", "[[07 - Automation Standard]]", "[[12 - Continuous Integration Standard]]", "[[Foundational Architecture]]"]
related_documents: ["[[Alpha Proxima App Architecture v1]]", "[[LUMIAION Architecture Spec v0.1]]", "[[Supabase Operational Gateway — Activation Runbook]]", "[[Galaxy Prototype Concept]]", "[[Alpha Proxima Engineering Toolkit]]"]
related_research_programs: []
---

# Alpha Proxima Live Integration Layer

## Purpose

Let the Foundation observe itself without letting anything outside it change
what the Foundation knows.

Before this layer, Alpha Proxima could describe its institutions in detail and
could not notice that one of them had just done something. Nothing external had
a way to report an occurrence except by a human writing it down. This layer is
that missing sense — and it is built so that acquiring a sense did not cost the
Foundation its single writer, its canonical Markdown, or its ability to tell a
fact from a guess.

## Mission

Carry observations from external systems to the Founder's attention, with
provenance preserved at every step, and with no path by which a provider payload
can become institutional truth.

## Definitions

**AlphaEvent** — one normalized observation. Provider-independent, validated,
immutable once stored.

**Adapter** — the one component allowed to know a provider's vocabulary. It
translates and rejects; it cannot act.

**Projection** — a derived read model (activity, presence, notifications,
badge). Disposable by design.

**Canonical truth** — the Markdown vault, and `founder-state.json` behind its
single writer. Nothing in this layer is canonical truth.

**Verified** — an external system's delivery arrived and was authenticated. The
only thing that may move an adapter to `connected`.

**Rehearsal** — a committed fixture replayed locally. Proves the adapter, proves
nothing about the connection.

## Context

Three existing invariants shaped every decision here, and each one ruled out an
otherwise obvious design.

**Canon is Markdown.** So the event ledger could not become a second place the
Foundation's truth lives. It is a transport record: delete it and the Foundation
loses its recent activity feed and its unread markers, and loses no knowledge.
Every field in it had to pass that test.

**Founder state has one writer.** So adapters could not be allowed to interpret
what they observe. An adapter publishes an event; deciding what an event *means*
for a priority or a blocker is a later, separate, approved step. This is enforced
structurally — `alpha_adapters.py` and `alpha_live.py` cannot import the state
engine, and a test reads their parse trees to prove it rather than trusting the
comment that says so.

**The Engineering Toolkit installs nothing.** So the live layer is Python
standard library throughout, and the vendor-specific parts are SQL and
documentation in an isolated boundary that the CI dependency gate never sees.

## Architecture

```
EXTERNAL SYSTEM
      │  provider payload, untrusted
      ▼
  ADAPTER  ──── rejects what it cannot understand
      │  AlphaEvent v1, validated
      ▼
 EVENT LEDGER ──── append-only, deduplicated
      │
      ├──► ACTIVITY      derived, disposable
      ├──► PRESENCE      ephemeral, expires
      ├──► NOTIFICATION  derived, mutable lifecycle
      └──► BADGE         one number: unread obligations
                │
                ▼
      READ MODELS (/api/v1/...)
                │
                ▼
      COUNCIL · MEMORY · DASHBOARD · PUSH
```

There is no arrow from an external system to an interface, and no arrow from
this layer back into canon. Both absences are load-bearing.

### The event contract

`AlphaEvent v1` (`08_SYSTEMS/Engineering Toolkit/alpha_events.py`) is one shape
for every observation the Foundation will ever receive. Validation reports every
fault rather than the first, so an adapter author fixes one payload mapping in
one pass. Unknown fields are refused by name, with the reason: provider-specific
data belongs in `metadata`, which is bounded — adapters summarize, they do not
mirror.

Four decisions in the contract are worth stating because each one is a refusal:

- **An unknown provider is rejected, not stored.** An unfamiliar `source` means
  an adapter nobody reviewed.
- **A credential-shaped key anywhere in `metadata` fails validation.** The most
  likely way a token reaches an interface is an adapter copying a provider
  payload wholesale, so the check is at the boundary rather than in a redaction
  step later.
- **`UNATTRIBUTED` exists** so an event whose department cannot be established
  says so instead of guessing.
- **An event with no stated cause is its own correlation root.** A single-step
  observation is a one-event workflow, not a null one.

### Severity is the notification policy

One ordered field decides everything about interruption:

| Severity | Channels | Meaning |
|---|---|---|
| `info` | feed | It happened. Routine indexing, a passing check, a commit. |
| `update` | feed + badge | Forward progress worth noticing. |
| `action` | feed + badge + push | The Founder personally owes something. |
| `critical` | feed + badge + push, bypassing preferences | Something is broken now. |

Only two of four may interrupt, and the asymmetry is the design: a system that
pushes everything is a system whose pushes get ignored. `requires_founder` can
only ever *raise* an event to at least `action`; nothing can lower an event
below the severity its adapter declared.

### Deduplication

Providers retry webhooks. The same push arrives three times. The key is
`source + provider_event_id + event_type`, because that triple is what the
provider itself considers one thing happening once. Where a provider supplies no
identifier, the key falls back to semantic content and is *marked* as the weaker
guarantee (`d:` rather than `p:`), so an operator can see which promise applied.

### Honest integration status

An adapter's status is **observed, never declared**. The rules, each a refusal to
overstate:

- A `planned` or `blocked` declaration is never overridden by telemetry.
- No success ever recorded means `disconnected`, whatever the errors say —
  `degraded` means it worked and then stopped.
- A success followed by a failure means `degraded`.
- A success older than 24 hours means `degraded`: silence from a webhook is
  indistinguishable from a broken webhook, and the interface must not present
  the two the same way.
- Only a recent, uncontradicted, **verified** success means `connected`.

A replayed fixture is recorded as a rehearsal and cannot promote anything. A test
replays every committed fixture and asserts that no adapter's status moves — so
a developer can exercise the whole layer locally without the integration screen
becoming a fiction.

`planned` and `blocked` are kept distinct on purpose. `planned` means nobody has
built it. `blocked` means a decision must come first: the semantic memory adapter
waits on an unfilled Chief Memory Architect appointment, which is the Founder's
to make, not an engineering task.

### Presence expires

Presence is the field most able to lie. A `CODING` badge from a process that died
twenty minutes ago is a false statement about the present, and it is the kind of
falsehood a viewer has no way to detect. So expiry is applied in the read model,
not left to each client: a record past its TTL reads as `offline`, with
`reported_state` kept for a "last seen coding, 14 minutes ago" line and the
activity string blanked so it cannot read as current.

### The badge counts obligations

Not activity. Twenty `info` events are a busy hour and zero obligations, and the
badge stays at zero — `info` produces no notification at all. Reading or
dismissing lowers it; *delivery* does not, because delivery is not reading; and a
**failed** push still counts, because the obligation did not stop existing when
the push failed.

### Degraded mode

Three honest states, never collapsed into one green dot: `unconfigured` (no
transport exists — the Foundation's actual state today), `stale` (configured and
silent past the window), `live`. In all three, `canonical_readable` is reported
true, because the vault does not depend on this layer. `presence_trustworthy` is
true only when the transport is live.

## Dependencies

| Component | Depends on | Nature |
|---|---|---|
| `alpha_events.py` | Python standard library | none |
| `alpha_adapters.py` | `alpha_events`, `state_io` | writes one health file |
| `alpha_live.py` | `alpha_events`, `alpha_adapters`, `state_io` | writes one projection file |
| `/api/v1/*` live routes | all three, loaded lazily | degrades to canon if absent |
| Supabase migrations | a resumed project and credentials | **not applied** |
| Push delivery | an APNs-equivalent credential | **does not exist** |

The live layer is loaded lazily by `alpha_app.py` precisely so `render`, `show`
and `check` keep working — and keep passing CI — on a machine where no ledger has
ever existed.

## Security

The layer treats every external payload as hostile and every credential as
something it must not hold.

- **Webhook signatures** are verified in constant time before a payload is read.
  An unverified body is an anonymous stranger claiming a commit happened.
- **No mutation endpoint exists.** Every live route is a `GET`. No interface can
  write Founder state through this server because there is nothing to write to.
- **Device tokens are hashed on arrival** and the plaintext is never retained.
  The read model omits even the fingerprint. What is never written cannot leak.
- **`FD-002` holds:** a non-loopback bind is refused without a token, checked
  before the socket opens rather than after the first request.
- **Row level security denies by default**, with `force` on the tables holding
  history so the owner is bound by its own policies. The one mutation an
  authenticated session may perform is moving a notification to `read` or
  `dismissed`, narrowed at both ends so a dismissed notification cannot be
  resurrected to inflate a badge.
- **Nothing anonymous holds any privilege**, including in future migrations —
  default privileges revoke rather than grant.
- **Dead letters store no headers.** A rejected webhook's headers carry its
  signature, and a debugging table is not a place to accumulate those.

## Failure modes and recovery

| Failure | Behaviour | Recovery |
|---|---|---|
| A torn final write in the ledger | That line is skipped; all earlier history reads normally | `ap.py events repair`, which reports exactly what it dropped and is never automatic |
| A corrupt health or projection file | Reads as empty; the layer degrades rather than refusing to start | Rebuild projections from the ledger |
| A provider retries a delivery | Stored once; the retry is reported, not raised | None needed |
| A payload the adapter cannot parse | Rejected at the boundary, counted as a failure, nothing stored | Fix the adapter; the dead-letter row says what arrived |
| Realtime transport down | `unconfigured`/`stale` is displayed; canon stays readable | Reconnect; resynchronize by `dedup_key` |
| The whole live state deleted | Activity feed and unread markers are lost | Nothing institutional to recover — this is the design |

## Examples

```bash
# What is broken, without reading a server log.
ap.py live status

# Replay a committed fixture. Stores events; cannot make anything look connected.
ap.py adapters ingest "13_OPERATIONS/Live Integration Layer/fixtures/github/push.json"

# Run the notification policy over what is stored.
ap.py live project

# One entity's whole life — the temporal half of Memory.
ap.py live history PR-48

# The contract itself, for an adapter author.
ap.py events contract
```

## Future Improvements

- **Runtime presence for the Council.** Today CODEX and Claude are observable
  through their commits, which is activity without presence. A runtime signal
  channel is what turns the Council from a list into a room.
- **Causal and temporal edges in Memory.** The galaxy's edge taxonomy already
  reserves both types and the view builder deliberately emits neither, because
  only the event ledger may create them. Joining the ledger to the spatial view
  is the next real step toward navigable institutional memory.
- **Delivery.** Queue, retry and badge synchronization are modelled and tested;
  the send is absent because the credential is.
- **Reconciliation** between the local ledger and a hosted one, which would make
  a transport outage recoverable rather than merely survivable.

## Open Questions

- **Should `github.deployment.failed` really be `critical`?** It is the one
  GitHub event that can leave the Foundation's hosted surface down, which is the
  argument for it. But `critical` bypasses the Founder's stated preferences, and
  that power should be granted deliberately rather than inherited from an
  adapter's judgement.
- **Does the Foundation want a hosted operational store at all?** The local
  ledger satisfies everything except push-while-closed. That single capability
  is the entire argument for the Supabase boundary.
- **Who may resume a paused vendor project?** No decision record covers routine
  infrastructure spend, and the whole realtime phase is blocked behind it.
- **How should a `blocked` adapter surface in the Council view?** An unfilled
  role is an institutional fact, not an error, and showing it as a red light
  would misrepresent a vacancy as a fault.

## Related Documents

- [[Alpha Proxima App Architecture v1]] — the read models and API this extends
- [[LUMIAION Architecture Spec v0.1]] — the interpretation layer above these events
- [[Supabase Operational Gateway — Activation Runbook]] — vendor configuration, kept out of doctrine
- [[Galaxy Prototype Concept]] — the spatial view consuming this layer
- [[Alpha Proxima Engineering Toolkit]] — where these modules live
- [[07 - Automation Standard]] — the approval boundary this respects
- [[12 - Continuous Integration Standard]] — the zero-dependency gate

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-29 | First specification. AlphaEvent v1, adapter boundary, projections, GitHub normalization, edge taxonomy. Supabase migrations verified locally, applied nowhere. |
