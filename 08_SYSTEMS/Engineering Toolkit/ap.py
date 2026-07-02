#!/usr/bin/env python3
"""Unified Alpha Proxima Engineering CLI."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parent
COMMANDS = {
    "validate": ("vault_validator.py", "Run the Vault Validator"),
    "yaml": ("yaml_validator.py", "Run the YAML Validator"),
    "stats": ("vault_statistics.py", "Generate the Engineering Dashboard Report"),
    "migrate": ("metadata_migrator.py", "Plan or apply metadata migration"),
    "report": ("vault_statistics.py", "Alias for stats"),
    "office-check": ("office_integrity_checker.py", "Generate the Office Integrity Report"),
    "research-check": ("research_integrity_checker.py", "Generate the Research Integrity Report"),
    "dependency-map": ("dependency_analyzer.py", "Generate the Vault Dependency Report"),
}


def load_tool(filename: str):
    path = TOOLKIT_DIR / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load tool: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=sorted(COMMANDS), help="Toolkit command to run.")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments passed to the selected command.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    filename, _ = COMMANDS[args.command]
    module = load_tool(filename)
    return int(module.main(args.args))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
