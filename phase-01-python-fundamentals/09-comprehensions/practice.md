# 09 — Comprehensions: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Build a list of the cubes of 1..5 with a comprehension.

*Hint: [x**3 for x in ...].*

<details>
<summary>✅ Solution</summary>

```python
print([x ** 3 for x in range(1, 6)])  # [1, 8, 27, 64, 125]
```

</details>

## Exercise 2

From [-2,-1,0,1,2] keep only the positive numbers.

*Hint: Add an if filter.*

<details>
<summary>✅ Solution</summary>

```python
nums = [-2, -1, 0, 1, 2]
print([x for x in nums if x > 0])  # [1, 2]
```

</details>

## Exercise 3

Uppercase every word in ['cat','dog'] using a comprehension.

*Hint: w.upper().*

<details>
<summary>✅ Solution</summary>

```python
print([w.upper() for w in ["cat", "dog"]])  # ['CAT', 'DOG']
```

</details>

## Exercise 4

Make a dict mapping each of 1..4 to True if even else False.

*Hint: Dict comprehension.*

<details>
<summary>✅ Solution</summary>

```python
print({n: n % 2 == 0 for n in range(1, 5)})
# {1: False, 2: True, 3: False, 4: True}
```

</details>

## Exercise 5

From a sentence, build a list of word lengths.

*Hint: split then len.*

<details>
<summary>✅ Solution</summary>

```python
s = "the quick brown fox"
print([len(w) for w in s.split()])  # [3, 5, 5, 3]
```

</details>

## Exercise 6

Replace negatives with 0 in [3,-1,4,-5] using a conditional expression.

*Hint: if/else before for.*

<details>
<summary>✅ Solution</summary>

```python
print([x if x > 0 else 0 for x in [3, -1, 4, -5]])  # [3, 0, 4, 0]
```

</details>

## Exercise 7

Get the set of unique vowels in 'mississippi alabama'.

*Hint: Set comprehension over chars.*

<details>
<summary>✅ Solution</summary>

```python
s = "mississippi alabama"
print({c for c in s if c in "aeiou"})  # {'i', 'a'}
```

</details>

## Exercise 8

Flatten [[1,2],[3,4],[5]] into [1,2,3,4,5] with a nested comprehension.

*Hint: Two for clauses.*

<details>
<summary>✅ Solution</summary>

```python
nested = [[1, 2], [3, 4], [5]]
print([x for row in nested for x in row])  # [1, 2, 3, 4, 5]
```

</details>

