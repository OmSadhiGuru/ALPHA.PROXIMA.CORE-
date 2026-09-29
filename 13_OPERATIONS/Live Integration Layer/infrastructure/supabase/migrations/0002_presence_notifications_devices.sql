-- Alpha Proxima Live Integration Layer — the mutable projections.
--
-- Everything in `0001` is append-only. Everything here changes, and the
-- separation is the point: presence expires, notifications are read, adapters
-- go degraded. Keeping those in different files makes it obvious which tables
-- a bug can corrupt and which it cannot.
--
-- Not applied. See `README.md` in this directory.

begin;

-- --------------------------------------------------------------------------
-- agent_presence — ephemeral, and enforced as such
-- --------------------------------------------------------------------------

create table alpha.agent_presence (
  node_id       text primary key,
  state         alpha.presence_state not null default 'offline',
  activity      text        not null default '',
  mission       text        not null default '',
  last_event_id uuid        references alpha.events (event_id),
  reported_at   timestamptz not null default now(),
  -- Stored per row rather than as a global constant: a slow indexing job and a
  -- fast coding loop do not become believable for the same length of time.
  ttl_seconds   integer     not null default 180 check (ttl_seconds between 10 and 3600)
);

comment on table alpha.agent_presence is
  'Ephemeral operational state. Never historical truth — read through alpha.presence, which applies expiry.';

-- The only presence anything should read. A stale "CODING" badge is a lie about
-- the present, so expiry is applied in the database rather than left to each
-- client to compute and get wrong.
create view alpha.presence as
select
  p.node_id,
  case when now() - p.reported_at > make_interval(secs => p.ttl_seconds)
       then 'offline'::alpha.presence_state else p.state end as state,
  p.state as reported_state,
  (now() - p.reported_at > make_interval(secs => p.ttl_seconds)) as stale,
  -- A stale activity string must not read as something happening now.
  case when now() - p.reported_at > make_interval(secs => p.ttl_seconds)
       then '' else p.activity end as activity,
  p.mission,
  p.last_event_id,
  p.reported_at,
  extract(epoch from (now() - p.reported_at))::bigint as age_seconds,
  p.reported_at + make_interval(secs => p.ttl_seconds) as expires_at
from alpha.agent_presence p;

comment on view alpha.presence is
  'Presence with expiry applied. Clients read this, never agent_presence directly.';

-- --------------------------------------------------------------------------
-- subscriptions — the Founder's notification preferences
-- --------------------------------------------------------------------------

create table alpha.subscriptions (
  id           text primary key,
  channels     text[]      not null default '{}'::text[]
                 check (channels <@ array['feed', 'badge', 'push']::text[]),
  source       alpha.event_source,
  event_type   text,
  department   alpha.department,
  min_severity alpha.severity,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);

comment on table alpha.subscriptions is
  'Preferences by source, event type, department and severity. A critical event overrides all of them.';

-- --------------------------------------------------------------------------
-- notifications — derived delivery records with their own lifecycle
-- --------------------------------------------------------------------------

create table alpha.notifications (
  id                 text primary key,
  event_id           uuid not null references alpha.events (event_id),
  created_at         timestamptz not null default now(),
  severity           alpha.severity not null,
  -- What the policy decided after `requires_founder` was applied, kept beside
  -- the declared severity so "why did this push?" is answerable from the row.
  effective_severity alpha.severity not null,
  channels           text[] not null
                       check (channels <@ array['feed', 'badge', 'push']::text[]),
  withheld           jsonb  not null default '[]'::jsonb,
  state              alpha.notification_state not null default 'queued',
  attempts           integer not null default 0 check (attempts >= 0),
  last_error         jsonb,
  delivered_at       timestamptz,
  read_at            timestamptz,
  dismissed_at       timestamptz,

  -- One notification per event. The ledger guarantees one event per occurrence;
  -- this guarantees a rebuilt projection cannot double the badge.
  constraint notifications_one_per_event unique (event_id)
);

comment on table alpha.notifications is
  'Derived delivery records. Mutable; the events behind them are not.';

create index notifications_created_at_desc on alpha.notifications (created_at desc);
-- The badge query, and the delivery worker's queue.
create index notifications_unread on alpha.notifications (state)
  where state in ('queued', 'delivered', 'failed');

-- --------------------------------------------------------------------------
-- devices — registered, never with a readable token
-- --------------------------------------------------------------------------

create table alpha.devices (
  device_id          text primary key,
  platform           text not null,
  label              text not null default '',
  -- A fingerprint, never the token. Delivery reads the raw token from a
  -- server-side secret store; this table exists to know a device is registered,
  -- not to be able to reach it. What is never written cannot leak.
  token_fingerprint  text not null,
  registered_at      timestamptz not null default now(),
  last_seen          timestamptz not null default now(),
  active             boolean not null default true
);

