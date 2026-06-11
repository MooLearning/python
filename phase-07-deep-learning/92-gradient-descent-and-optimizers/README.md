# 92 — Gradient Descent and Optimizers

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Gradient descent** minimizes the loss by repeatedly stepping weights opposite the gradient. Variants differ by how much data each step uses: **batch** (all data), **stochastic/SGD** (one sample), **mini-batch** (a small group). **Optimizers** improve plain SGD: **momentum** accelerates consistent directions, **RMSProp** adapts per-parameter step sizes, and **Adam** combines both — the popular default.

## Why it matters

Optimization is how networks actually learn. The optimizer and learning rate dramatically affect whether training converges, how fast, and how well — among the most important practical choices in deep learning.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install torch
```

## Key concepts

- **Batch vs SGD** — All data per step (stable, slow) vs one sample (noisy, fast).
- **Mini-batch** — A small batch — the practical sweet spot.
- **Learning rate** — Step size; the single most important hyperparameter.
- **Momentum** — Accumulate velocity to roll through small bumps and speed up.
- **Adam** — Adaptive per-parameter rates + momentum; strong default.
- **Convergence** — Loss decreasing and settling near a minimum.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def f(x):    return x ** 2          # minimize -> minimum at x=0
def grad(x): return 2 * x

def descend(lr, momentum=0.0, steps=15):
    x, v = 10.0, 0.0
    for _ in range(steps):
        g = grad(x)
        v = momentum * v - lr * g    # velocity (0 momentum = plain GD)
        x += v
    return x

print("plain GD   (lr=0.1):", round(descend(0.1), 5))
print("with momentum 0.9  :", round(descend(0.1, momentum=0.9), 5))
# Momentum reaches the minimum faster by building up velocity.
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Learning rate too high → divergence/NaN; too low → painfully slow or stuck.
- ⚠️ Always SHUFFLE data for SGD/mini-batch, or ordered batches bias the gradient.
- ⚠️ Adam is a great default but can generalize slightly worse than tuned SGD+momentum.
- ⚠️ Remember to zero gradients each step in frameworks, or they accumulate.
- ⚠️ Constant LR can stall near minima — learning-rate schedules/decay often help.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

