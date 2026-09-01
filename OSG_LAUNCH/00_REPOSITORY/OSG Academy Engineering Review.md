---
title: "OSG Academy Engineering Review"
status: draft
version: "2.0.0"
created: 2026-07-05
updated: 2026-07-05
artifact_type: engineering-review
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
core_question: "Can RI-001 support a 30-day MVP launch of Awaken the Inner Guru?"
dependencies: ["[[11 - One Question Document Standard]]", "[[OSG Launch Technical Foundation]]", "[[OSG Repository Structure]]", "[[OSG Notion Workspace Architecture]]", "[[OSG Naming Conventions]]"]
related_documents: ["[[OSG_LAUNCH/README]]", "[[Repository Structure]]", "[[Notion Workspace Architecture]]", "[[Naming Conventions]]", "[[Automation Opportunities]]", "[[30 Day Implementation Roadmap]]", "[[OSG_LAUNCH/09_TEMPLATES/README]]"]
related_research_programs: []
tags: [osg, academy, engineering-review, architecture, scalability, ri-001]
---

# OSG Academy Engineering Review

## Purpose

Re-audit OSG Academy production readiness using the actual committed Reference Implementation Blueprint for `RI-001 — Awaken the Inner Guru` as the primary audit target.

## Source Materials Reviewed

