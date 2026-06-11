# ======================================================================
# 77 — Random Forests  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Bootstrap sampling (the heart of bagging)
# ----------------------------------------------------------------------
print("\n--- Example 1: Bootstrap sampling (the heart of bagging) ---")
import random
random.seed(0)

data = [10, 20, 30, 40, 50]

# A bootstrap sample: draw len(data) items WITH replacement
def bootstrap(data):
    return [random.choice(data) for _ in range(len(data))]

for i in range(3):
    sample = bootstrap(data)
    unique = len(set(sample))
    print(f"sample {i}: {sample}  ({unique}/{len(data)} unique)")
# On average ~63% of rows appear; the rest are 'out-of-bag'.

# ----------------------------------------------------------------------
# Example 2: A tiny forest of stumps with majority voting
# ----------------------------------------------------------------------
print("\n--- Example 2: A tiny forest of stumps with majority voting ---")
import random
from collections import Counter
random.seed(1)

# 1-feature data: small x -> 0, large x -> 1 (with a little noise)
data = [(1, 0), (2, 0), (3, 0), (3, 1), (6, 1), (7, 1), (8, 1), (2, 0)]

def gini(labels):
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in Counter(labels).values()) if n else 0

def train_stump(rows):
    best = None
    for t in sorted(set(x for x, _ in rows)):
        left = [l for x, l in rows if x <= t]
        right = [l for x, l in rows if x > t]
        if not left or not right:
            continue
        g = (len(left)*gini(left) + len(right)*gini(right)) / len(rows)
        if best is None or g < best[0]:
            lbl_L = Counter(left).most_common(1)[0][0]
            lbl_R = Counter(right).most_common(1)[0][0]
            best = (g, t, lbl_L, lbl_R)
    return best        # (gini, threshold, left_label, right_label)

# Train a forest: each stump on its own bootstrap sample
forest = []
for _ in range(11):
    sample = [random.choice(data) for _ in range(len(data))]
    forest.append(train_stump(sample))

def forest_predict(x):
    votes = [lblL if x <= t else lblR for _, t, lblL, lblR in forest]
    return Counter(votes).most_common(1)[0][0]

for x in [2, 5, 8]:
    print(f"x={x} -> class {forest_predict(x)}")

# ----------------------------------------------------------------------
# Example 3: Random forest with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Random forest with scikit-learn ---")
try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_wine
    from sklearn.model_selection import train_test_split

    X, y = load_wine(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    rf = RandomForestClassifier(n_estimators=100, random_state=0).fit(X_tr, y_tr)
    print("accuracy:", round(rf.score(X_te, y_te), 3))

    # Top-3 most important features
    importances = list(enumerate(rf.feature_importances_))
    top = sorted(importances, key=lambda x: -x[1])[:3]
    print("top features (index, importance):",
          [(i, round(v, 3)) for i, v in top])
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
