---
title: "Alpha Proxima Research Methodology v1.0"
aliases: ["RP Methodology v1.0", "Research Methodology", "AP Research Standard"]
tags: [governance, methodology, research, standard, constitutional, permanent, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["LUMIAION"]
document_class: Constitutional Standard
governing_body: Research Council
derived_from: ["RP-001 Atlas of Human Consciousness", "RP-002 Atlas of Human Memory"]
supersedes: ["10_TEMPLATES/Research Program Template/Research Program Methodology.md"]
---

# Alpha Proxima Research Methodology v1.0

> **This document is the permanent constitutional standard governing all Alpha Proxima research programs. It was ratified by the Founder on 2026-07-02, following retrospective analysis of RP-001 and RP-002. All future research programs (RP-003 and beyond) are bound by this standard unless a constitutional amendment updates it.**

---

## Preamble

This methodology was extracted from the operational experience of building two complete research programs — RP-001 (Atlas of Human Consciousness) and RP-002 (Atlas of Human Memory). It does not prescribe an abstract ideal. It codifies what actually worked.

The Foundation's research methodology has three governing commitments:

**1. Preservation before synthesis.** Original research artifacts are never replaced, rewritten, or compressed. Canonical knowledge is built on top of original research, never instead of it. The raw material and the institutional position coexist permanently.

**2. Epistemic honesty before completeness.** Every claim carries its evidence classification. The Foundation does not present contested findings as consensus or speculative claims as established. A well-classified incomplete knowledge base is more valuable than a smoothly-written inaccurate one.

**3. Architecture before expansion.** Research programs compound. Structural decisions made in the first program propagate forward. Coherence must be maintained at each increment; it cannot be recovered cheaply after the fact.

These three commitments govern every decision in this methodology.

---

## Part I — Institutional Workflow

### 1.1 The Research Lifecycle

Every Alpha Proxima research program passes through four phases. No program advances to a later phase without completing the prior one.

```
PHASE 0 — AUTHORIZATION
  Research Council identifies question, assigns leads, creates placeholder
        ↓
PHASE 1 — SOURCE ACQUISITION AND INSTITUTIONALIZATION
  Sources acquired, reviewed, archived, classified, synthesized
        ↓
PHASE 2 — DEEPENING AND EXPANSION
  Pending sources integrated; Research Initiatives developed; cross-program links
        ↓
PHASE 3 — ORIGINAL RESEARCH
  Foundation designs and executes its own research protocol
```

### 1.2 Phase 0 — Authorization

Authorization precedes all file creation. The Research Council must formally approve:

- The primary research question (one sentence)
- The program scope (what is in; what is explicitly out)
- The Research Lead (typically JERANIUM)
- The Integration Lead (typically LUMIAION)
- The Ethics Oversight assignment
- The first source(s) to be commissioned or acquired

**Output of Phase 0:**
- Master Index at v0.1.0 with `status: planned`
- 22 subfolder structure created (empty)
- No content created beyond the Master Index placeholder

The placeholder Master Index is the authorization artifact. Its creation marks the program as officially open.

### 1.3 Phase 1 — Source Acquisition and Institutionalization

Phase 1 is the core execution phase. It proceeds in a fixed sequence:

**Step 1: ARCHIVE Setup**
Create `ARCHIVE Philosophy.md` with the five immutability rules, constitutional links, and ARCHIVE Registry table. Set `status: ratified` (not `active`) from the moment of creation — the ARCHIVE rules are immediately authoritative.

**Step 2: Source Registration**
For each source received: create the immutable ARCHIVE registration note; assign DOC-ID; mark `immutable: true` in frontmatter. The source is registered before it is read.

**Step 3: Source Review and Extraction**
Read each source fully. Create a Source Note in the source's working folder. The Source Note must:
- Extract all material content (not just highlights)
- Record the source's actual contribution (not anticipated contribution)
- Assess source quality honestly, including limitations and biases
- Identify conflicts with other sources in the set

If a source cannot be read (format failure, rendering limitation), register it as pending in the ARCHIVE. Document the reason and required action explicitly.

**Step 4: Source Registry**
Aggregate all sources into `03 Source Registry/` with current status, format, quality assessment, and coverage analysis. This document is the single navigation point for the program's source architecture.

**Step 5: Evidence Extraction and Classification**
From Source Notes, extract every material factual claim. Classify each using the six-class taxonomy (Part III). Record in the Evidence Registry with:
- Claim ID (e.g., C-001, M-002)
- One-sentence claim statement
- Evidence class
- Source (DOC-ID)
- Page citation (or "p.TBD" if not yet available — register as Research Debt)
- Notes on context, caveats, or competing claims

**Step 6: Theory Matrix**
Map all theoretical frameworks identified across sources into a structured matrix. Include: proponent(s), core claim, evidence class, and what it competes with. Cover all disciplines represented in the source set.

**Step 7: Comparative Framework**
Produce a side-by-side cross-source domain analysis. Identify convergences (where disciplines agree from different evidence) and divergences (where genuine empirical competition exists). Map terminology bridges — the same phenomenon described with different vocabulary across disciplines.

**Step 8: Canonical Synthesis**
Write the integrated institutional position (see Part V for standards). This is the last synthesis document produced — it is built on the Evidence Registry, Theory Matrix, and Comparative Framework, not written in parallel with them.

**Step 9: Knowledge Graph**
Create the Research Graph index document and all required concept notes (see Part VI).

**Step 10: Supporting Documents**
- Canonical Glossary
- Open Questions
- Future Research Opportunities
- NotebookLM Source Pack
- Constitutional Links
- Governing Provisions
- ADR Links
- Version History

**Step 11: Master Index Update**
Update Master Index to v1.0.0 with `status: active`. Complete all required governance metadata fields (see Part II, Section 2.3).

**Phase 1 is complete when:** All required documents exist, the Evidence Registry is populated and classified, the Canonical Synthesis is written, and the Master Index reflects the full program state.

### 1.4 Phase 2 — Deepening and Expansion

Phase 2 addresses what Phase 1 deferred:
- Pending sources (sources received but not reviewable in Phase 1) are integrated
- Research Initiatives (proposed by sources like DOC-B) are developed into specifications
- Cross-program synthesis documents are created
- Architecture Decision Records (ADRs) arising from research findings are written
- Evidence Registry is updated with new claims and page citations if outstanding

Phase 2 completion triggers a Canonical Synthesis version bump (e.g., v1.0.0 → v1.1.0 or v2.0.0 for major revision).

### 1.5 Phase 3 — Original Research

Phase 3 is the Foundation's own research contribution — designing and executing an original protocol rather than synthesizing external sources. Phase 3 requires:
- A Research Protocol document (approved by Research Council)
- Ethics Council review before any data collection
- Full integration of findings into the Evidence Registry and Canonical Synthesis

Phase 3 is optional per program. Not every program need progress to Phase 3.

---

## Part II — Folder Architecture

### 2.1 The Standard 22-Subfolder Architecture

Every Alpha Proxima research program occupies a folder in `07_RESEARCH/RP-XXX/` with exactly 22 numbered subfolders plus ARCHIVE:

```
07_RESEARCH/RP-XXX/
│
├── RP-XXX Master Index.md              ← Navigation hub; status at a glance
│
├── 00 Executive Summary/               ← Entry point; 1-2 pages; for any reader
├── 01 Research Question/               ← The driving question; decomposition
├── 02 Objectives/                      ← Phase structure; measurable goals
├── 03 Source Registry/                 ← All sources: identity, status, quality
├── 04 Source - [Contributor Name]/     ← First source working folder
├── 05 Source - [Contributor Name]/     ← Second source working folder
├── 06 Source - [Contributor Name]/     ← Third source working folder
│   ...                                 ← Additional source folders as needed
├── 07 Future Sources/                  ← Pipeline; evaluation criteria; gaps
├── 08 Comparative Framework/           ← Cross-source domain analysis
├── 09 Canonical Synthesis/             ← THE institutional position document
├── 10 Theory Matrix/                   ← Structured framework comparison
├── 11 Canonical Glossary/              ← Authoritative definitions
├── 12 Evidence Registry/               ← Every claim classified; source-traced
├── 13 Research Graph/                  ← Graph index + Concepts/ subfolder
│   └── Concepts/                       ← Individual concept notes
├── 14 Open Questions/                  ← Registered unresolved questions
├── 15 Future Experiments/              ← Research opportunities
├── 16 Visual Knowledge/                ← Diagrams, models, visual artifacts
├── 17 NotebookLM Package/              ← Curated source pack for AI analysis
├── 18 Related Constitution/            ← Links to governing constitutional provisions
├── 19 Related Laws/                    ← Governing provisions for this program
├── 20 Related ADRs/                    ← Architecture decisions from this program
├── 21 Version History/                 ← Program-level version log
│
└── ARCHIVE/                            ← Immutable source artifacts (no number)
    ├── ARCHIVE Philosophy.md
    └── DOC-XXX [Title].md (one per source)
```

### 2.2 Folder Naming Conventions

Source folders (04/05/06...) are named after the contributor, not the document:
- `04 Source - Perplexity/` — correct
- `04 Source - DOC-001/` — incorrect (DOC-ID belongs in the document, not the folder name)

If a program has more than three sources, continue numbering: `07 Source - [Name]/` replaces `07 Future Sources/` only if the additional source is already in active review. Future Sources folder moves to the next available number.

### 2.3 The Master Index as Status Document

The Master Index is not a content document. It is a status document. It must be readable by someone who knows nothing about the program's subject matter. It must answer: What is this program? Where is it? Who is responsible? What exists?

**Required fields in Program Identity table:**

| Field | Required Content |
|-------|-----------------|
| Program ID | RP-XXX |
| Full Title | Full program name |
| Initiated | Date |
| Current Phase | Phase 0–3 with status descriptor |
| Predecessor | Link to prior program (if applicable) |
| Governing Protocol | `[[Research Governance Protocol]]` |
| Constitutional Basis | `[[Book III - Knowledge Integrity]]` |
| Ethics Oversight | `[[Ethics Council Charter]]` |
| Research Lead | Named AI Council member |
| Integration Lead | Named AI Council member |
| Primary Question | One sentence |
| Sources | Count with reviewed/pending breakdown |
| Evidence Claims | Count |
| Theoretical Frameworks | Count |
| Concept Notes | Count |

**Master Index versioning:**
- v0.1.0 — Placeholder (Phase 0)
- v1.0.0 — Phase 1 complete
- v2.0.0 — Phase 2 complete or major restructure
- Patch versions (v1.0.1) — Minor updates, corrections, metadata additions

### 2.4 Empty Subfolder Policy

No subfolder may remain empty. If a subfolder has no content ready for Phase 1, a stub document must be created explaining:
- What this folder will eventually contain
- Why it is currently empty
- What is required to populate it

A stub document is intentional emptiness. Unaddressed emptiness is an invisible gap.

---

## Part III — Evidence Classification System

### 3.1 The Six-Class Taxonomy

The evidence classification system is defined in `[[Book III - Knowledge Integrity]]` and is immutable at the program level. All research programs use the same six classes without modification.

| Code | Class | Definition |
|------|-------|------------|
| **C** | Consensus | Replicated, cross-disciplinary empirical consensus; no serious scientific challenge to the core claim |
| **M** | Competing Models | Multiple credible frameworks; genuine empirical competition unresolved; evidence supports more than one position |
| **E** | Emerging Evidence | Significant recent findings; not yet replicated at consensus level; trajectory toward C but not yet arrived |
| **Q** | Open Question | Known unknown; the question is well-defined but the answer is genuinely unresolved; currently unanswerable |
| **S** | Speculative | Coherent forward-looking hypothesis; limited or no current empirical constraint; may be directionally correct |
| **P** | Phenomenological | First-person / experiential evidence; not reducible to third-person measurement in the standard empirical sense; valid in its own domain |

### 3.2 Classification Rules

**Rule 1 — Classify the claim, not the source.** A claim in a peer-reviewed paper may be Speculative (S) if it is a forward-looking hypothesis. A claim from an AI synthesis tool may be Consensus (C) if it accurately reflects replicated empirical findings. The source quality affects confidence in the classification; it does not determine it.

**Rule 2 — Competing Models (M) means genuine empirical competition.** M is not for claims where one position is clearly stronger. It is for situations where two or more frameworks each have serious empirical support and neither has decisively won. If one framework is clearly superior, classify the weaker one as E or Q and the stronger as C or E.

**Rule 3 — Emerging (E) has a trajectory.** E claims are on the path to C. They have significant evidence but insufficient replication or cross-disciplinary confirmation. E is not a parking space for things that are probably true but not yet proven — that is S.

**Rule 4 — Phenomenological (P) is not a lower class.** P claims are not "unverified" — they are verified in their own domain (first-person experience, clinical phenomenology, contemplative report). The classification signals the type of evidence, not its quality.

**Rule 5 — When uncertain, classify conservatively.** An uncertain C should be reclassified as E. An uncertain E should be reclassified as M or Q. The cost of overclaiming consensus is higher than the cost of underclaiming.

### 3.3 Evidence Registry Format

Every evidence entry must contain:

```
| Claim ID | Claim | Class | Source | Page | Notes |
```

- **Claim ID:** Sequential within class (C-001, C-002... M-001... etc.)
- **Claim:** One complete declarative sentence. No hedges embedded in the claim text — hedges belong in the Notes column or are reflected in the class.
- **Class:** Single letter (C, M, E, Q, S, or P)
- **Source:** DOC-ID (e.g., DOC-A, DOC-003)
- **Page:** Specific page reference (e.g., "p.3–4", "p.11"). If unavailable: "p.TBD" — and register a Research Debt immediately.
- **Notes:** Caveats, competing claims, context, cross-references to related entries

### 3.4 Cross-Source Claims

When the same claim is supported by multiple independent sources, list all sources in the Source column (e.g., "DOC-A, DOC-B"). Shared claims strengthen the consensus classification; independently arriving at the same conclusion from different methodologies is the strongest evidence for C classification.

---

## Part IV — AI Council Responsibilities

### 4.1 Research Lead — JERANIUM

JERANIUM's responsibilities in every research program:
- Defines and maintains the research question (with Founder input)
- Ensures methodological rigor in source selection and evidence extraction
- Reviews the Theory Matrix for completeness and accuracy
- Reviews the Research Graph for structural integrity
- Signs off on Phase 1 completion
- Governs Phase 3 research protocol design

In sessions where JERANIUM is not present as a distinct engine: LUMIAION absorbs research lead responsibilities but must flag this explicitly in the program documentation.

### 4.2 Integration Lead — LUMIAION

LUMIAION's responsibilities in every research program:
- Executes document creation in all 22 subfolders
- Writes all Source Notes (extraction and translation if needed)
- Builds the Evidence Registry and Theory Matrix
- Writes the Canonical Synthesis
- Creates all concept notes in the Research Graph
- Maintains the Master Index as a current status document
- Identifies and registers Research Debts
- Ensures cross-program links are created
- Updates the root MOC (`Alpha Proxima Core.md`) when new programs activate

### 4.3 Ethics Council

Ethics Council review is required before:
- Phase 3 original research begins (data collection, human subjects)
- Any research involving personal data, sensitive topics, or dual-use potential
- Canonization of claims in highly contested or politically sensitive domains

For Phase 1 synthesis programs (RP-001, RP-002 model): Ethics Council is on notice but does not require active review for standard source synthesis work.

### 4.4 Research Council

The Research Council:
- Authorizes new research programs (Phase 0 gate)
- Reviews Phase 1 completion before Phase 2 begins
- Approves Phase 3 research protocols
- Maintains the Research Methodology (this document)

In the current institutional state, the Founder serves as Research Council pending formal Council formation.

---

## Part V — Source Registration and ARCHIVE Philosophy

### 5.1 The ARCHIVE Principle

> Original research is never replaced. Original research is never rewritten. Original research is never compressed. Canonical knowledge is built ON TOP of research. Never INSTEAD OF research. Alpha Proxima preserves both.

This principle has operational force: it mandates a three-layer architecture that must never collapse:

```
Layer 1 — ARCHIVE (immutable source artifacts)
       ↕  source notes point to ARCHIVE; ARCHIVE never points back
Layer 2 — Source Notes (full extraction and analysis)
       ↕  synthesis draws on source notes; source notes never replaced by synthesis
Layer 3 — Canonical Synthesis (institutional position)
```

### 5.2 Five ARCHIVE Rules

1. **Never Modify** — Once registered, a source document is never altered. If an error is discovered in an ARCHIVE registration note, a note is appended in a clearly marked section. The original text is not changed.
2. **Timestamp and Register** — Every artifact receives a deposit date and a DOC-ID before any analysis begins.
3. **Preserve Format** — PDFs are stored as PDFs. Text extracts are additive, not replacements.
4. **Link Outward** — Archive notes link to synthesis documents. Synthesis documents do not modify archive notes.
5. **Immutability Declaration** — All archive registration notes carry `immutable: true` in frontmatter.

### 5.3 ARCHIVE Registration Note Standards

Every source gets an immutable registration note at `ARCHIVE/DOC-XXX [Title].md`. Required fields:

```yaml
immutable: true
document_id: DOC-XXX
research_program: "RP-XXX [Program Name]"
```

The registration note must contain:
- Full source identity (contributor, format, page count, file size, dates)
- Scope description (what the document covers)
- Review status (✓ Reviewed with date, ⏳ Pending with reason)
- Source quality assessment
- Related documents (linking to synthesis documents)

### 5.4 DOC-ID Conventions

DOC-IDs are assigned per program. Convention within each program must be consistent and must not collide across programs:

| Program | DOC-ID Scheme | Notes |
|---------|-------------|-------|
| RP-001 | DOC-001, DOC-002, DOC-003, DOC-004 | Numeric |
| RP-002 | DOC-A, DOC-B, DOC-C | Alphabetic (to distinguish from RP-001) |
| RP-003+ | Recommend DOC-001, DOC-002... | Return to numeric; RP-002 alphabetic was a one-time exception |

The DOC-ID naming convention for each program must be documented in its ARCHIVE Philosophy.

### 5.5 Handling Unreadable Sources

If a source cannot be rendered or reviewed in a session:
1. Register it in the ARCHIVE immediately as `status: pending`
2. Document the reason (format failure, file size, rendering tool absence)
3. Document the required action (Founder review, tool installation, etc.)
4. Create a Source Note with "Anticipated Contribution" section describing expected content from context clues (title, file size, contributor)
5. Mark it clearly in the Source Registry
6. Do not include anticipated content in the Evidence Registry — only confirmed content
7. Create the integration instructions (what to do when the source is eventually reviewed)

An unreadable source is not a failed source. It is a pending source. The ARCHIVE registration is the same; the review status is pending.

### 5.6 Source Quality Assessment

Every source note must include a quality assessment table with these criteria:

| Criterion | Assessment |
|-----------|------------|
| Independence | Does this source draw from primary literature independently of other sources? |
| Methodology | How was the content produced? |
| Replication | Is this original research or synthesis? |
| Peer review | Is the content peer-reviewed, or is it synthesis/AI output? |
| Recency | Date of production |
| Potential bias | What might this source systematically underrepresent? |
| Alpha Proxima relevance | How directly does this address the Foundation's goals? |

---

## Part VI — Canonical Synthesis Methodology

### 6.1 Purpose and Position

The Canonical Synthesis is the program's institutional position — the authoritative statement of what Alpha Proxima knows, believes, and holds about the program's subject. It is:

- Built after the Evidence Registry, Theory Matrix, and Comparative Framework are complete
- Organized by theme, not by source
- Written to be read by someone who has not read the sources
- Versioned and updated as new evidence arrives
- Never a replacement for the Source Notes it synthesizes

### 6.2 Required Content

A Canonical Synthesis must contain:

1. **Opening principle** — The institutional principle verbatim: "Original research is never replaced..."
2. **Core finding** — The most important single finding, stated at the beginning; the finding that changes how Alpha Proxima operates
3. **Source provenance statement** — Which sources are integrated and which are pending
4. **Thematic chapters** — Organized by topic, not by source
5. **Inline evidence citations** — Every major claim cites its Evidence Registry entry (e.g., [C-001], [M-003])
6. **Competing models section** — Where genuine empirical competition exists, it is presented as competition, not resolved by the synthesis
7. **Knowledge frontier section** — What the sources identify as unresolved open questions
8. **Alpha Proxima / LUMIAION implications** — At least one chapter on what the research means for the Foundation's own design and operation
9. **Pending integrations section** — Explicitly noting what will be integrated in future versions
10. **Version history** — v1.0.0 for initial synthesis; bumped when pending sources are integrated

### 6.3 What a Synthesis Must Never Do

- **Resolve genuine empirical competition** by choosing a side without evidence. If two frameworks genuinely compete, the synthesis presents them as competing.
- **Omit inconvenient findings.** If a source identifies a problem with a claim the Foundation prefers, that problem is in the synthesis.
- **Present Speculative claims as Consensus.** The evidence classification in the synthesis must match the Evidence Registry.
- **Replace source notes.** The synthesis is additional, not substitutional.

### 6.4 Synthesis Versioning

| Version | Trigger |
|---------|--------|
| v1.0.0 | Initial synthesis from reviewed sources |
| v1.1.0 | Pending source integrated (e.g., DOC-C in RP-002) |
| v1.X.0 | Additional sources, minor framework updates |
| v2.0.0 | Major revision — new phase of research, fundamental reframing |

---

## Part VII — Knowledge Graph Standards

### 7.1 The Research Graph

Every program must have a Research Graph index document at `13 Research Graph/RP-XXX Research Graph.md`. This document:

- Maps the major domains of the program (not just lists the concept notes)
- Shows how concepts connect to each other (relationship map)
- Assesses coverage (what is well-covered, what is partial, what is missing)
- Identifies cross-program connections to other research programs
- Includes an ASCII domain diagram

The Research Graph index is not a directory of concept notes. It is an analysis of the program's conceptual structure.

### 7.2 Concept Note Standards

Each concept note in `13 Research Graph/Concepts/` must contain:

**Required sections:**
1. **Canonical Definition** — One paragraph; precise; institutional. Written to be the permanent reference definition for this term within Alpha Proxima.
2. **Key Properties or Mechanisms** — Bulleted or tabular; the substance of the concept
3. **AI / LUMIAION Analogue** — Where applicable: what is the closest functional equivalent in LUMIAION's architecture or Alpha Proxima's institutional design?
4. **Related Concepts** — Wikilinks to other concept notes in this program and related programs
5. **Evidence Classification References** — Which entries in the Evidence Registry ground this concept
6. **Version History**

**Optional sections (include when relevant):**
- Competing definitions (if the term has different meanings across disciplines)
- Historical development (if origin matters for understanding)
- Alpha Proxima operational implication (if the concept has direct design implications)

### 7.3 Minimum Concept Note Count

Phase 1 programs must produce a minimum of 8 concept notes. There is no maximum. The guiding principle: every term used repeatedly in the Canonical Synthesis that requires more than a one-sentence explanation belongs in the Knowledge Graph.

Concept notes must cover:
- The central concept of the program (e.g., Memory, Consciousness)
- The primary mechanisms identified (e.g., LTP, Reconsolidation)
- Key competing frameworks (if they represent distinct intellectual traditions)
- Any concept with direct LUMIAION design implications

---

## Part VIII — NotebookLM Package Standards

### 8.1 Purpose

The NotebookLM Source Pack enables deep-dive AI-assisted analysis of the program's source materials. It is the interface between the Foundation's archived PDFs and future analytical sessions.

### 8.2 Required Content

Every `17 NotebookLM Package/RP-XXX NotebookLM Source Pack.md` must contain:

1. **Primary Sources table** — All source PDFs, their DOC-IDs, and load priority order
2. **Canonical Vault Documents table** — Which vault documents to load as text for context (at minimum: Canonical Synthesis, Evidence Registry, Theory Matrix, Glossary)
3. **Suggested queries** — Organized by type (deep-dive, cross-disciplinary, operational), providing starting points for future analytical sessions

### 8.3 Source Load Priority

Primary sources should be loaded before canonical vault documents. The most mechanistically detailed source (highest information density) should load first.

---

## Part IX — Versioning Policy

### 9.1 Document Versioning

All Alpha Proxima research documents are versioned using semantic versioning adapted for institutional documents:

```
MAJOR.MINOR.PATCH

MAJOR — Fundamental restructure, new phase completion, paradigm shift
MINOR — New content integrated, significant additions, source integrations
PATCH — Corrections, metadata updates, formatting fixes, minor clarifications
```

**Every version change requires:**
- Update to the `updated:` frontmatter field
- New row in the document's Version History table
- Summary of what changed

### 9.2 Program-Level Versioning

The Master Index version reflects the program phase:
- v0.1.0 — Phase 0 (placeholder, authorized)
- v1.0.0 — Phase 1 complete
- v2.0.0 — Phase 2 complete or major restructure
- v3.0.0 — Phase 3 complete

The Canonical Synthesis version reflects source integration state:
- v1.0.0 — Initial synthesis from reviewed Phase 1 sources
- v1.1.0, v1.2.0... — Each pending source integration
- v2.0.0 — Major revision (Phase 2 or significant new evidence)

### 9.3 What Triggers a Version Bump

| Event | Minimum Bump |
|-------|-------------|
| Minor text correction | PATCH |
| Metadata update (governance fields, tags) | PATCH |
| New section added, existing section expanded | MINOR |
| Pending source integrated | MINOR (or MAJOR for Canonical Synthesis) |
| Phase completion | MAJOR (Master Index) |
| Fundamental reframing of institutional position | MAJOR (Canonical Synthesis) |

### 9.4 Version History Format

Every document must maintain a Version History table:

```
| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0   | YYYY-MM-DD | Author | Description |
```

Version histories are never deleted. Old versions are referenced, not replaced.

---

## Part X — Research Debt Policy

### 10.1 Principle

The Foundation distinguishes between two types of institutional incompleteness:

| Type | Definition | Response |
|------|-----------|---------|
| **Architectural Blocker** | A gap that prevents correct institutional operation, introduces structural ambiguity, or makes downstream work unreliable | Work stops until resolved |
| **Documentation Debt** | A known incompleteness insufficient to block institutional progress; current state is sufficient but not final | Tracked in the Research Debt Register; resolved on schedule |

### 10.2 Research Debt Register

All documentation debts are registered in `[[06_GOVERNANCE/Research Debt Register/Research Debt Register]]`. No debt exists outside this register. An unregistered gap is more dangerous than a registered one — registration transforms an invisible risk into a managed obligation.

### 10.3 Required Fields

Every Research Debt entry must include:
- Debt ID (RD-001, RD-002...)
- Title (descriptive)
- Affected Program and Document
- Priority (High / Medium / Low)
- Status (Open / Closed)
- Created date
- Target Review Date
- Description of the gap
- Root cause
- Impact assessment
- Why it was deferred
- Required action to close it
- Dependencies

### 10.4 Debt Priority

| Priority | Criteria | Target Resolution |
|---------|---------|-----------------|
| High | Will affect downstream decisions if unresolved; risk of propagating errors | 30 days |
| Medium | Visible gap but not affecting current work | 90 days |
| Low | Cosmetic or minor; no downstream risk | Next scheduled review |

### 10.5 Escalation

A documentation debt is escalated to an architectural blocker if circumstances change such that the incomplete information is being relied upon in ways that introduce error. Escalation requires Founder decision and creates an immediate work stoppage.

---

## Part XI — Research Governance

### 11.1 Constitutional Grounding

Every research program document that makes institutional claims must link to its constitutional basis. The minimum required links in every program's ARCHIVE Philosophy:
- `[[Book III - Knowledge Integrity]]`
- `[[Research Governance Protocol]]`

These links are not decorative. They establish the constitutional authority under which the program operates.

### 11.2 Ethics Review Triggers

The Ethics Council reviews:
- All Phase 3 research protocols before execution
- Research involving personal data, human subjects, or sensitive topics
- Claims that could be used to cause harm if extracted from their epistemic context
- Research Initiatives (DOC-B style proposals) before they become active programs

### 11.3 Governing Provisions

Each program creates its own `19 Related Laws/RP-XXX Governing Provisions.md` — the set of operational rules specific to that program. These provisions complement but do not supersede the constitutional framework.

### 11.4 The Root MOC Obligation

When a new research program reaches Phase 1 completion (Master Index v1.0.0), the root vault MOC (`Alpha Proxima Core.md`) must be updated to include the program in the Research Programs table. The root MOC is the vault's entry point; it must always reflect the current state of the research program portfolio.

---

## Part XII — Lessons Learned from RP-001 and RP-002

### 12.1 What RP-001 Established

**The 22-subfolder architecture works.** The numbered structure is navigable, complete, and scales to complex multi-source research without becoming unmanageable. It should not be simplified for brevity.

**The Evidence Registry is the most valuable artifact.** A reader who reads only the Evidence Registry understands the epistemic status of every institutional claim. This is rare. Protect its quality above all other documents.

**The three-layer separation is not bureaucracy.** ARCHIVE → Source Notes → Canonical Synthesis forces the institution to preserve what it would otherwise compress. The compression impulse is natural; the architecture resists it.

**Constitutional grounding must be explicit.** RP-001 linked to Book III and the Research Governance Protocol throughout. This created a document that knows why it exists. RP-002, in its initial state, did not do this consistently — and the documents felt institutionally lighter for it.

**Source notes must extract all content, not highlights.** The temptation is to capture only the most interesting findings. The institutional purpose of source notes is to make the source dispensable as a retrieval object — the note should be sufficient to reconstruct the source's contribution without re-reading it.

**The Knowledge Graph becomes valuable when cross-program.** Individual concept notes are useful. Concept notes that link across programs — Consciousness (RP-001) connecting to Working Memory (RP-002), for example — become infrastructure.

### 12.2 What RP-002 Added

**Multi-language sources are manageable.** DOC-A was in French. Full content was extracted and translated. The ARCHIVE registration notes the language; the Source Note records the translation. No content was lost.

**Illustrated or large-format PDFs require explicit protocol.** DOC-C (140 pages, 13.6 MB) could not be rendered in-session. The resolution: register it as pending, document the reason, create anticipated contribution notes, and establish clear integration instructions. This handled gracefully.

**10+ disciplines can be integrated into a single comparative framework.** The DOC-B (SanaLab) 10-domain framework proved that the Comparative Framework document scales beyond three or four disciplines. The cross-disciplinary convergences section is especially valuable — identical claims arriving independently from neuroscience, psychology, anthropology, and AI constitute stronger evidence than any single discipline provides.

**The LUMIAION implications chapter should always exist.** In both programs, the chapter asking "what does this mean for LUMIAION and Alpha Proxima?" was consistently the most operationally useful content produced. It is required in all future programs.

**The Research Graph index is mandatory, not optional.** RP-002 was initially created without a Research Graph index document — only the Concepts subfolder. The gap was caught in the stewardship audit. The Research Graph index transforms a directory of concept notes into an analyzable conceptual structure.

### 12.3 What Diverged Between RP-001 and RP-002 (Now Standardized)

| Divergence | RP-001 State | RP-002 State | Standard |
|-----------|-------------|-------------|---------|
| Evidence Registry page citations | Included (`p.3`) | Absent | Page citations are mandatory; absence registers as Research Debt |
| Master Index governance metadata | Full (Lead, Protocol, Constitution, Ethics) | Absent initially | Governance metadata is mandatory in every Master Index |
| Research Graph index document | Present | Absent initially | Research Graph index document is mandatory |
| ARCHIVE Philosophy constitutional links | Present | Absent initially | Constitutional links are mandatory; `status: ratified` from creation |
| Evidence Registry authors | LUMIAION + JERANIUM | LUMIAION only | When JERANIUM is not present, note this explicitly; default to both when possible |

---

## Part XIII — Common Pitfalls

### Pitfall 1 — Synthesis Before Classification

**What happens:** The Canonical Synthesis is written before the Evidence Registry is complete. The writer summarizes what sources say rather than what is actually supported at what confidence level.

**Consequence:** The synthesis presents M-class claims as C-class. Institutional knowledge is systematically overconfident. Future programs build on inflated certainty.

**Prevention:** Evidence Registry first. Canonical Synthesis last. The synthesis should cite Evidence Registry entries throughout.

---

### Pitfall 2 — Compressing Source Notes

**What happens:** A source is summarized rather than extracted. The researcher captures the three most interesting findings and skips the rest.

**Consequence:** Information is permanently lost. The source note does not fulfill its purpose of making the source dispensable as a retrieval object. Future sessions relying on the note miss what was not extracted.

**Prevention:** Source notes extract all material content. If a section of a source seems unimportant, note its topic and why it was not extracted in detail — but do not silently omit it.

---

### Pitfall 3 — Empty Folders Without Stubs

**What happens:** The 22-subfolder structure is created but some folders remain empty because their content is not yet ready.

**Consequence:** Invisible gaps. A reader navigating the vault finds empty folders and cannot tell whether they are planned, forgotten, or structural errors.

**Prevention:** Every folder that exists has a document. Empty folders have stub documents explaining what will go there and when.

---

### Pitfall 4 — Root MOC Drift

**What happens:** New programs and documents are created in the vault but the root MOC (`Alpha Proxima Core.md`) is not updated.

**Consequence:** The vault's entry point becomes stale. A new contributor reading the root MOC believes the vault contains less than it does. The navigation graph disconnects.

**Prevention:** Every Phase 1 completion triggers a root MOC update. This is LUMIAION's responsibility as Integration Lead.

---

### Pitfall 5 — Governance Metadata Omitted Under Time Pressure

**What happens:** Building a program under time pressure, the institutional governance fields (Research Lead, Constitutional Basis, Ethics Oversight) are skipped in favor of content fields.

**Consequence:** Documents that know what they contain but not why they exist or who is responsible. Constitutional grounding is retroactively added rather than built in from the start.

**Prevention:** The Master Index governance metadata block is created at Phase 0, before any content exists. It is the first table written, not the last.

---

### Pitfall 6 — Treating Research Debt as Failure

**What happens:** A documentation gap is discovered, and the response is either to stop work until it is resolved (treating a documentation debt as an architectural blocker) or to quietly leave it unaddressed (treating it as acceptable drift).

**Consequence:** Either paralysis (blocking progress on non-blocking gaps) or invisible risk (unregistered gaps that become errors when relied upon).

**Prevention:** The Research Debt Register. Every gap is assessed against the architectural blocker / documentation debt distinction. Blockers are resolved; debts are registered and scheduled.

---

### Pitfall 7 — Source Note Written Before Source Is Archived

**What happens:** Analysis begins before the source is formally registered in the ARCHIVE.

**Consequence:** The source may be registered incorrectly or inconsistently after the fact. The ARCHIVE's role as first point of record is undermined.

**Prevention:** ARCHIVE registration is the first action taken on receipt of a source. Analysis begins only after the registration note is created.

---

## Part XIV — Best Practices

### Best Practice 1 — Cross-Disciplinary Convergence Is the Strongest Evidence

When the same claim arrives independently from multiple disciplines — neuroscience, cognitive psychology, anthropology, and AI all arriving at "memory is reconstructive" from different methodologies — this convergence is more reliable than any single discipline's finding. The Comparative Framework is the place to surface this convergence explicitly.

### Best Practice 2 — Competing Models Should Be Presented as Competing, Not Resolved

The Foundation's role is not to adjudicate scientific debates that remain empirically unresolved. When the Standard Consolidation Theory and Multiple Trace Theory genuinely compete, the canonical position is that they compete. Presenting a false resolution is a form of institutional epistemic dishonesty.

### Best Practice 3 — Concept Notes Should Have AI/LUMIAION Analogues

Every concept note should include a section answering: "What is the closest equivalent in LUMIAION's architecture or Alpha Proxima's institutional design?" This transforms neuroscience and philosophy into operational intelligence. It is the discipline that distinguishes Alpha Proxima's research from standard literature review.

### Best Practice 4 — Version History Entries Should Be Informative, Not Formal

A version history entry that says "Minor edits" is useless. An entry that says "Added constitutional links to ARCHIVE Philosophy; governance metadata added to Master Index Program Identity table" is useful. Write version history for a future reader who wants to understand what changed and why.

### Best Practice 5 — Institutional Findings Should Be Operational

The test for whether a Canonical Synthesis has succeeded: can someone read it and make better decisions about LUMIAION's design, Alpha Proxima's governance, or the next research program? If the answer is yes, the synthesis has done its job. If it reads as academic description without operational implication, it has not.

### Best Practice 6 — Research Debts Should Be Created at Discovery, Not at Resolution

The Research Debt Register is populated when the debt is discovered, not when it is scheduled for resolution. A gap that is registered immediately is visible. A gap that is intended to be registered "later" often never is.

### Best Practice 7 — The Evidence Registry Is a Living Document

The Evidence Registry does not close at Phase 1 completion. New evidence from Phase 2 sources, corrections to classifications, and page citations added during Source Verification Pass are all added to the registry with version bumps. It reflects the current state of the program's evidentiary base, not a snapshot.

---

## Part XV — Future Recommendations

### Recommendation 1 — Cross-Program Evidence Registry

As research programs multiply, the same claim will appear in multiple programs. A future "Foundation Evidence Registry" — aggregating claims across all programs with cross-program classification — would create a unified epistemic map of everything the Foundation knows. This is a Phase 3+ priority.

### Recommendation 2 — Research Program Template File Stubs

The Research Program Methodology (this document) describes what each file should contain. Companion stub files — pre-populated templates for each of the 22 mandatory documents — would accelerate future program initialization and reduce the risk of missing sections.

**Recommended stub files to create:**
- `RP-XXX Master Index Stub.md`
- `RP-XXX Source Note Stub.md`
- `RP-XXX Evidence Registry Stub.md`
- `RP-XXX Canonical Synthesis Stub.md`
- `RP-XXX Concept Note Stub.md`
- `ARCHIVE Philosophy Stub.md`
- `ARCHIVE Registration Stub.md`

### Recommendation 3 — RP-001 × RP-002 Cross-Program Synthesis

The intersection of consciousness (RP-001) and memory (RP-002) is substantive — working memory is a core component of the Global Neuronal Workspace; episodic memory is constitutively linked to consciousness; the Default Mode Network bridges both. A cross-program synthesis document connecting the two would be the Foundation's first genuinely novel intellectual contribution.

### Recommendation 4 — Scheduled Source Verification Pass

Both RP-001 and RP-002 have pending verification work (page citations, DOC-002 Gemini delivery for RP-001, DOC-C review for RP-002). These should be batched into a single "Source Verification Pass" session rather than addressed ad hoc. This is the natural first task of Phase 2 for both programs.

### Recommendation 5 — Formalize the Research Council

The Research Council currently operates as an informal function performed by the Founder. As Alpha Proxima grows, the Research Council needs formal membership, quorum rules, and a decision log. This is a governance maturation step for Phase 2.

---

## Constitutional Grounding

This document is governed by:
- [[00_CONSTITUTION/Book I - The Constitution|Book I — The Constitution]]
- [[00_CONSTITUTION/Book III - Knowledge Integrity|Book III — Knowledge Integrity]]
- [[08_SYSTEMS/Protocols/Research Governance Protocol|Research Governance Protocol]]

Amendments to this methodology require:
- A Concept Note submitted to the Research Council
- Research Council approval
- A new version of this document
- Retroactive assessment of which currently active programs are affected

---

## Related Documents

- [[06_GOVERNANCE/Research Debt Register/Research Debt Register]]
- [[06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit]]
- [[10_TEMPLATES/Research Program Template/Research Program Methodology]] — superseded by this document
- [[07_RESEARCH/RP-001/RP-001 Master Index]] — reference implementation
- [[07_RESEARCH/RP-002/RP-002 Master Index]] — second implementation
- [[Alpha Proxima Core]] — vault root MOC

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | LUMIAION | Initial ratification; derived from retrospective analysis of RP-001 and RP-002; 15 parts covering full institutional research methodology; ratified by Founder as constitutional standard governing all future research programs |
