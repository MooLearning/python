# 88 — Regularization (L1, L2)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Regularization** discourages overly complex models by adding a penalty on the size of the weights to the loss. **L2 (Ridge)** penalizes the sum of squared weights — shrinking them smoothly toward zero. **L1 (Lasso)** penalizes the sum of absolute weights — driving some exactly to zero (automatic **feature selection**). A strength **λ (alpha)** controls how hard you penalize.

## Why it matters

Regularization is the primary cure for overfitting in linear models and neural networks. L1 also yields sparse, interpretable models by zeroing out useless features. It's everywhere — Ridge/Lasso, weight decay, dropout.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Penalty term** — Added to the loss to punish large weights.
- **L2 / Ridge** — Σwᵢ² penalty; shrinks weights smoothly, keeps all features.
- **L1 / Lasso** — Σ|wᵢ| penalty; zeros out some weights → sparsity.
- **Lambda / alpha** — Regularization strength; bigger = simpler model.
- **Bias-variance** — Regularization adds bias to cut variance/overfitting.
- **Elastic Net** — Combines L1 and L2 penalties.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# Target depends only on feature 1; feature 2 is irrelevant noise.
data = [([1, 2], 2.0), ([2, 1], 4.0), ([3, 0], 6.0),
        ([4, 3], 8.0), ([5, 1], 10.0)]

def train(lam, epochs=2000, lr=0.01):
    w = [0.0, 0.0]
    for _ in range(epochs):
        gw = [0.0, 0.0]
        for x, y in data:
            pred = w[0] * x[0] + w[1] * x[1]
            err = pred - y
            for j in range(2):
                gw[j] += 2 * err * x[j]
        # add the L2 penalty gradient: d/dw (lam * w^2) = 2*lam*w
        for j in range(2):
            gw[j] = gw[j] / len(data) + 2 * lam * w[j]
            w[j] -= lr * gw[j]
    return w

for lam in [0.0, 0.1, 1.0, 5.0]:
    w = train(lam)
    print(f"lambda={lam:4}: weights = [{w[0]:.3f}, {w[1]:.3f}]")
# As lambda grows, BOTH weights shrink toward 0 (especially the noise feature).
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Standardize features first — penalties depend on weight scale, so unscaled features are penalized unfairly.
- ⚠️ Too much regularization (huge λ) underfits — weights shrink so much the model ignores signal.
- ⚠️ L1 yields sparsity (feature selection); L2 keeps all features but small — pick by goal.
- ⚠️ Don't usually regularize the bias/intercept term.
- ⚠️ λ is a hyperparameter — tune it with cross-validation, don't guess.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

