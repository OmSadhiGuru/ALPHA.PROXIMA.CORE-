#!/usr/bin/env python3
"""Adapter contract — the only place a provider's vocabulary is allowed to exist.

Every integration the Foundation will ever have follows one path:

    provider payload → adapter → validate → normalize → AlphaEvent → ledger

The adapter is the membrane. Above it, nothing knows what GitHub calls a pull
request or what Notion calls a page; below it, nothing knows what an AlphaEvent
is. Without that boundary, adding the twelfth integration means touching the
Council, the Memory and the interface — and the Foundation acquires eleven
reasons never to add the twelfth.

Two rules this module enforces rather than documents:

  * **Never claim `connected` without verification.** A status is a claim about
    the world, and an integration that reports `connected` while nothing is
    wired teaches the Founder to distrust every other status on the page. An
    adapter earns `connected` only by presenting evidence of a real exchange.
  * **Adapters are pure.** `normalize()` takes a payload and returns events. It
    opens no socket, reads no credential, and writes nothing. That is what makes
    the whole live layer testable with fixtures, offline, deterministically.

Networking, webhooks, credentials and provider SDKs belong to external
infrastructure. This file is the contract they must satisfy, not the place they
run.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Callable, Protocol

TOOLKIT_DIR = Path(__file__).resolve().parent


def _load_sibling(filename: str, name: str):
    path = (TOOLKIT_DIR / filename).resolve()
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


alpha_event = _load_sibling("alpha_event.py", "adapters_alpha_event")

SCHEMA_VERSION = "1.0"

# An integration's honest relationship with reality.
#
#   connected    — verified exchange with the provider, evidenced
#   degraded     — reachable but impaired; some events may be missing
#   disconnected — was connected, is not now
#   planned      — contract written, adapter not implemented
#   blocked      — implementation prevented by a decision or a missing credential
STATUSES = ("connected", "degraded", "disconnected", "planned", "blocked")

# Statuses that assert the provider is actually reachable. Claiming one of these
# requires evidence; the registry refuses it otherwise.
LIVE_STATUSES = ("connected", "degraded")


class AdapterError(Exception):
    """Raised when an adapter or its registration is malformed."""


class Adapter(Protocol):
    """What every provider integration must present.

    `source` is the slug that prefixes every event type it emits, so
    `github.pr.merged` can only come from the adapter whose source is `github`.
    """

    source: str
    event_types: tuple[str, ...]

    def normalize(self, payload: dict[str, Any]) -> list[dict[str, Any]]:
        """Provider payload to zero or more AlphaEvents. Pure; never I/O."""
        ...


# --------------------------------------------------------------------------
# registration
# --------------------------------------------------------------------------

def adapter_record(
    source: str,
    label: str,
    *,
    status: str = "planned",
    event_types: tuple[str, ...] | list[str] = (),
    normalize: Callable[[dict[str, Any]], list[dict[str, Any]]] | None = None,
    evidence: str | None = None,
    note: str = "",
) -> dict[str, Any]:
    """One integration's declared contract and honest status."""
    if status not in STATUSES:
        raise AdapterError(f"status must be one of {STATUSES}, got {status!r}")
    if not alpha_event.SOURCE_RE.match(source):
        raise AdapterError(f"source must be a lowercase slug, got {source!r}")
    if status in LIVE_STATUSES and not evidence:
        raise AdapterError(
            f"{source}: status {status!r} asserts the provider is reachable, so it "
            f"requires evidence of a verified exchange. Never claim connected "
            f"without verification.")
    for event_type in event_types:
        if not alpha_event.EVENT_TYPE_RE.match(event_type):
            raise AdapterError(f"{source}: malformed event_type {event_type!r}")
        if not event_type.startswith(f"{source}."):
            raise AdapterError(
                f"{source}: event_type {event_type!r} does not belong to this source")
    if status != "planned" and normalize is None:
        raise AdapterError(
            f"{source}: status {status!r} claims an implementation, but no "
            f"normalize() was supplied")
    return {
        "source": source,
        "label": label,
        "status": status,
        "event_types": sorted(event_types),
        "implemented": normalize is not None,
        "evidence": evidence,
        "note": note,
        "_normalize": normalize,
    }


