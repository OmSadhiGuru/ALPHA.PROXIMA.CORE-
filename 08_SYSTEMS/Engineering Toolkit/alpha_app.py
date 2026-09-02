#!/usr/bin/env python3
"""Alpha Proxima App — one interface over the Foundation's two halves.

The Foundation does two things: it *operates* (missions, priorities, decisions,
agents, execution) and it *knows* (a constitution, a council, research programs,
systems, standards). Until now those halves had separate surfaces: Founder OS
rendered a Console from `founder-state.json`, and the knowledge base was read
directly in Obsidian. This module composes both into a single application shell.

It is a presentation layer and nothing else. Two rules keep it that way:

  * **It writes nothing.** Founder state is written only by `founder_os`; vault
    notes are written only by their authors. This module reads, indexes, and
    renders. There is still exactly one writer per source of truth.
  * **It never copies vault content.** The knowledge half is an *index* that
    routes to notes, not a second copy of them. A note's text lives in exactly
    one place: the note. This is the Library Rule in code — the app makes the
    connections between documents visible without duplicating the documents.

Design constraints (inherited from `Founder OS Architecture v1`):
  * standard library only -- the Vault gains no runtime dependency;
  * derived views are generated and carry a banner; they are never hand-edited;
  * every presentation layer consumes the read model (`build_app_view`), never
    the renderer, so a later spatial, voice, or accessible interface needs no
    backend change;
  * loopback only. `FD-002` is ratified: the app ships no authentication
    because it is not reachable off-host. Hosting is a separate decision.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
APP_DIR = VAULT_ROOT / "13_OPERATIONS" / "Alpha Proxima App"
DEFAULT_TEMPLATE = APP_DIR / "app" / "app.template.html"
DEFAULT_APP = APP_DIR / "app" / "app.html"
DEFAULT_INDEX = APP_DIR / "app" / "vault-index.json"

APP_VERSION = "1.2.0"

VIEW_PLACEHOLDER = "/*__ALPHA_APP_VIEW__*/null"

# The canonical top-level hierarchy, in constitutional order, with the question
# each domain answers. Order is meaning here: 00 governs 13, never the reverse.
# Source: `10_TEMPLATES/Vault Structure Convention.md`.
DOMAINS: tuple[tuple[str, str, str], ...] = (
    ("00_CONSTITUTION", "Constitution", "What may not be violated"),
    ("01_VISION", "Vision", "Where the Foundation is going"),
    ("02_STRATEGY", "Strategy", "How it intends to get there"),
    ("03_AI_COUNCIL", "AI Council", "Who reasons on its behalf"),
    ("04_DECISIONS", "Decisions", "What has been settled"),
    ("05_PROPOSALS", "Proposals", "What is being considered"),
    ("06_GOVERNANCE", "Governance", "How institutional authority is constrained"),
    ("07_RESEARCH", "Research", "What is being investigated"),
    ("08_SYSTEMS", "Systems", "How the Foundation works"),
    ("09_OFFICES", "Offices", "Where institutional authority is housed"),
    ("10_TEMPLATES", "Templates", "How new knowledge is shaped"),
    ("11_PROJECTS", "Projects", "What is being built"),
    ("12_PEOPLE", "People", "Who the Foundation involves"),
    ("13_OPERATIONS", "Operations", "What is happening now"),
    ("14_FUTURE", "Future", "What is not yet due"),
    ("99_ARCHIVE", "Archive", "What has been retired"),
)

DOMAIN_ORDER = {prefix: index for index, (prefix, _, _) in enumerate(DOMAINS)}
DOMAIN_NAMES = {prefix: name for prefix, name, _ in DOMAINS}

# Folders that hold no institutional canon. Excluded from the knowledge index so
# the app reflects the Foundation, not its scaffolding.
EXCLUDED_TOPS = {
    ".obsidian", ".smart-env", ".makemd", ".space", ".claudian",
    "copilot", "Omi", "Tags",
}


class AppError(Exception):
    """Raised when the app cannot build or render a view."""


# --------------------------------------------------------------------------
# shared-module loading
# --------------------------------------------------------------------------

def _load_sibling(filename: str, name: str):
    """Import a toolkit module by path.

    `ap.py` execs tools into synthetic module namespaces, so ordinary imports
    are not available. This mirrors the loader `node_registry.py` already uses,
    which keeps the toolkit's single-file-per-tool property intact.
    """
    path = (TOOLKIT_DIR / filename).resolve()
    if not path.exists():
        raise AppError(f"Required toolkit module not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AppError(f"Unable to load toolkit module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


vault_validator = _load_sibling("vault_validator.py", "vault_validator")
founder_os = _load_sibling("founder_os.py", "founder_os")


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower())
    return value.strip("-") or "untitled"


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if value in (None, ""):
        return []
    return [str(value).strip()]


def as_text(value: Any) -> str:
    if value in (None, ""):
        return ""
    return str(value).strip()


def domain_of(relative_path: str) -> str:
    return relative_path.split("/", 1)[0] if "/" in relative_path else "root"


INLINE_CODE_RE = re.compile(r"`+[^`\n]*`+")


def link_targets(note) -> list[str]:
    """Outgoing wiki-links, excluding any that appear inside code.

    Code is stripped first -- fenced blocks, then inline spans -- so a link
    quoted as an example in a template or a standard does not become an
    institutional relationship. Both forms are documentation about links, not
    links; counting them would inflate connectedness with fiction and report
    phantom broken references.
    """
    body = INLINE_CODE_RE.sub(" ", vault_validator.strip_fenced_blocks(note.body))
    raw = re.findall(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", body)
    raw += [
        item[2:-2]
        for field in ("dependencies", "related_documents", "related_research_programs")
        for item in as_list(note.frontmatter.get(field))
        if item.startswith("[[") and item.endswith("]]")
    ]
    seen: dict[str, None] = {}
    for target in raw:
        cleaned = target.split("|", 1)[0].split("#", 1)[0].strip()
        if cleaned:
            seen.setdefault(cleaned, None)
    return list(seen)


# --------------------------------------------------------------------------
# the knowledge half -- vault index
# --------------------------------------------------------------------------

def index_entry(note, root: Path) -> dict[str, Any]:
    """One compact record per note.

    Deliberately excludes note bodies. The index describes and routes to a
    document; it never becomes a second copy of it.
    """
    front = note.frontmatter
    title = as_text(front.get("title")) or note.path.stem
    return {
        "id": slugify(note.relative_path),
        "path": note.relative_path,
        "title": title,
        "domain": domain_of(note.relative_path),
        "type": as_text(front.get("artifact_type")) or "unclassified",
        "status": as_text(front.get("status")) or "unknown",
        "version": as_text(front.get("version")),
        "owner": as_text(front.get("institutional_owner")),
        "function": as_text(front.get("cognitive_function")),
        "engine": as_text(front.get("reasoning_engine")),
        "authors": as_list(front.get("authors")),
        "tags": as_list(front.get("tags")),
        "updated": as_text(front.get("updated")) or as_text(front.get("created")),
        "has_frontmatter": note.has_frontmatter,
        "words": len(note.body.split()),
        "links": link_targets(note),
    }


def resolve_links(entries: list[dict[str, Any]]) -> None:
    """Turn wiki-link text into entry ids, in place.

    A link is institutional only when it lands somewhere. Targets that resolve
    become edges; targets that do not are kept separately as `unresolved`, which
    is exactly the signal CN-001 needs — a broken link is a coherence defect,
    not something to silently drop.
    """
    by_name: dict[str, str] = {}
    for entry in entries:
        for name in (entry["title"], Path(entry["path"]).stem):
            by_name.setdefault(name.lower(), entry["id"])

    for entry in entries:
        resolved: list[str] = []
        unresolved: list[str] = []
        for raw in entry.pop("links"):
            target = by_name.get(raw.lower())
            if target is None:
                unresolved.append(raw)
            elif target != entry["id"] and target not in resolved:
                resolved.append(target)
        entry["links"] = resolved
        entry["unresolved"] = unresolved


def build_vault_index(root: Path) -> dict[str, Any]:
    """Index the Foundation's knowledge, one record per note.

    Backlinks are derived rather than stored: storing both directions would put
    the same fact in two places, which is the duplication this whole module
    exists to avoid. Consumers invert `links` when they need the reverse edge.
    """
    if not root.exists():
        raise AppError(f"Vault root not found: {root}")

    notes = [
        note
        for note in vault_validator.load_notes(root, include_hidden=False)
        if domain_of(note.relative_path) not in EXCLUDED_TOPS
        and not note.relative_path.startswith(".")
    ]
    entries = [index_entry(note, root) for note in notes]
    resolve_links(entries)

    entries.sort(key=lambda e: (DOMAIN_ORDER.get(e["domain"], 99), e["path"].lower()))

    inbound: Counter[str] = Counter()
    for entry in entries:
        inbound.update(entry["links"])
    for entry in entries:
        entry["backlinks"] = inbound.get(entry["id"], 0)

    present = {entry["domain"] for entry in entries}
    domains = [
        {
            "id": prefix,
            "name": name,
            "question": question,
            "count": sum(1 for e in entries if e["domain"] == prefix),
        }
        for prefix, name, question in DOMAINS
        if prefix in present
    ]
    loose = sorted(present - set(DOMAIN_ORDER))
    domains += [
        {
            "id": prefix,
            "name": prefix.replace("_", " ").title(),
            "question": "Not yet placed in the canonical hierarchy",
            "count": sum(1 for e in entries if e["domain"] == prefix),
        }
        for prefix in loose
    ]

    return {
        "generated_at": now_iso(),
        "note_count": len(entries),
        "domains": domains,
        "entries": entries,
        "coherence": coherence_report(entries),
        "facets": {
            "type": Counter(e["type"] for e in entries).most_common(),
            "status": Counter(e["status"] for e in entries).most_common(),
            "function": Counter(e["function"] for e in entries if e["function"]).most_common(),
        },
    }


def coherence_report(entries: list[dict[str, Any]]) -> dict[str, Any]:
    """Make the Library Rule measurable.

    "Never create isolated information" is a constitutional principle. Without a
    number attached it stays an aspiration, so the app reports it: how many
    documents connect to nothing, how many carry no metadata, how many point at
    documents that do not exist. These are the inputs CN-001 needs and the only
    metrics in this application — each one names a repair, not a trend.
    """
    inbound: Counter[str] = Counter()
    for entry in entries:
        inbound.update(entry["links"])

    orphans = [
        {"id": e["id"], "path": e["path"], "title": e["title"], "domain": e["domain"]}
        for e in entries
        if not e["links"] and not inbound.get(e["id"])
    ]
    unmetadated = [
        {"id": e["id"], "path": e["path"], "title": e["title"], "domain": e["domain"]}
        for e in entries
        if not e["has_frontmatter"]
    ]
    broken = [
        {"id": e["id"], "path": e["path"], "title": e["title"], "targets": e["unresolved"]}
        for e in entries
        if e["unresolved"]
    ]
    empty = [
        {"id": e["id"], "path": e["path"], "title": e["title"], "domain": e["domain"]}
        for e in entries
        if e["words"] == 0
    ]

    total = len(entries) or 1
    connected = total - len(orphans)
    return {
        "note_count": len(entries),
        "connected": connected,
        "connectedness": round(connected / total, 4),
        "orphans": sorted(orphans, key=lambda o: o["path"]),
        "missing_frontmatter": sorted(unmetadated, key=lambda o: o["path"]),
        "broken_links": sorted(broken, key=lambda o: o["path"]),
        "empty_notes": sorted(empty, key=lambda o: o["path"]),
        "counts": {
            "orphans": len(orphans),
            "missing_frontmatter": len(unmetadated),
            "broken_links": sum(len(b["targets"]) for b in broken),
            "empty_notes": len(empty),
        },
    }


# --------------------------------------------------------------------------
# the composed read model
# --------------------------------------------------------------------------

def build_app_view(state: dict, root: Path) -> dict[str, Any]:
    """The application's read model: both halves, one document.

    This is the contract a second interface consumes — a spatial layer, a voice
    layer, an accessible layer. None of them need to know how state is stored or
    how the vault is laid out.
    """
    operate = founder_os.build_view(state)
    know = build_vault_index(root)
    return {
        "app_version": APP_VERSION,
        "generated_at": now_iso(),
        "today": operate["today"],
        "founder": operate["founder"],
        "operate": operate,
        "know": know,
        "halves": [
            {"id": "operate", "name": "Operate", "question": "What is happening now?",
             "count": operate["counts"]["priorities"] + operate["counts"]["decisions"]},
            {"id": "know", "name": "Know", "question": "What does the Foundation know?",
             "count": know["note_count"]},
        ],
    }


# --------------------------------------------------------------------------
# renderer
# --------------------------------------------------------------------------

def render_app(view: dict, template_path: Path) -> str:
    """Inline the read model so the page works from `file://` with no server."""
    if not template_path.exists():
        raise AppError(f"App template not found: {template_path}")
    template = template_path.read_text(encoding="utf-8")
    if VIEW_PLACEHOLDER not in template:
        raise AppError(f"App template is missing the {VIEW_PLACEHOLDER} placeholder.")
    payload = json.dumps(view, ensure_ascii=False, separators=(",", ":"))
    # Prevent an embedded </script> inside data from terminating the tag early.
    payload = payload.replace("</", "<\\/")
    return template.replace(VIEW_PLACEHOLDER, payload)


def write_outputs(view: dict, template_path: Path, app_path: Path,
                  index_path: Path | None) -> list[Path]:
    written = [app_path]
    app_path.parent.mkdir(parents=True, exist_ok=True)
    app_path.write_text(render_app(view, template_path), encoding="utf-8")
    if index_path is not None:
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(
            json.dumps(view["know"], indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        written.append(index_path)
    return written


# --------------------------------------------------------------------------
# terminal summary
# --------------------------------------------------------------------------

def summarize(view: dict) -> str:
    operate, know = view["operate"], view["know"]
    coherence = know["coherence"]
    lines = [
        f"ALPHA PROXIMA · {view['today']}",
        "",
        "OPERATE",
        f"  mission      {(operate['mission'] or {}).get('mission', '— none set —')}"
        + ("  [STALE]" if operate["mission_is_stale"] else ""),
        f"  priorities   {operate['counts']['priorities']} open",
        f"  decisions    {operate['counts']['decisions']} awaiting the Founder",
        f"  tasks        {operate['counts']['tasks']} active",
        f"  blockers     {operate['counts']['blockers']} open "
        f"({operate['counts']['founder_blockers']} need the Founder)",
        "",
        "KNOW",
        f"  notes        {know['note_count']} across {len(know['domains'])} domains",
        f"  connected    {coherence['connected']}/{coherence['note_count']}"
        f"  ({coherence['connectedness'] * 100:.1f}%)",
        f"  orphans      {coherence['counts']['orphans']}",
        f"  no metadata  {coherence['counts']['missing_frontmatter']}",
        f"  broken links {coherence['counts']['broken_links']}",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# localhost server -- the contract future presentation layers consume
# --------------------------------------------------------------------------

def serve(state_path: Path, root: Path, template_path: Path, port: int = 8788) -> int:
    """Serve the app and its read model on loopback only.

    Binding to 127.0.0.1 keeps the Foundation's state and index private by
    default: no authentication system is required because the socket is not
    reachable off-host. Exposing this beyond loopback is a Founder decision
    (`FD-002`, ratified), and would have to ship authentication first.
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

        def _json(self, payload: Any, status: int = 200) -> None:
            self._send(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"),
                       "application/json; charset=utf-8", status)

        def do_GET(self) -> None:  # noqa: N802 - stdlib naming
            try:
                state = founder_os.load_state(state_path)
                if self.path in ("/", "/index.html", "/app.html"):
                    view = build_app_view(state, root)
                    self._send(render_app(view, template_path).encode("utf-8"),
                               "text/html; charset=utf-8")
                elif self.path == "/api/app":
                    self._json(build_app_view(state, root))
                elif self.path == "/api/view":
                    self._json(founder_os.build_view(state))
                elif self.path == "/api/vault":
                    self._json(build_vault_index(root))
                elif self.path == "/api/state":
                    self._json(state)
                else:
                    self._json({"error": "not found"}, 404)
            except (AppError, founder_os.StateError) as exc:
                self._json({"error": str(exc)}, 500)

        def log_message(self, *args) -> None:  # keep the terminal calm
            pass

    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Alpha Proxima App: http://127.0.0.1:{port}/")
    print(f"Read model:        http://127.0.0.1:{port}/api/app")
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
    parser = argparse.ArgumentParser(prog="ap.py app", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT), help="Vault root to index.")
    parser.add_argument("--state", default=str(founder_os.DEFAULT_STATE),
                        help="Path to founder-state.json.")
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="App template path.")
    parser.add_argument("--app", default=str(DEFAULT_APP), help="Rendered app output.")
    parser.add_argument("--index", default=str(DEFAULT_INDEX), help="Vault index output.")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("render", help="Regenerate app.html and vault-index.json.")
    sub.add_parser("show", help="Print both halves in the terminal.")
    check_cmd = sub.add_parser(
        "check", help="Report coherence defects against an agreed ceiling.")
    check_cmd.add_argument(
        "--max-defects", type=int, default=0, metavar="N",
        help="Defects tolerated before this command fails. The Foundation lowers "
             "this number as CN-001 repairs the vault; it should never be raised.")
    sub.add_parser("index", help="Print the vault index as JSON.")
    sub.add_parser("view", help="Print the composed read model as JSON.")
    serve_cmd = sub.add_parser("serve", help="Serve the app on 127.0.0.1.")
    serve_cmd.add_argument("--port", type=int, default=8788)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    state_path = Path(args.state)
    template_path = Path(args.template)

    try:
        if args.command == "serve":
            return serve(state_path, root, template_path, args.port)

        if args.command == "index":
            print(json.dumps(build_vault_index(root), indent=2, ensure_ascii=False))
            return 0

        state = founder_os.load_state(state_path)
        view = build_app_view(state, root)

        if args.command == "view":
            print(json.dumps(view, indent=2, ensure_ascii=False))
            return 0

        if args.command == "show":
            print(summarize(view))
            return 0

        if args.command == "check":
            coherence = view["know"]["coherence"]
            print(summarize(view))
            defects = sum(coherence["counts"].values())
            ceiling = args.max_defects
            print()
            if not defects:
                print("No coherence defects.")
                return 0
            print(f"{defects} coherence defect(s) against a ceiling of {ceiling}.")
            if defects > ceiling:
                print("Above the ceiling. Repairs belong to CN-001, which owns the taxonomy.")
                return 1
            print("Within the agreed ceiling. Lower it as CN-001 closes the gap.")
            return 0

        if args.command == "render":
            written = write_outputs(view, template_path, Path(args.app), Path(args.index))
            for path in written:
                print(f"wrote {path}")
            return 0
    except (AppError, founder_os.StateError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
