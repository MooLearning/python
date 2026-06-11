# 43 — Trees and BST

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **tree** is a hierarchy of **nodes**: one **root** at the top, each node pointing to **children**, no cycles. A **binary tree** limits each node to ≤ 2 children (left/right). A **binary search tree (BST)** adds an ordering rule: every left descendant is smaller and every right descendant is larger than the node. That rule makes search, insert, and delete O(log n) on a balanced tree.

## Why it matters

Trees model hierarchy everywhere — file systems, the DOM, parse trees, decision trees. BSTs give ordered O(log n) operations and underpin databases/indexes (B-trees) and ordered containers.

## Key concepts

- **Root / leaf** — Root has no parent; a leaf has no children.
- **Depth / height** — Depth = distance from root; height = longest path to a leaf.
- **Binary tree** — Each node has at most a left and a right child.
- **BST property** — left subtree < node < right subtree, recursively.
- **Search O(h)** — Compare and go left/right; O(log n) if balanced, O(n) if skewed.
- **Insert/delete** — Follow the BST rule; delete has a three-case fix-up.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)        # found the spot
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node                       # duplicates ignored

    def search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

bst = BST()
for v in [5, 3, 8, 1, 4, 7, 9]:
    bst.insert(v)
print(bst.search(7))    # True
print(bst.search(6))    # False
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ An unbalanced BST (e.g. inserting sorted data) degrades to a linked list — O(n) operations.
- ⚠️ Forgetting the `node is None` base case in recursion causes AttributeError on `.left`.
- ⚠️ Deleting a node with two children needs the in-order successor/predecessor swap.
- ⚠️ Height of an empty tree is -1 (or 0 for one node) — pick a convention and be consistent.
- ⚠️ Duplicate handling is a design choice — ignore, count, or always go right; decide up front.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

