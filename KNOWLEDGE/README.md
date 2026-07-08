---
title: Knowledge Folder
id: apx-knowledge-readme
department: LUMIAION
domain: knowledge
type: readme
status: active
version: 1.1.0
created: 2026-07-07
updated: 2026-07-07
source: git
tags: [knowledge, memory, retrieval, osg-knowledge-object]
related: [../INDEX/master-index.md, ../TEMPLATES/knowledge-object.template.md, ../TEMPLATES/osg-knowledge-object.template.md, ../AUTOMATIONS/drive-sync-spec.md]
owner: Knowledge Atlas Office
---

# KNOWLEDGE

## Purpose

Store durable institutional knowledge objects that should be searchable, versioned, reusable, and compatible with future retrieval systems.

## Scope

Includes research outputs, OSG-native principles, source-backed notes, operating knowledge, project knowledge, synthesis records, and reusable references.

## Knowledge Object Lifecycle

```text
RAW SOURCE -> EXTRACTION -> SYNTHESIS -> OSG PRINCIPLE -> APPLICATION -> CONTENT OUTPUT
```

## Lifecycle Definitions

### 1. RAW SOURCE

Original material remains in its source location. Examples include Google Drive files, notes, transcripts, research sources, project documents, or exported Notion records.

Rule: preserve the original source reference.

### 2. EXTRACTION

Relevant claims, observations, facts, passages, or patterns are extracted from the source.

Rule: separate extracted material from interpretation.

### 3. SYNTHESIS

Extracted material is organized into a coherent understanding.

Rule: state confidence level and evidence type.

### 4. OSG PRINCIPLE

The synthesis is distilled into a durable OSG-native principle.

Rule: the principle must be reusable outside the original source context.

### 5. APPLICATION

The principle is mapped to a practical use case such as coaching, teaching, operations, product design, research, or content.

Rule: application must state its intended audience or context.

### 6. CONTENT OUTPUT

The knowledge object generates content ideas, teaching assets, prompts, scripts, articles, course material, or publication candidates.

Rule: public outputs require approval when they affect brand, claims, offers, or publication.

## Inputs

- Drive source indexes.
- Research notes.
- Department outputs.
- Project records.
- Published material.
- Approved decisions.

## Outputs

- OSG knowledge objects.
- Indexed institutional memory.
- Retrieval-ready Markdown.
- Content output candidates.
- Coaching and teaching applications.

## Owner

Knowledge Atlas Office.

## Status

Active.

## Related Folders

- `INDEX/`
- `TEMPLATES/`
- `ARCHIVE/`
- `PROJECTS/`
- `AUTOMATIONS/`

## Storage Rules

1. Use `TEMPLATES/osg-knowledge-object.template.md` for OSG-native knowledge objects.
2. Preserve source references.
3. Use YAML frontmatter.
4. Update `INDEX/master-index.md` and `INDEX/source-index.md`.
5. Archive superseded knowledge objects instead of deleting them.

