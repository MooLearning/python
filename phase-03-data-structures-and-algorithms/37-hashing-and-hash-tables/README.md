# 37 — Hashing and Hash Tables

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **hash table** stores key→value pairs and finds any key in **O(1) average** time. A **hash function** turns a key into an array index; collisions (two keys, same index) are resolved by **chaining** (a list per bucket) or **open addressing** (probe for a free slot). Python's `dict` and `set` are highly optimized hash tables.

## Why it matters

Hashing turns slow O(n) searches into O(1) lookups — the single biggest speedup tool in everyday coding. Counting, de-duplication, caching, and 'have I seen this?' problems all lean on it.

## Key concepts

- **Hash function** — Maps a key to a bucket index; good ones spread keys evenly.
- **Bucket** — A slot in the underlying array where entries live.
- **Collision** — Two keys hashing to the same bucket — must be handled.
- **Chaining** — Each bucket holds a list of entries that collided.
- **Load factor** — entries / buckets; when high, the table resizes (rehash).
- **Hashable keys** — Keys must be immutable (str, int, tuple) — lists can't be keys.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# dict: O(1) average insert, lookup, delete
phone = {"alice": 123, "bob": 456}
phone["carol"] = 789
print(phone["bob"])          # 456  -> O(1)
print("alice" in phone)      # True -> O(1) key check
print(phone.get("dave", -1)) # -1   -> default if missing

# set: membership in O(1) (vs O(n) for a list)
seen = set()
for x in [1, 2, 2, 3, 1]:
    if x in seen:
        print("duplicate:", x)
    seen.add(x)
print("unique:", seen)       # {1, 2, 3}
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Only immutable (hashable) values can be keys — `{[1,2]: 'x'}` raises TypeError.
- ⚠️ Hash order is not sorted; dict preserves INSERTION order, not key order.
- ⚠️ A bad hash function clusters keys into few buckets, degrading to O(n).
- ⚠️ Mutating an object after using it as a key corrupts lookups — keep keys immutable.
- ⚠️ `d[missing]` raises KeyError; use `d.get(k, default)` or `defaultdict` to avoid it.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

