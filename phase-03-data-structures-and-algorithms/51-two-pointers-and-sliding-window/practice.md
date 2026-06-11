# 51 — Two Pointers and Sliding Window: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Check if 'racecar' is a palindrome with two pointers.

*Hint: Compare ends inward.*

<details>
<summary>✅ Solution</summary>

```python
def is_pal(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]: return False
        i += 1; j -= 1
    return True
print(is_pal("racecar"))  # True
```

</details>

## Exercise 2

Find a pair in sorted [1,3,5,7] summing to 8.

*Hint: Move pointers by sum.*

<details>
<summary>✅ Solution</summary>

```python
def pair(a, t):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == t: return (a[i], a[j])
        if s < t: i += 1
        else: j -= 1
a = [1, 3, 5, 7]
print(pair(a, 8))  # (1, 7) or (3, 5) -> (1, 7)
```

</details>

## Exercise 3

Max sum of any 2 consecutive elements in [1,4,2,10,2].

*Hint: Window of size 2.*

<details>
<summary>✅ Solution</summary>

```python
def max2(a):
    best = a[0] + a[1]
    for i in range(2, len(a)):
        best = max(best, a[i] + a[i - 1])
    return best
print(max2([1, 4, 2, 10, 2]))  # 12
```

</details>

## Exercise 4

Remove duplicates in-place from sorted [1,1,2,3,3] (return new length).

*Hint: Slow/fast pointers.*

<details>
<summary>✅ Solution</summary>

```python
def dedup(a):
    if not a: return 0
    slow = 0
    for fast in range(1, len(a)):
        if a[fast] != a[slow]:
            slow += 1; a[slow] = a[fast]
    return slow + 1
print(dedup([1, 1, 2, 3, 3]))  # 3
```

</details>

## Exercise 5

Longest substring without repeats in 'abba'.

*Hint: Variable window + last-seen map.*

<details>
<summary>✅ Solution</summary>

```python
def longest(s):
    seen = {}; left = best = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = r
        best = max(best, r - left + 1)
    return best
print(longest("abba"))  # 2
```

</details>

## Exercise 6

Count subarrays of [1,2,3] with sum exactly 3.

*Hint: Sliding window on positives.*

<details>
<summary>✅ Solution</summary>

```python
def count_sum(a, target):
    left = total = count = 0
    for right in range(len(a)):
        total += a[right]
        while total > target and left <= right:
            total -= a[left]; left += 1
        if total == target: count += 1
    return count
print(count_sum([1, 2, 3], 3))  # 2  ([1,2] and [3])
```

</details>

## Exercise 7

Move all zeros to the end of [0,1,0,3,12] in place.

*Hint: Slow pointer for non-zeros.*

<details>
<summary>✅ Solution</summary>

```python
def move_zeros(a):
    slow = 0
    for fast in range(len(a)):
        if a[fast] != 0:
            a[slow], a[fast] = a[fast], a[slow]; slow += 1
    return a
print(move_zeros([0, 1, 0, 3, 12]))  # [1,3,12,0,0]
```

</details>

## Exercise 8

Find the smallest window in [2,3,1,2,4,3] with sum >= 7.

*Hint: Shrink-from-left window.*

<details>
<summary>✅ Solution</summary>

```python
def min_window(target, a):
    left = total = 0; best = float("inf")
    for right in range(len(a)):
        total += a[right]
        while total >= target:
            best = min(best, right - left + 1)
            total -= a[left]; left += 1
    return 0 if best == float("inf") else best
print(min_window(7, [2, 3, 1, 2, 4, 3]))  # 2
```

</details>

