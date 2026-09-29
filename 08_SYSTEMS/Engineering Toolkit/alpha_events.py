#!/usr/bin/env python3
"""AlphaEvent v1 — the Foundation's provider-independent event contract.

Every external system that will ever report activity to Alpha Proxima reports
it in exactly one shape. This module is that shape, plus the three operations
the shape needs to be trustworthy: validation, deduplication, and an
append-only ledger.

## Why this exists as its own module

The Foundation already has a read model (`alpha_app.build_app_view`) and a
canonical store (Markdown, plus `founder-state.json` behind its single
writer). What it did not have was a way for something *outside* the repository
to say "this happened" without either of those being touched.

This module is that boundary, and it is deliberately narrow:

  * **An AlphaEvent is an observation, never an instruction.** Appending one
    changes no priority, no decision, no blocker, no note. Interpretation is
    a later, separate, approved step — `alpha_live.py` projects, and only the
    existing single writer mutates Founder state.
  * **Provider vocabulary stops here.** A GitHub payload's `pull_request.
    merged_at`, a Notion `page_id`, an n8n `executionId` — each is normalized
    by its adapter into these fields, or rejected. Nothing downstream ever
    learns a provider's field names.
  * **The ledger is append-only.** A historical event is never edited to make
    an interface look right. Presentation state that needs to change (read,
    dismissed, expired) lives in the projections, not in the record of what
    happened.

## Canonical truth is elsewhere

Nothing in this module is constitutional truth. The ledger is an operational
transport record: an honest log of what external systems reported, with
provenance. If the whole ledger were deleted, the Foundation would lose its
recent activity feed and lose nothing institutional. That asymmetry is the
design, not an accident of it.

Standard library only, like every sibling in this toolkit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
LIVE_DIR = VAULT_ROOT / "13_OPERATIONS" / "Live Integration Layer"
DEFAULT_LEDGER = LIVE_DIR / "state" / "event-ledger.jsonl"
FIXTURE_DIR = LIVE_DIR / "fixtures"

SCHEMA_VERSION = "1.0"

# Severity is the whole notification policy in one field. It is ordered, and
# the order is load-bearing: `alpha_live.evaluate_notification` reads it to
# decide feed / badge / push, so a new value cannot be added here without
# deciding what it costs the Founder's attention.
SEVERITIES = ("info", "update", "action", "critical")
SEVERITY_RANK = {name: index for index, name in enumerate(SEVERITIES)}

# Every provider the Live Integration Layer is designed to accept. A source
# outside this set is rejected at the boundary rather than quietly stored:
# an unknown provider means an adapter nobody reviewed.
SOURCES = (
    "github",
    "chatgpt",
    "codex",
    "claude",
    "gemini",
    "perplexity",
    "pocket_ai",
    "obsidian",
    "google_drive",
    "google_calendar",
    "notion",
    "n8n",
    "alpha_proxima",
)

# Entity kinds a normalized event may describe. Adapters map provider nouns
# onto these; they never introduce their own.
ENTITY_TYPES = (
    "repository", "commit", "branch", "pull_request", "review", "check_run",
    "workflow_run", "deployment", "issue", "document", "note", "file",
    "calendar_event", "page", "database_row", "workflow_execution",
    "conversation", "capture", "agent", "mission", "system",
)

# `domain.object.verb`, lowercase, dot-separated. The taxonomy is a naming
# rule rather than a fixed list so a new provider does not require editing
# this module — but the rule is enforced, so `PR_MERGED!!` never lands.
EVENT_TYPE_RE = re.compile(r"^[a-z0-9]+(?:[._][a-z0-9]+)+$")
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/#@+-]{0,127}$")

REQUIRED_FIELDS = (
    "schema_version", "event_id", "occurred_at", "received_at", "source",
    "actor", "department", "event_type", "entity_type", "entity_id",
    "title", "summary", "severity", "requires_founder", "deep_link",
    "correlation_id", "causation_id", "metadata",
)

# Departments the Foundation actually has, plus the unattributed case. An
# event whose department cannot be established says so; it does not guess.
DEPARTMENTS = (
    "ENGINEERING", "RESEARCH", "EXECUTIVE", "KNOWLEDGE", "MEMORY",
    "OPERATIONS", "FINANCE", "HEALTH", "UNATTRIBUTED",
)

MAX_TITLE = 200
MAX_SUMMARY = 1000
# A bounded metadata payload keeps a chatty provider from turning the ledger
# into a copy of its own database. Adapters summarize; they do not mirror.
MAX_METADATA_BYTES = 8192


class EventError(Exception):
    """Raised when an event cannot be built, validated, or stored."""


# --------------------------------------------------------------------------
# time
# --------------------------------------------------------------------------

def now_iso() -> str:
    """UTC, second precision — the same format every sibling module emits."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def parse_iso(value: str) -> datetime:
    """Parse an ISO-8601 instant, accepting the `Z` suffix providers send.

    A naive timestamp is read as UTC rather than rejected: providers are
    inconsistent about offsets, and refusing the event would lose the
    observation over a formatting detail. The assumption is recorded here so
    it is a decision rather than a silent coercion.
    """
    text = value.strip()
    if text.endswith(("Z", "z")):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError as exc:
        raise EventError(f"Not an ISO-8601 instant: {value!r}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


# --------------------------------------------------------------------------
# construction
# --------------------------------------------------------------------------

def make_event(
    *,
    source: str,
    actor: str,
    department: str,
    event_type: str,
    entity_type: str,
    entity_id: str,
    title: str,
    summary: str = "",
    severity: str = "info",
    requires_founder: bool = False,
    deep_link: str = "",
    occurred_at: str | None = None,
    received_at: str | None = None,
    event_id: str | None = None,
    correlation_id: str | None = None,
    causation_id: str | None = None,
    provider_event_id: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build one AlphaEvent, then validate it. An invalid event is not returned.

    `provider_event_id` is kept in `metadata` rather than promoted to a field:
    it is the one piece of provider vocabulary the contract must retain (for
    deduplication), and keeping it in metadata means no consumer can mistake
    it for an Alpha Proxima identifier.
    """
    payload = dict(metadata or {})
    if provider_event_id is not None:
        payload["provider_event_id"] = str(provider_event_id)
    occurred = occurred_at or now_iso()
    event = {
        "schema_version": SCHEMA_VERSION,
        "event_id": event_id or str(uuid.uuid4()),
        "occurred_at": occurred,
        "received_at": received_at or now_iso(),
        "source": source,
        "actor": actor,
        "department": department,
        "event_type": event_type,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "title": title,
        "summary": summary,
        "severity": severity,
        "requires_founder": bool(requires_founder),
        "deep_link": deep_link,
        # An event with no explicit correlation is its own correlation root:
        # a single-step observation is a one-event workflow, not a null one.
        "correlation_id": correlation_id or (event_id or ""),
        "causation_id": causation_id or "",
        "metadata": payload,
    }
    if not event["correlation_id"]:
        event["correlation_id"] = event["event_id"]
    errors = validate(event)
    if errors:
        raise EventError("; ".join(errors))
    return event


# --------------------------------------------------------------------------
# validation
# --------------------------------------------------------------------------

def validate(event: Any) -> list[str]:
    """Every reason this object is not an AlphaEvent v1, as plain sentences.

    Returns all failures rather than the first, so an adapter author fixes one
    payload mapping in one pass instead of discovering faults one run at a
    time. An empty list means the event may enter canonical processing.
    """
    errors: list[str] = []
    if not isinstance(event, dict):
        return [f"Event must be a JSON object, got {type(event).__name__}."]

    for field in REQUIRED_FIELDS:
        if field not in event:
            errors.append(f"Missing required field: {field}.")
    extra = sorted(set(event) - set(REQUIRED_FIELDS))
    if extra:
        errors.append(
            "Unknown field(s) not in AlphaEvent v1: "
            + ", ".join(extra)
            + ". Provider-specific data belongs in metadata."
        )
    if errors and any(f.startswith("Missing") for f in errors):
        return errors

    version = event["schema_version"]
    if version != SCHEMA_VERSION:
        errors.append(
            f"Unsupported schema_version {version!r}; this Foundation speaks {SCHEMA_VERSION!r}."
        )

    for field in ("event_id", "entity_id", "correlation_id"):
        value = event[field]
        if not isinstance(value, str) or not ID_RE.match(value):
            errors.append(f"{field} must be a short printable identifier, got {value!r}.")
    causation = event["causation_id"]
    if not isinstance(causation, str) or (causation and not ID_RE.match(causation)):
        errors.append(f"causation_id must be empty or an identifier, got {causation!r}.")

    for field in ("occurred_at", "received_at"):
        value = event[field]
        if not isinstance(value, str):
            errors.append(f"{field} must be an ISO-8601 string, got {type(value).__name__}.")
            continue
        try:
            parse_iso(value)
        except EventError as exc:
            errors.append(f"{field}: {exc}")

    if event["source"] not in SOURCES:
        errors.append(
            f"Unknown source {event['source']!r}. Registered sources: {', '.join(SOURCES)}."
        )
    if event["department"] not in DEPARTMENTS:
        errors.append(
            f"Unknown department {event['department']!r}. "
            "Use UNATTRIBUTED rather than inventing one."
        )
    if event["severity"] not in SEVERITIES:
        errors.append(
            f"Unknown severity {event['severity']!r}. One of: {', '.join(SEVERITIES)}."
        )
    if event["entity_type"] not in ENTITY_TYPES:
        errors.append(
            f"Unknown entity_type {event['entity_type']!r}. One of: {', '.join(ENTITY_TYPES)}."
        )
    event_type = event["event_type"]
    if not isinstance(event_type, str) or not EVENT_TYPE_RE.match(event_type):
        errors.append(
            f"event_type must be lowercase dotted, like 'github.pr.opened', got {event_type!r}."
        )

    actor = event["actor"]
    if not isinstance(actor, str) or not actor.strip():
        errors.append("actor must name who or what acted; an anonymous event has no provenance.")

    title = event["title"]
    if not isinstance(title, str) or not title.strip():
        errors.append("title must be a non-empty string.")
    elif len(title) > MAX_TITLE:
        errors.append(f"title exceeds {MAX_TITLE} characters ({len(title)}).")
    summary = event["summary"]
    if not isinstance(summary, str):
        errors.append("summary must be a string (empty is allowed).")
    elif len(summary) > MAX_SUMMARY:
        errors.append(f"summary exceeds {MAX_SUMMARY} characters ({len(summary)}).")

    if not isinstance(event["requires_founder"], bool):
        errors.append("requires_founder must be a boolean, not a truthy value.")

    deep_link = event["deep_link"]
    if not isinstance(deep_link, str):
        errors.append("deep_link must be a string (empty is allowed).")
    elif deep_link:
        errors.extend(validate_deep_link(deep_link))

    metadata = event["metadata"]
    if not isinstance(metadata, dict):
        errors.append("metadata must be a JSON object.")
    else:
        try:
            encoded = json.dumps(metadata, ensure_ascii=False).encode("utf-8")
        except (TypeError, ValueError):
            errors.append("metadata must be JSON-serializable.")
        else:
            if len(encoded) > MAX_METADATA_BYTES:
                errors.append(
                    f"metadata exceeds {MAX_METADATA_BYTES} bytes ({len(encoded)}); "
                    "adapters summarize provider payloads, they do not mirror them."
                )
        errors.extend(secret_leaks(metadata))

    return errors


# Keys whose values must never reach the ledger. The ledger is served to
# interfaces; a token that lands here is a token published. Checked by name
# because that is what an adapter author actually gets wrong — copying a
# provider payload wholesale into metadata.
SECRET_KEY_RE = re.compile(
    r"(token|secret|password|passwd|credential|api[_-]?key|private[_-]?key|"
    r"authorization|access[_-]?key|bearer|signature|session[_-]?id|cookie)",
    re.IGNORECASE,
)


def secret_leaks(value: Any, path: str = "metadata") -> list[str]:
    """Every place a credential-shaped key appears, however deeply nested."""
    found: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            here = f"{path}.{key}"
            if isinstance(key, str) and SECRET_KEY_RE.search(key):
                found.append(
                    f"{here} looks like a credential. Secrets never enter the event ledger."
                )
            found.extend(secret_leaks(item, here))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(secret_leaks(item, f"{path}[{index}]"))
    return found


def is_valid(event: Any) -> bool:
    return not validate(event)


# --------------------------------------------------------------------------
# deep links
# --------------------------------------------------------------------------

DEEP_LINK_SCHEME = "alpha-proxima"
# Deep-link targets the interface knows how to open. A link to anything else
# is a dead end dressed as navigation, so it is a validation failure.
DEEP_LINK_ROOTS = ("memory", "council", "operate", "know", "github", "activity", "system")
DEEP_LINK_RE = re.compile(rf"^{DEEP_LINK_SCHEME}://([a-z]+)(/[A-Za-z0-9._:/#@+-]*)?$")
FRAGMENT_RE = re.compile(r"^#[A-Za-z0-9._:/#@+-]*$")


def validate_deep_link(link: str) -> list[str]:
    """A deep link is either an in-page fragment or an `alpha-proxima://` target."""
    if FRAGMENT_RE.match(link):
        return []
    match = DEEP_LINK_RE.match(link)
    if not match:
        return [
            f"deep_link {link!r} is neither a '#fragment' nor "
            f"'{DEEP_LINK_SCHEME}://<root>/<path>'."
        ]
    root = match.group(1)
    if root not in DEEP_LINK_ROOTS:
        return [
            f"deep_link root {root!r} is not a navigable surface. "
            f"One of: {', '.join(DEEP_LINK_ROOTS)}."
        ]
    return []


def deep_link(root: str, *parts: str) -> str:
    """Build a native deep link, refusing a root the interface cannot open."""
    if root not in DEEP_LINK_ROOTS:
        raise EventError(f"Unknown deep-link root {root!r}.")
    trail = "/".join(str(part).strip("/") for part in parts if str(part).strip("/"))
    return f"{DEEP_LINK_SCHEME}://{root}" + (f"/{trail}" if trail else "")


def web_deep_link(link: str, base: str = "") -> str:
    """The PWA equivalent of a native deep link, for platforms without schemes.

    `alpha-proxima://council/agent/CODEX` becomes `#council/agent/CODEX`, which
    the rendered single-page app can route on with no native handler
    registered. A fragment passes through unchanged — it is already portable.
    """
    if FRAGMENT_RE.match(link):
        return (base.rstrip("/") + "/" + link) if base else link
    match = DEEP_LINK_RE.match(link)
    if not match:
        raise EventError(f"Cannot convert {link!r}: not an Alpha Proxima deep link.")
    root, rest = match.group(1), (match.group(2) or "")
    fragment = "#" + root + rest
    return (base.rstrip("/") + "/" + fragment) if base else fragment


# --------------------------------------------------------------------------
# deduplication
# --------------------------------------------------------------------------

def dedup_key(event: dict[str, Any]) -> str:
    """The identity of an *occurrence*, not of a delivery.

    Providers retry webhooks; the same push can arrive three times. The key is
    provider + provider's own identifier + event type, because that triple is
    what the provider itself considers one thing happening once.

    When a provider sends no identifier of its own, the key falls back to the
    event's semantic content — source, type, entity, and the instant it
    occurred. That is weaker (two genuinely distinct events in the same second
    on the same entity collapse), and the fallback is marked in the key so an
    operator reading the ledger can see which guarantee applied.
    """
    provider_id = str(event.get("metadata", {}).get("provider_event_id") or "")
    if provider_id:
        material = f"provider|{event['source']}|{provider_id}|{event['event_type']}"
    else:
        material = (
            f"derived|{event['source']}|{event['event_type']}|{event['entity_type']}"
            f"|{event['entity_id']}|{parse_iso(event['occurred_at']).isoformat()}"
        )
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()[:32]
    kind = "p" if provider_id else "d"
    return f"{kind}:{digest}"


# --------------------------------------------------------------------------
# ordering and chains
# --------------------------------------------------------------------------

def sort_events(events: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Chronological by when it happened, then by when we heard, then by id.

    Arrival order is not occurrence order — a provider outage delivers an hour
    of history at once. `received_at` breaks ties because two things that
    occurred in the same second are best ordered by what we learned first, and
    `event_id` breaks the remaining tie so the sort is total and stable across
    runs rather than dependent on input order.
    """
    return sorted(
        events,
        key=lambda e: (parse_iso(e["occurred_at"]), parse_iso(e["received_at"]), e["event_id"]),
    )


def causation_chain(events: Iterable[dict[str, Any]], event_id: str) -> list[dict[str, Any]]:
    """Walk from a root cause to the named event, oldest first.

    A cycle — which means a buggy adapter, since causation is by definition
    backwards in time — terminates the walk instead of hanging.
    """
    by_id = {e["event_id"]: e for e in events}
    chain: list[dict[str, Any]] = []
    seen: set[str] = set()
    current = event_id
    while current and current in by_id and current not in seen:
        seen.add(current)
        event = by_id[current]
        chain.append(event)
        current = event.get("causation_id") or ""
    chain.reverse()
    return chain


def correlation_group(events: Iterable[dict[str, Any]], correlation_id: str) -> list[dict[str, Any]]:
    """Every event belonging to one mission or workflow, in occurrence order."""
    return sort_events([e for e in events if e.get("correlation_id") == correlation_id])


# --------------------------------------------------------------------------
# the append-only ledger
# --------------------------------------------------------------------------

class EventLedger:
    """An append-only JSONL log with an in-memory idempotency index.

    JSONL rather than a single JSON array so appending is one `write` that
    cannot corrupt what is already on disk, and so a partially written final
    line is recoverable by discarding exactly that line.

    This class deliberately offers no update and no delete. A projection that
    needs mutable state (read, dismissed, expired) keeps its own; the record of
    what an external system reported is not editable by the thing displaying
    it.
    """

    def __init__(self, path: Path | str = DEFAULT_LEDGER) -> None:
        self.path = Path(path)
        self._keys: set[str] | None = None

    # -- reading ---------------------------------------------------------
    def __iter__(self) -> Iterator[dict[str, Any]]:
        """Yield every well-formed record, skipping a torn trailing line.

        A malformed line is skipped rather than raised on: a truncated last
        write must not make the entire activity history unreadable. `repair()`
        reports what was skipped.
        """
        if not self.path.exists():
            return
        with self.path.open("r", encoding="utf-8") as stream:
            for line in stream:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(record, dict):
                    yield record

    def read_all(self) -> list[dict[str, Any]]:
        return list(self)

    def events(self) -> list[dict[str, Any]]:
        """Every stored event, in occurrence order."""
        return sort_events(self.read_all())

    def damaged_lines(self) -> list[int]:
        """1-based line numbers that are not parseable JSON objects."""
        if not self.path.exists():
            return []
        bad: list[int] = []
        with self.path.open("r", encoding="utf-8") as stream:
            for number, line in enumerate(stream, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    record = json.loads(stripped)
                except json.JSONDecodeError:
                    bad.append(number)
                    continue
                if not isinstance(record, dict):
                    bad.append(number)
        return bad

    # -- idempotency -----------------------------------------------------
    def keys(self) -> set[str]:
        if self._keys is None:
            keys: set[str] = set()
            for record in self:
                try:
                    keys.add(dedup_key(record))
                except (EventError, KeyError):
                    continue
            self._keys = keys
        return self._keys

    def contains(self, event: dict[str, Any]) -> bool:
        return dedup_key(event) in self.keys()

    # -- writing ---------------------------------------------------------
    def append(self, event: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
        """Append one validated event unless its occurrence is already stored.

        Returns `(stored, event)`. A duplicate is not an error — it is the
        normal result of a provider retry, and treating it as a failure would
        make every adapter's retry path noisy for no reason.
        """
        errors = validate(event)
        if errors:
            raise EventError("Refusing to store an invalid event: " + "; ".join(errors))
        if self.contains(event):
            return False, event
        self.path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n"
        # Opened per append and fsynced: an event that a provider will never
        # resend must survive the process that received it.
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write(line)
            stream.flush()
            os.fsync(stream.fileno())
        if self._keys is not None:
            self._keys.add(dedup_key(event))
        return True, event

    def extend(self, events: Iterable[dict[str, Any]]) -> dict[str, int]:
        """Append a batch, reporting how many were new and how many were retries."""
        stored = duplicates = 0
        for event in events:
            was_new, _ = self.append(event)
            if was_new:
                stored += 1
            else:
                duplicates += 1
        return {"stored": stored, "duplicates": duplicates}

    def repair(self) -> dict[str, Any]:
        """Rewrite the ledger with only its well-formed records.

        This drops damaged lines, which is a loss — so it reports exactly what
        it dropped, and it is never called automatically. Recovering a torn
        write is an operator's decision.
        """
        if not self.path.exists():
            return {"removed": 0, "kept": 0, "lines": []}
        damaged = self.damaged_lines()
        kept = self.read_all()
        descriptor, temporary = tempfile.mkstemp(
            prefix=f".{self.path.name}.", suffix=".tmp", dir=self.path.parent
        )
        scratch = Path(temporary)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                for record in kept:
                    stream.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(scratch, self.path)
        finally:
            if scratch.exists():
                scratch.unlink()
        self._keys = None
        return {"removed": len(damaged), "kept": len(kept), "lines": damaged}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _load_json_argument(value: str) -> Any:
    """Read JSON from a file path, from `-` for stdin, or from a literal."""
    if value == "-":
        return json.loads(sys.stdin.read())
    path = Path(value)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return json.loads(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ap.py events", description=__doc__)
    parser.add_argument("--ledger", default=str(DEFAULT_LEDGER), help="Path to the event ledger (JSONL).")

    sub = parser.add_subparsers(dest="command", required=True)

    contract = sub.add_parser("contract", help="Print the AlphaEvent v1 contract as JSON.")
    contract.set_defaults(handler="contract")

    check = sub.add_parser("validate", help="Validate an event or a list of events.")
    check.add_argument("payload", help="JSON file path, '-' for stdin, or a JSON literal.")

    show = sub.add_parser("list", help="Print stored events, newest last.")
    show.add_argument("--limit", type=int, default=0, help="Show only the most recent N events.")
    show.add_argument("--source", default="", help="Filter to one provider.")
    show.add_argument("--severity", default="", help="Show this severity and above.")

    append = sub.add_parser("append", help="Append an event (or list) to the ledger.")
    append.add_argument("payload", help="JSON file path, '-' for stdin, or a JSON literal.")
    append.add_argument("--dry-run", action="store_true",
                        help="Validate and report what would be stored; write nothing.")

    chain = sub.add_parser("chain", help="Show the causation chain leading to one event.")
    chain.add_argument("event_id")

    group = sub.add_parser("correlation", help="Show every event in one mission or workflow.")
    group.add_argument("correlation_id")

    sub.add_parser("repair", help="Rewrite the ledger without its damaged lines.")
    return parser


def _contract() -> dict[str, Any]:
    return {
        "name": "AlphaEvent",
        "schema_version": SCHEMA_VERSION,
        "required_fields": list(REQUIRED_FIELDS),
        "severities": list(SEVERITIES),
        "sources": list(SOURCES),
        "departments": list(DEPARTMENTS),
        "entity_types": list(ENTITY_TYPES),
        "event_type_pattern": EVENT_TYPE_RE.pattern,
        "deep_link_scheme": DEEP_LINK_SCHEME,
        "deep_link_roots": list(DEEP_LINK_ROOTS),
        "deduplication": "source + metadata.provider_event_id + event_type (sha256, truncated)",
        "limits": {
            "title": MAX_TITLE,
            "summary": MAX_SUMMARY,
            "metadata_bytes": MAX_METADATA_BYTES,
        },
        "canonical_truth": "Markdown vault and founder-state.json; this ledger is transport.",
    }


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    ledger = EventLedger(args.ledger)

    try:
        if args.command == "contract":
            print(json.dumps(_contract(), indent=2, ensure_ascii=False))
            return 0

        if args.command == "validate":
            payload = _load_json_argument(args.payload)
            batch = payload if isinstance(payload, list) else [payload]
            failures = 0
            for index, event in enumerate(batch):
                errors = validate(event)
                label = event.get("event_id", f"#{index}") if isinstance(event, dict) else f"#{index}"
                if errors:
                    failures += 1
                    print(f"INVALID {label}", file=sys.stderr)
                    for error in errors:
                        print(f"  - {error}", file=sys.stderr)
                else:
                    print(f"valid   {label}  {event['event_type']}")
            if failures:
                print(f"\n{failures} of {len(batch)} event(s) invalid.", file=sys.stderr)
                return 1
            print(f"\n{len(batch)} event(s) valid against AlphaEvent v{SCHEMA_VERSION}.")
            return 0

        if args.command == "append":
            payload = _load_json_argument(args.payload)
            batch = payload if isinstance(payload, list) else [payload]
            if args.dry_run:
                new = sum(1 for event in batch if not validate(event) and not ledger.contains(event))
                print(f"dry-run: {new} new, {len(batch) - new} duplicate or invalid; nothing written.")
                return 0
            result = ledger.extend(batch)
            print(f"stored {result['stored']}, {result['duplicates']} duplicate(s) ignored.")
            return 0

        if args.command == "list":
            events = ledger.events()
            if args.source:
                events = [e for e in events if e["source"] == args.source]
            if args.severity:
                if args.severity not in SEVERITY_RANK:
                    print(f"error: unknown severity {args.severity!r}", file=sys.stderr)
                    return 2
                floor = SEVERITY_RANK[args.severity]
                events = [e for e in events if SEVERITY_RANK.get(e["severity"], 0) >= floor]
            if args.limit > 0:
                events = events[-args.limit:]
            print(json.dumps(events, indent=2, ensure_ascii=False))
            return 0

        if args.command == "chain":
            chain = causation_chain(ledger.read_all(), args.event_id)
            if not chain:
                print(f"error: no event {args.event_id!r} in the ledger", file=sys.stderr)
                return 1
            print(json.dumps(chain, indent=2, ensure_ascii=False))
            return 0

        if args.command == "correlation":
            print(json.dumps(correlation_group(ledger.read_all(), args.correlation_id),
                             indent=2, ensure_ascii=False))
            return 0

        if args.command == "repair":
            result = ledger.repair()
            print(f"kept {result['kept']} record(s); removed {result['removed']} damaged line(s).")
            if result["lines"]:
                print("damaged lines: " + ", ".join(str(n) for n in result["lines"]))
            return 0
    except (EventError, json.JSONDecodeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
