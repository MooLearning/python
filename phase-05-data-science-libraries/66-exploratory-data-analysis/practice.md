# 66 — Exploratory Data Analysis (EDA): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute mean, median, min, max of [4,8,6,2,10].

*Hint: statistics + builtins.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
d = [4, 8, 6, 2, 10]
print(st.mean(d), st.median(d), min(d), max(d))
```

</details>

## Exercise 2

Find the range (max-min) of [12,5,9,20,3].

*Hint: max - min.*

<details>
<summary>✅ Solution</summary>

```python
d = [12, 5, 9, 20, 3]
print(max(d) - min(d))  # 17
```

</details>

## Exercise 3

Count the distinct values in ['x','y','x','z'].

*Hint: set length.*

<details>
<summary>✅ Solution</summary>

```python
print(len(set(["x", "y", "x", "z"])))  # 3
```

</details>

## Exercise 4

Compute the quartiles of [1,2,3,4,5,6,7,8].

*Hint: statistics.quantiles.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
print(st.quantiles([1, 2, 3, 4, 5, 6, 7, 8], n=4))
```

</details>

## Exercise 5

Get value counts of ['a','b','a','a','b'].

*Hint: Counter.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(dict(Counter(["a", "b", "a", "a", "b"])))  # {'a':3,'b':2}
```

</details>

## Exercise 6

Find the most common grade in ['A','B','A','C','A'].

*Hint: most_common.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter(["A", "B", "A", "C", "A"]).most_common(1)[0][0])  # A
```

</details>

## Exercise 7

Compute the standard deviation of [2,4,4,4,5,5,7,9].

*Hint: pstdev.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
print(st.pstdev([2, 4, 4, 4, 5, 5, 7, 9]))  # 2.0
```

</details>

## Exercise 8

Why look at the median in addition to the mean?

*Hint: Robustness.*

<details>
<summary>✅ Solution</summary>

The **median** is robust to outliers and skew, while the **mean** gets dragged
toward extreme values. Comparing them reveals skew: if mean >> median, the data
has a long right tail (a few large values).

</details>

