# 26 — Datetime: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Print today's date using date.today() (any date is fine).

*Hint: date.today().*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date
print(date.today())
```

</details>

## Exercise 2

Compute the date 100 days after 2026-01-01.

*Hint: timedelta(days=100).*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date, timedelta
print(date(2026, 1, 1) + timedelta(days=100))  # 2026-04-11
```

</details>

## Exercise 3

How many days are between 2026-01-01 and 2026-12-31?

*Hint: Subtract dates.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date
print((date(2026, 12, 31) - date(2026, 1, 1)).days)  # 364
```

</details>

## Exercise 4

Format datetime(2026,6,9,9,5) as 'YYYY-MM-DD HH:MM'.

*Hint: strftime.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import datetime
print(datetime(2026, 6, 9, 9, 5).strftime("%Y-%m-%d %H:%M"))  # 2026-06-09 09:05
```

</details>

## Exercise 5

Parse '09/06/2026' (DD/MM/YYYY) into a date object.

*Hint: strptime with %d/%m/%Y.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import datetime
print(datetime.strptime("09/06/2026", "%d/%m/%Y").date())  # 2026-06-09
```

</details>

## Exercise 6

Find the weekday name of 2026-06-09.

*Hint: strftime %A.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date
print(date(2026, 6, 9).strftime("%A"))  # Tuesday
```

</details>

## Exercise 7

Given a birthdate 2000-06-09, compute age in whole years as of 2026-06-09.

*Hint: Year diff with adjustment.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date
b, t = date(2000, 6, 9), date(2026, 6, 9)
age = t.year - b.year - ((t.month, t.day) < (b.month, b.day))
print(age)  # 26
```

</details>

## Exercise 8

Convert datetime(2026,6,9,14,30) to ISO format and back.

*Hint: isoformat / fromisoformat.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import datetime
s = datetime(2026, 6, 9, 14, 30).isoformat()
print(s, "->", datetime.fromisoformat(s))
```

</details>

