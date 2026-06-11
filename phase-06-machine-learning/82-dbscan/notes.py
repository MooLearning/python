# ======================================================================
# 82 — DBSCAN  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: DBSCAN from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: DBSCAN from scratch ---")
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

# ----------------------------------------------------------------------
# Example 2: Classifying core / border / noise points
# ----------------------------------------------------------------------
print("\n--- Example 2: Classifying core / border / noise points ---")
import math

points = [(0, 0), (0.5, 0), (1, 0), (5, 5)]
eps, min_pts = 1.0, 3

def neighbor_count(i):
    return sum(1 for j in range(len(points)) if math.dist(points[i], points[j]) <= eps)

for i, p in enumerate(points):
    c = neighbor_count(i)
    role = "core" if c >= min_pts else "non-core"
    print(f"{p}: {c} neighbors -> {role}")
# Non-core points near a core become 'border'; isolated ones are 'noise'.

# ----------------------------------------------------------------------
# Example 3: DBSCAN with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: DBSCAN with scikit-learn ---")
try:
    from sklearn.cluster import DBSCAN
    from sklearn.datasets import make_moons

    X, _ = make_moons(n_samples=150, noise=0.06, random_state=0)
    db = DBSCAN(eps=0.2, min_samples=5).fit(X)
    labels = db.labels_
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)
    print("clusters found:", n_clusters)      # ~2 crescent shapes
    print("noise points  :", n_noise)
    print("first 10 labels:", labels[:10].tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
