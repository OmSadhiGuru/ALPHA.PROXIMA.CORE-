---
title: "07 - Automation Standard"
aliases: ["Automation Philosophy", "Workflow Automation Standard"]
tags: [systems, engineering, standards, automation, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-07"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Vault Note Generator]]", "[[Decision Routing Protocol]]"]
related_research_programs: []
---

# 07 - Automation Standard

## Purpose

Define how Alpha Proxima automates repetitive technical work while preserving human governance, accountability, and durable institutional memory.

---

## Scope

Applies to scripts, scheduled jobs, n8n workflows, GitHub workflows, local services, MCP integrations, indexing pipelines, note generators, and write-back automations.

---

## Rules

- Automate repetition, not institutional judgment.
- Default generated artifacts to `draft` unless an approved process says otherwise.
- Require explicit human approval for governance status changes, constitutional edits, destructive operations, publication, and external sends.
- Log every write operation with timestamp, actor, target, and outcome.
- Make automation idempotent where possible.
- Use retries only for transient failures.
- Preserve source material; do not overwrite canonical notes without explicit override.
- Write back to the vault using approved templates and naming standards.
- Keep scheduling visible in documentation.
- Include a manual recovery path for every critical automation.

### Approval Boundary

Automation may:

- Generate drafts.
- Validate metadata.
- Create indexes.
- Update derived artifacts.
- Run tests.
- Produce reports.

Automation may not:

- Ratify ADRs.
- Approve concept notes.
- Change constitutional documents.
- Decide research canon status.
- Delete institutional records.
- Substitute for human review where governance requires judgment.

---

## Examples

### Safe Generated Draft

```text
Input: title, author, purpose
Action: create draft implementation note
Status: draft
Human review required: yes, before activation
```

### Scheduled Validation

```text
Trigger: daily local schedule
Action: scan Markdown files for required frontmatter
Write-back: validation report only
Approval required: no
```

### Governance-Sensitive Operation

```text
Trigger: request to mark ADR accepted
Action: stop and request governance confirmation
Write-back: none until approval
Approval required: yes
```

---

## Best Practices

- Document trigger, inputs, outputs, owner, and failure mode.
- Make dry runs available for writes.
- Keep automation narrow and composable.
- Use clear names for generated files.
- Keep generated content visibly reviewable.
- Prefer local-first workflows with Git history.

---

## Common Mistakes

- Treating generated output as approved output.
- Hiding automation behavior in undocumented scripts.
- Retrying permanent failures.
- Overwriting human edits.
- Writing logs without enough context to audit the action.
- Coupling automation to a vendor name instead of a stable function.

---

## Future Evolution

Future versions may define approval gates for n8n workflows, MCP write tools, background monitors, and vector database refresh jobs. Governance-sensitive gates should be approved institutionally before enforcement.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial automation standard |

---

## Related Standards

- [[02 - YAML Frontmatter Standard]]
- [[05 - Python Development Standard]]
- [[06 - CLI Standard]]
- [[08 - Logging Standard]]
- [[09 - Git Standard]]

