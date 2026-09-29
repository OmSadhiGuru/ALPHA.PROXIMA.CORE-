#!/usr/bin/env python3
"""The live projections — what the Foundation *shows* about what happened.

`alpha_events.py` records observations. This module reads them and produces the
four things an interface actually needs, each with a different relationship to
time:

  * **activities** — a presentation projection of the event ledger. Derived,
    disposable, rebuildable from events at any moment.
  * **presence** — ephemeral. It expires. A stale "CODEX • CODING" is a lie
    about the present, so presence that has aged past its TTL is reported as
    `offline` with the last known state kept separately for context.
  * **notifications** — delivery records with their own lifecycle (queued,
    delivered, failed, read, dismissed). These mutate; the events behind them
    never do.
  * **badge** — one number, and the one most easily made useless. It counts
    unread notifications the Founder can act on, not raw activity volume.

## The projection rule

Nothing here writes to `founder-state.json`, and nothing here writes a
Markdown note. The single-writer model is preserved structurally: this module
imports neither `founder_os` nor any vault writer. It owns exactly one file —
`live-state.json` — holding presence, notification, device, and subscription
records, all of which are operational and none of which are institutional.

Delete that file and the Foundation loses its badge count and its unread
markers. It loses no knowledge. That is the test every field in it had to pass.

## Why notifications are derived rather than sent here

Severity decides *policy*; it does not perform *delivery*. `evaluate` returns
the channels an event earns. Actually pushing to a device is a separate,
credentialed step that this module models (queue, retry, failure) but does not
perform, because no push credential exists in this repository and a module that
pretended otherwise would report deliveries that never happened.

Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import timedelta
from pathlib import Path
from typing import Any, Iterable

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
LIVE_DIR = VAULT_ROOT / "13_OPERATIONS" / "Live Integration Layer"
DEFAULT_LIVE_STATE = LIVE_DIR / "state" / "live-state.json"

sys.path.insert(0, str(TOOLKIT_DIR))
import alpha_events as ev  # noqa: E402
import alpha_adapters as ad  # noqa: E402
import state_io  # noqa: E402

LIVE_SCHEMA_VERSION = "1.0.0"

# --------------------------------------------------------------------------
# presence
# --------------------------------------------------------------------------

# The operational states a Council node can be in. `offline` is the only one
# that is also a *default*: an agent nobody has heard from is offline, never
# "idle", because idle claims knowledge of the agent that silence does not give.
PRESENCE_STATES = (
    "offline", "online", "thinking", "researching", "coding",
    "indexing", "waiting", "blocked", "error",
)

# How long a presence report stays believable. Chosen to be shorter than any
# plausible human glance interval: the failure mode this prevents is the Founder
# trusting a "CODING" badge from a process that died twenty minutes ago.
PRESENCE_TTL_SECONDS = 180

# States that mean the node is doing something right now, for the "who is
# active" count. `waiting`, `blocked`, and `error` are present but not working,
# and conflating them would overstate the Council's throughput.
WORKING_STATES = ("thinking", "researching", "coding", "indexing")


# --------------------------------------------------------------------------
# notification policy
# --------------------------------------------------------------------------

# Severity to channels. This table *is* the Founder notification policy, in the
# one place that decides it. The asymmetry is intentional and load-bearing:
# only two of four severities are allowed to interrupt, because a system that
# pushes everything is a system whose pushes get ignored.
SEVERITY_CHANNELS: dict[str, tuple[str, ...]] = {
    "info": ("feed",),
    "update": ("feed", "badge"),
    "action": ("feed", "badge", "push"),
    "critical": ("feed", "badge", "push"),
}

# `critical` differs from `action` not in which channels it uses but in whether
# it may be held back: a critical push ignores quiet preferences, an action push
# does not.
BYPASSES_PREFERENCES = ("critical",)

# Channels that consume the Founder's attention outside the app. Used by the
# badge calculation, so adding a channel cannot silently change what the number
# on the app icon means.
ATTENTION_CHANNELS = ("badge", "push")

NOTIFICATION_STATES = ("queued", "delivered", "failed", "read", "dismissed")
# A notification the Founder has neither read nor dismissed still wants
# attention, even if delivery itself failed — the underlying event did not stop
# mattering because a push did not land.
UNREAD_STATES = ("queued", "delivered", "failed")

MAX_DELIVERY_ATTEMPTS = 5


def evaluate_notification(event: dict[str, Any],
                          subscriptions: Iterable[dict[str, Any]] = ()) -> dict[str, Any]:
    """Decide what one event costs the Founder's attention.

    Returns the channels, and — when a channel was withheld — the reason. The
    reason is part of the contract because "why did I not get a push for that?"
    must be answerable from the record rather than by reading this function.

    `requires_founder` can only ever *raise* the outcome to at least `action`.
    An adapter that marks an event as needing the Founder cannot be overruled
    by a severity it also chose; but no adapter can lower an event below the
    severity it declared.
    """
    severity = event.get("severity", "info")
    if severity not in SEVERITY_CHANNELS:
        raise ev.EventError(f"Cannot route unknown severity {severity!r}.")
    effective = severity
    if event.get("requires_founder") and ev.SEVERITY_RANK[severity] < ev.SEVERITY_RANK["action"]:
        effective = "action"
    channels = list(SEVERITY_CHANNELS[effective])

    withheld: list[dict[str, str]] = []
    matched = match_subscriptions(event, subscriptions)
    if matched is not None and effective not in BYPASSES_PREFERENCES:
        allowed = set(matched.get("channels") or ())
        for channel in list(channels):
            if channel not in allowed:
                channels.remove(channel)
                withheld.append({
                    "channel": channel,
                    "reason": f"subscription {matched.get('id', 'unknown')} does not include it",
                })
    return {
        "severity": severity,
        "effective_severity": effective,
        "channels": channels,
        "withheld": withheld,
        "subscription_id": (matched or {}).get("id"),
        "bypassed_preferences": effective in BYPASSES_PREFERENCES,
    }


def match_subscriptions(event: dict[str, Any],
                        subscriptions: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    """The most specific subscription that applies, or None for the default.

    Specificity is the count of constraints a subscription states. A rule about
    `github` + `ENGINEERING` + `action` beats a rule about `github` alone,
    because the Founder wrote the narrower one later and meant it.
    """
    best: dict[str, Any] | None = None
    best_score = -1
    for subscription in subscriptions:
        score = 0
        for field, key in (("source", "source"), ("event_type", "event_type"),
                           ("department", "department")):
            wanted = subscription.get(field)
            if wanted:
                if event.get(key) != wanted:
                    score = -1
                    break
                score += 1
        if score < 0:
            continue
        floor = subscription.get("min_severity")
        if floor:
            if floor not in ev.SEVERITY_RANK:
                continue
            if ev.SEVERITY_RANK.get(event.get("severity", "info"), 0) < ev.SEVERITY_RANK[floor]:
                continue
            score += 1
        if score > best_score:
            best, best_score = subscription, score
    return best


# --------------------------------------------------------------------------
# activities projection
# --------------------------------------------------------------------------

def build_activities(events: Iterable[dict[str, Any]], limit: int = 50,
                     now: str | None = None) -> dict[str, Any]:
    """The activity feed: newest first, presentation-shaped, derived only.

    Every field here is computed from the event. Nothing is stored, so a change
    to how activity reads is a redeploy, never a migration — and an event is
    never edited to make the feed look different.
    """
    ordered = ev.sort_events(events)
    reference = ev.parse_iso(now or ev.now_iso())
    rows = []
    for event in reversed(ordered):
        occurred = ev.parse_iso(event["occurred_at"])
        rows.append({
            "event_id": event["event_id"],
            "occurred_at": event["occurred_at"],
            "age_seconds": max(0, int((reference - occurred).total_seconds())),
            "source": event["source"],
            "actor": event["actor"],
            "department": event["department"],
            "event_type": event["event_type"],
            "entity_type": event["entity_type"],
            "entity_id": event["entity_id"],
            "title": event["title"],
            "summary": event["summary"],
            "severity": event["severity"],
            "requires_founder": event["requires_founder"],
            "deep_link": event["deep_link"],
            "web_link": _safe_web_link(event["deep_link"]),
            "correlation_id": event["correlation_id"],
            "causation_id": event["causation_id"],
        })
    trimmed = rows[:limit] if limit > 0 else rows
    return {
        "schema_version": LIVE_SCHEMA_VERSION,
        "generated_at": reference.isoformat(timespec="seconds"),
        "activities": trimmed,
        "counts": {
            "returned": len(trimmed),
            "total": len(rows),
            "requires_founder": sum(1 for row in rows if row["requires_founder"]),
            "by_severity": {
                severity: sum(1 for row in rows if row["severity"] == severity)
                for severity in ev.SEVERITIES
            },
        },
    }


def _safe_web_link(link: str) -> str:
    """The PWA equivalent, or empty — a bad link never breaks a whole feed."""
    if not link:
        return ""
    try:
        return ev.web_deep_link(link)
    except ev.EventError:
        return ""


def build_entity_history(events: Iterable[dict[str, Any]], entity_id: str) -> dict[str, Any]:
    """Every event about one entity, plus who touched it and what it caused.

    This is the read model behind "select PR #48 and see its whole life": the
    temporal half of Memory. It asserts no semantic relationship — it reports
    only what the ledger already witnessed, with its provenance intact.
    """
    ordered = ev.sort_events(e for e in events if e["entity_id"] == entity_id)
    actors: list[str] = []
    departments: list[str] = []
    for event in ordered:
        if event["actor"] not in actors:
            actors.append(event["actor"])
        if event["department"] not in departments:
            departments.append(event["department"])
    correlations = []
    for event in ordered:
        if event["correlation_id"] not in correlations:
            correlations.append(event["correlation_id"])
    return {
        "schema_version": LIVE_SCHEMA_VERSION,
        "entity_id": entity_id,
        "entity_type": ordered[0]["entity_type"] if ordered else None,
        "first_seen": ordered[0]["occurred_at"] if ordered else None,
        "last_seen": ordered[-1]["occurred_at"] if ordered else None,
        "actors": actors,
        "departments": departments,
        "correlation_ids": correlations,
        "events": ordered,
        "counts": {"events": len(ordered), "actors": len(actors)},
    }


# --------------------------------------------------------------------------
# the live store
# --------------------------------------------------------------------------

class LiveStore:
    """Presence, notifications, devices, and subscriptions in one owned file.

    One writer, one file, written atomically. This is the same discipline the
    Founder OS applies to its own state, applied to a store that deliberately
    holds nothing institutional — so that the operational layer can be reset
    without a governance conversation.
    """

    def __init__(self, path: Path | str = DEFAULT_LIVE_STATE) -> None:
        self.path = Path(path)
        self.state = self._load()

    def _blank(self) -> dict[str, Any]:
        return {
            "schema_version": LIVE_SCHEMA_VERSION,
            "updated_at": ev.now_iso(),
            "presence": {},
            "notifications": [],
            "devices": [],
            "subscriptions": [],
        }

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return self._blank()
        try:
            stored = json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return self._blank()
        if not isinstance(stored, dict):
            return self._blank()
        blank = self._blank()
        for key, default in blank.items():
            stored.setdefault(key, default)
        return stored

    def save(self) -> Path:
        self.state["updated_at"] = ev.now_iso()
        state_io.write_json_atomic(self.path, self.state)
        return self.path

    # -- presence --------------------------------------------------------
    def set_presence(self, node_id: str, presence_state: str, *,
                     activity: str = "", mission: str = "", event_id: str = "",
                     at: str | None = None, ttl_seconds: int = PRESENCE_TTL_SECONDS) -> dict[str, Any]:
        """Report one node's current state. Overwrites, because presence is now."""
        if presence_state not in PRESENCE_STATES:
            raise ev.EventError(
                f"Unknown presence state {presence_state!r}. One of: {', '.join(PRESENCE_STATES)}."
            )
        record = {
            "node_id": node_id,
            "state": presence_state,
            "activity": activity,
            "mission": mission,
            "last_event_id": event_id,
            "reported_at": at or ev.now_iso(),
            "ttl_seconds": int(ttl_seconds),
        }
        self.state["presence"][node_id] = record
        return record

    def presence_view(self, now: str | None = None) -> dict[str, Any]:
        """Presence with expiry applied — the whole point of this projection.

        An expired record is reported as `offline`, with `reported_state` kept so
        an interface can say "last seen coding, 14 minutes ago" without
        rendering a live-looking badge. `stale` is the flag a renderer must
        honour; no consumer has to compute TTL arithmetic itself and get it
        wrong.
        """
        reference = ev.parse_iso(now or ev.now_iso())
        rows = []
        for record in self.state["presence"].values():
            reported = ev.parse_iso(record["reported_at"])
            age = (reference - reported).total_seconds()
            expired = age > record.get("ttl_seconds", PRESENCE_TTL_SECONDS)
            rows.append({
                "node_id": record["node_id"],
                "state": "offline" if expired else record["state"],
                "reported_state": record["state"],
                "stale": expired,
                "activity": "" if expired else record.get("activity", ""),
                "mission": record.get("mission", ""),
                "last_event_id": record.get("last_event_id", ""),
                "reported_at": record["reported_at"],
                "age_seconds": max(0, int(age)),
                "expires_at": (
                    reported + timedelta(seconds=record.get("ttl_seconds", PRESENCE_TTL_SECONDS))
                ).isoformat(timespec="seconds"),
            })
        rows.sort(key=lambda row: row["node_id"])
        return {
            "schema_version": LIVE_SCHEMA_VERSION,
            "generated_at": reference.isoformat(timespec="seconds"),
            "ephemeral": True,
            "ttl_seconds": PRESENCE_TTL_SECONDS,
            "presence": rows,
            "counts": {
                "reported": len(rows),
                "live": sum(1 for row in rows if not row["stale"]),
                "stale": sum(1 for row in rows if row["stale"]),
                "working": sum(1 for row in rows
                               if not row["stale"] and row["state"] in WORKING_STATES),
            },
        }

    def prune_presence(self, now: str | None = None, keep_seconds: int = 86400) -> int:
        """Drop presence records too old to inform even a 'last seen' line."""
        reference = ev.parse_iso(now or ev.now_iso())
        doomed = [
            node_id for node_id, record in self.state["presence"].items()
            if (reference - ev.parse_iso(record["reported_at"])).total_seconds() > keep_seconds
        ]
        for node_id in doomed:
            del self.state["presence"][node_id]
        return len(doomed)

    # -- devices ---------------------------------------------------------
    def register_device(self, device_id: str, *, platform: str, token: str,
                        label: str = "", at: str | None = None) -> dict[str, Any]:
        """Store a device by token *fingerprint*, never by token.

        The raw token is hashed on the way in and the plaintext is not retained
        anywhere in this store. That makes the read model safe by construction
        rather than by remembering to redact — a later endpoint cannot leak what
        was never written. The consequence is accepted deliberately: delivery
        needs the raw token, so it must come from the caller at send time, from
        a server-side secret store, not from here.
        """
        if not token:
            raise ev.EventError("A device registration needs a token to fingerprint.")
        fingerprint = hashlib.sha256(token.encode("utf-8")).hexdigest()
        record = {
            "device_id": device_id,
            "platform": platform,
            "label": label,
            "token_fingerprint": fingerprint[:32],
            "registered_at": at or ev.now_iso(),
            "last_seen": at or ev.now_iso(),
            "active": True,
        }
        self.state["devices"] = [
            d for d in self.state["devices"] if d["device_id"] != device_id
        ] + [record]
        return record

    def devices_view(self) -> list[dict[str, Any]]:
        """Devices as a public read model. No token, and no fingerprint either.

        A fingerprint is not a credential, but it is a stable identifier for a
        Founder's physical device, and a read API has no use for it.
        """
        return [
            {key: value for key, value in device.items() if key != "token_fingerprint"}
            for device in sorted(self.state["devices"], key=lambda d: d["device_id"])
        ]

    # -- subscriptions ---------------------------------------------------
    def set_subscription(self, subscription_id: str, *, channels: Iterable[str],
                         source: str = "", event_type: str = "", department: str = "",
                         min_severity: str = "") -> dict[str, Any]:
        allowed = tuple(dict.fromkeys(channels))
        unknown = [c for c in allowed if c not in ("feed", "badge", "push")]
        if unknown:
            raise ev.EventError(f"Unknown notification channel(s): {', '.join(unknown)}.")
        if min_severity and min_severity not in ev.SEVERITY_RANK:
            raise ev.EventError(f"Unknown min_severity {min_severity!r}.")
        record = {
            "id": subscription_id,
            "channels": list(allowed),
            "source": source,
            "event_type": event_type,
            "department": department,
            "min_severity": min_severity,
        }
        self.state["subscriptions"] = [
            s for s in self.state["subscriptions"] if s["id"] != subscription_id
        ] + [record]
        return record

    def subscriptions(self) -> list[dict[str, Any]]:
        return list(self.state["subscriptions"])

    # -- notifications ---------------------------------------------------
    def notify(self, event: dict[str, Any], at: str | None = None) -> dict[str, Any] | None:
        """Derive at most one notification record from one event.

        Returns None when the event earns no attention channel — an `info` event
        belongs in the feed, and the feed is the activities projection, not a
        notification. Creating a record for it would inflate every count that
        matters.

        Idempotent per event: a projection rebuilt twice does not double the
        badge. The event ledger already guarantees one record per occurrence;
        this guarantees one notification per record.
        """
        decision = evaluate_notification(event, self.subscriptions())
        channels = [c for c in decision["channels"] if c in ATTENTION_CHANNELS]
        if not channels:
            return None
        existing = self.find_notification(event["event_id"])
        if existing is not None:
            return existing
        record = {
            "id": f"NTF-{event['event_id'][:12]}",
            "event_id": event["event_id"],
            "created_at": at or ev.now_iso(),
            "severity": event["severity"],
            "effective_severity": decision["effective_severity"],
            "channels": channels,
            "withheld": decision["withheld"],
            "title": event["title"],
            "summary": event["summary"],
            "deep_link": event["deep_link"],
            "web_link": _safe_web_link(event["deep_link"]),
            "source": event["source"],
            "department": event["department"],
            "actor": event["actor"],
            "state": "queued",
            "attempts": 0,
            "last_error": None,
            "delivered_at": None,
            "read_at": None,
            "dismissed_at": None,
        }
        self.state["notifications"].append(record)
        return record

    def project_notifications(self, events: Iterable[dict[str, Any]]) -> dict[str, int]:
        """Run the policy over a batch of events, creating only what is missing.

        The three outcomes are reported separately because they mean different
        things to an operator: `created` is new work for a sender, `existing` is
        a re-run finding nothing to do, and `no_channel` is the policy correctly
        declining to interrupt. Collapsing them would make a repeated projection
        look like a burst of new obligations.
        """
        created = existing = no_channel = 0
        for event in ev.sort_events(events):
            already = self.find_notification(event["event_id"]) is not None
            if self.notify(event) is None:
                no_channel += 1
            elif already:
                existing += 1
            else:
                created += 1
        return {"created": created, "existing": existing, "no_channel": no_channel}

    def find_notification(self, event_id: str) -> dict[str, Any] | None:
        for record in self.state["notifications"]:
            if record["event_id"] == event_id:
                return record
        return None

    def _transition(self, notification_id: str, target: str, at: str | None,
                    field: str | None) -> dict[str, Any]:
        for record in self.state["notifications"]:
            if record["id"] == notification_id:
                record["state"] = target
                if field:
                    record[field] = at or ev.now_iso()
                return record
        raise ev.EventError(f"No notification {notification_id!r}.")

    def mark_delivered(self, notification_id: str, at: str | None = None) -> dict[str, Any]:
        record = self._transition(notification_id, "delivered", at, "delivered_at")
        record["attempts"] += 1
        return record

    def mark_failed(self, notification_id: str, reason: str, at: str | None = None) -> dict[str, Any]:
        """Record a failed delivery attempt, retryable until the attempt ceiling.

        The state stays `failed` either way; `retryable` is what a sender reads.
        A notification that has exhausted its attempts is not deleted — a push
        that never reached the Founder is exactly the thing an operator needs to
        be able to see.
        """
        record = self._transition(notification_id, "failed", at, None)
        record["attempts"] += 1
        record["last_error"] = {"at": at or ev.now_iso(), "reason": reason[:300]}
        record["retryable"] = record["attempts"] < MAX_DELIVERY_ATTEMPTS
        return record

    def mark_read(self, notification_id: str, at: str | None = None) -> dict[str, Any]:
        return self._transition(notification_id, "read", at, "read_at")

    def dismiss(self, notification_id: str, at: str | None = None) -> dict[str, Any]:
        return self._transition(notification_id, "dismissed", at, "dismissed_at")

    def queued(self) -> list[dict[str, Any]]:
        """What a delivery worker should attempt: queued, plus retryable failures."""
        return [
            record for record in self.state["notifications"]
            if record["state"] == "queued"
            or (record["state"] == "failed" and record["attempts"] < MAX_DELIVERY_ATTEMPTS)
        ]

    def badge_count(self) -> int:
        """Unread notifications that consume attention outside the app.

        Deliberately not "number of recent events". A badge that counts activity
        trains the Founder to ignore it; a badge that counts obligations does
        not. `info` events never reach this function — they produce no
        notification at all.
        """
        return sum(
            1 for record in self.state["notifications"]
            if record["state"] in UNREAD_STATES
            and any(channel in ATTENTION_CHANNELS for channel in record["channels"])
        )

    def synchronize_badge(self, at: str | None = None) -> dict[str, Any]:
        """What the app calls on open: the authoritative count, plus its parts.

        Opening the app does not mark anything read — that is the Founder's act,
        not the app's. This returns the number every device should display, so
        two devices cannot disagree about it.
        """
        return {
            "schema_version": LIVE_SCHEMA_VERSION,
            "synchronized_at": at or ev.now_iso(),
            "badge": self.badge_count(),
            "by_state": {
                state: sum(1 for r in self.state["notifications"] if r["state"] == state)
                for state in NOTIFICATION_STATES
            },
            "unread_push": sum(
                1 for r in self.state["notifications"]
                if r["state"] in UNREAD_STATES and "push" in r["channels"]
            ),
        }

    def notifications_view(self, limit: int = 50) -> dict[str, Any]:
        records = sorted(self.state["notifications"], key=lambda r: r["created_at"], reverse=True)
        trimmed = records[:limit] if limit > 0 else records
        return {
            "schema_version": LIVE_SCHEMA_VERSION,
            "generated_at": ev.now_iso(),
            "notifications": trimmed,
            "badge": self.badge_count(),
            "counts": {
                "returned": len(trimmed),
                "total": len(records),
                "queued": len(self.queued()),
                **{state: sum(1 for r in records if r["state"] == state)
                   for state in NOTIFICATION_STATES},
            },
        }


