# 87 — Hyperparameter Tuning

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Hyperparameters** are settings you choose BEFORE training (e.g. k in KNN, tree depth, learning rate, regularization strength) — distinct from parameters the model learns. **Tuning** searches for the combination that generalizes best, evaluated with **cross-validation**. Strategies: **grid search** (try every combo), **random search** (sample combos), and smarter Bayesian optimization.

## Why it matters

The right hyperparameters can be the difference between a mediocre and a great model. Systematic tuning with proper validation prevents both underfitting and overfitting and is a standard step in any serious ML pipeline.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Hyperparameter** — Set before training (k, depth, lr); not learned from data.
- **Grid search** — Exhaustively try all combinations in a grid.
- **Random search** — Sample random combinations — efficient for big spaces.
- **Validation score** — Use CV, not the test set, to compare settings.
- **Search space** — The ranges/values of each hyperparameter to try.
- **Overfitting the search** — Tuning too hard on validation leaks — keep a final test set.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Tune using cross-validation, never the final test set — that leaks and inflates results.
- ⚠️ Grid search explodes combinatorially; random/Bayesian search scales to many hyperparameters.
- ⚠️ Scale features when tuning distance/gradient models, or the search chases artifacts.
- ⚠️ Re-fit preprocessing inside CV folds (use pipelines) so each fold is independent.
- ⚠️ After choosing hyperparameters, evaluate ONCE on the held-out test set for an honest number.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

