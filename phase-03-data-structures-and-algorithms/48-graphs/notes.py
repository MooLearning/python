# ======================================================================
# 48 — Graphs  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Build a graph as an adjacency list
# ----------------------------------------------------------------------
print("\n--- Example 1: Build a graph as an adjacency list ---")
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

# ----------------------------------------------------------------------
# Example 2: Adjacency list vs adjacency matrix
# ----------------------------------------------------------------------
print("\n--- Example 2: Adjacency list vs adjacency matrix ---")
# Same graph, two representations
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
n = 4

# Adjacency list
adj_list = {i: [] for i in range(n)}
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
print("list  :", adj_list)

# Adjacency matrix
matrix = [[0] * n for _ in range(n)]
for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1
print("matrix:")
for row in matrix:
    print(" ", row)

# O(1) edge lookup with a matrix
print("edge 0-3?", bool(matrix[0][3]))   # False
print("edge 2-3?", bool(matrix[2][3]))   # True

# ----------------------------------------------------------------------
# Example 3: Weighted graph and degree counting
# ----------------------------------------------------------------------
print("\n--- Example 3: Weighted graph and degree counting ---")
from collections import defaultdict

# Weighted adjacency list: node -> list of (neighbor, weight)
graph = defaultdict(list)
roads = [("A", "B", 5), ("A", "C", 2), ("B", "C", 1), ("C", "D", 7)]
for u, v, w in roads:
    graph[u].append((v, w))
    graph[v].append((u, w))

for node in ["A", "B", "C", "D"]:
    print(f"{node}: {graph[node]}")

# Degree = number of edges touching a node
print("degree of C:", len(graph["C"]))   # 3

# Total weight of all unique edges
total = sum(w for _, _, w in roads)
print("total road length:", total)       # 15

print("\nDone! Tip: change values above and run again to learn by experiment.")
