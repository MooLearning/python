# ======================================================================
# 69 — ML Overview  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: A tiny supervised classifier learned from data
# ----------------------------------------------------------------------
print("\n--- Example 1: A tiny supervised classifier learned from data ---")
# Learn a threshold to classify animals as 'cat' or 'dog' by weight (kg).
train = [(4, "cat"), (5, "cat"), (3.5, "cat"), (20, "dog"), (25, "dog"), (18, "dog")]

# 'Training' = compute the midpoint between class averages
cats = [w for w, label in train if label == "cat"]
dogs = [w for w, label in train if label == "dog"]
threshold = (sum(cats) / len(cats) + sum(dogs) / len(dogs)) / 2
print("learned threshold:", round(threshold, 2), "kg")

def predict(weight):
    return "dog" if weight > threshold else "cat"

# Predict on NEW, unseen examples
for w in [6, 15, 22]:
    print(f"{w} kg -> {predict(w)}")

# ----------------------------------------------------------------------
# Example 2: The train / evaluate / predict loop
# ----------------------------------------------------------------------
print("\n--- Example 2: The train / evaluate / predict loop ---")
# Toy regression: learn that y ~ 2*x from examples, then evaluate.
train = [(1, 2), (2, 4), (3, 6), (4, 8)]

# 'Fit': estimate the slope as average(y/x)
slope = sum(y / x for x, y in train) / len(train)
print("learned slope:", slope)            # ~2.0

def model(x):
    return slope * x

# Evaluate on held-out data with mean absolute error
test = [(5, 10), (6, 12)]
mae = sum(abs(model(x) - y) for x, y in test) / len(test)
print("test MAE:", round(mae, 4))         # ~0 (great fit)
print("predict x=10 ->", model(10))       # ~20

# ----------------------------------------------------------------------
# Example 3: Supervised vs unsupervised with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Supervised vs unsupervised with scikit-learn ---")
try:
    from sklearn.linear_model import LinearRegression   # supervised
    from sklearn.cluster import KMeans                   # unsupervised

    # Supervised: learn y = 3x from labeled data
    X = [[1], [2], [3], [4]]
    y = [3, 6, 9, 12]
    reg = LinearRegression().fit(X, y)
    print("supervised slope ~", round(reg.coef_[0], 2))   # ~3
    print("predict 5 ->", round(reg.predict([[5]])[0], 2))

    # Unsupervised: group points with NO labels
    points = [[1], [1.5], [8], [8.5]]
    km = KMeans(n_clusters=2, n_init=10, random_state=0).fit(points)
    print("cluster labels:", km.labels_.tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
