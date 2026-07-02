---
title: "ES-001 - Orphan Document Classification"
aliases: ["Orphan Document Classification", "ES-001 Orphan Review"]
tags: [systems, engineering, validation, orphan-notes, backlinks, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: draft
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-report
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[Tool 001 - Vault Validator]]"]
related_documents: ["[[Vault Validation Report]]", "[[RP-001 Master Index]]", "[[Metadata Migration Plan v1.0]]"]
related_research_programs: ["RP-001", "RP-002", "RP-003", "RP-004", "RP-005", "RP-006"]
---

# ES-001 - Orphan Document Classification

## Purpose

Classify every document reported as missing incoming wiki links during ES-001 without automatically creating backlinks or changing institutional navigation.

## Dependencies

- [[Tool 001 - Vault Validator]]
- [[RP-001 Master Index]]
- [[Metadata Migration Plan v1.0]]

## Version

| Field | Value |
|-------|-------|
| Version | 1.0.0 |
| Status | draft |
| Date | 2026-07-02 |

## Author

[[CODEX]]

## Related Documents

- [[Vault Validation Report]]
- [[RP-001 Master Index]]
- [[Metadata Migration Plan v1.0]]

## Related Research Programs

- RP-001
- RP-002
- RP-003
- RP-004
- RP-005
- RP-006

## Classification Rules

| Classification | Meaning |
|----------------|---------|
| Intentional | The note may remain without incoming links because it is preserved for legacy, archival, or system reasons |
| Needs Index Link | The note should be reachable from a master index, registry, or office index |
| Deprecated | The note has likely been superseded and should be marked or routed through a deprecation process |
| Archive Candidate | The note should be considered for archive movement or removal after human confirmation |

## Orphan Classification

| Document | Classification | Recommended Institutional Location | Rationale |
|----------|----------------|------------------------------------|-----------|
| `06_GOVERNANCE/Standards Council/Standards Council Evaluation.md` | Needs Index Link | Governance index or Standards Council index | Active governance support document should be discoverable from the governance navigation layer |
| `07_RESEARCH/RP-001/05 Source - Gemini/RP-001 Source Note - Gemini.md` | Needs Index Link | RP-001 Master Index source notes section | Source note is part of RP-001 and should be linked explicitly, not only represented by folder name |
| `07_RESEARCH/RP-001/06 Source - SanaLab/RP-001 Source Note - SanaLab.md` | Needs Index Link | RP-001 Master Index source notes section | Source note documents DOC-003 and DOC-004 and should be reachable from RP-001 navigation |
| `07_RESEARCH/RP-001/07 Future Sources/RP-001 Future Sources.md` | Needs Index Link | RP-001 Master Index supporting documents section | Future-source registry is active research infrastructure |
| `07_RESEARCH/RP-001/16 Visual Knowledge/RP-001 Visual Knowledge Index.md` | Needs Index Link | RP-001 Master Index supporting documents section | Visual knowledge index is part of the 22-folder RP-001 structure |
| `07_RESEARCH/RP-001/19 Related Laws/RP-001 Governing Provisions.md` | Needs Index Link | RP-001 Master Index governing documents section | Governance relationship note should be discoverable from the RP-001 governance area |
| `07_RESEARCH/RP-001/20 Related ADRs/RP-001 ADR Links.md` | Needs Index Link | RP-001 Master Index governing documents section | ADR relationship note should be discoverable from the RP-001 governance area |
| `07_RESEARCH/RP-002/RP-002 Master Index.md` | Needs Index Link | Research program registry or research roadmap | Placeholder program index should be reachable from a research-level index |
| `07_RESEARCH/RP-003/RP-003 Master Index.md` | Needs Index Link | Research program registry or research roadmap | Placeholder program index should be reachable from a research-level index |
| `07_RESEARCH/RP-004/RP-004 Master Index.md` | Needs Index Link | Research program registry or research roadmap | Placeholder program index should be reachable from a research-level index |
| `07_RESEARCH/RP-005/RP-005 Master Index.md` | Needs Index Link | Research program registry or research roadmap | Placeholder program index should be reachable from a research-level index |
| `07_RESEARCH/RP-006/RP-006 Master Index.md` | Needs Index Link | Research program registry or research roadmap | Placeholder program index should be reachable from a research-level index |
| `ALPHA PROXIMA/ALPHA.PROXIMA.FOUNDATION/Building achitecture/LUMIAION VAULT.md` | Intentional | Legacy area, with later optional consolidation into `99_ARCHIVE/` | Existing status is archived and content is legacy navigation; no immediate fix required |
| `Building Milestone.md` | Archive Candidate | `99_ARCHIVE/` or legacy preservation area | Root placeholder exists only for legacy link integrity and should not remain root-level long term unless a current index links to it |

## Implementation Notes

No backlinks were created during this classification. The appropriate next engineering step is to add index links only where the owning office agrees that the note should remain active and discoverable.

The RP-001 master index already references several folder areas. The validator counts note-level incoming wiki links, so folder mentions do not satisfy graph health.

## Future Improvements

- [ ] Add an orphan allowlist for intentional archive and legacy notes.
- [ ] Add an index-link recommendation mode to the Link Integrity Scanner.
- [ ] Add a research program registry to link RP-002 through RP-006 intentionally.
- [ ] Add root-placeholder cleanup workflow requiring confirmation.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial ES-001 orphan classification |
