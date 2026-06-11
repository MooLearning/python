# 42 — Heap, Counting and Radix Sort: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Sort [3,1,2] using heapq (heapify + heappop).

*Hint: Min-heap pops smallest.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
h = [3, 1, 2]; heapq.heapify(h)
print([heapq.heappop(h) for _ in range(3)])  # [1, 2, 3]
```

</details>

## Exercise 2

Counting-sort the digits [1,4,1,2,7,5,2].

*Hint: Tally then rebuild.*

<details>
<summary>✅ Solution</summary>

```python
def counting_sort(a):
    counts = [0] * (max(a) + 1)
    for x in a: counts[x] += 1
    out = []
    for v, c in enumerate(counts): out += [v] * c
    return out
print(counting_sort([1, 4, 1, 2, 7, 5, 2]))  # [1,1,2,2,4,5,7]
```

</details>

## Exercise 3

Find the 3 largest numbers in [5,1,8,2,9,3] with a heap.

*Hint: heapq.nlargest.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
print(heapq.nlargest(3, [5, 1, 8, 2, 9, 3]))  # [9, 8, 5]
```

</details>

## Exercise 4

Why can radix sort beat O(n log n)? State its complexity.

*Hint: Digit passes.*

<details>
<summary>✅ Solution</summary>

Radix sort does **d** passes (one per digit), each a stable counting sort over n
items with base b → **O(d·(n + b))**. When d and b are small constants, that's
effectively **O(n)** — it never compares two keys, so it dodges the comparison
lower bound of O(n log n).

</details>

## Exercise 5

Use counting sort to sort the string 'dbca' alphabetically.

*Hint: Count chars.*

<details>
<summary>✅ Solution</summary>

```python
def sort_str(s):
    counts = [0] * 26
    for c in s: counts[ord(c) - 97] += 1
    return "".join(chr(i + 97) * n for i, n in enumerate(counts))
print(sort_str("dbca"))  # abcd
```

</details>

## Exercise 6

Build a max-heap behavior with heapq by negating values [3,1,2].

*Hint: Push negatives.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
nums = [3, 1, 2]
h = [-x for x in nums]; heapq.heapify(h)
print(-heapq.heappop(h))  # 3 (largest)
```

</details>

## Exercise 7

Radix-sort [170,45,75,90,802,24].

*Hint: LSD digit passes.*

<details>
<summary>✅ Solution</summary>

```python
def radix(a):
    a = a[:]; exp = 1; mx = max(a)
    while mx // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a: buckets[(x // exp) % 10].append(x)
        a = [x for b in buckets for x in b]
        exp *= 10
    return a
print(radix([170, 45, 75, 90, 802, 24]))  # [24,45,75,90,170,802]
```

</details>

## Exercise 8

Use counting sort to find the most frequent value in [2,3,3,3,1,2].

*Hint: Max count.*

<details>
<summary>✅ Solution</summary>

```python
def most_frequent(a):
    counts = [0] * (max(a) + 1)
    for x in a: counts[x] += 1
    return counts.index(max(counts))
print(most_frequent([2, 3, 3, 3, 1, 2]))  # 3
```

</details>

