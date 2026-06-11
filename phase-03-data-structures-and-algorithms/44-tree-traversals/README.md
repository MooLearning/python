# 44 — Tree Traversals

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **traversal** visits every node of a tree in some order. The **depth-first** orders differ by when you visit the node relative to its children: **pre-order** (node, left, right), **in-order** (left, node, right — sorted for a BST), **post-order** (left, right, node). **Level-order** (breadth-first) visits the tree row by row using a queue.

## Why it matters

Different tasks need different orders: in-order to read a BST sorted, pre-order to copy/serialize, post-order to delete/evaluate (children before parent), level-order for shortest paths and 'by depth' processing.

## Key concepts

- **Pre-order** — Node → Left → Right. Good for copying/serializing a tree.
- **In-order** — Left → Node → Right. Sorted output for a BST.
- **Post-order** — Left → Right → Node. Good for deletion/expression evaluation.
- **Level-order** — Row by row using a queue (BFS).
- **Recursive DFS** — Simple, but uses the call stack (O(h)).
- **Iterative DFS** — Use an explicit stack to avoid recursion limits.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ In-order gives sorted output ONLY for a binary SEARCH tree, not any binary tree.
- ⚠️ In iterative pre-order, push the RIGHT child before the left so left is visited first.
- ⚠️ Deep recursive traversal can exceed Python's recursion limit on tall trees — go iterative.
- ⚠️ Level-order needs a queue (FIFO); using a stack turns it into DFS.
- ⚠️ Don't forget the `if node:` guard — recursing into None throws AttributeError.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

