---
document_id: OSG-ACAD-INDEX
title: "OSG Academy — Canonical Index"
document_class: Index
status: active
version: "1.0.0"
owner: "Chief Learning Architect, OSG Academy"
updated: 2026-07-04
tags: [osg-academy, index, readme, reference]
---

# OSG Academy — Canonical Index

This folder holds the constitutional learning documents of **OSG Academy**. Together they form the governance stack that every OSG course is built and reviewed against.

## The governance stack

| Layer | Document | ID | Status | Role |
|-------|----------|----|--------|------|
| **1. Standard (law)** | [OSG Learning Standard (OLS) v1.0](./OSG%20Learning%20Standard%20%28OLS%29%20v1.0.md) | `OSG-ACAD-OLS` | Ratified · immutable | The constitutional learning standard. Every course must comply. |
| **2. Production (how-to)** | [Awaken the Inner Guru — Production Blueprint](./Awaken%20the%20Inner%20Guru%20%E2%80%94%20Production%20Blueprint.md) | `OSG-ACAD-PB-001` | v1.1 · incl. Bilingual FR/EN model | The full production architecture + bilingual (§11) model. |
| **3. Reference (benchmark)** | [**RI-001 — Awaken the Inner Guru — Reference Implementation Blueprint**](./RI-001%20Awaken%20the%20Inner%20Guru%20%E2%80%94%20Reference%20Implementation%20Blueprint.md) | `OSG-ACAD-RI-001` | Living reference · v1.1.0 | The minimum-quality benchmark every future course is reviewed against. |

## Reference Implementations

| Ref ID | Document ID | Course | Path | Status |
|--------|-------------|--------|------|--------|
| **RI-001** | `OSG-ACAD-RI-001` | Awaken the Inner Guru | `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md` | Living reference (v1.1.0) |

## How these relate

```
OLS (law, immutable)
   └── governs every course
        ├── Production Blueprint  → how to produce this course (+ bilingual model)
        └── RI-001 Reference      → the quality floor every FUTURE course is measured against
                                     (may innovate beyond it; may never violate the OLS)
```

## For engineering review (Codex)

- **Canonical reference document:** `OSG_BUSINESS/OSG_ACADEMY/RI-001 Awaken the Inner Guru — Reference Implementation Blueprint.md`
- **Stable identifiers:** `document_id: OSG-ACAD-RI-001` · `reference_id: RI-001` (both in the file's YAML frontmatter and its H1 subtitle).
- Locate locally by grepping `OSG-ACAD-RI-001` or `RI-001` from the repository root.

## Conventions

- **Reference Implementations** are numbered `RI-###`; document IDs are `OSG-ACAD-RI-###`.
- Each reference declares the `ols_version` it implements (forward-compatibility per RI-001 §16.8).
- Every future OSG course passes a **Reference Review** against the current RI before publication (RI-001 §16.2).
