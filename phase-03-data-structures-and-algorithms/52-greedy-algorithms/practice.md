# 52 — Greedy Algorithms: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Make change for 41 with coins [25,10,5,1], fewest coins.

*Hint: Biggest first.*

<details>
<summary>✅ Solution</summary>

```python
def change(amount, coins):
    coins = sorted(coins, reverse=True); used = []
    for c in coins:
        while amount >= c:
            amount -= c; used.append(c)
    return used
print(change(41, [25, 10, 5, 1]))  # [25, 10, 5, 1]
```

</details>

## Exercise 2

Select the max non-overlapping intervals from [(1,3),(2,4),(3,5)].

*Hint: Sort by end.*

<details>
<summary>✅ Solution</summary>

```python
def select(iv):
    iv.sort(key=lambda x: x[1]); out = []; end = float("-inf")
    for s, e in iv:
        if s >= end: out.append((s, e)); end = e
    return out
print(select([(1, 3), (2, 4), (3, 5)]))  # [(1,3),(3,5)]
```

</details>

## Exercise 3

Given [1,3,4] coins, show greedy is NOT optimal for amount 6.

*Hint: Compare counts.*

<details>
<summary>✅ Solution</summary>

Greedy takes 4 then 1+1 = **3 coins**. The optimal is 3+3 = **2 coins**. Because
this coin set isn't canonical, greedy fails and you must use **dynamic
programming** for the true minimum.

</details>

## Exercise 4

Maximize value in fractional knapsack: cap=10, items=[(60,10),(100,20)].

*Hint: Ratio sort.*

<details>
<summary>✅ Solution</summary>

```python
def knap(cap, items):
    items.sort(key=lambda it: it[0] / it[1], reverse=True)
    total = 0
    for v, w in items:
        take = min(w, cap); total += v * (take / w); cap -= take
        if cap == 0: break
    return total
print(knap(10, [(60, 10), (100, 20)]))  # 60.0
```

</details>

## Exercise 5

Assign the fewest meeting rooms for [(0,30),(5,10),(15,20)].

*Hint: Sort starts/ends.*

<details>
<summary>✅ Solution</summary>

```python
def min_rooms(meetings):
    starts = sorted(m[0] for m in meetings)
    ends = sorted(m[1] for m in meetings)
    rooms = used = 0; i = j = 0
    while i < len(starts):
        if starts[i] < ends[j]:
            used += 1; i += 1; rooms = max(rooms, used)
        else:
            used -= 1; j += 1
    return rooms
print(min_rooms([(0, 30), (5, 10), (15, 20)]))  # 2
```

</details>

## Exercise 6

Find the minimum number of jumps to reach the end of [2,3,1,1,4].

*Hint: Greedy farthest reach.*

<details>
<summary>✅ Solution</summary>

```python
def jumps(a):
    jumps = end = farthest = 0
    for i in range(len(a) - 1):
        farthest = max(farthest, i + a[i])
        if i == end:
            jumps += 1; end = farthest
    return jumps
print(jumps([2, 3, 1, 1, 4]))  # 2
```

</details>

## Exercise 7

Buy/sell stock for max profit with many transactions: [7,1,5,3,6,4].

*Hint: Sum upward steps.*

<details>
<summary>✅ Solution</summary>

```python
def max_profit(prices):
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
print(max_profit([7, 1, 5, 3, 6, 4]))  # 7
```

</details>

## Exercise 8

Arrange [3,30,34,5,9] to form the largest number string.

*Hint: Custom comparator.*

<details>
<summary>✅ Solution</summary>

```python
from functools import cmp_to_key
def largest(nums):
    s = list(map(str, nums))
    s.sort(key=cmp_to_key(lambda a, b: (a + b < b + a) - (a + b > b + a)))
    return "".join(s)
print(largest([3, 30, 34, 5, 9]))  # 9534330
```

</details>

