# 79 — Gradient Boosting

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Gradient boosting** builds an ensemble **sequentially**: each new weak learner (usually a shallow tree) is trained to correct the **residual errors** of the current ensemble. Predictions are added together, scaled by a **learning rate**. Unlike random forests (parallel, independent trees), boosting is additive and focuses on the mistakes — powering XGBoost, LightGBM, and CatBoost.

## Why it matters

Gradient-boosted trees are the dominant approach for tabular ML competitions and many production systems — typically the most accurate off-the-shelf model. Understanding the residual-fitting idea demystifies them.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Weak learner** — A simple model (shallow tree/stump) slightly better than chance.
- **Residuals** — The errors (actual − predicted) the next learner targets.
- **Additive model** — Final prediction = sum of all learners' outputs.
- **Learning rate** — Shrinks each learner's contribution to avoid overfitting.
- **Sequential** — Each tree depends on the ones before it.
- **vs bagging** — Boosting reduces bias by focusing on errors; bagging reduces variance.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
data = [(1, 1.0), (2, 1.5), (3, 3.5), (4, 4.2), (5, 6.0)]
xs = [x for x, _ in data]
ys = [y for _, y in data]

def best_stump(xs, residuals):
    # threshold that best predicts residuals by side means (min SSE)
    best = None
    for t in sorted(set(xs)):
        left = [r for x, r in zip(xs, residuals) if x <= t]
        right = [r for x, r in zip(xs, residuals) if x > t]
        if not left or not right:
            continue
        lm, rm = sum(left) / len(left), sum(right) / len(right)
        sse = sum((r - lm) ** 2 for r in left) + sum((r - rm) ** 2 for r in right)
        if best is None or sse < best[0]:
            best = (sse, t, lm, rm)
    return best

pred = [sum(ys) / len(ys)] * len(ys)     # start from the mean
lr = 0.5
for rnd in range(6):
    residuals = [y - p for y, p in zip(ys, pred)]
    _, t, lm, rm = best_stump(xs, residuals)
    pred = [p + lr * (lm if x <= t else rm) for x, p in zip(xs, pred)]
    mse = sum((y - p) ** 2 for y, p in zip(ys, pred)) / len(ys)
    print(f"round {rnd}: split@{t}, MSE={mse:.4f}")
print("final preds:", [round(p, 2) for p in pred])
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Boosting trains sequentially — it can't parallelize across trees like a random forest.
- ⚠️ Too many rounds or too-high learning rate overfits; tune n_estimators with early stopping.
- ⚠️ Sensitive to noisy data and outliers because it keeps chasing residuals.
- ⚠️ Use SHALLOW trees (stumps to depth ~3) as weak learners; deep trees defeat the purpose.
- ⚠️ Lower learning rate usually needs more trees — they trade off (lr × n_estimators).

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

