---
title: "OSG Naming Conventions"
status: active
version: "1.0.0"
created: 2026-07-04
updated: 2026-07-04
artifact_type: naming-standard
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[OSG_LAUNCH/README]]"]
related_documents: ["[[Repository Structure]]"]
related_research_programs: []
tags: [osg, naming, standard]
---

# OSG Naming Conventions

## Purpose

Keep launch files searchable, readable, and portable across GitHub, Notion, media tools, and automation systems.

## General Rules

- Use clear human-readable names in Notion.
- Use lowercase kebab-case for code folders and URLs.
- Use date prefixes for scheduled content and exports.
- Use client codes instead of full client names in technical systems.
- Avoid spaces in production asset filenames.

## Patterns

| Artifact | Pattern | Example |
|----------|---------|---------|
| Course folder | `course-slug` | `ai-workflow-foundations` |
| Lesson file | `lesson-##-slug.md` | `lesson-01-foundation.md` |
| Client code | `CLIENT-YYYY-###` | `CLIENT-2026-001` |
| Content item | `YYYY-MM-DD-channel-slug.md` | `2026-07-15-email-launch-note.md` |
| Media export | `YYYY-MM-DD-channel-slug-v##.ext` | `2026-07-15-youtube-intro-v01.mp4` |
| Automation | `tool-trigger-action` | `calendly-booking-create-lead` |
| Decision | `DEC-YYYY-### - Title` | `DEC-2026-001 - Launch Offer` |

## Future Improvements

- [ ] Add automated filename validator.
- [ ] Add Notion formula examples.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-04 | CODEX | Initial naming convention |

