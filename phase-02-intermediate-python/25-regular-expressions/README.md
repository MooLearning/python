# 25 — Regular Expressions

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Regular expressions** (regex) are a mini-language for describing text patterns. With the `re` module you can search, match, extract, and replace based on patterns like 'one or more digits' (`\d+`) or 'an email-ish string'. Patterns are best written as **raw strings** (`r"..."`) so backslashes survive.

## Why it matters

Validating input (emails, phone numbers), scraping data out of text, cleaning datasets, and tokenizing for NLP all lean on regex. A little regex replaces a lot of fiddly string code.

## Key concepts

- **Character classes** — `\d` digit, `\w` word char, `\s` whitespace; `[abc]` a set; `.` any char.
- **Quantifiers** — `*` 0+, `+` 1+, `?` 0/1, `{2,4}` a range. Add `?` for non-greedy.
- **Anchors** — `^` start, `$` end, `\b` word boundary.
- **Groups** — `( )` capture; `re.findall`/`group()` retrieve captured parts.
- **Key functions** — re.search, re.match, re.findall, re.sub, re.split, re.compile.
- **Raw strings** — Use `r"\d+"` so Python doesn't eat the backslashes.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import re

text = "Order 12345 shipped on 2026-06-09 for $42.50"

# search: find the FIRST match anywhere
m = re.search(r"\d+", text)
print(m.group())          # 12345

# findall: get ALL matches as a list
print(re.findall(r"\d+", text))   # ['12345', '2026', '06', '09', '42', '50']

# Capture groups: extract structured pieces (year, month, day)
date = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print(date.groups())      # ('2026', '06', '09')
print("year:", date.group(1))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Always write patterns as raw strings (`r"\d+"`) — otherwise Python interprets `\d` etc. first.
- ⚠️ `re.match` anchors at the START of the string; `re.search` looks anywhere. Mixing them up is common.
- ⚠️ `.` does NOT match a newline by default; add the `re.DOTALL` flag if you need it to.
- ⚠️ Quantifiers are greedy by default (`.*` grabs as much as possible); add `?` to make them lazy.
- ⚠️ `findall` returns the GROUPS if your pattern has capturing parentheses, not the whole match — watch out.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

