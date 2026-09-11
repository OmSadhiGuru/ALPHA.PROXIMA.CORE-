#!/usr/bin/env python3
"""Minimum Viable Council session kernel.

This is a local-first record and gatekeeper, not an autonomous council.  It
creates bounded sessions, records assignments and dissent, and refuses actions
that would impersonate Founder, Ethics Council, or unappointed roles.
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
DEFAULT_STATE = VAULT_ROOT / "13_OPERATIONS" / "AI Council" / "state" / "council-state.json"
SCHEMA_VERSION = "1.0.0"
CLASSES = ("I", "II", "III", "IV")
STATES = ("open", "investigating", "founder-review", "approved", "executing", "complete", "blocked")
ROLE_ID_RE = re.compile(r"^AGT-\d{3}$")


class StateError(Exception):
    pass


class ExecutionError(StateError):
    """Raised when a real subprocess invocation of an agent role fails."""


def _load_sibling(filename: str, name: str):
    """Import a toolkit module by path.

    `ap.py` execs tools into synthetic module namespaces, so an ordinary
    `import role_registry` does not reliably resolve when this file runs via
    `ap.py council ...`. Mirrors the loader `alpha_app.py` already uses.
    """
    path = (TOOLKIT_DIR / filename).resolve()
    if not path.exists():
        raise StateError(f"Required toolkit module not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise StateError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


role_registry = _load_sibling("role_registry.py", "council_kernel_role_registry")


def _role_sets(root: Path = VAULT_ROOT) -> tuple[set[str], set[str], set[str]]:
    """Derive available/advisory-only/blocked role ids from the registry.

    Replaces what used to be hand-maintained module-level constants
    (`AVAILABLE`/`ADVISORY_ONLY`/`BLOCKED`) that could drift from the actual
    Founder-approved registry document without any code noticing.
    """
    registry = role_registry.load_roles(root)
    available = {r["id"] for r in registry["roles"] if r["state"] == "available"}
    advisory_only = {r["id"] for r in registry["roles"] if r["state"] == "advisory-only"}
    blocked = {r["id"] for r in registry["roles"] if r["state"] == "blocked"}
    return available, advisory_only, blocked


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def empty_state() -> dict:
    return {"schema_version": SCHEMA_VERSION, "updated_at": now(), "sessions": []}


def validate_state(state: dict) -> None:
    if not isinstance(state, dict) or state.get("schema_version") != SCHEMA_VERSION:
        raise StateError("Unsupported or invalid Council state document.")
    sessions = state.get("sessions")
    if not isinstance(sessions, list):
        raise StateError("Council state must contain a sessions list.")
    ids: set[str] = set()
    for session in sessions:
        required = ("session_id", "founder_intent", "decision_class", "interim_authority_basis",
                    "accountable_role", "assignments", "dissent", "ethics_trigger", "state", "opened_at")
        missing = [field for field in required if field not in session]
        if missing:
            raise StateError(f"Session missing required fields: {', '.join(missing)}.")
        if session["session_id"] in ids:
            raise StateError(f"Duplicate session ID {session['session_id']!r}.")
        ids.add(session["session_id"])
        if session["decision_class"] not in CLASSES or session["state"] not in STATES:
            raise StateError(f"Session {session['session_id']} has invalid class or state.")
        # Structural check only: a role's live availability is enforced at the
        # point of action (open_session/assign/execute_assignment), not here.
        # A session opened against a role the registry later marks blocked
        # must stay loadable -- its historical record shouldn't become
        # unparseable JSON just because the registry changed after the fact.
        if not ROLE_ID_RE.fullmatch(session["accountable_role"]):
            raise StateError(f"Session {session['session_id']} has a malformed accountable role.")


def load(path: Path) -> dict:
    if not path.exists():
        raise StateError(f"State document not found: {path}. Run `council init` first.")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise StateError(f"State document is not valid JSON: {exc}") from exc
    validate_state(state)
    return state


def save(state: dict, path: Path) -> None:
    validate_state(state)
    state["updated_at"] = now()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def session(state: dict, session_id: str) -> dict:
    for item in state["sessions"]:
        if item["session_id"] == session_id:
            return item
    raise StateError(f"No Council session {session_id!r}.")


def next_session_id(state: dict) -> str:
    day = datetime.now(timezone.utc).strftime("%Y%m%d")
    prefix = f"MVC-{day}-"
    serials = [int(s["session_id"].rsplit("-", 1)[1]) for s in state["sessions"]
               if re.fullmatch(rf"{prefix}\\d{{3}}", s["session_id"])]
    return f"{prefix}{max(serials, default=0) + 1:03d}"


def require_role(role: str, *, accountable: bool = False, root: Path = VAULT_ROOT) -> None:
    available, advisory_only, blocked = _role_sets(root)
    if role in blocked:
        raise StateError(f"{role} is blocked pending a separate appointment.")
    if role in advisory_only:
        if accountable:
            raise StateError(f"{role} is advisory only and cannot own a session.")
        return
    if role not in available:
        raise StateError(f"Unknown or unavailable agent role {role!r}.")


def open_session(state: dict, intent: str, decision_class: str, authority: str, owner: str,
                 ethics_trigger: str) -> dict:
    if not intent.strip() or not authority.strip():
        raise StateError("Founder intent and interim authority basis are required.")
    require_role(owner, accountable=True)
    if ethics_trigger not in ("none", "advisory", "formal-review-required"):
        raise StateError("ethics trigger must be none, advisory, or formal-review-required.")
    record = {"session_id": next_session_id(state), "founder_intent": intent.strip(),
              "decision_class": decision_class, "interim_authority_basis": authority.strip(),
              "facilitator": "AGT-001", "accountable_role": owner, "advisors": [], "assignments": [],
              "dissent": [], "ethics_trigger": ethics_trigger, "recommendation": None,
              "founder_decision": None, "execution_owner": None,
              "state": "blocked" if ethics_trigger == "formal-review-required" else "open",
              "opened_at": now(), "updated_at": now(), "next_action": "Map required advisors and bounded deliverables."}
    state["sessions"].append(record)
    return record


def assign(state: dict, session_id: str, role: str, deliverable: str, kind: str = "agent") -> dict:
    item = session(state, session_id)
    if item["state"] == "blocked":
        raise StateError("Blocked session cannot receive assignments until its stop condition is resolved.")
    require_role(role)
    if not deliverable.strip() or kind not in ("agent", "subagent", "challenger"):
        raise StateError("A bounded deliverable and a valid assignment kind are required.")
    record = {"id": f"RUN-{len(item['assignments']) + 1:03d}", "role": role, "kind": kind,
              "deliverable": deliverable.strip(), "status": "assigned", "created_at": now(), "output": None}
    item["assignments"].append(record)
    if role not in item["advisors"] and role != item["accountable_role"]:
        item["advisors"].append(role)
    item["state"] = "investigating"
    item["updated_at"] = now()
    return record


def record_output(state: dict, session_id: str, run_id: str, output: str) -> dict:
    item = session(state, session_id)
    run = next((x for x in item["assignments"] if x["id"] == run_id), None)
    if not run:
        raise StateError(f"No assignment {run_id!r} in {session_id}.")
    if not output.strip():
        raise StateError("Output summary cannot be empty.")
    run.update({"status": "complete", "output": output.strip(), "completed_at": now()})
    item["updated_at"] = now()
    return run


SYSTEM_PROMPT_TEMPLATE = """You are {named_role} ({role_id}), operating under {operating_owner}.
Current implementation: {current_implementation}.
You may instantiate only these bounded subagent kinds: {may_instantiate}.

