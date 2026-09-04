---
title: "Truth Kernel Node Contract v0.1"
aliases: ["Truth Kernel Contract", "Node Contract v0.1"]
tags: [systems, engineering, truth-kernel, knowledge-graph, schema, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: draft
version: "0.1.0"
authors: ["CODEX"]
artifact_type: engineering-architecture
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Knowledge Graph Architecture v1.0]]", "[[Node Taxonomy]]", "[[Relationship Taxonomy]]"]
related_documents: ["[[Tool 010 - Node Registry Generator]]", "[[Tool 011 - Relationship Extractor]]", "[[Alpha Proxima App Architecture v1]]"]
related_research_programs: []
standard_id: "TK-NC-001"
---

# Truth Kernel Node Contract v0.1

## Purpose

Freeze the first executable, read-only contract between the canonical Obsidian Vault, the Institutional Knowledge Graph tooling, and Founder interfaces.

## Canonicality

- Obsidian Markdown remains canonical.
- Registries, validation reports, fingerprints, and API responses are derived and replaceable.
- Extraction never writes identity back into source notes.
- Unknown values remain empty or become validation findings; they are never invented.
- Inferred relationships remain `inferred` or `unresolved`, never canonical.

## Node schema

Every node record exposes:

| Field | Rule |
|---|---|
| `node_id` | Unique machine identifier using `apkg:<node_type>:<stable_slug>` |
| `node_type` | Candidate type from [[Node Taxonomy]] |
| `title` | YAML title, first H1, or filename fallback |
| `source_path` | Vault-relative Markdown path |
| `status` | Source value or null |
| `version` | Source value or null |
| `canonical_owner` | Source owner or null |
| `created`, `updated` | Source values or null |
| `identity_source` | Exact YAML field or `title_fallback` |
| `identity_stability` | `stable`, `provisional`, or `collision_bound` |
| `provenance` | Extraction method and source SHA-256 |
| `validation_findings` | Explicit identity or parsing defects |

## Identity precedence

1. Valid explicit YAML `node_id`.
2. Taxonomy identity such as `standard_id`, `tool_id`, `decision_id`, `project_id`, or `research_program_id`.
3. Title-based provisional identity.
4. If candidates collide, retain both nodes, append a deterministic path digest, and emit `identity_collision`.

Title fallback survives a file move but remains provisional because a title change can change the ID. A path is never silently presented as permanent institutional identity.

## Relationship schema

Every resolved relationship exposes its stable ID, type, source and target node IDs, source path, status, confidence, provenance, extraction source, and source detail. Missing or ambiguous targets remain in `unresolved_relationships`; ambiguity includes every candidate node ID and is never resolved by filesystem order.

## Read contract

`truth-kernel.json` provides:

- `schema_version`
- `mode: read_only`
- canonical-source declaration
- source and contract fingerprints
- health and reproducible counts
- nodes
- resolved relationships
- unresolved relationships
- validation findings

Machine-readable output contains no generation timestamp or absolute Vault path, allowing unchanged input to produce byte-identical output. The human validation report may include its generation time.

## Examples

| Source | Identity input | Result |
|---|---|---|
| Project | `project_id: FOUNDER-OS` | `apkg:founder_directive:founder-os` or mapped project type when added to the taxonomy |
| Decision | `decision_id: FD-002` | `apkg:founder_directive:fd-002` |
| Office | `office_id: LUMIAION` | `apkg:office:lumiaion` |
| Research program | `research_program_id: RP-001` | `apkg:research_program:rp-001` |
| Unclassified note | title only | provisional `apkg:unknown:<title-slug>` |

The node type and the identity field are independent signals. A validation finding is preferable to inventing a type that the current taxonomy does not define.

## Collision behavior

- Duplicate identity candidates are never overwritten.
- Every colliding record receives a deterministic suffix and `collision_bound` status.
- The unsuffixed request is preserved as `requested_node_id`.
- The validation report requires human resolution before downstream canonical use.

## Verification requirements

- Two unchanged runs produce byte-identical JSON registries.
- Moving a uniquely titled fallback note does not change its node ID.
- Missing YAML, malformed YAML, duplicate identities, unreadable inputs, and ambiguous links are tested.
- Source Markdown hashes are identical before and after generation.
- One Founder interface exposes the read-only summary and versioned endpoints.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | 2026-09-03 | CODEX | First executable Truth Kernel node, relationship, validation, and read contract |
