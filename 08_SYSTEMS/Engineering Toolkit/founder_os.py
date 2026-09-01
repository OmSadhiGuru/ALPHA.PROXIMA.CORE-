#!/usr/bin/env python3
"""Founder OS state engine.

Canonical state for Founder Console V1 lives in a single git-versioned JSON
document inside the Vault. This module is the only writer. It provides:

  * a validated state model (see `SCHEMA` and `validate_state`);
  * read/write commands for the Founder's daily operating lane;
  * a renderer that produces a self-contained Console page and an
    Obsidian-readable Markdown mirror;
  * a localhost-only server exposing the same state over HTTP.

Design constraints (see `Founder OS Architecture v1`):
  * standard library only -- the Vault gains no runtime dependency;
  * JSON is canonical, Markdown and HTML are generated read-only mirrors,
    so there is exactly one writer and no reconciliation problem;
  * every presentation layer (2D console today, spatial UI later) consumes
    the same state document, never the renderer.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
FOUNDER_OS_DIR = VAULT_ROOT / "11_OPERATIONS" / "Founder OS"
DEFAULT_STATE = FOUNDER_OS_DIR / "state" / "founder-state.json"
DEFAULT_TEMPLATE = FOUNDER_OS_DIR / "console" / "console.template.html"
DEFAULT_CONSOLE = FOUNDER_OS_DIR / "console" / "console.html"
DEFAULT_MIRROR = FOUNDER_OS_DIR / "Founder Console.md"

SCHEMA_VERSION = "1.0.0"
MAX_PRIORITIES = 3

TASK_STATES = ("assigned", "working", "waiting", "blocked", "review", "complete")
DECISION_STATES = ("open", "approved", "rejected", "deferred")
AGENT_STATES = ("active", "working", "idle", "proposed", "blocked", "retired")
INTEGRATION_STATES = ("connected", "not_connected", "planned", "blocked")
HEALTH_STATES = ("ok", "degraded", "unknown", "failing")
PRIORITY_STATES = ("open", "done", "dropped")
BLOCKER_STATES = ("open", "resolved")

# Collection name -> (id prefix, allowed status values, status field name).
COLLECTIONS = {
    "priorities": ("PRI", PRIORITY_STATES, "status"),
    "decisions": ("FD", DECISION_STATES, "status"),
    "tasks": ("TSK", TASK_STATES, "state"),
    "agents": ("AGT", AGENT_STATES, "status"),
    "agent_runs": ("RUN", None, "status"),
    "blockers": ("BLK", BLOCKER_STATES, "status"),
    "context_items": ("CTX", None, None),
    "results": ("RES", None, None),
    "projects": ("PRJ", None, "status"),
    "integrations": ("INT", INTEGRATION_STATES, "status"),
    "system_health": ("SYS", HEALTH_STATES, "status"),
}

# Fields every record in a collection must carry. Provenance fields are
# mandatory so any work item can answer why it exists and who owns it.
REQUIRED_RECORD_FIELDS = {
    "priorities": ("id", "rank", "title", "why", "owner", "status"),
    "decisions": ("id", "title", "context", "recommendation", "options",
                  "consequence_of_delay", "status", "requested_by"),
    "tasks": ("id", "title", "owner", "state", "requested_by", "why"),
    "agents": ("id", "name", "role", "status", "authority"),
    "agent_runs": ("id", "agent_id", "status"),
    "blockers": ("id", "title", "impact", "owner", "status", "needs_founder"),
    "context_items": ("id", "source", "summary"),
    "results": ("id", "kind", "summary"),
    "projects": ("id", "name", "status"),
    "integrations": ("id", "name", "status"),
    "system_health": ("id", "area", "status", "detail"),
}


class StateError(Exception):
    """Raised when the state document is invalid or a command is impossible."""


# --------------------------------------------------------------------------
# time / id helpers
# --------------------------------------------------------------------------

def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def today_iso() -> str:
    return date.today().isoformat()


def next_id(state: dict, collection: str) -> str:
    prefix = COLLECTIONS[collection][0]
    highest = 0
    for record in state.get(collection, []):
        match = re.fullmatch(rf"{prefix}-(\d+)", str(record.get("id", "")))
        if match:
            highest = max(highest, int(match.group(1)))
    return f"{prefix}-{highest + 1:03d}"


def find(state: dict, collection: str, record_id: str) -> dict:
    for record in state.get(collection, []):
        if record.get("id") == record_id:
            return record
    raise StateError(f"{collection}: no record with id {record_id!r}")


# --------------------------------------------------------------------------
# load / validate / save
# --------------------------------------------------------------------------

def empty_state() -> dict:
    state = {
        "schema_version": SCHEMA_VERSION,
        "updated_at": now_iso(),
        "founder": {"name": "Founder", "role": "Executive authority"},
        "daily_mission": None,
        "next_action": None,
    }
    for collection in COLLECTIONS:
        state[collection] = []
    return state


def load_state(path: Path) -> dict:
    if not path.exists():
        raise StateError(f"State document not found: {path}. Run `founder init` first.")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise StateError(f"State document is not valid JSON: {exc}") from exc
    validate_state(state)
    return state


def save_state(state: dict, path: Path) -> None:
    validate_state(state)
    state["updated_at"] = now_iso()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def validate_state(state: dict) -> list[str]:
    """Raise StateError on the first structural problem; return notes otherwise."""
    if not isinstance(state, dict):
        raise StateError("State document must be a JSON object.")
    if state.get("schema_version") != SCHEMA_VERSION:
        raise StateError(
            f"Unsupported schema_version {state.get('schema_version')!r}; expected {SCHEMA_VERSION!r}."
        )

    notes: list[str] = []
    for collection, (_prefix, allowed, status_field) in COLLECTIONS.items():
        records = state.get(collection)
        if records is None:
            raise StateError(f"State document is missing collection {collection!r}.")
        if not isinstance(records, list):
            raise StateError(f"Collection {collection!r} must be a list.")

        seen: set[str] = set()
        for record in records:
            if not isinstance(record, dict):
                raise StateError(f"{collection}: every record must be an object.")
            missing = [f for f in REQUIRED_RECORD_FIELDS[collection] if f not in record]
            if missing:
                raise StateError(
                    f"{collection}: record {record.get('id', '<no id>')!r} missing {', '.join(missing)}."
                )
            record_id = record["id"]
            if record_id in seen:
                raise StateError(f"{collection}: duplicate id {record_id!r}.")
            seen.add(record_id)
            if allowed and status_field:
                value = record.get(status_field)
                if value not in allowed:
                    raise StateError(
                        f"{collection}: record {record_id!r} has {status_field}={value!r}; "
                        f"allowed: {', '.join(allowed)}."
                    )

    open_priorities = [p for p in state["priorities"] if p["status"] == "open"]
    if len(open_priorities) > MAX_PRIORITIES:
        raise StateError(
            f"Founder Console holds at most {MAX_PRIORITIES} open priorities; "
            f"found {len(open_priorities)}. Complete or drop one first."
        )

    mission = state.get("daily_mission")
    if mission is not None:
        for field in ("date", "mission", "set_by", "set_at"):
            if field not in mission:
                raise StateError(f"daily_mission is missing {field!r}.")

    action = state.get("next_action")
    if action is not None:
        for field in ("title", "owner", "set_at"):
            if field not in action:
                raise StateError(f"next_action is missing {field!r}.")
        linked = action.get("priority_id")
        if linked and linked not in {p["id"] for p in state["priorities"]}:
            raise StateError(f"next_action references unknown priority {linked!r}.")

    for blocker in state["blockers"]:
        for blocked_id in blocker.get("blocking_ids", []):
            known = {t["id"] for t in state["tasks"]} | {p["id"] for p in state["priorities"]}
            if blocked_id not in known:
                notes.append(
                    f"blocker {blocker['id']} references unknown work item {blocked_id!r}"
                )
    return notes


# --------------------------------------------------------------------------
# derived views -- the four questions the Console must answer
# --------------------------------------------------------------------------

def open_priorities(state: dict) -> list[dict]:
    return sorted(
        (p for p in state["priorities"] if p["status"] == "open"),
        key=lambda p: p["rank"],
    )


def active_tasks(state: dict) -> list[dict]:
    return [t for t in state["tasks"] if t["state"] != "complete"]


def open_decisions(state: dict) -> list[dict]:
    return [d for d in state["decisions"] if d["status"] == "open"]


def open_blockers(state: dict) -> list[dict]:
    return [b for b in state["blockers"] if b["status"] == "open"]


def build_view(state: dict) -> dict:
    """The Console's read model. Presentation layers consume this, not raw state."""
    mission = state.get("daily_mission")
    stale = bool(mission) and mission["date"] != today_iso()
    return {
        "generated_at": now_iso(),
        "today": today_iso(),
        "schema_version": state["schema_version"],
        "founder": state["founder"],
        "mission": mission,
        "mission_is_stale": stale,
        "priorities": open_priorities(state),
        "next_action": state.get("next_action"),
        "decisions": open_decisions(state),
        "tasks": active_tasks(state),
        "agents": state["agents"],
        "blockers": open_blockers(state),
        "integrations": state["integrations"],
        "system_health": state["system_health"],
        "projects": state["projects"],
        "counts": {
            "priorities": len(open_priorities(state)),
            "decisions": len(open_decisions(state)),
            "tasks": len(active_tasks(state)),
            "blockers": len(open_blockers(state)),
            "founder_blockers": len([b for b in open_blockers(state) if b["needs_founder"]]),
        },
    }


