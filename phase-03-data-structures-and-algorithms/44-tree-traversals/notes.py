# ======================================================================
# 44 — Tree Traversals  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: All three depth-first traversals (recursive)
# ----------------------------------------------------------------------
print("\n--- Example 1: All three depth-first traversals (recursive) ---")
class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

#        1
#       / \
#      2   3
#     / \
#    4   5
root = N(1)
root.left = N(2); root.right = N(3)
root.left.left = N(4); root.left.right = N(5)

def pre(n, out):
    if n: out.append(n.value); pre(n.left, out); pre(n.right, out)

def ino(n, out):
    if n: ino(n.left, out); out.append(n.value); ino(n.right, out)

def post(n, out):
    if n: post(n.left, out); post(n.right, out); out.append(n.value)

a = []; pre(root, a);  print("pre  :", a)   # [1, 2, 4, 5, 3]
b = []; ino(root, b);  print("in   :", b)   # [4, 2, 5, 1, 3]
c = []; post(root, c); print("post :", c)   # [4, 5, 2, 3, 1]

# ----------------------------------------------------------------------
# Example 2: Level-order (BFS) with a queue
# ----------------------------------------------------------------------
print("\n--- Example 2: Level-order (BFS) with a queue ---")
from collections import deque

class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

root = N(1)
root.left = N(2); root.right = N(3)
root.left.left = N(4); root.right.right = N(5)

def level_order(root):
    if not root:
        return []
    rows, q = [], deque([root])
    while q:
        row = []
        for _ in range(len(q)):        # process one full level
            node = q.popleft()
            row.append(node.value)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        rows.append(row)
    return rows

print(level_order(root))   # [[1], [2, 3], [4, 5]]

# ----------------------------------------------------------------------
# Example 3: Iterative pre-order with an explicit stack
# ----------------------------------------------------------------------
print("\n--- Example 3: Iterative pre-order with an explicit stack ---")
class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

root = N(1)
root.left = N(2); root.right = N(3)
root.left.left = N(4); root.left.right = N(5)

def pre_order_iter(root):
    if not root:
        return []
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        out.append(node.value)
        if node.right: stack.append(node.right)   # push right FIRST
        if node.left:  stack.append(node.left)    # so left is popped first
    return out

print(pre_order_iter(root))   # [1, 2, 4, 5, 3]

print("\nDone! Tip: change values above and run again to learn by experiment.")
