#!/usr/bin/env python3
"""Entity Registry — canonical identity for actors that are not documents.

The Institutional Knowledge Graph was built on one assumption: every node is a
Markdown document. That assumption is wrong about the Foundation, and the graph
said so — 750 unresolved relationships, of which roughly 630 pointed at `CODEX`,
`LUMIAION`, `Alpha Proxima Foundation` and other *actors*. Those are not missing
documents. They are entities the vault names constantly and models nowhere.

This module gives them canonical identity **without creating a single document**.
Every entity is derived from a registry the Foundation already ratified:

  * `03_AI_COUNCIL/Cognitive Function Registry.md` — CF-01…CF-16. Canonical since
    Epoch V, per the Founder-ratified Governance Model Crosswalk. The Engine
    Registry it replaced is read only for historical aliases.
  * `13_OPERATIONS/Office Registry/Office Registry.md` — the offices.
  * `13_OPERATIONS/AI Council/Agent and Subagent Registry.md` — AGT-001…AGT-016.
  * `00_CONSTITUTION/Book I - The Constitution.md` — the Foundation itself.

Two rules make this safe to build on:

  * **Derived, never authored.** Nothing here invents an entity. If a name is not
    in a registry, it does not resolve, and the graph keeps reporting it. That is
    the difference between modelling the institution and silencing it.
  * **Provenance is mandatory.** Every entity carries `canonical_source`, the
    document that confers its identity. An entity nobody ratified cannot exist.

An alias resolves to at most one entity. Where two registries name the same
actor — LUMIAION is both an office and an engine — the more specific form wins:
`LUMIAION (CF-01)` is the cognitive function, bare `LUMIAION` is the office.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent

SCHEMA_VERSION = "1.0.0"

CF_REGISTRY = Path("03_AI_COUNCIL") / "Cognitive Function Registry.md"
OFFICE_REGISTRY = Path("13_OPERATIONS") / "Office Registry" / "Office Registry.md"
AGENT_REGISTRY = Path("13_OPERATIONS") / "AI Council" / "Agent and Subagent Registry.md"
CONSTITUTION = Path("00_CONSTITUTION") / "Book I - The Constitution.md"

ENTITY_TYPES = ("agent", "office", "organization", "person")

# Frontmatter values that are template scaffolding, not references to anything.
# A template that ships `authors: ["<AUTHOR>"]` is doing its job; counting that
# as a missing actor measures the template, not the institution.
PLACEHOLDER_RE = re.compile(
    r"^(?:<[^>]+>|\[[^\]]+\]|null|none|n/?a|tbd|to be appointed|unappointed|"
    r"owner pending|pending|—|-)$",
    re.IGNORECASE,
)

# Engine cells list alternatives ("Codex / DeepSeek") and qualify them
# ("LUMIAION (multi-engine)", "Perplexity Compute"). Both forms alias the entity.
_ENGINE_SPLIT_RE = re.compile(r"\s*/\s*")
_PARENTHETICAL_RE = re.compile(r"\s*\([^)]*\)\s*$")
_CF_CODE_RE = re.compile(r"\bCF-(\d{2})\b", re.IGNORECASE)
_SEPARATOR_ROW_RE = re.compile(r"^\|?[\s:|-]+\|?$")


class EntityError(Exception):
    """Raised when a canonical registry cannot be read or parsed."""


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def normalize(value: str) -> str:
    """Fold a reference to its comparison key."""
    return re.sub(r"\s+", " ", str(value or "")).strip().lower()


def is_placeholder(value: str) -> bool:
    """True when a frontmatter value is template scaffolding, not a reference."""
    return bool(PLACEHOLDER_RE.match(str(value or "").strip()))


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-") or "unnamed"


def table_rows(text: str, min_columns: int) -> list[list[str]]:
    """Every pipe-table row in a document, as trimmed cells.

    Header and separator rows are dropped. Reading all tables rather than one
    named section keeps this working when a registry is reorganised, which these
    documents are, often.
    """
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or _SEPARATOR_ROW_RE.match(stripped):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) >= min_columns:
            rows.append(cells)
    return rows


def read(root: Path, relative: Path, strict: bool = True) -> str | None:
    """A registry's text, or None when it is absent and absence is tolerated.

    The Truth Kernel builds against any root it is given, including the small
    fixture vaults the test suites use. Those have no Council registries, and a
    hard failure there would make entity resolution impossible to test in
    isolation. So absence degrades instead of raising — but the caller is told
    which sources were missing, and the shipped vault asserts that list is empty.
    """
    path = root / relative
    if not path.exists():
        if strict:
            raise EntityError(f"Canonical registry not found: {relative}")
        return None
    return path.read_text(encoding="utf-8", errors="replace")


def engine_aliases(cell: str) -> list[str]:
    """Alias forms for an engine cell, e.g. 'Codex / DeepSeek' or 'LUMIAION (multi-engine)'."""
    out: list[str] = []
    for part in _ENGINE_SPLIT_RE.split(cell or ""):
        part = part.strip()
        if not part or is_placeholder(part):
            continue
        out.append(part)
        bare = _PARENTHETICAL_RE.sub("", part).strip()
        if bare and bare != part:
            out.append(bare)
        # "ATHENA Office" is cited as an engine; documents credit bare "ATHENA".
        without_office = re.sub(r"\s+Office$", "", bare or part).strip()
        if without_office and without_office not in out:
            out.append(without_office)
    return out


# --------------------------------------------------------------------------
# entity construction
# --------------------------------------------------------------------------

def entity(entity_id: str, entity_type: str, label: str, source: Path,
           status: str = "active", aliases: list[str] | None = None,
           secondary: list[str] | None = None) -> dict[str, Any]:
    """One typed actor.

    Aliases come in two tiers, and the distinction decides real collisions. A
    *primary* alias is a name the registry gives the entity itself — its label,
    its code, its identifier. A *secondary* alias is a name the registry merely
    cites, such as the engine currently fulfilling a function. Engines move
    between functions; labels do not. So `LUMIAION` resolves to the office that
    is named LUMIAION, not to the cognitive function that happens to run on it.
    """
    if entity_type not in ENTITY_TYPES:
        raise EntityError(f"Unknown entity_type: {entity_type}")

    def clean(values: list[str]) -> list[str]:
        seen: dict[str, None] = {}
        for alias in values:
            key = str(alias or "").strip()
            if key and not is_placeholder(key):
                seen.setdefault(key, None)
        return list(seen)

    primary = clean([label, *(aliases or [])])
    secondary_clean = [a for a in clean(secondary or []) if a not in primary]
    return {
        "entity_id": entity_id,
        "entity_type": entity_type,
        "label": label,
        "aliases": primary,
        "secondary_aliases": secondary_clean,
        "canonical_source": source.as_posix(),
        "status": status,
    }


def cognitive_functions(root: Path, strict: bool = True) -> list[dict[str, Any]]:
    """CF-01…CF-16 — canonical since Epoch V."""
    text = read(root, CF_REGISTRY, strict)
    if text is None:
        return []
    out: list[dict[str, Any]] = []
    for cells in table_rows(text, 5):
        match = _CF_CODE_RE.match(cells[0].strip())
        if not match:
            continue
        code = f"CF-{match.group(1)}"
        function, engine, status = cells[1], cells[3], cells[4]
        # "Data & Systems Intelligence (JERANIUM)" — the parenthetical is the
        # legacy department name, and documents still cite it.
        legacy = re.findall(r"\(([^)]+)\)", function)
        bare_function = _PARENTHETICAL_RE.sub("", function).strip()
        aliases = [code, bare_function, f"{code} {bare_function}", *legacy]
        secondary: list[str] = []
        for name in engine_aliases(engine):
            secondary.append(name)
            secondary.append(f"{name} ({code})")
        out.append(entity(f"agent:{code.lower()}", "agent", bare_function,
                          CF_REGISTRY, status.strip().lower() or "active",
                          aliases, secondary))
    if not out and strict:
        raise EntityError(f"No cognitive functions parsed from {CF_REGISTRY}")
    return out


def offices(root: Path, strict: bool = True) -> list[dict[str, Any]]:
    """The offices, from the Office Registry's capability table."""
    text = read(root, OFFICE_REGISTRY, strict)
    if text is None:
        return []
    out: list[dict[str, Any]] = []
    for cells in table_rows(text, 11):
        name = cells[0].strip()
        if not name or name.lower() == "office" or "|" in name:
            continue
        # "LUMIAION / Institutional Intelligence" names one office two ways.
        parts = [p.strip() for p in _ENGINE_SPLIT_RE.split(name) if p.strip()]
        primary = parts[0]
        aliases = list(parts) + [f"{primary} Office"]
        out.append(entity(f"office:{slug(primary)}", "office", primary,
                          OFFICE_REGISTRY, "active", aliases))
    return out


