# 91 — Forward and Backpropagation

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Forward propagation** runs inputs through the network to produce a prediction and a **loss**. **Backpropagation** then applies the **chain rule** to compute the gradient of the loss with respect to every weight — flowing errors backward layer by layer. Gradient descent uses those gradients to nudge the weights. Repeating forward + backprop + update is how networks **learn**.

## Why it matters

Backpropagation is THE algorithm that makes deep learning possible — efficiently computing millions of gradients. Implementing it once (even for XOR) turns neural nets from magic into understandable calculus.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install torch
```

## Key concepts

- **Forward pass** — Compute activations layer by layer → prediction → loss.
- **Loss** — How wrong the prediction is (e.g. MSE, cross-entropy).
- **Chain rule** — Decompose the gradient through composed functions.
- **Backward pass** — Propagate error gradients from output back to inputs.
- **Weight update** — w ← w − lr · ∂loss/∂w.
- **Epoch** — One full pass over the training data.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math, random
random.seed(1)

def sigmoid(z): return 1 / (1 + math.exp(-z))
def dsig(a):    return a * (1 - a)           # derivative via the activation

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 1, 1, 0]                              # XOR: not linearly separable

r = lambda: random.uniform(-1, 1)
W1 = [[r(), r()], [r(), r()]]                 # 2 hidden neurons
b1 = [r(), r()]
W2 = [r(), r()]                               # 1 output neuron
b2 = r()
lr = 0.5

for epoch in range(10000):
    for x, y in zip(X, Y):
        # ---- forward ----
        h = [sigmoid(W1[j][0]*x[0] + W1[j][1]*x[1] + b1[j]) for j in range(2)]
        out = sigmoid(W2[0]*h[0] + W2[1]*h[1] + b2)
        # ---- backward (chain rule) ----
        d_out = (out - y) * dsig(out)         # dLoss/dz at output
        d_h = [d_out * W2[j] * dsig(h[j]) for j in range(2)]
        # ---- update ----
        W2[0] -= lr * d_out * h[0]; W2[1] -= lr * d_out * h[1]; b2 -= lr * d_out
        for j in range(2):
            W1[j][0] -= lr * d_h[j] * x[0]
            W1[j][1] -= lr * d_h[j] * x[1]
            b1[j] -= lr * d_h[j]

print("XOR predictions after training:")
for x, y in zip(X, Y):
    h = [sigmoid(W1[j][0]*x[0] + W1[j][1]*x[1] + b1[j]) for j in range(2)]
    out = sigmoid(W2[0]*h[0] + W2[1]*h[1] + b2)
    print(f"  {x} -> {out:.3f}  (target {y})")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Forgetting to ZERO gradients between steps (in frameworks) accumulates them — wrong updates.
- ⚠️ Sigmoid/tanh in deep nets cause VANISHING gradients; use ReLU and good initialization.
- ⚠️ Too-large learning rates make gradients explode and loss go to NaN.
- ⚠️ Backprop needs the forward activations cached — you can't discard them before the backward pass.
- ⚠️ A wrong derivative (e.g. sigmoid') silently breaks learning — verify gradients numerically.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

