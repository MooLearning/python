# 55 — Graph Algorithms: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Run Dijkstra from A on A->B(1), B->C(2), A->C(4).

*Hint: Relax with a heap.*

<details>
<summary>✅ Solution</summary>

```python
import heapq
g = {"A": [("B", 1), ("C", 4)], "B": [("C", 2)], "C": []}
def dijkstra(g, s):
    dist = {n: float("inf") for n in g}; dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, n = heapq.heappop(pq)
        for nb, w in g[n]:
            if d + w < dist[nb]:
                dist[nb] = d + w; heapq.heappush(pq, (d + w, nb))
    return dist
print(dijkstra(g, "A"))  # {'A':0,'B':1,'C':3}
```

</details>

## Exercise 2

Topologically sort {0:[1],1:[2],2:[]}.

*Hint: Zero-indegree first.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
g = {0: [1], 1: [2], 2: []}
def topo(g):
    indeg = {n: 0 for n in g}
    for n in g:
        for m in g[n]: indeg[m] += 1
    q = deque(n for n in g if indeg[n] == 0); out = []
    while q:
        n = q.popleft(); out.append(n)
        for m in g[n]:
            indeg[m] -= 1
            if indeg[m] == 0: q.append(m)
    return out
print(topo(g))  # [0, 1, 2]
```

</details>

## Exercise 3

Use Union-Find to test if 0 and 3 are connected after union(0,1),(1,3).

*Hint: find roots.*

<details>
<summary>✅ Solution</summary>

```python
parent = list(range(4))
def find(x):
    while parent[x] != x: x = parent[x]
    return x
def union(a, b): parent[find(a)] = find(b)
union(0, 1); union(1, 3)
print(find(0) == find(3))  # True
```

</details>

## Exercise 4

Detect a cycle in a directed graph {0:[1],1:[2],2:[0]}.

*Hint: Topo sort fails.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
g = {0: [1], 1: [2], 2: [0]}
def has_cycle(g):
    indeg = {n: 0 for n in g}
    for n in g:
        for m in g[n]: indeg[m] += 1
    q = deque(n for n in g if indeg[n] == 0); count = 0
    while q:
        n = q.popleft(); count += 1
        for m in g[n]:
            indeg[m] -= 1
            if indeg[m] == 0: q.append(m)
    return count != len(g)
print(has_cycle(g))  # True
```

</details>

## Exercise 5

Count connected components of 5 nodes with edges (0,1),(2,3).

*Hint: Union then count roots.*

<details>
<summary>✅ Solution</summary>

```python
parent = list(range(5))
def find(x):
    while parent[x] != x: x = parent[x]
    return x
def union(a, b): parent[find(a)] = find(b)
for a, b in [(0, 1), (2, 3)]: union(a, b)
print(len({find(i) for i in range(5)}))  # 3
```

</details>

## Exercise 6

Find the shortest distance to all nodes from 0 in an unweighted graph with BFS.

*Hint: Layer count.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
g = {0: [1, 2], 1: [3], 2: [3], 3: []}
def bfs_dist(g, s):
    dist = {s: 0}; q = deque([s])
    while q:
        n = q.popleft()
        for m in g[n]:
            if m not in dist:
                dist[m] = dist[n] + 1; q.append(m)
    return dist
print(bfs_dist(g, 0))  # {0:0,1:1,2:1,3:2}
```

</details>

## Exercise 7

Build an MST weight with Kruskal on edges (0,1,1),(1,2,2),(0,2,3).

*Hint: Sort + union.*

<details>
<summary>✅ Solution</summary>

```python
edges = [(1, 0, 1), (2, 1, 2), (3, 0, 2)]  # (weight,u,v)
parent = list(range(3))
def find(x):
    while parent[x] != x: x = parent[x]
    return x
total = 0
for w, u, v in sorted(edges):
    if find(u) != find(v):
        parent[find(u)] = find(v); total += w
print(total)  # 3
```

</details>

## Exercise 8

Return a valid course order for prereqs {0:[],1:[0],2:[0,1]}.

*Hint: Topo sort.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
g = {0: [], 1: [0], 2: [0, 1]}  # node -> prereqs
# Build forward graph
fwd = {n: [] for n in g}; indeg = {n: 0 for n in g}
for n in g:
    for pre in g[n]:
        fwd[pre].append(n); indeg[n] += 1
q = deque(n for n in g if indeg[n] == 0); order = []
while q:
    n = q.popleft(); order.append(n)
    for m in fwd[n]:
        indeg[m] -= 1
        if indeg[m] == 0: q.append(m)
print(order)  # [0, 1, 2]
```

</details>