def agents(root: Path, strict: bool = True) -> list[dict[str, Any]]:
    """AGT-001…AGT-016 — named roles, distinct from the functions they serve."""
    text = read(root, AGENT_REGISTRY, strict)
    if text is None:
        return []
    out: list[dict[str, Any]] = []
    for cells in table_rows(text, 6):
        agent_id = cells[0].strip()
        if not re.fullmatch(r"AGT-\d{3}", agent_id):
            continue
        named_role, state = cells[1].strip(), cells[5].strip().lower()
        out.append(entity(f"agent:{agent_id.lower()}", "agent", named_role,
                          AGENT_REGISTRY, state or "available",
                          [agent_id, f"{agent_id} {named_role}"]))
    return out


def organizations() -> list[dict[str, Any]]:
    """The institutional owners named in frontmatter across the whole vault.

    Declared here rather than parsed because the Constitution defines the
    Foundation in prose, not a table. Provenance still points at the document
    that confers the identity; a future constitutional table can replace this
    without changing a single consumer.
    """
    return [
        entity("organization:alpha-proxima-foundation", "organization",
               "Alpha Proxima Foundation", CONSTITUTION, "active",
               ["Alpha Proxima", "The Foundation", "Alpha Proxima Foundation"]),
        entity("organization:osg", "organization", "OSG", CONSTITUTION, "active",
               ["OSG Academy"]),
    ]


