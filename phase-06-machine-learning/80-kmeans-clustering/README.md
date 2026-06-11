# 80 — K-Means Clustering

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**K-Means** is an **unsupervised** algorithm that partitions data into **k clusters**. It alternates two steps until stable: **assign** each point to the nearest **centroid**, then **update** each centroid to the mean of its assigned points. It minimizes within-cluster variance (**inertia**). You choose k (e.g. via the **elbow method**).

## Why it matters

Clustering finds natural groups without labels — customer segmentation, image color quantization, anomaly grouping, document topics. K-Means is the fast, simple default and teaches the assign/update (EM-style) pattern.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Centroid** — The mean point of a cluster.
- **Assignment step** — Put each point in the nearest centroid's cluster.
- **Update step** — Move each centroid to its cluster's mean.
- **Inertia (WCSS)** — Sum of squared distances to centroids — lower is tighter.
- **Elbow method** — Plot inertia vs k; the 'elbow' suggests a good k.
- **k-means++** — Smart centroid initialization for better, faster convergence.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import random, math
random.seed(0)

points = [(1, 1), (1.5, 2), (1, 0.5),
          (8, 8), (9, 8), (8.5, 9),
          (1, 8), (1.5, 8.5)]

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def kmeans(points, k, iterations=20):
    centroids = random.sample(points, k)         # random init
    for _ in range(iterations):
        # ASSIGN each point to its nearest centroid
        clusters = [[] for _ in range(k)]
        for p in points:
            nearest = min(range(k), key=lambda i: dist(p, centroids[i]))
            clusters[nearest].append(p)
        # UPDATE centroids to cluster means
        new = []
        for i, cluster in enumerate(clusters):
            if cluster:
                cx = sum(p[0] for p in cluster) / len(cluster)
                cy = sum(p[1] for p in cluster) / len(cluster)
                new.append((cx, cy))
            else:
                new.append(centroids[i])
        if new == centroids:                     # converged
            break
        centroids = new
    return centroids, clusters

centroids, clusters = kmeans(points, k=3)
for i, (c, cl) in enumerate(zip(centroids, clusters)):
    print(f"cluster {i}: centroid={tuple(round(v,2) for v in c)}, points={cl}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ You must choose k in advance; the elbow/silhouette methods help estimate it.
- ⚠️ Results depend on random init — run multiple times (k-means++ / n_init) and keep the best.
- ⚠️ K-Means assumes spherical, similar-size clusters; it fails on elongated/odd shapes.
- ⚠️ Unscaled features distort distances — standardize first.
- ⚠️ Outliers pull centroids; consider removing them or using k-medoids.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

