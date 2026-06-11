# ======================================================================
# 81 — Hierarchical Clustering  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Agglomerative single-linkage from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: Agglomerative single-linkage from scratch ---")
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

# ----------------------------------------------------------------------
# Example 2: Cutting the tree to get k clusters
# ----------------------------------------------------------------------
print("\n--- Example 2: Cutting the tree to get k clusters ---")
import math

pts = {"A": (1, 1), "B": (1.5, 1.5), "C": (5, 5), "D": (5.5, 5), "E": (9, 9)}
def dist(a, b): return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))
def linkage(c1, c2): return min(dist(pts[a], pts[b]) for a in c1 for b in c2)

def cluster_until(k):
    clusters = [[n] for n in pts]
    while len(clusters) > k:              # stop once we have k clusters
        best = None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                d = linkage(clusters[i], clusters[j])
                if best is None or d < best[0]:
                    best = (d, i, j)
        _, i, j = best
        clusters[i] += clusters[j]
        del clusters[j]
    return clusters

print("2 clusters:", cluster_until(2))
print("3 clusters:", cluster_until(3))

# ----------------------------------------------------------------------
# Example 3: Hierarchical clustering with scikit-learn / SciPy
# ----------------------------------------------------------------------
print("\n--- Example 3: Hierarchical clustering with scikit-learn / SciPy ---")
try:
    from sklearn.cluster import AgglomerativeClustering
    X = [[1, 1], [1.5, 1.5], [5, 5], [5.5, 5], [9, 9]]
    model = AgglomerativeClustering(n_clusters=2, linkage="single").fit(X)
    print("sklearn labels:", model.labels_.tolist())

    try:
        from scipy.cluster.hierarchy import linkage, fcluster
        Z = linkage(X, method="single")       # the linkage matrix
        print("scipy 2-cluster labels:", fcluster(Z, t=2, criterion="maxclust").tolist())
    except ImportError:
        print("scipy not installed — pip install scipy for dendrograms")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn scipy")

print("\nDone! Tip: change values above and run again to learn by experiment.")
