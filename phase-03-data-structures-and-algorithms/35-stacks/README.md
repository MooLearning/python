# 35 — Stacks

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **stack** is a **LIFO** (Last-In, First-Out) collection: you add (`push`) and remove (`pop`) from the same end, the **top**. Think of a stack of plates — you take the last one you put down. In Python a plain `list` is a perfect stack: `append` to push and `pop()` to pop, both O(1).

## Why it matters

Stacks model 'undo', function call frames, expression evaluation, balanced-bracket checks, and depth-first traversal. Recognizing 'I need the most recent unfinished thing' is a core interview pattern.

## Key concepts

- **push** — Add to the top — `stack.append(x)` (O(1)).
- **pop** — Remove and return the top — `stack.pop()` (O(1)).
- **peek/top** — Look at the top without removing — `stack[-1]`.
- **LIFO order** — Last item pushed is the first popped.
- **Underflow** — Popping an empty stack errors — check `if stack` first.
- **Uses** — Bracket matching, undo, DFS, call stack, expression parsing.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)       # O(1)
    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()    # O(1) from the end
    def peek(self):
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0
    def __len__(self):
        return len(self._items)

s = Stack()
for x in [1, 2, 3]:
    s.push(x)
print("top:", s.peek())     # 3
print("pop:", s.pop())      # 3
print("pop:", s.pop())      # 2
print("size:", len(s))      # 1
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Popping an empty stack raises IndexError — guard with `if stack:` or catch it.
- ⚠️ `list.pop(0)` is O(n)! A stack pops from the END with `pop()` (no argument).
- ⚠️ Order matters in binary ops: pop the right operand first, then the left.
- ⚠️ Don't use a stack when you need FIFO order — that's a queue.
- ⚠️ `peek` on an empty list (`stack[-1]`) also errors — check emptiness first.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

