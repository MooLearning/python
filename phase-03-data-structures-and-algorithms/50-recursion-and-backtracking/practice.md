# 50 — Recursion and Backtracking: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute factorial(5) recursively.

*Hint: n * factorial(n-1).*

<details>
<summary>✅ Solution</summary>

```python
def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))  # 120
```

</details>

## Exercise 2

Generate all subsets of [1,2].

*Hint: Choose/skip each.*

<details>
<summary>✅ Solution</summary>

```python
def subsets(nums):
    out = []
    def bt(i, path):
        if i == len(nums):
            out.append(path[:]); return
        bt(i + 1, path)               # skip
        path.append(nums[i]); bt(i + 1, path); path.pop()  # take
    bt(0, [])
    return out
print(subsets([1, 2]))  # [[], [2], [1], [1,2]]
```

</details>

## Exercise 3

Generate all permutations of 'ab'.

*Hint: Place each remaining char.*

<details>
<summary>✅ Solution</summary>

```python
def perms(s):
    if len(s) <= 1: return [s]
    out = []
    for i, c in enumerate(s):
        for p in perms(s[:i] + s[i+1:]):
            out.append(c + p)
    return out
print(perms("ab"))  # ['ab', 'ba']
```

</details>

## Exercise 4

Sum a nested list [1,[2,[3,4]],5] recursively.

*Hint: Recurse into sublists.*

<details>
<summary>✅ Solution</summary>

```python
def deep_sum(x):
    total = 0
    for item in x:
        total += deep_sum(item) if isinstance(item, list) else item
    return total
print(deep_sum([1, [2, [3, 4]], 5]))  # 15
```

</details>

## Exercise 5

Count the ways to climb n=4 stairs taking 1 or 2 steps.

*Hint: Fib-like recursion.*

<details>
<summary>✅ Solution</summary>

```python
def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)
print(climb(4))  # 5
```

</details>

## Exercise 6

Generate all combinations of 2 from [1,2,3].

*Hint: Start index advances.*

<details>
<summary>✅ Solution</summary>

```python
def combos(nums, k):
    out = []
    def bt(start, path):
        if len(path) == k:
            out.append(path[:]); return
        for i in range(start, len(nums)):
            path.append(nums[i]); bt(i + 1, path); path.pop()
    bt(0, [])
    return out
print(combos([1, 2, 3], 2))  # [[1,2],[1,3],[2,3]]
```

</details>

## Exercise 7

Solve: can subset of [3,34,4,12] sum to 9? (subset-sum)

*Hint: Include/exclude recursion.*

<details>
<summary>✅ Solution</summary>

```python
def subset_sum(nums, target, i=0):
    if target == 0: return True
    if i >= len(nums) or target < 0: return False
    return (subset_sum(nums, target - nums[i], i + 1) or
            subset_sum(nums, target, i + 1))
print(subset_sum([3, 34, 4, 12], 9))  # False
```

</details>

## Exercise 8

Find all root-to-leaf paths summing to 8 in a small tree.

*Hint: Carry path + remaining sum.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(5); root.left = N(3); root.right = N(3)
root.left.left = N(0)        # 5+3+0 = 8
def paths(node, target, path, out):
    if node is None: return
    path.append(node.value)
    if not node.left and not node.right and sum(path) == target:
        out.append(path[:])
    paths(node.left, target, path, out)
    paths(node.right, target, path, out)
    path.pop()
out = []; paths(root, 8, [], out); print(out)  # [[5, 3, 0]]
```

</details>

