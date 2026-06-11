# ======================================================================
# 88 — Regularization (L1, L2)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: L2 regularization shrinks weights (gradient descent)
# ----------------------------------------------------------------------
print("\n--- Example 1: L2 regularization shrinks weights (gradient descent) ---")
# Target depends only on feature 1; feature 2 is irrelevant noise.
data = [([1, 2], 2.0), ([2, 1], 4.0), ([3, 0], 6.0),
        ([4, 3], 8.0), ([5, 1], 10.0)]

def train(lam, epochs=2000, lr=0.01):
    w = [0.0, 0.0]
    for _ in range(epochs):
        gw = [0.0, 0.0]
        for x, y in data:
            pred = w[0] * x[0] + w[1] * x[1]
            err = pred - y
            for j in range(2):
                gw[j] += 2 * err * x[j]
        # add the L2 penalty gradient: d/dw (lam * w^2) = 2*lam*w
        for j in range(2):
            gw[j] = gw[j] / len(data) + 2 * lam * w[j]
            w[j] -= lr * gw[j]
    return w

for lam in [0.0, 0.1, 1.0, 5.0]:
    w = train(lam)
    print(f"lambda={lam:4}: weights = [{w[0]:.3f}, {w[1]:.3f}]")
# As lambda grows, BOTH weights shrink toward 0 (especially the noise feature).

# ----------------------------------------------------------------------
# Example 2: L1 vs L2: sparsity via soft-thresholding
# ----------------------------------------------------------------------
print("\n--- Example 2: L1 vs L2: sparsity via soft-thresholding ---")
# L1's effect on a single weight is 'soft-thresholding': small weights -> 0.
def soft_threshold(w, lam):
    if w > lam:   return w - lam
    if w < -lam:  return w + lam
    return 0.0                       # |w| <= lam gets zeroed (sparsity!)

for w in [-2.0, -0.3, 0.0, 0.4, 1.5]:
    print(f"w={w:5} -> L1(lam=0.5) -> {soft_threshold(w, 0.5)}")
print("Small weights snap to exactly 0 -> L1 selects features.")
print("L2 would only shrink them proportionally, never exactly to 0.")

# ----------------------------------------------------------------------
# Example 3: Ridge and Lasso with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Ridge and Lasso with scikit-learn ---")
try:
    from sklearn.linear_model import Ridge, Lasso, LinearRegression
    from sklearn.datasets import make_regression

    X, y = make_regression(n_samples=80, n_features=8, n_informative=3,
                           noise=10, random_state=0)

    lr = LinearRegression().fit(X, y)
    ridge = Ridge(alpha=10).fit(X, y)
    lasso = Lasso(alpha=10).fit(X, y)

    print("plain coef (abs sum):", round(sum(abs(c) for c in lr.coef_), 1))
    print("ridge coef (abs sum):", round(sum(abs(c) for c in ridge.coef_), 1))
    print("lasso zeros          :", int(sum(1 for c in lasso.coef_ if abs(c) < 1e-6)),
          "of", len(lasso.coef_), "features set to 0")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
