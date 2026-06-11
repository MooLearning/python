# ======================================================================
# 79 — Gradient Boosting  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Boosting residuals with stumps (1-D regression)
# ----------------------------------------------------------------------
print("\n--- Example 1: Boosting residuals with stumps (1-D regression) ---")
data = [(1, 1.0), (2, 1.5), (3, 3.5), (4, 4.2), (5, 6.0)]
xs = [x for x, _ in data]
ys = [y for _, y in data]

def best_stump(xs, residuals):
    # threshold that best predicts residuals by side means (min SSE)
    best = None
    for t in sorted(set(xs)):
        left = [r for x, r in zip(xs, residuals) if x <= t]
        right = [r for x, r in zip(xs, residuals) if x > t]
        if not left or not right:
            continue
        lm, rm = sum(left) / len(left), sum(right) / len(right)
        sse = sum((r - lm) ** 2 for r in left) + sum((r - rm) ** 2 for r in right)
        if best is None or sse < best[0]:
            best = (sse, t, lm, rm)
    return best

pred = [sum(ys) / len(ys)] * len(ys)     # start from the mean
lr = 0.5
for rnd in range(6):
    residuals = [y - p for y, p in zip(ys, pred)]
    _, t, lm, rm = best_stump(xs, residuals)
    pred = [p + lr * (lm if x <= t else rm) for x, p in zip(xs, pred)]
    mse = sum((y - p) ** 2 for y, p in zip(ys, pred)) / len(ys)
    print(f"round {rnd}: split@{t}, MSE={mse:.4f}")
print("final preds:", [round(p, 2) for p in pred])

# ----------------------------------------------------------------------
# Example 2: Why the learning rate matters
# ----------------------------------------------------------------------
print("\n--- Example 2: Why the learning rate matters ---")
# Same idea, compare a small vs large learning rate over a few rounds.
ys = [10, 12, 14, 16]
def boost(lr, rounds=5):
    pred = [sum(ys) / len(ys)] * len(ys)
    for _ in range(rounds):
        residuals = [y - p for y, p in zip(ys, pred)]
        # one global stump: just add the mean residual (toy weak learner)
        step = sum(residuals) / len(residuals)
        pred = [p + lr * step for p in pred]
    return sum((y - p) ** 2 for y, p in zip(ys, pred)) / len(ys)

for lr in [0.1, 0.5, 1.0]:
    print(f"lr={lr}: final MSE after 5 rounds = {boost(lr):.4f}")
# Smaller lr learns slower but is more robust; larger lr can overshoot.

# ----------------------------------------------------------------------
# Example 3: Gradient boosting with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Gradient boosting with scikit-learn ---")
try:
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split

    X, y = load_breast_cancer(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1,
                                    max_depth=3, random_state=0).fit(X_tr, y_tr)
    print("accuracy:", round(gb.score(X_te, y_te), 3))
    print("n_estimators:", gb.n_estimators_, "| lr:", gb.learning_rate)
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
