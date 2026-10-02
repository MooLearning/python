# 03 — Operators

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

*⏱️ ~25 min · Loop: `README → notes.py → practice.md` · Prerequisite: [`02-variables-and-data-types`](../02-variables-and-data-types/).*

## What is it?

**Operators** are the symbols (and few keywords) that *do things* to values: arithmetic (`+ - * / //
% **`), comparison (`== != < > <= >=`), logical (`and or not`), assignment shortcuts (`+= -= *=` …),
and bitwise (`& | ^ ~ << >>`). Arithmetic turns numbers into numbers; comparisons and logical
combinations turn anything into a `bool`, the exact fuel that `if` statements and `while` loops burn.

Precedence decides who goes first when operators pile up — `**` before `* / // %` before `+ -`, with
comparisons, `not`, `and`, then `or` trailing behind — and parentheses always win. Python even lets
comparisons chain the way math class writes them: `0 < x < 10` means "between", no extra `and` needed.

Imagine a gameshow control room. Arithmetic operators are the kitchen crew dicing numbers (`17 % 5`
keeps the leftover `2`), comparison operators are bouncers answering only "yes" or "no" (`age >= 18`),
and logical operators are the producers combining bouncer reports (`tall and paid`). Assignment
shortcuts are tally counters that click upward (`score += 10`), while bitwise operators work in the
basement, flipping the actual binary switches behind each integer. Same room, five crews, zero overlap
once you learn the uniforms.

## Why it matters

- Practically all computation is operators: totals and remainders (`//`, `%`), range checks
  (`10 <= x <= 100`), combined conditions (`temp > 20 and humid`), running tallies (`total += sale`).
- The even/odd test (`n % 2 == 0`), pagination math (`page // size`), and retry backoff (`2 ** attempt`)
  are all one-line operator idioms you will reuse for years.
- Career hook: ML feature code is operator soup — normalizing (`(x - mean) / std`), masking
  (`(age > 18) & (active)`), shifting bits for encodings. Reading precedence fluently is reading models.

## How it works

Mental model — every operator is a mini-machine: values in, one value out:

1. **Feed** it operands: `17` and `5` into `//`.
2. **Compute** per its crew: arithmetic calculates, comparison judges to `True`/`False`.
3. **Combine** — `and`/`or` wire judgments together; `+=` writes the result back into the name.
4. **Order** — when machines chain, precedence (`**` → `*` → `+` → comparisons → `not` → `and` → `or`)
   picks the sequence; parentheses override everything.

```text
2 + 3 * 4 ** 2
        ^^^^^^^  step 1: **  -> 16
    ^^^^^^^^^^^  step 2: *   -> 48
^^^^^^^^^^^^^^^  step 3: +   -> 50
```

When in doubt, parenthesize — `(2 + 3) * 4` says what you mean for free.

## Key concepts

- **Arithmetic** — `17 + 5` is `22`; `17 / 5` is `3.4` (float!); `17 // 5` is `3`; `17 % 5` is `2`.
- **Power** — `2 ** 10` is `1024`; `**` binds tightest, so `-2 ** 2` is `-4`.
- **Comparison** — `7 == 7` is `True`; `7 != 5` is `True`; result is always a `bool`.
- **Chained comparison** — `0 < 7 < 10` is `True`, read exactly like math.
- **Logical** — `7 > 5 and 7 < 10` is `True`; `not False` is `True`; `or` needs just one side.
- **`and`/`or` return operands** — `0 or "x"` is `"x"`, not `True`; useful for defaults.
- **Assignment shortcuts** — `score = 0; score += 10` adds in place; also `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
- **Bitwise** — `5 & 3` is `1` (bits `101 & 011`); `1 << 4` is `16` (shift = × 2ⁿ).
- **Precedence** — `2 + 3 * 4` is `14`; wrap intent in parens: `(2 + 3) * 4` is `20`.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
a, b = 17, 5
print("add ", a + b)    # 22
print("sub ", a - b)    # 12
print("mul ", a * b)    # 85
print("div ", a / b)    # 3.4   (float)
print("floor", a // b)  # 3     (drops the decimal)
print("mod ", a % b)    # 2     (remainder)
print("pow ", a ** b)   # 1419857
```

This is Example 1 from `notes.py`: one pair (`17, 5`) runs the full arithmetic gauntlet so the
contrasts stick — `/` vs `//` (exact float vs dropped decimal), `%` as the leftover, `**` exploding
to `1419857`. Read each trailing comment as the machine's receipt for what it returned.

Keep going in `notes.py`: Example 2 ("Comparison and logical operators") judges `x = 7` with `>`, `==`,
`and`/`or`/`not`, and chained `0 < x < 10`, and Example 3 ("Assignment shortcuts and bitwise basics")
grows `score` with `+=`/`*=` then flips bits with `&`, `|`, `^`, and `<<`.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute challenge (no solution — predict first): without running, guess each result — `29 // 6`,
`29 % 6`, `2 + 3 * 4 ** 2`, and `5 and 3` vs `5 & 3`. Write your four guesses down, then run one
`python -c` line or a mini script to check. For any miss, add parentheses that would force *your*
guessed order and re-run — which version reads more clearly?

## Common mistakes & gotchas

- ⚠️ `/` always returns a float, even `4 / 2` gives `2.0`. Use `//` for integer division.
- ⚠️ `%` of negative numbers may surprise you: `-7 % 3` is `2` in Python, not `-1`.
- ⚠️ `and`/`or` return one of the operands, not always True/False: `0 or 'x'` is `'x'`.
- ⚠️ Don't confuse `&`/`|` (bitwise) with `and`/`or` (logical). `5 and 3` is `3`, but `5 & 3` is `1`.
- ⚠️ Precedence traps: `2 + 3 * 4` is 14, not 20. Use parentheses to be explicit.

## Cheat sheet

```python
print(29 // 6, 29 % 6)      # 4 5  (quotient, remainder)
print(2 + 3 * 4 ** 2)       # 50 (precedence: ** then * then +)
print(10 <= 50 <= 100)      # True (chained comparison)
print(12 % 2 == 0)          # True (even test)
n = 7; n *= 3; print(n)     # 21 (compound assignment)
print(5 & 3, 5 | 3, 1 << 4) # 1 7 16 (bitwise basics)
print(0 or "x")             # 'x' (or returns operand)
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Head to [`../04-input-output-and-type-casting/`](../04-input-output-and-type-casting/) to mix operators
with the outside world — reading typed input, printing formatted output, and converting types safely.
