# 60 — Distributions: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Sample 1000 values from a uniform [0,1) and print the mean.

*Hint: random.random.*

<details>
<summary>✅ Solution</summary>

```python
import random, statistics as st
random.seed(0)
print(round(st.mean([random.random() for _ in range(1000)]), 1))  # ~0.5
```

</details>

## Exercise 2

Sample from a normal(mean=100, std=15) and print one value.

*Hint: random.gauss.*

<details>
<summary>✅ Solution</summary>

```python
import random
random.seed(0)
print(round(random.gauss(100, 15), 2))
```

</details>

## Exercise 3

Compute the binomial probability of exactly 2 heads in 4 flips.

*Hint: comb * p^k * q^(n-k).*

<details>
<summary>✅ Solution</summary>

```python
from math import comb
print(round(comb(4, 2) * 0.5 ** 4, 4))  # 0.375
```

</details>

## Exercise 4

Compute the z-score of 85 given mean 75, std 5.

*Hint: (x-mu)/sigma.*

<details>
<summary>✅ Solution</summary>

```python
print((85 - 75) / 5)  # 2.0
```

</details>

## Exercise 5

Compute the Poisson probability of 0 events when lambda=3.

*Hint: e^-lambda.*

<details>
<summary>✅ Solution</summary>

```python
from math import exp
print(round(exp(-3), 4))  # 0.0498
```

</details>

## Exercise 6

Verify a binomial(n=3,p=0.5) PMF sums to 1.

*Hint: Sum over k.*

<details>
<summary>✅ Solution</summary>

```python
from math import comb
print(round(sum(comb(3, k) * 0.5 ** 3 for k in range(4)), 6))  # 1.0
```

</details>

## Exercise 7

Evaluate the standard normal density at x=0.

*Hint: 1/sqrt(2pi).*

<details>
<summary>✅ Solution</summary>

```python
import math
print(round(1 / math.sqrt(2 * math.pi), 4))  # 0.3989
```

</details>

## Exercise 8

Estimate P(|z|<=1) for a standard normal by simulation.

*Hint: Count within 1 std.*

<details>
<summary>✅ Solution</summary>

```python
import random
random.seed(1)
s = [random.gauss(0, 1) for _ in range(50000)]
print(round(sum(1 for x in s if abs(x) <= 1) / len(s), 2))  # ~0.68
```

</details>

