# ======================================================================
# 80 — K-Means Clustering  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: K-Means from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: K-Means from scratch ---")
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

# ----------------------------------------------------------------------
# Example 2: Inertia and the elbow method
# ----------------------------------------------------------------------
print("\n--- Example 2: Inertia and the elbow method ---")
import random, math
random.seed(0)
points = [(1, 1), (1.5, 2), (1, 0.5), (8, 8), (9, 8), (8.5, 9)]

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def kmeans_inertia(points, k, iters=20):
    centroids = random.sample(points, k)
    clusters = [[] for _ in range(k)]
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        for p in points:
            i = min(range(k), key=lambda j: dist(p, centroids[j]))
            clusters[i].append(p)
        centroids = [(sum(q[0] for q in c)/len(c), sum(q[1] for q in c)/len(c))
                     if c else centroids[i] for i, c in enumerate(clusters)]
    inertia = sum(dist(p, centroids[i]) ** 2
                  for i, c in enumerate(clusters) for p in c)
    return inertia

for k in range(1, 5):
    print(f"k={k}: inertia={kmeans_inertia(points, k):.2f}")
# Inertia drops sharply then levels off — the 'elbow' hints at the best k (2 here).

# ----------------------------------------------------------------------
# Example 3: K-Means with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: K-Means with scikit-learn ---")
try:
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs

    X, _ = make_blobs(n_samples=150, centers=3, random_state=0)
    km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
    print("inertia:", round(km.inertia_, 2))
    print("centroids:\n", km.cluster_centers_.round(2))
    print("first 10 labels:", km.labels_[:10].tolist())
    print("predict new point:", km.predict([[0, 0]]).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