Standing rules (Agent and Subagent Registry, Invocation Rules):
{invocation_rules}

Deliverable for this assignment: {deliverable}

You do not vote, ratify, appoint yourself, expand scope, or claim review by an
unconvened body. Return one bounded, text-only deliverable for this assignment
and nothing else. You cannot read or write files, run commands, or invoke tools."""


def _build_system_prompt(role_record: dict, deliverable: str, invocation_rules: list[str]) -> str:
    numbered_rules = "\n".join(f"{i}. {rule}" for i, rule in enumerate(invocation_rules, start=1))
    return SYSTEM_PROMPT_TEMPLATE.format(
        named_role=role_record["named_role"],
        role_id=role_record["id"],
        operating_owner=role_record["operating_owner"],
        current_implementation=role_record["current_implementation"],
        may_instantiate=", ".join(role_record["may_instantiate"]) or "none",
        invocation_rules=numbered_rules,
        deliverable=deliverable,
    )


def _parse_claude_output(stdout: str) -> str:
    """Extract the answer text from a `claude -p --output-format json` call.

    Prefers a single top-level JSON object (the normal `json` output shape,
    with a `result` field). Falls back to a line-by-line NDJSON scan for the
    last `type: "result"` event, in case the installed CLI only supports the
    streaming shape -- kept as a fallback, not the primary path, since v1 has
    no need for streaming (this call is a single blocking round trip).
    """
    text = stdout.strip()
    if not text:
        return ""
    try:
        payload = json.loads(text)
        if isinstance(payload, dict) and "result" in payload:
            return str(payload["result"] or "").strip()
    except json.JSONDecodeError:
        pass
    result = ""
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and event.get("type") == "result":
            result = str(event.get("result") or "").strip()
    return result


def execute_assignment(state: dict, session_id: str, run_id: str, prompt: str, *,
                       root: Path = VAULT_ROOT, timeout: int = 120,
                       claude_bin: str = "claude", model: str | None = None) -> dict:
    """Run a real `claude` CLI call for one assignment and record its output.

    This is the only function in this module that spawns a process. It still
    writes state through `record_output` -- the single-writer rule holds;
    this function only automates *how* the output text is produced, not *who*
    is allowed to persist it.

    v1 limitation, deliberate: this call is pure text-in/text-out. No MCP
    tools, no filesystem access, no sub-agent spawning. Extending tool access
    is a separate, explicitly-scoped decision, not an incidental capability
    of this function.
    """
    item = session(state, session_id)
    run = next((x for x in item["assignments"] if x["id"] == run_id), None)
    if not run:
        raise StateError(f"No assignment {run_id!r} in {session_id}.")

    available, advisory_only, blocked = _role_sets(root)
    if run["role"] in blocked:
        raise ExecutionError(f"{run['role']} is blocked pending a separate appointment.")
    if run["role"] in advisory_only:
        raise ExecutionError(
            f"{run['role']} is advisory-only and cannot be executed as an assignment; "
            "record a manual summary via `council output` instead."
        )
    if run["role"] not in available:
        raise ExecutionError(f"Unknown or unavailable agent role {run['role']!r}.")

    registry = role_registry.load_roles(root)
    role_record = role_registry.role(registry, run["role"])
    system_prompt = _build_system_prompt(role_record, run["deliverable"], registry["invocation_rules"])

    args = [claude_bin, "-p", prompt, "--output-format", "json",
            "--system-prompt", system_prompt,
            "--disallowedTools", "Bash,Edit,Write,Read,Glob,Grep,Agent,NotebookEdit,Task"]
    if model:
        args += ["--model", model]

    with tempfile.TemporaryDirectory(prefix="council-exec-") as tmp:
        env = {key: value for key, value in os.environ.items() if key != "CLAUDECODE"}
        try:
            result = subprocess.run(args, cwd=tmp, env=env, capture_output=True,
                                    text=True, timeout=timeout)
        except FileNotFoundError as exc:
            raise ExecutionError(
                f"`{claude_bin}` not found on PATH. Install the Claude CLI or pass --claude-bin."
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ExecutionError(f"Claude CLI timed out after {timeout}s for {run_id}.") from exc

    if result.returncode != 0:
        raise ExecutionError(
            f"Claude CLI exited {result.returncode} for {run_id}: {result.stderr.strip()[:500]}"
        )
    output_text = _parse_claude_output(result.stdout)
    if not output_text:
        raise ExecutionError(f"Claude CLI produced no usable result for {run_id}.")

    return record_output(state, session_id, run_id, output_text)


def synthesize(state: dict, session_id: str, recommendation: str, dissent: str | None) -> dict:
    item = session(state, session_id)
    if any(run["status"] != "complete" for run in item["assignments"]):
        raise StateError("Complete or explicitly remove all assignments before synthesis.")
    if not recommendation.strip():
        raise StateError("A non-binding recommendation is required.")
    item["recommendation"] = recommendation.strip()
    if dissent and dissent.strip():
        item["dissent"].append({"recorded_at": now(), "text": dissent.strip()})
    item["state"] = "founder-review"
    item["next_action"] = "Founder reviews the synthesis and records an explicit decision."
    item["updated_at"] = now()
    return item


def decide(state: dict, session_id: str, decision: str, by: str, execution_owner: str | None) -> dict:
    item = session(state, session_id)
    if by.strip().lower() not in ("founder", "frederick belizaire gunville"):
        raise StateError("Only the Founder may record an interim Council decision.")
    if item["state"] != "founder-review":
        raise StateError("A Founder decision requires a synthesized session in founder-review.")
    if decision not in ("approve", "reject", "defer", "ratify"):
        raise StateError("Decision must be approve, reject, defer, or ratify.")
    if decision == "ratify" and item["decision_class"] not in ("I", "II"):
        raise StateError("Ratification is reserved for Class I/II proposals.")
    if decision == "approve" and item["decision_class"] in ("I", "II"):
        raise StateError("Class I/II proposals require explicit ratify, not approve.")
    if decision in ("approve", "ratify") and execution_owner:
        require_role(execution_owner, accountable=True)
    item["founder_decision"] = {"decision": decision, "by": by.strip(), "recorded_at": now()}
    item["execution_owner"] = execution_owner
    item["state"] = "executing" if decision in ("approve", "ratify") and execution_owner else ("approved" if decision in ("approve", "ratify") else "complete")
    item["next_action"] = "Route bounded execution." if item["state"] == "executing" else "Record closure and write back durable context."
    item["updated_at"] = now()
    return item


def render(item: dict) -> str:
    lines = [f"# Council Decision Packet — {item['session_id']}", "", f"**State:** {item['state']}", f"**Decision class:** {item['decision_class']}", f"**Authority basis:** {item['interim_authority_basis']}", f"**Accountable role:** {item['accountable_role']}", "", "## Founder intent", "", item["founder_intent"], "", "## Work record", ""]
    for run in item["assignments"]:
        lines.append(f"- **{run['id']} · {run['role']} ({run['kind']})** — {run['status']}: {run['deliverable']}" + (f"\n  - Output: {run['output']}" if run.get("output") else ""))
    lines += ["", "## Recommendation", "", item["recommendation"] or "Pending synthesis.", "", "## Dissent", ""]
    lines += [f"- {entry['text']}" for entry in item["dissent"]] or ["- None recorded."]
    lines += ["", "## Founder decision", "", json.dumps(item["founder_decision"], ensure_ascii=False) if item["founder_decision"] else "Pending.", "", "## Next action", "", item["next_action"], "", "---", "This packet records advisory and delegated work only. It does not create a quorate Council, appoint an engine, or substitute for an Ethics Council review.", ""]
    return "\n".join(lines)


def build_view(state: dict) -> dict:
    """A compact read model for terminals, a local console, and future clients."""
    sessions = sorted(state["sessions"], key=lambda item: item["opened_at"], reverse=True)
    active = [item for item in sessions if item["state"] not in ("complete",)]
    founder_review = [item for item in sessions if item["state"] == "founder-review"]
    blocked = [item for item in sessions if item["state"] == "blocked"]
    return {"generated_at": now(), "schema_version": state["schema_version"], "sessions": sessions,
            "counts": {"total": len(sessions), "active": len(active),
                       "founder_review": len(founder_review), "blocked": len(blocked)},
            "next_action": (founder_review[0]["next_action"] if founder_review else
                            (active[0]["next_action"] if active else "Open a bounded Council session when structured cross-function work is needed."))}


def render_dashboard(state: dict) -> str:
    """Self-contained local Console; it reads state and never writes it."""
    view = build_view(state)
    def session_card(item: dict) -> str:
        decision = item.get("founder_decision") or {}
        return (f"<article class='session {html.escape(item['state'])}'>"
                f"<div class='meta'>{html.escape(item['session_id'])} · {html.escape(item['state'].upper())} · Class {html.escape(item['decision_class'])}</div>"
                f"<h3>{html.escape(item['founder_intent'])}</h3>"
                f"<p><b>Owner:</b> {html.escape(item['accountable_role'])} &nbsp; <b>Ethics:</b> {html.escape(item['ethics_trigger'])}</p>"
                f"<p><b>Next:</b> {html.escape(item['next_action'])}</p>"
                f"<p><b>Founder decision:</b> {html.escape(decision.get('decision', 'pending'))}</p></article>")
    cards = "".join(session_card(item) for item in view["sessions"]) or "<article class='empty'><h3>No sessions yet</h3><p>The Council is active and ready. Open one only for a real Founder intent requiring structured advice or delegated execution.</p></article>"
    counts = view["counts"]
    return f"""<!doctype html><html lang='en'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Alpha Proxima — Council Console</title><style>
