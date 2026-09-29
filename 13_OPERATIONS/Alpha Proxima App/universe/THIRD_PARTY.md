---
title: "Alpha Proxima Universe Third Party Sources"
aliases: ["Universe Third Party Sources"]
tags: [operations, app, provenance, prototype]
created: 2026-09-28
updated: 2026-09-29
status: active
version: "1.0.0"
authors: ["CODEX"]
artifact_type: provenance-record
institutional_owner: "Engineering Office"
dependencies: ["[[Alpha Proxima App Architecture v1]]"]
related_documents: ["[[Alpha Proxima Unified Interface]]"]
related_research_programs: []
---

# Volumetric body source

`public/assets/auric-human.glb` is the Xbot model distributed in the official Three.js examples:
https://github.com/mrdoob/three.js/blob/dev/examples/models/gltf/Xbot.glb
Downloaded 2026-09-28 from the repository's raw file. The runtime uses its idle pose, bakes actual posed vertex positions, replaces the original materials and adds internal field geometry. It is a stylized humanoid, not a medical anatomical model or a reconstruction of the supplied photographs.

Supplied floral-body and neural-cosmos images remain unchanged as reference assets. They are no longer used as the body's render geometry.

## Botanical volume (Higgsfield)
`public/assets/higgsfield-botanical.glb` is a procedural mesh created for this task with Higgsfield 3D Jutsu. The editable construction script is `design/higgsfield-botanical.py`; project: https://higgsfield.ai/3d-jutsu/7c823903-c97c-48c7-b424-1b29fe8f5b1f. No third-party images or textures are embedded. The user's supplied floral body and neural artwork guided the visual direction.
