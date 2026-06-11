# 67 — Feature Engineering

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Feature engineering** creates better input variables from raw data so models can learn more easily: deriving new columns (ratios, differences, date parts), **binning** continuous values, **polynomial/interaction** terms, encoding categoricals, and transforming skewed features (log). Good features often beat fancier algorithms.

## Why it matters

Models can only use the signal you expose. Thoughtful features (e.g. 'price per square foot' instead of price and area separately) inject domain knowledge and frequently produce the biggest accuracy gains in practical ML.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Derived features** — Combine columns: ratios, sums, differences, rates.
- **Date/time parts** — Extract year, month, day-of-week, is_weekend.
- **Binning** — Bucket a continuous variable into ranges/categories.
- **Polynomial & interaction** — x², x·y capture non-linear effects.
- **Log transform** — Compress skewed/heavy-tailed features.
- **Aggregations** — Group-level stats (mean per category) as features.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

houses = [
    {"price": 300_000, "area": 1500, "rooms": 3},
    {"price": 500_000, "area": 2000, "rooms": 4},
    {"price": 250_000, "area": 1000, "rooms": 2},
]

for h in houses:
    h["price_per_sqft"] = round(h["price"] / h["area"], 2)   # ratio feature
    h["area_per_room"] = round(h["area"] / h["rooms"], 1)
    h["log_price"] = round(math.log(h["price"]), 3)          # tame skew

for h in houses:
    print(h)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Don't engineer features using the target in a leaky way (e.g. target mean of the same row).
- ⚠️ Compute group aggregates on TRAIN folds only, or you leak test information.
- ⚠️ Polynomial expansion explodes dimensions fast — degree 3 on many features is huge.
- ⚠️ Log transforms need positive values; shift by a constant if zeros/negatives appear.
- ⚠️ More features isn't always better — irrelevant ones add noise and overfitting risk.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