# The integrations the Foundation intends to have. Every one is `planned` until
# an adapter exists and a real exchange has been observed — the registry is a
# statement of intent plus current truth, never a wish presented as a fact.
_DECLARED: tuple[tuple[str, str, str], ...] = (
    ("github", "GitHub", "Repository, review and CI activity."),
    ("codex", "CODEX", "Engineering intelligence session signals."),
    ("claude", "Claude", "Reasoning session signals."),
    ("lumiaion", "LUMIAION", "Orchestration and routing signals."),
    ("gemini", "Gemini", "Educational intelligence session signals."),
    ("perplexity", "Perplexity", "Research intelligence session signals."),
    ("pocket_ai", "Pocket AI", "Mobile capture signals."),
    ("obsidian", "Obsidian", "Vault edit and sync signals."),
    ("google_drive", "Google Drive", "Document change signals."),
    ("google_calendar", "Google Calendar", "Schedule signals."),
    ("notion", "Notion", "Project and task signals."),
    ("n8n", "n8n", "Workflow automation signals."),
)


def build_registry(
    overrides: dict[str, dict[str, Any]] | None = None
) -> dict[str, Any]:
    """The adapter registry: every declared integration and its current truth.

    `overrides` lets a real adapter replace its own declaration once it exists,
    which is how Phase D will register GitHub without this file becoming a
    dumping ground for provider logic.
    """
    overrides = overrides or {}
    adapters: list[dict[str, Any]] = []
    for source, label, note in _DECLARED:
        override = overrides.get(source)
        if override:
            adapters.append(adapter_record(source, override.get("label", label),
                                           status=override.get("status", "planned"),
                                           event_types=override.get("event_types", ()),
                                           normalize=override.get("normalize"),
                                           evidence=override.get("evidence"),
                                           note=override.get("note", note)))
        else:
            adapters.append(adapter_record(source, label, status="planned", note=note))

    unknown = set(overrides) - {source for source, _, _ in _DECLARED}
    if unknown:
        raise AdapterError(
            f"override for undeclared source(s): {sorted(unknown)}. Declare the "
            f"integration before registering an adapter for it.")

    by_status: dict[str, int] = {}
    for item in adapters:
        by_status[item["status"]] = by_status.get(item["status"], 0) + 1

    return {
        "schema_version": SCHEMA_VERSION,
        "adapters": adapters,
        "counts": {
            "total": len(adapters),
            "implemented": sum(1 for a in adapters if a["implemented"]),
            "by_status": by_status,
        },
    }


def get(registry: dict[str, Any], source: str) -> dict[str, Any]:
    for item in registry["adapters"]:
        if item["source"] == source:
            return item
    raise AdapterError(f"no adapter registered for source: {source!r}")


# --------------------------------------------------------------------------
# ingestion
# --------------------------------------------------------------------------

def ingest(
    registry: dict[str, Any], source: str, payload: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[str]]:
    """Run one payload through its adapter and validate what comes out.

    Returns `(events, problems)`. A malformed payload yields no events and every
    reason why — an adapter is not trusted to police itself, because the whole
    value of a normal form is that something downstream checks it.
    """
    record = get(registry, source)
    normalize = record.get("_normalize")
    if normalize is None:
        return [], [f"{source}: adapter is {record['status']}, not implemented"]

    try:
        produced = normalize(payload)
    except Exception as exc:  # an adapter must never take the ledger down with it
        return [], [f"{source}: adapter raised {type(exc).__name__}: {exc}"]

    if not isinstance(produced, list):
        return [], [f"{source}: normalize() must return a list, got {type(produced).__name__}"]

    events: list[dict[str, Any]] = []
    problems: list[str] = []
    for index, event in enumerate(produced):
        reasons = alpha_event.validate(event)
        if str(event.get("source")) != source:
            reasons.append(f"event source {event.get('source')!r} does not match adapter {source!r}")
        if reasons:
            problems.extend(f"{source}[{index}]: {reason}" for reason in reasons)
            continue
        event.setdefault("idempotency_key", alpha_event.idempotency_key(event))
        events.append(event)
    return events, problems


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ap.py adapters", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("view", help="Print the adapter registry as JSON.")
    sub.add_parser("check", help="Print integration statuses.")

    args = parser.parse_args(argv)
    try:
        registry = build_registry()
    except AdapterError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.command == "view":
        printable = {**registry, "adapters": [
            {k: v for k, v in a.items() if k != "_normalize"} for a in registry["adapters"]]}
        print(json.dumps(printable, indent=2, ensure_ascii=False))
        return 0

    counts = registry["counts"]
    print(f"Adapters: {counts['total']} declared, {counts['implemented']} implemented")
    for status in STATUSES:
        total = counts["by_status"].get(status, 0)
        if total:
            print(f"  {status:<14} {total}")
    print()
    for item in registry["adapters"]:
        mark = "·" if item["status"] == "planned" else "!"
        print(f"  {mark} {item['source']:<18} {item['status']:<14} {item['note']}")
    print("\nNo integration reports connected. None has been verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
