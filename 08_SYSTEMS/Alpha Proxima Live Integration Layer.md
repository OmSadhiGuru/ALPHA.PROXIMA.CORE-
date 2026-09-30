---
title: "Alpha Proxima Live Integration Layer"
aliases: ["Live Integration Layer", "AlphaEvent Architecture", "Alpha Event Bus"]
tags: [systems, architecture, live-integration, events, adapters, notifications, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: draft
version: "1.2.0"
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

### The one write path

`alpha_ingress.py` is the only component that accepts a `POST`, and it is a
separate process on a separate port started by a separate command, because a
write path should be something an operator starts on purpose rather than
something that arrives with a read model.

It checks in a fixed order, and the order is the design — each check is cheap
enough to run before the next, and each one rejects a class of request the
following check would otherwise have to trust:

1. **Path** — unknown endpoints are refused before anything is read.
2. **Size** — an oversized body is refused from its `Content-Length`, so a large
   POST cannot exhaust memory ahead of authentication.
3. **Rate** — a sliding window per provider, *before* the signature, because
   HMAC over a body is the expensive part and a flood must not be able to buy it.
4. **Signature** — constant-time, over the raw bytes, before any parse.
5. **Replay** — a delivery id already seen is acknowledged and dropped.
6. **Parse, then normalize** — only now is provider vocabulary read, and only by
   the adapter.

Four refusals are worth stating because each one is a way this component could
have been dangerous:

- **It refuses to start without a signing secret for every enabled provider.**
  An endpoint that accepted unsigned deliveries "until the secret is configured"
  would be an open relay that looked like an integration, and the Founder's
  screen would show a connected adapter fed by anyone who found the URL.
- **It refuses a non-loopback bind without being told it is behind TLS.** A
  signature protects a body's integrity, not its confidentiality.
- **It never echoes the payload.** A receiver that reflects what it was sent is
  an open relay for whatever the sender wanted logged. Responses carry counts.
- **An unauthenticated body is not even written to the dead letters.** Otherwise
  anyone who found the URL could fill the Foundation's disk.

An authentic delivery the adapter cannot report is answered `202`, not `400`:
the delivery *was* genuine, and telling GitHub it sent something bad would make
it retry a payload that will be rejected identically. The reason goes to the
dead letters instead.

This is also the only place `origin: webhook` is ever set, which is what lets a
delivery promote an adapter to `connected`.

### The memory graph

`alpha_memory.py` reads the ledger and produces the temporal half of Memory:
entities as nodes, and the ledger's own causation and chronology as edges. The
taxonomy it shares with the Council view lives in `alpha_edges.py`, which makes
the source asymmetry structural rather than conventional:

- `registry_edge` refuses `causal` and `temporal` outright. A registry witnesses
  structure; it cannot know that one thing caused another.
- `ledger_edge` refuses `semantic`. An event cannot make a document say something.

Four relationships come out, each witnessed rather than decided:

| Edge | Meaning |
|---|---|
| `causal` | B names A as its cause — drawn between the *entities* the two events touched, so the picture shows a push leading to a commit |
| `temporal` | two entities observed in order **inside one correlation group**; two unrelated things in sequence is a coincidence, not a relationship |
| `operational` | an actor acted on an entity |
| — | an entity's own chronology is a `timeline` **on the node**, not a self-loop: a line to itself cannot be walked |

Sequence defers to causation on the same pair, because causation is strictly
stronger and drawing both would double the visual weight of one fact. A workflow
that returns to an entity draws one edge, not two arrows pointing at each other.

#### The actor join, its three tiers, and why its residue is visible

Events name actors as providers know them — `codex-bot`, `CI`, `Founder`. The
Foundation knows ratified institutional identities. This is where a memory graph
would most easily start lying: matching `codex-bot` to `CODEX Engineering Lead`
because both contain "codex" would fabricate an institutional attribution from a
string coincidence, and the result would be indistinguishable from a real one.

So every match is exact, against two ratified sources, and the tier that
entitled it travels with it:

| Tier | Source | Claim | Weight |
|---|---|---|---|
| `seat` | Agent and Subagent Registry, exact registered name | the Council's own record of who it has | 1.0, witnessed |
| `identity` | Institutional Node Taxonomy names the actor outright | a ratified institutional actor | 1.0, witnessed |
| `engine` | the taxonomy cites the name only as an engine fulfilling a function | a citation, not an identity | 0.5, **interpreted** |

The third tier is the one that needed care. `CODEX` resolves to `CF-07` — but
only as a *secondary* alias, because the taxonomy cites CODEX as the engine
behind that function. Engines move between functions; labels do not. So "an actor
called CODEX did this" is not the claim "CF-07 did this". An engine-tier match
therefore resolves as an interpretation, and `alpha_edges` refuses a confident
interpretation outright — the guard holds this honest by construction rather than
by anyone remembering to. In the spatial view that edge draws dashed while a
ratified identity draws solid.

What still refuses to resolve is the point. Substrings (`Codex Engineering`,
`Engineering Lead`), placeholders (`Owner pending`, `TBD`, `Unappointed`) and
provider logins (`codex-bot`, `github-actions[bot]`, `OmSadhiGuru`) all decline,
each asserted by test. `CI` declines too: a CI runner is not an institutional
actor and should not be given one.

The residue is counted, listed with its event counts, and explained — and the
report says which registries it checked, so "unresolved" is never mistaken for
"unchecked". The spatial view says the same at the point a viewer would otherwise
assume a seat. The hand-written alias table remains **empty**, because the
taxonomy now supplies ratified names and a hand-written mapping would need a
reason; a stale alias raises rather than silently reading as unresolved.

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
| `alpha_ingress.py` | `alpha_events`, `alpha_adapters`, `alpha_live` | the only write path; refuses to start unsigned |
| `alpha_edges.py` | nothing | reads and writes nothing; pure taxonomy |
| `alpha_memory.py` | `alpha_edges`, `alpha_events`, `entity_registry` | derived and disposable; writes nothing |
| `entity_registry.py` | ratified Markdown registries | derives 42 typed actors; authors none |
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
| An unsigned or forged delivery | `401`, never parsed, never written anywhere | None needed; the attempt is not evidence about an adapter |
| A flood of deliveries | `429` per provider, before any HMAC work | None needed |
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

# The ledger as a navigable graph, and who the Council does not recognize.
ap.py memory report

# Travel outward from one node, along typed and attributed relationships.
ap.py memory path github:pull_request:PR-48

# The contract itself, for an adapter author.
ap.py events contract

# Why the door is shut today, in one honest sentence per reason.
ap.py ingress check

# Open it, once a secret exists. Loopback unless told it is behind TLS.
GITHUB_WEBHOOK_SECRET=... ap.py ingress serve
```

## Future Improvements

- **Runtime presence for the Council.** Today CODEX and Claude are observable
  through their commits, which is activity without presence. A runtime signal
  channel is what turns the Council from a list into a room.
- **Runtime presence reported under a ratified name.** The Institutional Node
  Taxonomy closed most of this gap: what remains unresolved is `codex-bot` and
  `CI`, and neither *should* resolve — a GitHub login and a CI runner are not
  institutional actors. The real remainder is narrower than it looked: an agent
  reporting its own work should announce itself as the identity acting, so an
  attribution lands at `seat` or `identity` rather than at `engine`, which is a
  citation. That is a runtime signal channel, not a matching heuristic.
- **Promoting an engine-tier attribution.** Today CODEX attributes to CF-07 only
  as the engine the taxonomy cites. Were CODEX a registered seat, or the taxonomy
  to name it directly, the same event would attribute at full confidence. Which
  of those the Foundation wants is a governance question, not an implementation
  one.
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

## Captures: Omi and Pocket AI

Two adapters cited a `ContextItem` contract as the reason they could not exist. `alpha_context.py` is that contract, and both are now implemented against it.

### The body never enters the ledger

A ContextItem carries **a reference and its shape** — when a capture happened, how long it was, which provider holds it, the provider's category, and a short title. It carries no transcript, no memory text, no content of any kind. Those stay with the provider.

The reason is measured, not assumed. A survey of the Founder's Omi account found that of **200 durable memories scanned, zero** were unmarked for sensitivity: the corpus is essentially all personal. The ledger is git-ignored, but git-ignored is a property of one checkout, not a guarantee about every machine that will ever hold one. A pipeline that moves personal content out of a provider and onto disk has made a privacy decision on the Founder's behalf; this contract declines to make it.

So the Foundation learns *that* a capture happened, when, and roughly about what. To read it, you open Omi. That is a smaller capability than a full sync, and the one that can be granted without a governance conversation. **The Founder chose it explicitly** over a vault inbox and over full synchronisation.

Two properties hold it in place, tested separately:

| Property | How |
|---|---|
| A content-bearing delivery yields a content-free event | the adapter reads only the fields it should; a fixture carrying a transcript is normalized and the transcript appears nowhere in the result |
| A ContextItem carrying content is refused | `body_leaks()` walks the item recursively and rejects any field named `text`, `body`, `transcript`, … — the mirror of `secret_leaks()`, which keeps credentials out; this keeps the Founder's own words out |

### Sensitivity is conservative, and silence is not permission

`sensitive` is the default. Only an explicit `false` from the provider lowers a capture to `standard`. Pocket AI states nothing about sensitivity, so everything it sends is sensitive.

### A capture is a proposal, never a record

Severity is always `info` and `requires_founder` always False. A device that records the Founder does not get to interrupt the Founder — and an adapter that could raise its own severity would eventually learn that marking everything urgent is how to be seen. Attention is earned by the Founder promoting a capture, never claimed by the device that made it.

`suggested_kind` maps the provider's category onto what a capture *might* become — task, idea, reference. It is addressed to a person. An unrecognised category proposes nothing rather than guessing.

### Neither claims a connection

Both normalize correctly against fixtures and both read **`disconnected`**. No webhook secret exists and no delivery has been observed.

The Omi adapter's `blocked_reason` records a distinction worth keeping: **a session-scoped Omi connector held by an operating agent is that agent's tooling, not a Foundation integration.** An agent that can read Omi has not thereby connected the Foundation to Omi, and the registry must not report otherwise.

---
## Version History

| Version | Date | Change |
|---|---|---|
| 1.2.0 | 2026-09-29 | Actor resolution consults the Institutional Node Taxonomy alongside the Council registry, in three tiers. An engine-tier match resolves as an interpretation, not an identity. Residue falls to the two actors that should not resolve. |
| 1.1.0 | 2026-09-29 | Added the memory graph: shared edge taxonomy, ledger-witnessed causal and temporal relationships, the exact actor join and its visible residue. |
| 1.0.0 | 2026-09-29 | First specification. AlphaEvent v1, adapter boundary, projections, GitHub normalization, signed webhook ingress, edge taxonomy. Supabase migrations verified locally, applied nowhere. |
