# 05 — Strings and Methods: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Print the first and last character of the string 'algorithm'.

*Hint: Index 0 and -1.*

<details>
<summary>✅ Solution</summary>

```python
s = "algorithm"
print(s[0], s[-1])  # a m
```

</details>

## Exercise 2

Reverse the string 'stressed' and print it.

*Hint: Slice with step -1.*

<details>
<summary>✅ Solution</summary>

```python
print("stressed"[::-1])  # desserts
```

</details>

## Exercise 3

Count how many characters are in 'antidisestablishmentarianism'.

*Hint: len().*

<details>
<summary>✅ Solution</summary>

```python
print(len("antidisestablishmentarianism"))  # 28
```

</details>

## Exercise 4

Split the CSV line 'name,age,city' into a list of fields.

*Hint: split(',').*

<details>
<summary>✅ Solution</summary>

```python
print("name,age,city".split(","))  # ['name', 'age', 'city']
```

</details>

## Exercise 5

Turn ['2026','06','09'] into the date string '2026/06/09'.

*Hint: '/'.join(...).*

<details>
<summary>✅ Solution</summary>

```python
print("/".join(["2026", "06", "09"]))  # 2026/06/09
```

</details>

## Exercise 6

Check (case-insensitively) whether 'Hello World' contains the word 'world'.

*Hint: lower() then in.*

<details>
<summary>✅ Solution</summary>

```python
text = "Hello World"
print("world" in text.lower())  # True
```

</details>

## Exercise 7

Given '  spaced out  ', remove leading/trailing spaces and make it uppercase.

*Hint: strip() then upper().*

<details>
<summary>✅ Solution</summary>

```python
print("  spaced out  ".strip().upper())  # SPACED OUT
```

</details>

## Exercise 8

Check if 'racecar' is a palindrome (same forwards and backwards).

*Hint: Compare to its reverse.*

<details>
<summary>✅ Solution</summary>

```python
w = "racecar"
print(w == w[::-1])  # True
```

</details>

