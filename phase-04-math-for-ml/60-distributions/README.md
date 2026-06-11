# 60 — Distributions

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **probability distribution** describes how likely each outcome is. **Discrete** distributions (Bernoulli, **binomial**, Poisson) assign probabilities to countable outcomes; **continuous** ones (**uniform**, **normal/Gaussian**) describe densities over a range. The **normal distribution** — the bell curve — is central to ML because of the Central Limit Theorem and the 68–95–99.7 rule.

## Why it matters

Models assume distributions (Naive Bayes assumes Gaussian features; errors are often assumed normal). Knowing distributions helps you simulate data, standardize features (z-scores), spot outliers, and understand sampling and confidence.

## Key concepts

- **Uniform** — Every value in a range equally likely.
- **Bernoulli / Binomial** — One trial / number of successes in n independent trials.
- **Poisson** — Count of rare events in a fixed interval.
- **Normal (Gaussian)** — Symmetric bell curve defined by mean μ and std σ.
- **68–95–99.7 rule** — Fraction of normal data within 1, 2, 3 std devs.
- **Z-score** — (x − μ)/σ: how many std devs from the mean a value sits.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import random
import statistics as st

random.seed(0)

# Uniform: every value in [0, 1) equally likely
uniform_sample = [random.random() for _ in range(10_000)]
print("uniform mean ~", round(st.mean(uniform_sample), 3))   # ~0.5

# Normal (Gaussian): bell curve with mean=50, std=10
normal_sample = [random.gauss(50, 10) for _ in range(10_000)]
print("normal mean ~", round(st.mean(normal_sample), 2))     # ~50
print("normal std  ~", round(st.stdev(normal_sample), 2))    # ~10

# A quick text histogram of the normal sample
buckets = {}
for x in normal_sample:
    b = int(x // 10) * 10
    buckets[b] = buckets.get(b, 0) + 1
for b in sorted(buckets):
    print(f"{b:3d}-{b+9:3d} | {'#' * (buckets[b] // 100)}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ A continuous PDF gives DENSITY, not probability — P(X = exact value) is 0; use ranges/areas.
- ⚠️ Binomial assumes independent trials with a CONSTANT success probability.
- ⚠️ `random.gauss(mu, sigma)` takes the standard deviation, not the variance.
- ⚠️ Real data is often skewed or heavy-tailed — don't assume normal without checking.
- ⚠️ Z-scores need the population/sample mean and std; computing them on tiny samples is unreliable.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

