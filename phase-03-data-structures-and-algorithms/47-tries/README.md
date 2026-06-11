# 47 — Tries

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **trie** (prefix tree) stores strings by their characters: each node represents one character, and a path from the root spells a prefix. Words sharing a prefix share nodes. Insert and search are **O(L)** where L is the word length — independent of how many words are stored. A flag marks where complete words end.

## Why it matters

Tries make prefix queries fast: autocomplete, spell-check, dictionary lookups, IP routing, and 'does any word start with…?'. They beat hash sets when you need PREFIX matching, not just exact membership.

## Key concepts

- **Node** — Holds a map child-char → child-node and an 'is end of word' flag.
- **Insert O(L)** — Walk/create one node per character of the word.
- **Search O(L)** — Follow characters; require the end flag for a full word.
- **startsWith** — Same walk but no end-flag needed — that's the trie's superpower.
- **Shared prefixes** — 'car' and 'cart' reuse the 'c-a-r' path — saves space.
- **Alphabet** — Children keyed by a dict (flexible) or a fixed-size array (fast).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
class TrieNode:
    def __init__(self):
        self.children = {}       # char -> TrieNode
        self.is_end = False      # True if a word ends here

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word):       # exact word present?
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix): # any word with this prefix?
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

t = Trie()
for w in ["cat", "car", "card", "dog"]:
    t.insert(w)
print(t.search("car"))        # True
print(t.search("ca"))         # False (prefix, not a full word)
print(t.starts_with("ca"))    # True
print(t.starts_with("z"))     # False
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Forgetting the `is_end` flag makes 'car' match when only 'card' was inserted.
- ⚠️ Searching a prefix with `search()` (needs is_end) vs `starts_with()` are different questions.
- ⚠️ Tries can use lots of memory for sparse data — many nodes with single children.
- ⚠️ Use `setdefault`/`defaultdict` to create child nodes; manual `if ch not in` is error-prone.
- ⚠️ Deletion is fiddly — you must avoid removing nodes still shared by other words.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

