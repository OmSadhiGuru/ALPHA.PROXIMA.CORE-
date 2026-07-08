---
title: Versioning Policy
id: apx-governance-versioning
department: LUMIAION
domain: governance
type: policy
status: active
version: 1.0.0
created: 2026-07-07
updated: 2026-07-07
source: git
tags: [versioning, lifecycle, git]
related: [archive-policy.md, documentation-standard.md]
owner: Engineering Office
---

# Versioning Policy

## Document Versioning

Use semantic versions for durable operating documents:

- `1.0.0`: first stable version.
- `1.1.0`: meaningful additive change.
- `1.1.1`: correction or clarification.
- `2.0.0`: breaking structure or policy change.

## Git Versioning

Every material change should be committed with a message that names the changed area.

Example:

```text
Add ALPHAPROXIMA metadata and index foundation
```

## Status Lifecycle

Allowed status values:

- `draft`
- `active`
- `review`
- `approved`
- `superseded`
- `archived`

## Supersession

When a file replaces another file, set the old file status to `superseded` and add the replacement file to `related`.

