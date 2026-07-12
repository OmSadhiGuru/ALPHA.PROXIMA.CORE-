---
title: Information Routing Map
id: apx-organization-information-routing-map
department: LUMIAION
domain: organization
type: organization-map
status: active
version: 1.0.0
created: 2026-07-11
updated: 2026-07-11
source: founder-request
tags: [organization, routing, knowledge-flow]
related: [../INGESTION/README.md, ../OPERATIONS/CPOS/README.md, ../KNOWLEDGE/README.md, escalation-map.md]
owner: "Office of Knowledge (scope pending Founder ratification)"
---

# Information Routing Map

## Purpose

Show how knowledge actually moves through the repository, tying together the Ingestion Engine, CPOS production flow, and Knowledge storage as one route rather than three separate systems.

## Route

```
External Source (Drive, research, Founder input)
  → INGESTION/ (Source Record → Extraction → Classification → Founder Synthesis)
    → gated by INGESTION/ingestion-approval-gates.md
      → KNOWLEDGE/<domain>/ (OSG Knowledge Object)
        → INDEX/master-index.md, INDEX/source-index.md (discoverability)
          → OPERATIONS/CPOS/ (if the object feeds active production work)
            → OPERATIONS/CPOS/PUBLISHING_QUEUE.md → OSGMETAPHYSICS (if public-bound)
              → OPERATIONS/CPOS/KNOWLEDGE_QUEUE.md (capture lessons back into KNOWLEDGE/)
```

## Cross-System Notes

- The Ingestion Engine (`../INGESTION/`) and CPOS (`../OPERATIONS/CPOS/`) are **sequential, not parallel**, for any item that starts as a raw source: ingestion produces the Knowledge Object; CPOS only picks it up once it exists, if it needs production/publishing handling.
- Not everything in `KNOWLEDGE/` passes through CPOS — internal-only knowledge objects (Gate 5 not triggered, see `../INGESTION/ingestion-approval-gates.md`) may stay purely within `KNOWLEDGE/` and `INDEX/`.
- `../OPERATIONS/CPOS/KNOWLEDGE_QUEUE.md` closes the loop: production lessons and published-content learnings route back into `KNOWLEDGE/`, which is a second entry point into knowledge storage besides raw-source ingestion.

## Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0.0 | 2026-07-11 | Claude (Constitutional Secretary / Institutional Architect) | Initial Information Routing Map, Phase II Sprint 2. |
