---
title: "Role Semantics Architecture v1"
aliases: ["Role Semantics", "role_semantics", "ap semantics", "Derived Role Semantics"]
tags: [systems, architecture, semantics, roles, council, offices, agents, derived, alpha-proxima]
created: 2026-09-30
updated: 2026-09-30
status: draft
version: "1.0.0"
authors: ["Founder", "Chief Knowledge Architect (CF-01)"]
artifact_type: architecture-note
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Institutional Architecture"
reasoning_engine: "Claude"
dependencies: ["Python 3 standard library", "[[Cognitive Function Registry]]", "[[Office Registry]]", "[[Agent and Subagent Registry]]", "[[Tool 008 - Engineering CLI]]"]
related_documents: ["[[Book I - The Constitution]]", "[[Governance Model Crosswalk]]", "[[Tool 014 - Truth Kernel]]", "[[Council Node Architecture]]"]
related_research_programs: []
---

# Role Semantics Architecture v1

## Purpose

Give the Foundation a machine-readable answer to the question *what is each of our
forty-two entities for* — responsibilities, authority, reporting — derived entirely
from registries already ratified, with per-field provenance, and with every gap
reported rather than filled.

## Mission

Make institutional role knowledge queryable without making it inventable. A
Foundation designed to outlive its creators cannot rely on the knowledge of who is
responsible for what living in the memory of whoever is currently reading the
vault. Neither can it afford a layer that manufactures that knowledge where the
documents are silent, because the manufactured answer would be read back as canon
by every reader who came after.

## Definitions

| Term | Meaning |
|------|---------|
| **Identity layer** | `entity_registry.py`. Answers *who exists*: forty-two typed actors, each with the document conferring its identity. |
| **Semantics layer** | `role_semantics.py`, this document's subject. Answers *what each one is for*. |
| **Derived** | Lifted from a ratified registry without alteration. The opposite of *authored*. |
| **Per-field provenance** | Each value carries `source` (the document) and `locator` (the heading, row and column inside it). |
| **Type-constrained resolution** | A link resolves by exact alias, accepted only if the result has the type the source field declares. |
| **Role class** | `cognitive_function`, `agent_role`, `office`, `organization`, `person`. Finer than the identity layer's `entity_type`, which types CF-07 and AGT-007 alike. |
| **Coverage** | Fields present over fields the role class can have. An office is never marked as missing a succession rule. |

## Context

The identity layer landed first and deliberately answered one question. It gave
CODEX, LUMIAION and the Foundation itself canonical identity and refused to say
anything further, because identity and semantics are different claims and a
registry that conflates them begins inventing things.

That left a real gap. Asking which function owns a decision, whether an agent role
has a documented mandate, or who a function answers to meant a human reading three
registries in three directories and holding the cross-references in their head.
Institutional memory that only exists while someone is holding it is the condition
this Foundation was built to end.

Three ratified registries already contain the answers:

- **[[Cognitive Function Registry]]** — CF-01…CF-16, canonical since Epoch V.
- **[[Office Registry]]** — the seven offices and their capability table.
- **[[Agent and Subagent Registry]]** — AGT-001…AGT-016 and the invocation rules.

Nothing was missing except a reader.

## Architecture

### The discipline

Three rules, and the layer is worth less than nothing without them.

1. **Derived, never authored.** No responsibility, authority or reporting line
   appears here that a document does not already state. Where a registry is
   silent, the field is absent and the absence is reported as a finding.
2. **Provenance per field, not per entity.** One `canonical_source` per actor is
   too coarse: an office's authority comes from one table cell and its dependencies
   from another. A reader checking a single claim should not have to re-derive
   which cell it came from.
3. **Never match identity by resemblance.** Links resolve by exact alias under a
   declared type, or they stay unresolved with the reason named. Deciding that
   `Implementation` means `Engineering Intelligence` because the words feel related
   would attribute institutional responsibility on the strength of a similar word.

### Two authored formats

The Cognitive Function Registry is written two ways. CF-01 through CF-14 use
`### Purpose` sections. CF-15 and CF-16 use inline `**Purpose.**` paragraphs with
their metadata on one middot-separated line — the form in which the Epoch V
reconciliation registered JERANIUM and YUNA, per the [[Governance Model Crosswalk]].

A parser that reads only headings reports CF-15 and CF-16 as empty. **They are not
empty.** CF-15 states a purpose, a mission, five primary responsibilities, three
boundaries and a succession rule. This layer reads both forms and normalises them
onto one field vocabulary, so no consumer needs to know which form an entry uses.

