# 05 — Strings and Methods

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~25 min · 🔁 Loop: `README → notes.py → practice.md` · ⬅️ Prerequisite: `../04-input-output-and-type-casting/`

## What is it?

A **string** is an ordered sequence of characters wrapped in quotes — single, double, or triple.
Python treats text as a first-class citizen: every string knows its own length, its own
position map, and carries a toolbox of **methods** (`.upper()`, `.strip()`, `.split()`,
`.replace()`, `.find()`) for reshaping itself. You reach inside with **indexing** (`s[0]`)
and carve out pieces with **slicing** (`s[1:4]`).

Crucially, strings are **immutable**. You never repaint a character in place; every "edit"
quietly builds and returns a brand-new string while the original sits untouched. Once that
clicks, apparently weird behavior — like `s.upper()` seemingly doing nothing — makes
perfect sense.

🎨 **Analogy — the bead necklace.** Picture each character as a glass bead threaded in order
on a string. You can count beads from either end, snip out a middle section to admire, or
photograph the whole necklace reversed. But you cannot melt one bead into a new color while
it stays threaded — you must restring a fresh copy with the bead swapped. That is exactly
how Python strings behave.

## Why it matters

- **User input and files are text first.** Names, CSV rows, log lines, and API responses all
  arrive as strings before you convert them into numbers or dates.
- **Cleaning is half the job.** Stripping whitespace, splitting on commas, swapping
  separators, and normalizing case turn messy real-world text into usable data.
- **Reports and prompts are built, not hardcoded.** f-strings let you inject live values,
  align columns, and format decimals directly inside readable sentences.

🐍➡️🤖 **Career hook:** every NLP and LLM pipeline starts as string surgery — tokenizing
sentences, chunking documents, and formatting prompts. Master `.split()`, `.join()`, and
f-strings now and prompt engineering later feels like home turf.

## How it works

Think of any string operation as a 4-step trip to the text workbench:

1. **Locate** — resolve a position (`s[0]`, `s[-1]`) or a span (`s[start:stop:step]`,
   stop excluded).
2. **Copy, don't mutate** — slicing and methods return a *new* string object.
3. **Transform** — apply a method (`.strip()`, `.replace()`, `.upper()`) to the copy.
4. **Capture** — assign the result (`clean = raw.strip()`) or it vanishes into thin air.

```text
original:  "   Hello, World!   "
                │ strip() │ upper() │ split(",")
                ▼         ▼         ▼
new strings ──► "Hello, World!" ──► "HELLO, WORLD!" ──► ["HELLO", " WORLD!"]
(original unchanged the whole time)
```

## Key concepts

- **Indexing** — first char is `s[0]`, last is `s[-1]`; counting starts at zero.
- **Slicing** — `s[start:stop:step]` carves a span; `s[0:3]` grabs indices 0–2.
- **Open-ended slices** — `s[2:]` runs to the end; `s[:2]` starts at the beginning.
- **Reverse trick** — `s[::-1]` walks backwards with step `-1`.
- **Immutability** — `s[0] = "X"` is illegal; build anew with `s.replace("P", "X")`.
- **Case + trim** — `"  Hi ".strip().upper()` gives `"HI"`.
- **Split and join** — `"a,b".split(",")` → list; `"-".join(["a", "b"])` → `"a-b"`.
- **Search** — `"hello".find("l")` returns `2`, or `-1` when absent.
- **f-strings** — `f"{name} scored {score:.1f}%"` embeds and formats values inline.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
s = "Python"
print(s[0])     # P    (first character, index 0)
print(s[-1])    # n    (last character)
print(s[0:3])   # Pyt  (indices 0,1,2 -- stop is excluded)
print(s[2:])    # thon (from index 2 to the end)
print(s[:2])    # Py   (start to index 1)
print(s[::-1])  # nohtyP (reverse using step -1)
print(len(s))   # 6    (number of characters)
```

This snippet is your position map for the word `"Python"`. Positive indices march left to
right from `0`, negative index `-1` grabs the tail, and every slice stops *before* its end
bound — which is why `s[0:3]` yields three letters, not four. The `[::-1]` reversal and
`len()` call round out the survival kit you will reuse on every text task.

Keep going in `notes.py`: Example 2 ("Essential string methods") chains `strip`, `split`,
`join`, `replace`, and `find` on messy input, and Example 3 ("Building and formatting strings")
builds aligned mini-reports with f-strings while proving immutability with `+`.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ *2-minute challenge (no peeking at solutions).* Open a Python REPL and predict — *before*
you run — what each of these prints: `s = "stressed"`; `s[1:5]`; `s[::-1]`; `s.upper().replace("S", "*")`.
Then tweak one slice bound at a time (`s[1:6]`, `s[-5:-1]`, `s[::2]`) and narrate out loud
why the output changed. Do not write the answer down here — just observe and experiment.

## Common mistakes & gotchas

- ⚠️ Strings are immutable: `s[0] = 'X'` raises TypeError. Create a new string instead.
- ⚠️ Indexing past the end (`s[100]`) raises IndexError, but SLICING past the end is safe.
- ⚠️ `.find()` returns -1 when not found (no error); `.index()` raises ValueError. Pick deliberately.
- ⚠️ `.split()` with no argument splits on ANY whitespace and drops empties — different from `.split(' ')`.
- ⚠️ Methods return NEW strings; `s.upper()` alone does nothing unless you store the result.

## Cheat sheet

```python
s = "  Hello, World!  "
s[0]                          # first character
s[-1]                         # last character
s[1:5]                        # slice (stop excluded)
s[::-1]                       # reverse the string
s.strip().lower()             # trim + normalize case
"a,b,c".split(",")            # ['a', 'b', 'c']
", ".join(["a", "b"])         # 'a, b'
f"Hi {name}, you are {age}"   # f-string interpolation
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard).
Try each one before revealing the solution.

## What's next

Strings clean? Time to make decisions with them — head to [`../06-conditional-statements/`](../06-conditional-statements/)
and learn how `if` / `elif` / `else` branches your programs.
