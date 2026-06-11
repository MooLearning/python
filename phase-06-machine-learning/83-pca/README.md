# 83 — Principal Component Analysis (PCA)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Principal Component Analysis (PCA)** reduces dimensionality by finding new axes (**principal components**) along which the data varies most. PC1 captures the most variance, PC2 the next (orthogonal to PC1), and so on. Projecting onto the top few components compresses the data while keeping most of its structure. Mechanically: center the data, compute the **covariance matrix**, and take its top **eigenvectors**.

## Why it matters

PCA fights the curse of dimensionality, speeds up models, removes correlated/redundant features, and enables 2-D visualization of high-dimensional data — a standard preprocessing and exploration tool.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Principal component** — A direction of maximum variance in the data.
- **Center the data** — Subtract the mean so PCA measures variance about 0.
- **Covariance matrix** — Captures how features vary together.
- **Eigenvectors/values** — Directions (components) and how much variance each holds.
- **Explained variance** — Fraction of total variance kept by each component.
- **Projection** — Map points onto the chosen components (the new coordinates).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

# Data that mostly varies along the diagonal (x ~ y)
data = [(2, 2.1), (3, 2.9), (4, 4.2), (5, 4.8), (6, 6.1), (1, 1.1)]

n = len(data)
mx = sum(p[0] for p in data) / n
my = sum(p[1] for p in data) / n
centered = [(x - mx, y - my) for x, y in data]      # center

# Covariance matrix [[a, b], [b, d]] (population)
a = sum(x * x for x, y in centered) / n
d = sum(y * y for x, y in centered) / n
b = sum(x * y for x, y in centered) / n

# Eigenvalues of a symmetric 2x2 matrix
tr, det = a + d, a * d - b * b
disc = math.sqrt((tr / 2) ** 2 - det)
l1, l2 = tr / 2 + disc, tr / 2 - disc

# Top eigenvector (principal component) for l1: v = (b, l1 - a), normalized
vx, vy = b, l1 - a
norm = math.hypot(vx, vy)
pc1 = (vx / norm, vy / norm)
print("PC1 direction:", tuple(round(v, 3) for v in pc1))   # ~(0.707, 0.707)
print("explained variance ratio:", round(l1 / (l1 + l2), 4))

# Project the centered points onto PC1 (the 1-D compressed coordinate)
proj = [round(x * pc1[0] + y * pc1[1], 3) for x, y in centered]
print("projected (1-D):", proj)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Always standardize features first — PCA chases variance, so large-scale features dominate.
- ⚠️ PCA components are linear combinations — they lose direct interpretability.
- ⚠️ It only captures LINEAR structure; use t-SNE/UMAP/kernel PCA for non-linear manifolds.
- ⚠️ Don't fit PCA on test data — fit on train, then transform test with the same components.
- ⚠️ Reducing too aggressively discards useful signal; check cumulative explained variance.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

