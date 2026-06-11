# 55 — Graph Algorithms

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Beyond BFS/DFS, **graph algorithms** solve weighted and structural problems: **Dijkstra's** shortest path (non-negative weights), **topological sort** (ordering a DAG by dependencies), **Union-Find** for connectivity, and **minimum spanning trees** (Kruskal/Prim). They combine traversals with heaps, sorting, and clever bookkeeping.

## Why it matters

These are the workhorses of routing (maps, networks), scheduling (build systems, course prerequisites), clustering, and network design. They appear constantly in real systems and harder interviews.

## Key concepts

- **Dijkstra** — Shortest paths from a source with a min-heap; non-negative weights only.
- **Topological sort** — Linear order of a DAG so every edge points forward.
- **Union-Find** — Near-O(1) union/find for connectivity and cycle detection.
- **MST** — Cheapest set of edges connecting all nodes (Kruskal/Prim).
- **Relaxation** — Update a node's best-known distance via a neighbor.
- **DAG** — Directed acyclic graph — required for topological sort.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import heapq

def dijkstra(graph, start):
    # graph: node -> list of (neighbor, weight)
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]                  # (distance, node)
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue                   # stale entry, skip
        for nbr, weight in graph[node]:
            nd = d + weight
            if nd < dist[nbr]:         # relaxation
                dist[nbr] = nd
                heapq.heappush(pq, (nd, nbr))
    return dist

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}
print(dijkstra(graph, "A"))   # {'A':0,'B':1,'C':3,'D':4}
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Dijkstra requires NON-NEGATIVE weights — use Bellman-Ford if edges can be negative.
- ⚠️ Skip stale heap entries (`if d > dist[node]: continue`) or you'll process nodes twice.
- ⚠️ Topological sort only works on a DAG; a cycle means no valid ordering (detect it!).
- ⚠️ Union-Find without path compression / union by rank degrades toward O(n) per op.
- ⚠️ For an unweighted shortest path, plain BFS is enough — Dijkstra is overkill.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

