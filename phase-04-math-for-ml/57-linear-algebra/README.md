# 57 — Linear Algebra

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Linear algebra** is the math of **vectors** (ordered lists of numbers) and **matrices** (grids of numbers). Core operations are vector addition, **dot products**, **matrix multiplication**, and **transpose**. Machine learning represents data as vectors/matrices and expresses models (a linear layer, a rotation, a projection) as matrix operations — so this is the language ML is written in.

## Why it matters

Every dataset is a matrix (rows = samples, columns = features); every neural-network layer is a matrix multiply. Understanding dot products, shapes, and matrix multiply makes ML math (and NumPy/PyTorch code) click instead of feeling like magic.

## Key concepts

- **Vector** — An ordered list of numbers; a point/arrow in n-D space.
- **Dot product** — Sum of elementwise products; measures alignment/similarity.
- **Matrix** — A 2-D grid; shape (rows, cols).
- **Matrix multiply** — (m×n)·(n×p) → (m×p); inner dimensions must match.
- **Transpose** — Flip rows and columns: shape (m,n) → (n,m).
- **Magnitude (norm)** — Length of a vector: sqrt(sum of squares).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

def add(u, v):       return [a + b for a, b in zip(u, v)]
def scale(k, v):     return [k * x for x in v]
def dot(u, v):       return sum(a * b for a, b in zip(u, v))
def magnitude(v):    return math.sqrt(dot(v, v))

u = [1, 2, 3]
v = [4, 5, 6]
print("u + v   :", add(u, v))        # [5, 7, 9]
print("3 * u   :", scale(3, u))      # [3, 6, 9]
print("u . v   :", dot(u, v))        # 32  (1*4 + 2*5 + 3*6)
print("|u|     :", round(magnitude(u), 4))   # 3.7417

# Cosine similarity = dot / (|u| * |v|)  -> how aligned two vectors are
cos_sim = dot(u, v) / (magnitude(u) * magnitude(v))
print("cos_sim :", round(cos_sim, 4))        # 0.9746
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Matrix multiply needs matching INNER dimensions: (m×n)·(n×p). Mismatched shapes error.
- ⚠️ Matrix multiplication is NOT commutative: A·B ≠ B·A in general.
- ⚠️ The dot product needs equal-length vectors — zip silently stops at the shorter one!
- ⚠️ `*` on NumPy arrays is ELEMENTWISE; matrix multiply is `@` or `np.dot`.
- ⚠️ Mixing row vectors and column vectors causes shape bugs — track shapes deliberately.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

