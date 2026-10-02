# 09 — Comprehensions

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~20 min · Loop: `README → notes.py → practice.md` · Prereq: [08 — Lists, Tuples, Sets, Dictionaries](../08-lists-tuples-sets-dictionaries/)

## What is it?

A **comprehension** builds a list, set, or dict in a single expressive line.
Instead of creating an empty collection and appending in a loop, you describe
the result directly: `[expr for item in iterable if condition]`. Python offers
three flavours — list `[...]`, set `{...}`, and dict `{key: value for ...}` —
all following the same inside-out grammar.

Think of it like a coffee-shop order slip. You don't stand behind the counter
steaming milk yourself; you hand over one slip that says "one oat latte for
every name on this list, except decaf drinkers." The barista reads the slip
left to right — what to make, where the names come from, who to skip — and
hands back a full tray. A comprehension is that slip: output, source, filter.

## Why it matters

- **Data shaping:** cleaning CSV rows, squaring sensor readings, or uppercasing
  a word list collapses a 4-line loop into one scannable line.
- **Dict and set building:** frequency tables (`{word: count ...}`), lookups
  (`{id: record ...}`), and deduplication (`{tag for ...}`) are one-liners.
- **Reading real code:** open-source Python, Kaggle notebooks, and Django
  codebases are full of comprehensions — fluency here pays off everywhere.
- **AI-career hook:** preprocessing datasets (token lengths, label maps,
  filtered samples) is comprehension-heavy work in ML pipelines.

## How it works

Mental model — every comprehension runs this little assembly line:

1. **Source:** `for item in iterable` pulls items one at a time.
2. **Filter (optional):** `if condition` at the END decides keep or skip.
3. **Transform:** the leading `expr` reshapes each kept item.
4. **Collect:** results gather into a brand-new list, set, or dict.

```text
source iterable ──► [ filter? ] ──► [ transform ] ──► NEW collection
                       (if)            (expr)         (original untouched)
```

The conditional *expression* (`a if cond else b`) is the exception: it lives
at the FRONT, before `for`, because it is part of the transform step.

## Key concepts

- **List comprehension** — `[x * x for x in range(5)]` gives `[0, 1, 4, 9, 16]`.
- **Filtering with trailing `if`** — `[x for x in nums if x > 0]` keeps positives.
- **Transform + filter together** — `[w.upper() for w in words if len(w) > 2]`.
- **Conditional expression (front)** — `[x if x > 0 else 0 for x in xs]` replaces values.
- **Dict comprehension** — `{n: n * n for n in range(1, 6)}` maps numbers to squares.
- **Dict inversion** — `{v: k for k, v in prices.items()}` swaps keys and values.
- **Set comprehension** — `{n % 3 for n in range(10)}` yields `{0, 1, 2}` (unique only).
- **Nested loops** — `[x for row in grid for x in row]` flattens one level, left to right.
- **Generator cousin** — `(x * x for x in range(6))` is lazy; wrap with `list()` to realise it.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# The loop way
squares = []
for x in range(6):
    squares.append(x * x)
print(squares)            # [0, 1, 4, 9, 16, 25]

# The comprehension way (same result, one line)
squares = [x * x for x in range(6)]
print(squares)

# With a filter: keep only evens, then square them
evens_sq = [x * x for x in range(10) if x % 2 == 0]
print(evens_sq)           # [0, 4, 16, 36, 64]
```

The loop version spells out every step; the one-liner says the same thing in
the order *transform → source → filter*. Notice the trailing `if x % 2 == 0`
runs before squaring, so only evens get squared. Keep exploring in `notes.py`:
Example 2 ("Transforming text and conditional expressions") uppercases words
and puts `if/else` up front, and Example 3 ("Dict and set comprehensions")
builds a square-map, inverts a price dict, and collects unique remainders.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute prediction (no peeking — run it after you guess): what does
`[w[::-1] for w in ["abc", "de", "fghi"] if len(w) > 2]` print, and in what
order do the filter and the reversal happen? Now change the trailing `if` to a
front `if/else` that keeps short words unchanged instead of dropping them, and
predict the new output before running.

## Common mistakes & gotchas

- ⚠️ The filtering `if` goes at the END; the `if/else` *expression* goes at the FRONT (before `for`).
- ⚠️ Deeply nested comprehensions become unreadable — if it needs comments, use a real loop.
- ⚠️ `{}` alone is an empty DICT, not an empty set. Use `set()` for an empty set.
- ⚠️ A comprehension creates a brand-new list each time; it doesn't modify the source iterable.
- ⚠️ Don't call expensive functions twice; comprehensions evaluate the expression for every item.

## Cheat sheet

```python
squares = [x * x for x in range(6)]            # list
evens = [x for x in range(10) if x % 2 == 0]   # filter
labels = ["big" if x > 5 else "small" for x in range(8)]
sq_map = {n: n * n for n in range(1, 6)}       # dict
by_price = {v: k for k, v in {"a": 3}.items()} # invert
unique = {n % 3 for n in range(10)}            # set
flat = [x for row in [[1, 2], [3]] for x in row]
lens = [len(w) for w in "the quick fox".split()]
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Finished the tray? Head to [`10 — Functions`](../10-functions/) to package logic into reusable blocks.
