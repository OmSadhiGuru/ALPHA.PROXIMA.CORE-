---
title: "OSG Academy Engineering Review"
status: draft
version: "1.0.0"
created: 2026-07-05
updated: 2026-07-05
artifact_type: engineering-review
institutional_owner: "OSG"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
core_question: "Can the OSG Academy blueprint become the foundation of a production ecosystem?"
dependencies: ["[[OSG Launch Technical Foundation]]", "[[OSG Repository Structure]]", "[[OSG Notion Workspace Architecture]]", "[[OSG Naming Conventions]]", "[[11 - One Question Document Standard]]"]
related_documents: ["[[OSG_LAUNCH/README]]", "[[Repository Structure]]", "[[Notion Workspace Architecture]]", "[[Naming Conventions]]", "[[Automation Opportunities]]", "[[30 Day Implementation Roadmap]]"]
related_research_programs: []
tags: [osg, academy, engineering-review, architecture, scalability]
---

# OSG Academy Engineering Review

## Purpose

Audit whether the current OSG Academy technical foundation can support a production ecosystem.

## Source Limitation

The Claude Reference Blueprint was not found in the local vault. Searches for `Reference Blueprint`, `Awaken the Inner Guru`, `Workbook Blueprint`, `Journal Blueprint`, `OSG Academy`, `Living Genome`, and `YUNA` returned no matching local Markdown source.

This review therefore audits the current OSG launch foundation and identifies what must exist before the Reference Blueprint can be accepted as a production foundation.

## Architecture Review

The current OSG foundation is suitable for launch operations. It is not yet sufficient for OSG Academy at scale.

Current strengths:

- OSG is isolated from Alpha Proxima infrastructure.
- Launch folders exist for repository, Notion, courses, media, clients, content, automation, operations, roadmap, and templates.
- Naming conventions exist for courses, lessons, clients, content, media, automations, and decisions.
- Basic Notion workspace architecture exists.
- GitHub practices exist at launch level.

Current gaps:

- No academy domain model exists.
- No Reference Blueprint file exists locally.
- No course, lesson, workbook, journal, media, translation, community, or progress ID standard exists.
- No database schema exists beyond high-level Notion database descriptions.
- No API contract exists.
- No AI retrieval model exists.
- No knowledge graph schema specific to OSG Academy exists.
- No multilingual content model exists.
- No learner progress model exists.
- No AI tutor interaction model exists.

## Missing Components

### Core Academy Systems

| System | Status | Required Before Scale |
|--------|--------|-----------------------|
| Course Catalog | Missing | Canonical course registry with stable IDs |
| Lesson Registry | Missing | Stable lesson IDs and sequence model |
| Workbook Registry | Missing | Workbook IDs, page IDs, exercise IDs |
| Journal Registry | Missing | Journal IDs, prompt IDs, reflection types |
| Media Registry | Partial | Media IDs, rights, language, transcript links |
| Translation Registry | Missing | Translation IDs, source locale, target locale, review status |
| Learner Registry | Missing | Learner profile, enrollment, consent, preferences |
| Progress Tracking | Missing | Lesson, module, workbook, journal, quiz, and milestone events |
| Knowledge Library | Missing | Concepts, practices, references, glossary, citations |
| Living Genome | Missing | Domain model and graph relation rules |
| AI Tutor Layer | Missing | Tutor memory boundaries, retrieval scope, escalation rules |
| YUNA | Missing | Product role, permissions, data access, memory contract |
| LUMIAION Interface | Missing | Boundary between Alpha Proxima reasoning and OSG product systems |
| Community System | Missing | Community IDs, roles, moderation, posts, cohorts |
| Assessment System | Missing | Quiz, reflection, rubric, and competency model |

### Required Templates

- Course Blueprint Template
- Module Blueprint Template
- Lesson Blueprint Template
- Workbook Blueprint Template
- Workbook Exercise Template
- Journal Blueprint Template
- Journal Prompt Template
- Media Asset Template
- Translation Package Template
- AI Tutor Prompt Template
- Knowledge Library Entry Template
- Living Genome Node Template
- Learner Progress Event Template
- Community Space Template
- API Endpoint Template

