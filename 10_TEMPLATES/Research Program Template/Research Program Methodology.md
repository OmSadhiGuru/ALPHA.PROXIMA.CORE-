---
title: "Research Program Methodology — Alpha Proxima Standard"
aliases: ["RP Methodology", "Research Program Standard", "RP Template Guide"]
tags: [template, methodology, research, standard, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: ratified
version: "1.0.0"
authors: ["LUMIAION"]
template_type: Research Program Methodology
derived_from: ["RP-001 Atlas of Human Consciousness", "RP-002 Atlas of Human Memory"]
---

# Research Program Methodology — Alpha Proxima Standard

> This document codifies the research program methodology extracted from RP-001 and RP-002. It is the canonical authority for how all future Alpha Proxima research programs (RP-003 and beyond) are initiated, structured, executed, and maintained.
>
> Use the companion file stubs in `Research Program File Stubs/` to create each document. Use this document to understand why each file exists and what it must contain.

---

## The Core Principle (Never Varies)

> Original research is never replaced. Original research is never rewritten. Original research is never compressed. Canonical knowledge is built ON TOP of research. Never INSTEAD OF research. Alpha Proxima preserves both.

This principle is the constitutional foundation of every research program. It mandates the three-layer architecture: source preservation (ARCHIVE), source analysis (Source Notes), and institutional synthesis (Canonical Synthesis). These three layers must never collapse into one.

---

## The Standard Architecture

Every Alpha Proxima research program occupies a folder in `07_RESEARCH/RP-XXX/` with exactly 22 numbered subfolders plus an ARCHIVE folder and a Master Index file.

```
07_RESEARCH/RP-XXX/
│
├── RP-XXX Master Index.md          ← Navigation hub; program status at a glance
│
├── 00 Executive Summary/           ← Entry point for outsiders and future contributors
├── 01 Research Question/           ← The question driving the program
├── 02 Objectives/                  ← Phase structure and measurable goals
├── 03 Source Registry/             ← All sources: identity, status, quality
├── 04 Source - [Name]/             ← Working folder for first source
├── 05 Source - [Name]/             ← Working folder for second source
├── 06 Source - [Name]/             ← Working folder for third source
│   ...                             ← Additional source folders as needed
├── 07 Future Sources/              ← Sources under evaluation; pipeline
├── 08 Comparative Framework/       ← Side-by-side cross-source analysis
├── 09 Canonical Synthesis/         ← THE canonical document; institutional position
├── 10 Theory Matrix/               ← Structured comparison of all frameworks
├── 11 Canonical Glossary/          ← Authoritative term definitions
├── 12 Evidence Registry/           ← Every claim classified with source trace
├── 13 Research Graph/              ← Knowledge graph index + Concepts/ subfolder
│   └── Concepts/                   ← Individual concept notes
├── 14 Open Questions/              ← Registered unresolved questions
├── 15 Future Experiments/          ← Research opportunities derived from program
├── 16 Visual Knowledge/            ← Diagrams, visual models, spatial artifacts
├── 17 NotebookLM Package/          ← Curated source pack for deep-dive AI analysis
├── 18 Related Constitution/        ← Links to constitutional provisions governing this program
├── 19 Related Laws/                ← Governing provisions specific to this program
├── 20 Related ADRs/                ← Architecture decisions arising from this program
├── 21 Version History/             ← Program-level version log
│
└── ARCHIVE/                        ← Immutable source artifacts
    ├── ARCHIVE Philosophy.md       ← Immutability rules for this program
    └── DOC-XXX [Title].md          ← One immutable registration per source
```

---

## Phase Structure

### Phase 0 — Authorization (Before Any Files Are Created)

1. Research Council authorizes the program with a formal question and scope
2. Research Lead (JERANIUM) and Integration Lead (LUMIAION) are assigned
3. Master Index placeholder is created at `0.1.0` — the only file created at this stage
4. No content is developed until authorization is complete

**Output:** Master Index v0.1.0 with `status: planned`

---

### Phase 1 — Source Acquisition and Institutionalization

**Steps (in order):**

1. **ARCHIVE setup** — Create `ARCHIVE Philosophy.md`; establish immutability rules
2. **Source registration** — For each source: create immutable ARCHIVE registration note; assign DOC-ID
3. **Source review** — Read each source fully; create Source Note with full content extraction
4. **Source Registry** — Create `Source Registry` document aggregating all sources with status
5. **Evidence extraction** — From source notes, extract all material claims
6. **Evidence classification** — Classify every claim (C / M / E / Q / S / P) with page citation
7. **Theory matrix** — Map all competing frameworks across sources
8. **Comparative framework** — Side-by-side cross-source domain analysis
9. **Canonical synthesis** — Write the integrated institutional position
10. **Knowledge graph** — Create Research Graph index + one concept note per key term
11. **Supporting documents** — Glossary, Open Questions, Future Research, infrastructure links
12. **Master Index** — Update to v1.0.0 with full program status

**Output:** Master Index v1.0.0 with `status: active`

---

### Phase 2 — Deepening and Expansion

- Additional source integration (DOC-XXX pending in Phase 1 → reviewed in Phase 2)
- Research Initiative development (taking DOC-B/SanaLab-style proposals to specifications)
- Cross-program synthesis (links to related RP programs)
- ADR development (research findings → architectural decisions)

**Output:** Canonical Synthesis bumped (v1.0.0 → v1.1.0 or v2.0.0 for major revision)

---

### Phase 3 — Original Research

- Design and execute original research protocol
- Report findings as new evidence entries in Evidence Registry
- Integrate into Canonical Synthesis
- Produce publishable artifacts if appropriate

---

## The Evidence Classification System

All research programs use the same six-class taxonomy. This is defined in `[[Book III - Knowledge Integrity]]` and must not be modified at the program level.

| Code | Class | Definition |
|------|-------|------------|
| C | Consensus | Replicated, cross-disciplinary empirical consensus; no serious scientific challenge |
| M | Competing Models | Multiple credible frameworks; genuine empirical competition unresolved |
| E | Emerging Evidence | Recent findings; promising but not yet replicated at consensus level |
| Q | Open Question | Known unknown; question well-defined but answer genuinely unresolved |
| S | Speculative | Forward-looking conjecture; limited current empirical constraint |
| P | Phenomenological | First-person / experiential evidence; not reducible to third-person measurement |

**Evidence Registry format:** Every claim must have:
- Claim ID (e.g., C-001, M-002)
- Claim statement (one declarative sentence)
- Class code
- Source (DOC-ID)
- Page citation (or "p.TBD" if not yet located)
- Notes (competing claims, caveats, context)

---

## The ARCHIVE Rules (Never Vary)

1. **Never Modify** — Once registered, a source document is never altered
2. **Timestamp and Register** — Every artifact receives a deposit date and a DOC-ID
3. **Preserve Format** — PDFs are stored as PDFs; text extracts are additive, not replacements
4. **Link Outward** — Archive notes link to synthesis documents; synthesis does not modify archive
5. **Immutability Declaration** — All archive registration notes carry `immutable: true` in frontmatter
6. **ARCHIVE Philosophy status** — Set to `ratified` (not just `active`) once program is authorized

**DOC-ID naming:** Each program uses its own convention to avoid collision:
- RP-001: DOC-001, DOC-002, DOC-003, DOC-004
- RP-002: DOC-A, DOC-B, DOC-C
- RP-003+: Recommend DOC-001/002/003 (aligned with RP-001) unless program has specific reason to differ

---

## The Canonical Synthesis Standard

The Canonical Synthesis is the most important document in the program. It must:

1. Open with the institutional principle (original research is never replaced...)
2. State the most important single finding prominently — the finding that changes how Alpha Proxima operates
3. Be organized into thematic chapters (not source-by-source)
4. Cite evidence classifications inline (e.g., [C-001], [M-003])
5. Include at least one chapter on Alpha Proxima / LUMIAION implications
6. Never replace a source note — it synthesizes; source notes preserve
7. Be versioned: v1.0.0 for initial synthesis; v1.1.0 for integration of pending sources; v2.0.0 for major revision

---

## The Research Graph Standard

`13 Research Graph/` has two components:

1. **Research Graph index document** (`RP-XXX Research Graph.md`) — A domain map showing how concepts relate, where coverage exists, where gaps remain. Includes an ASCII relationship diagram. Minimum: identify the major domains the program covers and show which concept notes map to which domains.

2. **Concept notes** (`Concepts/` subfolder) — One note per key term. Each concept note must include:
   - Canonical definition (one paragraph; precise; institutional)
   - Key properties or mechanisms (bulleted or tabular)
   - AI/LUMIAION analogue where applicable
   - Related concepts (wikilinks)
   - Evidence classification references
   - Version history

**Minimum concept notes:** 8–15 per program, covering all key terms used in the Canonical Synthesis.

---

## Master Index Standard

The Master Index must include:

| Required Field | Format |
|---------------|--------|
| Program ID | RP-XXX |
| Full Title | Full program name |
| Initiated | Date |
| Current Phase | Phase 0–3 with status |
| Governing Protocol | `[[Research Governance Protocol]]` |
| Constitutional Basis | `[[Book III - Knowledge Integrity]]` |
| Ethics Oversight | `[[Ethics Council Charter]]` |
| Research Lead | `[[JERANIUM Charter|JERANIUM]]` (or other designated lead) |
| Integration Lead | `[[LUMIAION Charter|LUMIAION]]` |
| Primary Question | One sentence |
| Sources | Count with reviewed/pending breakdown |
| Evidence Claims | Count |
| Frameworks | Count |
| Concept Notes | Count |

The Master Index is a status document, not a content document. It must be updatable without understanding the program's content.

---

## YAML Frontmatter Standards

All documents in a research program must include at minimum:

```yaml
---
title: "RP-XXX [Document Name]"
aliases: ["Alias 1", "Alias 2"]
tags: [research, rp-xxx, [relevant-tags], alpha-proxima]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active | pending | ratified | planned
version: "1.0.0"
authors: ["LUMIAION"]
research_program: "RP-XXX [Program Full Name]"
---
```

ARCHIVE registrations additionally require:
```yaml
immutable: true
document_id: DOC-XXX
```

---

## What Varies Between Programs

The following elements are customized per program while the structure remains constant:

| Element | Varies How |
|---------|-----------|
| Folder names `04/05/06 Source - [Name]/` | Named after the contributor |
| DOC-ID scheme | Convention within program; must not collide |
| Number of source folders | 3–5 typical; more if program warrants |
| Concept notes count | 8–15; more for broader programs |
| Subdomain map | Specific to program topic |
| Research Initiatives | Only if source set proposes them (e.g., DOC-B for RP-002) |

---

## What Never Varies

- 22 numbered subfolders (00–21) + ARCHIVE
- ARCHIVE Philosophy + 5 immutability rules
- Evidence classification system (C/M/E/Q/S/P)
- Three-layer separation (ARCHIVE / Source Notes / Canonical Synthesis)
- Constitutional grounding links (Book III, Research Governance Protocol)
- Governance metadata in Master Index (Research Lead, Integration Lead, Ethics Oversight)
- Version history in every document
- The core principle (original research is never replaced...)

---

## Lessons From RP-001 and RP-002

**What RP-001 demonstrated:**
- The 22-subfolder architecture is navigable and complete
- The evidence classification system is the most useful single artifact
- Source notes should extract all content from the source, not just highlights
- Constitutional grounding (Book III) must be explicit in every program

**What RP-002 added:**
- Multi-language sources (French) are handled by translation in the source note; archive registration notes the language
- Illustrated or large-format PDFs require Founder review if they cannot be rendered in-session
- 10+ disciplines can be integrated into a single comparative framework
- The LUMIAION implications chapter is the most strategically valuable synthesis chapter

**What diverged (to be standardized):**
- RP-001 Evidence Registry has page citations; RP-002 does not → page citations are now mandatory
- RP-001 Master Index has governance metadata; RP-002 does not → governance metadata is now mandatory
- RP-001 has Research Graph index document; RP-002 does not → Research Graph index is now mandatory
- RP-001 ARCHIVE Philosophy cites Constitution; RP-002 does not → constitutional citation is now mandatory

---

## Related Documents

- [[10_TEMPLATES/Research Program Template/RP-XXX Master Index Stub]]
- [[10_TEMPLATES/Research Program Template/RP-XXX Source Note Stub]]
- [[10_TEMPLATES/Research Program Template/RP-XXX Evidence Registry Stub]]
- [[10_TEMPLATES/Research Program Template/RP-XXX Canonical Synthesis Stub]]
- [[08_SYSTEMS/Protocols/Research Governance Protocol]]
- [[00_CONSTITUTION/Book III - Knowledge Integrity]]
- [[07_RESEARCH/RP-001/RP-001 Master Index]] — reference implementation
- [[07_RESEARCH/RP-002/RP-002 Master Index]] — second implementation
- [[06_GOVERNANCE/Foundation Gap Report/FGR-001 Epoch II Stewardship Audit]]

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | LUMIAION | Initial extraction from RP-001 and RP-002; codifies standard methodology for all future programs |
