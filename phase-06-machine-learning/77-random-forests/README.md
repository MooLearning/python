# 77 — Random Forests

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **random forest** is an **ensemble** of many decision trees whose predictions are combined (majority vote for classification, average for regression). Each tree trains on a **bootstrap sample** (random rows with replacement) and considers a **random subset of features** at each split. This **bagging** + feature randomness decorrelates the trees, slashing variance and overfitting while keeping low bias.

## Why it matters

Random forests are one of the best out-of-the-box models for tabular data: accurate, robust to outliers and noise, need little tuning, and provide feature-importance estimates. They fix the high variance of single trees.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Ensemble** — Combine many models for a better, more stable prediction.
- **Bagging** — Bootstrap Aggregating: train each tree on a resample of the data.
- **Bootstrap sample** — Random rows drawn WITH replacement (~63% unique).
- **Feature randomness** — Each split considers a random feature subset.
- **Voting / averaging** — Aggregate tree outputs into one prediction.
- **Feature importance** — How much each feature reduces impurity across trees.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ More trees never hurt accuracy but cost time/memory — there are diminishing returns.
- ⚠️ A forest is less interpretable than one tree; use feature importances / SHAP to explain.
- ⚠️ Importances are biased toward high-cardinality features — interpret with care.
- ⚠️ If all trees see the same features/data they correlate; randomness is what makes it work.
- ⚠️ Forests can still overfit noisy data; tune depth, min_samples_leaf, and max_features.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

