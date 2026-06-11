# 34 — Linked Lists

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **linked list** stores items in **nodes**, each holding a value and a reference to the next node. Unlike arrays, the items aren't contiguous — to reach the 5th item you follow 5 links (O(n)). The payoff: inserting/removing at a known position is O(1) (just rewire pointers). Variants: **singly** (next only), **doubly** (prev+next), **circular**.

## Why it matters

Linked lists teach pointer/reference thinking that underlies trees, graphs, and many structures. They're ideal when you insert/delete a lot and rarely random-access, and they appear constantly in interviews (reverse a list, detect a cycle, merge two lists).

## Key concepts

- **Node** — An object with `.value` and `.next` (and `.prev` for doubly).
- **Head** — Reference to the first node; `None` means empty.
- **Traversal** — Walk node.next until None — O(n).
- **Insert/delete** — O(1) once you have the node, but O(n) to FIND the spot.
- **No random access** — `list[i]` doesn't exist — you must traverse.
- **Cycle detection** — Floyd's fast/slow pointers find loops in O(1) space.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):           # add to the end -> O(n)
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):                 # for easy printing
        out, cur = [], self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

ll = LinkedList()
for x in [1, 2, 3]:
    ll.append(x)
print(ll.to_list())     # [1, 2, 3]
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Losing the `next` pointer before reattaching loses the rest of the list — save it first when reversing.
- ⚠️ Forgetting the empty-list (`head is None`) and single-node edge cases causes crashes.
- ⚠️ Deleting the head needs special handling (move head forward) vs deleting a middle node.
- ⚠️ No O(1) indexing: reaching position k is O(k); don't treat it like an array.
- ⚠️ Accidental cycles make traversal loop forever — be careful when rewiring pointers.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

