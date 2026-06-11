# 86 — Regression Metrics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Regression metrics** measure how far predictions fall from continuous targets. **MAE** (mean absolute error) averages |error|; **MSE** averages squared error (punishing big misses); **RMSE** is its square root (same units as the target); **R²** reports the fraction of variance explained (1 = perfect, 0 = no better than the mean, negative = worse).

## Why it matters

Choosing the right error metric shapes what the model optimizes and how you judge it. RMSE vs MAE encodes how much you care about large errors; R² gives an intuitive 'how much variance is explained' score for stakeholders.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **MAE** — Average absolute error; robust, same units as target.
- **MSE** — Average squared error; penalizes large errors heavily.
- **RMSE** — √MSE; interpretable in the target's units.
- **R²** — 1 − SS_res/SS_tot; variance explained.
- **MAPE** — Mean absolute PERCENTAGE error; scale-free but breaks near zero.
- **Metric choice** — Outliers → MAE; penalize big misses → RMSE.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

y_true = [3.0, -0.5, 2.0, 7.0, 4.2]
y_pred = [2.5,  0.0, 2.0, 8.0, 4.0]
n = len(y_true)

mae = sum(abs(t - p) for t, p in zip(y_true, y_pred)) / n
mse = sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / n
rmse = math.sqrt(mse)

mean_y = sum(y_true) / n
ss_res = sum((t - p) ** 2 for t, p in zip(y_true, y_pred))
ss_tot = sum((t - mean_y) ** 2 for t in y_true)
r2 = 1 - ss_res / ss_tot

print(f"MAE : {mae:.4f}")
print(f"MSE : {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R^2 : {r2:.4f}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ RMSE and MSE are dominated by outliers; use MAE if large errors shouldn't be over-weighted.
- ⚠️ R² can be NEGATIVE when the model is worse than predicting the mean.
- ⚠️ A high R² doesn't mean the model is good or causal — check residuals and context.
- ⚠️ MAPE explodes when true values are near zero — avoid it for targets that cross 0.
- ⚠️ Compare RMSE only on the same target scale; it's not comparable across different units.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