| Source | Location Reviewed | Status |
|--------|-------------------|--------|
| RI-001 Reference Implementation Blueprint | Git commit `4fe8d20`, path `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Committed in history; not present in current working tree |
| OSG Learning Standard | Git commit `4fe8d20`, path `OSG_BUSINESS/OSG_ACADEMY/OSG Learning Standard (OLS) v1.0.md` | Committed in history; not present in current working tree |
| Bilingual FR/EN Production Model | Git commit `4fe8d20`, path `OSG_BUSINESS/OSG_ACADEMY/Awaken the Inner Guru — Production Blueprint.md`, §11 | Committed in history; not present in current working tree |
| One Question Document Standard | `08_SYSTEMS/Engineering Standards/11 - One Question Document Standard.md` | Present in current tree |
| Repository README | `OSG_LAUNCH/README.md` and `OSG_LAUNCH/00_REPOSITORY/README.md` | Present in current tree |
| Templates README | `OSG_LAUNCH/09_TEMPLATES/README.md` | Present in current tree |

## Executive Assessment

RI-001 is a strong production architecture for a course MVP. It is substantially more mature than the launch foundation alone. It defines the transformation arc, weekly structure, lesson inventory, learning validation, Knowledge Library IDs, personalization layer, community layer, workbook and journal structure, production gates, AI compatibility, and governance.

The course can plausibly reach MVP launch readiness within 30 days if production is scoped tightly: one flagship course, FR-first with EN transcreation, limited automation, manual operations, and no app/API dependency.

The main issue is not course architecture. The main issue is production handoff: the canonical OSG Academy source files are committed in Git history but are not present in the current working tree. Production should not proceed until the active repository location for OSG Academy is restored or intentionally migrated.

## Production-Readiness Score

**82 / 100 for launching the Awaken the Inner Guru course MVP within 30 days.**

### Score Breakdown

| Dimension | Score | Assessment |
|-----------|-------|------------|
| RI-001 course architecture | 91 | Strong reference implementation; enough detail to guide production |
| OLS compliance | 88 | OLS alignment is explicit; Gate-1/Gate-2 process exists |
| Bilingual model | 84 | Strong FR/EN transcreation model; termbase and QC execution still needed |
| One-question modularity | 77 | Standard exists; RI-001 is still broad and should spawn smaller production artifacts |
| Course MVP readiness | 82 | Ready to enter production after Gate-1 and source restoration |
| Repository readiness | 62 | Current working tree lacks the committed OSG_BUSINESS source stack |
| Template readiness | 68 | Launch templates exist; academy-specific lesson/workbook/journal templates still missing |
| Future app/API readiness | 58 | Conceptual compatibility exists; schemas and API contracts do not |
| AI readiness | 70 | Boundaries are good; retrieval implementation and learner data policy are missing |
| Knowledge graph readiness | 74 | KL IDs exist; graph schema and registry still needed |

## Architecture Review

### What Works

- RI-001 correctly treats the course as architecture, not content.
- It implements a clear Week 0 to Week 8 progression plus 90-day integration.
- It defines 18 lessons with objectives, practice evidence, journal/community elements, Knowledge Library nodes, and future AI opportunities.
- It includes behavioral learning validation rather than relying on quizzes or passive completion.
- It incorporates workbook, journal, production, and bilingual details by reference rather than duplicating them.
- It defines living-reference governance, Reference Review, limitations, future improvements, and OLS compatibility.
- It preserves OSG's core constraint: the course builds learner sovereignty and does not provide answers.

### What Needs Engineering Work

- The active file location is unresolved: `OSG_BUSINESS/OSG_ACADEMY/` exists in Git history but not in the current tree.
- OLS version references are inconsistent across sources: RI-001 says OLS v1.1, the available OLS file is v1.0, and the Production Blueprint references OLS v1.0 while RI-001 references OLS v1.1.
- RI-001 uses Knowledge Library IDs (`KL-000` through `KL-026`), but no active Knowledge Library registry exists in the current OSG workspace.
- Lesson IDs exist informally (`L0.1`, `L8.2`) but not as formal durable IDs suitable for database/API use.
- Workbook, journal, media, translation, community, and progress IDs are specified conceptually or by examples, not as a complete ID standard.
- AI integration is architected as future-compatible, but no retrieval boundary, memory policy, or event schema exists.

## Review of Required Artifacts

### RI-001 Blueprint

Assessment: production-usable after source restoration and Gate-1 approval.

Strengths:

- Clear course mission and transformation promise.
- Explicit ideal learner and not-for criteria.
- Strong transformation map ending in autonomy, not mere completion.
- Weekly blueprint includes purpose, transformation, objectives, assets, evidence, and success criteria.
- Lesson inventory is sufficient for script planning.
- Knowledge Library integration is unusually strong for a first course.
- Known limitations are explicit, which improves governance.

Engineering concerns:

- It is still a large reference document. It should remain the benchmark, but production should split into separate single-question artifacts: course registry entry, lesson registry, workbook spec, journal spec, media manifest, translation manifest, and production checklist.
- It relies on the Production Blueprint by reference, but that file is not active in the current working tree.
- Gate-1 status is pending. That blocks recording and scripting under the OLS pipeline.

### OSG Learning Standard

Assessment: strong enough for MVP governance.

Strengths:

- Defines the Transformation Path.
- Defines Course Blueprint and Lesson Blueprint requirements.
- Provides production gates.
- Defines AI boundaries.
- Defines progress indicators.
- Defines compliance review.

Engineering concerns:

- The reviewed file is v1.0 while RI-001 references v1.1.
- OLS should have a canonical active path and stable `document_id`.
- OLS checklists should be extracted into executable templates/checklists for production QA.

### Bilingual Model

Assessment: strong for launch if operationalized immediately.

Strengths:

- French source and English transcreation are clearly defined.
- Asset strategy distinguishes native, transcreated, and subtitled outputs.
- Subtitles use soft `.srt` and `.vtt`.
- Language metadata schema exists.
- Translation QC is explicit and practical.
- ES/AR expansion is considered without overcommitting to launch scope.

Engineering concerns:

- Termbase does not appear in the current tree.
- Translation status tracking is not implemented as a registry or database.
- Bilingual reviewer roles are defined but not assigned in an operational system.
- Asset filenames are specified, but no media manifest exists.

### One Question Document Standard

Assessment: correct and important, but not yet enforced.

The standard is now present and should govern OSG Academy immediately. RI-001 itself is a broad reference artifact and can remain broad because its core question is clear: "How is Awaken the Inner Guru structured as the reference implementation?" Production artifacts derived from it must be narrower.

Required next step: add `core_question` to OSG Academy templates and validators.

### Repository README

Assessment: launch-suitable but not academy-complete.

The current `OSG_LAUNCH` README correctly isolates OSG from Alpha Proxima and organizes launch operations. It does not yet represent the committed `OSG_BUSINESS/OSG_ACADEMY` governance stack. That mismatch should be resolved before production.

### Templates README

Assessment: adequate for launch operations; insufficient for RI-001 production.

Current templates cover course, client, content, and automation basics. RI-001 requires academy-specific templates:

- Reference Implementation Template
- OLS Compliance Review Template
- Lesson Blueprint Template
- Lesson Script Template
- Workbook Blueprint Template
- Journal Blueprint Template
- Knowledge Node Template
- Bilingual Asset Template
- Translation QC Template
- Progress Event Template

## Blockers That Prevent Course Production Now

These block immediate recording/scripting under OLS discipline.

| Blocker | Why It Blocks | Required Action |
|---------|---------------|-----------------|
| Canonical OSG Academy files are not in current working tree | Production team cannot reliably work from historical Git objects | Restore or migrate `OSG_BUSINESS/OSG_ACADEMY/` into the active repository structure |
| Gate-1 approval is pending | OLS says nothing is scripted or recorded before blueprint approval | Record Gate-1 decision for RI-001 |
| OLS version mismatch | RI-001 references OLS v1.1, available OLS source is v1.0 | Add or restore OLS v1.1, or update RI-001 compatibility notes |
| Termbase missing from active workspace | Bilingual model requires termbase before lesson scripting | Create `AIG/_termbase` or database-backed termbase |
| Evidence reference list missing | `[E]` claims need sources before production scripts lock | Build evidence/reference registry for KL nodes and lessons |
| Lesson script templates missing | RI-001 has lesson architecture, not scripts | Create OLS 12-part lesson script template |
| Translation QC checklist not operationalized | Bilingual launch requires repeatable QC | Create Translation QC template and tracking database |
| Media/asset manifest missing | Production cannot manage FR/EN videos, subtitles, workbooks, audio reliably | Create media manifest with asset IDs and language metadata |

## Blockers That Only Affect Future App/API Scale

These do not block a 30-day course MVP if launch is manual or platform-based.

| Future Blocker | Affected Scale |
|----------------|----------------|
| No production database schema | Web/mobile apps, learner accounts, progress dashboards |
| No formal API contract | Future web app, mobile app, YUNA integrations |
| No learner event schema | Progress tracking automation and AI personalization |
| No authentication/authorization model | Learner app, community, paid access |
| No AI retrieval implementation | YUNA, LUMIAION orchestration, tutor memory |
| No OSG Knowledge Graph registry | Cross-course graph, Knowledge Library search, recommendation systems |
| No community data model | Scaled community, cohorts, moderation tooling |
| No analytics event taxonomy | Retention, completion, and learning outcome analysis |
| No mobile app structure | Native app delivery |
| No localization database | ES/AR expansion at scale |

## Nice-to-Have Improvements

These improve quality but should not block MVP launch.

- Build an automated OLS validator.
- Add a visual course map.
- Add graph exports for KL nodes.
- Add AI tutor prompt templates.
- Add cohort retrospective template.
- Add instructor certification checklist.
- Add auto-generated subtitles workflow.
- Add Notion dashboards for production status.
- Add GitHub Actions for Markdown/frontmatter validation.
- Add a lightweight static site preview for course docs.

## Scalability Review

### 100+ Courses

RI-001 gives a credible pattern for 100+ courses because it defines a reference course, OLS governance, Reference Review, stable KL nodes, and production gates.

Remaining requirement: formal course, module, lesson, asset, translation, and progress ID standards.

Recommended IDs:

```text
COURSE-AIG-001
MOD-AIG-00
LESSON-AIG-00-01
WB-AIG-001
WBEX-AIG-001-001
JRN-AIG-001
JP-AIG-001-001
MEDIA-AIG-M03-L02-TEACHING-FR-V001
TR-AIG-M03-L02-EN-V001
COMM-AIG-FR-001
PROG-AIG-LESSON-COMPLETE
```

### Thousands of Learners

RI-001 defines progress evidence, but not learner-scale storage.

MVP can use manual/self-reported tracking. Scale requires:

- learner table
- enrollment table
- lesson progress events
- practice logs
- workbook completion records
- journal prompt completion records
- community participation events
- consent and privacy controls

### Multilingual Content

The bilingual model is strong. It should be considered production-grade as architecture.

Execution requirements:

- termbase
- translation manifest
- language metadata
- reviewer sign-off
- subtitle files
- language-specific community routing

### AI Tutors

RI-001 is future-compatible but not implementation-ready. AI should not be part of the MVP launch dependency. It can be added after the first cohort if learner data, consent, retrieval boundaries, and OLS AI rules are implemented.

## Knowledge Graph Compatibility

Compatibility: good at architecture level, incomplete at implementation level.

Strengths:

- KL nodes exist and are stable enough to seed a Knowledge Library.
- Future Alpha Proxima bridge nodes are labeled.
- Lessons map to KL nodes.
- AI opportunities map to lessons.

Missing:

- active Knowledge Library registry
- graph node schema
- graph relationship schema for OSG Academy
- source/evidence references per `[E]` claim
- graph export from RI-001 tables

Recommended first graph nodes:

- Course
- Module
- Lesson
- Knowledge Node
- Practice
- Workbook Section
- Journal Prompt
- Media Asset
- Translation
- Progress Event
- Community Space

## Database Compatibility

Compatibility: partial.

RI-001 provides enough domain structure to design tables, but not enough to implement without translation into schema.

Minimum MVP database can be avoided if course launches on an existing platform. Future app/API scale requires:

- courses
- modules
- lessons
- lesson_assets
- knowledge_nodes
- media_assets
- translations
- learners
- enrollments
- progress_events
- journal_entries
- workbook_submissions
- community_spaces
- community_events

## API Readiness

Current API readiness: moderate conceptually, low technically.

RI-001 defines entities but not endpoint contracts. This does not block MVP if no custom app is being launched.

Future API groups:

- Course Catalog API
- Lesson Delivery API
- Asset API
- Translation API
- Learner Progress API
- Journal API
- Workbook API
- Knowledge Library API
- AI Tutor API
- Community API

## Future AI Readiness

AI readiness: good architecture, incomplete implementation.

Positive:

- RI-001 defines AI as support, not dependency.
- YUNA and LUMIAION roles are bounded.
- AI opportunities are mapped per lesson.
- OLS AI boundaries are explicit.

Missing:

- retrieval source registry
- learner memory consent model
- distress escalation workflow
- tutor prompt templates
- audit logs for AI interactions
- separation policy between OSG learner data and Alpha Proxima institutional memory

## Repository Recommendations

### Immediate Repository Fix

Decide one active canonical location:

```text
OSG_BUSINESS/OSG_ACADEMY/
```

or migrate into:

```text
OSG_LAUNCH/10_ACADEMY/
```

Do not keep RI-001 only in Git history. The production team needs the source files in the active tree.

### Recommended Active Structure for MVP

```text
OSG_LAUNCH/
  10_ACADEMY/
    README.md
    OSG Learning Standard.md
    RI-001 Awaken the Inner Guru Reference Implementation Blueprint.md
    Awaken the Inner Guru Production Blueprint.md
    AIG/
      _termbase/
      _manifests/
      FR/
      EN/
      _shared/