# --------------------------------------------------------------------------
# mutations
# --------------------------------------------------------------------------

def set_mission(state: dict, mission: str, set_by: str = "founder",
                on_date: str | None = None, sprint_id: str | None = None) -> dict:
    if not mission.strip():
        raise StateError("Mission of the Day cannot be empty.")
    record = {
        "date": on_date or today_iso(),
        "mission": mission.strip(),
        "set_by": set_by,
        "set_at": now_iso(),
        "sprint_id": sprint_id,
    }
    state["daily_mission"] = record
    return record


def add_priority(state: dict, title: str, why: str, owner: str,
                 project: str | None = None, rank: int | None = None) -> dict:
    current = open_priorities(state)
    if len(current) >= MAX_PRIORITIES:
        raise StateError(
            f"Top {MAX_PRIORITIES} is full. Complete or drop a priority before adding another."
        )
    record = {
        "id": next_id(state, "priorities"),
        "rank": rank if rank is not None else len(current) + 1,
        "title": title.strip(),
        "why": why.strip(),
        "project": project,
        "owner": owner,
        "status": "open",
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    state["priorities"].append(record)
    _renumber_priorities(state)
    return record


def set_priority_status(state: dict, priority_id: str, status: str) -> dict:
    if status not in PRIORITY_STATES:
        raise StateError(f"Unknown priority status {status!r}; allowed: {', '.join(PRIORITY_STATES)}.")
    record = find(state, "priorities", priority_id)
    record["status"] = status
    record["updated_at"] = now_iso()
    _renumber_priorities(state)
    action = state.get("next_action")
    if status != "open" and action and action.get("priority_id") == priority_id:
        # The Next Action pointed at work that is no longer a priority; clearing
        # it is better than showing the Founder a stale instruction.
        state["next_action"] = None
    return record


def _renumber_priorities(state: dict) -> None:
    for index, record in enumerate(open_priorities(state), start=1):
        record["rank"] = index


def set_next_action(state: dict, title: str, owner: str,
                    context: str | None = None, priority_id: str | None = None) -> dict:
    if priority_id:
        find(state, "priorities", priority_id)
    record = {
        "id": "NXT-001",
        "title": title.strip(),
        "owner": owner,
        "context": context,
        "priority_id": priority_id,
        "set_at": now_iso(),
    }
    state["next_action"] = record
    return record


def add_decision(state: dict, title: str, context: str, recommendation: str,
                 options: list[str], consequence_of_delay: str,
                 requested_by: str = "LUMIAION") -> dict:
    record = {
        "id": next_id(state, "decisions"),
        "title": title.strip(),
        "context": context.strip(),
        "recommendation": recommendation.strip(),
        "options": list(options),
        "consequence_of_delay": consequence_of_delay.strip(),
        "status": "open",
        "requested_by": requested_by,
        "created_at": now_iso(),
        "decided_at": None,
        "decision_note": None,
    }
    state["decisions"].append(record)
    return record


def resolve_decision(state: dict, decision_id: str, status: str, note: str | None = None) -> dict:
    if status not in ("approved", "rejected", "deferred"):
        raise StateError("Decision resolution must be approved, rejected, or deferred.")
    record = find(state, "decisions", decision_id)
    record["status"] = status
    record["decided_at"] = now_iso()
    record["decision_note"] = note
    return record


def add_task(state: dict, title: str, owner: str, why: str, requested_by: str,
             project: str | None = None, gate: str | None = None) -> dict:
    record = {
        "id": next_id(state, "tasks"),
        "title": title.strip(),
        "project": project,
        "owner": owner,
        "state": "assigned",
        "requested_by": requested_by,
        "why": why.strip(),
        "gate": gate,
        "output_ref": None,
        "blocker_ids": [],
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    state["tasks"].append(record)
    return record


def set_task_state(state: dict, task_id: str, new_state: str,
                   output_ref: str | None = None) -> dict:
    if new_state not in TASK_STATES:
        raise StateError(f"Unknown task state {new_state!r}; allowed: {', '.join(TASK_STATES)}.")
    record = find(state, "tasks", task_id)
    record["state"] = new_state
    record["updated_at"] = now_iso()
    if output_ref:
        record["output_ref"] = output_ref
    return record


def set_agent_status(state: dict, agent_id: str, status: str, notes: str | None = None) -> dict:
    if status not in AGENT_STATES:
        raise StateError(f"Unknown agent status {status!r}; allowed: {', '.join(AGENT_STATES)}.")
    record = find(state, "agents", agent_id)
    record["status"] = status
    if notes is not None:
        record["notes"] = notes
    return record


def set_health(state: dict, health_id: str, status: str,
               detail: str | None = None, source: str | None = None) -> dict:
    """Update a system-health signal.

    Health records are shown in the Console but were previously unreachable
    from the CLI, so they could only go stale. A signal nobody can correct is
    worse than no signal.
    """
    if status not in HEALTH_STATES:
        raise StateError(f"Unknown health status {status!r}; allowed: {', '.join(HEALTH_STATES)}.")
    record = find(state, "system_health", health_id)
    record["status"] = status
    if detail is not None:
        record["detail"] = detail
    if source is not None:
        record["source"] = source
    record["checked_at"] = now_iso()
    return record


def add_blocker(state: dict, title: str, impact: str, owner: str,
                needs_founder: bool = False, blocking_ids: list[str] | None = None) -> dict:
    record = {
        "id": next_id(state, "blockers"),
        "title": title.strip(),
        "impact": impact.strip(),
        "owner": owner,
        "status": "open",
        "needs_founder": bool(needs_founder),
        "blocking_ids": list(blocking_ids or []),
        "created_at": now_iso(),
        "resolved_at": None,
    }
    state["blockers"].append(record)
    return record


def resolve_blocker(state: dict, blocker_id: str, note: str | None = None) -> dict:
    record = find(state, "blockers", blocker_id)
    record["status"] = "resolved"
    record["resolved_at"] = now_iso()
    if note:
        record["resolution_note"] = note
    return record


def run_repository_health_lane(state: dict, intention: str, why: str,
                               vault_root: Path, report_path: Path) -> dict:
    """Route one Founder intention through LUMIAION to JERANIUM.

    This is intentionally the only executable V1 worker lane.  It invokes the
    existing report-only Vault Validator, records the routed task and agent run,
    persists a result reference, and leaves the task at Founder review.
    """
    intention = intention.strip()
    why = why.strip()
    if not intention or not why:
        raise StateError("Repository-health intention and why are required.")
    if not vault_root.is_dir():
        raise StateError(f"Vault root is not a directory: {vault_root}")

    jeranium = next(
        (agent for agent in state["agents"] if agent.get("name") == "JERANIUM"),
        None,
    )
    if jeranium is None or jeranium.get("status") in {"proposed", "blocked", "retired"}:
        raise StateError("JERANIUM must be registered and available for this lane.")

    # Import locally so Founder OS remains usable even if an optional worker is
    # moved later. Both modules are standard-library-only and share this folder.
    import vault_validator

    task = add_task(
        state, intention, owner="JERANIUM", why=why,
        requested_by="Founder via LUMIAION", gate="G1",
    )
    task["routing_decision"] = "LUMIAION -> JERANIUM -> Vault Validator"
    set_task_state(state, task["id"], "working")

    run = {
        "id": next_id(state, "agent_runs"),
        "agent_id": jeranium["id"],
        "task_id": task["id"],
        "status": "working",
        "started_at": now_iso(),
        "route": "LUMIAION -> JERANIUM",
        "worker": "vault_validator.validate",
    }
    state["agent_runs"].append(run)
    jeranium["status"] = "working"
    jeranium["last_run_id"] = run["id"]

    notes, issues = vault_validator.validate(vault_root, include_hidden=False)
    summary = vault_validator.summarize_issues(issues)
    report = vault_validator.render_markdown_report(vault_root, notes, issues)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=report_path.parent, delete=False,
        prefix=f".{report_path.name}.", suffix=".tmp",
    ) as handle:
        handle.write(report)
        temporary_report = Path(handle.name)
    temporary_report.replace(report_path)

    issue_text = ", ".join(
        f"{summary[level]} {level}" for level in ("critical", "error", "warning", "info")
    )
    result = {
        "id": next_id(state, "results"),
        "task_id": task["id"],
        "kind": "repository-health-report",
        "ref": str(report_path),
        "summary": f"Scanned {len(notes)} Markdown notes: {issue_text}.",
        "produced_at": now_iso(),
        "produced_by": "JERANIUM",
    }
    state["results"].append(result)
    set_task_state(state, task["id"], "review", output_ref=result["ref"])
    run.update({"status": "complete", "ended_at": now_iso(), "result_id": result["id"]})
    jeranium["status"] = "idle"
    validate_state(state)
    return {"task": task, "run": run, "result": result}


# --------------------------------------------------------------------------
# renderers
# --------------------------------------------------------------------------

STATE_PLACEHOLDER = "/*__FOUNDER_VIEW__*/null"


def render_console(state: dict, template_path: Path) -> str:
    """Inline the read model into the template so the page works from file://."""
    if not template_path.exists():
        raise StateError(f"Console template not found: {template_path}")
    template = template_path.read_text(encoding="utf-8")
    if STATE_PLACEHOLDER not in template:
        raise StateError(f"Console template is missing the {STATE_PLACEHOLDER} placeholder.")
    payload = json.dumps(build_view(state), indent=2, ensure_ascii=False)
    # Prevent an embedded </script> inside data from terminating the tag early.
    payload = payload.replace("</", "<\\/")
    return template.replace(STATE_PLACEHOLDER, payload)


MIRROR_FRONTMATTER = """---
title: "Founder Console"
aliases: ["Founder Console", "Founder OS Console", "Console V1"]
tags: [operations, founder-os, console, dashboard, lumiaion, alpha-proxima]
created: 2026-08-26
updated: {updated}
status: active
version: "1.0.0"
authors: ["LUMIAION", "CODEX"]
artifact_type: operations-dashboard
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Orchestration"
reasoning_engine: "LUMIAION"
dependencies: ["[[Founder OS Architecture v1]]", "[[LUMIAION - Operating Manual (LOOM)]]"]
related_documents: ["[[Founder Reboot Control Center]]", "[[Dashboards Index]]", "[[Workflow Registry]]"]
related_research_programs: []
---
"""


def render_mirror(state: dict) -> str:
    """Read-only Obsidian view. Generated from state; never edited by hand."""
    view = build_view(state)
    lines = [MIRROR_FRONTMATTER.format(updated=today_iso()), "# Founder Console", ""]
    lines += [
        "> [!warning] Generated file",
        "> This note is rendered from `state/founder-state.json` by "
        "`ap.py founder render`. Edits here are overwritten. Change state with "
        "`ap.py founder <command>`.",
        "",
        f"_Rendered {view['generated_at']} · schema {view['schema_version']}_",
        "",
        "## Today",
        "",
    ]

    mission = view["mission"]
    if mission:
        stale = " ⚠️ **stale — set today's mission**" if view["mission_is_stale"] else ""
        lines += [
            f"**{mission['date']}** — {mission['mission']}{stale}",
            "",
            f"_Set by {mission['set_by']}"
            + (f" · sprint {mission['sprint_id']}" if mission.get("sprint_id") else "")
            + "_",
            "",
        ]
    else:
        lines += ["_No Mission of the Day set._", ""]

    lines += ["### Top 3 Priorities", ""]
    if view["priorities"]:
        lines += ["| # | Priority | Why | Owner |", "|---|---|---|---|"]
        for p in view["priorities"]:
            lines.append(f"| {p['rank']} | {p['title']} | {p['why']} | {p['owner']} |")
    else:
        lines.append("_No open priorities._")
    lines.append("")

    action = view["next_action"]
    lines += ["### Next Action", ""]
    lines.append(f"**{action['title']}** — {action['owner']}" if action else "_No next action set._")
    lines.append("")

    def table(title: str, headers: list[str], rows: list[list[str]], empty: str) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if rows:
            lines.append("| " + " | ".join(headers) + " |")
            lines.append("|" + "|".join(["---"] * len(headers)) + "|")
            lines.extend("| " + " | ".join(r) + " |" for r in rows)
        else:
            lines.append(empty)
        lines.append("")

    table(
        "Decisions Requiring Founder",
        ["ID", "Decision", "Recommendation", "Consequence of delay"],
        [[d["id"], d["title"], d["recommendation"], d["consequence_of_delay"]]
         for d in view["decisions"]],
        "_No decisions awaiting the Founder._",
    )
    table(
        "Execution",
        ["ID", "Task", "State", "Owner", "Why"],
        [[t["id"], t["title"], t["state"].upper(), t["owner"], t["why"]] for t in view["tasks"]],
        "_No active work units._",
    )
    table(
        "Agents / Systems",
        ["Agent", "Role", "Status", "Authority"],
        [[a["name"], a["role"], a["status"].upper(), a["authority"]] for a in view["agents"]],
        "_No agents registered._",
    )
    table(
        "Blockers",
        ["ID", "Blocker", "Impact", "Owner", "Founder needed?"],
        [[b["id"], b["title"], b["impact"], b["owner"], "Yes" if b["needs_founder"] else "No"]
         for b in view["blockers"]],
        "_No open blockers._",
    )
    table(
        "System Health",
        ["Area", "Status", "Detail"],
        [[h["area"], h["status"].upper(), h["detail"]] for h in view["system_health"]],
        "_No health signals recorded._",
    )
    table(
        "Integrations",
        ["Integration", "Status", "Notes"],
        [[i["name"], i["status"].replace("_", " ").upper(), i.get("notes", "")]
         for i in view["integrations"]],
        "_No integrations registered._",
    )
    return "\n".join(lines).rstrip() + "\n"


def render_all(state: dict, template_path: Path, console_path: Path, mirror_path: Path) -> list[Path]:
    console_path.parent.mkdir(parents=True, exist_ok=True)
    console_path.write_text(render_console(state, template_path), encoding="utf-8")
    mirror_path.parent.mkdir(parents=True, exist_ok=True)
    mirror_path.write_text(render_mirror(state), encoding="utf-8")
    return [console_path, mirror_path]


# --------------------------------------------------------------------------
# text summary (terminal view of the same four questions)
# --------------------------------------------------------------------------

def summarize(state: dict) -> str:
    view = build_view(state)
    out = [f"FOUNDER CONSOLE — {view['today']}", "=" * 46, ""]
    mission = view["mission"]
    if mission:
        flag = "  [STALE]" if view["mission_is_stale"] else ""
        out += [f"MISSION ({mission['date']}){flag}", f"  {mission['mission']}", ""]
    else:
        out += ["MISSION", "  (not set)", ""]

    out.append("TOP 3")
    out += [f"  {p['rank']}. {p['title']}  — {p['owner']}" for p in view["priorities"]] or ["  (none)"]
    out.append("")

    action = view["next_action"]
    out += ["NEXT ACTION", f"  {action['title']}  — {action['owner']}" if action else "  (none)", ""]

    counts = view["counts"]
    out += [
        f"NEEDS YOU     decisions {counts['decisions']} · founder-blockers {counts['founder_blockers']}",
        f"IN FLIGHT     tasks {counts['tasks']} · blockers {counts['blockers']}",
        "",
        "AGENTS",
    ]
    out += [f"  {a['name']:<12} {a['status'].upper()}" for a in view["agents"]] or ["  (none)"]
    return "\n".join(out)


# --------------------------------------------------------------------------
# localhost server -- the API contract future presentation layers consume
# --------------------------------------------------------------------------

def serve(state_path: Path, template_path: Path, port: int = 8787) -> int:
    """Serve the Console and its read model on loopback only.

    Binding to 127.0.0.1 keeps Founder state private by default: no
    authentication system is required because the socket is not reachable
    off-host. Exposing this beyond loopback is a Founder decision (see
    `Founder OS Architecture v1`, Security).
    """
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class Handler(BaseHTTPRequestHandler):
        def _send(self, body: bytes, content_type: str, status: int = 200) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802 - stdlib naming
            try:
                state = load_state(state_path)
            except StateError as exc:
                self._send(json.dumps({"error": str(exc)}).encode(), "application/json", 500)
                return
            if self.path in ("/", "/index.html", "/console.html"):
                self._send(render_console(state, template_path).encode("utf-8"),
                           "text/html; charset=utf-8")
            elif self.path == "/api/state":
                self._send(json.dumps(state, indent=2).encode("utf-8"), "application/json")
            elif self.path == "/api/view":
                self._send(json.dumps(build_view(state), indent=2).encode("utf-8"),
                           "application/json")
            else:
                self._send(b'{"error":"not found"}', "application/json", 404)

        def log_message(self, *args) -> None:  # keep the terminal calm
            pass

    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Founder Console: http://127.0.0.1:{port}/")
    print(f"Read model:      http://127.0.0.1:{port}/api/view")
    print("Loopback only. Ctrl-C to stop.")
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
    parser = argparse.ArgumentParser(prog="ap.py founder", description=__doc__)
    parser.add_argument("--state", default=str(DEFAULT_STATE), help="Path to founder-state.json.")
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="Console template path.")
    parser.add_argument("--console", default=str(DEFAULT_CONSOLE), help="Rendered console output.")
    parser.add_argument("--mirror", default=str(DEFAULT_MIRROR), help="Markdown mirror output.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="Create an empty state document.")
    sub.add_parser("show", help="Print the Founder Console summary.")
    sub.add_parser("state", help="Print the raw state document.")
    sub.add_parser("view", help="Print the Console read model as JSON.")
    sub.add_parser("check", help="Validate the state document.")
    sub.add_parser("render", help="Regenerate console.html and the Markdown mirror.")

    p = sub.add_parser("serve", help="Serve the Console on 127.0.0.1.")
    p.add_argument("--port", type=int, default=8787)

    p = sub.add_parser("mission", help="Set the Mission of the Day.")
    p.add_argument("mission")
    p.add_argument("--by", default="founder")
    p.add_argument("--date")
    p.add_argument("--sprint")

    p = sub.add_parser("priority-add", help="Add a Top 3 priority.")
    p.add_argument("title")
    p.add_argument("--why", required=True)
    p.add_argument("--owner", required=True)
    p.add_argument("--project")

    p = sub.add_parser("priority-status", help="Set a priority to open/done/dropped.")
    p.add_argument("id")
    p.add_argument("status", choices=PRIORITY_STATES)

    p = sub.add_parser("next-action", help="Set the single Next Action.")
    p.add_argument("title")
    p.add_argument("--owner", required=True)
    p.add_argument("--context")
    p.add_argument("--priority")

    p = sub.add_parser("decision-add", help="Queue a Founder decision.")
    p.add_argument("title")
    p.add_argument("--context", required=True)
    p.add_argument("--recommendation", required=True)
    p.add_argument("--option", action="append", default=[], dest="options")
    p.add_argument("--consequence", required=True)
    p.add_argument("--by", default="LUMIAION")

    p = sub.add_parser("decision-resolve", help="Approve, reject, or defer a decision.")
    p.add_argument("id")
    p.add_argument("status", choices=["approved", "rejected", "deferred"])
    p.add_argument("--note")

    p = sub.add_parser("task-add", help="Add a work unit.")
    p.add_argument("title")
    p.add_argument("--owner", required=True)
    p.add_argument("--why", required=True)
    p.add_argument("--by", default="founder")
    p.add_argument("--project")
    p.add_argument("--gate")

    p = sub.add_parser("task-state", help="Move a work unit between states.")
    p.add_argument("id")
    # dest must not be "state": that is the global --state option's dest, and a
    # subparser positional of the same name overwrites the state-file path.
    p.add_argument("new_state", metavar="state", choices=TASK_STATES)
    p.add_argument("--output")

    p = sub.add_parser("agent-status", help="Set an agent's operational status.")
    p.add_argument("id")
    p.add_argument("status", choices=AGENT_STATES)
    p.add_argument("--notes")

    p = sub.add_parser("health-set", help="Update a system-health signal.")
    p.add_argument("id")
    p.add_argument("status", choices=HEALTH_STATES)
    p.add_argument("--detail")
    p.add_argument("--source")

    p = sub.add_parser("blocker-add", help="Record a blocker.")
    p.add_argument("title")
    p.add_argument("--impact", required=True)
    p.add_argument("--owner", required=True)
    p.add_argument("--needs-founder", action="store_true")
    p.add_argument("--blocking", action="append", default=[], dest="blocking_ids")

    p = sub.add_parser("blocker-resolve", help="Resolve a blocker.")
    p.add_argument("id")
    p.add_argument("--note")

    p = sub.add_parser(
        "repository-health",
        help="Run the Founder -> LUMIAION -> JERANIUM repository-health lane.",
    )
    p.add_argument("intention")
    p.add_argument("--why", required=True)
    p.add_argument("--vault", default=str(VAULT_ROOT))
    p.add_argument("--report", required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    state_path = Path(args.state)
    template_path = Path(args.template)

    try:
        if args.command == "init":
            if state_path.exists():
                print(f"State already exists: {state_path}")
                return 1
            save_state(empty_state(), state_path)
            print(f"Initialized {state_path}")
            return 0

        state = load_state(state_path)
        mutated = True

        if args.command == "show":
            print(summarize(state)); mutated = False
        elif args.command == "state":
            print(json.dumps(state, indent=2)); mutated = False
        elif args.command == "view":
            print(json.dumps(build_view(state), indent=2)); mutated = False
        elif args.command == "check":
            notes = validate_state(state)
            for note in notes:
                print(f"note: {note}")
            print(f"State OK — {sum(len(state[c]) for c in COLLECTIONS)} records, "
                  f"{len(notes)} note(s).")
            mutated = False
        elif args.command == "render":
            for path in render_all(state, template_path, Path(args.console), Path(args.mirror)):
                print(f"Rendered {path}")
            mutated = False
        elif args.command == "serve":
            return serve(state_path, template_path, args.port)
        elif args.command == "mission":
            print(set_mission(state, args.mission, args.by, args.date, args.sprint)["mission"])
        elif args.command == "priority-add":
            print(add_priority(state, args.title, args.why, args.owner, args.project)["id"])
        elif args.command == "priority-status":
            print(set_priority_status(state, args.id, args.status)["id"])
        elif args.command == "next-action":
            print(set_next_action(state, args.title, args.owner, args.context, args.priority)["title"])
        elif args.command == "decision-add":
            print(add_decision(state, args.title, args.context, args.recommendation,
                               args.options, args.consequence, args.by)["id"])
        elif args.command == "decision-resolve":
            print(resolve_decision(state, args.id, args.status, args.note)["id"])
        elif args.command == "task-add":
            print(add_task(state, args.title, args.owner, args.why, args.by,
                           args.project, args.gate)["id"])
        elif args.command == "task-state":
            print(set_task_state(state, args.id, args.new_state, args.output)["id"])
        elif args.command == "agent-status":
            print(set_agent_status(state, args.id, args.status, args.notes)["id"])
        elif args.command == "health-set":
            print(set_health(state, args.id, args.status, args.detail, args.source)["id"])
        elif args.command == "blocker-add":
            print(add_blocker(state, args.title, args.impact, args.owner,
                              args.needs_founder, args.blocking_ids)["id"])
        elif args.command == "blocker-resolve":
            print(resolve_blocker(state, args.id, args.note)["id"])
        elif args.command == "repository-health":
            lane = run_repository_health_lane(
                state, args.intention, args.why,
                Path(args.vault).expanduser().resolve(),
                Path(args.report).expanduser().resolve(),
            )
            print(
                f"{lane['task']['id']} -> {lane['run']['id']} -> "
                f"{lane['result']['id']} ({lane['result']['ref']})"
            )
        else:
            raise StateError(f"Unhandled command {args.command!r}")

        if mutated:
            save_state(state, state_path)
            render_all(state, template_path, Path(args.console), Path(args.mirror))
        return 0
    except StateError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