The divergence is itself reported (`registry_format_divergence`). A canonical
registry with two shapes will keep breaking derived layers until it has one.

### The direction that binds

The two directions of the office↔function relationship are not equally usable.

- **Function → office works.** The Cognitive Function Registry's
  `**Intelligence Office:**` field resolves for **10 of 16** functions.
- **Office → function does not.** The Office Registry's
  `Responsible Cognitive Function` column reads `Orchestration`, `Architecture`,
  `Implementation`, `Research`, `Observation`, `Executive`, `Evolution` — role
  verbs, which match **zero of sixteen** cognitive function labels. Seven rows,
  seven misses.

So the binding is derived from the Cognitive Function Registry alone, and the
Office Registry's column is reported as awaiting reconciliation. This is a
vocabulary decision for the Founder, not an arithmetic problem for a parser.

### Type-constrained resolution

The identity layer arbitrates alias collisions by source precedence, which is
right when the caller has no type to go on. Here the caller does: a field headed
`Intelligence Office` names an office.

Without that constraint, CF-08's office field resolves to **CF-08 itself**,
because the cognitive function and the office share the label
`Institutional Observatory` and the function won the collision. A self-loop is not
a weak edge; it is a false one, and the kind of fabricated graph edge the ratified
directive forbids outright.

Resolution therefore takes two exact-match steps and then stops:

1. The identity layer's resolver, accepted only if the result carries the expected
   type and is not the entity doing the referring. Method: `alias`.
2. The identity layer's own recorded collision. Where an alias matched exactly but
   was arbitrated to another type, the rejected entity *is* the answer for a field
   of that type. Method: `alias+type`. This is not guessing — the alias is
   identical and the field's declared type breaks the tie.

There is no third step.

### Escalation is authored only

The Cognitive Function Registry uses fourteen relationship words across
thirty-five edges. Only `Accountable to` carries answerability. `Upstream
supplier` and `Collaborator` describe how work flows, not who answers to whom, and
promoting them would manufacture a reporting structure the Foundation has never
written down.

The consequence is uncomfortable and is reported as such: **2 of 16** cognitive
functions state an accountability relationship. The registry documents
collaboration in detail and answerability barely. That is a gap in the documents,
not in the parser.

For offices the layer derives no escalation at all. The Office Registry has no
accountability column, and its `Authority` cells say things like *"subject to
Founder and AI Council approval"* — prose. Inferring an edge from prose is
inference, which this layer does not do.

For agent roles the escalation basis is the registry's own column name,
`Parent Function`. Invocation Rule 6 routes every result to the Founder, but that
is a rule about process, carried at layer level, not sixteen fabricated edges to
`person:founder`.

### Severity

The vocabulary the Truth Kernel and the Live Integration Layer already use, so one
reader can weigh all three together.

| Severity | Means | Example |
|----------|-------|---------|
| `error` | The layer is unsound. | An agent role whose parent function no cognitive function claims. |
| `warning` | Real, and not invalidating. | An active function with an appointed engine that states no responsibilities. |
| `info` | The expected state of something incomplete on purpose. | CF-11 is on standby with no engine appointed. |

Checks that pass still report. A check that only appears when it fails leaves the
reader unable to tell a clean result from an absent one — the same principle that
governs `available` / `unavailable` / `error` in the Live Integration Layer.

## Dependencies

- Python 3 standard library only. No third-party package, consistent with the
  zero-dependency gate on the Engineering Toolkit.
- `entity_registry.py` for identity, alias resolution and collision records.
- `role_registry.py` for the agent table and invocation rules. One parser per
  document: a second would drift from the first.
- [[Tool 008 - Engineering CLI]] for dispatch (`ap semantics`).

## Examples

```bash
# Coverage and findings for the whole Foundation
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" semantics check

# The full contract as JSON
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" semantics view

# One entity, by id, code or label
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" semantics show CF-07
python3 "08_SYSTEMS/Engineering Toolkit/ap.py" semantics show AGT-012
```

### Measured state, 2026-09-30

