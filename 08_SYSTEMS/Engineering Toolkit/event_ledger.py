#!/usr/bin/env python3
"""Append-only event ledger, and the projections read from it.

An event happened. History is therefore not editable — if the interface finds
it inconvenient, the interface changes, not the past. That single rule is what
makes institutional memory trustworthy enough to reason over a decade later.

So the ledger only ever appends, and everything mutable is a **projection**
computed from it:

    ledger (append-only, durable)
       ├── activity      what has been happening, newest first
       ├── presence      what is happening right now, and expires
       └── notifications what has reached the Founder, and what is unread

The storage is JSON Lines: one event per line, newline-terminated, never
rewritten. A format that appends by construction cannot be silently mutated by
a careless writer, and it stays readable with `tail` and `grep` long after this
code is gone. It is operational state, not canon — the Markdown vault remains
the Foundation's truth, and nothing here belongs in it.

**Presence is not truth.** It is a claim with an expiry. A crashed agent must
never read as CODING forever, so every presence signal carries a TTL and the
projection drops it at read time. Historical work lives in events; current
activity lives in presence; the two are never confused.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from datetime import timedelta
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
DEFAULT_LEDGER = VAULT_ROOT / "13_OPERATIONS" / "Alpha Proxima App" / "live" / "event-ledger.jsonl"


def _load_sibling(filename: str, name: str):
    path = (TOOLKIT_DIR / filename).resolve()
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


alpha_event = _load_sibling("alpha_event.py", "ledger_alpha_event")

SCHEMA_VERSION = "1.0"

# How long a presence signal is believed without renewal. Short enough that a
# crashed agent stops claiming to work within a minute; long enough that a
# healthy agent is not forced into a chatty heartbeat.
DEFAULT_PRESENCE_TTL_SECONDS = 90

PRESENCE_STATES = (
    "offline", "online", "thinking", "researching", "coding",
    "indexing", "waiting", "blocked", "error",
)

# States that mean an actor believes it is working. These are the ones whose
# expiry matters, because these are the ones that lie when a process dies.
WORKING_STATES = ("thinking", "researching", "coding", "indexing")


class LedgerError(Exception):
    """Raised when the ledger cannot be read or appended to."""


# --------------------------------------------------------------------------
# storage
# --------------------------------------------------------------------------

def read_ledger(path: Path = DEFAULT_LEDGER) -> list[dict[str, Any]]:
    """Every event ever appended, in the order it was appended.

    A corrupt line is reported, never skipped silently: a ledger that quietly
    drops what it cannot parse is worse than one that admits the gap.
    """
    path = Path(path)
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            events.append(json.loads(stripped))
        except json.JSONDecodeError as exc:
            raise LedgerError(f"{path}:{number}: corrupt ledger line: {exc}") from exc
    return events


def known_keys(path: Path = DEFAULT_LEDGER) -> set[str]:
    return {
        event.get("idempotency_key") or alpha_event.idempotency_key(event)
        for event in read_ledger(path)
    }


def append(events: list[dict[str, Any]], path: Path = DEFAULT_LEDGER
           ) -> dict[str, Any]:
    """Append valid, non-duplicate events. Never rewrites, never reorders.

    Idempotency is enforced here rather than trusted upstream, because the
    retry that produces a duplicate is exactly the case where upstream is
    already not behaving as expected.
    """
    path = Path(path)
    seen = known_keys(path)

    accepted: list[dict[str, Any]] = []
    duplicates: list[str] = []
    rejected: list[dict[str, Any]] = []

    for event in events:
        problems = alpha_event.validate(event)
        if problems:
            rejected.append({"event_id": event.get("event_id"), "problems": problems})
            continue
        key = event.get("idempotency_key") or alpha_event.idempotency_key(event)
        if key in seen:
            duplicates.append(key)
            continue
        seen.add(key)
        accepted.append({**event, "idempotency_key": key})

    if accepted:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            for event in accepted:
                handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")

    return {
        "appended": len(accepted),
        "duplicates": len(duplicates),
        "rejected": rejected,
        "events": accepted,
    }


# --------------------------------------------------------------------------
# projections
# --------------------------------------------------------------------------

def activity(events: list[dict[str, Any]], limit: int = 50) -> dict[str, Any]:
    """What has been happening, newest first."""
    ordered = sorted(events, key=lambda e: str(e.get("occurred_at", "")), reverse=True)
    return {
        "generated_at": alpha_event.now_iso(),
        "total": len(events),
        "by_source": dict(Counter(str(e.get("source")) for e in events).most_common()),
        "by_severity": dict(Counter(str(e.get("severity")) for e in events).most_common()),
        "items": ordered[:limit],
    }


def presence(events: list[dict[str, Any]], now: str | None = None,
             ttl_seconds: int = DEFAULT_PRESENCE_TTL_SECONDS) -> dict[str, Any]:
    """Who is doing what *right now*, with everything stale already dropped.

    Only the latest presence signal per actor counts, and only while it is
    within its TTL. An actor whose signal has expired is reported `offline`
    with the state it was last claiming, so a silent death is visible as a
    silent death rather than as work in progress.
    """
    moment = alpha_event.parse_iso(now or alpha_event.now_iso())
    cutoff = moment - timedelta(seconds=ttl_seconds)

    latest: dict[str, dict[str, Any]] = {}
    for event in events:
        if event.get("entity_type") != "presence":
            continue
        actor = event.get("actor_id")
        if not actor:
            continue
        occurred = str(event.get("occurred_at", ""))
        if not occurred:
            continue
        current = latest.get(actor)
        if current is None or occurred > str(current.get("occurred_at", "")):
            latest[actor] = event

    actors: list[dict[str, Any]] = []
    for actor, event in sorted(latest.items()):
        claimed = str((event.get("metadata") or {}).get("presence_state") or "online")
        if claimed not in PRESENCE_STATES:
            claimed = "online"
        occurred_at = alpha_event.parse_iso(str(event["occurred_at"]))
        ttl = int((event.get("metadata") or {}).get("ttl_seconds") or ttl_seconds)
        expires_at = occurred_at + timedelta(seconds=ttl)
        expired = expires_at <= moment
        actors.append({
            "actor_id": actor,
            "state": "offline" if expired else claimed,
            "claimed_state": claimed,
            "expired": expired,
            "since": event["occurred_at"],
            "expires_at": expires_at.isoformat(timespec="seconds"),
            "entity_id": event.get("entity_id"),
            "title": event.get("title"),
        })

    return {
        "generated_at": alpha_event.now_iso(),
        "as_of": moment.isoformat(timespec="seconds"),
        "ttl_seconds": ttl_seconds,
        "cutoff": cutoff.isoformat(timespec="seconds"),
        "actors": actors,
        "counts": {
            "total": len(actors),
            "live": sum(1 for a in actors if not a["expired"]),
            "expired": sum(1 for a in actors if a["expired"]),
            "working": sum(1 for a in actors
                           if not a["expired"] and a["state"] in WORKING_STATES),
        },
    }


def notifications(events: list[dict[str, Any]], read_keys: set[str] | None = None
                  ) -> dict[str, Any]:
    """What reached the Founder, and what is still unread.

    The badge counts unread *meaningful* notifications — those the policy grants
    a badge — not event volume. A hundred routine commits are a hundred feed
    items and zero badge, which is the only way a badge keeps meaning anything.
    """
    read_keys = read_keys or set()
    items: list[dict[str, Any]] = []
    for event in events:
        policy = alpha_event.notification_policy(event)
        if not policy["badge"] and not policy["push"]:
            continue
        key = event.get("idempotency_key") or alpha_event.idempotency_key(event)
        items.append({
            "idempotency_key": key,
            "event_id": event.get("event_id"),
            "occurred_at": event.get("occurred_at"),
            "severity": event.get("severity"),
            "title": event.get("title"),
            "summary": event.get("summary"),
            "actor_id": event.get("actor_id"),
            "deep_link": event.get("deep_link"),
            "requires_founder": bool(event.get("requires_founder")),
            "read": key in read_keys,
            "delivery": policy,
        })
    items.sort(key=lambda i: str(i["occurred_at"]), reverse=True)
    unread = [i for i in items if not i["read"]]
    return {
        "generated_at": alpha_event.now_iso(),
        "badge_count": len(unread),
        "items": items,
        "counts": {
            "total": len(items),
            "unread": len(unread),
            "push": sum(1 for i in items if i["delivery"]["push"]),
            "immediate": sum(1 for i in items if i["delivery"]["immediate"]),
        },
    }


def build_live_view(path: Path = DEFAULT_LEDGER, now: str | None = None
                    ) -> dict[str, Any]:
    """The composed live read model — the contract the interface consumes.

    Kept deliberately parallel to the App's `build_app_view`: one document, one
    read, every projection derived. Nothing here writes.
    """
    events = read_ledger(path)
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": alpha_event.now_iso(),
        "ledger": {"path": str(path), "events": len(events)},
        "activity": activity(events),
        "presence": presence(events, now=now),
        "notifications": notifications(events),
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ap.py live", description=__doc__)
    parser.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show", help="Summarize the live layer in the terminal.")
    sub.add_parser("view", help="Print the composed live read model as JSON.")
    sub.add_parser("activity", help="Print the activity projection as JSON.")
    sub.add_parser("presence", help="Print the presence projection as JSON.")
    sub.add_parser("notifications", help="Print the notification projection as JSON.")
    append_cmd = sub.add_parser("append", help="Append events from a JSON file, or -.")
    append_cmd.add_argument("path")

    args = parser.parse_args(argv)
    ledger = Path(args.ledger)

    try:
        if args.command == "append":
            text = sys.stdin.read() if args.path == "-" else Path(args.path).read_text(encoding="utf-8")
            document = json.loads(text)
            result = append(document if isinstance(document, list) else [document], ledger)
            print(f"appended {result['appended']}, duplicates {result['duplicates']}, "
                  f"rejected {len(result['rejected'])}")
            for item in result["rejected"]:
                for problem in item["problems"]:
                    print(f"  - {item['event_id']}: {problem}")
            return 1 if result["rejected"] else 0

        events = read_ledger(ledger)
        if args.command == "activity":
            print(json.dumps(activity(events), indent=2, ensure_ascii=False))
        elif args.command == "presence":
            print(json.dumps(presence(events), indent=2, ensure_ascii=False))
        elif args.command == "notifications":
            print(json.dumps(notifications(events), indent=2, ensure_ascii=False))
        elif args.command == "view":
            print(json.dumps(build_live_view(ledger), indent=2, ensure_ascii=False))
        else:
            view = build_live_view(ledger)
            live, notes = view["presence"], view["notifications"]
            print(f"LEDGER      {view['ledger']['events']} event(s)  ·  {ledger}")
            print(f"ACTIVITY    {view['activity']['total']} total  "
                  f"{view['activity']['by_severity'] or '{}'}")
            print(f"PRESENCE    {live['counts']['live']} live, "
                  f"{live['counts']['working']} working, "
                  f"{live['counts']['expired']} expired (ttl {live['ttl_seconds']}s)")
            print(f"BADGE       {notes['badge_count']} unread of {notes['counts']['total']} "
                  f"({notes['counts']['push']} push, {notes['counts']['immediate']} immediate)")
        return 0
    except (LedgerError, json.JSONDecodeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
