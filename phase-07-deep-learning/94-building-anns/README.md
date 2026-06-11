# 94 — Building ANNs

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

An **Artificial Neural Network (ANN)** for tabular/structured data is a stack of fully connected (**Dense**) layers. The recipe: choose an architecture (layer sizes, activations), pick a **loss** and **optimizer**, then `fit` on training data and `evaluate` on test data. Output layer/activation depends on the task: 1 sigmoid (binary), softmax (multiclass), or linear (regression).

## Why it matters

ANNs are the entry point to building real models in a framework — turning the theory (neurons, activations, backprop, optimizers) into a working classifier/regressor with a few lines of Keras/PyTorch.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install tensorflow
```

## Key concepts

- **Architecture** — Number of layers and neurons; the model's capacity.
- **Output layer** — sigmoid (binary), softmax (multiclass), linear (regression).
- **Loss function** — binary/categorical cross-entropy or MSE — match the task.
- **fit / evaluate** — Train on data, then measure on held-out test data.
- **Epochs & batch size** — How many passes and how many samples per update.
- **Overfitting signs** — Train accuracy ≫ validation accuracy.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math
def relu(z):    return max(0.0, z)
def softmax(zs):
    m = max(zs)
    exps = [math.exp(z - m) for z in zs]
    s = sum(exps)
    return [e / s for e in exps]

def dense(inputs, weights, biases, act):
    outs = []
    for j in range(len(biases)):
        z = sum(i * w for i, w in zip(inputs, weights[j])) + biases[j]
        outs.append(z if act is None else act(z))
    return outs

x = [0.5, -1.0, 2.0]
W1 = [[0.1, 0.2, -0.1], [0.0, 0.3, 0.2]]     # hidden: 2 ReLU units
b1 = [0.0, 0.1]
W2 = [[0.5, -0.2], [0.1, 0.4], [-0.3, 0.2]]  # output: 3 classes
b2 = [0.0, 0.0, 0.0]

hidden = dense(x, W1, b1, relu)
logits = dense(hidden, W2, b2, None)
probs = softmax(logits)
print("hidden       :", [round(h, 3) for h in hidden])
print("class probs  :", [round(p, 3) for p in probs])
print("predicted    :", probs.index(max(probs)))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Match output activation + loss to the task — softmax with MSE won't train well.
- ⚠️ Scale/normalize inputs; unscaled features slow or break training.
- ⚠️ Too many epochs overfits — watch validation loss and use early stopping.
- ⚠️ Use sparse_categorical_crossentropy for integer labels, categorical for one-hot.
- ⚠️ Start small — a giant network on little data just memorizes.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

