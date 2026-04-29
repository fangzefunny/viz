"""
Compatibility shim when the repo root is on sys.path (no pip install).

Prefer: pip install -e .  then  import viz

API matches the installed package: import viz; viz.violin(...), from viz import viz, etc.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_SRC = _ROOT / "src"
_STYLE = _SRC / "viz" / "style.py"

if not _STYLE.exists():
    raise ImportError("Could not find src/viz/style.py (package layout missing).")

_spec = importlib.util.spec_from_file_location("_viz_style", _STYLE)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Failed to load viz package module at {_STYLE}")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)  # type: ignore[attr-defined]

_Viz = _mod.viz
viz = _Viz


def __getattr__(name: str):
    return getattr(_Viz, name)


def __dir__() -> list[str]:
    extra = {n for n in dir(_Viz) if not n.startswith("_")}
    return sorted(set(globals().keys()) | extra)
