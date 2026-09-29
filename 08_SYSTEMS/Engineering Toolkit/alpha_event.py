#!/usr/bin/env python3
"""AlphaEvent v1 — the Foundation's normalized event contract.

Something happened. That is all an event asserts, and it is the whole reason
this contract exists: every provider the Foundation will ever integrate —
GitHub, Obsidian, Drive, Calendar, Notion, n8n, each reasoning engine — speaks
a different dialect about the same institutional fact. Without one normal form,
provider vocabulary leaks into the Council, the Memory and the interface, and
every new adapter becomes a change to all three.

So this module owns exactly one thing: **what a normalized event is**. It knows
nothing about webhooks, networks, databases or push providers. It validates,
normalizes and fingerprints. Everything provider-specific lives behind an
adapter (`event_adapters.py`); everything durable lives in the ledger
(`event_ledger.py`).

Three properties are load-bearing:

  * **`actor_id` resolves against the entity model.** An event produced by
    `CODEX` names `agent:cf-07`, not a string. That is why the entity registry
    had to exist first — an event whose actor is a free-text name cannot be
    joined to anything.
  * **Idempotency is structural.** A retried webhook must not create a second
    canonical event, so identity is derived from what happened rather than from
    when it was received.
  * **Severity is a delivery contract, not a mood.** `info` reaches the feed,
    `update` earns a badge, `action` and `critical` reach the Founder outside
    the application. Choosing a severity is choosing to interrupt someone.

Standard library only. No provider SDK reaches this layer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import uuid
from datetime import datetime, timezone
from typing import Any

SCHEMA_VERSION = "1.0"

# Delivery classes, in ascending order of how much of the Founder's attention
# they spend. The policy they imply is documented in `notification_policy`.
SEVERITIES = ("info", "update", "action", "critical")

# What an event is *about*. Deliberately small: a type earns its place when a
# real adapter produces it, never before.
ENTITY_TYPES = (
    "pull_request", "issue", "commit", "branch", "ci_run", "deployment",
    "document", "session", "mission", "decision", "presence", "system",
)

REQUIRED_FIELDS = (
    "schema_version", "event_id", "occurred_at", "received_at", "source",
    "event_type", "entity_type", "entity_id", "title", "severity",
    "requires_founder",
)

# `provider.noun.verb` — three or more dot-separated segments. The shape is
# enforced so a feed can group by provider and by noun without parsing prose.
EVENT_TYPE_RE = re.compile(r"^[a-z0-9]+(?:\.[a-z0-9_]+){2,}$")
SOURCE_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
ENTITY_ID_RE = re.compile(r"^[^\s].*$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$")


class EventError(Exception):
    """Raised when an event cannot be built from the values given."""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def parse_iso(value: str) -> datetime:
    """Parse an ISO-8601 instant, normalizing `Z` and naive values to UTC."""
    text = str(value or "").strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


# --------------------------------------------------------------------------
# identity
# --------------------------------------------------------------------------

def idempotency_key(event: dict[str, Any]) -> str:
    """A stable fingerprint of *what happened*, not of this delivery.

    A webhook retried three times is one institutional fact. The key therefore
    excludes `received_at` and `event_id`, which differ per delivery, and
    prefers the provider's own delivery identity when the adapter supplies one
    under `metadata.provider_event_id` — that is the only value the provider
    guarantees is stable across retries.
    """
    provider_id = str((event.get("metadata") or {}).get("provider_event_id") or "")
    parts = [
        str(event.get("source", "")),
        str(event.get("event_type", "")),
        str(event.get("entity_type", "")),
        str(event.get("entity_id", "")),
        provider_id or str(event.get("occurred_at", "")),
    ]
    return hashlib.sha256("\u0000".join(parts).encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------
# validation
# --------------------------------------------------------------------------

def validate(event: dict[str, Any]) -> list[str]:
    """Every reason this event is not a valid AlphaEvent, in reading order.

    Returns problems rather than raising so a batch can be reported whole. An
    adapter that emits ten malformed events should learn all ten at once.
    """
    problems: list[str] = []

    if not isinstance(event, dict):
        return ["event must be an object"]

    for field in REQUIRED_FIELDS:
        if event.get(field) in (None, ""):
            problems.append(f"missing required field: {field}")

    if event.get("schema_version") not in (None, SCHEMA_VERSION):
        problems.append(
            f"unsupported schema_version: {event.get('schema_version')!r} "
            f"(this build speaks {SCHEMA_VERSION})")

    severity = event.get("severity")
    if severity is not None and severity not in SEVERITIES:
        problems.append(f"severity must be one of {SEVERITIES}, got {severity!r}")

    entity_type = event.get("entity_type")
    if entity_type is not None and entity_type not in ENTITY_TYPES:
        problems.append(f"entity_type must be one of {ENTITY_TYPES}, got {entity_type!r}")

    source = event.get("source")
    if source and not SOURCE_RE.match(str(source)):
        problems.append(f"source must be a lowercase slug, got {source!r}")

    event_type = event.get("event_type")
    if event_type and not EVENT_TYPE_RE.match(str(event_type)):
        problems.append(
            f"event_type must look like provider.noun.verb, got {event_type!r}")

    if event_type and source and not str(event_type).startswith(f"{source}."):
        problems.append(
            f"event_type {event_type!r} must begin with its source {source!r}")

    for field in ("occurred_at", "received_at"):
        value = event.get(field)
        if value and not ISO_RE.match(str(value)):
            problems.append(f"{field} must be ISO-8601 with an offset, got {value!r}")

    occurred, received = event.get("occurred_at"), event.get("received_at")
    if occurred and received and ISO_RE.match(str(occurred)) and ISO_RE.match(str(received)):
        if parse_iso(received) < parse_iso(occurred):
            problems.append("received_at precedes occurred_at")

    entity_id = event.get("entity_id")
    if entity_id is not None and not ENTITY_ID_RE.match(str(entity_id)):
        problems.append("entity_id must not be blank or start with whitespace")

    if not isinstance(event.get("requires_founder", False), bool):
        problems.append("requires_founder must be a boolean")

    if event.get("metadata") is not None and not isinstance(event["metadata"], dict):
        problems.append("metadata must be an object")

    # An actor is optional — a CI run has no author — but when present it must
    # be an entity id, never a free-text name. This is the join that makes an
    # event navigable from the Council.
    actor = event.get("actor_id")
    if actor is not None and not re.match(r"^(agent|office|organization|person):[a-z0-9-]+$",
                                          str(actor)):
        problems.append(
            f"actor_id must be an entity id like 'agent:cf-07', got {actor!r}")

    # `critical` is the only severity that interrupts unconditionally. Pairing
    # it with requires_founder=False is almost always a mistake, and a silent
    # one, so it is rejected rather than tolerated.
    if severity == "critical" and event.get("requires_founder") is False:
        problems.append("a critical event must set requires_founder=true")

    return problems


def is_valid(event: dict[str, Any]) -> bool:
    return not validate(event)


# --------------------------------------------------------------------------
# construction
# --------------------------------------------------------------------------

def new_event(
    *,
    source: str,
    event_type: str,
    entity_type: str,
    entity_id: str,
    title: str,
    occurred_at: str | None = None,
    received_at: str | None = None,
    actor_id: str | None = None,
    department_id: str | None = None,
    summary: str = "",
    severity: str = "info",
    requires_founder: bool = False,
    correlation_id: str | None = None,
    causation_id: str | None = None,
    deep_link: str | None = None,
    metadata: dict[str, Any] | None = None,
    event_id: str | None = None,
) -> dict[str, Any]:
    """Build a validated AlphaEvent, or raise with every reason it is invalid."""
    occurred = occurred_at or now_iso()
    event: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "event_id": event_id or str(uuid.uuid4()),
        "occurred_at": occurred,
        "received_at": received_at or now_iso(),
        "source": source,
        "actor_id": actor_id,
        "department_id": department_id,
        "event_type": event_type,
        "entity_type": entity_type,
        "entity_id": str(entity_id),
        "title": title,
        "summary": summary,
        "severity": severity,
        "requires_founder": bool(requires_founder),
        "correlation_id": correlation_id,
        "causation_id": causation_id,
        "deep_link": deep_link,
        "metadata": dict(metadata or {}),
    }
    problems = validate(event)
    if problems:
        raise EventError("; ".join(problems))
    event["idempotency_key"] = idempotency_key(event)
    return event


# --------------------------------------------------------------------------
# delivery policy
# --------------------------------------------------------------------------

def notification_policy(event: dict[str, Any]) -> dict[str, bool]:
    """How far into the Founder's attention this event is allowed to reach.

    The badge counts *unread meaningful notifications*, not event volume — a
    hundred routine commits must not read as a hundred things to look at, or
    the badge stops meaning anything and gets ignored, which is the same
    failure the coherence ceiling was built to avoid.
    """
    severity = event.get("severity", "info")
    feed = True
    badge = severity in ("update", "action", "critical")
    push = severity in ("action", "critical") or bool(event.get("requires_founder"))
    immediate = severity == "critical"
    return {"feed": feed, "badge": badge, "push": push, "immediate": immediate}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ap.py event", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("schema", help="Print the AlphaEvent v1 contract.")
    check = sub.add_parser("validate", help="Validate an event document.")
    check.add_argument("path", help="Path to a JSON event, or - for stdin.")

    args = parser.parse_args(argv)

    if args.command == "schema":
        print(json.dumps({
            "schema_version": SCHEMA_VERSION,
            "required_fields": list(REQUIRED_FIELDS),
            "severities": list(SEVERITIES),
            "entity_types": list(ENTITY_TYPES),
            "event_type_pattern": EVENT_TYPE_RE.pattern,
            "actor_id": "entity id from the Institutional Node Taxonomy",
        }, indent=2))
        return 0

    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    try:
        document = json.loads(text)
    except json.JSONDecodeError as exc:
        print(f"error: not valid JSON: {exc}", file=sys.stderr)
        return 2

    events = document if isinstance(document, list) else [document]
    failed = 0
    for index, event in enumerate(events):
        problems = validate(event)
        if problems:
            failed += 1
            print(f"event[{index}] invalid:")
            for problem in problems:
                print(f"  - {problem}")
    if failed:
        print(f"\n{failed} of {len(events)} event(s) invalid.")
        return 1
    print(f"{len(events)} event(s) valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
