# 74 — K-Nearest Neighbors (KNN)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**K-Nearest Neighbors (KNN)** is a simple, **instance-based** algorithm: to classify a new point, find the **k** closest training points (by a distance like Euclidean) and take a **majority vote** (or average, for regression). There's no real 'training' — it just stores the data and computes distances at prediction time (a 'lazy learner').

## Why it matters

KNN is intuitive, needs no training, and works as a strong baseline. It teaches the importance of distance metrics, feature scaling, and the choice of k — concepts that recur throughout ML.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Distance** — Euclidean (or Manhattan/cosine) measures closeness.
- **k neighbors** — How many nearest points vote; odd k avoids ties.
- **Majority vote** — Classification: most common label among neighbors.
- **Averaging** — Regression: mean of neighbors' target values.
- **Lazy learning** — No model is fit; all work happens at prediction time.
- **Scaling matters** — Features must be scaled or large-range ones dominate distance.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math
from collections import Counter

# training points: (features, label)
train = [
    ((1, 1), "A"), ((1, 2), "A"), ((2, 1), "A"),
    ((6, 6), "B"), ((7, 7), "B"), ((6, 7), "B"),
]

def euclidean(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))

def knn_predict(point, k=3):
    # sort training points by distance to the query point
    distances = sorted(train, key=lambda item: euclidean(point, item[0]))
    neighbors = [label for _, label in distances[:k]]
    return Counter(neighbors).most_common(1)[0][0]

print("(2,2) ->", knn_predict((2, 2)))    # A (near the A cluster)
print("(6,5) ->", knn_predict((6, 5)))    # B (near the B cluster)
print("(4,4) ->", knn_predict((4, 4)))    # depends on k / ties
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Unscaled features wreck KNN — a feature in thousands dominates one in fractions. Scale first.
- ⚠️ Small k overfits (sensitive to noise); large k oversmooths. Tune it (often odd).
- ⚠️ Prediction is O(n) per query — slow on big datasets (no precomputed model).
- ⚠️ The curse of dimensionality: distances become meaningless with many features.
- ⚠️ Ties in voting need a rule (reduce k, weight by distance, or pick lowest label).

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

