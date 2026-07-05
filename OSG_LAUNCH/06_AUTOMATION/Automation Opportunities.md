---
title: "OSG Automation Opportunities"
status: active
version: "1.0.0"
created: 2026-07-04
updated: 2026-07-04
artifact_type: automation-plan
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[OSG_LAUNCH/README]]"]
related_documents: ["[[Notion Workspace Architecture]]", "[[Content Workflow]]"]
related_research_programs: []
tags: [osg, automation, calendly, stripe, email]
---

# OSG Automation Opportunities

## Purpose

Identify launch automations that reduce repetitive work without adding unnecessary complexity.

## Priority Automations

| Area | Trigger | Action | Launch Priority |
|------|---------|--------|-----------------|
| Calendly | Discovery call booked | Create Notion client lead, send confirmation, add prep task | High |
| Calendly | Call completed | Create follow-up task and email draft | High |
| Stripe | Payment completed | Create client/course access task, send receipt sequence | High |
| Stripe | Failed payment | Notify owner and create follow-up task | Medium |
| Email | New lead magnet signup | Add subscriber tag and welcome sequence | High |
| Email | Course purchase | Send onboarding sequence | High |
| Content | Content status becomes scheduled | Create publication checklist | Medium |
| Content | Content published | Create repurpose task and metrics checkpoint | Medium |
| Operations | Weekly review day | Generate review checklist | Medium |

## Launch Stack Boundary

Do not automate everything on day one. Launch needs:

- booking confirmation
- payment confirmation
- lead capture
- welcome email
- client/course onboarding checklist
- weekly review reminder

## Failure Handling

Each automation should define:

- owner
- trigger
- expected output
- retry rule
- manual fallback
- notification channel

## Future Improvements

- [ ] Add n8n workflows after manual workflow is stable.
- [ ] Add webhook logging.
- [ ] Add automation health dashboard.
- [ ] Add CRM sync if client volume requires it.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-04 | CODEX | Initial automation opportunity map |

