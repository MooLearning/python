# 66 — Exploratory Data Analysis (EDA)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Exploratory Data Analysis (EDA)** is the first look at a dataset: compute summary statistics (count, mean, min/max, quartiles), check distributions, spot missing values and outliers, and examine relationships between variables (correlation). The goal is to **understand** the data and form hypotheses before modeling.

## Why it matters

EDA catches data-quality problems, surprising distributions, and leakage early — saving you from training models on broken data. It guides which features to engineer and which models are appropriate.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install pandas
```

## Key concepts

- **Summary statistics** — count, mean, std, min, quartiles, max per column.
- **Distribution shape** — Symmetric, skewed, multimodal? Histograms reveal it.
- **Missing values** — How many, and where? Decide impute vs drop.
- **Outliers** — Extreme values that distort means and models.
- **Correlation** — Which features move together (and with the target).
- **Cardinality** — How many distinct values a categorical column has.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import statistics as st

ages = [23, 25, 31, 35, 41, 22, 29, 33, 60, 27]

print("count :", len(ages))
print("mean  :", round(st.mean(ages), 2))
print("median:", st.median(ages))
print("stdev :", round(st.stdev(ages), 2))
print("min   :", min(ages), " max:", max(ages))

# Quartiles (Q1, Q2, Q3)
q1, q2, q3 = st.quantiles(ages, n=4)
print(f"quartiles: Q1={q1}, Q2={q2}, Q3={q3}")
print("range :", max(ages) - min(ages))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ The mean hides skew and outliers — always look at median and a histogram too.
- ⚠️ Correlation only captures LINEAR relationships; a 0 correlation can still hide a curve.
- ⚠️ Don't impute or drop missing values before understanding WHY they're missing.
- ⚠️ High-cardinality categoricals (IDs, names) usually aren't useful features as-is.
- ⚠️ Quantile methods differ (inclusive vs exclusive) — small datasets give slightly different quartiles.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

