# 64 — Seaborn

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Seaborn** is a high-level statistical visualization library built on matplotlib. It makes attractive, informative plots with one line — histograms with KDE, box/violin plots, scatter plots with regression lines, and **correlation heatmaps** — and works directly with pandas DataFrames. It handles styling and color palettes for you.

## Why it matters

Seaborn turns common statistical charts into one-liners and looks great by default, so it's the fastest way to explore relationships and distributions during EDA without fiddling with matplotlib boilerplate.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install seaborn
```

## Key concepts

- **Built on matplotlib** — Returns matplotlib Axes you can further tweak.
- **DataFrame-aware** — Pass `data=df` and column names to x/y/hue.
- **histplot / kdeplot** — Distribution of a single variable.
- **boxplot / violinplot** — Compare distributions across categories.
- **scatterplot / regplot** — Relationships, optionally with a fitted line.
- **heatmap** — Visualize a matrix (e.g. correlations) with color.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
try:
    import matplotlib
    matplotlib.use("Agg")
    import seaborn as sns
    import matplotlib.pyplot as plt
    import tempfile, os, random

    random.seed(0)
    data = [random.gauss(0, 1) for _ in range(500)]

    sns.set_theme()                       # apply seaborn styling
    ax = sns.histplot(data, kde=True, bins=20)
    ax.set_title("Distribution with KDE")
    out = os.path.join(tempfile.gettempdir(), "sns_dist.png")
    plt.savefig(out, dpi=80); plt.close()
    print("saved distribution plot ->", out)
except ImportError:
    print("seaborn not installed — run: pip install seaborn")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Seaborn needs matplotlib; on headless systems set the 'Agg' backend before importing pyplot.
- ⚠️ Pass tidy/long-form DataFrames (one observation per row) for most seaborn functions.
- ⚠️ Seaborn functions return a matplotlib Axes — save/show with plt, not a seaborn call.
- ⚠️ `sns.set_theme()` changes global matplotlib styling for the rest of the session.
- ⚠️ Heatmaps need numeric matrices; call `df.corr()` (numeric columns only) first.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

