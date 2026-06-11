# 65 — Data Preprocessing

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Data preprocessing** transforms raw data into a clean, numeric form models can use: **scaling** features to comparable ranges (min-max or standardization), **encoding** categorical text into numbers (label or one-hot), and splitting data. Models like KNN, SVM, and neural nets are sensitive to feature scale, so preprocessing often decides whether they work at all.

## Why it matters

'Garbage in, garbage out.' Most ML effort is data prep. Correct scaling and encoding prevent features with big numbers from dominating and let algorithms converge — frequently more impactful than the model choice.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Min-max scaling** — Rescale to [0, 1]: (x − min)/(max − min).
- **Standardization** — Center & scale to mean 0, std 1: (x − μ)/σ.
- **Label encoding** — Map categories to integers (for ordinal data/trees).
- **One-hot encoding** — Each category becomes its own 0/1 column.
- **Fit on train only** — Learn scaling params from training data, then apply to test.
- **Pipelines** — Chain preprocessing + model so steps stay consistent.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import statistics as st

data = [10, 20, 30, 40, 50]

# Min-max scaling to [0, 1]
lo, hi = min(data), max(data)
minmax = [(x - lo) / (hi - lo) for x in data]
print("min-max     :", minmax)            # [0.0, 0.25, 0.5, 0.75, 1.0]

# Standardization (z-scores): mean 0, std 1
mu = st.mean(data)
sigma = st.pstdev(data)                    # population std
standardized = [(x - mu) / sigma for x in data]
print("standardized:", [round(z, 3) for z in standardized])
print("new mean ~", round(st.mean(standardized), 6))   # ~0
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Fit scalers/encoders on the TRAINING set only, then transform test — fitting on all data leaks.
- ⚠️ One-hot encoding high-cardinality columns explodes dimensions; group rare categories first.
- ⚠️ Label encoding implies an ORDER (0<1<2); don't use it for unordered categories in linear models.
- ⚠️ Standardize for distance/gradient models (KNN, SVM, NN); tree models barely care about scale.
- ⚠️ Apply the SAME fitted transform to new data — re-fitting on test changes the scale.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

