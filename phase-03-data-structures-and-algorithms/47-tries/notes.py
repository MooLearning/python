# ======================================================================
# 47 — Tries  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A Trie class with insert, search, startsWith
# ----------------------------------------------------------------------
print("\n--- Example 1: A Trie class with insert, search, startsWith ---")
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

# ----------------------------------------------------------------------
# Example 2: Autocomplete: all words with a given prefix
# ----------------------------------------------------------------------
print("\n--- Example 2: Autocomplete: all words with a given prefix ---")
class TrieNode:
    def __init__(self):
        self.children = {}; self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True
    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:                 # walk to the prefix node
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._collect(node, prefix, results)   # DFS from there
        return results
    def _collect(self, node, path, out):
        if node.is_end:
            out.append(path)
        for ch, child in sorted(node.children.items()):
            self._collect(child, path + ch, out)

t = Trie()
for w in ["app", "apple", "apply", "apt", "banana"]:
    t.insert(w)
print(t.autocomplete("app"))   # ['app', 'apple', 'apply']
print(t.autocomplete("b"))     # ['banana']

# ----------------------------------------------------------------------
# Example 3: Counting words and longest common prefix
# ----------------------------------------------------------------------
print("\n--- Example 3: Counting words and longest common prefix ---")
class TrieNode:
    def __init__(self):
        self.children = {}; self.is_end = False

root = TrieNode()
def insert(word):
    node = root
    for ch in word:
        node = node.children.setdefault(ch, TrieNode())
    node.is_end = True

for w in ["flower", "flow", "flight"]:
    insert(w)

# Longest common prefix = walk while exactly one child and not a word-end
def longest_common_prefix():
    node, prefix = root, []
    while len(node.children) == 1 and not node.is_end:
        ch = next(iter(node.children))
        prefix.append(ch)
        node = node.children[ch]
    return "".join(prefix)

print("LCP:", longest_common_prefix())   # 'fl'

print("\nDone! Tip: change values above and run again to learn by experiment.")
