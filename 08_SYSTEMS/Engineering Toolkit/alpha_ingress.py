#!/usr/bin/env python3
"""Webhook ingress — the only door an external system may knock on.

Everything else in the Live Integration Layer serves `GET`. This module is the
single exception, and it is deliberately a separate process with a separate port
and a separate command, because a write path deserves to be something an
operator starts on purpose rather than something that arrives with a read model.

## What the door checks, in order

The order is the design. Each check is cheap enough to run before the next, and
each one rejects a class of request the following check would have to trust:

1. **Path.** An unknown path is a 404 before anything is read.
2. **Size.** A body over the limit is refused without being buffered, so a
   large POST cannot exhaust memory before authentication.
3. **Rate.** A token bucket per provider, checked before the signature, because
   HMAC over a large body is the expensive part and a flood should not be able
   to buy that work.
4. **Signature.** Constant-time, over the raw bytes, before any parse. An
   unsigned or wrongly-signed body is an anonymous stranger claiming a commit
   happened, and is never parsed at all.
5. **Replay.** A delivery id already seen is acknowledged and dropped. A
   provider retry and an attacker's replay are the same bytes; treating the
   first as normal and the second as an error is impossible, so both are
   idempotent no-ops.
6. **Parse, then normalize.** Only now does provider vocabulary get read, and
   only by the adapter.

## What it refuses to do

* **It never echoes the payload.** A webhook receiver that reflects what it was
  sent is an open relay for whatever the sender wanted logged.
* **It never stores headers.** They carry the signature.
* **It has no GET.** Reading is the app's job; this process only receives.
* **It will not bind beyond loopback without a secret** — `FD-002` again, and
  with the additional refusal that a non-loopback bind must also be told it is
  behind a TLS terminator, because an HMAC over a plaintext connection protects
  the body's integrity and not its confidentiality.

## What it cannot do

It cannot write Founder state or a Markdown note; it has no path to either. It
appends normalized events and updates adapter health. Interpretation is a later,
separate, approved step.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import deque
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLKIT_DIR))
import alpha_adapters as ad  # noqa: E402
import alpha_events as ev  # noqa: E402
import alpha_live as live  # noqa: E402
import state_io  # noqa: E402

LIVE_DIR = ev.LIVE_DIR
DEFAULT_DEAD_LETTERS = LIVE_DIR / "state" / "dead-letters.jsonl"

LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}

# 2 MiB. GitHub's own documented maximum is 25 MiB, and the Foundation has no
# use for a payload that large: adapters read a handful of named fields. A lower
# bound is a smaller attack surface, and a rejected oversized delivery is
# visible in the dead letters rather than silent.
MAX_BODY_BYTES = 2 * 1024 * 1024

# Per-provider token bucket. Generous for a repository this size, and low enough
# that a flood cannot buy unbounded HMAC work.
RATE_LIMIT_REQUESTS = 60
RATE_LIMIT_WINDOW_SECONDS = 60

# How many delivery ids to remember for replay protection. Bounded because an
# unbounded set is a memory leak wearing a security hat; a provider that retries
# beyond this window is simply deduplicated again by the ledger, which keys on
# the occurrence rather than the delivery.
REPLAY_MEMORY = 4096

# Which environment variable holds each provider's shared secret. Named here,
# never valued here.
SECRET_ENV = {
    "github": "GITHUB_WEBHOOK_SECRET",
    "pocket_ai": "POCKET_AI_WEBHOOK_SECRET",
    "n8n": "N8N_WEBHOOK_SECRET",
}

# Which header carries each provider's signature.
SIGNATURE_HEADER = {
    "github": "X-Hub-Signature-256",
    "pocket_ai": "X-Alpha-Signature-256",
    "n8n": "X-Alpha-Signature-256",
}

# Which header carries each provider's own delivery identifier, used for replay
# protection.
DELIVERY_HEADER = {
    "github": "X-GitHub-Delivery",
    "pocket_ai": "X-Alpha-Delivery",
    "n8n": "X-Alpha-Delivery",
}

# Which header names the provider's own event type.
EVENT_HEADER = {
    "github": "X-GitHub-Event",
    "pocket_ai": "X-Alpha-Event",
    "n8n": "X-Alpha-Event",
}


class IngressError(Exception):
    """Raised when the receiver cannot be started safely."""


# --------------------------------------------------------------------------
# rate limiting and replay protection
# --------------------------------------------------------------------------

class RateLimiter:
    """A sliding window per provider. Cheap, and checked before any HMAC."""

    def __init__(self, limit: int = RATE_LIMIT_REQUESTS,
                 window: int = RATE_LIMIT_WINDOW_SECONDS) -> None:
        self.limit = limit
        self.window = window
        self._hits: dict[str, deque[float]] = {}

    def allow(self, key: str, now: float | None = None) -> bool:
        moment = now if now is not None else time.monotonic()
        hits = self._hits.setdefault(key, deque())
        while hits and moment - hits[0] > self.window:
            hits.popleft()
        if len(hits) >= self.limit:
            return False
        hits.append(moment)
        return True


class ReplayGuard:
    """Remembers recent delivery ids, bounded.

    A provider's retry and an attacker's replay are byte-identical, so both are
    answered the same way: acknowledged, and dropped. Acknowledging matters — a
    provider that receives an error will retry harder.
    """

    def __init__(self, capacity: int = REPLAY_MEMORY) -> None:
        self.capacity = capacity
        self._seen: dict[str, None] = {}

    def seen(self, delivery_id: str) -> bool:
        if not delivery_id:
            # Nothing to remember. The ledger still deduplicates on the
            # occurrence, so this is a weaker guarantee, not an absent one.
            return False
        if delivery_id in self._seen:
            return True
        self._seen[delivery_id] = None
        while len(self._seen) > self.capacity:
            self._seen.pop(next(iter(self._seen)))
        return False


# --------------------------------------------------------------------------
# dead letters
# --------------------------------------------------------------------------

def record_dead_letter(path: Path, *, provider: str, kind: str, reason: str,
                       payload: Any = None, adapter_id: str | None = None) -> None:
    """Keep a rejected delivery so a broken adapter is visible, not invisible.

    Deliberately stores no headers: a rejected webhook's headers carry its
    signature, and a debugging file is not a place to accumulate those. The
    payload is truncated, because the point is to recognize the shape of what
    arrived, not to archive it.
    """
    record = {
        "received_at": ev.now_iso(),
        "provider": provider,
        "kind": kind,
        "adapter_id": adapter_id,
        "reason": reason[:300],
    }
    if payload is not None:
        excerpt = json.dumps(payload, ensure_ascii=False)[:2000]
        record["payload_excerpt"] = excerpt
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


# --------------------------------------------------------------------------
# the gate
# --------------------------------------------------------------------------

def resolve_secrets(providers: tuple[str, ...]) -> dict[str, str]:
    """Read each enabled provider's secret from the environment, or refuse.

    Refusing to start is the correct response to a missing secret. A receiver
    that accepted unsigned deliveries "until the secret is configured" would be
    an open endpoint that looked configured, and the Founder's integration screen
    would show a connected adapter fed by anyone who found the URL.
    """
    secrets: dict[str, str] = {}
    missing: list[str] = []
    for provider in providers:
        name = SECRET_ENV.get(provider)
        if not name:
            raise IngressError(
                f"No signing scheme is defined for provider {provider!r}; refusing to receive it."
            )
        value = os.environ.get(name, "")
        if not value:
            missing.append(name)
            continue
        secrets[provider] = value
    if missing:
        raise IngressError(
            "Refusing to start without a signing secret for every enabled provider. "
            f"Set: {', '.join(missing)}. An endpoint that accepts unsigned deliveries is "
            "an open relay that looks like an integration."
        )
    return secrets


def check_exposure_gate(host: str, port: int, behind_tls: bool) -> None:
    """FD-002, plus the part an HMAC does not cover.

    A signature proves a body was not altered. It does not hide it. A
    non-loopback bind therefore has to assert that something in front of it
    terminates TLS, or the Foundation's activity crosses a network in plaintext
    with a valid signature attached.
    """
    if host in LOOPBACK_HOSTS:
        return
    if not behind_tls:
        raise IngressError(
            f"Refusing to bind {host}:{port} without --behind-tls. A signature protects a "
            "body's integrity, not its confidentiality; this receiver must sit behind a "
            "TLS terminator (FD-002: authentication and confidentiality before reachability)."
        )


def serve(providers: tuple[str, ...] = ("github",), port: int = 8789,
          host: str = "127.0.0.1", behind_tls: bool = False,
          ledger_path: Path | None = None, registry_path: Path | None = None,
          live_state_path: Path | None = None,
          dead_letter_path: Path | None = None,
          project_notifications: bool = True) -> int:
    """Receive signed webhooks and turn them into stored AlphaEvents."""
    check_exposure_gate(host, port, behind_tls)
    secrets = resolve_secrets(providers)

    from http.server import BaseHTTPRequestHandler, HTTPServer

    ledger = ev.EventLedger(ledger_path or ev.DEFAULT_LEDGER)
    registry = ad.AdapterRegistry(registry_path or ad.DEFAULT_REGISTRY)
    store = live.LiveStore(live_state_path or live.DEFAULT_LIVE_STATE)
    dead_letters = dead_letter_path or DEFAULT_DEAD_LETTERS
    limiter = RateLimiter()
    replay = ReplayGuard()

    class Handler(BaseHTTPRequestHandler):
        # Announce the least about ourselves that the stdlib allows.
        server_version = "AlphaProximaIngress"
        sys_version = ""

        def _reply(self, status: int, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802
            # There is deliberately no read surface here. Reading is the app's
            # job, and an ingress that also serves state is two trust boundaries
            # wearing one port.
            self._reply(405, {"error": "this endpoint receives only"})

        def do_POST(self) -> None:  # noqa: N802
            provider = self.path.strip("/").split("/")[-1].lower()
            if not self.path.startswith("/webhooks/") or provider not in secrets:
                self._reply(404, {"error": "unknown endpoint"})
                return

            length = int(self.headers.get("Content-Length") or 0)
            if length <= 0:
                self._reply(400, {"error": "empty body"})
                return
            if length > MAX_BODY_BYTES:
                # Refused before reading, so a large POST cannot exhaust memory
                # ahead of authentication.
                record_dead_letter(dead_letters, provider=provider, kind="",
                                   reason=f"body of {length} bytes exceeds {MAX_BODY_BYTES}")
                self._reply(413, {"error": "payload too large"})
                return

            if not limiter.allow(provider):
                # Before the signature check: HMAC over a body is the expensive
                # part, and a flood must not be able to buy it.
                self._reply(429, {"error": "rate limited"})
                return

            raw = self.rfile.read(length)
            signature = self.headers.get(SIGNATURE_HEADER[provider], "")
            if not ad.verify_hmac_sha256(secrets[provider], raw, signature):
                # Not parsed, and not stored as a dead letter: an unauthenticated
                # body is not evidence about an adapter, and writing it to disk
                # would let anyone who found the URL fill the Foundation's disk.
                self._reply(401, {"error": "signature verification failed"})
                return

            delivery_id = self.headers.get(DELIVERY_HEADER[provider], "")
            if replay.seen(delivery_id):
                # A provider retry and a replay are the same bytes. Both are
                # acknowledged, because an error makes a provider retry harder.
                self._reply(202, {"status": "duplicate delivery ignored",
                                  "stored": 0, "duplicates": 0})
                return

            try:
                payload = json.loads(raw.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                record_dead_letter(dead_letters, provider=provider, kind="",
                                   reason=f"unparseable body: {exc}")
                self._reply(400, {"error": "body is not JSON"})
                return

            kind = self.headers.get(EVENT_HEADER[provider], "")
            delivery = {
                "provider": provider,
                "kind": kind,
                "delivery_id": delivery_id,
                "received_at": ev.now_iso(),
                # The one place this value is ever set. A signed delivery that
                # reached this point came from the world, which is what lets it
                # promote the adapter's status.
                "origin": "webhook",
                "payload": payload,
            }

            try:
                result = registry.ingest(delivery, ledger=ledger)
            except ad.AdapterError as exc:
                record_dead_letter(dead_letters, provider=provider, kind=kind,
                                   reason=str(exc), payload=payload)
                registry.save()
                # 202 rather than 400: the delivery was authentic and we simply
                # do not report this event. Telling GitHub it sent something bad
                # would make it retry a payload we will reject identically.
                self._reply(202, {"status": "accepted, not reported",
                                  "reason": str(exc)[:200]})
                return

            if project_notifications:
                store.project_notifications(ledger.events())
                store.save()
            registry.save()

            # Counts only. Never the payload, and never the events — a receiver
            # that reflects what it was sent is an open relay.
            self._reply(202, {
                "status": "accepted",
                "adapter_id": result["adapter_id"],
                "stored": result["stored"],
                "duplicates": result["duplicates"],
                "badge": store.badge_count(),
            })

        def log_message(self, *args) -> None:
            pass

    server = HTTPServer((host, port), Handler)
    print(f"Alpha Proxima ingress: http://{host}:{port}/webhooks/<provider>")
    print(f"Receiving (signed only): {', '.join(sorted(secrets))}")
    print(f"Ledger: {ledger.path}")
    print("Loopback only." if host in LOOPBACK_HOSTS else "Behind a TLS terminator, as asserted.")
    print("POST only. Ctrl-C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ap.py ingress", description=__doc__)
    parser.add_argument("--ledger", default=None, help="Event ledger (JSONL).")
    parser.add_argument("--registry", default=None, help="Adapter health file.")
    parser.add_argument("--live-state", default=None, help="Live projection store.")
    parser.add_argument("--dead-letters", default=None, help="Rejected-delivery log (JSONL).")

    sub = parser.add_subparsers(dest="command", required=True)

    receive = sub.add_parser("serve", help="Receive signed webhooks (POST only).")
    receive.add_argument("--provider", action="append", default=None,
                         help="Provider to receive. Repeatable. Defaults to github.")
    receive.add_argument("--port", type=int, default=8789)
    receive.add_argument("--host", default="127.0.0.1",
                         help="Bind address. Anything but loopback requires --behind-tls.")
    receive.add_argument("--behind-tls", action="store_true",
                         help="Assert that a TLS terminator sits in front of this process.")
    receive.add_argument("--no-notifications", action="store_true",
                         help="Store events without running the notification policy.")

    check = sub.add_parser("check", help="Report whether ingress could start, and why not.")
    check.add_argument("--provider", action="append", default=None)
    check.add_argument("--host", default="127.0.0.1")
    check.add_argument("--port", type=int, default=8789)
    check.add_argument("--behind-tls", action="store_true")

    sub.add_parser("dead-letters", help="Print rejected deliveries as JSON.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    dead_letters = Path(args.dead_letters) if args.dead_letters else DEFAULT_DEAD_LETTERS

    if args.command == "dead-letters":
        if not dead_letters.exists():
            print("[]")
            return 0
        records = [json.loads(line) for line in dead_letters.read_text(encoding="utf-8").splitlines()
                   if line.strip()]
        print(json.dumps(records, indent=2, ensure_ascii=False))
        return 0

    providers = tuple(args.provider or ("github",))

    if args.command == "check":
        problems: list[str] = []
        for test in (lambda: check_exposure_gate(args.host, args.port, args.behind_tls),
                     lambda: resolve_secrets(providers)):
            try:
                test()
            except IngressError as exc:
                problems.append(str(exc))
        if problems:
            # An honest report of why the door is shut, which is the state today.
            print("ingress cannot start:", file=sys.stderr)
            for problem in problems:
                print(f"  - {problem}", file=sys.stderr)
            return 1
        print(f"ingress can start on {args.host}:{args.port} for {', '.join(providers)}.")
        return 0

    try:
        return serve(
            providers=providers,
            port=args.port,
            host=args.host,
            behind_tls=args.behind_tls,
            ledger_path=Path(args.ledger) if args.ledger else None,
            registry_path=Path(args.registry) if args.registry else None,
            live_state_path=Path(args.live_state) if args.live_state else None,
            dead_letter_path=dead_letters,
            project_notifications=not args.no_notifications,
        )
    except IngressError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