## Scalability Review

### 100+ Courses

Current launch folders can store course files, but they do not yet support 100+ courses safely. At that scale OSG needs a course registry, course IDs, lifecycle statuses, ownership, prerequisites, language variants, versions, and dependency maps.

Required ID pattern:

```text
COURSE-YYYY-###
MODULE-COURSE-###
LESSON-COURSE-###
```

### Thousands of Learners

The current structure has no learner data model. Thousands of learners require a database-backed model, not Markdown or Notion as the source of truth.

Required objects:

- learner
- enrollment
- progress event
- completion
- journal entry
- workbook submission
- preference
- consent record

### Multilingual Content

The current structure has no translation system. Translation cannot be handled as duplicated files without IDs and source mapping.

Required objects:

- source artifact
- locale
- translation status
- translator or reviewer
- source version
- translated version
- localization notes

### AI Tutors

AI tutors require strict retrieval boundaries. They should not retrieve private Alpha Proxima material or unrestricted learner data.

Required controls:

- tutor persona definition
- allowed knowledge sources
- blocked knowledge sources
- learner memory permissions
- escalation rules
- answer citation rules
- safety review logs

## Engineering Risk Report

| Risk | Severity | Explanation | Mitigation |
|------|----------|-------------|------------|
| Missing Reference Blueprint | Critical | The claimed source architecture is not locally auditable | Add blueprint as a canonical OSG artifact |
| Missing stable IDs | Critical | APIs, graph, database, translations, and retrieval cannot scale without IDs | Define ID standard before course production |
| Notion overreach | High | Notion is useful for operations but weak as production backend | Use Notion for workflow, database for learner/product state |
| Mega-document risk | High | Large blueprints become unmaintainable and poor AI retrieval units | Enforce [[11 - One Question Document Standard]] |
| Translation drift | High | Multilingual variants can diverge from source content | Add translation registry and source version locks |
| AI memory leakage | High | YUNA or tutors could cross boundaries between OSG and Alpha Proxima | Define retrieval scopes and memory policy |
| Progress tracking ambiguity | High | Completion and learning signals need precise event types | Create progress event schema |
| Media duplication | Medium | Course, content, and app media can fork without registry | Add media asset registry |
| Community data complexity | Medium | Community IDs, permissions, and moderation are absent | Add community model before community launch |
| API rework | Medium | Without entities and IDs, APIs will be rewritten later | Define domain model before app development |

## Repository Recommendations

Recommended OSG Academy repository structure:

```text
osg-academy/
  apps/
    web/
    mobile/
    admin/
  packages/
    domain/
    ui/
    api-client/
  content/
    courses/
    knowledge-library/
    translations/
  media/
    registry/
    source/
    exports/
  data/
    schemas/
    seeds/
  services/
    api/
    ai-tutor/
    retrieval/
  automation/
    stripe/
    email/
    calendly/
    content-publishing/
  docs/
    architecture/
    decisions/
    standards/
    runbooks/
```

Do not create this full structure immediately. Use it as the target architecture once the Reference Blueprint, ID standards, and database model exist.

## Knowledge Graph Compatibility

Current compatibility: partial.

Needed graph node types:

- Course
- Module
- Lesson
- Workbook
- Workbook Exercise
- Journal
- Journal Prompt
- Media Asset
- Translation
- Learner Concept
- Practice
- Assessment
- Community
- AI Tutor
- Knowledge Library Entry
- Living Genome Node

Needed relationship types:

- PART_OF
- PRECEDES
- REQUIRES
- TEACHES
- PRACTICES
- REFLECTS_ON
- TRANSLATES
- HAS_MEDIA
- ASSESSES
- COMPLETED_BY
- RECOMMENDED_BY
- RETRIEVED_BY
- RELATED_TO

