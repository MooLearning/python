# ======================================================================
# 36 — Queues  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A queue with collections.deque
# ----------------------------------------------------------------------
print("\n--- Example 1: A queue with collections.deque ---")
from collections import deque

q = deque()
q.append("a")          # enqueue at rear
q.append("b")
q.append("c")
print("front:", q[0])  # a
print("dequeue:", q.popleft())   # a  (O(1))
print("dequeue:", q.popleft())   # b
print("remaining:", list(q))     # ['c']
print("size:", len(q))           # 1

# ----------------------------------------------------------------------
# Example 2: A Queue class and why deque beats list
# ----------------------------------------------------------------------
print("\n--- Example 2: A Queue class and why deque beats list ---")
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, x):
        self._items.append(x)        # O(1)
    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft() # O(1) from the front
    def peek(self):
        return self._items[0]
    def __len__(self):
        return len(self._items)

q = Queue()
for task in ["build", "test", "deploy"]:
    q.enqueue(task)
while len(q):
    print("processing:", q.dequeue())   # build, test, deploy (in order)

# ----------------------------------------------------------------------
# Example 3: BFS level-order on a tree uses a queue
# ----------------------------------------------------------------------
print("\n--- Example 3: BFS level-order on a tree uses a queue ---")
from collections import deque

# tree as dict: node -> list of children
tree = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}

def bfs(root):
    order = []
    q = deque([root])
    while q:
        node = q.popleft()       # FIFO -> visit level by level
        order.append(node)
        for child in tree[node]:
            q.append(child)
    return order

print(bfs(1))   # [1, 2, 3, 4, 5, 6]

print("\nDone! Tip: change values above and run again to learn by experiment.")
