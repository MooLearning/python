# 47 — Tries: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Insert 'hi' into a trie and confirm search('hi') is True.

*Hint: Walk chars, set is_end.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self): self.children = {}; self.is_end = False
root = Node()
def insert(w):
    n = root
    for c in w: n = n.children.setdefault(c, Node())
    n.is_end = True
def search(w):
    n = root
    for c in w:
        if c not in n.children: return False
        n = n.children[c]
    return n.is_end
insert("hi"); print(search("hi"))  # True
```

</details>

## Exercise 2

After inserting 'cat', is search('ca') True or False? Why?

*Hint: is_end flag.*

<details>
<summary>✅ Solution</summary>

**False.** 'ca' is only a prefix; the `is_end` flag is set on the 'cat' node, not
the 'a' node. Use `starts_with('ca')` to test for the prefix instead.

</details>

## Exercise 3

Implement starts_with('ap') after inserting 'apple'.

*Hint: Walk, ignore is_end.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self): self.children = {}; self.is_end = False
root = Node()
def insert(w):
    n = root
    for c in w: n = n.children.setdefault(c, Node())
    n.is_end = True
def starts_with(p):
    n = root
    for c in p:
        if c not in n.children: return False
        n = n.children[c]
    return True
insert("apple"); print(starts_with("ap"))  # True
```

</details>

## Exercise 4

Count how many words are stored in a trie.

*Hint: DFS counting is_end nodes.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self): self.children = {}; self.is_end = False
root = Node()
def insert(w):
    n = root
    for c in w: n = n.children.setdefault(c, Node())
    n.is_end = True
def count(node):
    total = 1 if node.is_end else 0
    for ch in node.children.values(): total += count(ch)
    return total
for w in ["a", "ab", "abc"]: insert(w)
print(count(root))  # 3
```

</details>

## Exercise 5

List all words in a trie via DFS.

*Hint: Accumulate the path.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self): self.children = {}; self.is_end = False
root = Node()
def insert(w):
    n = root
    for c in w: n = n.children.setdefault(c, Node())
    n.is_end = True
def words(node, path, out):
    if node.is_end: out.append(path)
    for c, child in sorted(node.children.items()):
        words(child, path + c, out)
for w in ["to", "tea", "ted"]: insert(w)
out = []; words(root, "", out); print(out)  # ['tea','ted','to']
```

</details>

## Exercise 6

Find the longest word in a trie.

*Hint: Track max-length is_end path.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self): self.children = {}; self.is_end = False
root = Node()
def insert(w):
    n = root
    for c in w: n = n.children.setdefault(c, Node())
    n.is_end = True
def longest(node, path):
    best = path if node.is_end else ""
    for c, child in node.children.items():
        cand = longest(child, path + c)
        if len(cand) > len(best): best = cand
    return best
for w in ["a", "abc", "ab"]: insert(w)
print(longest(root, ""))  # abc
```

</details>

## Exercise 7

Check if any inserted word is a prefix of 'apple' (e.g. 'app').

*Hint: Stop at any is_end.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self): self.children = {}; self.is_end = False
root = Node()
def insert(w):
    n = root
    for c in w: n = n.children.setdefault(c, Node())
    n.is_end = True
def has_prefix_word(word):
    n = root
    for c in word:
        if c not in n.children: return False
        n = n.children[c]
        if n.is_end: return True
    return False
insert("app"); print(has_prefix_word("apple"))  # True
```

</details>

## Exercise 8

Build a trie and return the number of words sharing prefix 'ca'.

*Hint: Walk then DFS count.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self): self.children = {}; self.is_end = False
root = Node()
def insert(w):
    n = root
    for c in w: n = n.children.setdefault(c, Node())
    n.is_end = True
def count_from(node):
    total = 1 if node.is_end else 0
    for ch in node.children.values(): total += count_from(ch)
    return total
for w in ["cat", "car", "card", "dog"]: insert(w)
n = root
for c in "ca": n = n.children[c]
print(count_from(n))  # 3
```

</details>

