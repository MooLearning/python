# 75 — Support Vector Machines (SVM)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **Support Vector Machine (SVM)** finds the **decision boundary** (hyperplane) that separates classes with the **widest margin** — the largest gap to the nearest points (the **support vectors**). For non-linear data, the **kernel trick** (e.g. RBF) implicitly maps features into a higher-dimensional space where a linear separator exists.

## Why it matters

SVMs are powerful, work well in high dimensions, and were state-of-the-art for many tasks before deep learning. The margin idea and kernels are important concepts; SVMs remain strong for small/medium structured datasets and text.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Hyperplane** — The linear boundary w·x + b = 0 separating classes.
- **Margin** — Distance from the boundary to the nearest points; SVM maximizes it.
- **Support vectors** — The closest points that define the margin.
- **Kernel trick** — Implicitly map to higher dimensions (linear, poly, RBF).
- **C parameter** — Trades margin width vs misclassification (regularization).
- **gamma (RBF)** — How far each point's influence reaches; controls flexibility.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# A hand-chosen boundary: x + y - 5 = 0. Sign tells the side/class.
def classify(point, w=(1, 1), b=-5):
    score = sum(wi * xi for wi, xi in zip(w, point)) + b
    return 1 if score >= 0 else 0, round(score, 2)

for p in [(1, 1), (4, 4), (3, 2), (5, 5)]:
    label, score = classify(p)
    print(f"{p}: score={score:5} -> class {label}")
# The 'margin' is how far points sit from score == 0.
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Scale features before an SVM — like KNN, it's distance/margin based.
- ⚠️ The RBF kernel needs tuning of C and gamma; bad values badly under/overfit.
- ⚠️ SVMs don't output probabilities by default (enable `probability=True`, which is slower).
- ⚠️ They scale poorly to very large datasets (training is roughly quadratic).
- ⚠️ A linear kernel can't separate non-linear data (e.g. concentric circles) — use RBF/poly.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

