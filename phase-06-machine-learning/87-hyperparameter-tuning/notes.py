# ======================================================================
# 87 — Hyperparameter Tuning  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Grid search from scratch (tune k for KNN)
# ----------------------------------------------------------------------
print("\n--- Example 1: Grid search from scratch (tune k for KNN) ---")
import math
from collections import Counter

train = [((1,), "A"), ((2,), "A"), ((3,), "A"),
         ((6,), "B"), ((7,), "B"), ((8,), "B")]
val =   [((2.5,), "A"), ((6.5,), "B"), ((1.5,), "A"), ((7.5,), "B")]

def knn_predict(x, k):
    nearest = sorted(train, key=lambda it: abs(x[0] - it[0][0]))[:k]
    return Counter(lab for _, lab in nearest).most_common(1)[0][0]

def accuracy(k):
    correct = sum(1 for x, y in val if knn_predict(x, k) == y)
    return correct / len(val)

# Grid search over candidate k values
best_k, best_acc = None, -1
for k in [1, 2, 3, 4, 5]:
    acc = accuracy(k)
    print(f"k={k}: validation accuracy = {acc:.2f}")
    if acc > best_acc:
        best_k, best_acc = k, acc
print(f"-> best k = {best_k} (acc {best_acc:.2f})")

# ----------------------------------------------------------------------
# Example 2: Grid vs random search size
# ----------------------------------------------------------------------
print("\n--- Example 2: Grid vs random search size ---")
import random
random.seed(0)

# A 2-hyperparameter grid
learning_rates = [0.001, 0.01, 0.1, 1.0]
depths = [2, 3, 5, 10]

grid = [(lr, d) for lr in learning_rates for d in depths]
print("grid search tries:", len(grid), "combinations")   # 4*4 = 16

# Random search: sample a few combos instead of all
random_combos = [(random.choice(learning_rates), random.choice(depths))
                 for _ in range(5)]
print("random search tries:", len(random_combos), "->", random_combos)
print("Random search scales better when there are many hyperparameters.")

# ----------------------------------------------------------------------
# Example 3: GridSearchCV with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: GridSearchCV with scikit-learn ---")
try:
    from sklearn.model_selection import GridSearchCV
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_iris

    X, y = load_iris(return_X_y=True)
    param_grid = {"n_estimators": [10, 50], "max_depth": [2, 3, None]}

    search = GridSearchCV(RandomForestClassifier(random_state=0),
                          param_grid, cv=5)
    search.fit(X, y)
    print("best params:", search.best_params_)
    print("best CV score:", round(search.best_score_, 3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
