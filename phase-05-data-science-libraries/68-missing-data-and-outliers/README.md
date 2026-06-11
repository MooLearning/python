# 68 — Missing Data and Outliers

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Real data has holes and extremes. **Missing data** (NaN/None) must be handled by **dropping** rows/columns or **imputing** (filling with mean/median/mode or a model). **Outliers** are values far from the rest; detect them with the **IQR rule** (outside Q1−1.5·IQR or Q3+1.5·IQR) or **z-scores** (|z| > 3), then decide to keep, cap, or remove.

## Why it matters

Missing values crash many algorithms, and outliers distort means, scaling, and model fits. Handling them well is essential to trustworthy analysis — and how you handle them can change your conclusions.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install pandas
```

## Key concepts

- **Detect missing** — Find None/NaN before doing math on a column.
- **Drop** — Remove rows/columns with missing values (simple, can lose data).
- **Impute** — Fill missing with mean/median/mode or a predicted value.
- **IQR rule** — Outlier if below Q1−1.5·IQR or above Q3+1.5·IQR.
- **Z-score rule** — Outlier if |(x−μ)/σ| exceeds ~3.
- **Cap (winsorize)** — Clip extremes to a threshold instead of deleting.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import statistics as st

data = [10, 20, None, 40, None, 60]

# Detect
missing = [i for i, x in enumerate(data) if x is None]
print("missing at indices:", missing)        # [2, 4]

present = [x for x in data if x is not None]

# Impute with the mean
mean_val = st.mean(present)
mean_filled = [mean_val if x is None else x for x in data]
print("mean-imputed  :", mean_filled)

# Impute with the median (robust to outliers)
median_val = st.median(present)
median_filled = [median_val if x is None else x for x in data]
print("median-imputed:", median_filled)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Imputing with the MEAN is skewed by outliers — the median is usually safer.
- ⚠️ Dropping rows with any NaN can throw away most of your data; check how much you lose.
- ⚠️ Not every outlier is an error — some are the most important signal (fraud, failures).
- ⚠️ Impute using TRAINING statistics only; using test stats leaks information.
- ⚠️ NaN != NaN in floats; test with `math.isnan`/`pd.isna`, not `== None`, for float columns.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

