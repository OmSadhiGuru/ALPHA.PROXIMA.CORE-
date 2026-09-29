---
title: "Supabase Operational Gateway — Activation Runbook"
aliases: ["Live Integration Supabase Runbook", "Alpha Realtime Activation"]
tags: [operations, live-integration, supabase, infrastructure, runbook, alpha-proxima]
created: 2026-09-29
updated: 2026-09-29
status: draft
version: "1.0.0"
authors: ["Claude — Chief Knowledge Architect"]
artifact_type: operational-runbook
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "Claude"
dependencies: ["[[Alpha Proxima Live Integration Layer]]", "[[07 - Automation Standard]]", "[[12 - Continuous Integration Standard]]"]
related_documents: ["[[Alpha Proxima Live Integration Layer]]", "[[Alpha Proxima App Architecture v1]]"]
related_research_programs: []
---

# Supabase Operational Gateway — Activation Runbook

## Purpose

State exactly what is built, what is not, and what a human must decide before
the Live Integration Layer carries real traffic. Vendor configuration belongs
here rather than in the architecture note, so that replacing Supabase is a
change to one runbook and not an amendment to institutional doctrine.

## Mission

Keep the gap between "the schema exists" and "the integration is live" visible,
named, and owned — so nobody reading the Foundation's own documents mistakes a
migration file for a running system.

## Definitions

**Applied** — executed against a database that serves real traffic. Nothing in
this directory is applied.

**Verified** — a delivery from the real external system arrived, was
authenticated, and was normalized. No adapter is verified.

**Rehearsal** — a committed fixture replayed locally. Rehearsals prove the
adapter; they say nothing about the connection, and the registry refuses to let
one promote an adapter's status.

## Context

The Founder's Supabase account holds one project, `OmSadhiGuru's Project`
(region `ca-central-1`), and it is **paused**. Resuming a paused project and
applying a schema to it are outward-facing acts with billing consequences, so
they sit outside what implementation work may do on its own authority (§26 of
the implementation directive; `07 - Automation Standard`, Approval Boundary).

The migrations were therefore written, applied, and verified against a
**local PostgreSQL 16 instance** created for that purpose and destroyed
afterwards. That is a real test of the schema and not a test of the Foundation's
hosted infrastructure, and the distinction is the whole point of this document.

## Architecture

```
migrations/
  0001_alpha_event_ledger.sql            append-only events, activities view
  0002_presence_notifications_devices.sql presence, notifications, devices,
                                          subscriptions, adapter registry,
                                          badge function, dead letters
  0003_row_level_security.sql             deny by default, then each exception
```

Three files rather than one, split on mutability: everything in `0001` is
append-only and everything in `0002` changes. A reader can tell at a glance
which tables a bug can corrupt.

## Dependencies

| Needs | Why | Who supplies it |
|---|---|---|
| A resumed Supabase project | The project is paused; a paused project accepts no connections | Founder (billing) |
| `GITHUB_WEBHOOK_SECRET` | Signature verification at ingress; an unverified body is an anonymous stranger claiming a commit | Founder (GitHub repo settings) |
| A deployed webhook endpoint | GitHub needs somewhere authenticated to POST | Engineering, after the secret exists |
| `SUPABASE_SERVICE_ROLE_KEY` | Server-side ingress writes | Founder (project settings) |
| An authenticated Founder session | `FD-002`: authentication before reachability | Founder (Supabase Auth) |
| A push credential (APNs or equivalent) | Delivery of `action` and `critical` notifications | Founder (Apple Developer account) |

None of these exist in this repository, and none should: a credential committed
to a vault is a credential published.

## Examples

Verify the schema the way it was verified here — against a throwaway local
database, never against the Foundation's project:

```bash
# A local cluster on a short socket path (Postgres rejects long ones).
initdb -D /tmp/apdb/data -U ap --auth=trust
pg_ctl -D /tmp/apdb/data -o '-k /tmp/apdb/sock -p 55432 -c listen_addresses=' start

# Supabase's roles are not present in a bare Postgres; the migrations reference them.
psql -h /tmp/apdb/sock -p 55432 -U ap -d postgres \
  -c "create role anon nologin; create role authenticated nologin; create role service_role nologin;" \
  -c "create extension if not exists pgcrypto;"

for f in migrations/000*.sql; do
  psql -h /tmp/apdb/sock -p 55432 -U ap -d postgres -v ON_ERROR_STOP=1 -f "$f"
done
```

Check the same contract without a database at all — this is what CI runs:

```bash
python3 "08_SYSTEMS/Engineering Toolkit/test_live_infrastructure.py"
```

## Activation sequence

Each step is gated on the one before it. The order exists so that nothing is
reachable before it is authenticated.

1. **Founder decision** — resume the Supabase project, or choose a different
   operational backend. Until this happens every step below is blocked, and the
   local JSONL ledger remains the whole layer.
2. Apply `0001`, `0002`, `0003` in order, to a non-production branch first.
3. Create the Founder's authenticated identity. Confirm `anon` can read
   nothing — the migrations revoke it, and a manual check costs one query.
4. Deploy the webhook endpoint. Verify the signature check rejects an unsigned
   body **before** pointing GitHub at it.
5. Register the GitHub webhook. The first real delivery is what moves
   `ADP-GITHUB` from `disconnected` to `connected`, and nothing else can.
6. Confirm `alpha.integrations` reports exactly one connected adapter and
   eleven that honestly are not.
7. Push notifications last. They need a credential the Foundation does not yet
   hold, and the badge is useful without them.

## Future Improvements

- Realtime Broadcast and Presence, once a hosted ledger exists to broadcast from.
- An Edge Function for webhook ingress, so the signature check runs before any
  row is written rather than after.
- A reconciliation job comparing the local JSONL ledger to the hosted one by
  `dedup_key`, which would make a transport outage recoverable rather than lossy.

## Open Questions

- **Does the Foundation want a hosted operational store at all?** The local
  ledger already satisfies everything except push-when-the-app-is-closed. That
  one capability is the entire argument for this directory, and it deserves to
  be argued rather than assumed.
- **Who may resume a paused project?** No decision record covers routine
  infrastructure spend.
- **Should the hosted ledger be authoritative or a mirror?** A mirror is safer
  and costs a reconciliation job. Making it authoritative is faster and puts
  operating history behind a vendor.

## Related Documents

- [[Alpha Proxima Live Integration Layer]] — the architecture this configures
- [[Alpha Proxima App Architecture v1]] — the read models this extends
- [[07 - Automation Standard]] — the approval boundary this respects
- [[12 - Continuous Integration Standard]] — the zero-dependency gate

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-29 | First runbook. Migrations written and verified locally; nothing applied to a hosted project. |
