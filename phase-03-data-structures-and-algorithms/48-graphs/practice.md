# 48 — Graphs: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Build an adjacency list for edges (1,2),(1,3),(2,3).

*Hint: dict of lists.*

<details>
<summary>✅ Solution</summary>

```python
from collections import defaultdict
adj = defaultdict(list)
for u, v in [(1, 2), (1, 3), (2, 3)]:
    adj[u].append(v); adj[v].append(u)
print(dict(adj))  # {1:[2,3],2:[1,3],3:[1,2]}
```

</details>

## Exercise 2

Count the degree of node 1 in that graph.

*Hint: len(neighbors).*

<details>
<summary>✅ Solution</summary>

```python
from collections import defaultdict
adj = defaultdict(list)
for u, v in [(1, 2), (1, 3), (2, 3)]:
    adj[u].append(v); adj[v].append(u)
print(len(adj[1]))  # 2
```

</details>

## Exercise 3

Build a 3x3 adjacency matrix for edges (0,1),(1,2).

*Hint: 2D list of 0/1.*

<details>
<summary>✅ Solution</summary>

```python
n = 3
m = [[0] * n for _ in range(n)]
for u, v in [(0, 1), (1, 2)]:
    m[u][v] = 1; m[v][u] = 1
for row in m: print(row)
```

</details>

## Exercise 4

Check whether edge (0,2) exists in the matrix above.

*Hint: Index lookup.*

<details>
<summary>✅ Solution</summary>

```python
n = 3
m = [[0] * n for _ in range(n)]
for u, v in [(0, 1), (1, 2)]:
    m[u][v] = 1; m[v][u] = 1
print(bool(m[0][2]))  # False
```

</details>

## Exercise 5

Build a DIRECTED graph and list out-neighbors of A: A->B, A->C, B->C.

*Hint: One direction only.*

<details>
<summary>✅ Solution</summary>

```python
from collections import defaultdict
g = defaultdict(list)
for u, v in [("A", "B"), ("A", "C"), ("B", "C")]:
    g[u].append(v)
print(g["A"])  # ['B', 'C']
```

</details>

## Exercise 6

Find all nodes in a graph (the vertex set).

*Hint: Collect keys + neighbors.*

<details>
<summary>✅ Solution</summary>

```python
edges = [(1, 2), (2, 3), (4, 5)]
nodes = set()
for u, v in edges:
    nodes.add(u); nodes.add(v)
print(sorted(nodes))  # [1, 2, 3, 4, 5]
```

</details>

## Exercise 7

Detect whether the undirected graph {1:[2],2:[1,3],3:[2]} has a node of degree 2.

*Hint: Scan degrees.*

<details>
<summary>✅ Solution</summary>

```python
graph = {1: [2], 2: [1, 3], 3: [2]}
print(any(len(nbrs) == 2 for nbrs in graph.values()))  # True
```

</details>

## Exercise 8

Convert an edge list [(0,1),(1,2),(0,2)] to an adjacency-list string.

*Hint: Format dict.*

<details>
<summary>✅ Solution</summary>

```python
from collections import defaultdict
adj = defaultdict(list)
for u, v in [(0, 1), (1, 2), (0, 2)]:
    adj[u].append(v); adj[v].append(u)
for node in sorted(adj):
    print(node, "->", adj[node])
```

</details>

