from .style import viz as _Viz

# `from viz import viz` — the styling class
viz = _Viz


def __getattr__(name: str):
    return getattr(_Viz, name)


def __dir__() -> list[str]:
    extra = {n for n in dir(_Viz) if not n.startswith("_")}
    return sorted(set(globals().keys()) | extra)
