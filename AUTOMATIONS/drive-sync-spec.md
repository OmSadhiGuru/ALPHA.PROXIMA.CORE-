---
title: Drive Sync Specification
id: apx-automation-drive-sync-spec
department: LUMIAION
domain: automations
type: sync-spec
status: active
version: 1.0.0
created: 2026-07-07
updated: 2026-07-07
source: founder-request
tags: [drive-sync, google-drive, source-archive, knowledge-ingestion]
related: [../KNOWLEDGE/README.md, ../INDEX/source-index.md, ../TEMPLATES/osg-knowledge-object.template.md]
owner: Engineering Office
---

# Drive Sync Specification

## Purpose

Define how Google Drive folder `.My life unfolding.` is treated as a raw source archive for ALPHAPROXIMA knowledge ingestion.

## Scope

This specification covers indexing, source preservation, transformation, and derived OSG-native knowledge storage. It does not define a live automation implementation.

## Source Folder

```text
Google Drive/.My life unfolding.
```

## Operating Rules

### Raw Archive Remains Untouched

The Drive folder `.My life unfolding.` is treated as a source archive. Files are not renamed, reorganized, rewritten, summarized in place, or deleted by ALPHAPROXIMA workflows.

### Files Are Indexed

Each selected Drive source should receive a source index entry in `INDEX/source-index.md`.

Minimum source index fields:

- Source ID.
- Original title or filename.
- Drive path.
- File type.
- Created or observed date.
- Owner or source context.
- Processing status.
- Derived knowledge object IDs.

### Content Is Transformed Into OSG-Native Knowledge Objects

Source content is processed into structured OSG knowledge objects using `TEMPLATES/osg-knowledge-object.template.md`.

Transformation stages:

1. Raw source identification.
2. Extraction of claims, themes, or observations.
3. Synthesis into a durable principle.
4. Separation of scientific perspective and metaphysical perspective.
5. Application mapping for coaching, teaching, or operations.
6. Content output ideation.

### Original Sources Are Preserved

Derived documents must reference the original source path or source ID. The original Drive file remains the evidence base.

### Derived Documents Are Stored Under KNOWLEDGE

All transformed OSG-native documents are stored under `KNOWLEDGE/`. They should use repository metadata, source references, and stable IDs.

Recommended path pattern:

```text
KNOWLEDGE/<domain>/<knowledge-object-id>.md
```

If the domain folder does not exist, create it with a README before adding multiple objects.

## Processing Status Values

- `unindexed`
- `indexed`
- `extracted`
- `synthesized`
- `converted`
- `reviewed`
- `archived-source`

## Non-Goals

- No automatic Drive mutation.
- No automatic deletion.
- No unsupervised publication.
- No replacement of Drive as raw archive.
- No vector database write until ingestion policy is approved.

## Future Automation Notes

A future sync tool may:

- Read Drive file metadata.
- Generate source index candidates.
- Detect changed source files.
- Produce extraction drafts.
- Validate derived knowledge object metadata.

Any future automation must preserve the raw archive rule.

