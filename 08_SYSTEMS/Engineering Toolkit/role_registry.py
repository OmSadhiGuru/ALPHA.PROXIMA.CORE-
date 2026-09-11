#!/usr/bin/env python3
"""Parse the Agent and Subagent Registry into a validated read model.

`13_OPERATIONS/AI Council/Agent and Subagent Registry.md` names the sixteen
non-voting agent roles the Council may route work to, each with a bounded set
of subagent kinds it may instantiate, and the Founder-approved availability
state (`available`, `advisory-only`, `blocked`) each currently holds.

This module reads that one document. It never writes it: the registry is
Founder-approved governance content, edited by a human, versioned in its own
Version History table -- not operational state a program should mutate. Two
consumers depend on this parse being faithful rather than a re-summary:
`council_kernel.py` derives its role-availability gate from it (replacing a
hand-maintained, driftable duplicate of the same three sets), and
`office_spatial.py` groups the sixteen roles into desks by `operating_owner`
for the read-only 3D view. Neither should ever see a normalized or
reinterpreted version of a field -- e.g. `operating_owner` for AGT-010 is the
literal string "Ethics Council when convened", not "Ethics Council": fidelity
to the source document is the entire point of parsing it instead of
hand-copying it a second time.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
DEFAULT_REGISTRY_PATH = (
    VAULT_ROOT / "13_OPERATIONS" / "AI Council" / "Agent and Subagent Registry.md"
)

SCHEMA_VERSION = "1.0.0"
VALID_ROLE_STATES = {"available", "advisory-only", "blocked"}
ROLE_ID_RE = re.compile(r"^AGT-\d{3}$")

_SEPARATOR_ROW_RE = re.compile(r"^\|?[\s:|-]+\|?$")
_VERSION_FRONTMATTER_RE = re.compile(r'^version:\s*"?([^"\n]+)"?\s*$', re.MULTILINE)
_INVOCATION_RULE_RE = re.compile(r"^\d+\.\s+(.*)$")


class RegistryError(Exception):
    """Raised when the registry document cannot be found, parsed, or is structurally invalid."""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# --------------------------------------------------------------------------
# table extraction
# --------------------------------------------------------------------------

def _section_lines(text: str, heading: str) -> list[str]:
    """Every line between a `### heading` and the next heading of any level."""
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip().lstrip("#").strip() == heading and line.lstrip().startswith("#"):
            start = index + 1
            break
    if start is None:
        raise RegistryError(f"{heading!r} section not found in registry document.")
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].lstrip().startswith("#"):
            end = index
            break
    return lines[start:end]


def _table_rows(lines: list[str], expected_columns: int) -> list[list[str]]:
    """Parse consecutive `| a | b | ... |` lines into cell lists, header/separator dropped."""
    raw_rows = [line for line in lines if line.strip().startswith("|")]
    if not raw_rows:
        raise RegistryError("No table found where one was expected in the registry document.")
    data_rows = [row for row in raw_rows if not _SEPARATOR_ROW_RE.match(row.strip())]
    if len(data_rows) < 2:
        raise RegistryError("Table has no data rows after its header.")
    data_rows = data_rows[1:]  # drop the header row itself

    parsed: list[list[str]] = []
    for raw in data_rows:
        cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
        if len(cells) != expected_columns:
            raise RegistryError(f"Malformed table row (expected {expected_columns} columns): {raw!r}")
        parsed.append(cells)
    return parsed


# --------------------------------------------------------------------------
# per-table parsers
# --------------------------------------------------------------------------

def parse_roles_table(markdown_text: str) -> list[dict[str, Any]]:
    rows = _table_rows(_section_lines(markdown_text, "Agent Roles"), expected_columns=7)
    roles: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for cells in rows:
        role_id, named_role, parent_function, operating_owner, current_implementation, state, may_instantiate = cells
        if not ROLE_ID_RE.fullmatch(role_id):
            raise RegistryError(f"Malformed role ID {role_id!r} in registry.")
        if role_id in seen_ids:
            raise RegistryError(f"Duplicate role ID {role_id!r} in registry.")
        seen_ids.add(role_id)
        normalized_state = state.strip().lower()
        if normalized_state not in VALID_ROLE_STATES:
            raise RegistryError(
                f"Role {role_id} has unrecognized state {state!r}; expected one of {sorted(VALID_ROLE_STATES)}."
            )
        roles.append({
            "id": role_id,
            "named_role": named_role,
            "parent_function": parent_function,
            "operating_owner": operating_owner,
            "current_implementation": current_implementation,
            "state": normalized_state,
            "may_instantiate": [part.strip() for part in may_instantiate.split(";") if part.strip()],
        })
    if not roles:
        raise RegistryError("Roles table parsed with zero rows — check the document has not been reshaped.")
    return roles


def parse_subagent_profiles_table(markdown_text: str) -> list[dict[str, str]]:
    rows = _table_rows(_section_lines(markdown_text, "Standard Subagent Profiles"), expected_columns=3)
    return [
        {"profile": profile, "output": output, "boundary": boundary}
        for profile, output, boundary in rows
    ]


def parse_invocation_rules(markdown_text: str) -> list[str]:
    lines = _section_lines(markdown_text, "Invocation Rules")
    rules = []
    for line in lines:
        match = _INVOCATION_RULE_RE.match(line.strip())
        if match:
            rules.append(match.group(1).strip())
    if not rules:
        raise RegistryError("Invocation Rules section parsed with zero rules.")
    return rules


def _document_version(markdown_text: str) -> str:
    match = _VERSION_FRONTMATTER_RE.search(markdown_text)
    return match.group(1) if match else ""


# --------------------------------------------------------------------------
# grouping + the public read model
# --------------------------------------------------------------------------

def _owners(roles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Group role ids by `operating_owner`, preserving first-seen (registry) order."""
    order: list[str] = []
    grouped: dict[str, list[str]] = {}
    for record in roles:
        owner = record["operating_owner"]
        if owner not in grouped:
            grouped[owner] = []
            order.append(owner)
        grouped[owner].append(record["id"])
    return [{"owner": owner, "role_ids": grouped[owner]} for owner in order]


