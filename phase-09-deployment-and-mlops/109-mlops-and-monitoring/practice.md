# 109 — MLOps and Monitoring: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the mean shift in std devs: train mean 5 std 1, prod mean 7.

*Hint: z = |diff|/std.*

<details>
<summary>✅ Solution</summary>

```python
print(abs(7 - 5) / 1)  # 2.0
```

</details>

## Exercise 2

Data drift vs concept drift: which changes inputs only?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Data drift** — the input distribution changes while the input→output relationship
may stay the same. **Concept drift** is when that relationship itself changes.

</details>

## Exercise 3

PSI term for one bin: (a-e)*ln(a/e), a=0.4,e=0.25.

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
import math
a, e = 0.4, 0.25
print(round((a - e) * math.log(a / e), 4))
```

</details>

## Exercise 4

Compute the p50 (median) latency of [10,20,30].

*Hint: Median.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
print(st.median([10, 20, 30]))  # 20
```

</details>

## Exercise 5

What does a model registry store?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Versioned models with metadata** (metrics, training data/version, stage like
staging/production) — enabling rollback, auditing, and controlled promotion.

</details>

## Exercise 6

PSI of 0.3 means what?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Significant drift** (rule of thumb PSI > 0.25). The production distribution has
shifted enough from training that you should investigate/retrain.

</details>

## Exercise 7

Why monitor input drift when labels are delayed?

*Hint: Early signal.*

<details>
<summary>✅ Solution</summary>

True accuracy needs ground-truth labels, which often arrive late. **Input drift** is
an **early proxy** — if inputs shift, performance is likely degrading before labels
confirm it.

</details>

## Exercise 8

Compute positive rate of predictions [1,0,1,1].

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
p = [1, 0, 1, 1]
print(sum(p) / len(p))  # 0.75
```

</details>

