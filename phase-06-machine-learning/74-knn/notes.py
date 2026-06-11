# ======================================================================
# 74 — K-Nearest Neighbors (KNN)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: KNN classifier from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: KNN classifier from scratch ---")
import math
from collections import Counter

# training points: (features, label)
train = [
    ((1, 1), "A"), ((1, 2), "A"), ((2, 1), "A"),
    ((6, 6), "B"), ((7, 7), "B"), ((6, 7), "B"),
]

def euclidean(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))

def knn_predict(point, k=3):
    # sort training points by distance to the query point
    distances = sorted(train, key=lambda item: euclidean(point, item[0]))
    neighbors = [label for _, label in distances[:k]]
    return Counter(neighbors).most_common(1)[0][0]

print("(2,2) ->", knn_predict((2, 2)))    # A (near the A cluster)
print("(6,5) ->", knn_predict((6, 5)))    # B (near the B cluster)
print("(4,4) ->", knn_predict((4, 4)))    # depends on k / ties

# ----------------------------------------------------------------------
# Example 2: How k changes the prediction; KNN regression
# ----------------------------------------------------------------------
print("\n--- Example 2: How k changes the prediction; KNN regression ---")
import math
from collections import Counter

train = [((1,), "low"), ((2,), "low"), ((3,), "low"),
         ((4,), "high"), ((5,), "high"), ((3.2,), "high")]

def knn(point, k):
    dist = sorted(train, key=lambda it: abs(point[0] - it[0][0]))
    labels = [lab for _, lab in dist[:k]]
    return Counter(labels).most_common(1)[0][0]

for k in [1, 3, 5]:
    print(f"k={k}: (3.1,) -> {knn((3.1,), k)}")

# KNN regression: average the neighbors' values
reg_train = [(1, 10), (2, 20), (3, 30), (4, 40)]
def knn_reg(x, k=2):
    nearest = sorted(reg_train, key=lambda it: abs(x - it[0]))[:k]
    return sum(v for _, v in nearest) / k
print("regress x=2.5 ->", knn_reg(2.5))   # (20+30)/2 = 25

# ----------------------------------------------------------------------
# Example 3: KNN with scikit-learn (and why scaling matters)
# ----------------------------------------------------------------------
print("\n--- Example 3: KNN with scikit-learn (and why scaling matters) ---")
try:
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline

    X, y = load_iris(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    # scale features, then KNN — chained so test data is scaled the same way
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(X_tr, y_tr)
    print("accuracy:", round(model.score(X_te, y_te), 3))
    print("predict first 5:", model.predict(X_te[:5]).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
