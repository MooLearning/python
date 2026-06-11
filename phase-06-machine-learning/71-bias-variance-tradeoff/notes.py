# ======================================================================
# 71 — Bias-Variance Tradeoff  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Underfitting: a too-simple model has high error everywhere
# ----------------------------------------------------------------------
print("\n--- Example 1: Underfitting: a too-simple model has high error everywhere ---")
# True relationship: y = 2x. A high-bias model predicts the global mean.
train = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]
mean_y = sum(y for _, y in train) / len(train)     # constant predictor

def underfit(x):
    return mean_y                                  # ignores x entirely!

train_err = sum((underfit(x) - y) ** 2 for x, y in train) / len(train)
test = [(6, 12), (7, 14)]
test_err = sum((underfit(x) - y) ** 2 for x, y in test) / len(test)
print("constant prediction:", mean_y)
print("train MSE:", round(train_err, 2), "(high)")
print("test  MSE:", round(test_err, 2), "(high) -> UNDERFIT / high bias")

# ----------------------------------------------------------------------
# Example 2: Overfitting: memorizing train gives 0 train error, bad test error
# ----------------------------------------------------------------------
print("\n--- Example 2: Overfitting: memorizing train gives 0 train error, bad test error ---")
train = [(1, 2), (2, 4), (3, 5), (4, 8)]

# A model that memorizes exact training points (a lookup table)
memory = {x: y for x, y in train}

def overfit(x):
    return memory.get(x, 0)        # perfect on train, clueless on new x

train_err = sum((overfit(x) - y) ** 2 for x, y in train) / len(train)
test = [(5, 10), (6, 12)]
test_err = sum((overfit(x) - y) ** 2 for x, y in test) / len(test)
print("train MSE:", train_err, "(zero -> looks perfect!)")
print("test  MSE:", round(test_err, 1), "(terrible) -> OVERFIT / high variance")

# ----------------------------------------------------------------------
# Example 3: Polynomial degree vs error with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Polynomial degree vs error with scikit-learn ---")
try:
    import numpy as np
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.model_selection import train_test_split

    rng = np.random.RandomState(0)
    X = np.linspace(-3, 3, 60).reshape(-1, 1)
    y = X.ravel() ** 2 + rng.normal(0, 1.5, 60)    # true: quadratic + noise

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)
    for degree in [1, 2, 10]:
        m = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        m.fit(X_tr, y_tr)
        tr = m.score(X_tr, y_tr); te = m.score(X_te, y_te)
        tag = "underfit" if degree == 1 else ("good" if degree == 2 else "overfit")
        print(f"degree {degree:2}: train R2={tr:.2f}, test R2={te:.2f} -> {tag}")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn numpy")

print("\nDone! Tip: change values above and run again to learn by experiment.")
