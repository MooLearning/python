# 59 — Probability and Statistics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Statistics** summarizes data (mean, median, variance, standard deviation, correlation); **probability** quantifies uncertainty (the chance of events between 0 and 1). Together they let us describe datasets, reason about randomness, and judge whether a pattern is real or noise. Python's `statistics` module and `random` module cover the basics with no installs.

## Why it matters

ML is applied statistics: we estimate parameters from samples, measure spread and relationships, and quantify confidence. Mean/variance/correlation and basic probability (including Bayes' theorem) underpin metrics, feature analysis, and model evaluation.

## Key concepts

- **Mean / median / mode** — Center of data: average, middle value, most frequent.
- **Variance / std dev** — Spread: average squared distance from the mean (and its root).
- **Probability** — Chance of an event in [0, 1]; complement is 1 − P.
- **Combinations** — Count ways to choose k of n (order ignored): n!/(k!(n−k)!).
- **Correlation** — How two variables move together, from −1 to +1.
- **Bayes' theorem** — Update a probability given new evidence.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import statistics as st

data = [4, 8, 15, 16, 23, 42]
print("mean    :", st.mean(data))                 # 18
print("median  :", st.median(data))               # 15.5
print("stdev   :", round(st.stdev(data), 3))      # sample std dev
print("variance:", round(st.variance(data), 3))   # sample variance

scores = [90, 85, 85, 70, 95, 85]
print("mode    :", st.mode(scores))               # 85 (most frequent)

# Compute the mean and variance by hand to see the formula
n = len(data)
mean = sum(data) / n
var = sum((x - mean) ** 2 for x in data) / n      # population variance
print("by hand : mean =", mean, " pop_var =", round(var, 3))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Sample variance divides by (n−1); population variance divides by n — know which you need.
- ⚠️ The mean is sensitive to outliers; the median is robust — report both for skewed data.
- ⚠️ Correlation is NOT causation — a strong correlation can be coincidental or confounded.
- ⚠️ Probabilities must lie in [0, 1] and a full set of outcomes must sum to 1.
- ⚠️ Bayes surprises people: a 99%-accurate test can still mostly flag healthy people if the disease is rare.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

