# ======================================================================
# 73 — Logistic Regression  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: The sigmoid function and probabilities
# ----------------------------------------------------------------------
print("\n--- Example 1: The sigmoid function and probabilities ---")
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

for z in [-4, -1, 0, 1, 4]:
    print(f"sigmoid({z:2}) = {sigmoid(z):.4f}")
# sigmoid(0) = 0.5  -> the decision boundary
# large positive z -> ~1 (class 1), large negative -> ~0 (class 0)

# ----------------------------------------------------------------------
# Example 2: Logistic regression from scratch (gradient descent)
# ----------------------------------------------------------------------
print("\n--- Example 2: Logistic regression from scratch (gradient descent) ---")
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# 1 feature: hours studied -> pass(1)/fail(0)
xs = [1, 2, 3, 4, 5, 6]
ys = [0, 0, 0, 1, 1, 1]
n = len(xs)

w, b = 0.0, 0.0
lr = 0.3
for epoch in range(3000):
    grad_w = grad_b = 0.0
    for x, y in zip(xs, ys):
        p = sigmoid(w * x + b)
        grad_w += (p - y) * x          # gradient of log loss
        grad_b += (p - y)
    w -= lr * grad_w / n
    b -= lr * grad_b / n

def predict_proba(x):
    return sigmoid(w * x + b)

print(f"weights: w={w:.3f}, b={b:.3f}")
for x in [2, 3.5, 5]:
    p = predict_proba(x)
    print(f"x={x}: P(pass)={p:.3f} -> {'pass' if p >= 0.5 else 'fail'}")

# ----------------------------------------------------------------------
# Example 3: Logistic regression with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Logistic regression with scikit-learn ---")
try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    X, y = make_classification(n_samples=200, n_features=4,
                               n_informative=3, random_state=0)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    clf = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
    preds = clf.predict(X_te)
    print("accuracy:", round(accuracy_score(y_te, preds), 3))

    # Predicted probabilities for the first 3 test samples
    probs = clf.predict_proba(X_te[:3])[:, 1]
    print("P(class 1):", probs.round(3).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
