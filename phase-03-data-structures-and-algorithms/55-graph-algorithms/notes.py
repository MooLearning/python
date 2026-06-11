# ======================================================================
# 55 — Graph Algorithms  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Dijkstra's shortest path with a heap
# ----------------------------------------------------------------------
print("\n--- Example 1: Dijkstra's shortest path with a heap ---")
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

# ----------------------------------------------------------------------
# Example 2: Topological sort of a DAG (Kahn's algorithm)
# ----------------------------------------------------------------------
print("\n--- Example 2: Topological sort of a DAG (Kahn's algorithm) ---")
from collections import deque

def topological_sort(graph):
    indegree = {n: 0 for n in graph}
    for n in graph:
        for nbr in graph[n]:
            indegree[nbr] += 1
    # start with all zero-indegree nodes
    q = deque([n for n in graph if indegree[n] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nbr in graph[node]:
            indegree[nbr] -= 1         # 'remove' the edge
            if indegree[nbr] == 0:
                q.append(nbr)
    return order if len(order) == len(graph) else None   # None = cycle

# course prerequisites: must do 0 before 1 and 2, etc.
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(topological_sort(graph))   # [0, 1, 2, 3]

# ----------------------------------------------------------------------
# Example 3: Union-Find (Disjoint Set Union)
# ----------------------------------------------------------------------
print("\n--- Example 3: Union-Find (Disjoint Set Union) ---")
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # each node is its own root
        self.rank = [0] * n

    def find(self, x):                 # with path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):             # union by rank
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False               # already connected (cycle if adding edge)
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

uf = UnionFind(5)
uf.union(0, 1); uf.union(1, 2); uf.union(3, 4)
print(uf.find(0) == uf.find(2))   # True  (0,1,2 connected)
print(uf.find(0) == uf.find(4))   # False (different component)

# Count connected components
roots = {uf.find(i) for i in range(5)}
print("components:", len(roots))  # 2

print("\nDone! Tip: change values above and run again to learn by experiment.")
