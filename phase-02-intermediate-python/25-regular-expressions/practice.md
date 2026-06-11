# 25 — Regular Expressions: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Extract all numbers from 'a1b22c333' as a list of strings.

*Hint: findall with \d+.*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.findall(r"\d+", "a1b22c333"))  # ['1', '22', '333']
```

</details>

## Exercise 2

Check whether 'Hello123' contains any digit.

*Hint: search \d.*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.search(r"\d", "Hello123") is not None)  # True
```

</details>

## Exercise 3

Replace every whitespace run in 'a  b   c' with a single space.

*Hint: sub \s+.*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.sub(r"\s+", " ", "a  b   c"))  # 'a b c'
```

</details>

## Exercise 4

Validate a simple phone format like 123-456-7890.

*Hint: Anchors + {n}.*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.match(r"^\d{3}-\d{3}-\d{4}$", "123-456-7890") is not None)  # True
```

</details>

## Exercise 5

Split 'one,two;three four' on commas, semicolons, or spaces.

*Hint: split with a class.*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.split(r"[,; ]+", "one,two;three four"))  # ['one','two','three','four']
```

</details>

## Exercise 6

Capture the year and month from '2026-06'.

*Hint: Two groups.*

<details>
<summary>✅ Solution</summary>

```python
import re
m = re.search(r"(\d{4})-(\d{2})", "2026-06")
print(m.groups())  # ('2026', '06')
```

</details>

## Exercise 7

Find all words starting with a capital letter in 'The Quick Brown fox'.

*Hint: [A-Z]\w*.*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.findall(r"\b[A-Z]\w*", "The Quick Brown fox"))  # ['The','Quick','Brown']
```

</details>

## Exercise 8

Use a non-greedy match to pull 'a' and 'b' from '(a)(b)'.

*Hint: \((.+?)\).*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.findall(r"\((.+?)\)", "(a)(b)"))  # ['a', 'b']
```

</details>

