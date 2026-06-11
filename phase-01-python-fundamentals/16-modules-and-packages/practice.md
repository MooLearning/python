# 16 — Modules and Packages: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Import math and print the square root of 81.

*Hint: math.sqrt.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(math.sqrt(81))  # 9.0
```

</details>

## Exercise 2

Use random (seeded with 0) to pick a random item from ['x','y','z'].

*Hint: random.choice.*

<details>
<summary>✅ Solution</summary>

```python
import random
random.seed(0)
print(random.choice(["x", "y", "z"]))
```

</details>

## Exercise 3

Import only mean from statistics and average [10,20,30].

*Hint: from statistics import mean.*

<details>
<summary>✅ Solution</summary>

```python
from statistics import mean
print(mean([10, 20, 30]))  # 20
```

</details>

## Exercise 4

Import json as J and turn {'a':1} into a JSON string.

*Hint: J.dumps.*

<details>
<summary>✅ Solution</summary>

```python
import json as J
print(J.dumps({"a": 1}))  # {"a": 1}
```

</details>

## Exercise 5

Use datetime to print today's year.

*Hint: date.today().year.*

<details>
<summary>✅ Solution</summary>

```python
from datetime import date
print(date.today().year)
```

</details>

## Exercise 6

Use collections.Counter to count letters in 'banana'.

*Hint: Counter(str).*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter("banana"))  # Counter({'a': 3, 'n': 2, 'b': 1})
```

</details>

## Exercise 7

Write the __main__ guard for a file with a function main() that prints 'run'.

*Hint: if __name__...*

<details>
<summary>✅ Solution</summary>

```python
def main():
    print("run")
if __name__ == "__main__":
    main()
```

</details>

## Exercise 8

Use os to print the current working directory.

*Hint: os.getcwd().*

<details>
<summary>✅ Solution</summary>

```python
import os
print(os.getcwd())
```

</details>

