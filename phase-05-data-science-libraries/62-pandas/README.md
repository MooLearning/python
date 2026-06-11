# 62 — pandas

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**pandas** is the go-to library for tabular data. Its two structures are the **Series** (a labeled 1-D array) and the **DataFrame** (a labeled 2-D table, like a spreadsheet). pandas makes loading (CSV/Excel/SQL), cleaning, filtering, transforming, **grouping**, and summarizing data concise and fast. It's where most real data analysis starts.

## Why it matters

Real datasets are tables, and pandas is the standard tool to wrangle them: select columns, filter rows, handle missing values, join tables, and compute group statistics — the daily work of data science before any model is trained.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install pandas
```

## Key concepts

- **Series** — A labeled 1-D column of values.
- **DataFrame** — A labeled 2-D table of rows and columns.
- **Selection** — `df['col']`, `df.loc[label]`, `df.iloc[pos]`.
- **Boolean filtering** — `df[df['age'] > 30]` keeps matching rows.
- **groupby** — Split-apply-combine: group rows and aggregate.
- **Missing data** — `isna()`, `fillna()`, `dropna()` handle NaNs.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
try:
    import pandas as pd

    df = pd.DataFrame({
        "name": ["Ada", "Bob", "Cy", "Dee"],
        "age": [30, 25, 35, 28],
        "city": ["NYC", "LA", "NYC", "LA"],
    })
    print(df)
    print("\nshape   :", df.shape)        # (4, 3)
    print("columns :", list(df.columns))
    print("\ndescribe (numeric):")
    print(df["age"].describe())
except ImportError:
    print("pandas not installed — run: pip install pandas")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `df['col']` returns a Series; `df[['col']]` (double brackets) returns a DataFrame.
- ⚠️ Chained indexing like `df[df.a>0]['b'] = 1` may not assign — use `.loc[mask, 'b']`.
- ⚠️ Operations return NEW frames by default; assign the result or use `inplace=`/reassign.
- ⚠️ Missing values are NaN (a float) — they propagate; handle with fillna/dropna before math.
- ⚠️ `groupby` skips NaN keys by default and returns a grouped object — you must aggregate it.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