comment on column alpha.devices.token_fingerprint is
  'sha256 prefix of the push token. The raw token is never stored here and never served.';

-- The readable device shape is defined in 0003 (`alpha.devices_readable`),
-- beside the revoke that makes it the *only* way to see a device. Defining a
-- second one here would leave an ungranted view that a later migration could
-- grant by mistake, exposing the fingerprint.

-- --------------------------------------------------------------------------
-- adapter_registry — honest integration status
-- --------------------------------------------------------------------------

create table alpha.adapter_registry (
  adapter_id       text primary key,
  provider         alpha.event_source not null,
  display_name     text not null,
  -- What the adapter can be before any delivery arrives. A `connected`
  -- declaration is rejected: connection is observed, never declared.
  declared_status  alpha.adapter_status not null
                     check (declared_status <> 'connected'),
  capabilities     text[] not null default '{}'::text[],
  configuration_required text[] not null default '{}'::text[],
  blocked_reason   text not null default '',
  schema_version   text not null default '1.0',
  last_seen        timestamptz,
  last_success     timestamptz,
  last_error       jsonb,
  error_count      integer not null default 0,
  success_count    integer not null default 0,
  event_count      integer not null default 0,
  -- Fixture replays, counted separately and deliberately unable to promote
  -- status: a local file is not evidence about the world.
  last_rehearsal   timestamptz,
  rehearsal_count  integer not null default 0,
  last_latency_ms  numeric
);

comment on table alpha.adapter_registry is
  'Each adapter''s declared contract joined to its observed health. Status is earned by a verified delivery.';

-- The honesty guard, as a function so no view or client can reimplement it
-- more generously. Mirrors AdapterRegistry.observed_status exactly.
create or replace function alpha.observed_status(row_in alpha.adapter_registry)
returns alpha.adapter_status
language sql stable as $$
  select case
    -- Telemetry never promotes an adapter nobody built or that waits on a
    -- decision.
    when row_in.declared_status in ('planned', 'blocked') then row_in.declared_status
    -- Errors alone do not mean degraded: degraded means it worked and stopped.
    when row_in.last_success is null then 'disconnected'::alpha.adapter_status
    when row_in.last_error is not null
         and (row_in.last_error->>'at')::timestamptz > row_in.last_success
      then 'degraded'::alpha.adapter_status
    -- Silence is indistinguishable from a broken webhook, so it reads the same.
    when now() - row_in.last_success > interval '24 hours'
      then 'degraded'::alpha.adapter_status
    else 'connected'::alpha.adapter_status
  end;
$$;

create view alpha.integrations as
select
  r.adapter_id,
  r.provider,
  r.display_name,
  r.declared_status,
  alpha.observed_status(r.*) as status,
  alpha.observed_status(r.*) = 'connected' as connected,
  r.capabilities,
  r.configuration_required,
  r.blocked_reason,
  r.schema_version,
  r.last_seen,
  r.last_success,
  r.last_error,
  r.error_count,
  r.success_count,
  r.event_count,
  r.last_rehearsal,
  r.rehearsal_count,
  r.last_latency_ms
from alpha.adapter_registry r;

comment on view alpha.integrations is
  'What the Founder''s integration screen reads. A planned adapter can never appear connected here.';

-- --------------------------------------------------------------------------
-- badge — one number, and the one most easily made useless
-- --------------------------------------------------------------------------

create or replace function alpha.badge_count() returns integer
language sql stable as $$
  -- Unread obligations, not activity volume. A badge that counts activity
  -- trains its reader to ignore it. `info` events produce no notification at
  -- all, so they cannot reach this count.
  select count(*)::integer
  from alpha.notifications
  where state in ('queued', 'delivered', 'failed')
    and channels && array['badge', 'push']::text[];
$$;

-- --------------------------------------------------------------------------
-- dead letters — a delivery that could not be understood
-- --------------------------------------------------------------------------
-- A rejected payload is evidence about an adapter, so it is kept rather than
-- dropped. Note what is NOT stored: headers. A rejected webhook's headers carry
-- its signature, and a debugging table is not a place to accumulate those.

create table alpha.dead_letters (
  id           bigserial primary key,
  received_at  timestamptz not null default now(),
  provider     text not null,
  kind         text not null default '',
  adapter_id   text,
  reason       text not null,
  payload      jsonb not null default '{}'::jsonb,
  constraint dead_letter_payload_is_bounded check (pg_column_size(payload) <= 32768)
);

comment on table alpha.dead_letters is
  'Deliveries rejected at the adapter boundary, kept so a broken adapter is visible. Headers are never stored.';

create index dead_letters_recent on alpha.dead_letters (received_at desc);

commit;
