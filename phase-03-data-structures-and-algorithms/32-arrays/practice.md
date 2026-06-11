# 32 — Arrays and Dynamic Arrays: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Reverse a list in place without using reverse() or [::-1].

*Hint: Two-pointer swap.*

<details>
<summary>✅ Solution</summary>

```python
def reverse(a):
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1; j -= 1
    return a
print(reverse([1, 2, 3, 4]))  # [4, 3, 2, 1]
```

</details>

## Exercise 2

Find the second-largest number in [3, 9, 1, 9, 7].

*Hint: Track top two, handle dupes.*

<details>
<summary>✅ Solution</summary>

```python
def second_largest(a):
    first = second = float("-inf")
    for x in a:
        if x > first:
            first, second = x, first
        elif first > x > second:
            second = x
    return second
print(second_largest([3, 9, 1, 9, 7]))  # 7
```

</details>

## Exercise 3

Rotate [1,2,3,4,5] right by 2 -> [4,5,1,2,3].

*Hint: Slice and concatenate.*

<details>
<summary>✅ Solution</summary>

```python
def rotate(a, k):
    k %= len(a)
    return a[-k:] + a[:-k]
print(rotate([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

</details>

## Exercise 4

Build a 3x3 identity matrix as a list of lists.

*Hint: 1 on the diagonal.*

<details>
<summary>✅ Solution</summary>

```python
n = 3
I = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
for row in I: print(row)
```

</details>

## Exercise 5

Move all zeros in [0,1,0,3,12] to the end, keeping order -> [1,3,12,0,0].

*Hint: Stable partition.*

<details>
<summary>✅ Solution</summary>

```python
def move_zeros(a):
    nonzero = [x for x in a if x != 0]
    return nonzero + [0] * (len(a) - len(nonzero))
print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
```

</details>

## Exercise 6

Use a prefix-sum array to answer the sum of indices 1..3 of [2,4,6,8,10].

*Hint: prefix[hi+1]-prefix[lo].*

<details>
<summary>✅ Solution</summary>

```python
nums = [2, 4, 6, 8, 10]
pre = [0]
for x in nums: pre.append(pre[-1] + x)
print(pre[4] - pre[1])  # 4+6+8 = 18
```

</details>

## Exercise 7

Find the maximum sum of any contiguous subarray (Kadane's) of [-2,1,-3,4,-1,2,1,-5,4].

*Hint: Track running and best sums.*

<details>
<summary>✅ Solution</summary>

```python
def max_subarray(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
```

</details>

## Exercise 8

Merge two sorted arrays [1,3,5] and [2,4,6] into one sorted array.

*Hint: Two pointers.*

<details>
<summary>✅ Solution</summary>

```python
def merge(a, b):
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 3, 5], [2, 4, 6]))  # [1,2,3,4,5,6]
```

</details>

