# 54 — Dynamic Programming: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute fib(10) with memoization.

*Hint: Cache recursive calls.*

<details>
<summary>✅ Solution</summary>

```python
from functools import lru_cache
@lru_cache(None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(10))  # 55
```

</details>

## Exercise 2

Count ways to climb 5 stairs taking 1 or 2 steps (DP).

*Hint: dp[i]=dp[i-1]+dp[i-2].*

<details>
<summary>✅ Solution</summary>

```python
def climb(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(climb(5))  # 8
```

</details>

## Exercise 3

Fewest coins to make 6 from [1,3,4].

*Hint: Bottom-up min.*

<details>
<summary>✅ Solution</summary>

```python
def coin(coins, amt):
    dp = [0] + [float("inf")] * amt
    for x in range(1, amt + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amt]
print(coin([1, 3, 4], 6))  # 2
```

</details>

## Exercise 4

Longest common subsequence of 'abcde' and 'ace'.

*Hint: 2D table.*

<details>
<summary>✅ Solution</summary>

```python
def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = (dp[i-1][j-1] + 1 if a[i-1] == b[j-1]
                        else max(dp[i-1][j], dp[i][j-1]))
    return dp[-1][-1]
print(lcs("abcde", "ace"))  # 3
```

</details>

## Exercise 5

Max sum of non-adjacent elements in [2,7,9,3,1] (house robber).

*Hint: Take or skip.*

<details>
<summary>✅ Solution</summary>

```python
def rob(a):
    prev = cur = 0
    for x in a:
        prev, cur = cur, max(cur, prev + x)
    return cur
print(rob([2, 7, 9, 3, 1]))  # 12
```

</details>

## Exercise 6

Count unique paths in a 3x3 grid (only right/down moves).

*Hint: dp[i][j]=up+left.*

<details>
<summary>✅ Solution</summary>

```python
def paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
print(paths(3, 3))  # 6
```

</details>

## Exercise 7

Edit distance between 'cat' and 'cut'.

*Hint: Insert/delete/replace table.*

<details>
<summary>✅ Solution</summary>

```python
def edit(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1]
            else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
print(edit("cat", "cut"))  # 1
```

</details>

## Exercise 8

Length of the longest increasing subsequence of [10,9,2,5,3,7,101,18].

*Hint: O(n^2) DP.*

<details>
<summary>✅ Solution</summary>

```python
def lis(a):
    if not a: return 0
    dp = [1] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
```

</details>

