# 82 — DBSCAN

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) groups points that are **densely packed** and labels sparse points as **noise**. Two parameters: **eps** (the neighborhood radius) and **min_pts** (how many neighbors make a **core point**). It finds **arbitrarily shaped** clusters and the number of clusters **automatically** — unlike K-Means.

## Why it matters

DBSCAN handles non-spherical clusters, doesn't need k, and explicitly detects outliers — ideal for spatial data, anomaly detection, and messy real-world data where K-Means fails.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **eps** — Radius defining a point's neighborhood.
- **min_pts** — Minimum neighbors (incl. self) to be a core point.
- **Core point** — Has ≥ min_pts neighbors within eps.
- **Border point** — Within eps of a core point but not core itself.
- **Noise** — Neither core nor border — an outlier.
- **No preset k** — Cluster count emerges from the density structure.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

points = [(1, 1), (1.2, 1.1), (0.8, 1.0),      # dense cluster 0
          (8, 8), (8.1, 8.2),                   # dense cluster 1
          (5, 5)]                               # lone noise point
eps, min_pts = 1.0, 2

def neighbors(i):
    return [j for j in range(len(points)) if math.dist(points[i], points[j]) <= eps]

labels = [None] * len(points)     # None=unvisited, -1=noise, >=0 cluster id
cluster_id = 0
for i in range(len(points)):
    if labels[i] is not None:
        continue
    nbrs = neighbors(i)
    if len(nbrs) < min_pts:
        labels[i] = -1            # provisionally noise
        continue
    labels[i] = cluster_id        # start a new cluster
    seeds = list(nbrs)
    k = 0
    while k < len(seeds):
        j = seeds[k]
        if labels[j] == -1:
            labels[j] = cluster_id            # border point
        elif labels[j] is None:
            labels[j] = cluster_id
            j_nbrs = neighbors(j)
            if len(j_nbrs) >= min_pts:         # j is core -> expand
                seeds += j_nbrs
        k += 1
    cluster_id += 1

for p, lab in zip(points, labels):
    kind = "noise" if lab == -1 else f"cluster {lab}"
    print(f"{p} -> {kind}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ DBSCAN is very sensitive to eps — too small = all noise, too big = one blob.
- ⚠️ It struggles when clusters have very different densities (one eps can't fit all).
- ⚠️ Distance-based, so scale features first; high dimensions weaken density estimates.
- ⚠️ Border points can be assigned to whichever core reaches them first (order-dependent).
- ⚠️ Pick min_pts ≈ dimensions + 1 (or more); eps via a k-distance plot.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

