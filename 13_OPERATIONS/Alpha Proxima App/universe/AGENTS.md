---
title: "Alpha Proxima Universe Prototype Instructions"
aliases: ["Universe Prototype Instructions"]
tags: [operations, app, interface, prototype]
created: 2026-09-02
updated: 2026-09-29
status: active
version: "1.0.0"
authors: ["Founder", "CODEX"]
artifact_type: implementation-guide
institutional_owner: "Engineering Office"
dependencies: ["[[Alpha Proxima App Architecture v1]]"]
related_documents: ["[[Alpha Proxima Unified Interface]]"]
related_research_programs: []
---

# Prototype Instructions

Run the local server yourself and open the preview in the browser available to this environment. Do not give the user server-start instructions when you can run it.

Before making substantial visual changes, use the Product Design plugin's `get-context` skill when the visual source is unclear or no longer matches the current goal. When the user gives durable prototype-specific design feedback, preferences, or decisions, record them in `AGENTS.md`.

When implementing from a selected generated mock, treat that image as the source of truth for layout, component anatomy, density, spacing, color, typography, visible content, and hierarchy.

Durable direction: Founder OS should feel like a navigable spatial environment, not a flat dashboard. Preserve the calm peripheral HUD and the Orbit / Surface / Inward Path mental model while giving the central operational field real depth, camera movement, selectable beacons, and a provenance tunnel.

The first/main Orbit interface must retain the auric body as the embodied operational map. System nodes align to that body; choosing one initiates the Surface dive, and the deeper provenance tunnel follows from inside the selected node.

Build app UI in `src/`. Keep `.openai/hosting.json`, `worker/index.js`, `scripts/prepare-sites-build.mjs`, and `tests/sites-worker.test.mjs` intact so the same local prototype can be handed to Sites. Before a Sites handoff, run `npm run build` and `npm run test:sites`; the build must leave `dist/client/index.html`, `dist/server/index.js`, and `dist/.openai/hosting.json`.

## Founder-confirmed direction (2026-09-02)

This is the Founder's actual interface, not a mockup to iterate away from. Direction confirmed: **pure void immersion** — minimal HUD, let the auric body and star field dominate; explicitly not the visor/cockpit-instrument-panel alternatives.

The Founder's two non-negotiable interaction foundations are **Orbit → Surface → Inward** and a **spatial dashboard experience**. Both stay; they are to be refined rather than replaced. Here, “dashboard” means an embodied, navigable decision interface—not a conventional grid of analytics cards or dense telemetry.

Mobile direction confirmed on 2026-09-04: a compressed desktop composition is not acceptable. Portrait access must preserve a centered, undistorted auric body; use one clear information layer per depth, keep essential touch controls readable during idle, and prevent mission, chakra rail, inspector, command, and mode navigation from competing simultaneously.

The spatial dashboard is intended to become a usable Founder control surface backed directly by the Obsidian Vault as institutional memory. LUMIAION is the consciousness/coordination layer embodied by the auric figure; specialist departments appear as chakra control centers that hold their orientations, objectives, and attention signals. The Founder navigates as Observer by default. Vault reads may be automatic, but canonical Vault writes and consequential actions remain explicitly Founder-gated.

Canonical data-control rule confirmed by the Founder: the Obsidian application is the base data-control surface, and the **ALPHAPROXIMA Vault** is the canonical memory/source of truth. The spatial Founder OS is a navigable projection and control interface over that Vault; it must not become a separate competing database.

- HUD chrome (header, mission, inspector, beacon-index, modes nav, command bar, depth-readout, gesture-hint) recedes to near-invisible after ~3.8s idle and restores instantly on interaction (see `quiet` state in `App.jsx`, `.quiet` rules in `styles.css`). Keep this — it's the mechanism that makes "void immersion" actually feel void most of the time while staying a usable console on demand.
- The reference art at `/Users/Fred/.codex/generated_images/01a03d69-8ca4-7763-8f5e-8af22970989c/exec-e845493a-810d-48aa-8ffa-f192f9e6053e.png` depicts a wireframe human figure inside a geodesic sphere with a radiant core and chakra-point glows down the spine — this is literal source truth for the "auric body" concept, not just mood reference. The system beacons are intentionally positioned to echo that chakra column.
- The auric texture is a camera-facing `THREE.Sprite`, not a fixed-orientation plane — needed so it doesn't break apart under orbit. Don't revert to a `Mesh`+`PlaneGeometry` for it.
- Bloom (`UnrealBloomPass`) is load-bearing for the "immersive glow" feel and for the auric texture's own glow points to read at all — but it's screen-space, so it does NOT scale down with camera distance the way real geometry does. Tuning it for a good close-up (Surface/Inward) will typically wash out the wide Orbit shot. Always re-check the wide Orbit composition (sphere geometry should stay legible, not just a light-blob) after touching bloom strength/radius/threshold or the sprite's `color.setScalar(...)` boost.