def people() -> list[dict[str, Any]]:
    return [
        entity("person:founder", "person", "Founder", CONSTITUTION, "active",
               ["Frederick Belizaire Gunville", "Om Sadhi Guru", "The Founder"]),
    ]


def build(root: Path = VAULT_ROOT, *, strict: bool = True) -> dict[str, Any]:
    """The entity contract: typed actors, each with provenance.

    `strict` decides what a missing registry means. The CLI wants it loud — a
    vault without its Council registries is misconfigured. The Truth Kernel
    wants it survivable, because it indexes fixture roots too, and records
    `missing_sources` so under-resolution is never silent.
    """
    root = Path(root).expanduser().resolve()
    if not root.is_dir():
        raise EntityError(f"Vault root is not a directory: {root}")

    missing = [source.as_posix() for source in
               (CF_REGISTRY, OFFICE_REGISTRY, AGENT_REGISTRY, CONSTITUTION)
               if not (root / source).exists()]

    entities: list[dict[str, Any]] = []
    entities += cognitive_functions(root, strict)
    entities += offices(root, strict)
    entities += agents(root, strict)
    entities += organizations()
    entities += people()

    # One alias, one entity. Earlier sources win, so the canonical Cognitive
    # Function model takes precedence over the offices and the legacy registries
    # it superseded — the crosswalk's ordering, expressed in code.
    index: dict[str, str] = {}
    collisions: list[dict[str, str]] = []
    for tier in ("aliases", "secondary_aliases"):
        for item in entities:
            for alias in item.get(tier, []):
                key = normalize(alias)
                if not key:
                    continue
                if key in index and index[key] != item["entity_id"]:
                    collisions.append({"alias": alias, "tier": tier,
                                       "kept": index[key],
                                       "rejected": item["entity_id"]})
                    continue
                index[key] = item["entity_id"]

    by_type: dict[str, int] = {}
    for item in entities:
        by_type[item["entity_type"]] = by_type.get(item["entity_type"], 0) + 1

    return {
        "schema_version": SCHEMA_VERSION,
        "canonical_sources": [CF_REGISTRY.as_posix(), OFFICE_REGISTRY.as_posix(),
                              AGENT_REGISTRY.as_posix(), CONSTITUTION.as_posix()],
        "missing_sources": missing,
        "entities": entities,
        "alias_index": index,
        "alias_collisions": collisions,
        "counts": {"entities": len(entities), "aliases": len(index),
                   "by_type": by_type},
    }


def resolve(registry: dict[str, Any], reference: str) -> str | None:
    """Entity id for a reference, or None when nothing canonical claims it.

    Tries the literal form first so a qualified reference beats a bare one, then
    falls back to the form without its parenthetical.
    """
    raw = str(reference or "").strip()
    if not raw or is_placeholder(raw):
        return None
    index = registry["alias_index"]
    # `LUMIAION (CF-01)` names CF-01, whatever LUMIAION resolves to on its own.
    code = _CF_CODE_RE.search(raw)
    if code:
        coded = index.get(normalize(f"CF-{code.group(1)}"))
        if coded:
            return coded
    found = index.get(normalize(raw))
    if found:
        return found
    bare = _PARENTHETICAL_RE.sub("", raw).strip()
    if bare and bare != raw:
        return index.get(normalize(bare))
    return None


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ap.py entities", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("view", help="Print the entity contract as JSON.")
    sub.add_parser("check", help="Report entity counts and alias collisions.")
    resolve_cmd = sub.add_parser("resolve", help="Resolve one reference.")
    resolve_cmd.add_argument("reference")

    args = parser.parse_args(argv)
    try:
        registry = build(Path(args.root))
    except EntityError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.command == "view":
        print(json.dumps(registry, indent=2, ensure_ascii=False))
        return 0

    if args.command == "resolve":
        found = resolve(registry, args.reference)
        print(found or "(unresolved)")
        return 0 if found else 1

    counts = registry["counts"]
    print(f"Entities: {counts['entities']} across {len(counts['by_type'])} types")
    for entity_type, total in sorted(counts["by_type"].items()):
        print(f"  {entity_type:<14} {total}")
    print(f"Aliases:  {counts['aliases']}")
    if registry["alias_collisions"]:
        print(f"\n{len(registry['alias_collisions'])} alias collision(s) "
              f"— first registry wins:")
        for item in registry["alias_collisions"][:10]:
            print(f"  {item['alias']}: kept {item['kept']}, rejected {item['rejected']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
