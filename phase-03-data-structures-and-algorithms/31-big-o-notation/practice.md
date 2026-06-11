# 31 — Big-O Notation: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

State the Big-O of looking up a key in a dict of n items.

*Hint: Hash tables are constant time.*

<details>
<summary>✅ Solution</summary>

**O(1)** on average. Python dicts use hashing, so lookups don't depend on size.

</details>

## Exercise 2

What is the Big-O of this loop: for i in range(n): for j in range(n): ...?

*Hint: Nested over n.*

<details>
<summary>✅ Solution</summary>

**O(n^2)** — the inner loop runs n times for each of the n outer iterations.

</details>

## Exercise 3

Simplify O(5n + 3) and O(n^2 + 100n + 7) to Big-O.

*Hint: Drop constants and lower terms.*

<details>
<summary>✅ Solution</summary>

`O(5n + 3)` → **O(n)**.  `O(n^2 + 100n + 7)` → **O(n^2)** (the n^2 term dominates).

</details>

## Exercise 4

Write an O(n) function that returns the max of a list (no built-in max).

*Hint: One pass.*

<details>
<summary>✅ Solution</summary>

```python
def my_max(arr):
    best = arr[0]
    for x in arr:
        if x > best:
            best = x
    return best
print(my_max([3, 9, 1, 7]))  # 9
```

</details>

## Exercise 5

Is binary search O(log n) or O(n)? Why?

*Hint: It halves the search space.*

<details>
<summary>✅ Solution</summary>

**O(log n)** — each comparison discards half of the remaining elements, so it
takes about log2(n) steps.

</details>

## Exercise 6

Rewrite an O(n^2) 'contains duplicate' check as O(n).

*Hint: Use a set.*

<details>
<summary>✅ Solution</summary>

```python
def has_dup(arr):
    return len(set(arr)) != len(arr)
print(has_dup([1, 2, 2]))  # True
```

</details>

## Exercise 7

What is the time complexity of appending to a Python list (amortized)?

*Hint: Dynamic array.*

<details>
<summary>✅ Solution</summary>

**O(1) amortized.** Most appends are constant; occasional resizes are rare enough
to average out to O(1).

</details>

## Exercise 8

Order these from fastest- to slowest-growing: O(n^2), O(1), O(n log n), O(log n), O(n).

<details>
<summary>✅ Solution</summary>

**O(1) < O(log n) < O(n) < O(n log n) < O(n^2)** (slowest-growing first).

</details>

