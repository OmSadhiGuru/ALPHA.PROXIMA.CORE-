---
title: ALPHAPROXIMA Repository
id: apx-root-readme
department: LUMIAION
domain: institutional-memory
type: readme
status: active
version: 1.1.0
created: 2026-07-07
updated: 2026-07-07
source: git
tags: [alphaproxima, lumiaion, osgmetaphysics, knowledge-system, repository]
related: [SEARCH.md, INDEX/master-index.md, GOVERNANCE/documentation-standard.md, AUTOMATIONS/drive-sync-spec.md]
owner: Executive Office
---

# ALPHAPROXIMA

## Purpose

ALPHAPROXIMA is the canonical institutional knowledge repository for the OSGMETAPHYSICS ecosystem. It stores the long-term memory, operating records, department knowledge, agent profiles, governance rules, indexes, templates, and future retrieval substrate for the organization.

## Scope

This repository supports:

- Enterprise knowledge management.
- AI department coordination.
- Self-searching documentation.
- Metadata-driven retrieval.
- Future RAG and vector search compatibility.
- Notion, GitHub, and Google Drive synchronization.
- Long-term versioned institutional memory.

## Relationship to OSGMETAPHYSICS

OSGMETAPHYSICS is the broader institutional and philosophical ecosystem. ALPHAPROXIMA is its technical knowledge plane: the Git-native repository where OSGMETAPHYSICS knowledge is structured, versioned, indexed, and prepared for retrieval.

OSGMETAPHYSICS may contain teachings, schools, offers, field knowledge, and public outputs. ALPHAPROXIMA stores the institutional memory and operational structure that makes those assets searchable, maintainable, and reusable.

## Relationship to LUMIAION and Subminds

LUMIAION is the executive mastermind and primary coordinating intelligence for ALPHAPROXIMA.

Subminds are department-aligned knowledge functions:

| Submind | Department Function | Primary Repository Area |
| --- | --- | --- |
| LUMIAION | Executive synthesis, governance routing, institutional coherence | `DEPARTMENTS/LUMIAION/`, `GOVERNANCE/`, `INDEX/` |
| VORTEX | Signal intelligence, timing, pattern analysis, dashboards | `DEPARTMENTS/VORTEX/`, `KNOWLEDGE/`, `PROJECTS/` |
| JERANIUM | Growth, offers, distribution, business workflows | `DEPARTMENTS/JERANIUM/`, `PROJECTS/`, `PROMPTS/` |
| SOHMA | Observatory synthesis, reports, journal and dream analysis structures | `DEPARTMENTS/SOHMA/`, `KNOWLEDGE/`, `PROMPTS/` |
| ATHENA | Research, source evaluation, knowledge classification | `DEPARTMENTS/ATHENA/`, `KNOWLEDGE/`, `INDEX/source-index.md` |

Departments are permanent. Current AI models are replaceable employees.

## Relationship to Drive

Google Drive is treated as a raw source archive and working storage layer. The Drive folder `.My life unfolding.` remains untouched as source material. ALPHAPROXIMA indexes selected source files, preserves source references, and stores derived OSG-native knowledge objects under `KNOWLEDGE/`.

See `AUTOMATIONS/drive-sync-spec.md`.

## Relationship to Notion

Notion may be used as a working interface, database surface, or publishing workspace. Git remains the canonical versioned source for institutional memory. Notion records should reference ALPHAPROXIMA IDs, paths, and source indexes when mirroring durable knowledge.

## Relationship to Future Vector Database Ingestion

Future vector ingestion should treat ALPHAPROXIMA Markdown files as source documents and preserve YAML frontmatter as metadata. Each vector chunk should include:

- `id`
- `title`
- `department`
- `domain`
- `type`
- `status`
- `version`
- `source`
- `tags`
- `related`
- repository path
- Git commit reference

The vector database is a retrieval layer, not the canonical memory store.

## Inputs

- Founder decisions.
- Department outputs.
- Research notes.
- Project specifications.
- Architecture decisions.
- Agent profiles.
- Prompt libraries.
- External source summaries.
- Drive source indexes.
- Notion workspace exports or references.

## Outputs

- Versioned knowledge objects.
- Searchable indexes.
- Approved operating standards.
- Department maps.
- Project records.
- Prompt and workflow libraries.
- Archive-ready institutional memory.
- Future RAG-ready Markdown.

## Owner

Executive Mastermind: LUMIAION.

## Status

Canonical repository foundation.

## Related Folders

- `GOVERNANCE/`: policy and standards.
- `ARCHITECTURE/`: system architecture and design records.
- `DEPARTMENTS/`: permanent functional offices.
- `AGENTS/`: agent and submind profiles.
- `KNOWLEDGE/`: durable knowledge objects.
- `PROJECTS/`: project records and specifications.
- `PROMPTS/`: reusable prompt assets.
- `AUTOMATIONS/`: automation designs and integration notes.
- `INDEX/`: human and machine-readable indexes.
- `TEMPLATES/`: document templates.
- `LOGS/`: handoffs, sync notes, and operational logs.
- `ARCHIVE/`: retired or superseded material.
- `SCRIPTS/`: metadata and search utilities.

## Repository Rules

1. Every durable knowledge document must include YAML frontmatter.
2. Every major folder must keep a current `README.md`.
3. Index files must be updated when durable content is added, moved, or archived.
4. Strategic decisions must be recorded through governance or architecture decision records.
5. Archive instead of deleting institutional memory unless removal is required for security or privacy.
6. Raw external archives remain untouched; derived OSG-native knowledge objects are stored under `KNOWLEDGE/`.

