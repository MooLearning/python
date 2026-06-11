# 71 — Bias-Variance Tradeoff

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Prediction error splits into **bias** (error from overly simple assumptions — **underfitting**), **variance** (sensitivity to the training sample — **overfitting**), and irreducible noise. Simple models have high bias/low variance; complex models have low bias/high variance. The **tradeoff** is finding the sweet-spot complexity that minimizes total error on unseen data.

## Why it matters

Diagnosing whether a model underfits or overfits tells you what to do next (more features/complexity vs more data/regularization). It's the central tension in all of ML.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Bias** — Error from wrong assumptions; underfitting (too simple).
- **Variance** — Error from sensitivity to training data; overfitting (too complex).
- **Underfitting** — High train AND test error — model too weak.
- **Overfitting** — Low train but high test error — memorized noise.
- **Sweet spot** — Complexity that minimizes test/validation error.
- **Fixes** — Underfit → add complexity/features; overfit → more data/regularize.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# True relationship: y = 2x. A high-bias model predicts the global mean.
train = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]
mean_y = sum(y for _, y in train) / len(train)     # constant predictor

def underfit(x):
    return mean_y                                  # ignores x entirely!

train_err = sum((underfit(x) - y) ** 2 for x, y in train) / len(train)
test = [(6, 12), (7, 14)]
test_err = sum((underfit(x) - y) ** 2 for x, y in test) / len(test)
print("constant prediction:", mean_y)
print("train MSE:", round(train_err, 2), "(high)")
print("test  MSE:", round(test_err, 2), "(high) -> UNDERFIT / high bias")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Low training error alone means nothing — a memorizing model has zero train error.
- ⚠️ A big gap between train and test performance signals overfitting (high variance).
- ⚠️ High error on BOTH train and test signals underfitting (high bias).
- ⚠️ Adding data helps variance/overfitting, but rarely fixes bias/underfitting.
- ⚠️ More complexity isn't free — it needs more data to avoid overfitting.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

