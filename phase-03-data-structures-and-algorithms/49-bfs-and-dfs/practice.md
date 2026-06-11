# 49 — BFS and DFS: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

BFS-traverse {A:[B,C],B:[D],C:[],D:[]} from A.

*Hint: Queue + visited.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
def bfs(s):
    seen, out, q = {s}, [], deque([s])
    while q:
        n = q.popleft(); out.append(n)
        for x in g[n]:
            if x not in seen: seen.add(x); q.append(x)
    return out
print(bfs("A"))  # ['A','B','C','D']
```

</details>

## Exercise 2

DFS-traverse the same graph recursively.

*Hint: Recurse neighbors.*

<details>
<summary>✅ Solution</summary>

```python
g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
def dfs(n, seen=None, out=None):
    if seen is None: seen, out = set(), []
    seen.add(n); out.append(n)
    for x in g[n]:
        if x not in seen: dfs(x, seen, out)
    return out
print(dfs("A"))  # ['A','B','D','C']
```

</details>

## Exercise 3

Check if node D is reachable from A.

*Hint: Traverse and test membership.*

<details>
<summary>✅ Solution</summary>

```python
g = {"A": ["B"], "B": ["C"], "C": ["D"], "D": []}
def reachable(s, t):
    seen, stack = set(), [s]
    while stack:
        n = stack.pop()
        if n == t: return True
        seen.add(n)
        stack += [x for x in g[n] if x not in seen]
    return False
print(reachable("A", "D"))  # True
```

</details>

## Exercise 4

Find the shortest path length from 1 to 4 in {1:[2,3],2:[4],3:[4],4:[]}.

*Hint: BFS depth.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
g = {1: [2, 3], 2: [4], 3: [4], 4: []}
def dist(s, t):
    q = deque([(s, 0)]); seen = {s}
    while q:
        n, d = q.popleft()
        if n == t: return d
        for x in g[n]:
            if x not in seen: seen.add(x); q.append((x, d + 1))
    return -1
print(dist(1, 4))  # 2
```

</details>

## Exercise 5

Count connected components in {0:[1],1:[0],2:[],3:[4],4:[3]}.

*Hint: Traverse from each.*

<details>
<summary>✅ Solution</summary>

```python
g = {0: [1], 1: [0], 2: [], 3: [4], 4: [3]}
def components(g):
    seen, count = set(), 0
    for start in g:
        if start in seen: continue
        count += 1; stack = [start]
        while stack:
            n = stack.pop(); seen.add(n)
            stack += [x for x in g[n] if x not in seen]
    return count
print(components(g))  # 3
```

</details>

## Exercise 6

Detect a cycle in an undirected graph {0:[1],1:[0,2],2:[1,0]}.

*Hint: Track parent.*

<details>
<summary>✅ Solution</summary>

```python
g = {0: [1, 2], 1: [0, 2], 2: [1, 0]}
def has_cycle(g):
    seen = set()
    def dfs(n, parent):
        seen.add(n)
        for x in g[n]:
            if x not in seen:
                if dfs(x, n): return True
            elif x != parent:
                return True
        return False
    return any(dfs(n, -1) for n in g if n not in seen)
print(has_cycle(g))  # True
```

</details>

## Exercise 7

Flood-fill a grid: count cells reachable from (0,0) that equal 1.

*Hint: DFS on a matrix.*

<details>
<summary>✅ Solution</summary>

```python
grid = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
def flood(r, c):
    if not (0 <= r < 3 and 0 <= c < 3) or grid[r][c] != 1:
        return 0
    grid[r][c] = 2                # mark visited
    return 1 + flood(r+1, c) + flood(r-1, c) + flood(r, c+1) + flood(r, c-1)
print(flood(0, 0))  # 3
```

</details>

## Exercise 8

Return BFS levels (list of lists) of {A:[B,C],B:[D],C:[D],D:[]} from A.

*Hint: Process per level.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
def levels(s):
    seen, out, q = {s}, [], deque([s])
    while q:
        row = []
        for _ in range(len(q)):
            n = q.popleft(); row.append(n)
            for x in g[n]:
                if x not in seen: seen.add(x); q.append(x)
        out.append(row)
    return out
print(levels("A"))  # [['A'], ['B','C'], ['D']]
```

</details>

