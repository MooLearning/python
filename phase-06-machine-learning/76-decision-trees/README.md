# 76 — Decision Trees

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **decision tree** classifies (or regresses) by asking a sequence of yes/no questions about features, splitting the data at each **node** to make child groups as **pure** as possible. Purity is measured by **Gini impurity** or **entropy**. Splitting continues until leaves are pure or a depth limit is hit. The result is a flowchart you can read and explain.

## Why it matters

Trees are highly interpretable, need no feature scaling, handle non-linear relationships and mixed data types, and are the building block of random forests and gradient boosting — among the most effective models on tabular data.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Node / split** — A question on one feature that divides the data.
- **Gini impurity** — 1 − Σp²; 0 means a pure node (one class).
- **Entropy / info gain** — Alternative purity measure based on information.
- **Leaf** — A terminal node giving the prediction (majority class).
- **Max depth** — Limits tree size to prevent overfitting.
- **Greedy** — Picks the locally best split at each node.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Unpruned trees overfit badly (pure leaves memorize) — limit depth or min_samples_leaf.
- ⚠️ Greedy splitting isn't globally optimal; a slightly worse split now can be better overall.
- ⚠️ Small data changes can flip splits — trees are high-variance (random forests fix this).
- ⚠️ They can't extrapolate beyond the training range; predictions are piecewise-constant.
- ⚠️ Biased toward features with many distinct values when using naive impurity gains.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

