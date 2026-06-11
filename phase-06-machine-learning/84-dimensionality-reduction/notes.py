# ======================================================================
# 84 — Dimensionality Reduction (t-SNE)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Variance-threshold feature selection (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: Variance-threshold feature selection (pure Python) ---")
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

# ----------------------------------------------------------------------
# Example 2: Simple linear projection to fewer dimensions
# ----------------------------------------------------------------------
print("\n--- Example 2: Simple linear projection to fewer dimensions ---")
# Keep the two highest-variance features as a crude 4-D -> 2-D reduction
import statistics as st

samples = [[1, 9, 2, 8], [2, 1, 2, 7], [3, 8, 2, 9], [4, 2, 2, 6]]
cols = list(zip(*samples))
variances = [(i, st.pvariance(c)) for i, c in enumerate(cols)]
top2 = [i for i, _ in sorted(variances, key=lambda t: -t[1])[:2]]
print("top-2 variance feature indices:", sorted(top2))

projected = [[row[i] for i in sorted(top2)] for row in samples]
print("projected to 2-D:")
for p in projected:
    print(" ", p)

# ----------------------------------------------------------------------
# Example 3: t-SNE and PCA with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: t-SNE and PCA with scikit-learn ---")
try:
    from sklearn.datasets import load_digits
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE

    X, y = load_digits(return_X_y=True)       # 64-dimensional (8x8 images)
    print("original dimensions:", X.shape[1])

    # PCA: fast linear reduction to 2-D
    X_pca = PCA(n_components=2, random_state=0).fit_transform(X)
    print("PCA 2-D first point:", X_pca[0].round(2).tolist())

    # t-SNE: slower, non-linear, great for visualization (subset for speed)
    X_tsne = TSNE(n_components=2, perplexity=30,
                  init="pca", random_state=0).fit_transform(X[:300])
    print("t-SNE 2-D first point:", X_tsne[0].round(2).tolist())
    print("reduced to 2-D for plotting clusters of digits 0-9")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
