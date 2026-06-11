# ======================================================================
# 75 — Support Vector Machines (SVM)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: A linear separator: classify by the sign of w·x + b
# ----------------------------------------------------------------------
print("\n--- Example 1: A linear separator: classify by the sign of w·x + b ---")
# A hand-chosen boundary: x + y - 5 = 0. Sign tells the side/class.
def classify(point, w=(1, 1), b=-5):
    score = sum(wi * xi for wi, xi in zip(w, point)) + b
    return 1 if score >= 0 else 0, round(score, 2)

for p in [(1, 1), (4, 4), (3, 2), (5, 5)]:
    label, score = classify(p)
    print(f"{p}: score={score:5} -> class {label}")
# The 'margin' is how far points sit from score == 0.

# ----------------------------------------------------------------------
# Example 2: A perceptron learns a separating line (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 2: A perceptron learns a separating line (pure Python) ---")
# Linearly separable data: class -1 (lower-left) vs +1 (upper-right)
data = [((1, 1), -1), ((2, 1), -1), ((1, 2), -1),
        ((5, 5),  1), ((6, 5),  1), ((5, 6),  1)]

w = [0.0, 0.0]
b = 0.0
lr = 0.1
for epoch in range(20):
    errors = 0
    for (x1, x2), y in data:
        score = w[0] * x1 + w[1] * x2 + b
        pred = 1 if score >= 0 else -1
        if pred != y:                       # update on mistakes
            w[0] += lr * y * x1
            w[1] += lr * y * x2
            b += lr * y
            errors += 1
    if errors == 0:                         # converged: perfectly separated
        print(f"converged at epoch {epoch}")
        break

print("weights:", [round(v, 2) for v in w], "bias:", round(b, 2))
test = (4, 4)
print(f"{test} ->", 1 if w[0]*4 + w[1]*4 + b >= 0 else -1)

# ----------------------------------------------------------------------
# Example 3: SVM with scikit-learn: linear vs RBF kernel
# ----------------------------------------------------------------------
print("\n--- Example 3: SVM with scikit-learn: linear vs RBF kernel ---")
try:
    from sklearn.svm import SVC
    from sklearn.datasets import make_circles, make_classification
    from sklearn.model_selection import train_test_split

    # Linearly separable-ish data
    X, y = make_classification(n_samples=200, n_features=2, n_redundant=0,
                               n_informative=2, random_state=1)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)
    lin = SVC(kernel="linear", C=1.0).fit(X_tr, y_tr)
    print("linear kernel acc:", round(lin.score(X_te, y_te), 3))
    print("support vectors:", lin.n_support_.tolist())

    # Concentric circles: NOT linearly separable -> RBF wins
    Xc, yc = make_circles(n_samples=200, noise=0.1, factor=0.4, random_state=0)
    Xc_tr, Xc_te, yc_tr, yc_te = train_test_split(Xc, yc, test_size=0.3, random_state=0)
    print("RBF on circles  :", round(SVC(kernel="rbf").fit(Xc_tr, yc_tr).score(Xc_te, yc_te), 3))
    print("linear on circles:", round(SVC(kernel="linear").fit(Xc_tr, yc_tr).score(Xc_te, yc_te), 3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
