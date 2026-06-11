# 59 — Probability and Statistics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the mean of [2,4,6,8].

*Hint: Sum / count.*

<details>
<summary>✅ Solution</summary>

```python
data = [2, 4, 6, 8]
print(sum(data) / len(data))  # 5.0
```

</details>

## Exercise 2

Find the median of [7,1,3,9,5].

*Hint: Sort, take middle.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
print(st.median([7, 1, 3, 9, 5]))  # 5
```

</details>

## Exercise 3

Compute the population variance of [1,2,3,4,5].

*Hint: Mean squared deviation.*

<details>
<summary>✅ Solution</summary>

```python
data = [1, 2, 3, 4, 5]
m = sum(data) / len(data)
print(sum((x - m) ** 2 for x in data) / len(data))  # 2.0
```

</details>

## Exercise 4

What is P(even) when rolling a fair die?

*Hint: 3 of 6 outcomes.*

<details>
<summary>✅ Solution</summary>

```python
print(3 / 6)  # 0.5
```

</details>

## Exercise 5

How many ways to choose 3 from 6 (combinations)?

*Hint: math.comb.*

<details>
<summary>✅ Solution</summary>

```python
from math import comb
print(comb(6, 3))  # 20
```

</details>

## Exercise 6

Find the mode of [1,2,2,3,3,3,4].

*Hint: Most frequent.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
print(st.mode([1, 2, 2, 3, 3, 3, 4]))  # 3
```

</details>

## Exercise 7

Compute P(at least one 6 in two rolls).

*Hint: 1 - P(no 6).*

<details>
<summary>✅ Solution</summary>

```python
p_no_six = (5 / 6) ** 2
print(round(1 - p_no_six, 4))  # 0.3056
```

</details>

## Exercise 8

Estimate P(heads) from 10000 simulated coin flips.

*Hint: random + count.*

<details>
<summary>✅ Solution</summary>

```python
import random
random.seed(0)
flips = [random.choice("HT") for _ in range(10000)]
print(round(flips.count("H") / len(flips), 2))  # ~0.5
```

</details>

