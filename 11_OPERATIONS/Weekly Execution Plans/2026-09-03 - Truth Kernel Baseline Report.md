---
title: "Truth Kernel Baseline Report"
aliases: ["Truth Kernel Baseline 2026-09-03"]
tags: [operations, engineering, backend, knowledge-graph, baseline, alpha-proxima]
created: 2026-09-03
updated: 2026-09-03
status: draft
version: "0.1.0"
authors: ["CODEX"]
artifact_type: engineering-baseline
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[2026-09-03 - Truth Kernel Execution Plan]]", "[[Graph Readiness Assessment]]", "[[Knowledge Graph Architecture v1.0]]"]
related_documents: ["[[2026-09-03 - Truth Kernel Execution Plan]]"]
---

# Truth Kernel Baseline Report

## Baseline decision

For the v0 read-only Truth Kernel, the canonical input boundary is:

```text
/Users/Fred/Documents/Obsidian Vault
```

This selection follows the Founder's stated operating model: Obsidian is the base data control and ALPHAPROXIMA is the Vault. This report does not declare other checkouts disposable or authorize their deletion.

## Evidence captured

Captured on Thursday 2026-09-03 at approximately 12:42 EDT.

| Field | Confirmed value |
|---|---|
| Vault root | `/Users/Fred/Documents/Obsidian Vault` |
| Git root | `/Users/Fred/Documents/Obsidian Vault` |
| Git branch | `main` |
| Git HEAD | `844a37ef2e6a01c6f90232f1539e81f677649d48` |
| Git remote | `https://github.com/OmSadhiGuru/ALPHA.PROXIMA.CORE-.git` |
| Markdown files in proposed scan boundary | 297 |
| Symbolic links detected | 0 |
| Approximate Vault size including local system data | 109 MB |

The Markdown count excludes the local/system directories listed below. It is a baseline count, not yet a validated Node Registry total.

## Competing or adjacent roots

These paths exist and must not be merged, removed, or treated as canonical input by the v0 generator:

| Path | Observed state | Classification |
|---|---|---|
| `/Users/Fred/Desktop/ALPHAPROXIMA` | Git branch `reboot/2026-08-23-control-center`, HEAD `89353f220dde51657766b238350ad266ec6ecbc9` | Separate historical/implementation checkout; preserve pending reconciliation |
| `/Users/Fred/.codex/visualizations/2026/08/26/01a03d69-8ca4-7763-8f5e-8af22970989c/founder-os-3d-prototype` | Located inside Git root `/Users/Fred`, HEAD observed as `0b5d9b3aa164bee71b3d1474bc37026626f63bd8` | Interface prototype; consumer of derived data, not canonical knowledge source |

## v0 scan boundary

Include:

- Markdown files below the canonical Vault root.
- YAML frontmatter and document body required for identity and relationship extraction.

Exclude:

- `.git/`
- `.obsidian/`
- `.claude/`
- `.claudian/`
- `.codex/`
- `.makemd/`
- `.smart-env/`
- `.space/`
- Any future generated-output directory.
- Binary attachments for v0; paths may be recorded later without content extraction.

## Generated-output boundary

Proposed dedicated output root:

```text
/Users/Fred/Documents/Obsidian Vault/.alpha-proxima/generated/truth-kernel
```

The directory has not been created by this baseline step. Before the generator writes there, the implementation must:

1. Exclude it from its own scan.
2. Decide explicitly whether generated artifacts are Git-ignored or selectively preserved.
3. Never treat generated output as canonical source material.

## Verification boundary

Confirmed:

- Exact canonical input path for v0.
- Git root, branch, HEAD, and remote for that path.
- Existence and identity of two adjacent/competing implementation roots.
- Initial Markdown count using explicit system-directory exclusions.
- No symbolic links were found in the canonical Vault root.

Not confirmed:

- Full working-tree cleanliness. A full `git status` did not return within the observation window and no clean-state claim is made.
- Byte-level equality between the canonical Vault and the Desktop checkout.
- Remote recoverability of the observed commits.
- Whether every Markdown file belongs in the institutional graph.
- Whether the proposed generated-output path should be versioned.

## Reproduction commands

```sh
pwd -P
git rev-parse --show-toplevel
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
git remote -v
find . \( -path './.git' -o -path './.obsidian' -o -path './.claudian' -o -path './.codex' -o -path './.makemd' -o -path './.smart-env' -o -path './.space' \) -prune -o -type f -name '*.md' -print | wc -l
find . -type l -print | wc -l
du -sh .
```

## Gate result

**T1 — Canonical input boundary: CONFIRMED WITH DECLARED LIMITS**

Implementation may proceed to the Node Contract only within this read boundary. This confirmation does not authorize canonical note mutation, repository reconciliation, merge, deletion, or remote publication.
