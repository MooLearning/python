# 97 — Dropout and Batch Normalization

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Dropout** randomly 'drops' (zeros) a fraction of neurons during training, forcing the network to not rely on any single unit — a powerful **regularizer** against overfitting. **Batch Normalization** normalizes each layer's inputs to zero mean/unit variance per mini-batch (then rescales with learnable γ, β), which **stabilizes and speeds up** training and allows higher learning rates.

## Why it matters

These two layers are standard tools for training deep networks reliably: dropout combats overfitting, batch norm smooths the loss landscape so training converges faster and is less sensitive to initialization.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install tensorflow
```

## Key concepts

- **Dropout** — Randomly zero neurons during training; keep all at inference.
- **Inverted dropout** — Scale survivors by 1/(1−p) so the expected value is unchanged.
- **Train vs eval mode** — Dropout/BN behave differently in training vs inference.
- **Batch norm** — Normalize layer inputs over the batch, then scale/shift.
- **Internal covariate shift** — BN reduces shifting input distributions across layers.
- **Regularization** — Dropout (and BN slightly) reduce overfitting.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import random
random.seed(0)

def dropout(activations, p=0.5, training=True):
    if not training:
        return activations[:]                 # inference: use everything
    out = []
    for a in activations:
        keep = random.random() >= p
        out.append(a / (1 - p) if keep else 0.0)   # scale survivors
    return out

acts = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print("train (some zeroed, rest scaled):", [round(v, 2) for v in dropout(acts, 0.5)])
print("eval  (all kept)               :", dropout(acts, 0.5, training=False))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Dropout is ON only during training — it must be OFF at inference (frameworks handle this).
- ⚠️ Use inverted dropout (scale by 1/(1−p)) so activations have the same expected scale.
- ⚠️ Batch norm behaves differently in train (batch stats) vs eval (running averages).
- ⚠️ Very small batch sizes make batch-norm statistics noisy — consider LayerNorm/GroupNorm.
- ⚠️ Too-high dropout (e.g. 0.8) can underfit — 0.2–0.5 is typical.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

