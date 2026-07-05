---
title: "OSG GitHub Best Practices"
status: active
version: "1.0.0"
created: 2026-07-04
updated: 2026-07-04
artifact_type: technical-standard
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Repository Structure]]"]
related_documents: ["[[Naming Conventions]]"]
related_research_programs: []
tags: [osg, github, repository]
---

# OSG GitHub Best Practices

## Purpose

Define practical GitHub rules for launch without overbuilding process.

## Branches

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready state |
| `launch/*` | Launch implementation branches |
| `content/*` | Content updates |
| `automation/*` | Automation updates |
| `hotfix/*` | Urgent fixes |

## Pull Requests

Every pull request should include:

- purpose
- screenshots or preview link when visual changes exist
- test or validation result
- deployment impact
- rollback note

## Required Files

- `README.md`
- `.gitignore`
- `.env.example`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/validate.yml`
- `docs/setup/local-development.md`
- `docs/decisions/`

## Commit Style

Use clear, small commits:

```text
feat: add launch landing page
fix: repair checkout redirect
docs: add client onboarding runbook
chore: update content calendar
```

## Release Tags

Use tags for launch milestones:

```text
launch-v0.1
launch-v1.0
course-v1.0
automation-v1.0
```

## Security Rules

- Never commit API keys.
- Never commit client personal data.
- Use GitHub secrets for deployment variables.
- Keep `.env.example` complete but non-sensitive.
- Require review before changing Stripe, email, or booking flows.

## Future Improvements

- [ ] Add CODEOWNERS when multiple contributors join.
- [ ] Add protected branches after initial launch velocity stabilizes.
- [ ] Add automated preview deployments.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-04 | CODEX | Initial GitHub practice standard |

