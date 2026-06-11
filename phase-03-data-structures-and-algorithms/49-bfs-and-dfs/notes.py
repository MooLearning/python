# ======================================================================
# 49 — BFS and DFS  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: BFS and DFS on the same graph
# ----------------------------------------------------------------------
print("\n--- Example 1: BFS and DFS on the same graph ---")
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

# ----------------------------------------------------------------------
# Example 2: BFS finds the shortest (fewest-edge) path
# ----------------------------------------------------------------------
print("\n--- Example 2: BFS finds the shortest (fewest-edge) path ---")
from collections import deque

graph = {
    1: [2, 3], 2: [1, 4], 3: [1, 4, 5],
    4: [2, 3, 6], 5: [3, 6], 6: [4, 5],
}

def shortest_path(start, goal):
    q = deque([[start]])             # queue of PATHS
    visited = {start}
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal:
            return path              # first time we reach goal = shortest
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(path + [nbr])
    return None

print(shortest_path(1, 6))   # [1, 3, 5, 6] or [1, 2, 4, 6] (length 4)

# ----------------------------------------------------------------------
# Example 3: Iterative DFS and counting connected components
# ----------------------------------------------------------------------
print("\n--- Example 3: Iterative DFS and counting connected components ---")
def dfs_iter(graph, start):
    visited, order = set(), []
    stack = [start]
    while stack:
        node = stack.pop()           # LIFO -> go deep
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nbr in reversed(graph[node]):   # reversed = natural order
            if nbr not in visited:
                stack.append(nbr)
    return order

graph = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3], 5: []}
print("DFS from 0:", dfs_iter(graph, 0))   # [0, 1, 2]

def count_components(graph):
    seen, count = set(), 0
    for node in graph:
        if node not in seen:
            count += 1
            for v in dfs_iter(graph, node):  # mark the whole component
                seen.add(v)
    return count

print("components:", count_components(graph))   # 3  ({0,1,2},{3,4},{5})

print("\nDone! Tip: change values above and run again to learn by experiment.")