## Known issue: `ap.py truth-kernel` is very slow (found 2026-09-22)

The page was found stuck forever on "Loading institutional memory…" / "CONNECTING MEMORY". Root cause: `server/vault-data.mjs`'s `/api/truth-kernel/field` route shells out to `python3 .../08_SYSTEMS/Engineering Toolkit/ap.py truth-kernel …` on every request, and that command — which finished in 2.57s per the 2026-09-03 QA manifest (`.alpha-proxima/evidence/truth-kernel-2026-09-03/qa-manifest.json`) — now takes well over 90s even run standalone with no contention. The frontend originally required both `/api/vault/overview` (which loads fine, ~9s for ~800 notes) and the Truth Kernel to succeed before rendering anything, so one slow endpoint blocked the whole console.

Fixed here (scoped to keep the page usable, not to fix the underlying Python slowness):
- `App.jsx`: Vault and Truth Kernel are now fetched and polled independently. Vault-derived content (mission, attention, department objectives) renders as soon as the Vault overview resolves, regardless of Kernel state.
- `server/vault-data.mjs`: `/api/truth-kernel/field` builds are now cached (25s TTL) and de-duplicated (concurrent requests share one in-flight build) so the 30s frontend poll can't stack up overlapping `ap.py` subprocesses.

Not fixed / not investigated: why `ap.py truth-kernel` itself regressed from ~2.57s to 90s+. It was not simply a concurrency artifact — a single, uncontended standalone run also took over 90s. Two long-lived `ap.py office serve` / `ap.py app serve` processes were found already running against this same vault (one pair from today, one pair running for multiple days) — worth checking whether they hold a lock or resource `truth-kernel` also needs, but that's Engineering Toolkit / Python-side work, not something to poke at from this prototype without the Founder's go-ahead given those look like live services.

## Unified interface direction (2026-09-24)

The user requested one immersive, simple, iOS-friendly interface for both notes and project tracking. This copy is the Universe view embedded in the unified Vault application; its parent owns capture, projects, and document reading. Preserve Orbit / Surface / Inward and read the shared `/api/v1/app` contract. Do not restore a separate data source or pretend search executes agent actions.

## Reference direction (2026-09-28)
Use the supplied transparent floral body and cosmic neural column as the visual sources. Preserve void immersion and Orbit / Surface / Inward. Corps vivant and Réseau cosmique are visual layers over the same institutional data; they do not establish new dimensions of authority. Preserve source aspect ratios, dark space, cyan and rose detail. The supplied video guides luminous depth and peripheral information placement.

## Founder correction — true volume and working centers (2026-09-28)

The Founder explicitly rejected the camera-facing image, screen-crossing line and constrained orbit. This supersedes the earlier Sprite requirement. Use a volumetric humanoid with actual front/back/side geometry and one persistent interior field. Camera transitions occur only on explicit navigation; never pull the camera back every animation frame. Dragging must remain free. Inside mode enters the same model rather than substituting an unrelated tunnel.

Spatial anchor order: crown purple above head; third eye indigo between eyebrows; throat blue; heart green at sternum; solar plexus yellow just below sternum; sacral orange at navel; root red low in pelvis. These are presentation anchors, not medical claims or institutional authority.

Each center opens its department workspace. Explicit-owner data comes from the existing canonical API. Personal colleague/agent/tool shortcuts are browser-local links and must not claim authenticated integration, invitations, execution or sync. Real connector execution remains a separate implementation boundary.

## Higgsfield refinement (2026-09-28)
The Founder requested Higgsfield to refine the existing interface. Its botanical GLB is a decorative volume in the same body coordinates, with clear central chakra targets and separate organic/neural visibility. Preserve actual geometry and free camera navigation; do not replace the body with a rendered still or video. Keep the local unified app as the working entry.

## Gate of the Soul and full body rotation (2026-10-04)

This supersedes the previous sphere, orbital dashboard, embodiment switches and mannequin presentation. Keep the approved `alpha-hero-gold-v2.jpg` as the Gate's visual identity. Seven chakra vortex portals open distinct department interfaces in the same mounted Universe. The Founder explicitly requires a full 360-degree spatial body, with side and back geometry, manual rotation, 2D return, recenter, pause, reduced motion and a functional WebGL fallback. Project the accessible hit targets from the same coordinates as the rendered centers.

The current body surface is reconstructed from the reference silhouette with bounded depth. Its unseen profile and back are an interpretation, not an exact recovered model. Preserve source fidelity from the front and distinguish technical validation from Founder visual acceptance. Keep the canonical API and explicit-owner routing unchanged; hide/inert the parent iframe between routes so department and camera state survive.
