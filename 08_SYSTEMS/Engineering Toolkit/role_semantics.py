#!/usr/bin/env python3
"""Role Semantics -- what each of the Foundation's forty-two entities is *for*.

`entity_registry.py` answers "who exists": forty-two typed actors, each with the
document that confers its identity. It deliberately answers nothing else. Ask it
what CF-07 is responsible for, who an office answers to, or whether an agent role
has a mandate, and it is silent -- correctly, because identity and semantics are
different claims and conflating them is how registries start inventing things.

This module answers the second question, under the same discipline:

  * **Derived, never authored.** Every field here is lifted from a registry the
    Foundation already ratified. This module adds no responsibility, no authority
    and no reporting line that a document does not already state. Where a registry
    is silent, the field is absent and the absence is reported. A semantics layer
    that fills gaps with plausible text is worse than no semantics layer, because
    the Foundation would then read its own guesses back as canon.
  * **Provenance per field, not per entity.** `entity_registry` records one
    `canonical_source` per actor. That is too coarse here: an office's authority
    comes from one table cell and its dependencies from another, and a reader
    checking a single claim should not have to re-derive which. Every field
    carries `source` (the document) and `locator` (the heading, row and column
    inside it).
  * **Never fuzzy-match identity.** Links between entities resolve by exact alias
    through `entity_registry`, constrained by the type the field declares. Where
    no exact match exists the link is unresolved, with the reason named. Deciding
    that `Implementation` means `Engineering Intelligence` because the words feel
    related would be inventing an institutional attribution out of a resemblance
    -- the same class of error as fabricating a graph edge.

## Two authored formats

The Cognitive Function Registry is written two ways. CF-01 through CF-14 use
`### Purpose` sections. CF-15 and CF-16 use inline `**Purpose.**` paragraphs with
their metadata on one middot-separated line. Both are canonical; the compact form
is how the Epoch V reconciliation registered JERANIUM and YUNA.

A parser that reads only headings reports CF-15 and CF-16 as empty. They are not
empty -- CF-15 states a purpose, a mission, primary responsibilities, boundaries
and a succession rule. This module reads both formats and normalises them onto one
field vocabulary, so a consumer never has to know which form an entry uses. The
divergence itself is reported as a finding: a canonical registry with two shapes
will keep breaking derived layers until it has one.

## The direction that works

The Cognitive Function Registry names each function's `Intelligence Office`, and
that direction resolves. The Office Registry's `Responsible Cognitive Function`
column uses a different vocabulary -- `Orchestration`, `Architecture`,
`Implementation` -- and matches no cognitive function label at all. So the
function-to-office binding is derived from the Cognitive Function Registry, and
the Office Registry's column is reported as awaiting reconciliation. Seven rows,
zero matches: that is a vocabulary decision for the Founder, not an arithmetic
problem for a parser.

## Severity

Findings use the vocabulary the Truth Kernel and the Live Integration Layer
already use, so one reader can weigh them together:

  * `error`   -- the layer is unsound. A link that cannot be trusted, an entity
                 with no identity, a duplicate. None are expected; the checks run
                 anyway, because a check that only appears when it fails leaves a
                 reader unable to tell a clean result from an absent one.
  * `warning` -- real, and not invalidating. A ratified function missing its
                 responsibilities; an office cited by a function but absent from
                 the Office Registry.
  * `info`    -- the expected state of something incomplete on purpose. CF-15's
                 engine is `[To be appointed]`; AGT-015 is `blocked` until that
                 appointment. Reporting those as problems would train the reader
                 to ignore the report.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent

sys.path.insert(0, str(TOOLKIT_DIR))
import entity_registry as er  # noqa: E402  (path-based sibling import, as the toolkit does elsewhere)
import role_registry as rr  # noqa: E402  (the agent table already has a parser; do not write a second)

SCHEMA_VERSION = "1.0.0"

#: What kind of role an entity plays. `entity_registry` types CF-07 and AGT-007
#: both as `agent`, which is right for identity and too coarse here: a cognitive
#: function is a standing mandate, an agent role is a dispatchable instance of one.
ROLE_CLASSES = ("cognitive_function", "agent_role", "office", "organization", "person")

#: One field vocabulary, whatever format the source used. Consumers read these
#: names; they never read `### Primary Responsibilities` or `**Boundaries.**`.
SEMANTIC_FIELDS = (
    "purpose", "mission", "authority", "inputs", "outputs", "responsibilities",
    "limitations", "review_cycle", "succession", "artifacts", "dependencies",
    "operating_owner", "implementation", "may_instantiate", "engine",
    "category", "status",
)

#: What each role class can have. Coverage is measured against this, never against
#: the union -- an office has no succession rule to be missing.
EXPECTED_FIELDS: dict[str, tuple[str, ...]] = {
    "cognitive_function": ("purpose", "mission", "authority", "inputs", "outputs",
                           "responsibilities", "limitations", "review_cycle",
                           "succession", "engine", "category", "status"),
    "agent_role": ("operating_owner", "implementation", "may_instantiate", "status"),
    "office": ("purpose", "authority", "inputs", "outputs", "artifacts",
               "review_cycle", "dependencies"),
    "organization": (),
    "person": (),
}

#: Sectioned form (CF-01..CF-14): heading -> canonical field.
CF_SECTION_FIELDS: dict[str, str] = {
    "Purpose": "purpose",
    "Mission": "mission",
    "Authority": "authority",
    "Inputs": "inputs",
    "Outputs": "outputs",
    "Primary Responsibilities": "responsibilities",
    "Limitations": "limitations",
    "Review Cycle": "review_cycle",
    "Succession Rules": "succession",
}

#: Compact form (CF-15, CF-16): inline bold label -> canonical field. `Boundaries`
#: is the compact form's word for what the sectioned form calls `Limitations`;
#: normalising them is reading two dialects of one registry, not equating two
#: different claims.
CF_INLINE_FIELDS: dict[str, str] = {
    "Purpose": "purpose",
    "Mission": "mission",
    "Primary responsibilities": "responsibilities",
    "Boundaries": "limitations",
    "Succession": "succession",
}

#: Office Registry column header -> canonical field. Resolved by header name, not
#: by position, so inserting a column does not silently re-point every field.
OFFICE_COLUMN_FIELDS: dict[str, str] = {
    "Purpose": "purpose",
    "Authority": "authority",
    "Inputs": "inputs",
    "Outputs": "outputs",
    "Artifacts Produced": "artifacts",
    "Review Cycle": "review_cycle",
    "Dependencies": "dependencies",
}

OFFICE_CF_COLUMN = "Responsible Cognitive Function"
OFFICE_ENGINE_COLUMN = "Preferred Reasoning Engine"

#: Fields whose value is a list. Everything else is a string.
LIST_FIELDS = frozenset({"authority", "inputs", "outputs", "responsibilities",
                         "limitations", "review_cycle", "artifacts",
                         "dependencies", "may_instantiate"})

#: The relationship types that carry escalation, in the registry's own words. Only
#: these become an escalation edge. `Upstream supplier` and `Collaborator` describe
#: how work flows, not who answers to whom, and promoting them would manufacture a
#: reporting structure the Foundation has not written down.
ESCALATION_TYPES = ("Accountable to",)
OVERSIGHT_TYPES = ("Reviews",)

#: `All functions` is an authored broadcast target, not a missing entity. It stays
#: one edge with no `target_entity_id`; expanding it into sixteen would be
#: fabricating fifteen relationships the registry never wrote.
COLLECTIVE_TARGETS = frozenset({"all functions", "all cognitive functions"})

_CF_HEADING_RE = re.compile(r"^## (CF-\d{2})\s*[—-]\s*(.+?)\s*$", re.MULTILINE)
_SECTION_RE = r"^### {heading}\s*$(.*?)(?=^#{{2,3}} |\Z)"
_BOLD_KV_RE = re.compile(r"\*\*([A-Za-z][A-Za-z &]*?):\*\*\s*([^*\n·]+)")
_BULLET_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(.*)$")
#: Every registry entry ends with a `---` rule. It belongs to the document's
#: layout, not to the last field, and a field value carrying it would be quoting
#: punctuation back to the reader as institutional text.
_RULE_RE = re.compile(r"^\s*-{3,}\s*$", re.MULTILINE)


class SemanticsError(Exception):
    """Raised when a source registry cannot be read at all."""


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


# --------------------------------------------------------------------------
# fields and provenance
# --------------------------------------------------------------------------

def field(value: Any, source: str, locator: str) -> dict[str, Any]:
    """One derived value and the exact place it came from.

    A reader who doubts a single claim should be able to check that claim alone.
    That is only possible if provenance is attached to the claim rather than to
    the document as a whole.
    """
    return {"value": value, "source": source, "locator": locator}


def _strip_rule(text: str) -> str:
    """Drop trailing `---` separators from a captured field body."""
    return _RULE_RE.sub("", text).strip()


def _bullets(text: str) -> list[str]:
    """Bullet or numbered items, in document order.

    Falls back to the whole paragraph as a single item when a field the registry
    writes as a list is written as prose somewhere. Returning `[]` there would
    report an authored field as missing.
    """
    items = [m.group(1).strip() for line in text.splitlines()
             for m in [_BULLET_RE.match(line)] if m and m.group(1).strip()]
    if items:
        return items
    prose = " ".join(line.strip() for line in text.splitlines() if line.strip())
    return [prose] if prose else []


def _coerce(name: str, text: str) -> Any:
    text = _strip_rule(text)
    if not text:
        return None
    if name in LIST_FIELDS:
        return _bullets(text) or None
    return " ".join(line.strip() for line in text.splitlines() if line.strip()) or None


def _section_body(body: str, heading: str) -> str | None:
    match = re.search(_SECTION_RE.format(heading=re.escape(heading)), body,
                      re.MULTILINE | re.DOTALL)
    return match.group(1) if match else None


def _inline_body(body: str, label: str) -> str | None:
    """The paragraph introduced by `**Label.**`, up to the next such paragraph."""
    pattern = (r"^\*\*" + re.escape(label) + r"\.\*\*\s*(.*?)"
               r"(?=^\*\*[A-Z][^*]*\.\*\*|^#{2,3} |^\s*-{3,}\s*$|\Z)")
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL)
    if not match:
        return None
    # The compact form runs several claims together in one sentence-separated
    # paragraph; semicolons are its list separator.
    return match.group(1)


def _inline_list(text: str) -> list[str]:
    """Semicolons are the compact form's list separator.

    The trailing full stop belongs to the sentence, not to the last item, so it
    is removed -- but only from the end, because `CF-02/CF-03` and `Book III.`
    carry meaning mid-item.
    """
    text = _strip_rule(text)
    parts = [part.strip().rstrip(".").strip()
             for part in text.split(";") if part.strip().rstrip(".").strip()]
    return parts or ([text] if text else [])


def _split_cell(text: str) -> list[str]:
    """Split a table cell into items on top-level `;` and `,` only.

    The Office Registry enumerates with commas (`Tools, reports, scripts`) and
    separates contrastive clauses with semicolons (`Implementation only; no
    governance authority`). Both are list separators. A comma inside `[[Book I,
    Chapter 2]]` or inside a parenthetical is not, so the scan tracks depth and
    splits only outside brackets -- otherwise a dependency would be reported as
    two documents that do not exist.
    """
    items: list[str] = []
    buffer: list[str] = []
    brackets = parens = 0
    for char in _strip_rule(text):
        if char == "[":
            brackets += 1
        elif char == "]":
            brackets = max(0, brackets - 1)
        elif char == "(":
            parens += 1
        elif char == ")":
            parens = max(0, parens - 1)
        if char in ";," and brackets == 0 and parens == 0:
            items.append("".join(buffer))
            buffer = []
            continue
        buffer.append(char)
    items.append("".join(buffer))
    cleaned = [item.strip().rstrip(".").strip() for item in items]
    return [item for item in cleaned if item]


def _bold_values(body: str) -> dict[str, str]:
    """`**Current Engine:** Claude (Anthropic)` in either layout.

    The sectioned form puts each on its own line; the compact form joins them with
    middots on one line. One regex reads both, because the pair delimiter is the
    bold marker, not the newline.
    """
    return {m.group(1).strip(): m.group(2).strip() for m in _BOLD_KV_RE.finditer(body)}


# --------------------------------------------------------------------------
# type-constrained resolution
# --------------------------------------------------------------------------

def _entity_index(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["entity_id"]: item for item in registry["entities"]}


def resolve_typed(registry: dict[str, Any], reference: str, expect_type: str,
                  *, exclude: str | None = None) -> dict[str, Any]:
    """Resolve a reference that the source field declares to be of one type.

    `entity_registry.resolve` arbitrates alias collisions by source precedence,
    which is right when the caller has no type to go on. Here the caller does:
    a field headed `Intelligence Office` names an office. Without that constraint
    CF-08's office field resolves to CF-08 itself, because the cognitive function
    and the office share the label `Institutional Observatory` and the function
    won the collision. A self-loop is not a weak link, it is a false one.

    So resolution proceeds in two exact-match steps and then stops:

    1. `entity_registry.resolve`, accepted only if the result has `expect_type`
       and is not the entity doing the referring.
    2. The registry's own collision record. When an alias matched exactly but was
       arbitrated to another type, the rejected entity *is* the answer for a field
       of that type. Reading a recorded collision is not guessing -- the alias is
       identical, and the field's declared type breaks the tie.

    There is no third step. A reference no exact alias claims stays unresolved,
    with the reason, which is the only honest outcome available.
    """
    raw = str(reference or "").strip()
    if not raw or er.is_placeholder(raw):
        return {"value": raw or None, "entity_id": None, "method": None,
                "reason": "not_stated"}

    index = _entity_index(registry)
    candidate = er.resolve(registry, raw)
    if candidate and candidate != exclude:
        found = index.get(candidate)
        if found and found["entity_type"] == expect_type:
            return {"value": raw, "entity_id": candidate, "method": "alias",
                    "reason": None}

    # Step 2 -- the recorded collision. Compare on the same normalisation the
    # index used, and on the form without a trailing parenthetical, because
    # `Institutional Observatory (Metrics Division)` names the same office.
    bare = er._PARENTHETICAL_RE.sub("", raw).strip()
    wanted = {er.normalize(raw), er.normalize(bare)} - {""}
    for collision in registry.get("alias_collisions", []):
        if er.normalize(collision["alias"]) not in wanted:
            continue
        for entity_id in (collision["rejected"], collision["kept"]):
            found = index.get(entity_id)
            if (found and found["entity_type"] == expect_type
                    and entity_id != exclude):
                return {"value": raw, "entity_id": entity_id,
                        "method": "alias+type", "reason": None}

    if exclude is not None and candidate == exclude:
        return {"value": raw, "entity_id": None, "method": None,
                "reason": "self_reference"}
    if candidate:
        found = index.get(candidate)
        actual = found["entity_type"] if found else "unknown"
        return {"value": raw, "entity_id": None, "method": None,
                "reason": f"resolves_to_{actual}_not_{expect_type}"}
    return {"value": raw, "entity_id": None, "method": None,
            "reason": f"no_{expect_type}_of_that_name"}


# --------------------------------------------------------------------------
# cognitive functions
# --------------------------------------------------------------------------

def _cf_sections(text: str) -> list[tuple[str, str, str]]:
    """`(code, label, body)` per cognitive function, in registry order."""
    matches = list(_CF_HEADING_RE.finditer(text))
    out: list[tuple[str, str, str]] = []
    for position, match in enumerate(matches):
        end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
        out.append((match.group(1), match.group(2).strip(),
                    text[match.end():end]))
    return out


def _cf_relationships(body: str, code: str, source: str,
                      registry: dict[str, Any]) -> list[dict[str, Any]]:
    """The `Relationships with Other Functions` table as typed edges.

    The `type` column is kept verbatim. This module does not rank, group or
    reinterpret the fourteen relationship words the registry uses; it records them
    and lets `ESCALATION_TYPES` decide which two carry authority.
    """
    section = _section_body(body, "Relationships with Other Functions")
    if section is None:
        return []
    locator = f"{code} § Relationships with Other Functions"
    edges: list[dict[str, Any]] = []
    for cells in er.table_rows(section, 3):
        target = cells[0].strip()
        if not target or target.lower() == "function":
            continue
        relationship, nature = cells[1].strip(), cells[2].strip()
        if er.normalize(target) in COLLECTIVE_TARGETS:
            edges.append({"target": target, "target_entity_id": None,
                          "scope": "collective", "type": relationship,
                          "nature": nature, "source": source, "locator": locator,
                          "unresolved_reason": None})
            continue
        link = resolve_typed(registry, target, "agent",
                            exclude=f"agent:{code.lower()}")
        edges.append({"target": target, "target_entity_id": link["entity_id"],
                      "scope": "entity", "type": relationship, "nature": nature,
                      "source": source, "locator": locator,
                      "unresolved_reason": link["reason"]})
    return edges


def cognitive_function_semantics(text: str, source: str,
                                registry: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for code, label, body in _cf_sections(text):
        entity_id = f"agent:{code.lower()}"
        fields: dict[str, Any] = {}
        sectioned = bool(re.search(r"^### ", body, re.MULTILINE))
        source_format = "sectioned" if sectioned else "compact"

        if sectioned:
            for heading, name in CF_SECTION_FIELDS.items():
                raw = _section_body(body, heading)
                if raw is None:
                    continue
                value = _coerce(name, raw)
                if value is not None:
                    fields[name] = field(value, source, f"{code} § {heading}")
        else:
            for heading, name in CF_INLINE_FIELDS.items():
                raw = _inline_body(body, heading)
                if raw is None:
                    continue
                value = (_inline_list(raw) if name in LIST_FIELDS
                         else _coerce(name, raw))
                if value:
                    fields[name] = field(value, source, f"{code} § **{heading}.**")

        bold = _bold_values(body)
        for key, name in (("Current Engine", "engine"), ("Category", "category"),
                          ("Status", "status")):
            value = bold.get(key, "").strip()
            if value:
                fields[name] = field(value, source, f"{code} § **{key}:**")

        office_raw = bold.get("Intelligence Office", "")
        office = resolve_typed(registry, office_raw, "office", exclude=entity_id)
        office.update({"source": source, "locator": f"{code} § **Intelligence Office:**"})

        relationships = _cf_relationships(body, code, source, registry)
        out.append({
            "entity_id": entity_id,
            "role_class": "cognitive_function",
            "code": code,
            "label": label,
            "source_format": source_format,
            "fields": fields,
            "office": office,
            "relationships": relationships,
            "escalation": [
                {"entity_id": edge["target_entity_id"], "target": edge["target"],
                 "basis": edge["type"], "source": edge["source"],
                 "locator": edge["locator"]}
                for edge in relationships if edge["type"] in ESCALATION_TYPES
            ],
            "oversees": [
                {"entity_id": edge["target_entity_id"], "target": edge["target"],
                 "basis": edge["type"], "source": edge["source"],
                 "locator": edge["locator"]}
                for edge in relationships if edge["type"] in OVERSIGHT_TYPES
            ],
        })
    return out


# --------------------------------------------------------------------------
# offices
# --------------------------------------------------------------------------

def office_semantics(text: str, source: str,
                     registry: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    """Office semantics, plus the header row actually found.

    Columns are located by header name. The Office Registry's eleven columns are
    stable today, but a derived layer that indexes them by position turns a column
    insertion into seven silently wrong attributions.
    """
    rows = er.table_rows(text, len(OFFICE_COLUMN_FIELDS) + 4)
    header: list[str] | None = None
    for cells in rows:
        if cells and cells[0].strip().lower() == "office":
            header = [cell.strip() for cell in cells]
            break
    if header is None:
        raise SemanticsError(
            f"{source}: no 'Office' header row found -- the capability table has "
            f"been reshaped, and reading it by position would invent attributions.")

    position = {name: index for index, name in enumerate(header)}
    out: list[dict[str, Any]] = []
    for cells in rows:
        name = cells[0].strip()
        if not name or name.lower() == "office":
            continue
        primary = [part.strip() for part in er._ENGINE_SPLIT_RE.split(name) if part.strip()][0]
        entity_id = f"office:{er.slug(primary)}"
        fields: dict[str, Any] = {}
        for column, canonical in OFFICE_COLUMN_FIELDS.items():
            index = position.get(column)
            if index is None or index >= len(cells):
                continue
            cell = cells[index]
            if canonical in LIST_FIELDS:
                value = _split_cell(cell) or None
            else:
                value = _coerce(canonical, cell)
            if value is not None:
                fields[canonical] = field(
                    value, source,
                    f"§ Core Content · row '{primary}' · column '{column}'")

        cf_index = position.get(OFFICE_CF_COLUMN)
        declared = cells[cf_index].strip() if cf_index is not None and cf_index < len(cells) else ""
        responsible = resolve_typed(registry, declared, "agent", exclude=entity_id)
        responsible.update({
            "source": source,
            "locator": f"§ Core Content · row '{primary}' · column '{OFFICE_CF_COLUMN}'",
        })

        engine_index = position.get(OFFICE_ENGINE_COLUMN)
        if engine_index is not None and engine_index < len(cells):
            engine = cells[engine_index].strip()
            if engine:
                fields["engine"] = field(
                    engine, source,
                    f"§ Core Content · row '{primary}' · column '{OFFICE_ENGINE_COLUMN}'")

        out.append({
            "entity_id": entity_id,
            "role_class": "office",
            "code": None,
            "label": primary,
            "source_format": "table",
            "fields": fields,
            "responsible_cognitive_function": responsible,
            "relationships": [],
            # The Office Registry has no accountability column. Deriving escalation
            # from the prose in `Authority` ("subject to Founder approval") would be
            # inference from natural language, which this layer does not do.
            "escalation": [],
            "oversees": [],
        })
    return out, header


# --------------------------------------------------------------------------
# agent roles
# --------------------------------------------------------------------------

def agent_semantics(roles: list[dict[str, Any]], source: str,
                    registry: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for role in roles:
        agent_id = role["id"]
        entity_id = f"agent:{agent_id.lower()}"
        locator = f"§ Agent Roles · row '{agent_id}'"
        fields: dict[str, Any] = {}
        for column, name in (("operating_owner", "operating_owner"),
                             ("current_implementation", "implementation"),
                             ("state", "status")):
            value = str(role.get(column, "")).strip()
            if value:
                fields[name] = field(value, source, f"{locator} · column '{column}'")
        if role.get("may_instantiate"):
            fields["may_instantiate"] = field(
                list(role["may_instantiate"]), source,
                f"{locator} · column 'may_instantiate'")

        parent = resolve_typed(registry, role.get("parent_function", ""), "agent",
                              exclude=entity_id)
        parent.update({"source": source,
                       "locator": f"{locator} · column 'parent_function'"})
        out.append({
            "entity_id": entity_id,
            "role_class": "agent_role",
            "code": agent_id,
            "label": role.get("named_role", agent_id),
            "source_format": "table",
            "fields": fields,
            "parent_function": parent,
            "relationships": [],
            # An agent role's authority is the parent function's, in the registry's
            # own word for the column. Nothing else is claimed: Invocation Rule 6
            # routes every result to the Founder, but that is a rule about the
            # process, carried at layer level, not sixteen edges to `person:founder`.
            "escalation": ([{"entity_id": parent["entity_id"],
                             "target": parent["value"], "basis": "Parent Function",
                             "source": source, "locator": parent["locator"]}]
                           if parent["entity_id"] else []),
            "oversees": [],
        })
    return out


# --------------------------------------------------------------------------
# entities with no semantics table
# --------------------------------------------------------------------------

def declared_only_semantics(registry: dict[str, Any]) -> list[dict[str, Any]]:
    """Organizations and the Founder.

    The Constitution defines these in prose, not a table. Parsing narrative into
    `authority` and `inputs` would mean this module writing their mandate, so it
    does not: they appear with identity and provenance, no derived fields, and an
    `info` finding recording that the source is prose. The Foundation can add a
    constitutional table later and these entries fill in with no consumer change.
    """
    out: list[dict[str, Any]] = []
    for item in registry["entities"]:
        if item["entity_type"] not in ("organization", "person"):
            continue
        out.append({
            "entity_id": item["entity_id"],
            "role_class": item["entity_type"],
            "code": None,
            "label": item["label"],
            "source_format": "prose",
            "fields": {},
            "relationships": [],
            "escalation": [],
            "oversees": [],
        })
    return out


# --------------------------------------------------------------------------
# coverage and findings
# --------------------------------------------------------------------------

def coverage(record: dict[str, Any]) -> dict[str, Any]:
    expected = EXPECTED_FIELDS.get(record["role_class"], ())
    present = [name for name in expected if name in record["fields"]]
    absent = [name for name in expected if name not in record["fields"]]
    return {
        "expected": len(expected),
        "present": present,
        "absent": absent,
        "ratio": round(len(present) / len(expected), 3) if expected else None,
    }


def _finding(code: str, severity: str, message: str, *,
             entity_id: str | None = None, evidence: Any = None) -> dict[str, Any]:
    return {"code": code, "severity": severity, "entity_id": entity_id,
            "message": message, "evidence": evidence}


def _is_unappointed(record: dict[str, Any]) -> bool:
    """True when the registry itself says nobody holds this yet.

    CF-11 and CF-15 carry `Current Engine: [To be appointed]`. A function with no
    engine cannot be expected to have a filled-in mandate, and reporting it as a
    gap every run would teach the reader to skip the report.
    """
    engine = record["fields"].get("engine", {}).get("value", "")
    status = record["fields"].get("status", {}).get("value", "")
    return er.is_placeholder(str(engine).strip("*").strip()) or \
        str(status).strip().lower() in ("standby", "registered (epoch v)")


def findings(records: list[dict[str, Any]], registry: dict[str, Any],
             office_header: list[str]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    index = _entity_index(registry)
    by_id = {record["entity_id"]: record for record in records}

    # --- error: the layer would be unsound ---
    for record in records:
        if record["entity_id"] not in index:
            out.append(_finding(
                "semantics_without_identity", "error",
                f"{record['entity_id']} has derived semantics but no entity in the "
                f"identity registry; nothing ratifies it.",
                entity_id=record["entity_id"]))
    seen: set[str] = set()
    for record in records:
        if record["entity_id"] in seen:
            out.append(_finding("duplicate_semantics", "error",
                                f"{record['entity_id']} derived twice.",
                                entity_id=record["entity_id"]))
        seen.add(record["entity_id"])
    for record in records:
        parent = record.get("parent_function")
        if parent and parent["entity_id"] is None:
            out.append(_finding(
                "agent_parent_unresolved", "error",
                f"{record['code']} names parent function {parent['value']!r}, which "
                f"no cognitive function claims ({parent['reason']}); the role has no "
                f"mandate to inherit.",
                entity_id=record["entity_id"], evidence=parent["locator"]))

    # --- warning: real, not invalidating ---
    for record in records:
        if record["role_class"] != "cognitive_function":
            continue
        absent = record["coverage"]["absent"]
        if not absent:
            continue
        # Why a field is missing decides who fixes it. A compact entry has no slot
        # for `authority` at all, so its gap is editorial and waits on nobody; a
        # standby function's gap waits on an appointment. Filing both as one
        # finding would send the second reader to the wrong remedy.
        if record["source_format"] == "compact":
            out.append(_finding(
                "compact_entry_incomplete", "warning",
                f"{record['code']} {record['label']} is written in the compact form, "
                f"which has no slot for {', '.join(absent)}. Rewriting the entry in "
                f"the sectioned form would state them; no appointment is required.",
                entity_id=record["entity_id"], evidence={"absent": absent}))
        elif _is_unappointed(record):
            out.append(_finding(
                "cognitive_function_incomplete", "info",
                f"{record['code']} {record['label']} states no "
                f"{', '.join(absent)}. Expected: no engine is appointed "
                f"({record['fields'].get('status', {}).get('value', 'status unstated')}).",
                entity_id=record["entity_id"], evidence={"absent": absent}))
        else:
            out.append(_finding(
                "cognitive_function_incomplete", "warning",
                f"{record['code']} {record['label']} is active with an appointed "
                f"engine but states no {', '.join(absent)}.",
                entity_id=record["entity_id"], evidence={"absent": absent}))

    for record in records:
        office = record.get("office")
        if not office or office["entity_id"] or office["reason"] == "not_stated":
            continue
        if office["reason"] == "self_reference":
            out.append(_finding(
                "office_is_self_alias", "warning",
                f"{record['code']} names Intelligence Office {office['value']!r}, "
                f"which is one of {record['code']}'s own aliases -- a function "
                f"cannot be its own office. The Office Registry lists no office of "
                f"that name, so the function's home is unconfirmed either way.",
                entity_id=record["entity_id"], evidence=office["locator"]))
        else:
            out.append(_finding(
                "office_not_registered", "warning",
                f"{record['code']} names Intelligence Office {office['value']!r}, "
                f"which the Office Registry does not list ({office['reason']}). The "
                f"function has a home the registry of offices cannot confirm.",
                entity_id=record["entity_id"], evidence=office["locator"]))
    for record in records:
        office = record.get("office")
        if office and office["method"] == "alias+type":
            out.append(_finding(
                "office_alias_contested", "warning",
                f"{record['code']} resolves its office {office['value']!r} only "
                f"because the field declares a type: a cognitive function holds the "
                f"same alias. Give one of them a distinct name and the ambiguity ends.",
                entity_id=record["entity_id"], evidence=office["locator"]))

    mismatched = [record for record in records
                  if record["role_class"] == "office"
                  and record["responsible_cognitive_function"]["entity_id"] is None
                  and record["responsible_cognitive_function"]["reason"] != "not_stated"]
    if mismatched:
        out.append(_finding(
            "office_cf_vocabulary_mismatch", "warning",
            f"{len(mismatched)} of "
            f"{sum(1 for r in records if r['role_class'] == 'office')} office rows "
            f"name a Responsible Cognitive Function that matches no cognitive "
            f"function label. The Office Registry uses role verbs "
            f"({', '.join(sorted({r['responsible_cognitive_function']['value'] for r in mismatched}))}); "
            f"the Cognitive Function Registry uses named functions. Until one "
            f"vocabulary is chosen the office-to-function binding is derived only "
            f"from the Cognitive Function Registry's Intelligence Office field. "
            f"Resolving this by resemblance would attribute institutional "
            f"responsibility on the strength of a similar word.",
            evidence={"rows": [{"office": r["label"],
                                "declared": r["responsible_cognitive_function"]["value"],
                                "reason": r["responsible_cognitive_function"]["reason"]}
                               for r in mismatched],
                      "header": office_header}))

    for record in records:
        if record["role_class"] != "agent_role":
            continue
        status = record["fields"].get("status", {}).get("value", "")
        parent = record.get("parent_function") or {}
        parent_record = by_id.get(parent.get("entity_id") or "")
        if status == "available" and parent_record and \
                "responsibilities" not in parent_record["fields"]:
            out.append(_finding(
                "agent_available_without_mandate", "warning",
                f"{record['code']} {record['label']} is available for dispatch, but "
                f"its parent {parent_record['code']} states no primary "
                f"responsibilities. The role can be assigned work that no document "
                f"defines.",
                entity_id=record["entity_id"],
                evidence={"parent": parent_record["entity_id"]}))

    for record in records:
        for edge in record["relationships"]:
            if edge["scope"] != "entity" or edge["target_entity_id"]:
                continue
            out.append(_finding(
                "relationship_target_unresolved", "warning",
                f"{record['code']} declares a {edge['type']!r} relationship with "
                f"{edge['target']!r}, which no entity claims "
                f"({edge['unresolved_reason']}). The relationship is recorded and "
                f"stays unresolved; naming the nearest similar function would "
                f"invent the edge.",
                entity_id=record["entity_id"], evidence=edge["locator"]))

    formats = {record["source_format"] for record in records
               if record["role_class"] == "cognitive_function"}
    if len(formats) > 1:
        compact = [record["code"] for record in records
                   if record["role_class"] == "cognitive_function"
                   and record["source_format"] == "compact"]
        out.append(_finding(
            "registry_format_divergence", "warning",
            f"The Cognitive Function Registry is written in "
            f"{len(formats)} formats: sectioned headings, and inline bold labels "
            f"for {', '.join(compact)}. Both are read here, but any derived layer "
            f"that reads only headings will report those functions as empty when "
            f"they are not.",
            evidence={"formats": sorted(formats), "compact": compact}))

    escalating = [record for record in records
                  if record["role_class"] == "cognitive_function" and record["escalation"]]
    functions = [record for record in records if record["role_class"] == "cognitive_function"]
    if functions and len(escalating) < len(functions):
        out.append(_finding(
            "escalation_thinly_authored", "warning",
            f"{len(escalating)} of {len(functions)} cognitive functions state an "
            f"accountability relationship. The registry documents collaboration in "
            f"detail and answerability barely, so this layer can derive very little "
            f"escalation. That is a gap in the documents, not in the parser.",
            evidence={"with_escalation": [r["code"] for r in escalating]}))

    # --- info: expected states ---
    for record in records:
        status = str(record["fields"].get("status", {}).get("value", "")).lower()
        if record["role_class"] != "agent_role" or status not in ("blocked", "advisory-only"):
            continue
        # Say why only where the registries say why. AGT-011 is blocked and its
        # parent CF-11 is on standby with no engine, so the two facts explain each
        # other. AGT-010 is advisory-only while CF-10 is active and appointed --
        # that state is a constitutional choice about voting, and attributing it to
        # an appointment would be this module inventing a reason.
        parent = by_id.get((record.get("parent_function") or {}).get("entity_id") or "")
        because = ""
        if parent and _is_unappointed(parent):
            because = (f", consistent with {parent['code']}, which has no engine "
                       f"appointed")
        out.append(_finding(
            "agent_state_limited", "info",
            f"{record['code']} {record['label']} is {status}{because}.",
            entity_id=record["entity_id"]))
    for record in records:
        if record["role_class"] in ("organization", "person"):
            out.append(_finding(
                "semantics_source_is_prose", "info",
                f"{record['label']} is defined in the Constitution as prose, so no "
                f"fields are derived. Identity and provenance only.",
                entity_id=record["entity_id"]))
    collective = [edge for record in records for edge in record["relationships"]
                  if edge["scope"] == "collective"]
    if collective:
        out.append(_finding(
            "collective_relationship_targets", "info",
            f"{len(collective)} relationship edge(s) address all functions at once. "
            f"Each stays one edge; expanding them into per-function links would "
            f"create relationships no registry wrote.",
            evidence=[{"locator": edge["locator"], "type": edge["type"]}
                      for edge in collective]))
    return out


# --------------------------------------------------------------------------
# contract
# --------------------------------------------------------------------------

def build(root: Path = VAULT_ROOT, *, strict: bool = True) -> dict[str, Any]:
    """The role semantics contract: every entity, what it is for, and from where."""
    root = Path(root).expanduser().resolve()
    if not root.is_dir():
        raise SemanticsError(f"Vault root is not a directory: {root}")

    registry = er.build(root, strict=strict)

    cf_text = er.read(root, er.CF_REGISTRY, strict)
    office_text = er.read(root, er.OFFICE_REGISTRY, strict)
    if cf_text is None or office_text is None:
        missing = [source.as_posix() for source, text
                   in ((er.CF_REGISTRY, cf_text), (er.OFFICE_REGISTRY, office_text))
                   if text is None]
        raise SemanticsError(
            f"Cannot derive role semantics without {', '.join(missing)}.")

    records: list[dict[str, Any]] = []
    records += cognitive_function_semantics(cf_text, er.CF_REGISTRY.as_posix(), registry)
    offices, office_header = office_semantics(office_text,
                                              er.OFFICE_REGISTRY.as_posix(), registry)
    records += offices
    try:
        roles = rr.load_roles(root)
    except rr.RegistryError as exc:
        raise SemanticsError(f"Agent registry unreadable: {exc}") from exc
    records += agent_semantics(roles["roles"], er.AGENT_REGISTRY.as_posix(), registry)
    records += declared_only_semantics(registry)

    for record in records:
        record["coverage"] = coverage(record)

    reported = findings(records, registry, office_header)
    by_severity = {level: sum(1 for item in reported if item["severity"] == level)
                   for level in ("error", "warning", "info")}
    by_class: dict[str, int] = {}
    for record in records:
        by_class[record["role_class"]] = by_class.get(record["role_class"], 0) + 1

    linked = sum(1 for record in records
                 if record["role_class"] == "cognitive_function"
                 and record["office"]["entity_id"])
    edges = [edge for record in records for edge in record["relationships"]]
    # A collective edge is authored and resolved as far as it can be; counting it
    # against a "resolved" ratio would report the registry as broken for writing
    # `All functions`, which is a legitimate thing to write.
    collective_edges = [edge for edge in edges if edge["scope"] == "collective"]
    failed_edges = [edge for edge in edges
                    if edge["scope"] == "entity" and not edge["target_entity_id"]]
    escalation_by_basis: dict[str, int] = {}
    for record in records:
        for link in record["escalation"]:
            escalation_by_basis[link["basis"]] = \
                escalation_by_basis.get(link["basis"], 0) + 1

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": now_iso(),
        "derived_from": [er.CF_REGISTRY.as_posix(), er.OFFICE_REGISTRY.as_posix(),
                         er.AGENT_REGISTRY.as_posix()],
        "identity_schema_version": registry["schema_version"],
        "invocation_rules": roles["invocation_rules"],
        "entities": records,
        "findings": reported,
        "counts": {
            "entities": len(records),
            "by_role_class": by_class,
            "identity_entities": registry["counts"]["entities"],
            "relationship_edges": len(edges),
            "relationship_edges_resolved": sum(
                1 for edge in edges if edge["target_entity_id"]),
            "relationship_edges_collective": len(collective_edges),
            "relationship_edges_unresolved": len(failed_edges),
            "functions_bound_to_office": linked,
            "escalation_edges": sum(len(record["escalation"]) for record in records),
            "escalation_edges_by_basis": escalation_by_basis,
            "findings_by_severity": by_severity,
        },
    }


def entity(contract: dict[str, Any], reference: str) -> dict[str, Any] | None:
    """One entity's semantics, by entity id, code or label."""
    wanted = er.normalize(reference)
    for record in contract["entities"]:
        for key in (record["entity_id"], record["code"] or "", record["label"]):
            if key and er.normalize(key) == wanted:
                return record
    return None


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _print_check(contract: dict[str, Any]) -> None:
    counts = contract["counts"]
    print(f"Role semantics v{contract['schema_version']} — "
          f"{counts['entities']} entities derived from "
          f"{len(contract['derived_from'])} registries")
    for role_class in ROLE_CLASSES:
        total = counts["by_role_class"].get(role_class, 0)
        if total:
            print(f"  {role_class:<20} {total}")
    print(f"\nFunctions bound to an office: {counts['functions_bound_to_office']}/"
          f"{counts['by_role_class'].get('cognitive_function', 0)}")
    print(f"Relationship edges:           {counts['relationship_edges']} "
          f"({counts['relationship_edges_resolved']} resolved, "
          f"{counts['relationship_edges_collective']} collective, "
          f"{counts['relationship_edges_unresolved']} unresolved)")
    basis = ", ".join(f"{count} by {name}"
                      for name, count in sorted(counts["escalation_edges_by_basis"].items()))
    print(f"Escalation edges derived:     {counts['escalation_edges']}"
          f"{f' ({basis})' if basis else ''}")

    print("\nCoverage by entity:")
    for record in contract["entities"]:
        ratio = record["coverage"]["ratio"]
        if ratio is None:
            continue
        absent = ", ".join(record["coverage"]["absent"]) or "—"
        label = f"{record['code'] or record['entity_id']} {record['label']}"
        print(f"  {label:<44} {ratio:>5.0%}  missing: {absent}")

    severities = contract["counts"]["findings_by_severity"]
    print(f"\nFindings: {severities['error']} error, {severities['warning']} warning, "
          f"{severities['info']} info")
    for level in ("error", "warning", "info"):
        for item in contract["findings"]:
            if item["severity"] != level:
                continue
            where = f" [{item['entity_id']}]" if item["entity_id"] else ""
            print(f"  {level:<7} {item['code']}{where}: {item['message']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ap.py semantics", description=__doc__)
    parser.add_argument("--root", default=str(VAULT_ROOT))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("view", help="Print the role semantics contract as JSON.")
    sub.add_parser("check", help="Report coverage and findings.")
    show = sub.add_parser("show", help="Print one entity's semantics.")
    show.add_argument("reference", help="Entity id, code (CF-07, AGT-007) or label.")

    args = parser.parse_args(argv)
    try:
        contract = build(Path(args.root))
    except (SemanticsError, er.EntityError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.command == "view":
        print(json.dumps(contract, indent=2, ensure_ascii=False))
        return 0

    if args.command == "show":
        record = entity(contract, args.reference)
        if record is None:
            print(f"error: no entity matches {args.reference!r}", file=sys.stderr)
            return 1
        print(json.dumps(record, indent=2, ensure_ascii=False))
        return 0

    _print_check(contract)
    return 1 if contract["counts"]["findings_by_severity"]["error"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
