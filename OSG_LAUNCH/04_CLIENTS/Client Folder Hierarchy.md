---
title: "OSG Client Folder Hierarchy"
status: active
version: "1.0.0"
created: 2026-07-04
updated: 2026-07-04
artifact_type: folder-standard
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[OSG_LAUNCH/README]]"]
related_documents: ["[[Naming Conventions]]"]
related_research_programs: []
tags: [osg, clients, folders]
---

# OSG Client Folder Hierarchy

## Purpose

Define a privacy-conscious client folder pattern.

## Client Folder

```text
CLIENT-CODE/
  README.md
  00_profile.md
  01_onboarding.md
  02_sessions/
  03_deliverables/
  04_follow_up/
  99_archive/
```

## Required Client README Sections

- client code
- offer
- status
- start date
- next action
- delivery links
- private data location

## Security Boundary

Client folders should not become the legal, financial, or sensitive-data source of truth unless the repository is private and access-controlled.

## Future Improvements

- [ ] Add CRM sync later.
- [ ] Add sanitized export workflow.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-04 | CODEX | Initial client folder standard |

