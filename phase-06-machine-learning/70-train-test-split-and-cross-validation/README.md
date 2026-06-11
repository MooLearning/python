# 70 — Train/Test Split and Cross-Validation

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

To estimate how a model generalizes, you **hold out** data it never trains on. A **train/test split** (e.g. 80/20) trains on one part and evaluates on the other. **K-fold cross-validation** does this k times — each fold is the test set once — and averages the scores, giving a more reliable estimate that uses all the data for both training and validation.

## Why it matters

Evaluating on training data overstates performance (memorization). Splits and cross-validation give honest estimates, reduce the luck of a single split, and are the basis for comparing models and tuning hyperparameters.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Train/test split** — Hold out a fraction (e.g. 20%) for final evaluation.
- **Shuffle + seed** — Randomize order; fix a seed for reproducibility.
- **K-fold CV** — Split into k folds; each is the validation set once.
- **Stratified** — Keep class proportions balanced across folds.
- **Validation set** — A third split for tuning, separate from the final test.
- **Average score** — CV reports mean ± std across folds, not one number.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import random

data = list(range(1, 11))          # 10 samples
random.seed(42)
random.shuffle(data)               # shuffle so the split isn't biased

split = int(0.8 * len(data))       # 80% train
train, test = data[:split], data[split:]
print("train:", train)             # 8 items
print("test :", test)              # 2 items
print(f"{len(train)} train / {len(test)} test")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Always shuffle before splitting (unless it's time series) — ordered data biases the split.
- ⚠️ Fit preprocessing on the TRAIN fold only inside CV, or you leak test info.
- ⚠️ Use stratified splits for imbalanced classes so each fold has all classes.
- ⚠️ Never tune on the final test set — use a validation set or CV, then test once at the end.
- ⚠️ For time series, use forward-chaining splits — random shuffling leaks the future.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

