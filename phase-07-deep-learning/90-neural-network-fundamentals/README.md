# 90 — Neural Network Fundamentals

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **neural network** is layers of **neurons**. Each neuron computes a **weighted sum** of its inputs plus a **bias**, then applies a non-linear **activation function** (sigmoid, ReLU, tanh). Stacking layers (**input → hidden → output**) lets the network approximate complex, non-linear functions. The activation's non-linearity is essential — without it, any depth collapses to a single linear map.

## Why it matters

Neural networks are the foundation of deep learning, powering vision, language, and speech. Understanding the neuron, weights, bias, and activations demystifies everything that follows — backprop, CNNs, transformers.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install tensorflow
```

## Key concepts

- **Neuron** — Weighted sum of inputs + bias, then an activation.
- **Weights & bias** — Learnable parameters; weights scale inputs, bias shifts.
- **Activation** — Non-linearity (ReLU/sigmoid/tanh) enabling complex functions.
- **Layer** — A group of neurons; networks stack input/hidden/output layers.
- **Forward pass** — Data flows input → output to produce a prediction.
- **Why non-linear** — Without it, stacked layers reduce to one linear layer.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def neuron(inputs, weights, bias, activation=sigmoid):
    z = sum(i * w for i, w in zip(inputs, weights)) + bias   # weighted sum
    return activation(z)

# An OR-like neuron
inputs_list = [[0, 0], [0, 1], [1, 0], [1, 1]]
weights = [10, 10]      # large weights -> sharp decision
bias = -5
for x in inputs_list:
    out = neuron(x, weights, bias)
    print(f"{x} -> {out:.3f} -> {round(out)}")   # behaves like logical OR
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Without a non-linear activation, any number of layers equals a single linear layer.
- ⚠️ Sigmoid/tanh saturate for large |z| (tiny gradients) — ReLU avoids this in hidden layers.
- ⚠️ Initialize weights randomly (not all zeros), or every neuron learns the same thing.
- ⚠️ ReLU neurons can 'die' (always output 0) if learning rate is too high — try leaky ReLU.
- ⚠️ Bias terms matter — without them a neuron's boundary must pass through the origin.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