def load_roles(root: Path = VAULT_ROOT, *, path: Path | None = None) -> dict[str, Any]:
    """The registry as one read model: roles, subagent profiles, rules, owner groups.

    Re-parses the document on every call. The registry is small (sixteen
    rows) and changes only when a human edits it; caching would mean a
    `council run` or `office serve` could act on a stale classification the
    moment the document is edited without a process restart -- the one
    failure mode every other read model in this toolkit is built to avoid.
    """
    registry_path = path if path is not None else (root / "13_OPERATIONS" / "AI Council" / "Agent and Subagent Registry.md")
    if not registry_path.exists():
        raise RegistryError(f"Registry not found: {registry_path}.")
    text = registry_path.read_text(encoding="utf-8")

    roles = parse_roles_table(text)
    subagent_profiles = parse_subagent_profiles_table(text)
    invocation_rules = parse_invocation_rules(text)

    try:
        source_path = str(registry_path.relative_to(root))
    except ValueError:
        source_path = str(registry_path)

    counts = {
        "roles": len(roles),
        "available": sum(1 for r in roles if r["state"] == "available"),
        "advisory_only": sum(1 for r in roles if r["state"] == "advisory-only"),
        "blocked": sum(1 for r in roles if r["state"] == "blocked"),
    }
    owners = _owners(roles)
    counts["owners"] = len(owners)

    return {
        "schema_version": SCHEMA_VERSION,
        "source_path": source_path,
        "generated_at": now_iso(),
        "document_version": _document_version(text),
        "roles": roles,
        "subagent_profiles": subagent_profiles,
        "invocation_rules": invocation_rules,
        "owners": owners,
        "counts": counts,
    }


def role(registry: dict[str, Any], role_id: str) -> dict[str, Any]:
    for record in registry["roles"]:
        if record["id"] == role_id:
            return record
    raise RegistryError(f"No role {role_id!r} in the registry.")


# --------------------------------------------------------------------------
# CLI (read-only: view the parsed registry as JSON)
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    import argparse
    import json

    parser = argparse.ArgumentParser(prog="ap.py role-registry", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("view", help="Print the parsed registry as JSON.")
    sub.add_parser("check", help="Parse the registry and report counts, or fail with a reason.")
    args = parser.parse_args(argv)

    try:
        registry = load_roles(Path(args.root))
        if args.command == "view":
            print(json.dumps(registry, indent=2, ensure_ascii=False))
            return 0
        if args.command == "check":
            counts = registry["counts"]
            print(
                f"Registry OK — {counts['roles']} roles across {counts['owners']} owners "
                f"({counts['available']} available, {counts['advisory_only']} advisory-only, "
                f"{counts['blocked']} blocked)."
            )
            return 0
    except RegistryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
