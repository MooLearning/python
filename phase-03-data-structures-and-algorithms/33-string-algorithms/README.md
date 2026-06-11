# 33 — String Algorithms

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**String algorithms** manipulate and analyze text: reversing, checking palindromes, detecting anagrams, counting character frequencies, and searching for patterns. Because Python strings are immutable, you often build results with lists or generators and `''.join(...)` at the end.

## Why it matters

Text problems are everywhere in interviews and real work (parsing, validation, search, NLP). Many showcase core techniques — two pointers, hashing/counting, and sliding windows — on an easy-to-visualize structure.

## Key concepts

- **Immutability** — Strings can't change in place; build with a list then ''.join().
- **Two pointers** — Compare/scan from both ends (palindromes) or with a fast/slow pointer.
- **Frequency counting** — collections.Counter or a dict to tally characters.
- **Anagram test** — Two strings are anagrams iff their character counts match.
- **Pattern search** — Naive O(n*m) scan; advanced: KMP/Rabin-Karp for O(n+m).
- **Normalization** — lower(), strip(), and filtering for case/space-insensitive checks.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def is_palindrome(s):
    # keep only letters/digits, ignore case
    cleaned = [c.lower() for c in s if c.isalnum()]
    i, j = 0, len(cleaned) - 1
    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1; j -= 1
    return True

print(is_palindrome("racecar"))               # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))                 # False
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Strings are immutable — repeatedly doing `s += c` in a loop is O(n^2); build a list and join.
- ⚠️ Case and whitespace break naive comparisons; normalize with lower()/strip() first.
- ⚠️ `Counter(a) == Counter(b)` is the cleanest anagram test — no need to sort.
- ⚠️ Slicing inside a loop (`text[i:i+m]`) copies substrings; fine for learning, costly at scale.
- ⚠️ Beware Unicode: `len` counts code points, and case-folding can be subtle for non-ASCII text.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

