# ======================================================================
# 83 — Principal Component Analysis (PCA)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: PCA on 2-D data from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: PCA on 2-D data from scratch ---")
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

# ----------------------------------------------------------------------
# Example 2: Explained variance across components
# ----------------------------------------------------------------------
print("\n--- Example 2: Explained variance across components ---")
# Suppose eigenvalues (variances) of components came out as:
eigenvalues = [4.0, 1.0, 0.4, 0.1]
total = sum(eigenvalues)

print("explained variance ratios:")
cumulative = 0.0
for i, ev in enumerate(eigenvalues, 1):
    ratio = ev / total
    cumulative += ratio
    print(f"  PC{i}: {ratio:.1%}  (cumulative {cumulative:.1%})")

# Keep enough components to reach 90% of the variance
keep = 0
cumulative = 0.0
for ev in eigenvalues:
    keep += 1
    cumulative += ev / total
    if cumulative >= 0.90:
        break
print(f"-> keep {keep} components to retain >=90% variance")

# ----------------------------------------------------------------------
# Example 3: PCA with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: PCA with scikit-learn ---")
try:
    from sklearn.decomposition import PCA
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler

    X, y = load_iris(return_X_y=True)
    X_scaled = StandardScaler().fit_transform(X)    # scale before PCA

    pca = PCA(n_components=2).fit(X_scaled)
    X_2d = pca.transform(X_scaled)
    print("original shape:", X.shape, "-> reduced:", X_2d.shape)
    print("explained variance ratio:", pca.explained_variance_ratio_.round(3).tolist())
    print("total kept:", round(pca.explained_variance_ratio_.sum(), 3))
    print("first point in 2-D:", X_2d[0].round(3).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
