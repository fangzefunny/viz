# viz
The visualization methods I preferred 

## Install (from git)

### Regular install

```bash
pip install "git+https://github.com/fangzefunny/viz.git"
```

### Editable install (recommended for personal tweaks)

```bash
pip install -e "git+https://github.com/fangzefunny/viz.git#egg=zeming-viz"
```

### Upgrade the package

```bash
pip install --upgrade "git+https://github.com/fangzefunny/viz.git"
```

## Usage

```python
import viz

viz.get_style()
viz.violin(ax, data, x="x", y="y", order=[...], palette=viz.Palette)
```

The class is also available as `from viz import viz` (same object as `viz.viz` after `import viz`).
