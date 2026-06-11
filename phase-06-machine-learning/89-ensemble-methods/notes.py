# ======================================================================
# 89 — Ensemble Methods  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Hard voting from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: Hard voting from scratch ---")
from collections import Counter

# Three simple 'models' each return a class label for an input.
def model_a(x): return "spam" if x > 5 else "ham"
def model_b(x): return "spam" if x > 3 else "ham"
def model_c(x): return "spam" if x > 7 else "ham"

def hard_vote(x):
    votes = [model_a(x), model_b(x), model_c(x)]
    return Counter(votes).most_common(1)[0][0], votes

for x in [2, 6, 8]:
    decision, votes = hard_vote(x)
    print(f"x={x}: votes={votes} -> {decision}")

# ----------------------------------------------------------------------
# Example 2: Soft voting (average probabilities)
# ----------------------------------------------------------------------
print("\n--- Example 2: Soft voting (average probabilities) ---")
# Each model outputs P(class=1). Soft voting averages them.
def model_a(x): return min(1.0, x / 10)        # probability-like score
def model_b(x): return min(1.0, x / 8)
def model_c(x): return min(1.0, (x - 1) / 9)

def soft_vote(x, threshold=0.5):
    probs = [model_a(x), model_b(x), model_c(x)]
    avg = sum(probs) / len(probs)
    label = 1 if avg >= threshold else 0
    return label, round(avg, 3), [round(p, 2) for p in probs]

for x in [3, 5, 8]:
    label, avg, probs = soft_vote(x)
    print(f"x={x}: probs={probs}, avg={avg} -> class {label}")

# ----------------------------------------------------------------------
# Example 3: Voting and Stacking with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Voting and Stacking with scikit-learn ---")
try:
    from sklearn.ensemble import VotingClassifier, StackingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import cross_val_score

    X, y = load_iris(return_X_y=True)
    estimators = [
        ("lr", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(max_depth=3, random_state=0)),
        ("knn", KNeighborsClassifier()),
    ]
    voting = VotingClassifier(estimators, voting="hard")
    print("voting CV acc :", round(cross_val_score(voting, X, y, cv=5).mean(), 3))

    stacking = StackingClassifier(estimators,
                                  final_estimator=LogisticRegression(max_iter=1000))
    print("stacking CV acc:", round(cross_val_score(stacking, X, y, cv=5).mean(), 3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")