| Measure | Value |
|---------|-------|
| Entities with derived semantics | 42 of 42 |
| By role class | 16 cognitive functions, 16 agent roles, 7 offices, 2 organizations, 1 person |
| Functions bound to an office | 10 of 16 |
| Office rows bound to a function | 0 of 7 |
| Relationship edges | 35 — 32 resolved, 3 collective, 0 unresolved |
| Escalation edges | 18 — 2 by `Accountable to`, 16 by `Parent Function` |
| Findings | 0 error, 16 warning, 9 info |
| Agent roles with a resolved parent function | 16 of 16 |

### What the warnings say

| Finding | Count | What it means |
|---------|-------|---------------|
| `cognitive_function_incomplete` | 3 | CF-12, CF-13, CF-14 are active with appointed engines but state no primary responsibilities. |
| `compact_entry_incomplete` | 2 | CF-15 and CF-16 are written in the compact form, which has no slot for authority, inputs, outputs or review cycle. Editorial; no appointment required. |
| `office_is_self_alias` | 4 | CF-10, CF-12, CF-13, CF-14 name an Intelligence Office that is one of their own aliases (`Ethics Council`, `ATHENA`, `VORTEX`, `SOHMA`). A function cannot be its own office, and the Office Registry lists none of these four. |
| `office_alias_contested` | 1 | CF-08 resolves its office only because the field declares a type; a cognitive function holds the same label. |
| `office_cf_vocabulary_mismatch` | 1 | All 7 office rows name a responsible function in a vocabulary no function uses. |
| `agent_available_without_mandate` | 3 | AGT-012, AGT-013, AGT-014 are available for dispatch while their parent functions state no responsibilities. They can be assigned work no document defines. |
| `registry_format_divergence` | 1 | Two formats in one canonical registry. |
| `escalation_thinly_authored` | 1 | 2 of 16 functions state accountability. |

## Future Improvements

1. **Reconcile the office↔function vocabulary.** One decision closes
   `office_cf_vocabulary_mismatch` and makes the relationship bidirectional. Either
   the Office Registry cites CF codes, or the Cognitive Function Registry adopts the
   role verbs. Citing CF codes is the smaller change and the more durable one, since
   codes survive renaming.
2. **Register the four missing offices, or stop citing them.** `Ethics Council`
   exists as a directory under `09_OFFICES` and is absent from the Office Registry;
   `ATHENA`, `VORTEX` and `SOHMA` are cited at paths that do not exist at all.
3. **Rewrite CF-15 and CF-16 in the sectioned form**, or adopt the compact form
   registry-wide. Either ends the divergence; a registry in two shapes does not.
4. **Give CF-12, CF-13 and CF-14 primary responsibilities**, which also clears the
   three `agent_available_without_mandate` warnings.
5. **Author accountability deliberately.** Thirty-three of thirty-five relationship
   edges describe collaboration. Deciding who answers to whom is a governance act
   and cannot be derived.
6. **Surface this layer in the App's know half** once the warnings are down, so the
   Founder Console can show a role's mandate with its provenance.

## Open Questions

- [ ] Should the four alias collisions be resolved by renaming (giving the office
      and the function distinct labels) or by a qualified-alias convention
      (`LUMIAION (CF-09)` versus bare `LUMIAION`)? The identity layer already uses
      the second for engines; extending it to offices would be consistent.
- [ ] Does an agent role inherit its parent function's authority, or only its
      subject matter? The Agent Registry says `Parent Function` and stops there.
      This layer records the column and claims nothing more.
- [ ] Should organizations and the Founder get a constitutional table, so their
      semantics are derived rather than absent? Today they carry identity and
      provenance only, because parsing narrative into `authority` would mean this
      layer writing the Founder's mandate.
- [ ] Should `ap semantics check` exit non-zero on warnings once they reach zero,
      making the office↔function binding a gate rather than a report?

## Related Documents

- [[Cognitive Function Registry]] — primary source for CF-01…CF-16.
- [[Office Registry]] — primary source for the seven offices.
- [[Agent and Subagent Registry]] — primary source for AGT-001…AGT-016.
- [[Governance Model Crosswalk]] — why CF-15 and CF-16 exist and why they read differently.
- [[Tool 014 - Truth Kernel]] — the severity vocabulary this layer shares.
- [[Council Node Architecture]] — the Council structure these roles populate.
- [[Book I - The Constitution]] — confers identity on the Foundation and the Founder.
- [[Tool 008 - Engineering CLI]] — `ap semantics` dispatch.

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-09-30 | First derived role semantics layer. Forty-two entities, per-field provenance, type-constrained resolution, two registry formats read. 0 errors, 16 warnings, 9 info findings recorded rather than resolved. |
