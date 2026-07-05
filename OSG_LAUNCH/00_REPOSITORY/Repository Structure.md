---
title: "OSG Repository Structure"
status: active
version: "1.0.0"
created: 2026-07-04
updated: 2026-07-04
artifact_type: technical-architecture
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[OSG_LAUNCH/README]]"]
related_documents: ["[[GitHub Best Practices]]", "[[Naming Conventions]]"]
related_research_programs: []
tags: [osg, repository, launch]
---

# OSG Repository Structure

## Purpose

Define the minimum production-ready repository structure required for launch.

## Recommended Repository

Use a separate public-business repository:

```text
osg-launch/
  README.md
  .gitignore
  .env.example
  .github/
    workflows/
      validate.yml
    ISSUE_TEMPLATE/
    PULL_REQUEST_TEMPLATE.md
  apps/
    web/
  content/
    courses/
    posts/
    emails/
    media-index/
  operations/
    runbooks/
    checklists/
    launch/
  automation/
    calendly/
    stripe/
    email/
    content-workflow/
  clients/
    templates/
  docs/
    architecture/
    decisions/
    setup/
  scripts/
  tests/
```

## Rules

- Keep OSG code, clients, revenue systems, and public content separate from Alpha Proxima.
- Store secrets only in environment managers or GitHub secrets, never in Markdown or code.
- Keep `content/` portable so it can move between Notion, GitHub, email, and website systems.
- Keep client-specific files out of public repositories unless explicitly sanitized.
- Add tooling only when it supports a launch workflow.

## Launch Minimum

The first production repository only needs:

- landing page or web app
- content publishing folder
- automation documentation
- deployment workflow
- environment example
- README
- PR template
- validation workflow

## Future Improvements

- [ ] Add monorepo tooling only if multiple apps appear.
- [ ] Add package publishing only if reusable libraries emerge.
- [ ] Add API service folder only after real API endpoints exist.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-04 | CODEX | Initial launch repository structure |

