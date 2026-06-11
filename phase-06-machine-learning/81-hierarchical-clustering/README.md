# 81 — Hierarchical Clustering

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Hierarchical clustering** builds a tree of clusters (a **dendrogram**). The common **agglomerative** approach starts with each point as its own cluster and repeatedly **merges the two closest clusters** until one remains. 'Closest' depends on a **linkage**: single (min distance), complete (max), or average. You cut the dendrogram at a height to get any number of clusters — no need to pre-specify k.

## Why it matters

It reveals nested structure and relationships at multiple scales, doesn't require choosing k up front, and the dendrogram is a great visualization. Used in genomics, document organization, and taxonomy.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Agglomerative** — Bottom-up: start with singletons, merge upward.
- **Linkage** — How to measure cluster distance: single/complete/average/ward.
- **Dendrogram** — Tree diagram of the merge order and heights.
- **Cut height** — Slice the tree to choose the number of clusters.
- **No preset k** — Decide clusters after seeing the structure.
- **Distance matrix** — Pairwise distances drive the merges.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

pts = {"A": (1, 1), "B": (1.5, 1.5), "C": (5, 5), "D": (5.5, 5), "E": (9, 9)}

def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def single_linkage(c1, c2):
    return min(dist(pts[a], pts[b]) for a in c1 for b in c2)

clusters = [[name] for name in pts]      # each point starts alone
while len(clusters) > 1:
    # find the two closest clusters
    best = None
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            d = single_linkage(clusters[i], clusters[j])
            if best is None or d < best[0]:
                best = (d, i, j)
    d, i, j = best
    print(f"merge {clusters[i]} + {clusters[j]}  (distance {d:.2f})")
    clusters[i] = clusters[i] + clusters[j]
    del clusters[j]
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Naive agglomerative clustering is O(n³)/O(n²) — too slow for very large datasets.
- ⚠️ Linkage choice changes results: single linkage 'chains', complete makes compact clusters.
- ⚠️ Scale features first — distances drive every merge.
- ⚠️ Once merged, clusters can't be split — early mistakes propagate (greedy).
- ⚠️ Reading a dendrogram: the merge HEIGHT is the distance, not the horizontal position.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

