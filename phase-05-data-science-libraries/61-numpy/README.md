# 61 — NumPy

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**NumPy** is the foundation of scientific Python. Its core object is the **ndarray**: a fast, fixed-type N-dimensional array. NumPy runs **vectorized** operations in compiled C, so `arr * 2` transforms a million numbers without a Python loop. It adds **broadcasting** (operating on different-shaped arrays), powerful **slicing/masking**, and a huge library of math, linear-algebra, and random functions.

## Why it matters

Pandas, scikit-learn, matplotlib, TensorFlow, and PyTorch all build on NumPy arrays. Vectorization makes numeric code 10–100× faster and far shorter than pure-Python loops — it's the workhorse of all data science and ML.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install numpy
```

## Key concepts

- **ndarray** — A fixed-type, N-dimensional array; the central NumPy object.
- **Vectorization** — Elementwise ops over whole arrays with no Python loop.
- **Broadcasting** — Auto-expanding shapes so arrays of different sizes combine.
- **Slicing & masking** — `a[1:3]`, `a[a > 0]` select sub-arrays (views, not copies).
- **Axis** — Aggregate along rows (axis=1) or columns (axis=0).
- **dtype & shape** — Every array has a data type and a shape tuple.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
try:
    import numpy as np

    a = np.array([1, 2, 3, 4, 5])
    print("array :", a, "| shape", a.shape, "| dtype", a.dtype)
    print("a * 2 :", a * 2)            # vectorized: [ 2  4  6  8 10]
    print("a + 10:", a + 10)           # broadcast a scalar
    print("a ** 2:", a ** 2)           # [ 1  4  9 16 25]
    print("sum   :", a.sum(), "mean", a.mean(), "std", round(float(a.std()), 3))

    # Handy constructors
    print("zeros :", np.zeros(3))
    print("range :", np.arange(0, 10, 2))      # [0 2 4 6 8]
    print("linsp :", np.linspace(0, 1, 5))     # 5 evenly spaced points
except ImportError:
    print("NumPy not installed — run: pip install numpy")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Array slices are VIEWS, not copies — modifying a slice changes the original. Use `.copy()`.
- ⚠️ NumPy arrays are fixed-dtype; mixing types silently up-casts (ints become floats).
- ⚠️ `*` is ELEMENTWISE multiply; use `@` or `np.dot` for matrix multiplication.
- ⚠️ Broadcasting only works when trailing dimensions match (or are 1) — otherwise it errors.
- ⚠️ Integer arrays overflow silently in some dtypes; watch for unexpected negatives.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

