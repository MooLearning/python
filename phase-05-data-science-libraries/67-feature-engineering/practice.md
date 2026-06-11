# 67 — Feature Engineering: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create a 'bmi' feature from weight=70kg, height=1.75m.

*Hint: weight / height^2.*

<details>
<summary>✅ Solution</summary>

```python
weight, height = 70, 1.75
print(round(weight / height ** 2, 2))  # 22.86
```

</details>

## Exercise 2

Compute price_per_unit for price=120, units=4.

*Hint: Ratio.*

<details>
<summary>✅ Solution</summary>

```python
print(120 / 4)  # 30.0
```

</details>

## Exercise 3

Bin score 85 into 'low'(<60),'mid'(<80),'high'.

*Hint: If/elif.*

<details>
<summary>✅ Solution</summary>

```python
def bucket(s):
    return "low" if s < 60 else "mid" if s < 80 else "high"
print(bucket(85))  # high
```

</details>

## Exercise 4

Extract the weekday name from date(2026,6,9).

*Hint: strftime.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date
print(date(2026, 6, 9).strftime("%A"))  # Tuesday
```

</details>

## Exercise 5

Log-transform the value 1000.

*Hint: math.log.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(round(math.log(1000), 3))  # 6.908
```

</details>

## Exercise 6

Create an interaction feature x*y for x=3,y=4.

*Hint: Multiply.*

<details>
<summary>✅ Solution</summary>

```python
x, y = 3, 4
print(x * y)  # 12
```

</details>

## Exercise 7

Make an is_weekend flag for date(2026,6,13) (a Saturday).

*Hint: weekday()>=5.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date
print(date(2026, 6, 13).weekday() >= 5)  # True
```

</details>

## Exercise 8

Square the feature 5 to capture a non-linear effect.

*Hint: x**2.*

<details>
<summary>✅ Solution</summary>

```python
print(5 ** 2)  # 25
```

</details>

