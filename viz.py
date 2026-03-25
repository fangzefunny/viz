"""
Compatibility shim.

Prefer importing from the installed package:
  from viz import viz
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_SRC = _ROOT / "src"
_STYLE = _SRC / "viz" / "style.py"

if _STYLE.exists():
    _spec = importlib.util.spec_from_file_location("_viz_style", _STYLE)
    if _spec is None or _spec.loader is None:
        raise ImportError(f"Failed to load viz package module at {_STYLE}")
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)  # type: ignore[attr-defined]
    viz = _mod.viz
else:
    raise ImportError("Could not find src/viz/style.py (package layout missing).")

