#!/usr/bin/env python3
"""ContextItem v1 — the normal form for a capture, before it means anything.

A capture is something the Founder said, recorded, or that a device produced:
an Omi memory, a Pocket AI transcript, a voice note. It is raw. It has not been
decided, filed, or made institutional, and most of it never will be.

Two adapters in this toolkit already cite this contract as the reason they
cannot exist — `pocket_ai` and Founder OS's `OMI` both say they "depend on the
same ContextItem contract". This is that contract.

## The body never enters the ledger

This is the load-bearing rule, and it is enforced rather than documented.

A ContextItem carries **a reference and its shape** — when it happened, how
long it was, which provider holds it, what category the provider assigned, and
a short title. It does **not** carry the transcript, the memory text, or any
other content. Those stay in the provider.

The reason is concrete. A survey of the Founder's Omi account found that of 200
durable memories scanned, **zero** were unmarked for sensitivity: the corpus is
essentially all personal. The event ledger is git-ignored, but "git-ignored" is
a property of one checkout, not a guarantee about every machine that will ever
hold one. A pipeline that moves personal content out of the provider and into
a file on disk has made a privacy decision on the Founder's behalf, and this
contract declines to make it.

So the Foundation learns *that* a capture happened, when, and roughly about
what. To read it, you open Omi. That is a smaller capability than a full sync,
and it is the one that can be granted without a governance conversation.

## A capture is a proposal, never a record

Nothing here writes Markdown. A ContextItem becomes an AlphaEvent, which
appears in activity and — if it asks for attention — in notifications.
Promoting one into the vault is a Founder act, performed by a human who has
read it. The single-writer model is not bent for convenience.

`suggested_kind` exists for that promotion: an adapter may say "this looks like
a task", and that is a suggestion addressed to a person, never a classification
the Foundation acts on by itself.

Standard library only, like every sibling in this toolkit.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent


def _load_sibling(filename: str, name: str):
    import importlib.util
    path = (TOOLKIT_DIR / filename).resolve()
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ev = _load_sibling("alpha_events.py", "context_alpha_events")

SCHEMA_VERSION = "1.0"

# What kind of thing was captured. Provider nouns map onto these; a provider
# never introduces its own, for the same reason `ENTITY_TYPES` is closed.
CAPTURE_KINDS = (
    "memory",        # a durable fact the provider has distilled
    "conversation",  # a recorded exchange
    "transcript",    # speech rendered to text
    "voice_note",    # a deliberate spoken capture
    "action_item",   # something the provider believes was committed to
    "screen",        # screen or activity capture
)

# How freely this capture's *content* may be handled. The default is the
# careful one: a capture whose sensitivity the provider did not state is
# treated as sensitive, because the cost of guessing wrong is asymmetric.
SENSITIVITY = ("sensitive", "standard")
DEFAULT_SENSITIVITY = "sensitive"

# What a capture might become, if a human decides it should. A suggestion,
# addressed to the Founder, never acted on by the Foundation.
SUGGESTED_KINDS = (
    "task", "decision", "idea", "question", "reference", "none",
)

REQUIRED_FIELDS = (
    "schema_version", "provider", "provider_item_id", "capture_kind",
    "occurred_at", "title", "sensitivity", "suggested_kind", "reference",
)

# Field names that would carry content. Rejected on sight: the point of this
# contract is that the body stays with the provider, and a field named `text`
# arriving in a ContextItem means an adapter has misunderstood the boundary.
BODY_FIELDS = frozenset({
    "text", "body", "content", "transcript", "transcript_segments",
    "memory", "message", "messages", "summary_text", "full_text", "raw",
})

MAX_TITLE = 200
PROVIDER_RE = re.compile(r"^[a-z][a-z0-9_]*$")


class ContextError(Exception):
    """Raised when a capture does not satisfy the contract."""


def make_context_item(
    *,
    provider: str,
    provider_item_id: str,
    capture_kind: str,
    occurred_at: str,
    title: str,
    sensitivity: str = DEFAULT_SENSITIVITY,
    suggested_kind: str = "none",
    reference: str = "",
    category: str = "",
    duration_seconds: int | None = None,
    word_count: int | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build one ContextItem, then validate it. An invalid item is not returned.

    `title` is the one piece of text that travels, because a feed of captures
    with no titles is a feed nobody reads. Adapters are expected to use the
    provider's own short label, never the first line of a transcript — a rule
    a test enforces on the adapters rather than here, since this function
    cannot tell one string from another.
    """
    item = {
        "schema_version": SCHEMA_VERSION,
        "provider": provider,
        "provider_item_id": str(provider_item_id),
        "capture_kind": capture_kind,
        "occurred_at": occurred_at,
        "title": title,
        "sensitivity": sensitivity,
        "suggested_kind": suggested_kind,
        # Where the capture actually lives. A pointer, not a copy.
        "reference": reference,
        "category": category,
        "duration_seconds": duration_seconds,
        "word_count": word_count,
        "metadata": dict(metadata or {}),
    }
    problems = validate(item)
    if problems:
        raise ContextError("; ".join(problems))
    return item


