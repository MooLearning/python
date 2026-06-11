# 63 — Matplotlib

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Matplotlib** is the foundational plotting library for Python. Its `pyplot` interface draws line plots, bar charts, scatter plots, histograms, and more. You build a figure, add data and labels, then show or save it. Almost every other Python viz tool (including seaborn and pandas `.plot`) sits on top of matplotlib.

## Why it matters

Visualization is how you understand data and communicate results. A quick plot reveals trends, outliers, and distributions that raw numbers hide — an essential step in EDA and model evaluation.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install matplotlib
```

## Key concepts

- **Figure & Axes** — The canvas (figure) holds one or more plots (axes).
- **plot / scatter / bar / hist** — The common chart types.
- **Labels & title** — xlabel, ylabel, title, legend make plots readable.
- **savefig vs show** — Save to a file (headless) or display interactively.
- **Backends** — Use the 'Agg' backend to render without a screen.
- **Subplots** — Multiple axes in one figure with plt.subplots.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
try:
    import matplotlib
    matplotlib.use("Agg")                 # render without a display
    import matplotlib.pyplot as plt
    import tempfile, os

    x = [0, 1, 2, 3, 4, 5]
    y = [v ** 2 for v in x]               # y = x^2

    plt.figure(figsize=(5, 3))
    plt.plot(x, y, marker="o", label="y = x^2")
    plt.title("Line Plot")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend(); plt.grid(True)

    out = os.path.join(tempfile.gettempdir(), "line_plot.png")
    plt.savefig(out, dpi=80); plt.close()
    print("saved line plot ->", out)
except ImportError:
    print("matplotlib not installed — run: pip install matplotlib")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ On a headless server, set `matplotlib.use('Agg')` BEFORE importing pyplot, or it may error.
- ⚠️ Call `plt.close()` after saving in loops, or figures pile up and leak memory.
- ⚠️ `plt.show()` blocks until you close the window; use `savefig` in scripts/notebooks.
- ⚠️ Re-plotting onto the same figure overlays data — start a new `plt.figure()` each chart.
- ⚠️ Set labels/titles BEFORE savefig/show; adding them after rendering has no effect.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

