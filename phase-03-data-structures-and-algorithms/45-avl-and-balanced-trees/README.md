# 45 — AVL and Balanced Trees

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A plain BST can degenerate into a linked list (O(n)) if you insert sorted data. **Balanced trees** keep the height ~log n automatically. An **AVL tree** is a BST where every node's **balance factor** (height of left − height of right) stays in {-1, 0, +1}; after each insert/delete it restores balance with **rotations** (LL, RR, LR, RL). Result: guaranteed O(log n) search/insert/delete.

## Why it matters

Balancing is what makes tree-based maps/sets reliably fast. AVL trees teach rotations — the mechanism behind red-black trees (used in many language libraries) and database B-trees.

## Key concepts

- **Balance factor** — height(left) − height(right); must stay in [-1, 1].
- **Rotation** — Local re-link of 2–3 nodes that rebalances while preserving BST order.
- **LL / RR** — Single rotation (right / left) for straight-line imbalance.
- **LR / RL** — Double rotation for 'zig-zag' imbalance.
- **Height tracking** — Each node caches its height to compute balance in O(1).
- **Guarantee** — Height stays O(log n), so all operations are O(log n).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

def insert(root, v):
    if root is None: return N(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))

# Inserting SORTED data makes a right-leaning 'stick'
root = None
for v in [1, 2, 3, 4, 5]:
    root = insert(root, v)
print("height of skewed tree:", height(root))   # 4 -> O(n), not O(log n)!
# A balanced tree of 5 nodes would have height 2.
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Forgetting to UPDATE node heights after a rotation corrupts every later balance check.
- ⚠️ Mixing up the four cases (LL/RR/LR/RL) rotates the wrong way and breaks BST order.
- ⚠️ Rotations must preserve the BST property — re-link children in the exact documented order.
- ⚠️ Balance factor uses HEIGHTS, not node counts; an off-by-one in height breaks balancing.
- ⚠️ Deletion rebalancing is trickier than insertion — you may need rotations up the whole path.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

