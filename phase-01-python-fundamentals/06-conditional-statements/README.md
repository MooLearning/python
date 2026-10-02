# 06 — Conditional Statements

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~25 min · 🔁 Loop: `README → notes.py → practice.md` · ⬅️ Prerequisite: `../05-strings-and-methods/`

## What is it?

Conditional statements give your program **judgment**. An `if` block runs only when its
condition is `True`; `elif` ("else if") offers the next candidate test; `else` catches
everything left over. Python reads these branches top to bottom and executes the *first*
one that matches — then skips the rest entirely.

Instead of curly braces, Python uses **indentation** to show which lines belong to each
branch. Four spaces are the convention, and the interpreter enforces them: indent wrong
and the program will not even start. That strictness is a feature — it forces your logic
to look the way it behaves.

🚦 **Analogy — the nightclub bouncer with a checklist.** A guest walks up and the bouncer
works down the list: "On the VIP list? In you go. No? Got a ticket and ID? This way. No?
Then it's the general queue." Only one door opens per guest, the checks happen in order,
and the fallback line at the bottom catches everyone else. `if` / `elif` / `else` is that
bouncer, deciding which code path each value walks through.

## Why it matters

- **Input validation lives here.** Empty names, out-of-range ages, wrong passwords — every
  guard clause that keeps bad data out is a conditional.
- **Business rules are branches.** Grading scales, shipping tiers, leap-year math, and
  FizzBuzz-style filters are all ordered `if` / `elif` chains.
- **Combined conditions scale up.** `and`, `or`, `not`, and chained comparisons like
  `0 < x < 10` let one line express surprisingly rich decisions.

🐍➡️🤖 **Career hook:** ML systems are wrapped in conditionals — confidence thresholds
("serve the prediction *if* score > 0.9, *else* ask a human"), data-quality gates, and
safety filters. Clean branching is what makes smart models behave reliably in production.

## How it works

Run this mental checklist every time you write a branch:

1. **Test top-down** — Python evaluates `if`, then each `elif`, in written order.
2. **First True wins** — the matching block runs; every later branch is skipped unseen.
3. **Fall through to `else`** — if nothing matched, the `else` block runs (if present).
4. **Indent to belong** — everything indented under the header is one atomic branch.
5. **Keep tests honest** — lean on truthiness (`if items:`) instead of `== True`.

```text
score = 82
  │ score >= 90? ── No ──▶│ score >= 80? ── Yes ──▶ grade = "B" ──▶ skip rest
                          │ score >= 70? (never checked)
                          │ else (never reached)
```

## Key concepts

- **if / elif / else** — `if score >= 90:` opens a branch; first `True` wins.
- **Colon + indent** — every header ends with `:` and its body is indented 4 spaces.
- **Branch order** — put the most specific test first; `elif` never runs if `if` matched.
- **Truthiness** — `if "":` is falsy; `if [1, 2]:` is truthy without calling `len()`.
- **not** — `if not name:` elegantly catches `""`, `None`, and other empty values.
- **and / or** — `if age >= 18 and has_ticket:` demands both halves be true.
- **Chained comparisons** — `if 0 < x < 10:` reads like math and beats nested `and`s.
- **Ternary** — `"even" if n % 2 == 0 else "odd"` picks a value in a single line.
- **No fall-through** — unlike `switch` in other languages, only one branch ever fires.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:        # only checked if the previous test was False
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)   # B
```

Walk through it like the interpreter does: `82 >= 90` is `False`, so the first block is
skipped; `82 >= 80` is `True`, so `grade` becomes `"B"` and Python jumps straight past
the remaining `elif` and `else` without testing them. Reorder these thresholds — or feed
in `95`, `74`, `40` — and watch a different single branch claim the win each time.

Then open `notes.py`: Example 2 ("Truthiness and combined conditions") uses `if not name:`,
`if items:`, and `and` for ticket-gate logic, while Example 3 ("Ternary expression (one-line if/else)")
compresses even/odd labeling and a temperature check into one-liners.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ *2-minute challenge (no solution here).* Without running anything, predict what prints for
`temp = 19` in this chain: `if temp > 28: print("hot")` / `elif temp > 18: print("mild")` /
`elif temp > 10: print("cool")` / `else: print("cold")`. Then swap the first two branches
so `> 18` comes first — does `temp = 30` still print `"hot"`? Argue with yourself about
*why* before you touch the keyboard.

## Common mistakes & gotchas

- ⚠️ Use `==` to compare, not `=` (which assigns). `if x = 5:` is a SyntaxError.
- ⚠️ Indentation must be consistent (4 spaces is standard). Mixing tabs and spaces causes errors.
- ⚠️ Every `if`/`elif`/`else` line ends with a colon `:` — forgetting it is a SyntaxError.
- ⚠️ `elif` only runs if earlier conditions were False. Order your branches from most to least specific.
- ⚠️ `if items == True:` is fragile — just write `if items:` to test truthiness.

## Cheat sheet

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
label = "even" if n % 2 == 0 else "odd"
if 0 < x < 10 and items:
    print("in range, non-empty")
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard).
Try each one before revealing the solution.

## What's next

Decisions down? Now repeat them at scale — continue to [`../07-loops/`](../07-loops/)
where `for` and `while` turn one branch of logic into thousands of repetitions.
