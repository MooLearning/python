# 08 — Lists, Tuples, Sets and Dictionaries

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Python's four core **collections**: a **list** `[]` is an ordered, changeable sequence; a **tuple** `()` is an ordered but **immutable** sequence; a **set** `{}` is an unordered collection of **unique** items; a **dictionary** `{key: value}` maps keys to values for instant lookup. Choosing the right one is half of writing clean Python.

## Why it matters

These four structures store and organize almost all data you'll handle. Lists for sequences, tuples for fixed records, sets for uniqueness/membership, dicts for labelled data and fast lookups — they're the workhorses of every program and the basis for DSA later.

## Key concepts

- **list** — Ordered, mutable: `nums = [1,2,3]`. Use .append, .pop, indexing, slicing.
- **tuple** — Ordered, immutable: `point = (3, 4)`. Great for fixed groups / dict keys.
- **set** — Unordered, unique: `{1,2,2}` becomes `{1,2}`. Fast `in` checks; supports union/intersection.
- **dict** — Key→value map: `ages = {'Ada': 36}`. O(1) lookup by key; keys must be unique.
- **Mutability** — Lists/sets/dicts can change in place; tuples and strings cannot.
- **Membership** — `x in collection` checks presence; very fast for sets and dicts.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
nums = [3, 1, 2]
nums.append(4)         # add to end -> [3, 1, 2, 4]
nums.sort()            # sort in place -> [1, 2, 3, 4]
print(nums, "len", len(nums))
print("first/last:", nums[0], nums[-1])
print("slice:", nums[1:3])     # [2, 3]
nums.remove(2)         # remove first matching value
print("after remove:", nums)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `b = a` for a list does NOT copy it — both names point to the same list. Use `a.copy()` or `a[:]`.
- ⚠️ Tuples are immutable: `t[0] = 5` raises TypeError. To 'change' one, build a new tuple.
- ⚠️ Sets are unordered — don't rely on their printing order, and you can't index `s[0]`.
- ⚠️ Accessing a missing dict key with `d['x']` raises KeyError; use `d.get('x', default)` to be safe.
- ⚠️ A single-element tuple needs a trailing comma: `(5,)`. `(5)` is just the integer 5.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

