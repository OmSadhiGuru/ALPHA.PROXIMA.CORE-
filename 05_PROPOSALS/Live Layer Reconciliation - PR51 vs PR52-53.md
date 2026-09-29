---
title: "Live Layer Reconciliation - PR51 vs PR52-53"
aliases: ["Live Layer Reconciliation", "PR51 vs PR52", "Duplicate Live Layer"]
tags: [proposals, live, events, adapters, reconciliation, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: proposed
version: "1.0.0"
authors: ["CLAUDE"]
artifact_type: proposal
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Architecture"
reasoning_engine: "Claude"
dependencies: ["[[Alpha Proxima App Architecture v1]]"]
related_documents: ["[[ADR-0002 - Reconciling the Four Institutional Taxonomies]]", "[[Alpha Proxima Engineering Toolkit]]", "[[12 - Continuous Integration Standard]]"]
related_research_programs: []
---

# Live Layer Reconciliation — PR #51 vs PR #52/#53

## Purpose

Two complete, independently built implementations of the Foundation's live event layer are open at once. This document measures them against each other so the Founder can decide which becomes canonical, and records the measurement so the decision is never re-litigated from memory.

## Mission

End with **one** event contract. Lose none of the work that earned its place in either.

---

## Definitions

| Term | Meaning here |
|---|---|
| **The stack** | PR #50 → #52 → #53. Phases A, B, C of the Realignment Directive. |
| **The layer** | PR #51, "Live Integration Layer". Phases B, D, partial E, partial G in one PR. |
| **Forward reference** | A document named in backticks rather than wiki-links because it exists only on an unmerged branch. It becomes a link when that branch lands. |
| **Typed actor** | An `actor_id` matching `^(agent\|office\|organization\|person):[a-z0-9-]+$`, resolved against ratified registries. |
| **Observed status** | An integration's health derived from recorded deliveries, never declared by a human or a config file. |

---

## Context

PR #51 was opened at **06:46Z**. PR #52 was opened at **10:30Z**, roughly four hours later, by a different session that did not check for open work first. That omission is the cause of this document; it is recorded here rather than elsewhere because the remedy is procedural and belongs with the evidence.

Both are draft, both are **4/4 green**, both hold coherence at **123/123**.

---

## Architecture

### The duplication is invisible to git

| Pair | Conflicting files |
|---|---|
| #50 ↔ #51 | 1 — the Toolkit index table |
| #52 ↔ #51 | 2 — `.gitignore`, the Toolkit index |
| #53 ↔ #51 | 3 — the above plus `alpha_app.py` |

**No Python file conflicts between #52 and #51.** The modules are named differently — `alpha_event.py` / `event_ledger.py` / `event_adapters.py` against `alpha_events.py` / `alpha_live.py` / `alpha_adapters.py` — so git would merge both without a murmur and leave the Foundation holding two complete event contracts for the same facts.

This is the dangerous case. A conflict is a warning; silent duplication is not.

### Verified independently, not taken from either description

| Measure | The stack (#50/#52/#53) | The layer (#51) |
|---|---|---|
| Tests | 274 across 10 suites | **467 across 14 suites** |
| CI | 4/4 green | 4/4 green |
| Coherence | 123/123 | 123/123 |
| Dependencies added | none | none |

Both test counts were run locally, not read from the pull request bodies.

### Where the layer (#51) is stronger

| Property | #51 | The stack |
|---|---|---|
| **Secret scanning** | `secret_leaks()` walks metadata recursively and rejects credential-shaped keys | *absent* |
| **Bounded payloads** | `MAX_METADATA_BYTES` 8192, title 200, summary 1000 | *unbounded* |
| **Dedup honesty** | Key is prefixed `p:` (provider id) or `d:` (derived fallback), so the operator sees which guarantee applied | falls back silently |
| **Causation** | `correlation_id`, `causation_id`, entity history | *absent* |
| **Deep links** | Validated `alpha-proxima://` scheme with roots | free string |
| **Integration status** | **Observed** — only a recorded delivery can reach `connected`; replayed fixtures cannot promote | **Declared** with required evidence — weaker: a human still asserts it |
| **Staleness** | A success older than 24h reads `degraded`, because a quiet webhook and a broken one look identical | *absent* |
| **Notifications** | Full lifecycle — queued/delivered/failed/read/dismissed, devices, subscriptions, retry cap | badge only |
| **Ingress** | HMAC verification, rate limiting, replay guard, dead letters, TLS gate | *absent* |
| **GitHub adapter** | implemented and fixture-tested | declared `planned` |
| **Supabase** | 593 lines of migrations + RLS, applied to throwaway Postgres | *absent* |

The observed-status design deserves particular note. `Live Core Architecture v1` states the rule *never claim `connected` without verification* and enforces it by demanding evidence alongside a declared status. #51 removes the declaration entirely: status is a function of delivery history. **That is the same principle implemented one level deeper**, and it is the better implementation.

Likewise, #51's dedup key marks whether the strong or weak guarantee applied. The stack preaches *absence is not silence* in its backbone and then falls back silently in its own idempotency. #51 does not.

### Where the stack is stronger

| Property | The stack | #51 |
|---|---|---|
| **Actor identity** | `actor_id` typed and resolved against the ratified registries — `agent:cf-07` | `actor` is any non-empty string |
| **Phase C** | `/api/v1/system-backbone` extended to **1.1.0** with `activity`, `presence`, `integration_health`, `notification_summary`; backward compatibility test-enforced | backbone left at 1.0.0; live routes added **beside** it |
| **Register reconciliation** | Founder OS integrations reconciled against the adapter registry; drift reported, neither overwritten | *absent* |

Only the first is hard to retrofit. Free-text actors reintroduce at the event layer exactly the defect PR #50 closed in the graph: a name no registry resolves, unnavigable from the Council. It propagates through every event, projection and stored row, so it is cheapest to fix before volume exists.

PR #51 predates #50 and could not have used the entity model.

### The two directions, measured

| Direction | What must be ported | Volume |
|---|---|---|
| **A** — keep the stack, port #51 onto it | GitHub adapter, ingress, notification lifecycle, Supabase schema, secret scanning, bounds, causation, deep links, observed status | **~3,384 lines Python + 593 SQL** |
| **B** — keep #51, port the stack onto it | `entity_registry.py` (merges near-cleanly — one Markdown table conflict), type the `actor` field, extend the backbone to 1.1.0 | **~401 lines + two bounded changes** |

Direction A is roughly an order of magnitude more work and would discard the better implementation of the Foundation's own stated principle.

---

## Recommendation

**Direction B.**

1. **Merge #50 first.** The entity model is independent of both live layers and valuable regardless. Its only conflict with #51 is one row in a Markdown table.
2. **Merge #51** as the canonical live layer.
3. **Close #52 without merging.** Its contract is superseded. Nothing in it is lost that #51 does not do as well or better, except the typed actor — which step 4 carries forward.
4. **Open one focused PR** that (a) types `actor` against `entity_registry`, and (b) extends `/api/v1/system-backbone` to 1.1.0 over `alpha_live` rather than `event_ledger`. This is #53's contribution, rebased onto the surviving contract.

This leaves the Foundation with one contract, the stronger implementation, the typed identity, and the Phase C extension the Directive asked for.

### What this costs

PR #52 — three modules, 953 lines, 51 tests — is discarded. That is the correct outcome of building without looking first, and the cost should be recorded rather than softened by merging both.

---

## Dependencies

- `Institutional Node Taxonomy v1` (proposed, PR #50) — the entity model step 4 resolves against
- `Live Core Architecture v1` (proposed, PR #52) — superseded by #51's contract if Direction B is taken; its *principles* survive, its code does not
- [[Alpha Proxima App Architecture v1]] — §7.2.1 must be rewritten against `alpha_live`

---

## Related Documents

- [[ADR-0002 - Reconciling the Four Institutional Taxonomies]] — the Foundation's precedent for choosing one model over several honest ones
- [[Alpha Proxima Engineering Toolkit]] — the tool inventory both PRs edit, and the file they conflict in
- [[12 - Continuous Integration Standard]] — *check the instrument before raising the tolerance*; the sibling rule this episode suggests

---

## Examples

```bash
# Reproduce every measurement in this document:
git merge-tree --write-tree fix/truth-kernel-entity-resolution <pr51-head>   # 1 conflict
git merge-tree --write-tree feat/live-event-core              <pr51-head>   # 2, no Python
git merge-tree --write-tree feat/system-backbone-live         <pr51-head>   # 3

git worktree add /tmp/wt51 <pr51-head>
cd /tmp/wt51 && python3 -m unittest discover -s "08_SYSTEMS/Engineering Toolkit" -p "test_*.py"
# Ran 467 tests — OK
```

---

## Future Improvements

1. **A standing rule: read the open pull requests before building a phase.** This episode cost 953 lines. The remedy is one command, and it belongs in the Engineering Handbook beside the CI rules.
2. **Port the stack's register reconciliation** (`integration_health`) onto #51's observed status. Observed health and Founder-registered intent are still two registers, and they will still drift.
3. **Revisit presence TTL.** The stack uses 90s, #51 uses 180s. Neither number has been justified against how long an agent actually thinks.

---

## Open Questions

- Does the Founder want #52 closed, or kept open as a record of the alternative contract?
- `github.deployment.failed` is `critical` in #51, which bypasses stated preferences. That power should be granted deliberately — it is a Founder decision, not an adapter's.
- Should the surviving live layer's documents move under `08_SYSTEMS/` beside `Live Core Architecture v1`, or stay at `13_OPERATIONS/Live Integration Layer/`?

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-09-29 | CLAUDE | Line-level reconciliation of the two live-layer implementations; recommends Direction B |
