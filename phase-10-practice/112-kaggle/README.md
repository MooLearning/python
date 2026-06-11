# 112 — Kaggle

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Kaggle** is a platform for data-science competitions, datasets, notebooks, and learning. A competition gives you a **training set** (with labels) and a **test set** (without); you build a model and submit predictions, scored on a hidden leaderboard. The standard loop: EDA → baseline model → **cross-validation** → feature engineering → ensembling → submit. It's the best place to practice end-to-end ML on real data.

## Why it matters

Kaggle gives real datasets, public baselines, and instant feedback. Competing (or just completing) builds practical skills — data cleaning, validation discipline, and feature engineering — far faster than tutorials alone.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install pandas scikit-learn
```

## Key concepts

- **Train/test split** — Labeled train; unlabeled test you predict on.
- **Baseline first** — A simple model to beat before getting fancy.
- **Cross-validation** — Trust local CV over leaderboard to avoid overfitting it.
- **Feature engineering** — Often the biggest source of score gains.
- **Submission file** — Usually a CSV of id,prediction rows.
- **Leaderboard** — Public (partial) vs private (final) — don't overfit public.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
steps = [
    "1. Understand the problem and the evaluation metric",
    "2. EDA: explore distributions, missing values, correlations",
    "3. Build a BASELINE (e.g. predict the mean / a simple model)",
    "4. Set up cross-validation you trust",
    "5. Feature engineering + better models",
    "6. Tune hyperparameters; try ensembling",
    "7. Generate predictions on the test set",
    "8. Write submission.csv and submit",
]
for s in steps:
    print(s)
print("\nGolden rule: trust your local CV score over the public leaderboard.")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Don't overfit the PUBLIC leaderboard — the private split decides final rank.
- ⚠️ Build robust cross-validation early and trust it over leaderboard noise.
- ⚠️ Avoid leakage: never fit preprocessing on test data or use future/target info.
- ⚠️ A strong baseline beats a fancy model with bugs — get end-to-end working first.
- ⚠️ Match the EXACT submission format (column names, id order) or it's rejected.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