# --------------------------------------------------------------------------
# degraded mode
# --------------------------------------------------------------------------

# How long the operational layer may be silent before the interface must say
# so. Longer than the presence TTL: one missed heartbeat is not an outage, but
# ten minutes of silence is something the Founder should be told rather than
# left to infer from a feed that stopped moving.
REALTIME_STALE_AFTER_SECONDS = 600


def realtime_status(last_event_at: str | None, *, realtime_configured: bool = False,
                    now: str | None = None) -> dict[str, Any]:
    """How much of what the interface is showing can still be trusted.

    Three honest outcomes, never collapsed into one green dot:

      * `unconfigured` — no realtime transport exists. Canonical knowledge and
        the stored ledger are fully readable; nothing is live. This is the
        Foundation's actual state today.
      * `stale` — a transport exists but has been silent past the window.
      * `live` — configured and recently heard from.

    In every case `canonical_readable` is true, because the Markdown vault does
    not depend on this layer. That is the guarantee §19 asks for, stated as a
    field rather than as a promise in a document.
    """
    reference = ev.parse_iso(now or ev.now_iso())
    age = None
    if last_event_at:
        age = max(0, int((reference - ev.parse_iso(last_event_at)).total_seconds()))

    if not realtime_configured:
        mode, detail = "unconfigured", (
            "No realtime transport is configured. Activity is read from the local "
            "event ledger; nothing streams."
        )
    elif age is None:
        mode, detail = "stale", "Realtime is configured but no event has ever arrived."
    elif age > REALTIME_STALE_AFTER_SECONDS:
        mode, detail = "stale", f"No event for {age}s; showing the last known state."
    else:
        mode, detail = "live", f"Last event {age}s ago."

    return {
        "mode": mode,
        "detail": detail,
        "realtime_configured": realtime_configured,
        "last_event_at": last_event_at,
        "last_event_age_seconds": age,
        "stale_after_seconds": REALTIME_STALE_AFTER_SECONDS,
        # The Foundation's knowledge never depends on this layer being up.
        "canonical_readable": True,
        "presence_trustworthy": mode == "live",
    }