:root{{color-scheme:dark;--ink:#e8edf1;--muted:#a8b3bc;--line:#29353e;--panel:#11191e;--accent:#75d4b2;--warn:#ffcc75;--block:#ff8d88}}*{{box-sizing:border-box}}body{{margin:0;background:#091015;color:var(--ink);font:16px system-ui,-apple-system,sans-serif}}main{{max-width:1060px;margin:auto;padding:44px 24px 64px}}h1{{margin:0 0 8px;font-size:2rem}}.lead,.meta{{color:var(--muted)}}.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:28px 0}}.metric,.session,.next,.empty{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px}}.metric b{{font-size:1.7rem;display:block;color:var(--accent)}}.next{{border-color:var(--accent);margin-bottom:20px}}.session{{margin:12px 0}}.session.blocked{{border-left:4px solid var(--block)}}.session.founder-review{{border-left:4px solid var(--warn)}}h3{{margin:.45rem 0}}p{{margin:.55rem 0;line-height:1.45}}footer{{color:var(--muted);font-size:.85rem;margin-top:26px}}@media(max-width:680px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}</style>
<main><p class='meta'>ALPHA PROXIMA · MINIMUM VIABLE COUNCIL · LOCAL READ MODEL</p><h1>Council Console</h1><p class='lead'>What is happening? What needs the Founder? What happens next?</p>
<section class='grid'><div class='metric'><b>{counts['active']}</b>active</div><div class='metric'><b>{counts['founder_review']}</b>need Founder</div><div class='metric'><b>{counts['blocked']}</b>blocked</div><div class='metric'><b>{counts['total']}</b>total sessions</div></section>
<section class='next'><div class='meta'>NEXT ACTION</div><b>{html.escape(view['next_action'])}</b></section><section><h2>Sessions</h2>{cards}</section><footer>Rendered {html.escape(view['generated_at'])}. This console is read-only and does not confer authority, appoint roles, or substitute for Council review.</footer></main></html>"""


def serve(path: Path, port: int) -> int:
    from http.server import BaseHTTPRequestHandler, HTTPServer
    class Handler(BaseHTTPRequestHandler):
        def send_body(self, body: bytes, content_type: str, status: int = 200) -> None:
            self.send_response(status); self.send_header("Content-Type", content_type); self.send_header("Content-Length", str(len(body))); self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(body)
        def do_GET(self) -> None:  # noqa: N802
            try: state = load(path)
            except StateError as exc: self.send_body(json.dumps({"error": str(exc)}).encode(), "application/json", 500); return
            if self.path in ("/", "/index.html"): self.send_body(render_dashboard(state).encode(), "text/html; charset=utf-8")
            elif self.path == "/api/view": self.send_body(json.dumps(build_view(state), indent=2).encode(), "application/json")
            elif self.path == "/api/state": self.send_body(json.dumps(state, indent=2).encode(), "application/json")
            else: self.send_body(b'{"error":"not found"}', "application/json", 404)
        def log_message(self, *args) -> None: pass
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Council Console: http://127.0.0.1:{port}/\nRead model:      http://127.0.0.1:{port}/api/view\nLoopback only. Ctrl-C to stop.")
    try: server.serve_forever()
    except KeyboardInterrupt: print("\nStopped.")
    finally: server.server_close()
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ap.py council", description=__doc__)
    p.add_argument("--state", default=str(DEFAULT_STATE)); sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("init"); sub.add_parser("list"); sub.add_parser("check"); sub.add_parser("dashboard", help="Print the self-contained Council Console HTML.")
    x = sub.add_parser("serve", help="Serve the Council Console on 127.0.0.1."); x.add_argument("--port", type=int, default=8788)
    x = sub.add_parser("open"); x.add_argument("intent"); x.add_argument("--class", dest="decision_class", choices=CLASSES, required=True); x.add_argument("--authority", required=True); x.add_argument("--owner", required=True); x.add_argument("--ethics-trigger", default="none")
    x = sub.add_parser("assign"); x.add_argument("session_id"); x.add_argument("role"); x.add_argument("deliverable"); x.add_argument("--kind", default="agent")
    x = sub.add_parser("output"); x.add_argument("session_id"); x.add_argument("run_id"); x.add_argument("summary")
    x = sub.add_parser("run", help="Execute an assignment via the real `claude` CLI and record its output.")
    x.add_argument("session_id"); x.add_argument("run_id"); x.add_argument("--prompt", required=True)
    x.add_argument("--timeout", type=int, default=120); x.add_argument("--model", default=None)
    x.add_argument("--claude-bin", default="claude")
    x = sub.add_parser("synthesize"); x.add_argument("session_id"); x.add_argument("recommendation"); x.add_argument("--dissent")
    x = sub.add_parser("decide"); x.add_argument("session_id"); x.add_argument("decision"); x.add_argument("--by", required=True); x.add_argument("--execution-owner")
    x = sub.add_parser("render"); x.add_argument("session_id"); x.add_argument("--output")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv); path = Path(args.state)
    try:
        if args.command == "init":
            if path.exists(): raise StateError(f"State already exists: {path}")
            save(empty_state(), path); print(f"Initialized {path}"); return 0
        state = load(path)
        if args.command == "check": validate_state(state); print(f"State OK — {len(state['sessions'])} session(s)."); return 0
        if args.command == "list":
            for item in state["sessions"]: print(f"{item['session_id']}  {item['state']:<15} {item['founder_intent']}")
            return 0
        if args.command == "dashboard": print(render_dashboard(state)); return 0
        if args.command == "serve": return serve(path, args.port)
        if args.command == "open": result = open_session(state, args.intent, args.decision_class, args.authority, args.owner, args.ethics_trigger)
        elif args.command == "assign": result = assign(state, args.session_id, args.role, args.deliverable, args.kind)
        elif args.command == "output": result = record_output(state, args.session_id, args.run_id, args.summary)
        elif args.command == "run": result = execute_assignment(state, args.session_id, args.run_id, args.prompt, timeout=args.timeout, claude_bin=args.claude_bin, model=args.model)
        elif args.command == "synthesize": result = synthesize(state, args.session_id, args.recommendation, args.dissent)
        elif args.command == "decide": result = decide(state, args.session_id, args.decision, args.by, args.execution_owner)
        elif args.command == "render":
            content = render(session(state, args.session_id))
            if args.output: Path(args.output).write_text(content, encoding="utf-8"); print(f"Rendered {args.output}")
            else: print(content)
            return 0
        else: raise StateError(f"Unhandled command {args.command!r}")
        save(state, path); print(result.get("session_id") or result.get("id")); return 0
    except StateError as exc:
        print(f"error: {exc}", file=sys.stderr); return 1


if __name__ == "__main__": raise SystemExit(main(sys.argv[1:]))
