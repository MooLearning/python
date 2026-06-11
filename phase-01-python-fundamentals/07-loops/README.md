# 07 — Loops

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Loops** repeat work. A `for` loop iterates over a sequence (a list, a string, a `range`). A `while` loop repeats as long as a condition stays True. `break` exits a loop early, `continue` skips to the next iteration, and the loop's `else` runs if the loop finished without breaking.

## Why it matters

Computers shine at repetition. Processing every item in a dataset, retrying until success, or summing a list — all loops. `for` + `range` and `for` over collections are everyday tools.

## Key concepts

- **for loop** — Repeats once per item: `for x in [1,2,3]:`.
- **range(start, stop, step)** — Generates numbers; stop is excluded. `range(5)` -> 0..4.
- **while loop** — Repeats while a condition is True. Make sure it eventually becomes False!
- **break / continue** — Exit the loop entirely / skip to the next iteration.
- **enumerate()** — Loop with an index AND the item: `for i, x in enumerate(seq):`.
- **loop else** — Runs only if the loop didn't hit `break` — handy for search loops.

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

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `range(5)` is 0,1,2,3,4 — it STOPS before 5. Off-by-one errors come from forgetting this.
- ⚠️ A `while` loop with a condition that never becomes False runs forever. Always update the variable.
- ⚠️ Modifying a list while looping over it causes skipped/duplicated items. Loop over a copy instead.
- ⚠️ `for i in range(len(seq))` then `seq[i]` is clumsy — prefer iterating items directly or `enumerate`.
- ⚠️ `break` only exits the INNERMOST loop, not all nested loops.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

