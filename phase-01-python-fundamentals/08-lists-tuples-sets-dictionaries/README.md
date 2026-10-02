# 08 — Lists, Tuples, Sets and Dictionaries

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~30 min · 🔁 Loop: `README → notes.py → practice.md` · ⬅️ Prerequisite: `../07-loops/`

## What is it?

Python organizes multi-value data with four core **collections**. A **list** (`[]`) is an
ordered, changeable queue — your everyday workhorse. A **tuple** (`()`) is its disciplined
sibling: ordered but **immutable**, ideal for fixed records like coordinates. A **set**
(`{}`) throws away order and duplicates to answer "have I seen this?" at lightning speed.
A **dictionary** (`{key: value}`) attaches labels to values so you can look anything up by
name instead of position.

The real skill is not memorizing syntax but **choosing**. Need order plus edits? List.
A permanent pair that should never change? Tuple. Fast membership or dedup? Set.
Lookup by meaningful key? Dict. Pick well and your code practically writes itself.

🍱 **Analogy — the bento kitchen.** A list is the open shelf where you stack, reorder, and
grab plates freely. A tuple is a sealed lunchbox — what is packed at noon is exactly what
you eat. A set is the spice rack that keeps one jar per spice no matter how many times you
restock. And a dict is the labeled pantry: you ask for "flour" by name and the right bin
slides out instantly, no counting shelves required.

## Why it matters

- **Almost every program is collection wrangling.** Playlists, carts, leaderboards, and
  CSV columns are lists; config pairs and coordinates are tuples.
- **Uniqueness and lookup are superpowers.** Sets dedupe millions of rows and power
  union/intersection logic; dicts turn slow scans into instant `d[key]` retrievals.
- **DSA starts here.** Stacks, queues, graphs, and frequency tables are all just clever
  arrangements of these four building blocks.

🐍➡️🤖 **Career hook:** ML feature stores are dicts, vocabularies are sets, batches are
lists of tuples. Word-frequency counters (`counts[w] = counts.get(w, 0) + 1`) are the
direct ancestor of tokenizers and bag-of-words models you will meet in NLP.

## How it works

Choose and use a collection in four moves:

1. **Ask what you need** — order? mutability? uniqueness? lookup by key?
2. **Pick the container** — list `[]` / tuple `()` / set `{}` / dict `{k: v}`.
3. **Operate** — list `.append()` / `.sort()` / `.remove()`; set `|` / `&`; dict `d[k]` / `.get()`.
4. **Respect the contract** — tuples and dict keys stay hashable and fixed; sets stay unordered.

```text
need ── ordered + editable? ──▶ list [3, 1, 2] ── append/sort/remove
  ├── fixed record? ──────────▶ tuple (3, 4) ──── unpack, never mutate
  ├── unique / membership? ───▶ set {1, 2, 3} ─── | union, & intersect
  └── lookup by label? ───────▶ dict {"Ada": 36} ─ d[key], d.get(k, default)
```

## Key concepts

- **list literal** — `nums = [3, 1, 2]` keeps insertion order and allows duplicates.
- **list edits** — `nums.append(4)` grows; `nums.sort()` reorders; `nums.remove(2)` deletes by value.
- **Indexing + slicing** — `nums[0]` is first, `nums[-1]` is last; `nums[1:3]` carves a span.
- **tuple** — `point = (3, 4)` is fixed; `x, y = point` unpacks it into names.
- **Single tuple** — `(5,)` with a trailing comma is a tuple; `(5)` is just an int.
- **set dedup** — `{1, 2, 2, 3}` collapses to `{1, 2, 3}` automatically.
- **set algebra** — `a | b` is union, `a & b` is intersection, `3 in a` is instant.
- **dict lookup** — `ages["Ada"]` is direct; `ages.get("Zed", "?")` is the safe version.
- **dict iteration** — `for name, age in ages.items():` walks key-value pairs together.

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

This is the list lifecycle in miniature: grow with `append`, reorder with `sort` (note it
mutates in place and returns `None`), inspect with indexing and slicing, then shrink with
`remove`. Every `print` freezes one stage so you can see mutation happening step by step —
contrast that with tuples later, where the equivalent "edit" would raise `TypeError`.

Continue in `notes.py`: Example 2 ("Tuples and sets") unpacks a coordinate and demos union,
intersection, and membership speed, while Example 3 ("Dictionaries: key-value lookups") adds
`"Grace"`, contrasts `d[key]` with safe `.get()`, and loops with `.items()`.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ *2-minute challenge (no solution here).* Predict the final state — without running — of:
`bag = [2, 1, 2]` then `bag.append(3)` then `bag.sort()` then `bag.remove(2)`. What is
`bag` now, and what are `bag[0]` and `bag[-1]`? Then ask yourself: what would `set(bag)`
contain, and why does converting there and back lose information? Run only to confirm.

## Common mistakes & gotchas

- ⚠️ `b = a` for a list does NOT copy it — both names point to the same list. Use `a.copy()` or `a[:]`.
- ⚠️ Tuples are immutable: `t[0] = 5` raises TypeError. To 'change' one, build a new tuple.
- ⚠️ Sets are unordered — don't rely on their printing order, and you can't index `s[0]`.
- ⚠️ Accessing a missing dict key with `d['x']` raises KeyError; use `d.get('x', default)` to be safe.
- ⚠️ A single-element tuple needs a trailing comma: `(5,)`. `(5)` is just the integer 5.

## Cheat sheet

```python
nums = [3, 1, 2]
nums.append(4); nums.sort(); nums.remove(2)
point = (3, 4); x, y = point
single = (5,)                      # one-element tuple
uniq = set([1, 2, 2, 3])           # {1, 2, 3}
a | b                              # union
a & b                              # intersection
d = {"a": 1}; d.get("z", 0)        # safe lookup
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard).
Try each one before revealing the solution.

## What's next

Collections in your pocket? Level them up with one-liner construction in
[`../09-comprehensions/`](../09-comprehensions/) — where loops that build lists,
sets, and dicts collapse into elegant single expressions.
