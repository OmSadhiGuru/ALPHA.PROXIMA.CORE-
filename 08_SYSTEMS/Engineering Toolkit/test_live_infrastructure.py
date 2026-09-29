#!/usr/bin/env python3
"""The hosted schema and the local contract must not drift apart.

`alpha_events.py` and the Supabase migrations express the same contract twice,
in two languages. That duplication is deliberate — an operator should be able to
move between the local JSONL ledger and a hosted Postgres without learning a
second vocabulary — but duplication rots silently. A severity added in Python
and forgotten in SQL would not fail anything until a real event was rejected at
3am by a database nobody was looking at.

These tests read the migration files as text and compare them to the Python
contract, so the drift fails here instead. They need no database, which is why
they can run in a CI job that installs nothing.
"""

from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
INFRA = (VAULT_ROOT / "13_OPERATIONS" / "Live Integration Layer" / "infrastructure"
         / "supabase" / "migrations")


def _load(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLKIT_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ev = _load("alpha_events.py", "alpha_events")
ad = _load("alpha_adapters.py", "alpha_adapters")
live = _load("alpha_live.py", "alpha_live")


def sql() -> str:
    return "\n".join(path.read_text(encoding="utf-8") for path in sorted(INFRA.glob("*.sql")))


def sql_code() -> str:
    """The migrations with `--` comments stripped.

    Needed wherever a test scans for statements: this file's comments discuss
    grants and revokes in prose, and a scan that reads them finds privileges
    nobody granted.
    """
    return "\n".join(
        re.sub(r"--.*$", "", line)
        for line in sql().splitlines()
    )


def enum_values(name: str) -> list[str]:
    """The values of one `create type ... as enum (...)`, in declaration order."""
    match = re.search(rf"create type alpha\.{name} as enum \(([^)]*)\)", sql(), re.S)
    if not match:
        raise AssertionError(f"alpha.{name} is not declared in any migration")
    return re.findall(r"'([^']+)'", match.group(1))


class MigrationsExistTests(unittest.TestCase):
    def test_the_migrations_are_present_and_ordered(self):
        names = sorted(path.name for path in INFRA.glob("*.sql"))
        self.assertTrue(names, "no migrations found")
        for name in names:
            self.assertRegex(name, r"^\d{4}_[a-z0-9_]+\.sql$",
                             "a migration must sort by a numeric prefix")

    def test_every_migration_states_that_it_is_not_applied(self):
        # An unapplied migration that reads as applied is the dishonesty §26
        # forbids, in the one place a Founder would check first.
        for path in sorted(INFRA.glob("*.sql")):
            with self.subTest(migration=path.name):
                self.assertIn("Not applied", path.read_text(encoding="utf-8"))

    def test_the_migrations_are_not_a_dependency_manifest(self):
        # The Engineering Toolkit's zero-dependency property is a CI gate. This
        # infrastructure boundary must not smuggle a manifest past it.
        for forbidden in ("package.json", "requirements.txt", "pyproject.toml", "setup.py"):
            self.assertFalse((INFRA.parent / forbidden).exists(),
                             f"{forbidden} would break the zero-dependency gate")


class VocabularyParityTests(unittest.TestCase):
    def test_severity_matches_and_keeps_its_order(self):
        # Order is load-bearing in both languages: the notification policy reads
        # it to decide feed / badge / push.
        self.assertEqual(enum_values("severity"), list(ev.SEVERITIES))

    def test_every_registered_provider_exists_in_the_schema(self):
        self.assertEqual(sorted(enum_values("event_source")), sorted(ev.SOURCES))

    def test_departments_match(self):
        self.assertEqual(sorted(enum_values("department")), sorted(ev.DEPARTMENTS))

    def test_presence_states_match(self):
        self.assertEqual(sorted(enum_values("presence_state")), sorted(live.PRESENCE_STATES))

    def test_notification_states_match(self):
        self.assertEqual(sorted(enum_values("notification_state")),
                         sorted(live.NOTIFICATION_STATES))

    def test_adapter_statuses_match(self):
        self.assertEqual(sorted(enum_values("adapter_status")), sorted(ad.STATUSES))

    def test_the_event_type_pattern_is_the_same_rule(self):
        # Written once in Python as a compiled regex and once in SQL as a check
        # constraint; the same string, so a new taxonomy rule cannot land in one
        # place only.
        self.assertIn("^[a-z0-9]+([._][a-z0-9]+)+$", sql())
        self.assertEqual(ev.EVENT_TYPE_RE.pattern, "^[a-z0-9]+(?:[._][a-z0-9]+)+$")

    def test_the_metadata_bound_is_the_same_number(self):
        self.assertIn(f"pg_column_size(metadata) <= {ev.MAX_METADATA_BYTES}", sql())

    def test_the_title_and_summary_limits_are_the_same_numbers(self):
        self.assertIn(f"length(title) <= {ev.MAX_TITLE}", sql())
        self.assertIn(f"length(summary) <= {ev.MAX_SUMMARY}", sql())

    def test_the_presence_ttl_default_is_the_same_number(self):
        self.assertIn(f"ttl_seconds   integer     not null default {live.PRESENCE_TTL_SECONDS}",
                      sql())

    def test_the_badge_counts_the_same_states_in_both_languages(self):
        badge = re.search(r"create or replace function alpha\.badge_count.*?\$\$;", sql(), re.S)
        self.assertIsNotNone(badge)
        for state in live.UNREAD_STATES:
            self.assertIn(f"'{state}'", badge.group(0))
        for channel in live.ATTENTION_CHANNELS:
            self.assertIn(f"'{channel}'", badge.group(0))
        # And nothing else: a read or dismissed notification must not count.
        self.assertNotIn("'dismissed'", badge.group(0))


class SchemaGuaranteeTests(unittest.TestCase):
    """The claims the migrations make, asserted as text so a deletion is loud."""

    def test_the_event_ledger_refuses_updates_and_deletes(self):
        body = sql()
        self.assertIn("reject_history_change", body)
        self.assertIn("events_no_update", body)
        self.assertIn("events_no_delete", body)

    def test_deduplication_is_a_unique_constraint_not_a_convention(self):
        self.assertIn("create unique index events_dedup_key_uniq", sql())

    def test_one_notification_per_event_is_a_unique_constraint(self):
        self.assertIn("notifications_one_per_event unique (event_id)", sql())

    def test_presence_is_read_through_a_view_that_applies_expiry(self):
        body = sql()
        self.assertIn("create view alpha.presence as", body)
        self.assertIn("make_interval(secs => p.ttl_seconds)", body)

    def test_activities_is_a_view_so_it_cannot_be_edited(self):
        self.assertIn("create view alpha.activities as", sql())
        self.assertNotIn("create table alpha.activities", sql())

    def test_an_adapter_cannot_declare_itself_connected(self):
        self.assertIn("check (declared_status <> 'connected')", sql())

    def test_observed_status_cannot_promote_a_planned_adapter(self):
        status = re.search(r"create or replace function alpha\.observed_status.*?\$\$;",
                           sql(), re.S)
        self.assertIsNotNone(status)
        self.assertIn("declared_status in ('planned', 'blocked')", status.group(0))

    def test_no_raw_push_token_column_exists_anywhere(self):
        body = sql()
        self.assertIn("token_fingerprint", body)
        self.assertNotRegex(body, r"\n\s+(push_)?token\s+text")

    def test_row_level_security_is_enabled_on_every_table(self):
        body = sql()
        tables = set(re.findall(r"create table alpha\.(\w+)", body))
        enabled = set(re.findall(r"alter table alpha\.(\w+)\s+enable row level security", body))
        self.assertEqual(tables - enabled, set(),
                         f"RLS is not enabled on: {sorted(tables - enabled)}")

    def test_row_level_security_is_forced_where_history_lives(self):
        # Without `force`, the table owner silently bypasses its own policies,
        # which makes them advisory rather than enforced.
        self.assertIn("alter table alpha.events           force row level security", sql())

    def test_no_mutation_policy_exists_for_events(self):
        body = sql()
        for statement in re.findall(r"create policy [^;]+;", body, re.S):
            if "on alpha.events" in statement:
                with self.subTest(policy=statement.split("\n")[0]):
                    self.assertNotIn(" for update ", statement)
                    self.assertNotIn(" for delete ", statement)
                    self.assertNotIn(" for all ", statement)

    def test_the_founder_may_only_move_a_notification_forward_to_read(self):
        policy = re.search(r"create policy founder_marks_notifications[^;]+;", sql(), re.S)
        self.assertIsNotNone(policy)
        self.assertIn("using (state in ('queued', 'delivered', 'failed'))", policy.group(0))
        self.assertIn("with check (state in ('read', 'dismissed'))", policy.group(0))

    def test_nothing_anonymous_holds_any_privilege(self):
        body = sql()
        self.assertIn("revoke all on all tables in schema alpha from anon", body)
        # And future tables inherit the denial rather than a grant.
        self.assertIn("alter default privileges in schema alpha revoke all on tables from anon",
                      body)
        self.assertNotRegex(sql_code(), r"grant \w+[^;]*to [^;]*\banon\b")

    def test_dead_letters_never_store_webhook_headers(self):
        # A rejected delivery's headers carry its signature. A debugging table is
        # not a place to accumulate those.
        dead = re.search(r"create table alpha\.dead_letters[^;]+;", sql(), re.S)
        self.assertIsNotNone(dead)
        self.assertNotIn("header", dead.group(0).lower())

    def test_the_schema_states_that_it_is_not_canonical_truth(self):
        self.assertIn("Not canonical truth", sql())


class PrivilegeTests(unittest.TestCase):
    """A policy without a grant is inert, and the failure is silent until used.

    RLS narrows which rows a role may see; it does not confer the right to look.
    With policies but no `GRANT SELECT`, PostgreSQL refuses on privilege grounds
    before consulting any policy — so the Founder's feed reads "permission
    denied" and, because an UPDATE must read the rows it matches, the badge can
    never be cleared. Verified against PostgreSQL 16; these tests keep the
    grants from being dropped again.
    """

    def grants_to(self, role: str) -> str:
        """Every `grant ... to <role>` statement, concatenated. Code only."""
        return "\n".join(
            statement for statement in re.findall(r"grant [^;]+;", sql_code(), re.S)
            if re.search(rf"\b{role}\b", statement)
        )

    def test_every_table_the_founder_has_a_read_policy_for_is_also_granted(self):
        body = sql_code()
        granted = self.grants_to("authenticated")
        policied = re.findall(r"create policy founder_reads_(\w+) on alpha\.(\w+)", body)
        self.assertTrue(policied, "no Founder read policies found")
        for _, table in policied:
            with self.subTest(table=table):
                self.assertRegex(
                    granted, rf"alpha\.{table}\b",
                    f"alpha.{table} has a read policy but no SELECT grant, so the policy "
                    "is inert and the read fails with permission denied",
                )

    def test_the_update_grant_is_column_scoped_not_whole_table(self):
        granted = self.grants_to("authenticated")
        self.assertIn("grant update (state, read_at, dismissed_at) on alpha.notifications",
                      granted)
        self.assertIn("revoke update on alpha.notifications from authenticated", sql_code())

    def test_marking_a_notification_read_requires_and_has_its_select_grant(self):
        # The subtle half of the defect: the column-level UPDATE grant alone is
        # not enough, because the policy's USING clause reads the row.
        self.assertRegex(self.grants_to("authenticated"), r"alpha\.notifications\b")

    def test_the_device_table_is_never_granted_only_its_barrier_view(self):
        granted = self.grants_to("authenticated")
        self.assertNotRegex(granted, r"alpha\.devices\s*(,|to)\b")
        self.assertIn("alpha.devices_readable", granted)
        self.assertIn("revoke all on alpha.devices from authenticated, anon", sql_code())

    def test_only_one_readable_device_view_exists(self):
        # Two views for one job invites a later migration granting the wrong one.
        body = sql_code()
        views = re.findall(r"create view alpha\.(devices\w*)", body)
        self.assertEqual(views, ["devices_readable"], f"found {views}")

    def test_the_ingress_role_can_write_without_relying_on_an_rls_bypass(self):
        # Supabase's service_role bypasses RLS, but a bypass is not a privilege.
        # Stating the grants keeps the schema portable to any other Postgres.
        granted = self.grants_to("service_role")
        self.assertRegex(granted, r"grant select, insert on\s+alpha\.events")
        self.assertIn("grant usage on all sequences in schema alpha to service_role", granted)

    def test_the_ingress_role_is_never_granted_update_or_delete_on_events(self):
        for statement in re.findall(r"grant [^;]+;", sql_code(), re.S):
            if "service_role" in statement and "alpha.events" in statement:
                with self.subTest(statement=statement.split("\n")[0]):
                    self.assertNotIn("update", statement)
                    self.assertNotIn("delete", statement)

    def test_the_anon_denial_comes_after_every_grant(self):
        # Order matters: a revoke that runs before a grant is undone by it.
        body = sql_code()
        last_grant = max(match.start() for match in re.finditer(r"grant ", body))
        last_revoke = max(match.start()
                          for match in re.finditer(r"revoke all on all tables in schema alpha from anon",
                                                   body))
        self.assertGreater(last_revoke, last_grant,
                           "the anon revoke must be the last word on privileges")

    def test_nothing_is_granted_to_anon_anywhere(self):
        self.assertEqual(self.grants_to("anon"), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
