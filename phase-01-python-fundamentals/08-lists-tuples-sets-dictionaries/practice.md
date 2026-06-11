# 08 — Lists, Tuples, Sets and Dictionaries: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create a list of 3 colors, append a 4th, and print the list and its length.

*Hint: .append, len.*

<details>
<summary>✅ Solution</summary>

```python
colors = ["red", "green", "blue"]
colors.append("yellow")
print(colors, len(colors))
```

</details>

## Exercise 2

From [5, 3, 9, 1] print the largest and smallest values.

*Hint: max() and min().*

<details>
<summary>✅ Solution</summary>

```python
nums = [5, 3, 9, 1]
print(max(nums), min(nums))  # 9 1
```

</details>

## Exercise 3

Remove duplicates from [1,2,2,3,3,3] and print the unique count.

*Hint: Convert to a set.*

<details>
<summary>✅ Solution</summary>

```python
data = [1, 2, 2, 3, 3, 3]
print(len(set(data)))  # 3
```

</details>

## Exercise 4

Make a dict mapping 'a'->1, 'b'->2, then print the value for 'b'.

*Hint: {} literal.*

<details>
<summary>✅ Solution</summary>

```python
d = {"a": 1, "b": 2}
print(d["b"])  # 2
```

</details>

## Exercise 5

Given two sets {1,2,3} and {2,3,4}, print items in BOTH and items in EITHER.

*Hint: & and |.*

<details>
<summary>✅ Solution</summary>

```python
a, b = {1, 2, 3}, {2, 3, 4}
print(a & b)  # {2, 3}
print(a | b)  # {1, 2, 3, 4}
```

</details>

## Exercise 6

Unpack the tuple (10, 20, 30) into three variables and print their sum.

*Hint: x, y, z = t.*

<details>
<summary>✅ Solution</summary>

```python
x, y, z = (10, 20, 30)
print(x + y + z)  # 60
```

</details>

## Exercise 7

Count word frequencies in 'a b a c b a' using a dict.

*Hint: Split, then use get().*

<details>
<summary>✅ Solution</summary>

```python
text = "a b a c b a"
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
print(counts)  # {'a': 3, 'b': 2, 'c': 1}
```

</details>

## Exercise 8

Safely get the value for a missing key 'z' from {'a':1} returning 0 instead of crashing.

*Hint: dict.get with default.*

<details>
<summary>✅ Solution</summary>

```python
d = {"a": 1}
print(d.get("z", 0))  # 0
```

</details>

