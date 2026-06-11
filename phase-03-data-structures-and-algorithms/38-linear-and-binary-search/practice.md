# 38 — Linear and Binary Search: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write a linear search returning the index of 7 in [4,7,1,7].

*Hint: First match.*

<details>
<summary>✅ Solution</summary>

```python
def find(a, t):
    for i, x in enumerate(a):
        if x == t: return i
    return -1
print(find([4, 7, 1, 7], 7))  # 1
```

</details>

## Exercise 2

Binary-search for 23 in [2,5,8,12,16,23,38].

*Hint: lo/mid/hi loop.*

<details>
<summary>✅ Solution</summary>

```python
def bsearch(a, t):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == t: return mid
        if a[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return -1
print(bsearch([2, 5, 8, 12, 16, 23, 38], 23))  # 5
```

</details>

## Exercise 3

Count steps binary search takes to find 1 in range(0,1000).

*Hint: Increment a counter.*

<details>
<summary>✅ Solution</summary>

```python
def steps_to_find(a, t):
    lo, hi, steps = 0, len(a) - 1, 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if a[mid] == t: return steps
        if a[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return steps
print(steps_to_find(list(range(1000)), 1))  # ~9
```

</details>

## Exercise 4

Find the first index where you could insert 6 into [1,3,5,7].

*Hint: bisect_left.*

<details>
<summary>✅ Solution</summary>

```python
import bisect
print(bisect.bisect_left([1, 3, 5, 7], 6))  # 3
```

</details>

## Exercise 5

Find the leftmost position of a duplicate value 2 in [1,2,2,2,3].

*Hint: bisect_left.*

<details>
<summary>✅ Solution</summary>

```python
import bisect
print(bisect.bisect_left([1, 2, 2, 2, 3], 2))  # 1
```

</details>

## Exercise 6

Find the square root of 36 using binary search (integer).

*Hint: Search 0..n.*

<details>
<summary>✅ Solution</summary>

```python
def isqrt(n):
    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid == n: return mid
        if mid * mid < n: lo = mid + 1
        else: hi = mid - 1
    return hi
print(isqrt(36))  # 6
```

</details>

## Exercise 7

Find the peak index in [1,3,7,4,2] (an element bigger than neighbors).

*Hint: Binary search on slope.*

<details>
<summary>✅ Solution</summary>

```python
def peak(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < a[mid + 1]: lo = mid + 1
        else: hi = mid
    return lo
print(peak([1, 3, 7, 4, 2]))  # 2
```

</details>

## Exercise 8

Search a rotated sorted array [4,5,6,7,0,1,2] for 0.

*Hint: Decide which half is sorted.*

<details>
<summary>✅ Solution</summary>

```python
def search_rotated(a, t):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == t: return mid
        if a[lo] <= a[mid]:                # left half sorted
            if a[lo] <= t < a[mid]: hi = mid - 1
            else: lo = mid + 1
        else:                              # right half sorted
            if a[mid] < t <= a[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
```

</details>

