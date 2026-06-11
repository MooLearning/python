# 48 — Graphs

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **graph** is a set of **vertices** (nodes) connected by **edges**. Edges can be **directed** (one-way) or **undirected**, and **weighted** (carry a cost) or not. Common representations: an **adjacency list** (dict: node → neighbors, space-efficient for sparse graphs) or an **adjacency matrix** (2D grid, O(1) edge lookup, O(V²) space).

## Why it matters

Graphs model networks of every kind: social connections, maps/roads, the web, dependencies, state machines. Most 'find a path / reach / connect / order' problems are graph problems in disguise.

## Key concepts

- **Vertex / edge** — Nodes and the connections between them.
- **Directed vs undirected** — One-way edges vs symmetric connections.
- **Weighted** — Edges carry a cost/distance.
- **Adjacency list** — dict {node: [neighbors]} — great for sparse graphs.
- **Adjacency matrix** — matrix[i][j] = edge — O(1) lookup, O(V²) space.
- **Degree** — Number of edges at a vertex (in/out for directed).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)     # undirected -> both ways

    def neighbors(self, u):
        return self.adj[u]

    def __str__(self):
        return "\n".join(f"{n}: {nbrs}" for n, nbrs in self.adj.items())

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
print(g)
print("neighbors of A:", g.neighbors("A"))   # ['B', 'C']
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Undirected edges must be added in BOTH directions — forgetting one breaks traversal.
- ⚠️ Adjacency matrix uses O(V²) memory; wasteful for sparse graphs (use a list instead).
- ⚠️ `defaultdict(list)` avoids KeyError, but reading a missing node CREATES an empty entry.
- ⚠️ Self-loops and parallel/duplicate edges may need explicit handling depending on the problem.
- ⚠️ Directed graphs: in-degree ≠ out-degree; don't assume edges are symmetric.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

