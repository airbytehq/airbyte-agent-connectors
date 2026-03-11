"""Shared test configuration for generate_skill_references tests."""

from __future__ import annotations

import sys
from pathlib import Path

# Make the scripts directory importable so tests can
# ``from generate_skill_references import ...`` without sys.path hacks
# in every test module.
REPO_ROOT = Path(__file__).resolve().parent.parent
_scripts_dir = str(REPO_ROOT / "scripts")
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)
