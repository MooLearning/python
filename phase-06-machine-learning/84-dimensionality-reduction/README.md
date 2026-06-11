# 84 — Dimensionality Reduction (t-SNE)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Dimensionality reduction** compresses many features into fewer while preserving structure. **PCA** does this linearly (max variance). **t-SNE** and **UMAP** are non-linear techniques tuned for **visualization**: they place similar points near each other in 2-D/3-D, revealing clusters. Simpler approaches include **feature selection** (drop low-variance or redundant features).

## Why it matters

Fewer dimensions mean faster training, less overfitting, smaller storage, and — crucially — the ability to SEE high-dimensional data in a 2-D scatter, which is invaluable for understanding clusters and class separation.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Curse of dimensionality** — Distances blur and data sparsifies as dimensions grow.
- **Feature selection** — Keep a subset of original features (e.g. by variance).
- **Feature extraction** — Build new combined features (PCA components).
- **t-SNE / UMAP** — Non-linear methods that preserve local neighborhoods for plots.
- **Linear vs non-linear** — PCA = linear; t-SNE/UMAP capture curved manifolds.
- **For viz, not modeling** — t-SNE coordinates aren't meant as model features.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import statistics as st

# 4 features across 5 samples; feature 2 (index 2) barely varies
samples = [
    [1.0, 5.0, 3.0, 100],
    [2.0, 6.0, 3.0, 220],
    [3.0, 4.0, 3.0, 150],
    [4.0, 7.0, 3.1, 300],
    [5.0, 5.0, 3.0, 180],
]
cols = list(zip(*samples))
variances = [st.pvariance(c) for c in cols]
print("variances:", [round(v, 3) for v in variances])

threshold = 0.1
keep = [i for i, v in enumerate(variances) if v > threshold]
print("keep feature indices:", keep)       # drops the near-constant feature 2
reduced = [[row[i] for i in keep] for row in samples]
print("reduced first row:", reduced[0])
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ t-SNE is for VISUALIZATION — don't feed its 2-D output into a model as features.
- ⚠️ t-SNE distances/cluster sizes aren't meaningful globally; only local neighborhoods are.
- ⚠️ t-SNE is sensitive to 'perplexity' and random seed — try a few settings.
- ⚠️ Reduce after scaling, and fit the reducer on train only to avoid leakage.
- ⚠️ Aggressive reduction can destroy signal — validate that downstream accuracy holds.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

