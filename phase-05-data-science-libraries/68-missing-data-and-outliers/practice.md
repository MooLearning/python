# 68 — Missing Data and Outliers: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Count the missing (None) values in [1,None,3,None,5].

*Hint: Sum a condition.*

<details>
<summary>✅ Solution</summary>

```python
data = [1, None, 3, None, 5]
print(sum(1 for x in data if x is None))  # 2
```

</details>

## Exercise 2

Impute missing with the mean of present values in [2,None,4].

*Hint: Mean of [2,4].*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
data = [2, None, 4]
present = [x for x in data if x is not None]
m = st.mean(present)
print([m if x is None else x for x in data])  # [2, 3, 4]
```

</details>

## Exercise 3

Compute the IQR of [1,2,3,4,5,6,7,8].

*Hint: Q3 - Q1.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
q1, _, q3 = st.quantiles([1, 2, 3, 4, 5, 6, 7, 8], n=4)
print(q3 - q1)
```

</details>

## Exercise 4

Flag outliers in [10,11,12,13,90] with the IQR rule.

*Hint: Outside fences.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
d = [10, 11, 12, 13, 90]
q1, _, q3 = st.quantiles(d, n=4); iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print([x for x in d if x < lo or x > hi])  # [90]
```

</details>

## Exercise 5

Impute with the median of [5,None,7,9].

*Hint: Robust fill.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
data = [5, None, 7, 9]
present = [x for x in data if x is not None]
med = st.median(present)
print([med if x is None else x for x in data])
```

</details>

## Exercise 6

Cap the value 150 to a max of 100.

*Hint: min(x, cap).*

<details>
<summary>✅ Solution</summary>

```python
print(min(150, 100))  # 100
```

</details>

## Exercise 7

Compute the z-score of 90 in data mean=50,std=20.

*Hint: (x-mu)/sigma.*

<details>
<summary>✅ Solution</summary>

```python
print((90 - 50) / 20)  # 2.0
```

</details>

## Exercise 8

Drop all None values from [1,None,2,None,3].

*Hint: List comprehension.*

<details>
<summary>✅ Solution</summary>

```python
data = [1, None, 2, None, 3]
print([x for x in data if x is not None])  # [1, 2, 3]
```

</details>