```

### Recommended Production Manifests

- `course_manifest.yaml`
- `lesson_manifest.yaml`
- `knowledge_nodes.yaml`
- `media_manifest.yaml`
- `translation_manifest.yaml`
- `progress_events.yaml`
- `community_spaces.yaml`

## 30-Day MVP Readiness Plan

### Week 1

- Restore/migrate canonical OSG Academy files into active tree.
- Resolve OLS v1.0/v1.1 version mismatch.
- Approve Gate-1 for RI-001.
- Create termbase.
- Create lesson script template.
- Create production manifests.

### Week 2

- Script Week 0 through Week 2.
- Build workbook and journal skeletons.
- Create evidence registry for `[E]` claims.
- Build FR/EN translation workflow tracker.
- Create community onboarding flow.

### Week 3

- Record MVP lessons or pilot module set.
- Produce FR/EN workbook and journal MVP.
- Produce subtitles/captions for first module.
- Configure course platform, payments, booking, and email.
- Run internal QC.

### Week 4

- Complete MVP QA.
- Run OLS Gate-2 review for launch scope.
- Open pilot cohort enrollment.
- Track learner onboarding, practice logs, and community participation manually.
- Capture production lessons learned.

## Final Classification

### Production Can Start After These Are Done

- Source files restored to active tree.
- Gate-1 approved.
- OLS version mismatch resolved.
- Termbase created.
- Lesson script template created.
- Evidence/reference registry started.
- Media and translation manifests created.

### MVP Can Launch Without These

- Custom web app.
- Mobile app.
- API.
- Database-backed learner platform.
- AI tutor.
- Automated Knowledge Graph.
- Full ES/AR localization.
- Advanced analytics.

### MVP Should Not Launch Without These

- Clear course source of truth.
- FR/EN language workflow if bilingual launch is promised.
- OLS compliance checklist.
- Therapy/refer-out boundary language.
- Payment, access, and onboarding flow.
- Community rules and moderation owner.
- Minimum progress tracking.

## Implementation Notes

This review does not rewrite RI-001, OLS, or the bilingual production model. It verifies technical implementability and production readiness.

The key engineering conclusion: RI-001 is architecturally strong enough for MVP production. The remaining hard blockers are operationalization, source restoration, ID/manifest discipline, and production gates.

## Future Improvements

- [ ] Restore/migrate `OSG_BUSINESS/OSG_ACADEMY` into the active workspace.
- [ ] Create OSG Academy ID Standard.
- [ ] Create OSG Academy Production Manifest Standard.
- [ ] Create OLS Validator.
- [ ] Create Knowledge Library registry from RI-001 KL nodes.
- [ ] Create course MVP dashboard.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 2.0.0 | 2026-07-05 | CODEX | Revised review using committed RI-001, OLS, and bilingual model as primary audit sources |
| 1.0.0 | 2026-07-05 | CODEX | Initial review based only on visible OSG launch foundation |

