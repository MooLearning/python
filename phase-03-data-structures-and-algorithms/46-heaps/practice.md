# 46 — Heaps: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Push 4,1,7,3 into a min-heap and pop the smallest.

*Hint: heappush/heappop.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
h = []
for x in [4, 1, 7, 3]: heapq.heappush(h, x)
print(heapq.heappop(h))  # 1
```

</details>

## Exercise 2

Find the 3 smallest of [8,2,5,1,9,3].

*Hint: heapq.nsmallest.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
print(heapq.nsmallest(3, [8, 2, 5, 1, 9, 3]))  # [1, 2, 3]
```

</details>

## Exercise 3

Turn [5,2,8,1] into a max-heap and read the max.

*Hint: Negate values.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
nums = [5, 2, 8, 1]
h = [-x for x in nums]; heapq.heapify(h)
print(-h[0])  # 8
```

</details>

## Exercise 4

Build a priority queue: pop tasks (3,'c'),(1,'a'),(2,'b') in order.

*Hint: Tuples sort by first.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
pq = []
for item in [(3, "c"), (1, "a"), (2, "b")]:
    heapq.heappush(pq, item)
print([heapq.heappop(pq)[1] for _ in range(3)])  # ['a','b','c']
```

</details>

## Exercise 5

Merge sorted lists [1,4] and [2,3] with a heap.

*Hint: heapq.merge.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
print(list(heapq.merge([1, 4], [2, 3])))  # [1, 2, 3, 4]
```

</details>

## Exercise 6

Find the k=2 largest in a stream using a size-k heap.

*Hint: Keep only k items.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
def two_largest(stream):
    h = []
    for x in stream:
        heapq.heappush(h, x)
        if len(h) > 2: heapq.heappop(h)
    return sorted(h, reverse=True)
print(two_largest([4, 1, 7, 3, 8, 5]))  # [8, 7]
```

</details>

## Exercise 7

Compute the array index of the parent of node at index 5.

*Hint: (i-1)//2.*

<details>
<summary>✅ Solution</summary>

```python
i = 5
print((i - 1) // 2)  # 2
```

</details>

## Exercise 8

Use a heap to sort [3,1,4,1,5] ascending (heap sort).

*Hint: heapify + pop all.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
def heap_sort(a):
    h = a[:]; heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
print(heap_sort([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
```

</details>

