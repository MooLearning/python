# 49 — BFS and DFS

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**BFS** (breadth-first search) and **DFS** (depth-first search) are the two ways to explore a graph. BFS uses a **queue** to fan out level by level — it finds the **shortest path in an unweighted graph**. DFS uses a **stack** (or recursion) to plunge deep before backtracking — great for cycle detection, topological sort, and connectivity. Both are **O(V + E)** and need a **visited** set to avoid loops.

## Why it matters

These two traversals underlie a huge fraction of graph algorithms: shortest paths, connected components, maze solving, dependency resolution, flood fill. Master them and most graph problems become approachable.

## Key concepts

- **BFS = queue** — Explore nearest-first; shortest path in unweighted graphs.
- **DFS = stack/recursion** — Explore deepest-first; natural for backtracking.
- **visited set** — Mark nodes seen so you never revisit (prevents infinite loops).
- **O(V + E)** — Each vertex and edge is processed once.
- **Shortest path** — BFS layer count = fewest edges from the source.
- **Components** — Run a traversal from each unvisited node to count islands.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"], "E": ["B", "F"], "F": ["C", "E"],
}

def bfs(start):
    visited, order = {start}, []
    q = deque([start])
    while q:
        node = q.popleft()           # FIFO -> nearest first
        order.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)
    return order

def dfs(start, visited=None, order=None):
    if visited is None: visited, order = set(), []
    visited.add(start); order.append(start)
    for nbr in graph[start]:
        if nbr not in visited:
            dfs(nbr, visited, order)
    return order

print("BFS:", bfs("A"))   # A B C D E F
print("DFS:", dfs("A"))   # A B D E F C
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Without a `visited` set, cycles make traversal loop forever.
- ⚠️ BFS gives the shortest path ONLY in unweighted graphs — use Dijkstra when edges have weights.
- ⚠️ Mark a node visited when you ENQUEUE it (BFS), not when you dequeue, or you add duplicates.
- ⚠️ Recursive DFS can hit the recursion limit on deep/large graphs — switch to an explicit stack.
- ⚠️ BFS uses a queue (popleft); using pop() turns it into DFS and breaks shortest-path guarantees.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

