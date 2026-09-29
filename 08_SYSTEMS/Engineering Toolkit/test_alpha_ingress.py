#!/usr/bin/env python3
"""Tests for the webhook receiver — the layer's only write path.

Almost every test here is about a refusal, because an ingress is judged by what
it declines. The end-to-end case runs a real socket and posts real signed bytes
at it, since the checks under test are ordered and the order is only observable
from outside.
"""

from __future__ import annotations

import hashlib
import hmac
import importlib.util
import json
import sys
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from unittest.mock import patch

TOOLKIT_DIR = Path(__file__).resolve().parent


def _load(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLKIT_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ev = _load("alpha_events.py", "alpha_events")
ad = _load("alpha_adapters.py", "alpha_adapters")
live = _load("alpha_live.py", "alpha_live")
ingress = _load("alpha_ingress.py", "alpha_ingress")

SECRET = "a-test-signing-secret"


def sign(body: bytes, secret: str = SECRET) -> str:
    return "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()


def pull_request_payload(number: int = 48, action: str = "review_requested") -> dict:
    return {
        "action": action,
        "repository": {"full_name": "OmSadhiGuru/ALPHA.PROXIMA.CORE-"},
        "sender": {"login": "codex-bot"},
        "pull_request": {
            "number": number, "title": "Memory navigation", "state": "open",
            "updated_at": "2026-09-29T14:00:00Z", "head": {"ref": "codex/x"},
            "changed_files": 3, "additions": 412, "deletions": 18,
        },
    }


class SignatureTests(unittest.TestCase):
    def test_a_correct_signature_verifies(self):
        body = b'{"action":"opened"}'
        self.assertTrue(ad.verify_hmac_sha256(SECRET, body, sign(body)))

    def test_a_tampered_body_does_not_verify(self):
        self.assertFalse(ad.verify_hmac_sha256(SECRET, b"tampered", sign(b"original")))

    def test_a_missing_secret_refuses_rather_than_skipping_the_check(self):
        # "No secret configured, so accept everything" is how an ingress becomes
        # an open relay.
        body = b"{}"
        self.assertFalse(ad.verify_hmac_sha256("", body, sign(body)))

    def test_the_github_specific_name_is_the_same_function(self):
        self.assertIs(ad.verify_github_signature, ad.verify_hmac_sha256)


class StartupGateTests(unittest.TestCase):
    def test_a_missing_secret_refuses_startup_and_names_the_variable(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ingress.IngressError) as caught:
                ingress.resolve_secrets(("github",))
        self.assertIn("GITHUB_WEBHOOK_SECRET", str(caught.exception))
        self.assertIn("open relay", str(caught.exception))

    def test_a_present_secret_permits_startup(self):
        with patch.dict("os.environ", {"GITHUB_WEBHOOK_SECRET": SECRET}, clear=True):
            self.assertEqual(ingress.resolve_secrets(("github",)), {"github": SECRET})

    def test_a_provider_with_no_signing_scheme_is_refused(self):
        with self.assertRaises(ingress.IngressError):
            ingress.resolve_secrets(("notion",))

    def test_loopback_needs_no_tls_assertion(self):
        for host in ("127.0.0.1", "localhost", "::1"):
            with self.subTest(host=host):
                ingress.check_exposure_gate(host, 8789, behind_tls=False)

    def test_a_public_bind_without_tls_is_refused(self):
        with self.assertRaises(ingress.IngressError) as caught:
            ingress.check_exposure_gate("0.0.0.0", 8789, behind_tls=False)
        self.assertIn("confidentiality", str(caught.exception))

    def test_a_public_bind_behind_tls_is_permitted(self):
        ingress.check_exposure_gate("0.0.0.0", 8789, behind_tls=True)

    def test_every_receivable_provider_has_a_secret_signature_and_delivery_header(self):
        for provider in ingress.SECRET_ENV:
            with self.subTest(provider=provider):
                self.assertIn(provider, ingress.SIGNATURE_HEADER)
                self.assertIn(provider, ingress.DELIVERY_HEADER)
                self.assertIn(provider, ingress.EVENT_HEADER)
                self.assertIn(provider, ev.SOURCES)

    def test_the_module_names_secrets_and_contains_no_secret_values(self):
        # Every credential appears here as the name of an environment variable
        # and nowhere as a value. A default secret is worse than none: it looks
        # configured.
        source = (TOOLKIT_DIR / "alpha_ingress.py").read_text(encoding="utf-8")
        for name in ingress.SECRET_ENV.values():
            with self.subTest(variable=name):
                self.assertEqual(name, name.upper())
                self.assertIn(f'"{name}"', source)
        # No environment lookup anywhere supplies a non-empty fallback: a
        # default secret is worse than none, because it looks configured.
        self.assertNotRegex(source, r'environ\.get\([^)]*,\s*"[^"]+"\s*\)')
        self.assertNotRegex(source, r"environ\.get\([^)]*,\s*'[^']+'\s*\)")
        self.assertIn('os.environ.get(name, "")', source)


class RateLimiterTests(unittest.TestCase):
    def test_requests_inside_the_limit_are_allowed(self):
        limiter = ingress.RateLimiter(limit=3, window=60)
        self.assertTrue(all(limiter.allow("github", now=0) for _ in range(3)))

    def test_the_limit_is_enforced(self):
        limiter = ingress.RateLimiter(limit=3, window=60)
        for _ in range(3):
            limiter.allow("github", now=0)
        self.assertFalse(limiter.allow("github", now=0))

    def test_the_window_slides(self):
        limiter = ingress.RateLimiter(limit=2, window=60)
        limiter.allow("github", now=0)
        limiter.allow("github", now=1)
        self.assertFalse(limiter.allow("github", now=2))
        self.assertTrue(limiter.allow("github", now=120))

    def test_providers_are_limited_independently(self):
        limiter = ingress.RateLimiter(limit=1, window=60)
        self.assertTrue(limiter.allow("github", now=0))
        self.assertFalse(limiter.allow("github", now=0))
        self.assertTrue(limiter.allow("n8n", now=0))


class ReplayGuardTests(unittest.TestCase):
    def test_a_repeated_delivery_id_is_recognized(self):
        guard = ingress.ReplayGuard()
        self.assertFalse(guard.seen("d-1"))
        self.assertTrue(guard.seen("d-1"))

    def test_distinct_deliveries_are_not_confused(self):
        guard = ingress.ReplayGuard()
        self.assertFalse(guard.seen("d-1"))
        self.assertFalse(guard.seen("d-2"))

    def test_an_absent_delivery_id_is_never_treated_as_a_replay(self):
        # A weaker guarantee, not an absent one: the ledger still deduplicates
        # on the occurrence itself.
        guard = ingress.ReplayGuard()
        self.assertFalse(guard.seen(""))
        self.assertFalse(guard.seen(""))

    def test_the_memory_is_bounded_so_it_cannot_leak(self):
        guard = ingress.ReplayGuard(capacity=4)
        for index in range(20):
            guard.seen(f"d-{index}")
        self.assertLessEqual(len(guard._seen), 4)
        # The oldest is forgotten, which is why the ledger remains the real
        # idempotency guarantee.
        self.assertFalse(guard.seen("d-0"))


class DeadLetterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "dead.jsonl"

    def tearDown(self):
        self.tmp.cleanup()

    def test_a_rejected_delivery_is_recorded_with_its_reason(self):
        ingress.record_dead_letter(self.path, provider="github", kind="pull_request",
                                  reason="no pull_request.number", payload={"action": "opened"})
        record = json.loads(self.path.read_text(encoding="utf-8").strip())
        self.assertEqual(record["provider"], "github")
        self.assertIn("no pull_request.number", record["reason"])

    def test_no_header_is_ever_stored(self):
        ingress.record_dead_letter(self.path, provider="github", kind="push", reason="bad")
        record = json.loads(self.path.read_text(encoding="utf-8").strip())
        self.assertNotIn("headers", record)
        for key in record:
            self.assertNotIn("signature", key.lower())

    def test_the_payload_excerpt_is_truncated(self):
        ingress.record_dead_letter(self.path, provider="github", kind="push",
                                  reason="huge", payload={"blob": "x" * 50000})
        record = json.loads(self.path.read_text(encoding="utf-8").strip())
        self.assertLessEqual(len(record["payload_excerpt"]), 2000)


class NoWriteTests(unittest.TestCase):
    def identifiers(self, filename: str) -> set[str]:
        import ast
        tree = ast.parse((TOOLKIT_DIR / filename).read_text(encoding="utf-8"))
        names: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                names.add(node.id)
            elif isinstance(node, ast.Attribute):
                names.add(node.attr)
            elif isinstance(node, ast.Import):
                names.update(alias.asname or alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                names.add(node.module or "")
        return names

    def test_the_receiver_cannot_reach_the_founder_state_engine(self):
        names = self.identifiers("alpha_ingress.py")
        self.assertNotIn("founder_os", names)

    def test_the_receiver_has_no_read_surface(self):
        source = (TOOLKIT_DIR / "alpha_ingress.py").read_text(encoding="utf-8")
        # A GET handler exists only to refuse. An ingress that also serves state
        # is two trust boundaries wearing one port.
        self.assertIn("def do_GET", source)
        self.assertIn('"this endpoint receives only"', source)


class EndToEndTests(unittest.TestCase):
    """A real socket, real signed bytes, and the check order observed from outside."""

    PORT = 8797

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        cls.ledger_path = root / "ledger.jsonl"
        cls.registry_path = root / "registry.json"
        cls.live_path = root / "live.json"
        cls.dead_path = root / "dead.jsonl"
        cls.env = patch.dict("os.environ", {"GITHUB_WEBHOOK_SECRET": SECRET})
        cls.env.start()
        cls.thread = threading.Thread(
            target=ingress.serve,
            kwargs=dict(providers=("github",), port=cls.PORT, host="127.0.0.1",
                        ledger_path=cls.ledger_path, registry_path=cls.registry_path,
                        live_state_path=cls.live_path, dead_letter_path=cls.dead_path),
            daemon=True,
        )
        cls.thread.start()
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            try:
                cls.request("GET", "/webhooks/github")
                break
            except urllib.error.URLError:
                time.sleep(0.05)

    @classmethod
    def tearDownClass(cls):
        cls.env.stop()
        cls.tmp.cleanup()

    @classmethod
    def request(cls, method: str, path: str, body: bytes = b"",
                headers: dict[str, str] | None = None) -> tuple[int, dict]:
        request = urllib.request.Request(
            f"http://127.0.0.1:{cls.PORT}{path}", data=body or None,
            headers=headers or {}, method=method)
        try:
            with urllib.request.urlopen(request, timeout=5) as response:
                return response.status, json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read().decode("utf-8") or "{}")

    def post(self, payload: dict, *, kind: str = "pull_request", delivery: str = "d-1",
             secret: str = SECRET, signed: bool = True) -> tuple[int, dict]:
        body = json.dumps(payload).encode("utf-8")
        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Event": kind,
            "X-GitHub-Delivery": delivery,
        }
        if signed:
            headers["X-Hub-Signature-256"] = sign(body, secret)
        return self.request("POST", "/webhooks/github", body, headers)

    # -- refusals, in the order the receiver applies them -----------------
    def test_get_is_refused_because_this_endpoint_only_receives(self):
        status, _ = self.request("GET", "/webhooks/github")
        self.assertEqual(status, 405)

    def test_an_unknown_path_is_refused(self):
        status, _ = self.post(pull_request_payload())
        self.assertEqual(status, 202)  # sanity: the known path works
        body = json.dumps({}).encode()
        status, _ = self.request("POST", "/webhooks/notion", body,
                                 {"X-Hub-Signature-256": sign(body)})
        self.assertEqual(status, 404)

    def test_an_unsigned_body_is_rejected_and_never_stored(self):
        before = len(ev.EventLedger(self.ledger_path).events())
        status, _ = self.post(pull_request_payload(number=101), delivery="unsigned-1",
                              signed=False)
        self.assertEqual(status, 401)
        self.assertEqual(len(ev.EventLedger(self.ledger_path).events()), before)

    def test_a_wrongly_signed_body_is_rejected(self):
        status, _ = self.post(pull_request_payload(number=102), delivery="wrong-1",
                              secret="not-the-secret")
        self.assertEqual(status, 401)

    def test_an_unauthenticated_body_is_not_even_written_to_the_dead_letters(self):
        # Otherwise anyone who found the URL could fill the Foundation's disk.
        before = self.dead_path.read_text(encoding="utf-8") if self.dead_path.exists() else ""
        self.post(pull_request_payload(number=103), delivery="unsigned-2", signed=False)
        after = self.dead_path.read_text(encoding="utf-8") if self.dead_path.exists() else ""
        self.assertEqual(before, after)

    def test_an_empty_body_is_refused(self):
        status, _ = self.request("POST", "/webhooks/github", b"",
                                 {"X-Hub-Signature-256": sign(b"")})
        self.assertEqual(status, 400)

    def test_a_signed_but_unparseable_body_becomes_a_dead_letter(self):
        body = b"{not json"
        status, _ = self.request("POST", "/webhooks/github", body, {
            "X-GitHub-Event": "push", "X-GitHub-Delivery": "bad-json-1",
            "X-Hub-Signature-256": sign(body)})
        self.assertEqual(status, 400)
        self.assertIn("unparseable", self.dead_path.read_text(encoding="utf-8"))

    def test_a_signed_payload_the_adapter_rejects_is_accepted_but_not_reported(self):
        # 202, not 400: the delivery was authentic. Telling GitHub it sent
        # something bad would make it retry a payload we reject identically.
        status, payload = self.post({"action": "opened", "pull_request": {}},
                                    delivery="no-number-1")
        self.assertEqual(status, 202)
        self.assertEqual(payload["status"], "accepted, not reported")
        self.assertIn("pull_request.number", self.dead_path.read_text(encoding="utf-8"))

    # -- the accepted path -----------------------------------------------
    def test_a_signed_delivery_is_normalized_stored_and_counted(self):
        status, payload = self.post(pull_request_payload(number=200), delivery="ok-200")
        self.assertEqual(status, 202)
        self.assertEqual(payload["status"], "accepted")
        self.assertEqual(payload["stored"], 1)
        stored = ev.EventLedger(self.ledger_path).events()
        self.assertTrue(any(e["entity_id"] == "PR-200" for e in stored))

    def test_the_response_never_echoes_the_payload(self):
        status, payload = self.post(pull_request_payload(number=201), delivery="ok-201")
        body = json.dumps(payload)
        self.assertNotIn("Memory navigation", body)
        self.assertNotIn("codex-bot", body)
        self.assertNotIn("events", payload)

    def test_a_retried_delivery_id_is_acknowledged_and_dropped(self):
        self.post(pull_request_payload(number=202), delivery="retry-202")
        before = len(ev.EventLedger(self.ledger_path).events())
        status, payload = self.post(pull_request_payload(number=202), delivery="retry-202")
        self.assertEqual(status, 202)
        self.assertIn("duplicate", payload["status"])
        self.assertEqual(len(ev.EventLedger(self.ledger_path).events()), before)

    def test_the_same_occurrence_under_a_new_delivery_id_is_still_deduplicated(self):
        # Replay memory is bounded, so the ledger is the real guarantee.
        self.post(pull_request_payload(number=203), delivery="first-203")
        before = len(ev.EventLedger(self.ledger_path).events())
        status, payload = self.post(pull_request_payload(number=203), delivery="second-203")
        self.assertEqual(status, 202)
        self.assertEqual(payload["stored"], 0)
        self.assertEqual(payload["duplicates"], 1)
        self.assertEqual(len(ev.EventLedger(self.ledger_path).events()), before)

    def test_a_verified_delivery_is_what_makes_the_adapter_connected(self):
        self.post(pull_request_payload(number=204), delivery="ok-204")
        registry = ad.AdapterRegistry(self.registry_path)
        self.assertEqual(registry.observed_status("ADP-GITHUB"), "connected")
        # And only GitHub. A verified delivery says nothing about anything else.
        for row in registry.view()["adapters"]:
            if row["adapter_id"] != "ADP-GITHUB":
                self.assertFalse(row["connected"], row["adapter_id"])

    def test_the_notification_policy_runs_and_the_badge_reflects_it(self):
        self.post(pull_request_payload(number=205), delivery="ok-205")
        store = live.LiveStore(self.live_path)
        self.assertGreater(store.badge_count(), 0)
        record = next(r for r in store.state["notifications"]
                      if "PR-205" in r["title"])
        # A requested review is the Founder's business, so it earns a push.
        self.assertIn("push", record["channels"])
        self.assertEqual(record["deep_link"], "alpha-proxima://github/pr/205")

    def test_routine_progress_does_not_earn_a_push(self):
        self.post(pull_request_payload(number=206, action="opened"), delivery="ok-206")
        store = live.LiveStore(self.live_path)
        record = next(r for r in store.state["notifications"] if "PR-206" in r["title"])
        self.assertNotIn("push", record["channels"])

    def test_an_oversized_body_is_refused_before_it_is_read(self):
        body = b"x" * 64
        status, _ = self.request("POST", "/webhooks/github", body, {
            "X-GitHub-Event": "push", "X-GitHub-Delivery": "big-1",
            "Content-Length": str(ingress.MAX_BODY_BYTES + 1),
            "X-Hub-Signature-256": sign(body)})
        self.assertEqual(status, 413)

    def test_the_server_does_not_advertise_its_python_version(self):
        # Read off the wire rather than the source, so this tests the behaviour
        # and not the intention.
        request = urllib.request.Request(
            f"http://127.0.0.1:{self.PORT}/webhooks/github", method="GET")
        try:
            urllib.request.urlopen(request, timeout=5)
            header = ""
        except urllib.error.HTTPError as exc:
            header = exc.headers.get("Server", "")
        self.assertTrue(header, "no Server header was sent at all")
        self.assertNotIn("Python", header)
        self.assertIn("AlphaProxima", header)


if __name__ == "__main__":
    unittest.main(verbosity=2)
