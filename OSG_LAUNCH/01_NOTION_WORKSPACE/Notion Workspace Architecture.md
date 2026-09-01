---
title: "OSG Notion Workspace Architecture"
status: active
version: "1.0.0"
created: 2026-07-04
updated: 2026-07-04
artifact_type: workspace-architecture
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[OSG_LAUNCH/README]]"]
related_documents: ["[[Automation Opportunities]]", "[[30 Day Implementation Roadmap]]"]
related_research_programs: []
tags: [osg, notion, operations, clients, content]
---

# OSG Notion Workspace Architecture

## Purpose

Design the launch Notion workspace for courses, clients, content, automation, and operations.

## Top-Level Pages

```text
OSG HQ
  Launch Dashboard
  Courses
  Clients
  Content Calendar
  Media Library
  Automation Hub
  Operations
  Metrics
  Archive
```

## Core Databases

| Database | Purpose | Minimum Properties |
|----------|---------|--------------------|
| Courses | Track course products and modules | Name, Status, Offer, Owner, Launch Date, Assets, Notes |
| Lessons | Track lesson production | Lesson, Course, Status, Script, Media, Publish Status |
| Clients | Track leads and clients | Name, Status, Source, Offer, Next Action, Owner |
| Sessions | Track client delivery | Client, Date, Type, Notes, Follow Up |
| Content | Track public content | Title, Channel, Status, Publish Date, Asset, CTA |
| Media Assets | Track reusable media | Name, Type, Status, Location, Usage Rights |
| Automations | Track automation workflows | Name, Trigger, Tool, Status, Owner, Failure Mode |
| Operations Tasks | Track launch work | Task, Priority, Status, Due Date, Owner |
| Metrics | Track business signals | Metric, Period, Value, Source |

## Status Values

Use consistent statuses:

```text
idea
draft
ready
scheduled
published
active
paused
done
archived
```

## Launch Dashboard

The dashboard should show:

- launch checklist
- current week priorities
- active clients
- next content to publish
- course build progress
- automation status
- revenue and booking metrics
- blockers

## Boundaries

- Do not store Alpha Proxima constitutional material in this workspace.
- Do not store secrets in Notion.
- Do not use Notion as the source of truth for production code.
- Do not store sensitive client data beyond what is operationally required.

## Future Improvements

- [ ] Add synced templates for course, client, and content records.
- [ ] Add Notion-to-GitHub content export.
- [ ] Add lightweight client portal after launch.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-04 | CODEX | Initial Notion workspace architecture |

