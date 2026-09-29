-- Alpha Proxima Live Integration Layer — the operational event ledger.
--
-- WHAT THIS IS NOT
--
-- This schema holds no institutional truth. The Foundation's canon is Markdown
-- in the vault; its operating state is founder-state.json behind its single
-- writer. Everything below is transport: an honest record of what external
-- systems reported, and the projections an interface reads.
--
-- Drop this entire database and the Foundation loses its recent activity feed,
-- its unread markers, and its presence badges. It loses no knowledge. Every
-- table here had to pass that test to be included.
--
-- WHY IT MIRRORS THE LOCAL LEDGER EXACTLY
--
-- `alpha_events.py` is the contract; this is the same contract expressed in
-- Postgres. The column names, the enums, and the deduplication key are
-- deliberately identical, so an operator can move between the local JSONL
-- ledger and a hosted one without learning a second vocabulary — and so a
-- divergence between the two is a schema error rather than a silent semantic
-- drift.
--
-- STATUS
--
-- Not applied. See `README.md` in this directory for exactly what activation
-- requires and who must decide it.

begin;

create schema if not exists alpha;

comment on schema alpha is
  'Operational projection and event transport for Alpha Proxima. Not canonical truth.';

-- --------------------------------------------------------------------------
-- enums — the same closed vocabularies alpha_events.py validates against
-- --------------------------------------------------------------------------

-- Ordered deliberately: the notification policy reads this order to decide
-- feed / badge / push, so adding a value is a policy decision.
create type alpha.severity as enum ('info', 'update', 'action', 'critical');

create type alpha.event_source as enum (
  'github', 'chatgpt', 'codex', 'claude', 'gemini', 'perplexity', 'pocket_ai',
  'obsidian', 'google_drive', 'google_calendar', 'notion', 'n8n', 'alpha_proxima'
);

create type alpha.department as enum (
  'ENGINEERING', 'RESEARCH', 'EXECUTIVE', 'KNOWLEDGE', 'MEMORY',
  'OPERATIONS', 'FINANCE', 'HEALTH', 'UNATTRIBUTED'
);

-- `offline` is the default because an agent nobody has heard from is offline.
-- "idle" would claim knowledge of the agent that silence does not give.
create type alpha.presence_state as enum (
  'offline', 'online', 'thinking', 'researching', 'coding',
  'indexing', 'waiting', 'blocked', 'error'
);

create type alpha.notification_state as enum (
  'queued', 'delivered', 'failed', 'read', 'dismissed'
);

create type alpha.adapter_status as enum (
  'connected', 'degraded', 'disconnected', 'planned', 'blocked'
);

-- --------------------------------------------------------------------------
-- events — append-only
-- --------------------------------------------------------------------------

create table alpha.events (
  event_id         uuid primary key default gen_random_uuid(),
  schema_version   text        not null default '1.0',
  occurred_at      timestamptz not null,
  received_at      timestamptz not null default now(),
  source           alpha.event_source not null,
  actor            text        not null check (length(btrim(actor)) > 0),
  department       alpha.department   not null,
  event_type       text        not null check (event_type ~ '^[a-z0-9]+([._][a-z0-9]+)+$'),
  entity_type      text        not null,
  entity_id        text        not null,
  title            text        not null check (length(btrim(title)) > 0 and length(title) <= 200),
  summary          text        not null default '' check (length(summary) <= 1000),
  severity         alpha.severity not null default 'info',
  requires_founder boolean     not null default false,
  deep_link        text        not null default '',
  correlation_id   text        not null,
  causation_id     text        not null default '',
  metadata         jsonb       not null default '{}'::jsonb,

  -- The deduplication key, computed the same way alpha_events.dedup_key does.
  -- Stored rather than derived so the unique index below is a plain btree, and
  -- so an operator can read why two deliveries collapsed into one event.
  dedup_key        text        not null,

  -- Bounded for the same reason the local ledger bounds it: adapters summarize
  -- provider payloads, they do not mirror them.
  constraint metadata_is_bounded check (pg_column_size(metadata) <= 8192)
);

comment on table alpha.events is
  'Append-only normalized event ledger. Historical rows are never mutated to change what an interface shows.';
comment on column alpha.events.dedup_key is
  'provider + provider_event_id + event_type, hashed. Prefix p: provider-supplied, d: derived from content.';

-- Idempotency. A provider that retries a webhook three times produces one row.
create unique index events_dedup_key_uniq on alpha.events (dedup_key);

-- The feed's only access pattern: newest first.
create index events_occurred_at_desc on alpha.events (occurred_at desc);
-- "Everything about PR-48" — the temporal half of Memory.
create index events_entity on alpha.events (entity_id, occurred_at desc);
-- One mission or workflow, assembled without a join table.
create index events_correlation on alpha.events (correlation_id, occurred_at);
create index events_causation on alpha.events (causation_id) where causation_id <> '';
create index events_founder_attention on alpha.events (occurred_at desc)
  where requires_founder;

-- Append-only, enforced rather than promised. A projection that needs mutable
-- state keeps its own; the record of what an external system reported is not
-- editable by the thing displaying it.
create or replace function alpha.reject_history_change() returns trigger
language plpgsql as $$
begin
  raise exception
    'alpha.events is append-only. % rejected on event %. Presentation state belongs in a projection.',
    tg_op, coalesce(old.event_id::text, 'unknown');
end;
$$;

create trigger events_no_update before update on alpha.events
  for each row execute function alpha.reject_history_change();
create trigger events_no_delete before delete on alpha.events
  for each row execute function alpha.reject_history_change();

-- Causation points backwards in time. A row that claims otherwise means a buggy
-- adapter, and catching it here stops a cycle reaching the interface.
create or replace function alpha.check_causation_order() returns trigger
language plpgsql as $$
declare parent_occurred timestamptz;
begin
  if new.causation_id = '' then
    return new;
  end if;
  select occurred_at into parent_occurred
    from alpha.events where event_id::text = new.causation_id;
  if parent_occurred is not null and parent_occurred > new.occurred_at then
    raise exception
      'Event % claims to be caused by %, which occurred later. Causation runs backwards in time.',
      new.event_id, new.causation_id;
  end if;
  return new;
end;
$$;

create trigger events_causation_order before insert on alpha.events
  for each row execute function alpha.check_causation_order();

-- --------------------------------------------------------------------------
-- activities — a view, not a table
-- --------------------------------------------------------------------------
-- Derived and disposable by construction. Making this a table would invite
-- someone to edit a row to fix how the feed reads, which is exactly the
-- mutation the append-only trigger above exists to prevent.

create view alpha.activities as
select
  e.event_id,
  e.occurred_at,
  greatest(0, extract(epoch from (now() - e.occurred_at))::bigint) as age_seconds,
  e.source,
  e.actor,
  e.department,
  e.event_type,
  e.entity_type,
  e.entity_id,
  e.title,
  e.summary,
  e.severity,
  e.requires_founder,
  e.deep_link,
  -- The PWA equivalent, for platforms with no native scheme handler.
  -- 'alpha-proxima://' is 16 characters, so the path starts at 17.
  case when e.deep_link like 'alpha-proxima://%'
       then '#' || substring(e.deep_link from 17)
       else e.deep_link end as web_link,
  e.correlation_id,
  e.causation_id
from alpha.events e
order by e.occurred_at desc;

comment on view alpha.activities is
  'Presentation projection over alpha.events. Rebuildable at any moment; stores nothing.';

commit;
