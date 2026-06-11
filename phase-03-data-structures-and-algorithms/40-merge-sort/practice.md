# 40 — Merge Sort: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Merge two sorted lists [1,4,6] and [2,3,5] into one.

*Hint: Two pointers.*

<details>
<summary>✅ Solution</summary>

```python
def merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 4, 6], [2, 3, 5]))  # [1,2,3,4,5,6]
```

</details>

## Exercise 2

Sort [9,3,7,1] with merge sort.

*Hint: Split, sort halves, merge.*

<details>
<summary>✅ Solution</summary>

```python
def msort(a):
    if len(a) <= 1: return a
    m = len(a) // 2
    L, R = msort(a[:m]), msort(a[m:])
    out, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: out.append(L[i]); i += 1
        else: out.append(R[j]); j += 1
    return out + L[i:] + R[j:]
print(msort([9, 3, 7, 1]))  # [1, 3, 7, 9]
```

</details>

## Exercise 3

How many levels of recursion for a list of 8 items?

*Hint: log2(n).*

<details>
<summary>✅ Solution</summary>

**3 levels** of splitting (8 → 4 → 2 → 1), i.e. log2(8) = 3, plus the merges back
up. In general merge sort has about **log2(n)** levels.

</details>

## Exercise 4

Merge while removing duplicates: [1,2,2] and [2,3].

*Hint: Skip equal to last.*

<details>
<summary>✅ Solution</summary>

```python
def merge_unique(a, b):
    out, i, j = [], 0, 0
    while i < len(a) or j < len(b):
        if j >= len(b) or (i < len(a) and a[i] <= b[j]):
            x = a[i]; i += 1
        else:
            x = b[j]; j += 1
        if not out or out[-1] != x: out.append(x)
    return out
print(merge_unique([1, 2, 2], [2, 3]))  # [1, 2, 3]
```

</details>

## Exercise 5

Count inversions in [2,3,1].

*Hint: Pairs out of order.*

<details>
<summary>✅ Solution</summary>

```python
def inversions(a):
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]: count += 1
    return count
print(inversions([2, 3, 1]))  # 2
```

</details>

## Exercise 6

Use heapq.merge to merge [1,5] and [2,3].

*Hint: It returns an iterator.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
print(list(heapq.merge([1, 5], [2, 3])))  # [1, 2, 3, 5]
```

</details>

## Exercise 7

Write an iterative (bottom-up) merge sort on [4,3,2,1].

*Hint: Merge widths 1,2,4...*

<details>
<summary>✅ Solution</summary>

```python
def merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
def bottom_up(arr):
    width = 1; a = arr[:]
    while width < len(a):
        for i in range(0, len(a), 2 * width):
            a[i:i+2*width] = merge(a[i:i+width], a[i+width:i+2*width])
        width *= 2
    return a
print(bottom_up([4, 3, 2, 1]))  # [1, 2, 3, 4]
```

</details>

## Exercise 8

Merge sort a list of words by length, keeping stability.

*Hint: Compare len(), use <=.*

<details>
<summary>✅ Solution</summary>

```python
def msort_len(a):
    if len(a) <= 1: return a
    m = len(a) // 2
    L, R = msort_len(a[:m]), msort_len(a[m:])
    out, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if len(L[i]) <= len(R[j]): out.append(L[i]); i += 1
        else: out.append(R[j]); j += 1
    return out + L[i:] + R[j:]
print(msort_len(["bb", "a", "ccc", "dd"]))  # ['a','bb','dd','ccc']
```

</details>

