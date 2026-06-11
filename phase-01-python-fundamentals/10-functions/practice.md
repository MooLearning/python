# 10 — Functions: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write a function square(n) that returns n*n, and print square(6).

*Hint: return n*n.*

<details>
<summary>✅ Solution</summary>

```python
def square(n):
    return n * n
print(square(6))  # 36
```

</details>

## Exercise 2

Write greet(name, greeting='Hi') and call it both with and without the greeting.

*Hint: Default param.*

<details>
<summary>✅ Solution</summary>

```python
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"
print(greet("Ada"))
print(greet("Ada", "Welcome"))
```

</details>

## Exercise 3

Write average(*nums) that returns the mean of any count of numbers.

*Hint: sum/len, guard empty.*

<details>
<summary>✅ Solution</summary>

```python
def average(*nums):
    return sum(nums) / len(nums) if nums else 0
print(average(2, 4, 6))  # 4.0
```

</details>

## Exercise 4

Write is_even(n) returning True/False and test 10 and 7.

*Hint: n % 2 == 0.*

<details>
<summary>✅ Solution</summary>

```python
def is_even(n):
    return n % 2 == 0
print(is_even(10), is_even(7))  # True False
```

</details>

## Exercise 5

Write min_max(lst) returning both the min and max as a tuple.

*Hint: Return two values.*

<details>
<summary>✅ Solution</summary>

```python
def min_max(lst):
    return min(lst), max(lst)
print(min_max([3, 8, 1]))  # (1, 8)
```

</details>

## Exercise 6

Write a function that counts vowels in a string.

*Hint: Loop and tally.*

<details>
<summary>✅ Solution</summary>

```python
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
print(count_vowels("Education"))  # 5
```

</details>

## Exercise 7

Fix this buggy function that uses a mutable default to accumulate items.

*Hint: Use None as the default.*

<details>
<summary>✅ Solution</summary>

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b']  (not ['a','b']!)
```

</details>

## Exercise 8

Write describe(**kwargs) that prints each keyword argument as 'key: value'.

*Hint: Iterate items().*

<details>
<summary>✅ Solution</summary>

```python
def describe(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
describe(name="Ada", age=36)
```

</details>

