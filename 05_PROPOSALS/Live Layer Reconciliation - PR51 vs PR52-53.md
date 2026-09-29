---
title: "Live Layer Reconciliation - PR51 vs PR52-53"
aliases: ["Live Layer Reconciliation", "PR51 vs PR52", "Duplicate Live Layer"]
tags: [proposals, live, events, adapters, reconciliation, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: adopted
version: "2.0.0"
authors: ["CLAUDE"]
artifact_type: proposal
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Architecture"
reasoning_engine: "Claude"
dependencies: ["[[Alpha Proxima App Architecture v1]]", "[[Alpha Proxima Live Integration Layer]]"]
related_documents: ["[[ADR-0002 - Reconciling the Four Institutional Taxonomies]]", "[[Alpha Proxima Engineering Toolkit]]", "[[12 - Continuous Integration Standard]]"]
related_research_programs: []
---

# Live Layer Reconciliation — PR #51 vs PR #52/#53

> **Outcome, recorded 2026-09-29.** #51 merged to `main` at `7f648af` and is the Foundation's canonical live layer. #52 and #53 were merged into #50, which is therefore superseded and must not merge — against this `main` it would install two event contracts. Phase A returned alone as #55. **Direction B was adopted**, with one variation: #52 was collapsed into #50 rather than closed, so the closure is still outstanding.
>
> This document is kept as the decision record. Everything below is written in the present tense of the decision, not of today.

## Purpose

Two complete, independently built implementations of the Foundation's live event layer are open at once. This document measures them against each other so the Founder can decide which becomes canonical, and records the measurement so the decision is never re-litigated from memory.

## Mission

End with **one** event contract. Lose none of the work that earned its place in either.

---

## Definitions

| Term | Meaning here |
|---|---|
| **The stack** | PR #50 → #52. Phases A, B, C of the Realignment Directive. #53 was merged into #52 on 2026-09-29, so **#52 now carries Phases B and C together**; it is no longer a three-level stack. |
| **The layer** | PR #51, "Live Integration Layer". Phases B, D, partial E, partial G in one PR. |
| **Forward reference** | A document named in backticks rather than wiki-links because it exists only on an unmerged branch. It becomes a link when that branch lands. |
| **Typed actor** | An `actor_id` matching `^(agent\|office\|organization\|person):[a-z0-9-]+$`, resolved against ratified registries. |
| **Observed status** | An integration's health derived from recorded deliveries, never declared by a human or a config file. |

---

## Context

PR #51 was opened at **06:46Z**. PR #52 was opened at **10:30Z**, roughly four hours later, by a different session that did not check for open work first. That omission is the cause of this document; it is recorded here rather than elsewhere because the remedy is procedural and belongs with the evidence.

Both are draft, both are **4/4 green**, both hold coherence at **123/123**.

**#51 is still moving.** Every figure below was re-measured at `8bc543d` (15:2x), which is two commits past the head this document first measured (`f795b73`). Those commits added a device/subscription CLI and fixed an RLS defect — see *Evidence of active hardening*. Any figure quoted from this document should be re-measured before it is relied on.

---

## Architecture

### The duplication is invisible to git

| Pair | Conflicting files |
|---|---|
| #50 ↔ #51 | 1 — the Toolkit index table |
| #52 ↔ #51 | **3** — `.gitignore`, the Toolkit index, `alpha_app.py` |

Before #53 was merged into it, #52 conflicted in two files; absorbing Phase C brought `alpha_app.py` with it.

**Until #53 landed, no Python file conflicted between #52 and #51.** The modules are named differently — `alpha_event.py` / `event_ledger.py` / `event_adapters.py` against `alpha_events.py` / `alpha_live.py` / `alpha_adapters.py` — so git would merge both without a murmur and leave the Foundation holding two complete event contracts for the same facts.

This is the dangerous case. A conflict is a warning; silent duplication is not.

### Verified independently, not taken from either description

| Measure | The stack (#50/#52/#53) | The layer (#51) |
|---|---|---|
| Tests | **275 across 10 suites** (#50 + #52, Phases A–C) | **484 across 13 suites** |
| CI | 4/4 green | 4/4 green |
| Coherence | 123/123 | 123/123 |
| Dependencies added | none | none |

Both counts were run locally, not read from the pull request bodies. An earlier revision of this document recorded #51 as *467 across 14 suites*: the test count was correct for the head then measured, and the **suite count was simply miscounted** — that branch had 13 suites then as it does now.

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

### Evidence of active hardening

After this document was first written, a security review of #51 found a defect worth recording, because *how* it was found argues for the branch as much as the fix does.

The `founder_reads_*` RLS policies had **no matching `GRANT`**. PostgreSQL refuses on privilege grounds before consulting any policy, so every one of those tables answered *permission denied* and the activity feed was unreadable. Marking a notification read failed too: an `UPDATE` must read the rows it matches, and without `SELECT` the badge could never be cleared — the central interaction of the whole notification model.

It failed **closed**, which is why nothing leaked and why nothing caught it. Every earlier test had queried as the table owner. The fix re-verifies as *each principal* separately, and nine tests now hold it — including that every table with a read policy has a grant, and that the `anon` revoke is the last word on privileges, since a revoke placed before a grant is undone by it.

That is the same discipline that produced #51's observed-status design: assume the convenient reading is wrong, and test from the position of the party who will actually be refused.

### The two directions, measured

| Direction | What must be ported | Volume |
|---|---|---|
| **A** — keep the stack, port #51 onto it | GitHub adapter, ingress, notification lifecycle, Supabase schema, secret scanning, bounds, causation, deep links, observed status | **3,458 lines Python + 647 SQL** |
| **B** — keep #51, port the stack onto it | `entity_registry.py` (merges near-cleanly — one Markdown table conflict), type the `actor` field, extend the backbone to 1.1.0 | **~401 lines + two bounded changes** |

Direction A is roughly an order of magnitude more work and would discard the better implementation of the Foundation's own stated principle.

---

## Recommendation

**Direction B.** *(Adopted — see the outcome note at the top. Step status is marked against each item.)*

1. ~~**Merge #50 first.**~~ **Superseded in execution.** #51 merged first, and #50 had by then absorbed #52 and #53. The entity model returned on its own as **#55**, rebased onto the new `main` — one conflict, the Markdown table, exactly as predicted.
2. ✅ **Merge #51** as the canonical live layer. *Done, `7f648af`.*
3. ⏳ **Close #52 without merging.** Its event contract is superseded. Note that #52 now carries **Phase C as well as Phase B**, so closing it defers both — step 4 carries both forward.
4. ⏳ **Open one focused PR** that (a) types `actor` against `entity_registry`, and (b) extends `/api/v1/system-backbone` to 1.1.0 over `alpha_live` rather than `event_ledger`. This is Phase C's contribution, rebased onto the surviving contract.

This leaves the Foundation with one contract, the stronger implementation, the typed identity, and the Phase C extension the Directive asked for.

### What this costs

PR #52's event layer — three modules, 953 lines, 51 tests — is discarded. Phase C's backbone extension is **not** discarded; it is re-pointed at `alpha_live` in step 4. That is the correct outcome of building without looking first, and the cost should be recorded rather than softened by merging both.

---

## Dependencies

- `Institutional Node Taxonomy v1` (proposed, PR #50) — the entity model step 4 resolves against
- [[Alpha Proxima Live Integration Layer]] — superseded by #51's contract if Direction B is taken; its *principles* survive, its code does not
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
| 2.0.0 | 2026-09-29 | CLAUDE | Outcome recorded: #51 merged to main at `7f648af` and is canonical; Direction B adopted with one variation (#52 collapsed into #50 rather than closed); Phase A returned as #55. Status moves from proposed to adopted, and the reference to the superseded `Live Core Architecture v1` is re-pointed at the document that actually landed |
| 1.2.0 | 2026-09-29 | CLAUDE | #53 merged into #52: the stack is now two levels, #52 carries Phases B and C, and its conflict surface against #51 grows from 2 files to 3 as `alpha_app.py` comes with it; restate what closing #52 would and would not discard |
| 1.1.0 | 2026-09-29 | CLAUDE | Re-measure at #51 `8bc543d`: 484 tests / 13 suites, port volume 3,458 + 647; correct an earlier suite miscount; record the RLS finding as evidence of active hardening; note that #51 is still moving |
| 1.0.0 | 2026-09-29 | CLAUDE | Line-level reconciliation of the two live-layer implementations; recommends Direction B |
