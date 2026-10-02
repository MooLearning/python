# 04 — Input, Output and Type Casting

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

*⏱️ ~30 min · Loop: `README → notes.py → practice.md` · Prerequisite: [`03-operators`](../03-operators/).*

## What is it?

Python talks to humans through two doors: `print()` sends values **out** to the screen, and `input()`
reads keystrokes **in** from the user. The catch that defines this whole topic: `input()` always hands
you a `str`, even when the user types digits — so `"42" + 8` crashes until you **cast** (convert) with
`int()` or `float()`. Casting runs both ways: `str(2026)` turns numbers back into text for joining,
and f-strings like `f"{name} is {age}"` are the modern, readable way to weave values into messages.

`print()` is more flexible than it looks: `sep=` changes what goes *between* items, `end=` changes what
goes *at the end* (newline by default), and f-string formats like `{pi:.2f}` round numbers inline.
Together these five tools — `print`, `input`, `int`/`float`, `str`, f-strings — form the complete
airlock between human text and Python values.

Picture an airport customs desk with a translator. Arriving passengers (`input()`) always carry foreign
phrasebooks — everything is text, `"42"` with invisible quotes. The translator (`int()`, `float()`)
stamps the phrasebook into local currency your calculators accept; without the stamp, the till
(`+ 8`) rejects it. Departing flights (`print()`) reverse the trip: the translator (`str()`,
f-strings) turns local coins back into announcements every traveller reads, with `sep` and `end`
deciding the seating layout and whether the announcement ends with a full stop or a "to be continued".

## Why it matters

- Nearly every script is a conversation: prompt for a name, read an age, validate a price, print a
  receipt. Forgetting the input-is-text rule causes the most common beginner traceback of all.
- Formatting is a user-facing skill: aligned receipts, `2`-decimal prices (`{pi:.2f}`), dash-joined
  codes (`sep="-"`) — small touches that separate toy scripts from trustworthy tools.
- Career hook: AI pipelines are type airlocks at scale — CSV cells arrive as strings, models demand
  floats, reports need formatted text. Casting cleanly here is data cleaning later.

## How it works

Mental model — data crosses the human/Python border in five steps:

1. **Prompt** — `input("Enter a number: ")` displays text and waits for Enter.
2. **Arrive as text** — keystrokes land as a `str`: `"42"`, never `42`.
3. **Cast to compute** — `number = int(raw)` (or `float(raw)`) converts; math now works.
4. **Compute** — operators run on real numbers: `number + 8` is `50`.
5. **Format to show** — `print(f"total: {number}")` or `str(x)` turns values back into text.

```text
keyboard "42" --input()--> [str "42"] --int()--> [int 42] --+ 8--> [int 50] --f-string--> screen "50"
```

Skip step 3 and step 4 explodes; skip step 5 and concatenation complains.

## Key concepts

- **`print()`** — shows values: `print("hi", 42)` puts a space between items by default.
- **`sep=`** — separator between items: `print("a", "b", sep="-")` shows `a-b`.
- **`end=`** — line ending: `print("x", end=" ")` stays on the same line instead of newline.
- **`input(prompt)`** — waits for typing, returns it: `raw = input("Age? ")` is always a `str`.
- **`int()` / `float()`** — text-to-number: `int("42")` is `42`; `float("3.5")` is `3.5`.
- **`str()`** — anything-to-text: `str(2026) + "!"` is `"2026!"`.
- **f-strings** — embed values: `f"{name} is {age}"`; format inline with `f"{pi:.2f}"` for `3.14`.
- **`int()` truncates** — `int(9.9)` is `9`, no rounding; `round(9.9)` is `10`.
- **`bool()` of empties** — `bool(0)` and `bool("")` are `False`; `bool(3)` is `True`.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
name = "Ada"
age = 36

# f-strings: put variables inside {curly braces}
print(f"{name} is {age} years old.")

# sep controls what goes BETWEEN items; end controls what goes at the END
print("a", "b", "c", sep="-")        # a-b-c
print("no newline here ->", end=" ")
print("...continued on same line")

# Format numbers: 2 decimal places
pi = 3.14159
print(f"pi is about {pi:.2f}")        # pi is about 3.14
```

This is Example 1 from `notes.py`: it tours the *output* side only — a plain f-string greeting, then
`sep="-"` joining versus `end=" "` gluing two prints onto one line, then `{pi:.2f}` rounding `3.14159`
for display without changing the variable. Watch how `{...}` placeholders keep text readable where
`+` concatenation would need manual `str()` calls.

Keep going in `notes.py`: Example 2 ("Reading input is always a string") simulates `input()` returning
`"42"` and casts it with `int()` so `+ 8` works, and Example 3 ("Casting between types (and what
breaks)") converts `int("100")`, `float("3.5")`, `str(2026)`, truncates `int(9.9)`, and probes
`bool(0)` vs `bool("")` vs `bool(3)`.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute challenge (no solution — reason it out): predict what each of these prints —
`print(int("7") + int("8"))`, `print("7" + "8")`, and `print(int(9.9))` — before running them. Then
tinker: what happens with `int("3.5")`, and how would you fix it to get `3.5` as a number? Try your
fix two ways: one with a nested cast, one that skips `int()` entirely.

## Common mistakes & gotchas

- ⚠️ `input()` returns a string ALWAYS. `input() + 1` crashes; cast with `int()` first.
- ⚠️ `int("3.5")` raises ValueError — you can't int() a decimal string. Use `int(float("3.5"))`.
- ⚠️ `int(9.9)` gives `9` (it truncates toward zero); it does NOT round. Use `round()` to round.
- ⚠️ You can't do `"age: " + 30` — concatenate strings only. Use an f-string or `str(30)`.
- ⚠️ Empty string, 0, 0.0, None and empty containers are all 'falsy' — `bool()` of them is False.

## Cheat sheet

```python
print(f"Name: Sam | Age: 20")       # f-string interpolation
print("a", "b", "c", sep=", ")      # custom separator
print("hi", end=" ")                # no newline at end
print(f"{3.14159:.1f}")             # 3.1 (1 decimal place)
print(int("7") + int("8"))          # 15 (cast, then add)
print(float("3.75") * 2)            # 7.5
print("Year " + str(2026))          # Year 2026
print(int(9.9), round(9.9))         # 9 10 (truncate vs round)
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Head to [`../05-strings-and-methods/`](../05-strings-and-methods/) to go deeper on text itself —
slicing, casing, searching, and splitting the strings you now know how to read and print.
