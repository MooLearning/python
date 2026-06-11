# 73 — Logistic Regression

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Logistic regression** is a **classification** model (despite the name). It computes a linear score `w·x + b`, then squashes it through the **sigmoid** into a probability between 0 and 1. Predict class 1 if the probability exceeds a threshold (usually 0.5). It's trained by minimizing **log loss** (cross-entropy) via gradient descent.

## Why it matters

It's the default baseline for binary classification: fast, interpretable (weights = log-odds effects), and outputs calibrated probabilities. It underlies neural-network output layers and many real systems (spam, churn, click prediction).

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Sigmoid** — σ(z) = 1/(1+e^−z) maps any score to (0, 1).
- **Decision boundary** — Predict 1 when probability ≥ 0.5 (score ≥ 0).
- **Log loss** — Cross-entropy penalizes confident wrong predictions heavily.
- **Probabilities** — Output is a probability, not just a hard label.
- **Linear in features** — The boundary is a line/hyperplane in feature space.
- **Threshold tuning** — Move 0.5 to trade precision vs recall.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

for z in [-4, -1, 0, 1, 4]:
    print(f"sigmoid({z:2}) = {sigmoid(z):.4f}")
# sigmoid(0) = 0.5  -> the decision boundary
# large positive z -> ~1 (class 1), large negative -> ~0 (class 0)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ It outputs PROBABILITIES — threshold them (default 0.5) to get class labels.
- ⚠️ The decision boundary is linear; for curved boundaries add features or use another model.
- ⚠️ Imbalanced classes bias it toward the majority — use class weights or resampling.
- ⚠️ Scale/standardize features so gradient descent converges and weights are comparable.
- ⚠️ Perfectly separable data makes weights blow up — regularization keeps them finite.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

