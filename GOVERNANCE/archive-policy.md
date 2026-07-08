---
title: Archive Policy
id: apx-governance-archive-policy
department: LUMIAION
domain: governance
type: policy
status: active
version: 1.0.0
created: 2026-07-07
updated: 2026-07-07
source: git
tags: [archive, retention, memory]
related: [versioning-policy.md, ../ARCHIVE/README.md]
owner: Knowledge Atlas Office
---

# Archive Policy

## Archive Instead of Delete

Move superseded or retired material to `ARCHIVE/` unless removal is required for security, privacy, or legal reasons.

## Archive Metadata

Archived files must retain frontmatter and set:

```yaml
status: archived
```

## Archive Notes

Each archived file should include:

- Reason for archive.
- Replacement document, if any.
- Archive date.
- Owner.

## Index Updates

When content is archived:

1. Update `INDEX/status-index.md`.
2. Update `INDEX/master-index.md`.
3. Add replacement links if applicable.