# --------------------------------------------------------------------------
# the composed live read model
# --------------------------------------------------------------------------

def build_live_view(ledger: ev.EventLedger, store: LiveStore,
                    registry: ad.AdapterRegistry | None = None,
                    limit: int = 50, now: str | None = None) -> dict[str, Any]:
    """One document holding every live projection, for one interface read.

    Composed the same way `alpha_app.build_app_view` composes its halves: each
    projection is independently obtainable, and this is the convenience that
    stops an interface making five round trips to render one screen.
    """
    reference = now or ev.now_iso()
    events = ledger.events()
    last_event_at = events[-1]["occurred_at"] if events else None
    integrations = (registry or ad.AdapterRegistry()).view(reference)
    connected_realtime = any(
        row["status"] == "connected" for row in integrations["adapters"]
    )
    return {
        "schema_version": LIVE_SCHEMA_VERSION,
        "generated_at": reference,
        "mode": "read_only",
        "canonical_sources": {
            "operate": "13_OPERATIONS/Founder OS/state/founder-state.json",
            "know": "obsidian_markdown",
            "live": "13_OPERATIONS/Live Integration Layer/state/event-ledger.jsonl",
        },
        "realtime": realtime_status(last_event_at, realtime_configured=connected_realtime,
                                    now=reference),
        "activity": build_activities(events, limit=limit, now=reference),
        "presence": store.presence_view(reference),
        "notifications": store.notifications_view(limit=limit),
        "badge": store.synchronize_badge(reference),
        "integrations": integrations,
        "devices": store.devices_view(),
        "subscriptions": store.subscriptions(),
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ap.py live", description=__doc__)
    parser.add_argument("--ledger", default=str(ev.DEFAULT_LEDGER), help="Event ledger (JSONL).")
    parser.add_argument("--live-state", default=str(DEFAULT_LIVE_STATE), help="Live projection store.")
    parser.add_argument("--registry", default=str(ad.DEFAULT_REGISTRY), help="Adapter health file.")
    parser.add_argument("--limit", type=int, default=50, help="Rows per projection.")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("view", help="Print the whole live read model as JSON.")
    sub.add_parser("activity", help="Print the activity projection as JSON.")
    sub.add_parser("presence", help="Print presence, with expiry applied.")
    sub.add_parser("notifications", help="Print notification records and the badge.")
    sub.add_parser("badge", help="Print the synchronized badge count.")
    sub.add_parser("integrations", help="Print adapter status, honestly.")
    sub.add_parser("status", help="Answer 'what is broken?' in one screen.")

    project = sub.add_parser("project", help="Run the notification policy over stored events.")
    project.add_argument("--dry-run", action="store_true", help="Report only; write nothing.")

    presence = sub.add_parser("set-presence", help="Report one node's current state.")
    presence.add_argument("node_id")
    presence.add_argument("state", choices=PRESENCE_STATES)
    presence.add_argument("--activity", default="")
    presence.add_argument("--mission", default="")

    history = sub.add_parser("history", help="Every stored event about one entity.")
    history.add_argument("entity_id")

    mark = sub.add_parser("mark", help="Move one notification through its lifecycle.")
    mark.add_argument("notification_id")
    mark.add_argument("state", choices=("delivered", "read", "dismissed", "failed"))
    mark.add_argument("--reason", default="unspecified", help="Required context for 'failed'.")

    link = sub.add_parser("deep-link", help="Build a deep link and its web equivalent.")
    link.add_argument("root", choices=ev.DEEP_LINK_ROOTS)
    link.add_argument("parts", nargs="*")
    return parser


def _render_status(view: dict[str, Any]) -> str:
    lines = ["LIVE INTEGRATION LAYER", ""]
    realtime = view["realtime"]
    lines.append(f"  realtime     {realtime['mode']:<14} {realtime['detail']}")
    lines.append(f"  canonical    {'readable' if realtime['canonical_readable'] else 'UNREADABLE'}")
    presence = view["presence"]["counts"]
    lines.append(
        f"  presence     {presence['live']} live, {presence['stale']} stale, "
        f"{presence['working']} working"
    )
    activity = view["activity"]["counts"]
    lines.append(
        f"  activity     {activity['total']} event(s), "
        f"{activity['requires_founder']} awaiting the Founder"
    )
    lines.append(f"  badge        {view['badge']['badge']}")
    lines.append("")
    counts = view["integrations"]["counts"]
    lines.append(
        "  adapters     "
        + ", ".join(f"{counts[s]} {s}" for s in ad.STATUSES if counts[s])
    )
    broken = view["integrations"]["broken"]
    if broken:
        lines.append("")
        lines.append("  NOT CARRYING TRAFFIC")
        for row in broken:
            lines.append(f"    {row['adapter_id']:<22} {row['status']:<13} {row['reason'][:52]}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    ledger = ev.EventLedger(args.ledger)
    store = LiveStore(args.live_state)
    registry = ad.AdapterRegistry(args.registry)

    def emit(payload: Any) -> int:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    try:
        if args.command == "view":
            return emit(build_live_view(ledger, store, registry, limit=args.limit))
        if args.command == "status":
            print(_render_status(build_live_view(ledger, store, registry, limit=args.limit)))
            return 0
        if args.command == "activity":
            return emit(build_activities(ledger.events(), limit=args.limit))
        if args.command == "presence":
            return emit(store.presence_view())
        if args.command == "notifications":
            return emit(store.notifications_view(limit=args.limit))
        if args.command == "badge":
            return emit(store.synchronize_badge())
        if args.command == "integrations":
            return emit(registry.view())
        if args.command == "history":
            return emit(build_entity_history(ledger.events(), args.entity_id))
        if args.command == "deep-link":
            native = ev.deep_link(args.root, *args.parts)
            return emit({"deep_link": native, "web_link": ev.web_deep_link(native)})

        if args.command == "project":
            result = store.project_notifications(ledger.events())
            if not args.dry_run:
                store.save()
            print(
                f"created {result['created']} notification(s); "
                f"{result['existing']} already existed; "
                f"{result['no_channel']} event(s) earned no attention channel."
                + (" (dry run — nothing written)" if args.dry_run else "")
            )
            return 0

        if args.command == "set-presence":
            record = store.set_presence(args.node_id, args.state,
                                        activity=args.activity, mission=args.mission)
            store.save()
            return emit(record)

        if args.command == "mark":
            if args.state == "delivered":
                record = store.mark_delivered(args.notification_id)
            elif args.state == "read":
                record = store.mark_read(args.notification_id)
            elif args.state == "dismissed":
                record = store.dismiss(args.notification_id)
            else:
                record = store.mark_failed(args.notification_id, args.reason)
            store.save()
            return emit(record)
    except (ev.EventError, ad.AdapterError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
