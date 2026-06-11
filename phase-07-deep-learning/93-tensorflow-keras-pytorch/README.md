# 93 — TensorFlow, Keras and PyTorch

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**TensorFlow/Keras** and **PyTorch** are the two dominant deep-learning frameworks. They provide **tensors** (GPU-accelerated arrays), **automatic differentiation** (autograd, so you never hand-code backprop), prebuilt **layers/optimizers/losses**, and training utilities. **Keras** offers a simple high-level API; **PyTorch** is Pythonic and flexible (the research favorite).

## Why it matters

You won't implement backprop by hand in practice — frameworks make building, training, and deploying networks fast and GPU-accelerated. Knowing both (and their tensor/autograd model) is essential for real deep learning.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install tensorflow torch
```

## Key concepts

- **Tensor** — An N-dimensional array (like NumPy) that can live on a GPU.
- **Autograd** — Automatic gradient computation — no manual backprop.
- **Keras Sequential** — Stack layers in a list for a quick model.
- **nn.Module** — PyTorch's base class for custom models.
- **Optimizer & loss** — Prebuilt SGD/Adam and MSE/cross-entropy.
- **GPU acceleration** — Move tensors/models to a GPU for speed.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# A 'tensor' is just an n-dimensional array. Pure-Python stand-ins:
scalar = 3.14                       # 0-D
vector = [1, 2, 3]                  # 1-D
matrix = [[1, 2], [3, 4]]           # 2-D
tensor3d = [[[1], [2]], [[3], [4]]] # 3-D

def shape(x):
    s = []
    while isinstance(x, list):
        s.append(len(x)); x = x[0]
    return tuple(s)

print("scalar shape :", shape(scalar) or "()")
print("vector shape :", shape(vector))     # (3,)
print("matrix shape :", shape(matrix))     # (2, 2)
print("tensor shape :", shape(tensor3d))   # (2, 2, 1)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Don't mix framework tensors with NumPy mid-graph — convert explicitly and watch the device.
- ⚠️ Keep tensors on the SAME device (CPU/GPU); mismatches raise runtime errors.
- ⚠️ PyTorch: call `optimizer.zero_grad()` before `backward()` each step.
- ⚠️ Keras expects the right input shape; the first layer needs `input_shape`/`Input`.
- ⚠️ Framework version differences (TF1 vs TF2, torch APIs) break old tutorials — check versions.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