Minimum requirement: every graph node must have a stable ID, title, type, version, status, source document, and `core_question` when document-backed.

## Database Compatibility

Current compatibility: not production-ready.

Required tables or collections:

- courses
- modules
- lessons
- workbooks
- workbook_exercises
- journals
- journal_prompts
- media_assets
- translations
- learners
- enrollments
- progress_events
- assessments
- community_spaces
- community_memberships
- knowledge_entries
- ai_tutor_sessions
- retrieval_events

Required cross-cutting fields:

- id
- slug
- title
- status
- version
- locale
- source_id
- created_at
- updated_at
- owner
- visibility
- access_level

## API Readiness

Current readiness: low.

APIs cannot be designed cleanly until the entity model and ID standards exist.

Future API groups:

- Catalog API
- Course API
- Lesson API
- Media API
- Translation API
- Learner API
- Progress API
- Journal API
- Workbook API
- Community API
- AI Tutor API
- Knowledge Library API
- Retrieval API

Minimum endpoint pattern:

```text
GET /courses
GET /courses/{course_id}
GET /courses/{course_id}/modules
GET /lessons/{lesson_id}
POST /learners/{learner_id}/progress-events
GET /knowledge/{knowledge_id}
POST /ai-tutor/sessions
```

## Future AI Readiness

Current readiness: partial.

The current OSG foundation has clean folders and launch discipline, but AI retrieval requires smaller modular documents, stable IDs, source boundaries, and metadata.

Required for AI readiness:

- one document, one question
- stable knowledge IDs
- document type metadata
- source version
- language metadata
- audience metadata
- retrieval permissions
- citation source links
- learner data access policy
- separation between OSG public knowledge and Alpha Proxima private institutional memory

## One Document, One Question Rule

This review adopts [[11 - One Question Document Standard]] as mandatory for OSG Academy and Alpha Proxima artifacts.

Examples:

| Artifact | Core Question |
|----------|---------------|
| OLS | How are OSG courses designed? |
| Reference Blueprint | How is Awaken the Inner Guru structured? |
| Workbook Blueprint | How is the workbook organized? |
| Journal Blueprint | How is reflection organized? |

This rule is not cosmetic. It is required for modularity, search, versioning, graph extraction, API mapping, AI retrieval, and long-term maintainability.

## Overall Engineering Score

**58 / 100**

### Score Breakdown

| Area | Score | Reason |
|------|-------|--------|
| Launch foundation | 78 | Good operational base exists |
| Academy architecture | 45 | Domain model is missing |
| Scalability | 48 | No ID, translation, learner, or progress model yet |
| Database readiness | 35 | No production schema |
| API readiness | 35 | Entities and IDs are undefined |
| Knowledge graph readiness | 52 | Alpha Proxima graph tooling exists, but OSG taxonomy is missing |
| AI readiness | 50 | Retrieval boundaries and tutor model are missing |
| Repository discipline | 70 | Basic GitHub practices exist |
| Documentation modularity | 62 | Good launch docs, but academy blueprint source is absent |

## Immediate Engineering Priorities

1. Add the Claude Reference Blueprint as a canonical OSG artifact.
2. Apply `core_question` to the Reference Blueprint and split it if it answers more than one question.
3. Create the OSG Academy ID Standard.
4. Create the OSG Academy Domain Model.
5. Create database schema draft v0.1.
6. Create Knowledge Graph taxonomy for OSG Academy.
7. Create AI tutor retrieval boundary standard.
8. Create templates for lesson, workbook, journal, media, translation, and progress events.

## Implementation Notes

This report audits engineering readiness only. It does not judge course philosophy, pedagogy, brand positioning, or institutional meaning.

## Future Improvements

- [ ] Rerun this audit after the Reference Blueprint is added.
- [ ] Generate ID standards and database schema.
- [ ] Add OSG Academy graph registry generator.
- [ ] Add OSG Academy document validator.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-05 | CODEX | Initial OSG Academy engineering review |

