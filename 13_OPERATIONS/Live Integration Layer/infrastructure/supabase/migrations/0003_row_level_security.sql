-- Alpha Proxima Live Integration Layer — row level security.
--
-- FD-002 as SQL: authentication ships before reachability, never after. The
-- local server enforces that by refusing a non-loopback bind without a token;
-- a hosted database has no loopback to hide behind, so the equivalent is that
-- every table denies by default and each grant below is a deliberate exception.
--
-- THE SHAPE OF THE POLICY
--
-- There are exactly two principals:
--
--   the Founder (an authenticated session)
--     May READ the projections. May UPDATE a notification's read and dismissed
--     state, because marking something read is the Founder's act. May not
--     insert an event, change history, or read a device token.
--
--   the ingress (the service role, server side only)
--     May INSERT events and write projections. Its key never reaches a browser.
--
-- There is deliberately no anonymous role. A public read of this schema would
-- publish the Foundation's operating tempo — who is working on what, and when
-- nobody is — which is not something a paused integration should leak.
--
-- Not applied. See `README.md` in this directory.

begin;

-- Deny by default, everywhere. Enabling RLS without a policy means no row is
-- visible, which is the correct starting point for every table below.
alter table alpha.events           enable row level security;
alter table alpha.agent_presence   enable row level security;
alter table alpha.notifications    enable row level security;
alter table alpha.devices          enable row level security;
alter table alpha.subscriptions    enable row level security;
alter table alpha.adapter_registry enable row level security;
alter table alpha.dead_letters     enable row level security;

-- `force` so the table owner is bound by its own policies too. Without this a
-- superuser connection silently bypasses everything above, which makes the
-- policies advisory rather than enforced.
alter table alpha.events           force row level security;
alter table alpha.devices          force row level security;

-- --------------------------------------------------------------------------
-- the Founder reads
-- --------------------------------------------------------------------------

create policy founder_reads_events on alpha.events
  for select to authenticated using (true);

create policy founder_reads_presence on alpha.agent_presence
  for select to authenticated using (true);

create policy founder_reads_notifications on alpha.notifications
  for select to authenticated using (true);

create policy founder_reads_subscriptions on alpha.subscriptions
  for select to authenticated using (true);

create policy founder_reads_integrations on alpha.adapter_registry
  for select to authenticated using (true);

-- Devices are deliberately absent from the read grants. `alpha.devices_public`
-- is the only device shape a client sees, and it is reached through a security
-- barrier view rather than a policy, so no column list mistake can expose the
-- fingerprint.
create view alpha.devices_readable with (security_barrier = true) as
  select device_id, platform, label, registered_at, last_seen, active
  from alpha.devices;

revoke all on alpha.devices from authenticated, anon;
grant select on alpha.devices_readable to authenticated;

-- Dead letters carry rejected provider payloads. The Founder may read them —
-- "what is broken?" must be answerable without a server log — but nothing
-- anonymous may.
create policy founder_reads_dead_letters on alpha.dead_letters
  for select to authenticated using (true);

-- --------------------------------------------------------------------------
-- the Founder marks things read
-- --------------------------------------------------------------------------

-- The single mutation an authenticated session is allowed, and it is narrowed
-- twice: only these lifecycle states, and only forward from an unread one. A
-- client cannot resurrect a dismissed notification to inflate a badge, and
-- cannot rewrite which channels a notification used.
create policy founder_marks_notifications on alpha.notifications
  for update to authenticated
  using (state in ('queued', 'delivered', 'failed'))
  with check (state in ('read', 'dismissed'));

revoke update on alpha.notifications from authenticated;
grant update (state, read_at, dismissed_at) on alpha.notifications to authenticated;

-- Subscriptions are the Founder's own preferences, so they are the Founder's to
-- change.
create policy founder_writes_subscriptions on alpha.subscriptions
  for all to authenticated using (true) with check (true);

-- --------------------------------------------------------------------------
-- the ingress writes
-- --------------------------------------------------------------------------
-- `service_role` bypasses RLS in Supabase by design. These policies are written
-- anyway, because the bypass is a property of one deployment and the intent
-- should survive a move to any other Postgres.

create policy ingress_inserts_events on alpha.events
  for insert to service_role with check (true);
-- No update or delete policy for events, for anyone. The append-only triggers
-- in 0001 refuse them regardless; this is the second lock on the same door.

create policy ingress_writes_presence on alpha.agent_presence
  for all to service_role using (true) with check (true);

create policy ingress_writes_notifications on alpha.notifications
  for all to service_role using (true) with check (true);

create policy ingress_writes_devices on alpha.devices
  for all to service_role using (true) with check (true);

create policy ingress_writes_registry on alpha.adapter_registry
  for all to service_role using (true) with check (true);

create policy ingress_writes_dead_letters on alpha.dead_letters
  for insert to service_role with check (true);

-- --------------------------------------------------------------------------
-- nothing anonymous, ever
-- --------------------------------------------------------------------------

revoke all on schema alpha from anon;
revoke all on all tables in schema alpha from anon;
revoke all on all functions in schema alpha from anon;
revoke all on all sequences in schema alpha from anon;

-- And nothing anonymous by default in future migrations either: a table added
-- later must grant access deliberately rather than inherit it.
alter default privileges in schema alpha revoke all on tables from anon;
alter default privileges in schema alpha revoke all on functions from anon;

grant usage on schema alpha to authenticated, service_role;
grant select on alpha.activities, alpha.presence, alpha.integrations to authenticated;

commit;
