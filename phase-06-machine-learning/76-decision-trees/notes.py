# ======================================================================
# 76 — Decision Trees  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Gini impurity and finding the best split
# ----------------------------------------------------------------------
print("\n--- Example 1: Gini impurity and finding the best split ---")
from collections import Counter

def gini(labels):
    if not labels:
        return 0.0
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in Counter(labels).values())

print("gini pure   [A,A,A]:", gini(["A", "A", "A"]))      # 0.0
print("gini mixed  [A,B]  :", gini(["A", "B"]))           # 0.5
print("gini  [A,A,B,B,B]  :", round(gini(["A","A","B","B","B"]), 3))

# Best threshold split on a 1-feature dataset (minimize weighted Gini)
rows = [(1, "A"), (2, "A"), (3, "A"), (6, "B"), (7, "B"), (8, "B")]
def best_threshold(rows):
    best = None
    vals = sorted(set(x for x, _ in rows))
    for i in range(len(vals) - 1):
        t = (vals[i] + vals[i + 1]) / 2
        left = [l for x, l in rows if x <= t]
        right = [l for x, l in rows if x > t]
        weighted = (len(left) * gini(left) + len(right) * gini(right)) / len(rows)
        if best is None or weighted < best[0]:
            best = (weighted, t)
    return best
print("best split:", best_threshold(rows))   # (0.0, 4.5) -> perfectly pure

# ----------------------------------------------------------------------
# Example 2: Build a small decision tree from scratch
# ----------------------------------------------------------------------
print("\n--- Example 2: Build a small decision tree from scratch ---")
from collections import Counter

def gini(labels):
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in Counter(labels).values()) if n else 0

def best_split(rows):
    best = None
    n_features = len(rows[0][0])
    for f in range(n_features):
        for t in sorted(set(r[0][f] for r in rows)):
            left = [r for r in rows if r[0][f] <= t]
            right = [r for r in rows if r[0][f] > t]
            if not left or not right:
                continue
            g = (len(left) * gini([r[1] for r in left]) +
                 len(right) * gini([r[1] for r in right])) / len(rows)
            if best is None or g < best[0]:
                best = (g, f, t, left, right)
    return best

def build(rows, depth=0, max_depth=3):
    labels = [r[1] for r in rows]
    if len(set(labels)) == 1 or depth >= max_depth:
        return Counter(labels).most_common(1)[0][0]
    split = best_split(rows)
    if not split:
        return Counter(labels).most_common(1)[0][0]
    _, f, t, left, right = split
    return {"f": f, "t": t, "L": build(left, depth+1, max_depth),
            "R": build(right, depth+1, max_depth)}

def predict(tree, x):
    while isinstance(tree, dict):
        tree = tree["L"] if x[tree["f"]] <= tree["t"] else tree["R"]
    return tree

data = [((2, 1), 0), ((1, 1), 0), ((2, 2), 0),
        ((6, 5), 1), ((7, 4), 1), ((6, 6), 1)]
tree = build(data)
print("tree:", tree)
print("predict (2,2) ->", predict(tree, (2, 2)))   # 0
print("predict (6,5) ->", predict(tree, (6, 5)))   # 1

# ----------------------------------------------------------------------
# Example 3: Decision tree with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Decision tree with scikit-learn ---")
try:
    from sklearn.tree import DecisionTreeClassifier, export_text
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    X, y = load_iris(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    clf = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X_tr, y_tr)
    print("accuracy:", round(clf.score(X_te, y_te), 3))
    print("feature importances:", clf.feature_importances_.round(3).tolist())
    print("\ntree rules:\n", export_text(clf, max_depth=2))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
