# 07 — Loops

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~30 min · 🔁 Loop: `README → notes.py → practice.md` · ⬅️ Prerequisite: `../06-conditional-statements/`

## What is it?

**Loops** repeat work without repeating yourself. A `for` loop walks through a sequence —
a list, a string, or the numbers from `range()` — running its body once per item. A
`while` loop instead repeats *as long as* a condition stays `True`, which makes it ideal
for countdowns, retries, and "keep going until done" tasks.

Two steering commands shape every loop: `break` exits immediately, and `continue` skips
the rest of the current lap and starts the next one. Python even ships a quirky bonus —
the loop `else` clause — which runs only if the loop finished *without* hitting `break`,
perfect for "search everything, then report failure" patterns.

🔁 **Analogy — the sushi conveyor belt.** Dishes glide past and you act on each one in turn:
take the tuna, skip the wasabi (`continue`), stop eating entirely when you are full
(`break`). A `for` loop is a belt with a fixed number of plates; a `while` loop is a belt
that keeps serving until you raise your hand and say "no more." Either way, you write the
reaction once and the belt replays it for every plate.

## Why it matters

- **Datasets are loops.** Summing columns, cleaning rows, rendering every search result —
  nearly all data work is "do this to each item."
- **`range()` builds counting loops.** Timers, table generation, retries, and index math
  all start from `range(stop)` or `range(start, stop, step)`.
- **`enumerate()` keeps your place.** When you need both the item *and* its position
  (ranked lists, numbered menus), it beats manual counters.

🐍➡️🤖 **Career hook:** training loops are the heartbeat of machine learning — epoch after
epoch, batch after batch, the same `for` structure you learn here iterates over millions
of examples while tracking loss. Nail loops now and ML training code reads like déjà vu.

## How it works

Picture each loop as a 4-stage lap around a track:

1. **Set up** — `for` grabs the next item (or `while` checks its condition).
2. **Enter or exit** — items left / condition `True`? Run the body. Otherwise, leave.
3. **Steer** — `continue` jumps to the next lap; `break` leaves the track entirely.
4. **Finish** — fall off the end normally and the optional `else` block runs once;
   exit via `break` and `else` is skipped.

```text
for n in range(1, 10):
  n == 5? ── Yes ──▶ break (leave loop, skip else)
  n even? ── Yes ──▶ continue (skip print, next lap)
  otherwise ────────▶ print(n) → next lap
exhausted? ── Yes ──▶ else: "done" (only if no break)
```

## Key concepts

- **for over items** — `for fruit in ["apple", "pear"]:` visits each element directly.
- **range(stop)** — `range(5)` yields `0, 1, 2, 3, 4`; the stop is always excluded.
- **range(start, stop, step)** — `range(2, 11, 2)` yields `2, 4, 6, 8, 10`.
- **Accumulator pattern** — `total = 0` then `total += i` inside the loop builds a sum.
- **while** — `while count > 0:` repeats until the test flips; update the variable!
- **break** — `if n == 5: break` abandons the loop on the spot.
- **continue** — `if n % 2 == 0: continue` skips one lap and keeps looping.
- **enumerate()** — `for i, x in enumerate(names, start=1):` gives index plus value.
- **loop-else** — the `else:` after a loop runs only when no `break` fired.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# Iterate directly over items
for fruit in ["apple", "banana", "cherry"]:
    print("I like", fruit)

# range(stop): 0,1,2,3,4
total = 0
for i in range(5):
    total += i
print("sum 0..4 =", total)   # 10

# range(start, stop, step)
for n in range(2, 11, 2):     # 2,4,6,8,10
    print(n, end=" ")
print()
```

Three mini-patterns in one block: loop straight over values when you care about *things*,
loop over `range(5)` with an accumulator when you care about *adding up*, and loop over
`range(2, 11, 2)` when you need a stepped sequence. Notice the last loop prints on one
line via `end=" "` — a small trick with big payoff for tables and progress output.

Up next in `notes.py`: Example 2 ("while loops, break and continue") counts down to
liftoff and filters odds before 5, and Example 3 ("enumerate and the loop-else") numbers
names from 1 and uses `for...else` to report a failed search.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ *2-minute challenge (no solution here).* Guess the exact output of this fragment before
running it: `for n in range(1, 7):` / `if n == 4: break` / `if n % 2 == 0: continue` /
`print(n, end=" ")`. Which numbers survive both filters, and what would change if you
swapped the `break` and `continue` lines? Run it only after committing to a prediction.

## Common mistakes & gotchas

- ⚠️ `range(5)` is 0,1,2,3,4 — it STOPS before 5. Off-by-one errors come from forgetting this.
- ⚠️ A `while` loop with a condition that never becomes False runs forever. Always update the variable.
- ⚠️ Modifying a list while looping over it causes skipped/duplicated items. Loop over a copy instead.
- ⚠️ `for i in range(len(seq))` then `seq[i]` is clumsy — prefer iterating items directly or `enumerate`.
- ⚠️ `break` only exits the INNERMOST loop, not all nested loops.

## Cheat sheet

```python
for x in ["a", "b", "c"]:
    print(x)
for i in range(5):            # 0..4
    print(i)
for n in range(2, 11, 2):     # evens 2..10
    print(n, end=" ")
for i, v in enumerate(seq, start=1):
    print(i, v)
while count > 0:
    count -= 1
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard).
Try each one before revealing the solution.

## What's next

Repetition mastered? Time to store what you repeat over — step into
[`../08-lists-tuples-sets-dictionaries/`](../08-lists-tuples-sets-dictionaries/)
and meet Python's four essential collections.
