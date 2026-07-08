---
title: Search Guide
id: apx-search-guide
department: LUMIAION
domain: retrieval
type: guide
status: active
version: 1.0.0
created: 2026-07-07
updated: 2026-07-07
source: git
tags: [search, retrieval, metadata, rag, vector-search]
related: [INDEX/master-index.md, GOVERNANCE/documentation-standard.md]
owner: Knowledge Atlas Office
---

# Search Guide

## Purpose

This file defines how humans and future AI systems search ALPHAPROXIMA using Git-native tools and metadata.

## GitHub Search

Use GitHub repository search for exact terms, paths, and metadata keys.

Examples:

```text
repo:OWNER/REPO department: VORTEX
repo:OWNER/REPO tags: source
repo:OWNER/REPO path:ALPHAPROXIMA/KNOWLEDGE status: active
repo:OWNER/REPO "type: architecture-decision"
```

## VS Code Search

Use global search for plain text and metadata fields.

Recommended searches:

```text
department: SOHMA
status: draft
tags: [
related:
owner:
```

## ripgrep

Use `rg` from the repository root.

```bash
rg -n "department: VORTEX" ALPHAPROXIMA
rg -n "status: active" ALPHAPROXIMA/KNOWLEDGE
rg -n "tags: .*rag" ALPHAPROXIMA
rg -n "related: .*LUMIAION" ALPHAPROXIMA
```

## Tags

Tags are used for lightweight retrieval. Use lowercase kebab-case values.

Examples:

- `institutional-memory`
- `agent-profile`
- `research-note`
- `architecture`
- `prompt`
- `notion-sync`
- `drive-sync`
- `github-sync`

## Metadata Search

All durable documents support this YAML frontmatter:

```yaml
---
title:
id:
department:
domain:
type:
status:
version:
created:
updated:
source:
tags:
related:
owner:
---
```

Use `id` for durable references. Use `related` for graph traversal. Use `status` to filter active, draft, archived, or superseded records.

## Index Files

Indexes in `INDEX/` are the first place to search when the exact file is unknown.

- `master-index.md`: all durable objects.
- `department-index.md`: department-owned material.
- `project-index.md`: project records.
- `prompt-index.md`: prompt assets.
- `source-index.md`: source material.
- `tag-index.md`: controlled tag vocabulary.
- `status-index.md`: lifecycle state.

## Future Vector Database

Future vector search should ingest:

- Markdown body text.
- YAML frontmatter.
- File path.
- Git commit reference.
- Index references.
- Outgoing `related` links.

Chunking recommendation:

- Split by heading.
- Preserve frontmatter in every chunk payload.
- Store `id`, `department`, `domain`, `type`, `status`, `version`, `tags`, `owner`, and path as metadata.

