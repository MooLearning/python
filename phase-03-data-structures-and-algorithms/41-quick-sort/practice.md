# 41 — Quick Sort: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Quick-sort [4,2,6,1] with the list-comprehension version.

*Hint: Pivot + partition.*

<details>
<summary>✅ Solution</summary>

```python
def qsort(a):
    if len(a) <= 1: return a
    p = a[len(a) // 2]
    return (qsort([x for x in a if x < p]) +
            [x for x in a if x == p] +
            qsort([x for x in a if x > p]))
print(qsort([4, 2, 6, 1]))  # [1, 2, 4, 6]
```

</details>

## Exercise 2

Write a partition that returns (smaller, equal, larger) for pivot 5 on [3,5,8,5,1].

*Hint: Three lists.*

<details>
<summary>✅ Solution</summary>

```python
def partition(a, p):
    return ([x for x in a if x < p],
            [x for x in a if x == p],
            [x for x in a if x > p])
print(partition([3, 5, 8, 5, 1], 5))  # ([3,1],[5,5],[8])
```

</details>

## Exercise 3

Why is quicksort O(n^2) worst case? When does it happen?

*Hint: Lopsided partitions.*

<details>
<summary>✅ Solution</summary>

When every pivot is the smallest or largest element (e.g. already-sorted data with
a first/last pivot), each partition shrinks the problem by only **one** element, so
there are n levels of O(n) work → **O(n^2)**. Random/median pivots avoid this.

</details>

## Exercise 4

Find the 2nd smallest in [8,3,5,1,9] using quickselect.

*Hint: Recurse one side.*

<details>
<summary>✅ Solution</summary>

```python
def quickselect(a, k):
    p = a[len(a) // 2]
    lows = [x for x in a if x < p]
    eq = [x for x in a if x == p]
    if k <= len(lows): return quickselect(lows, k)
    if k <= len(lows) + len(eq): return p
    return quickselect([x for x in a if x > p], k - len(lows) - len(eq))
print(quickselect([8, 3, 5, 1, 9], 2))  # 3
```

</details>

## Exercise 5

Sort [3,1,2] in DESCENDING order with quicksort.

*Hint: Flip the comparisons.*

<details>
<summary>✅ Solution</summary>

```python
def qsort_desc(a):
    if len(a) <= 1: return a
    p = a[0]
    return (qsort_desc([x for x in a[1:] if x > p]) + [p] +
            qsort_desc([x for x in a[1:] if x <= p]))
print(qsort_desc([3, 1, 2]))  # [3, 2, 1]
```

</details>

## Exercise 6

Count partition operations (comparisons) sorting [2,1,3].

*Hint: Tally in partition.*

<details>
<summary>✅ Solution</summary>

```python
def qsort_count(a, c=[0]):
    if len(a) <= 1: return a
    p = a[len(a)//2]
    less, eq, more = [], [], []
    for x in a:
        c[0] += 1
        (less if x < p else eq if x == p else more).append(x)
    return qsort_count(less) + eq + qsort_count(more)
counter = [0]; qsort_count([2, 1, 3], counter)
print(counter[0])  # 5
```

</details>

## Exercise 7

Use median-of-three to pick a better pivot from [9,1,5].

*Hint: Median of first/mid/last.*

<details>
<summary>✅ Solution</summary>

```python
def median_of_three(a):
    first, mid, last = a[0], a[len(a)//2], a[-1]
    return sorted([first, mid, last])[1]
print(median_of_three([9, 1, 5]))  # 5
```

</details>

## Exercise 8

Implement the Dutch National Flag partition of [2,0,2,1,1,0] around 1.

*Hint: Three-way pointers.*

<details>
<summary>✅ Solution</summary>

```python
def three_way(a, pivot):
    a = a[:]; lo, mid, hi = 0, 0, len(a) - 1
    while mid <= hi:
        if a[mid] < pivot:
            a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1
        elif a[mid] > pivot:
            a[mid], a[hi] = a[hi], a[mid]; hi -= 1
        else:
            mid += 1
    return a
print(three_way([2, 0, 2, 1, 1, 0], 1))  # [0,0,1,1,2,2]
```

</details>

