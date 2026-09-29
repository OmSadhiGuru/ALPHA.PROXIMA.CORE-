#!/usr/bin/env python3
"""The adapter boundary — where provider vocabulary stops and AlphaEvent begins.

An adapter's whole job is translation, and it is the only place in the
Foundation allowed to know what a GitHub payload or a Notion page object looks
like. Downstream, everything is an `AlphaEvent`.

## The three rules every adapter obeys

1. **It normalizes; it does not act.** `normalize()` returns events. It writes
   no state, touches no note, and cannot reach `founder_os`. The single-writer
   model is preserved by construction, not by convention — this module does not
   import the state engine at all.
2. **It rejects rather than guesses.** A payload it does not recognize, or one
   missing the fields the event needs, raises `AdapterError` at the boundary.
   A half-understood event is worse than a dropped one: it enters the ledger
   with fabricated provenance and stays there.
3. **It reports its own status honestly.** `planned` and `blocked` adapters
   exist here as real, testable contracts with fixtures and health records —
   and they never report `connected`. An integration is connected when a
   verified delivery has arrived, which is a fact about the world, not a fact
   about this file.

## Why the unimplemented adapters are here at all

Each one carries the configuration it will need, the capabilities it will
offer, and the reason it is not live. That makes the Founder's honest answer
to "what is connected?" a single read of the registry rather than an
archaeology expedition through eleven half-finished branches. It also makes
the first credential that arrives a configuration change instead of a design.

Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import sys
import time
from pathlib import Path
from typing import Any, Callable

TOOLKIT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = TOOLKIT_DIR.parent.parent
LIVE_DIR = VAULT_ROOT / "13_OPERATIONS" / "Live Integration Layer"
DEFAULT_REGISTRY = LIVE_DIR / "state" / "adapter-registry.json"

sys.path.insert(0, str(TOOLKIT_DIR))
import alpha_events as ev  # noqa: E402  (path-based sibling import, as the toolkit does elsewhere)
import state_io  # noqa: E402

REGISTRY_SCHEMA_VERSION = "1.0.0"

# The honest status vocabulary. `connected` is earned by a verified delivery;
# every other value is a statement about what is missing.
STATUSES = ("connected", "degraded", "disconnected", "planned", "blocked")


class AdapterError(Exception):
    """Raised when a provider payload cannot be normalized. Rejected at the edge."""


# --------------------------------------------------------------------------
# webhook ingress security
# --------------------------------------------------------------------------

def verify_github_signature(secret: str, body: bytes, header: str) -> bool:
    """Constant-time check of GitHub's `X-Hub-Signature-256`.

    An unverified webhook body is an anonymous stranger claiming a commit
    happened. Callers treat a `False` here as a rejected delivery, not a
    degraded one — there is nothing to degrade to.
    """
    if not secret or not header:
        return False
    expected = "sha256=" + hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, header)


# --------------------------------------------------------------------------
# the adapter interface
# --------------------------------------------------------------------------

class Adapter:
    """One external system's translation contract.

    Subclasses set the class attributes and implement `normalize`. Everything
    else — health bookkeeping, capability reporting, the refusal to write —
    is inherited so that a new provider cannot accidentally acquire powers the
    boundary does not grant.
    """

    adapter_id: str = ""
    provider: str = ""
    display_name: str = ""
    # Declared status: what this adapter can be *before* any delivery arrives.
    # A live adapter declares `disconnected` and becomes `connected` only once
    # the registry records a success.
    declared_status: str = "planned"
    capabilities: tuple[str, ...] = ()
    # Provider event names this adapter accepts. Anything else is rejected.
    accepts: tuple[str, ...] = ()
    department: str = "UNATTRIBUTED"
    # Why it is not live, in one sentence a Founder can act on. Empty for a
    # live adapter.
    blocked_reason: str = ""
    # What a human must supply to activate it. Names only — never values.
    configuration: tuple[str, ...] = ()
    schema_version: str = ev.SCHEMA_VERSION

    def normalize(self, delivery: dict[str, Any]) -> list[dict[str, Any]]:
        """Translate one provider delivery into zero or more AlphaEvents."""
        raise NotImplementedError(
            f"{type(self).__name__}.normalize is not implemented; "
            "this adapter is a contract, not a connection."
        )

    # -- shared boundary checks -----------------------------------------
    def check_delivery(self, delivery: Any) -> dict[str, Any]:
        """Validate the delivery envelope itself before reading its payload."""
        if not isinstance(delivery, dict):
            raise AdapterError(f"Delivery must be a JSON object, got {type(delivery).__name__}.")
        kind = delivery.get("kind")
        if not isinstance(kind, str) or not kind:
            raise AdapterError("Delivery is missing 'kind' (the provider's own event name).")
        if self.accepts and kind not in self.accepts:
            raise AdapterError(
                f"{self.provider} adapter does not handle {kind!r}. "
                f"Accepted: {', '.join(self.accepts)}."
            )
        payload = delivery.get("payload")
        if not isinstance(payload, dict):
            raise AdapterError("Delivery is missing a 'payload' object.")
        return delivery

    def descriptor(self) -> dict[str, Any]:
        """What the registry publishes about this adapter, with no secrets in it."""
        return {
            "adapter_id": self.adapter_id,
            "provider": self.provider,
            "display_name": self.display_name or self.provider,
            "declared_status": self.declared_status,
            "capabilities": list(self.capabilities),
            "accepts": list(self.accepts),
            "department": self.department,
            "blocked_reason": self.blocked_reason,
            "configuration_required": list(self.configuration),
            "schema_version": self.schema_version,
            "implemented": type(self).normalize is not Adapter.normalize,
        }


# --------------------------------------------------------------------------
# GitHub — the first production adapter
# --------------------------------------------------------------------------

def _short(text: Any, limit: int = 160) -> str:
    """One line, bounded. Provider prose is summarized, never mirrored."""
    value = " ".join(str(text or "").split())
    return value if len(value) <= limit else value[: limit - 1] + "…"


class GitHubAdapter(Adapter):
    """Normalize GitHub webhook deliveries into AlphaEvents.

    This is the one adapter in the Foundation with a real transport today: the
    repository already exists, the events already happen, and a webhook secret
    is the only thing between this code and live activity. It therefore carries
    the fullest event coverage, and the rest of the adapters are shaped after
    it.

    Severity is assigned here, deliberately, per event kind — not inherited
    from GitHub, which has no concept of the Founder's attention. The rule: a
    failed check or a review the Founder personally owes is `action`; ordinary
    forward progress is `update`; bookkeeping is `info`. Nothing GitHub can
    send is `critical`, because a red build is not an institutional emergency.
    """

    adapter_id = "ADP-GITHUB"
    provider = "github"
    display_name = "GitHub"
    declared_status = "disconnected"
    department = "ENGINEERING"
    capabilities = (
        "push", "commit", "branch", "pull_request", "review", "ci", "issue", "deployment",
    )
    accepts = (
        "push", "create", "pull_request", "pull_request_review", "check_run",
        "check_suite", "workflow_run", "issues", "deployment", "deployment_status",
    )
    configuration = ("GITHUB_WEBHOOK_SECRET", "GITHUB_REPOSITORY")
    # GitHub is the one adapter whose translation is finished, so its reason is
    # about transport, not implementation: nothing has verified a delivery yet.
    blocked_reason = (
        "Normalization is implemented and tested against fixtures. No webhook "
        "secret is configured and no authenticated ingress is deployed, so no "
        "delivery has been verified — replays from fixtures never promote status."
    )

    def normalize(self, delivery: dict[str, Any]) -> list[dict[str, Any]]:
        self.check_delivery(delivery)
        kind = delivery["kind"]
        payload = delivery["payload"]
        received_at = delivery.get("received_at") or ev.now_iso()
        delivery_id = str(delivery.get("delivery_id") or "")
        correlation = delivery.get("correlation_id") or ""
        causation = delivery.get("causation_id") or ""

        handler: Callable[..., list[dict[str, Any]]] = {
            "push": self._push,
            "create": self._create,
            "pull_request": self._pull_request,
            "pull_request_review": self._review,
            "check_run": self._check,
            "check_suite": self._check,
            "workflow_run": self._workflow_run,
            "issues": self._issue,
            "deployment": self._deployment,
            "deployment_status": self._deployment,
        }[kind]

        context = {
            "received_at": received_at,
            "delivery_id": delivery_id,
            "correlation_id": correlation,
            "causation_id": causation,
            "repository": _short(payload.get("repository", {}).get("full_name"), 120),
        }
        events = handler(payload, context)
        if not events:
            raise AdapterError(
                f"GitHub {kind!r} delivery carried no event this adapter reports "
                "(an ignored action is rejected, not silently stored)."
            )
        return events

    # -- helpers ---------------------------------------------------------
    def _actor(self, payload: dict[str, Any]) -> str:
        """Who acted, as GitHub knows them, with one Foundation-specific mapping.

        CODEX and Claude both commit through GitHub accounts, so a login alone
        under-describes the Council. Only the logins the Foundation has actually
        seen are mapped; every other login passes through unchanged rather than
        being guessed at.
        """
        login = _short(
            (payload.get("sender") or {}).get("login")
            or (payload.get("pusher") or {}).get("name"),
            80,
        )
        known = {
            "omsadhiguru": "Founder",
            "github-actions[bot]": "CI",
        }
        return known.get(login.lower(), login) or "unknown"

    def _base(self, context: dict[str, Any], **fields: Any) -> dict[str, Any]:
        """Build one event, threading delivery provenance through consistently."""
        metadata = dict(fields.pop("metadata", {}) or {})
        if context["repository"]:
            metadata["repository"] = context["repository"]
        if context["delivery_id"]:
            metadata["delivery_id"] = context["delivery_id"]
        # An explicit correlation from the handler wins over the delivery's own:
        # a per-entity correlation (one pull request, one issue) is a stronger
        # grouping than the webhook that happened to carry it.
        correlation = fields.pop("correlation_id", None) or context["correlation_id"] or None
        causation = fields.pop("causation_id", None) or context["causation_id"] or None
        return ev.make_event(
            source="github",
            department=self.department,
            received_at=context["received_at"],
            correlation_id=correlation,
            causation_id=causation,
            metadata=metadata,
            **fields,
        )

    # -- per-kind normalization -----------------------------------------
    def _push(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        commits = payload.get("commits") or []
        ref = _short(payload.get("ref"), 120)
        branch = ref.rsplit("/", 1)[-1] if ref else "unknown"
        after = _short(payload.get("after"), 64) or "unknown"
        actor = self._actor(payload)
        events = [
            self._base(
                context,
                actor=actor,
                event_type="github.push.completed",
                entity_type="branch",
                entity_id=f"{branch}@{after[:12]}",
                title=f"{len(commits)} commit(s) pushed to {branch}",
                summary=_short(
                    (commits[-1].get("message") if commits else "") or f"Branch {branch} updated"
                ),
                severity="update",
                deep_link=ev.deep_link("github", "branch", branch),
                occurred_at=self._push_time(payload, commits),
                provider_event_id=f"push:{after}" if after != "unknown" else None,
                metadata={"branch": branch, "commit_count": len(commits), "head": after[:12]},
            )
        ]
        # Each commit is its own event so Memory can hold a commit as a node,
        # not only the push that carried it. They share the push's correlation
        # id and name it as their cause.
        for commit in commits[:20]:
            commit_id = _short(commit.get("id"), 64)
            if not commit_id:
                continue
            events.append(
                self._base(
                    dict(context, correlation_id=events[0]["correlation_id"],
                         causation_id=events[0]["event_id"]),
                    actor=_short((commit.get("author") or {}).get("name"), 80) or actor,
                    event_type="github.commit.created",
                    entity_type="commit",
                    entity_id=commit_id[:12],
                    title=_short(commit.get("message"), 120) or f"Commit {commit_id[:12]}",
                    summary=f"{len(commit.get('modified') or [])} file(s) modified on {branch}",
                    severity="info",
                    deep_link=ev.deep_link("github", "commit", commit_id[:12]),
                    occurred_at=self._instant(commit.get("timestamp")) or context["received_at"],
                    provider_event_id=f"commit:{commit_id}",
                    metadata={
                        "branch": branch,
                        "added": len(commit.get("added") or []),
                        "modified": len(commit.get("modified") or []),
                        "removed": len(commit.get("removed") or []),
                    },
                )
            )
        return events

    def _push_time(self, payload: dict[str, Any], commits: list[dict[str, Any]]) -> str:
        for commit in reversed(commits):
            instant = self._instant(commit.get("timestamp"))
            if instant:
                return instant
        return self._instant((payload.get("head_commit") or {}).get("timestamp")) or ev.now_iso()

    def _instant(self, value: Any) -> str:
        """Provider timestamp, or empty when it is absent or unparseable."""
        if not isinstance(value, str) or not value.strip():
            return ""
        try:
            return ev.parse_iso(value).isoformat(timespec="seconds")
        except ev.EventError:
            return ""

    def _create(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        ref_type = _short(payload.get("ref_type"), 32)
        if ref_type != "branch":
            raise AdapterError(f"GitHub 'create' for {ref_type!r} is not a reported event.")
        branch = _short(payload.get("ref"), 120)
        if not branch:
            raise AdapterError("GitHub 'create' delivery has no ref.")
        return [
            self._base(
                context,
                actor=self._actor(payload),
                event_type="github.branch.created",
                entity_type="branch",
                entity_id=branch,
                title=f"Branch {branch} created",
                summary=f"New branch on {context['repository'] or 'the repository'}",
                severity="info",
                deep_link=ev.deep_link("github", "branch", branch),
                provider_event_id=f"branch:{branch}",
                metadata={"branch": branch},
            )
        ]

    def _pull_request(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        action = _short(payload.get("action"), 40)
        pull = payload.get("pull_request") or {}
        number = pull.get("number")
        if not isinstance(number, int):
            raise AdapterError("GitHub pull_request delivery has no pull_request.number.")
        entity = f"PR-{number}"
        title = _short(pull.get("title"), 120) or entity
        link = ev.deep_link("github", "pr", str(number))
        merged = bool(pull.get("merged"))

        # (event_type, headline, severity, requires_founder) per action. Actions
        # absent from this table are genuinely uninteresting to the Foundation
        # (labeled, assigned, synchronize noise) and are rejected rather than
        # recorded, keeping the activity feed about progress.
        table = {
            "opened": ("github.pr.opened", f"{entity} opened", "update", False),
            "reopened": ("github.pr.reopened", f"{entity} reopened", "update", False),
            "edited": ("github.pr.updated", f"{entity} updated", "info", False),
            "synchronize": ("github.pr.updated", f"{entity} received new commits", "info", False),
            "ready_for_review": ("github.pr.review_required", f"{entity} is ready for review",
                                 "action", True),
            "review_requested": ("github.pr.review_required", f"{entity} requests a review",
                                 "action", True),
            "closed": ("github.pr.closed", f"{entity} closed without merging", "update", False),
        }
        if action == "closed" and merged:
            event_type, headline, severity, founder = (
                "github.pr.merged", f"{entity} merged", "update", False)
        elif action in table:
            event_type, headline, severity, founder = table[action]
        else:
            raise AdapterError(f"GitHub pull_request action {action!r} is not a reported event.")

        occurred = (
            self._instant(pull.get("merged_at"))
            or self._instant(pull.get("closed_at") if action == "closed" else "")
            or self._instant(pull.get("updated_at"))
            or context["received_at"]
        )
        return [
            self._base(
                context,
                actor=self._actor(payload),
                event_type=event_type,
                entity_type="pull_request",
                entity_id=entity,
                title=f"{headline}: {title}" if title != entity else headline,
                summary=_short(
                    f"{pull.get('changed_files') or 0} file(s), "
                    f"+{pull.get('additions') or 0}/-{pull.get('deletions') or 0}"
                ),
                severity=severity,
                requires_founder=founder,
                deep_link=link,
                occurred_at=occurred,
                # The PR number correlates every event about one pull request,
                # so Memory can assemble its whole history without a join table.
                correlation_id=f"github:pr:{number}",
                provider_event_id=f"pr:{number}:{action}:{'merged' if merged else 'open'}",
                metadata={
                    "number": number,
                    "state": _short(pull.get("state"), 20),
                    "merged": merged,
                    "draft": bool(pull.get("draft")),
                    "branch": _short((pull.get("head") or {}).get("ref"), 120),
                },
            )
        ]

    def _review(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        if _short(payload.get("action"), 40) != "submitted":
            raise AdapterError("Only a submitted GitHub review is a reported event.")
        review = payload.get("review") or {}
        pull = payload.get("pull_request") or {}
        number = pull.get("number")
        if not isinstance(number, int):
            raise AdapterError("GitHub review delivery has no pull_request.number.")
        state = _short(review.get("state"), 40).lower() or "commented"
        # `changes_requested` is the one review outcome that puts work back on
        # the author, so it is the one that costs the Founder's attention.
        severity = "action" if state == "changes_requested" else "update"
        return [
            self._base(
                context,
                actor=self._actor(payload),
                event_type=f"github.review.{state}",
                entity_type="review",
                entity_id=f"PR-{number}-review-{_short(review.get('id'), 32) or 'unknown'}",
                title=f"Review {state.replace('_', ' ')} on PR-{number}",
                summary=_short(review.get("body")) or f"Review submitted on PR-{number}",
                severity=severity,
                requires_founder=(state == "changes_requested"),
                deep_link=ev.deep_link("github", "pr", str(number)),
                occurred_at=self._instant(review.get("submitted_at")) or context["received_at"],
                correlation_id=f"github:pr:{number}",
                provider_event_id=f"review:{review.get('id')}",
                metadata={"number": number, "state": state},
            )
        ]

    def _check(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        run = payload.get("check_run") or payload.get("check_suite") or {}
        status = _short(run.get("status"), 40).lower()
        conclusion = _short(run.get("conclusion"), 40).lower()
        name = _short(run.get("name") or "check suite", 120)
        identity = _short(run.get("id"), 32) or "unknown"

        if status in ("queued", "in_progress"):
            event_type, severity, headline, founder = (
                "github.ci.started", "info", f"CI started: {name}", False)
        elif conclusion == "success":
            event_type, severity, headline, founder = (
                "github.ci.succeeded", "info", f"CI passed: {name}", False)
        elif conclusion in ("failure", "timed_out", "action_required", "startup_failure"):
            event_type, severity, headline, founder = (
                "github.ci.failed", "action", f"CI failed: {name}", True)
        elif conclusion in ("cancelled", "skipped", "neutral", "stale"):
            event_type, severity, headline, founder = (
                "github.ci.skipped", "info", f"CI {conclusion}: {name}", False)
        else:
            raise AdapterError(
                f"GitHub check delivery has no reportable outcome (status={status!r}, "
                f"conclusion={conclusion!r})."
            )

        pulls = run.get("pull_requests") or []
        number = pulls[0].get("number") if pulls and isinstance(pulls[0], dict) else None
        correlation = f"github:pr:{number}" if isinstance(number, int) else ""
        return [
            self._base(
                dict(context, correlation_id=correlation or context["correlation_id"]),
                actor="CI",
                event_type=event_type,
                entity_type="check_run",
                entity_id=f"check-{identity}",
                title=headline,
                summary=_short(
                    (run.get("output") or {}).get("title")
                    or f"{status or 'unknown'} / {conclusion or 'pending'}"
                ),
                severity=severity,
                requires_founder=founder,
                deep_link=(
                    ev.deep_link("github", "pr", str(number)) if isinstance(number, int)
                    else ev.deep_link("github", "check", str(identity))
                ),
                occurred_at=(
                    self._instant(run.get("completed_at"))
                    or self._instant(run.get("started_at"))
                    or context["received_at"]
                ),
                provider_event_id=f"check:{identity}:{status}:{conclusion}",
                metadata={"check": name, "status": status, "conclusion": conclusion},
            )
        ]

    def _workflow_run(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        run = payload.get("workflow_run") or {}
        # A workflow run is a check suite by another name; reuse one mapping so
        # `github.ci.*` means the same thing whichever webhook reported it.
        synthetic = {
            "check_run": {
                "id": run.get("id"),
                "name": run.get("name") or "workflow",
                "status": run.get("status"),
                "conclusion": run.get("conclusion"),
                "started_at": run.get("run_started_at"),
                "completed_at": run.get("updated_at"),
                "pull_requests": run.get("pull_requests") or [],
            },
            "repository": payload.get("repository") or {},
            "sender": payload.get("sender") or {},
        }
        events = self._check(synthetic, context)
        for event in events:
            event["entity_type"] = "workflow_run"
        return events

    def _issue(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        action = _short(payload.get("action"), 40)
        issue = payload.get("issue") or {}
        number = issue.get("number")
        if not isinstance(number, int):
            raise AdapterError("GitHub issues delivery has no issue.number.")
        table = {
            "opened": ("github.issue.created", f"Issue #{number} opened", "update"),
            "edited": ("github.issue.updated", f"Issue #{number} updated", "info"),
            "reopened": ("github.issue.updated", f"Issue #{number} reopened", "info"),
            "closed": ("github.issue.closed", f"Issue #{number} closed", "info"),
        }
        if action not in table:
            raise AdapterError(f"GitHub issues action {action!r} is not a reported event.")
        event_type, headline, severity = table[action]
        return [
            self._base(
                context,
                actor=self._actor(payload),
                event_type=event_type,
                entity_type="issue",
                entity_id=f"ISSUE-{number}",
                title=f"{headline}: {_short(issue.get('title'), 120)}",
                summary=_short(issue.get("body")) or headline,
                severity=severity,
                deep_link=ev.deep_link("github", "issue", str(number)),
                occurred_at=self._instant(issue.get("updated_at")) or context["received_at"],
                correlation_id=f"github:issue:{number}",
                provider_event_id=f"issue:{number}:{action}",
                metadata={"number": number, "state": _short(issue.get("state"), 20)},
            )
        ]

    def _deployment(self, payload: dict[str, Any], context: dict[str, Any]) -> list[dict[str, Any]]:
        deployment = payload.get("deployment") or {}
        status = payload.get("deployment_status") or {}
        identity = _short(deployment.get("id"), 32) or "unknown"
        environment = _short(deployment.get("environment") or status.get("environment"), 60) or "unknown"
        state = _short(status.get("state"), 40).lower()

        if not state:
            event_type, severity, headline, founder = (
                "github.deployment.created", "update", f"Deployment to {environment} created", False)
        elif state in ("success",):
            event_type, severity, headline, founder = (
                "github.deployment.succeeded", "update", f"Deployed to {environment}", False)
        elif state in ("failure", "error"):
            # A failed deployment is the one GitHub event that can be critical:
            # it is the only one that can leave the Foundation's own hosted
            # surface unavailable.
            event_type, severity, headline, founder = (
                "github.deployment.failed", "critical", f"Deployment to {environment} failed", True)
        else:
            event_type, severity, headline, founder = (
                "github.deployment.updated", "info", f"Deployment to {environment} is {state}", False)

        return [
            self._base(
                context,
                actor=self._actor(payload) or "CI",
                event_type=event_type,
                entity_type="deployment",
                entity_id=f"deploy-{identity}",
                title=headline,
                summary=_short(status.get("description") or deployment.get("description")) or headline,
                severity=severity,
                requires_founder=founder,
                deep_link=ev.deep_link("system", "deployment", str(identity)),
                occurred_at=(
                    self._instant(status.get("updated_at"))
                    or self._instant(deployment.get("created_at"))
                    or context["received_at"]
                ),
                correlation_id=f"github:deployment:{identity}",
                provider_event_id=f"deployment:{identity}:{state or 'created'}",
                metadata={"environment": environment, "state": state or "created"},
            )
        ]


# --------------------------------------------------------------------------
# the adapters that are contracts, not connections
# --------------------------------------------------------------------------

class PlannedAdapter(Adapter):
    """Base for an adapter whose transport does not exist yet.

    `normalize` deliberately raises. A planned adapter that silently produced
    plausible events would be the exact dishonesty the registry exists to
    prevent — the Founder would see activity from a system nobody connected.
    """

    def normalize(self, delivery: dict[str, Any]) -> list[dict[str, Any]]:
        raise AdapterError(
            f"{self.display_name} is {self.declared_status}, not connected. "
            f"{self.blocked_reason} "
            f"Required configuration: {', '.join(self.configuration) or 'none recorded'}."
        )


class ChatGPTAdapter(PlannedAdapter):
    adapter_id = "ADP-CHATGPT"
    provider = "chatgpt"
    display_name = "ChatGPT / LUMIAION runtime"
    declared_status = "planned"
    department = "KNOWLEDGE"
    capabilities = ("conversation", "synthesis", "presence")
    accepts = ("conversation.completed", "synthesis.produced", "presence.changed")
    blocked_reason = (
        "LUMIAION reasons inside a chat session that emits no webhook; a runtime "
        "signal channel has to exist before presence can be reported honestly."
    )
    configuration = ("OPENAI_API_KEY", "ALPHA_RUNTIME_SIGNAL_ENDPOINT")


class CodexAdapter(PlannedAdapter):
    adapter_id = "ADP-CODEX"
    provider = "codex"
    display_name = "CODEX runtime"
    declared_status = "planned"
    department = "ENGINEERING"
    capabilities = ("presence", "task_status", "run_reporting")
    accepts = ("run.started", "run.completed", "run.failed", "presence.changed")
    blocked_reason = (
        "CODEX participates through commits and pull requests, which the GitHub "
        "adapter already normalizes. A direct runtime channel adds presence, "
        "not activity, and does not exist yet."
    )
    configuration = ("ALPHA_RUNTIME_SIGNAL_ENDPOINT",)


class ClaudeAdapter(PlannedAdapter):
    adapter_id = "ADP-CLAUDE"
    provider = "claude"
    display_name = "Claude runtime"
    declared_status = "planned"
    department = "KNOWLEDGE"
    capabilities = ("presence", "run_reporting", "documentation")
    accepts = ("run.started", "run.completed", "presence.changed")
    blocked_reason = (
        "Same shape as CODEX: sessions are observable through their commits, "
        "not through a runtime API this repository holds."
    )
    configuration = ("ANTHROPIC_API_KEY", "ALPHA_RUNTIME_SIGNAL_ENDPOINT")


class GeminiAdapter(PlannedAdapter):
    adapter_id = "ADP-GEMINI"
    provider = "gemini"
    display_name = "Gemini"
    declared_status = "planned"
    department = "RESEARCH"
    capabilities = ("presence", "research_output")
    accepts = ("run.completed", "presence.changed")
    blocked_reason = "No credential and no assigned Council role consuming it."
    configuration = ("GOOGLE_AI_API_KEY",)


class PerplexityAdapter(PlannedAdapter):
    adapter_id = "ADP-PERPLEXITY"
    provider = "perplexity"
    display_name = "Perplexity"
    declared_status = "planned"
    department = "RESEARCH"
    capabilities = ("research_output", "citation_capture")
    accepts = ("research.completed",)
    blocked_reason = "No credential; research capture has no approved write path yet."
    configuration = ("PERPLEXITY_API_KEY",)


class PocketAIAdapter(PlannedAdapter):
    adapter_id = "ADP-POCKET-AI"
    provider = "pocket_ai"
    display_name = "Pocket AI"
    declared_status = "planned"
    department = "MEMORY"
    capabilities = ("capture", "transcript", "classification")
    accepts = ("capture.created", "transcript.ready")
    blocked_reason = (
        "Depends on the same ContextItem contract as INT-003 (OMI); no adapter "
        "or credential exists in this repository."
    )
    configuration = ("POCKET_AI_WEBHOOK_SECRET",)


class ObsidianAdapter(PlannedAdapter):
    adapter_id = "ADP-OBSIDIAN"
    provider = "obsidian"
    display_name = "Obsidian Vault"
    declared_status = "planned"
    department = "KNOWLEDGE"
    capabilities = ("note_modified", "note_created", "indexing")
    accepts = ("note.created", "note.modified", "note.renamed")
    blocked_reason = (
        "The Vault is canonical and already git-versioned, so GitHub reports its "
        "changes. A direct Obsidian channel would be a second, racing observer "
        "of the same truth; it is planned only for local-edit latency."
    )
    configuration = ("OBSIDIAN_LOCAL_BRIDGE_TOKEN",)


class GoogleDriveAdapter(PlannedAdapter):
    adapter_id = "ADP-GDRIVE"
    provider = "google_drive"
    display_name = "Google Drive"
    declared_status = "planned"
    department = "OPERATIONS"
    capabilities = ("file_created", "file_modified", "sharing_changed")
    accepts = ("file.created", "file.modified", "permission.changed")
    blocked_reason = "No OAuth client registered for the Foundation."
    configuration = ("GOOGLE_OAUTH_CLIENT_ID", "GOOGLE_OAUTH_CLIENT_SECRET", "GOOGLE_DRIVE_CHANNEL_TOKEN")


class GoogleCalendarAdapter(PlannedAdapter):
    adapter_id = "ADP-GCAL"
    provider = "google_calendar"
    display_name = "Google Calendar"
    declared_status = "planned"
    department = "EXECUTIVE"
    capabilities = ("event_created", "event_changed", "commitment_signal")
    accepts = ("event.created", "event.updated", "event.cancelled")
    blocked_reason = (
        "INT-005 records the same gap: no adapter or credential in this "
        "repository. Calendar commitments becoming Founder OS tasks is also a "
        "write path, which needs the single writer's approval, not an adapter's."
    )
    configuration = ("GOOGLE_OAUTH_CLIENT_ID", "GOOGLE_OAUTH_CLIENT_SECRET", "GOOGLE_CALENDAR_ID")


class NotionAdapter(PlannedAdapter):
    adapter_id = "ADP-NOTION"
    provider = "notion"
    display_name = "Notion"
    declared_status = "planned"
    department = "OPERATIONS"
    capabilities = ("page_updated", "database_row_changed", "project_status")
    accepts = ("page.updated", "database.row_changed")
    blocked_reason = "No integration token; Notion has no outbound webhook for the needed scope."
    configuration = ("NOTION_API_TOKEN", "NOTION_PROJECT_DATABASE_ID")


class N8nAdapter(PlannedAdapter):
    adapter_id = "ADP-N8N"
    provider = "n8n"
    display_name = "n8n"
    declared_status = "planned"
    department = "OPERATIONS"
    capabilities = ("workflow_started", "workflow_succeeded", "workflow_failed")
    accepts = ("execution.started", "execution.finished", "execution.failed")
    blocked_reason = "No n8n instance is reachable from this repository."
    configuration = ("N8N_WEBHOOK_SECRET", "N8N_BASE_URL")


class SemanticMemoryAdapter(PlannedAdapter):
    """Blocked rather than planned — and the distinction is the point.

    `planned` means nobody has built it. `blocked` means something must be
    decided first. This one waits on an unfilled Council role, which is a
    Founder decision, not an engineering task, so it is reported differently.
    """

    adapter_id = "ADP-SEMANTIC-MEMORY"
    provider = "alpha_proxima"
    display_name = "Semantic memory (vector index)"
    declared_status = "blocked"
    department = "MEMORY"
    capabilities = ("indexing", "retrieval", "presence")
    accepts = ("index.completed", "retrieval.completed")
    blocked_reason = (
        "INT-006: the Chief Memory Architect role is unfilled, which blocks "
        "Layer 3 of the LUMIAION memory architecture. A Founder appointment "
        "unblocks this, not an implementation."
    )
    configuration = ()


ADAPTER_CLASSES: tuple[type[Adapter], ...] = (
    GitHubAdapter,
    ChatGPTAdapter,
    CodexAdapter,
    ClaudeAdapter,
    GeminiAdapter,
    PerplexityAdapter,
    PocketAIAdapter,
    ObsidianAdapter,
    GoogleDriveAdapter,
    GoogleCalendarAdapter,
    NotionAdapter,
    N8nAdapter,
    SemanticMemoryAdapter,
)


# --------------------------------------------------------------------------
# the registry
# --------------------------------------------------------------------------

class AdapterRegistry:
    """Every adapter's declared contract joined to its observed health.

    Health is observed, not declared: `record_success` and `record_failure` are
    the only things that can move an adapter to `connected` or `degraded`. This
    is the honesty guard in code — a registry entry cannot claim a connection
    that no delivery ever demonstrated.

    Health lives in its own JSON file, written atomically through the same
    helper the Founder OS uses. It is deliberately *not* in `founder-state.json`:
    adapter liveness is operational telemetry, and giving it a second writer
    into Founder state would break the single-writer model this whole layer
    exists to preserve.
    """

    # An adapter that has succeeded but not recently is degraded, not connected:
    # silence from a webhook is indistinguishable from a broken webhook, and the
    # interface must not present the two the same way.
    STALE_AFTER_SECONDS = 24 * 3600

    def __init__(self, path: Path | str = DEFAULT_REGISTRY,
                 adapters: tuple[type[Adapter], ...] = ADAPTER_CLASSES) -> None:
        self.path = Path(path)
        self.adapters: dict[str, Adapter] = {}
        for cls in adapters:
            adapter = cls()
            self.adapters[adapter.adapter_id] = adapter
        self.health: dict[str, dict[str, Any]] = self._load()

    # -- persistence -----------------------------------------------------
    def _load(self) -> dict[str, dict[str, Any]]:
        if not self.path.exists():
            return {}
        try:
            stored = json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            # Telemetry that cannot be read is telemetry that never existed.
            # Losing it degrades the display; refusing to start would take the
            # whole layer down over a corrupt cache.
            return {}
        entries = stored.get("adapters") if isinstance(stored, dict) else None
        return entries if isinstance(entries, dict) else {}

    def save(self) -> Path:
        state_io.write_json_atomic(self.path, {
            "schema_version": REGISTRY_SCHEMA_VERSION,
            "updated_at": ev.now_iso(),
            "adapters": self.health,
        })
        return self.path

    # -- observation -----------------------------------------------------
    def _entry(self, adapter_id: str) -> dict[str, Any]:
        return self.health.setdefault(adapter_id, {
            "last_seen": None, "last_success": None, "last_error": None,
            "error_count": 0, "success_count": 0, "event_count": 0,
            "last_event_id": None, "last_latency_ms": None,
            "last_rehearsal": None, "rehearsal_count": 0,
        })

    def record_success(self, adapter_id: str, *, events: int = 0,
                       latency_ms: float | None = None, last_event_id: str | None = None,
                       at: str | None = None, verified: bool = True) -> dict[str, Any]:
        """Record a normalization that worked.

        `verified=False` is the honesty guard that matters most in this file. A
        fixture replayed from `fixtures/` proves the *adapter* works; it proves
        nothing about the *connection*, because no external system sent it. Such
        a run is counted as a rehearsal and deliberately does not touch
        `last_success`, so no amount of local testing can make a disconnected
        provider read as connected in the Founder's interface.
        """
        if adapter_id not in self.adapters:
            raise AdapterError(f"Unknown adapter {adapter_id!r}; an unregistered adapter has no health.")
        entry = self._entry(adapter_id)
        stamp = at or ev.now_iso()
        entry["last_seen"] = stamp
        if verified:
            entry["last_success"] = stamp
            entry["success_count"] += 1
            entry["event_count"] += events
        else:
            entry["last_rehearsal"] = stamp
            entry["rehearsal_count"] += 1
        if latency_ms is not None:
            entry["last_latency_ms"] = round(float(latency_ms), 3)
        if last_event_id:
            entry["last_event_id"] = last_event_id
        return entry

    def record_failure(self, adapter_id: str, reason: str, at: str | None = None) -> dict[str, Any]:
        if adapter_id not in self.adapters:
            raise AdapterError(f"Unknown adapter {adapter_id!r}; an unregistered adapter has no health.")
        entry = self._entry(adapter_id)
        stamp = at or ev.now_iso()
        entry["last_seen"] = stamp
        entry["error_count"] += 1
        entry["last_error"] = {"at": stamp, "reason": _short(reason, 300)}
        return entry

    # -- honest status ---------------------------------------------------
    def observed_status(self, adapter_id: str, now: str | None = None) -> str:
        """The status a delivery record actually supports.

        The rules, in order, each one a refusal to overstate:
          * a `planned` or `blocked` declaration is never overridden by
            telemetry — those adapters cannot produce a success;
          * no success ever recorded means `disconnected`, whatever errors say;
          * a success plus a more recent failure means `degraded`;
          * a success older than the staleness window means `degraded`;
          * only a recent, uncontradicted success means `connected`.
        """
        adapter = self.adapters.get(adapter_id)
        if adapter is None:
            raise AdapterError(f"Unknown adapter {adapter_id!r}.")
        if adapter.declared_status in ("planned", "blocked"):
            return adapter.declared_status
        entry = self.health.get(adapter_id) or {}
        success = entry.get("last_success")
        if not success:
            return "disconnected"
        error = (entry.get("last_error") or {}).get("at")
        if error and ev.parse_iso(error) > ev.parse_iso(success):
            return "degraded"
        reference = ev.parse_iso(now or ev.now_iso())
        if (reference - ev.parse_iso(success)).total_seconds() > self.STALE_AFTER_SECONDS:
            return "degraded"
        return "connected"

    def view(self, now: str | None = None) -> dict[str, Any]:
        """The `/api/v1/integrations` read model: contract plus observed health."""
        reference = now or ev.now_iso()
        rows = []
        for adapter_id, adapter in self.adapters.items():
            entry = self.health.get(adapter_id) or {}
            status = self.observed_status(adapter_id, reference)
            rows.append({
                **adapter.descriptor(),
                "status": status,
                "connected": status == "connected",
                "last_seen": entry.get("last_seen"),
                "last_success": entry.get("last_success"),
                "last_error": entry.get("last_error"),
                "error_count": entry.get("error_count", 0),
                "success_count": entry.get("success_count", 0),
                "event_count": entry.get("event_count", 0),
                "last_event_id": entry.get("last_event_id"),
                "last_latency_ms": entry.get("last_latency_ms"),
                "last_rehearsal": entry.get("last_rehearsal"),
                "rehearsal_count": entry.get("rehearsal_count", 0),
            })
        rows.sort(key=lambda row: (STATUSES.index(row["status"]), row["adapter_id"]))
        counts: dict[str, int] = {status: 0 for status in STATUSES}
        for row in rows:
            counts[row["status"]] += 1
        broken = [
            {"adapter_id": row["adapter_id"], "status": row["status"],
             "reason": (row["last_error"] or {}).get("reason") or row["blocked_reason"]}
            for row in rows
            if row["status"] in ("degraded", "disconnected")
        ]
        return {
            "schema_version": REGISTRY_SCHEMA_VERSION,
            "generated_at": reference,
            "mode": "read_only",
            "adapters": rows,
            "counts": {**counts, "total": len(rows)},
            # "What is broken?" answered without opening a server log.
            "broken": broken,
        }

    # -- ingestion -------------------------------------------------------
    # A delivery's `origin` says whether it came from the world. Anything other
    # than `webhook` (a replayed fixture, a local rehearsal) is normalized and
    # stored, but never counted as evidence of a live connection.
    VERIFIED_ORIGINS = ("webhook",)

    def ingest(self, delivery: dict[str, Any], ledger: ev.EventLedger | None = None,
               adapter_id: str | None = None) -> dict[str, Any]:
        """Normalize one delivery, record health, and optionally store the events.

        This is the whole path from `EXTERNAL SYSTEM` to `EVENT LEDGER`, and it
        is the only path: there is no route from a provider payload to a
        projection that skips validation and deduplication.

        A delivery that does not declare `"origin": "webhook"` is treated as a
        rehearsal: its events are real and storable, but the adapter's status is
        left where it was. Verification is a fact about the world, and a local
        file cannot supply it.
        """
        provider = delivery.get("provider") if isinstance(delivery, dict) else None
        if adapter_id is None:
            matches = [a.adapter_id for a in self.adapters.values()
                       if a.provider == provider and type(a).normalize is not Adapter.normalize
                       and a.declared_status not in ("planned", "blocked")]
            if not matches:
                matches = [a.adapter_id for a in self.adapters.values() if a.provider == provider]
            if not matches:
                raise AdapterError(
                    f"No adapter registered for provider {provider!r}. "
                    "An unknown provider is rejected, never stored."
                )
            adapter_id = matches[0]
        adapter = self.adapters[adapter_id]

        started = time.perf_counter()
        try:
            events = adapter.normalize(delivery)
        except AdapterError as exc:
            self.record_failure(adapter_id, str(exc))
            raise
        except (KeyError, TypeError, ValueError, ev.EventError) as exc:
            # A provider payload that breaks the adapter's own assumptions is a
            # rejected delivery, not a crash that takes ingress down.
            self.record_failure(adapter_id, f"{type(exc).__name__}: {exc}")
            raise AdapterError(f"{adapter.display_name} payload rejected: {exc}") from exc
        latency_ms = (time.perf_counter() - started) * 1000

        stored = duplicates = 0
        if ledger is not None:
            result = ledger.extend(events)
            stored, duplicates = result["stored"], result["duplicates"]
        verified = str(delivery.get("origin") or "").lower() in self.VERIFIED_ORIGINS
        self.record_success(
            adapter_id,
            events=stored,
            latency_ms=latency_ms,
            last_event_id=events[-1]["event_id"] if events else None,
            verified=verified,
        )
        return {
            "adapter_id": adapter_id,
            "accepted": len(events),
            "stored": stored,
            "duplicates": duplicates,
            "latency_ms": round(latency_ms, 3),
            "verified": verified,
            "events": events,
        }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ap.py adapters", description=__doc__)
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY), help="Adapter health file.")
    parser.add_argument("--ledger", default=str(ev.DEFAULT_LEDGER), help="Event ledger (JSONL).")

    sub = parser.add_subparsers(dest="command", required=True)

    listing = sub.add_parser("list", help="Every adapter, its honest status, and why.")
    listing.add_argument("--json", action="store_true", help="Machine-readable output.")

    normalize = sub.add_parser("normalize", help="Normalize a delivery; print events, store nothing.")
    normalize.add_argument("delivery", help="JSON file path, '-' for stdin, or a JSON literal.")
    normalize.add_argument("--adapter", default=None, help="Force a specific adapter id.")

    ingest = sub.add_parser("ingest", help="Normalize a delivery and append its events.")
    ingest.add_argument("delivery", help="JSON file path, '-' for stdin, or a JSON literal.")
    ingest.add_argument("--adapter", default=None, help="Force a specific adapter id.")
    ingest.add_argument("--dry-run", action="store_true", help="Normalize and report; write nothing.")

    sub.add_parser("health", help="Adapter health, including what is broken.")
    return parser


def _render_list(view: dict[str, Any]) -> str:
    lines = [f"{'ADAPTER':<22} {'STATUS':<13} {'EVENTS':>7}  WHY / LAST ERROR"]
    lines.append("-" * 96)
    for row in view["adapters"]:
        why = (row["last_error"] or {}).get("reason") or row["blocked_reason"] or ""
        lines.append(
            f"{row['adapter_id']:<22} {row['status']:<13} {row['event_count']:>7}  {_short(why, 54)}"
        )
    counts = view["counts"]
    lines.append("")
    lines.append(
        f"{counts['total']} adapter(s): "
        + ", ".join(f"{counts[status]} {status}" for status in STATUSES if counts[status])
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    registry = AdapterRegistry(args.registry)

    try:
        if args.command == "list":
            view = registry.view()
            print(json.dumps(view, indent=2, ensure_ascii=False) if args.json else _render_list(view))
            return 0

        if args.command == "health":
            view = registry.view()
            print(json.dumps({"counts": view["counts"], "broken": view["broken"]},
                             indent=2, ensure_ascii=False))
            return 0

        delivery = ev._load_json_argument(args.delivery)
        if args.command == "normalize":
            adapter_id = args.adapter
            if adapter_id is None:
                provider = delivery.get("provider") if isinstance(delivery, dict) else None
                candidates = [a.adapter_id for a in registry.adapters.values() if a.provider == provider]
                if not candidates:
                    raise AdapterError(f"No adapter registered for provider {provider!r}.")
                adapter_id = candidates[0]
            events = registry.adapters[adapter_id].normalize(delivery)
            print(json.dumps(events, indent=2, ensure_ascii=False))
            return 0

        if args.command == "ingest":
            ledger = None if args.dry_run else ev.EventLedger(args.ledger)
            result = registry.ingest(delivery, ledger=ledger, adapter_id=args.adapter)
            if not args.dry_run:
                registry.save()
            print(
                f"{result['adapter_id']}: accepted {result['accepted']}, stored {result['stored']}, "
                f"{result['duplicates']} duplicate(s), {result['latency_ms']}ms"
                + ("" if result["verified"] else " (rehearsal — status unchanged)")
                + (" (dry run — nothing written)" if args.dry_run else "")
            )
            return 0
    except (AdapterError, ev.EventError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        # A rejected delivery is a distinct outcome from a usage error: exit 1
        # so ingress can tell "you sent nonsense" from "I was called wrong".
        return 1
    except (json.JSONDecodeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