def validate(item: Any) -> list[str]:
    """Every fault, not the first. A caller fixing one at a time learns slowly."""
    if not isinstance(item, dict):
        return [f"A ContextItem must be a JSON object, got {type(item).__name__}."]

    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in item:
            errors.append(f"Missing required field {field!r}.")
    if errors:
        return errors

    if item["schema_version"] != SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SCHEMA_VERSION!r}, got {item['schema_version']!r}.")

    provider = item["provider"]
    if not isinstance(provider, str) or not PROVIDER_RE.match(provider):
        errors.append(f"provider must be a lowercase slug, got {provider!r}.")

    if not str(item["provider_item_id"]).strip():
        errors.append(
            "provider_item_id must identify the capture in the provider; without it "
            "a retried delivery becomes a second institutional fact.")

    if item["capture_kind"] not in CAPTURE_KINDS:
        errors.append(
            f"Unknown capture_kind {item['capture_kind']!r}. One of: {', '.join(CAPTURE_KINDS)}.")

    if item["sensitivity"] not in SENSITIVITY:
        errors.append(
            f"sensitivity must be one of {SENSITIVITY}, got {item['sensitivity']!r}. "
            f"An unstated sensitivity is {DEFAULT_SENSITIVITY!r}, never absent.")

    if item["suggested_kind"] not in SUGGESTED_KINDS:
        errors.append(
            f"Unknown suggested_kind {item['suggested_kind']!r}. "
            f"One of: {', '.join(SUGGESTED_KINDS)}.")

    title = item["title"]
    if not isinstance(title, str) or not title.strip():
        errors.append("title must be a non-empty string.")
    elif len(title) > MAX_TITLE:
        errors.append(f"title exceeds {MAX_TITLE} characters ({len(title)}).")

    try:
        ev.parse_iso(str(item["occurred_at"]))
    except Exception:
        errors.append(f"occurred_at must be an ISO 8601 timestamp, got {item['occurred_at']!r}.")

    for field in ("duration_seconds", "word_count"):
        value = item.get(field)
        if value is not None and (not isinstance(value, int) or isinstance(value, bool) or value < 0):
            errors.append(f"{field} must be a non-negative integer or None, got {value!r}.")

    errors.extend(body_leaks(item))
    return errors


def body_leaks(item: Any, path: str = "item") -> list[str]:
    """Every place captured content appears, however deeply nested.

    The mirror of `alpha_events.secret_leaks`. That one keeps credentials out of
    the ledger; this one keeps the Founder's own words out of it.
    """
    found: list[str] = []
    if isinstance(item, dict):
        for key, value in item.items():
            here = f"{path}.{key}"
            if isinstance(key, str) and key.lower() in BODY_FIELDS:
                found.append(
                    f"{here} carries captured content. A ContextItem references a "
                    f"capture; it never copies one. The body stays with the provider.")
            found.extend(body_leaks(value, here))
    elif isinstance(item, list):
        for index, value in enumerate(item):
            found.extend(body_leaks(value, f"{path}[{index}]"))
    return found


def is_valid(item: Any) -> bool:
    return not validate(item)


def to_event(item: dict[str, Any], *, actor: str, department: str,
             received_at: str | None = None) -> dict[str, Any]:
    """Turn a validated ContextItem into an AlphaEvent.

    Severity is `info` and `requires_founder` is False, always. A capture is
    something that happened, not something that needs the Founder — and an
    adapter that could raise its own severity would eventually learn that
    marking everything urgent is the way to be seen. Attention is earned by
    the Founder promoting a capture, not claimed by the device that made it.
    """
    problems = validate(item)
    if problems:
        raise ContextError("; ".join(problems))

    return ev.make_event(
        source=item["provider"],
        actor=actor,
        department=department,
        event_type=f"{item['provider']}.capture.{item['capture_kind']}",
        entity_type="capture",
        entity_id=item["provider_item_id"],
        title=item["title"],
        summary="",
        severity="info",
        requires_founder=False,
        # The Foundation's own navigation scheme, not the provider's URL. A
        # capture is reachable at `alpha-proxima://memory/<id>`; the provider
        # link travels in metadata, where an interface can offer "open in Omi"
        # without any consumer mistaking an external address for an Alpha
        # Proxima one.
        deep_link=ev.deep_link("memory", item["provider"], item["provider_item_id"]),
        occurred_at=item["occurred_at"],
        received_at=received_at,
        provider_event_id=item["provider_item_id"],
        metadata={
            "capture_kind": item["capture_kind"],
            "sensitivity": item["sensitivity"],
            "suggested_kind": item["suggested_kind"],
            "category": item.get("category", ""),
            "duration_seconds": item.get("duration_seconds"),
            "word_count": item.get("word_count"),
            # Stated on every capture event so a reader never has to infer it.
            "content_location": "provider",
            "provider_url": item.get("reference", ""),
        },
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ap.py context", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("contract", help="Print the ContextItem contract as JSON.")
    check = sub.add_parser("check", help="Validate a ContextItem from a file or stdin.")
    check.add_argument("path", nargs="?", help="JSON file; omit to read stdin.")
    args = parser.parse_args(argv)

    if args.command == "contract":
        print(json.dumps({
            "schema_version": SCHEMA_VERSION,
            "capture_kinds": list(CAPTURE_KINDS),
            "sensitivity": list(SENSITIVITY),
            "default_sensitivity": DEFAULT_SENSITIVITY,
            "suggested_kinds": list(SUGGESTED_KINDS),
            "required_fields": list(REQUIRED_FIELDS),
            "refused_fields": sorted(BODY_FIELDS),
            "content_location": "provider",
        }, indent=2))
        return 0

    raw = Path(args.path).read_text(encoding="utf-8") if args.path else sys.stdin.read()
    problems = validate(json.loads(raw))
    if problems:
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    print("ContextItem is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
