"""Atomic JSON replacement for the existing state owners; no new state store.

This protects readers from truncated JSON. It does not serialize a complete
read/modify/write transaction or prevent lost updates from concurrent writers.
The file is fsynced before replacement; directory-entry durability after power
loss is not guaranteed by this helper.
"""
from __future__ import annotations

import json
import os
import stat
import tempfile
from pathlib import Path
from typing import Any


def write_json_atomic(path: Path, value: Any) -> None:
    """Publish one complete JSON snapshot, retaining the old file on precommit failure."""
    payload = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    # Preserve the previous writer's behavior for a symlinked state path.
    target = path.resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(target.stat().st_mode) if target.exists() else 0o600
    descriptor, temporary = tempfile.mkstemp(prefix=f".{target.name}.", suffix=".tmp", dir=target.parent)
    scratch = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            os.chmod(scratch, mode)
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(scratch, target)
    finally:
        if scratch.exists():
            scratch.unlink()
