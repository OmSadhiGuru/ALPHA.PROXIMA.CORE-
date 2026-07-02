---
title: "08 - Logging Standard"
aliases: ["Log Standard", "Audit Logging Standard"]
tags: [systems, engineering, standards, logging, audit, alpha-proxima]
created: 2026-07-02
updated: 2026-07-02
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: engineering-standard
standard_id: "ES-08"
institutional_owner: "Alpha Proxima Foundation"
cognitive_function: "Implementation"
reasoning_engine: "CODEX"
dependencies: ["[[ALPHA PROXIMA ENGINEERING HANDBOOK]]"]
related_documents: ["[[Vault Note Generator]]"]
related_research_programs: []
---

# 08 - Logging Standard

## Purpose

Define logging practices that make automation observable, failures diagnosable, and institutional write activity auditable without leaking sensitive information.

---

## Scope

Applies to local scripts, CLI tools, scheduled jobs, GitHub workflows, MCP integrations, n8n workflows, local services, and indexing pipelines.

---

## Rules

- Log operational events, not private content.
- Use ISO 8601 timestamps with timezone when available.
- Include severity, component, action, target, and outcome.
- Include correlation IDs for multi-step workflows.
- Include research IDs or document IDs when relevant.
- Keep debug logs disabled by default.
- Do not log secrets, tokens, credentials, private keys, or full sensitive payloads.
- Retain logs only as long as they support maintenance and audit needs.
- Prefer structured logs for automation and concise text logs for simple local tools.

### Severity Levels

| Level | Meaning |
|-------|---------|
| DEBUG | Detailed diagnostic information, disabled by default |
| INFO | Expected operational event |
| WARNING | Recoverable issue or unusual condition |
| ERROR | Operation failed and needs attention |
| CRITICAL | System integrity, data loss, or governance boundary risk |

---

## Examples

### Text Log

```text
2026-07-02T14:05:00-04:00 INFO vault_note create target="08_SYSTEMS/Implementation Notes/API Plan.md" outcome=created correlation_id=vn-20260702-001
```

### JSON Log

```json
{
  "timestamp": "2026-07-02T14:05:00-04:00",
  "severity": "INFO",
  "component": "vault_note",
  "action": "create",
  "target": "08_SYSTEMS/Implementation Notes/API Plan.md",
  "outcome": "created",
  "correlation_id": "vn-20260702-001"
}
```

### Error Log

```text
2026-07-02T14:06:00-04:00 ERROR vault_note create target="Plan.md" outcome=refused reason="file exists"
```

---

## Best Practices

- Use one correlation ID per workflow run.
- Log before and after destructive or external operations.
- Keep log messages stable enough for future parsing.
- Store audit-worthy logs in a documented location.
- Use summaries for large validation runs.
- Redact sensitive values before logging.

---

## Common Mistakes

- Logging entire documents when only file paths are needed.
- Treating debug logs as permanent audit logs.
- Omitting target paths from write operations.
- Using inconsistent severity names.
- Recording timestamps without timezone.
- Keeping logs forever without a retention reason.

---

## Future Evolution

Future versions may define canonical log storage paths, retention periods, event schemas, and audit report formats. Any retention policy involving sensitive data should be reviewed through governance.

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | [[CODEX]] | Initial logging standard |

---

## Related Standards

- [[05 - Python Development Standard]]
- [[06 - CLI Standard]]
- [[07 - Automation Standard]]
- [[09 - Git Standard]]

