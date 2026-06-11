# -*- coding: utf-8 -*-
"""Phase 3 — Data Structures & Algorithms content (built in chunks)."""

CONTENT = {}

CONTENT["big-o-notation"] = {
    "what": (
        "**Big-O notation** describes how an algorithm's running time (or memory) grows as the "
        "input size `n` grows. It ignores constants and small terms to capture the *shape* of "
        "growth: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n), O(n^2) quadratic, "
        "O(2^n) exponential. You compare algorithms by their worst-case Big-O."
    ),
    "why": (
        "It's the universal language for 'will this scale?'. An O(n^2) solution that's fine for 100 "
        "items can freeze on 100,000. Every DSA topic and every coding interview leans on reasoning "
        "about Big-O."
    ),
    "concepts": [
        ("O(1)", "Constant — same work regardless of n (e.g. dict lookup, list index)."),
        ("O(log n)", "Halves the problem each step (binary search)."),
        ("O(n)", "Touches each item once (a single loop, linear search)."),
        ("O(n log n)", "Efficient sorts (merge sort, Timsort)."),
        ("O(n^2)", "Nested loops over the data (bubble sort, all pairs)."),
        ("Drop constants/lower terms", "O(2n + 5) is O(n); O(n^2 + n) is O(n^2)."),
    ],
    "examples": [
        ("Counting operations for different complexities", r'''
def constant(n):          # O(1): work doesn't depend on n
    return n * 2

def linear(arr):          # O(n): one pass
    ops = 0
    for _ in arr:
        ops += 1
    return ops

def quadratic(arr):       # O(n^2): nested loops -> all pairs
    ops = 0
    for _ in arr:
        for _ in arr:
            ops += 1
    return ops

for n in (10, 100, 1000):
    data = list(range(n))
    print(f"n={n:5} | linear ops={linear(data):6} | quadratic ops={quadratic(data)}")
'''),
        ("Timing: linear vs quadratic growth", r'''
import time

def time_it(fn, data):
    start = time.perf_counter()
    fn(data)
    return (time.perf_counter() - start) * 1000   # ms

def find_dupes_slow(arr):     # O(n^2)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def has_dupes_fast(arr):      # O(n) using a set
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

data = list(range(2000))      # no duplicates -> worst case
print(f"O(n^2): {time_it(find_dupes_slow, data):.1f} ms")
print(f"O(n)  : {time_it(has_dupes_fast, data):.3f} ms")
'''),
        ("Why we drop constants and lower-order terms", r'''
# Two algorithms doing 'n' vs '3n + 100' steps:
def a(n): return n
def b(n): return 3 * n + 100

for n in (10, 1000, 1_000_000):
    print(f"n={n:9} | a={a(n):10} | b={b(n):10} | ratio={b(n)/a(n):.3f}")
# As n grows huge, the ratio approaches the constant 3 and the +100 vanishes.
# So both are O(n): the GROWTH SHAPE is what matters, not the constants.
'''),
    ],
    "gotchas": [
        "Big-O is about GROWTH, not absolute speed: an O(n) with huge constants can lose to O(n^2) on small n.",
        "Worst case vs average case differ — quicksort is O(n log n) average but O(n^2) worst case.",
        "Nested loops aren't always O(n^2): if the inner loop runs a fixed number of times, it's O(n).",
        "Watch hidden costs: `x in a_list` is O(n), but `x in a_set` is O(1).",
        "Space complexity matters too — a recursive solution may be O(n) time but O(n) stack space.",
    ],
    "exercises": [
        ("State the Big-O of looking up a key in a dict of n items.", "Hash tables are constant time.",
         r'''#md
**O(1)** on average. Python dicts use hashing, so lookups don't depend on size.'''),
        ("What is the Big-O of this loop: for i in range(n): for j in range(n): ...?", "Nested over n.",
         r'''#md
**O(n^2)** — the inner loop runs n times for each of the n outer iterations.'''),
        ("Simplify O(5n + 3) and O(n^2 + 100n + 7) to Big-O.", "Drop constants and lower terms.",
         r'''#md
`O(5n + 3)` → **O(n)**.  `O(n^2 + 100n + 7)` → **O(n^2)** (the n^2 term dominates).'''),
        ("Write an O(n) function that returns the max of a list (no built-in max).", "One pass.",
         r'''def my_max(arr):
    best = arr[0]
    for x in arr:
        if x > best:
            best = x
    return best
print(my_max([3, 9, 1, 7]))  # 9'''),
        ("Is binary search O(log n) or O(n)? Why?", "It halves the search space.",
         r'''#md
**O(log n)** — each comparison discards half of the remaining elements, so it
takes about log2(n) steps.'''),
        ("Rewrite an O(n^2) 'contains duplicate' check as O(n).", "Use a set.",
         r'''def has_dup(arr):
    return len(set(arr)) != len(arr)
print(has_dup([1, 2, 2]))  # True'''),
        ("What is the time complexity of appending to a Python list (amortized)?", "Dynamic array.",
         r'''#md
**O(1) amortized.** Most appends are constant; occasional resizes are rare enough
to average out to O(1).'''),
        ("Order these from fastest- to slowest-growing: O(n^2), O(1), O(n log n), O(log n), O(n).", "",
         r'''#md
**O(1) < O(log n) < O(n) < O(n log n) < O(n^2)** (slowest-growing first).'''),
    ],
}

CONTENT["arrays"] = {
    "what": (
        "An **array** stores items in contiguous memory so any element is reachable by index in "
        "O(1). Python's built-in `list` is a **dynamic array**: it grows automatically and supports "
        "indexing, slicing, append/pop at the end (O(1) amortized), and insert/remove in the middle "
        "(O(n)). 2D arrays are lists of lists."
    ),
    "why": (
        "Arrays are the most fundamental data structure — the basis for strings, matrices, stacks, "
        "heaps, and almost every algorithm. Mastering indexing, slicing, and common patterns "
        "(prefix sums, two-pointer, rotation) unlocks the rest of DSA."
    ),
    "concepts": [
        ("Index access", "`a[i]` is O(1); the position is computed directly from memory."),
        ("Append/pop end", "O(1) amortized at the end; insert/remove elsewhere is O(n) (shifts)."),
        ("Slicing", "`a[i:j]` copies a sub-array — handy but O(k) in time and space."),
        ("2D arrays", "Lists of lists; build with comprehensions, not `[[0]*n]*m` (shared rows!)."),
        ("Prefix sums", "Precompute running totals to answer range-sum queries in O(1)."),
        ("In-place vs copy", "Operations like reverse() mutate; sorted()/[::-1] make copies."),
    ],
    "examples": [
        ("Core list operations and their costs", r'''
a = [10, 20, 30, 40]
print(a[0], a[-1])         # 10 40  -> O(1) index
a.append(50)               # O(1) amortized at the end
a.insert(1, 15)            # O(n): shifts everything right -> [10,15,20,30,40,50]
print(a)
a.pop()                    # O(1): remove last
a.pop(0)                   # O(n): remove first, shifts left
print(a)                   # [15, 20, 30, 40]
print(a[1:3])              # [20, 30] -> slice copy
print(20 in a)             # O(n) membership scan -> True
'''),
        ("Building 2D arrays correctly", r'''
rows, cols = 3, 4

# WRONG: every row is the SAME list object
bad = [[0] * cols] * rows
bad[0][0] = 9
print("bad  :", bad)       # the 9 appears in EVERY row!

# RIGHT: a comprehension makes independent rows
grid = [[0] * cols for _ in range(rows)]
grid[0][0] = 9
print("good :", grid)      # only row 0 changed

# Access and iterate
grid[1][2] = 5
for r in range(rows):
    print(grid[r])
'''),
        ("Prefix sums for fast range queries", r'''
nums = [3, 1, 4, 1, 5, 9, 2]

# Precompute prefix[i] = sum of nums[0:i]
prefix = [0] * (len(nums) + 1)
for i, x in enumerate(nums):
    prefix[i + 1] = prefix[i] + x

def range_sum(lo, hi):      # sum of nums[lo:hi+1] in O(1)
    return prefix[hi + 1] - prefix[lo]

print("prefix:", prefix)
print("sum[2..5] =", range_sum(2, 5))   # 4+1+5+9 = 19
print("sum[0..6] =", range_sum(0, 6))   # 25
'''),
    ],
    "gotchas": [
        "`[[0]*n]*m` creates m references to the SAME row — use `[[0]*n for _ in range(m)]`.",
        "`list.insert(0, x)` and `list.pop(0)` are O(n); use `collections.deque` for fast ends.",
        "`x in a_list` is O(n); if you do many membership checks, use a set.",
        "Slicing copies data — `a[:]` is a shallow copy, not a view (unlike NumPy).",
        "Modifying a list while iterating over it skips elements; iterate a copy or build a new list.",
    ],
    "exercises": [
        ("Reverse a list in place without using reverse() or [::-1].", "Two-pointer swap.",
         r'''def reverse(a):
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1; j -= 1
    return a
print(reverse([1, 2, 3, 4]))  # [4, 3, 2, 1]'''),
        ("Find the second-largest number in [3, 9, 1, 9, 7].", "Track top two, handle dupes.",
         r'''def second_largest(a):
    first = second = float("-inf")
    for x in a:
        if x > first:
            first, second = x, first
        elif first > x > second:
            second = x
    return second
print(second_largest([3, 9, 1, 9, 7]))  # 7'''),
        ("Rotate [1,2,3,4,5] right by 2 -> [4,5,1,2,3].", "Slice and concatenate.",
         r'''def rotate(a, k):
    k %= len(a)
    return a[-k:] + a[:-k]
print(rotate([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]'''),
        ("Build a 3x3 identity matrix as a list of lists.", "1 on the diagonal.",
         r'''n = 3
I = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
for row in I: print(row)'''),
        ("Move all zeros in [0,1,0,3,12] to the end, keeping order -> [1,3,12,0,0].", "Stable partition.",
         r'''def move_zeros(a):
    nonzero = [x for x in a if x != 0]
    return nonzero + [0] * (len(a) - len(nonzero))
print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]'''),
        ("Use a prefix-sum array to answer the sum of indices 1..3 of [2,4,6,8,10].", "prefix[hi+1]-prefix[lo].",
         r'''nums = [2, 4, 6, 8, 10]
pre = [0]
for x in nums: pre.append(pre[-1] + x)
print(pre[4] - pre[1])  # 4+6+8 = 18'''),
        ("Find the maximum sum of any contiguous subarray (Kadane's) of [-2,1,-3,4,-1,2,1,-5,4].",
         "Track running and best sums.",
         r'''def max_subarray(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6'''),
        ("Merge two sorted arrays [1,3,5] and [2,4,6] into one sorted array.", "Two pointers.",
         r'''def merge(a, b):
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 3, 5], [2, 4, 6]))  # [1,2,3,4,5,6]'''),
    ],
}

CONTENT["string-algorithms"] = {
    "what": (
        "**String algorithms** manipulate and analyze text: reversing, checking palindromes, "
        "detecting anagrams, counting character frequencies, and searching for patterns. Because "
        "Python strings are immutable, you often build results with lists or generators and "
        "`''.join(...)` at the end."
    ),
    "why": (
        "Text problems are everywhere in interviews and real work (parsing, validation, search, "
        "NLP). Many showcase core techniques — two pointers, hashing/counting, and sliding "
        "windows — on an easy-to-visualize structure."
    ),
    "concepts": [
        ("Immutability", "Strings can't change in place; build with a list then ''.join()."),
        ("Two pointers", "Compare/scan from both ends (palindromes) or with a fast/slow pointer."),
        ("Frequency counting", "collections.Counter or a dict to tally characters."),
        ("Anagram test", "Two strings are anagrams iff their character counts match."),
        ("Pattern search", "Naive O(n*m) scan; advanced: KMP/Rabin-Karp for O(n+m)."),
        ("Normalization", "lower(), strip(), and filtering for case/space-insensitive checks."),
    ],
    "examples": [
        ("Palindrome check with two pointers", r'''
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
'''),
        ("Anagrams and character frequency", r'''
from collections import Counter

def are_anagrams(a, b):
    return Counter(a.replace(" ", "").lower()) == Counter(b.replace(" ", "").lower())

print(are_anagrams("listen", "silent"))       # True
print(are_anagrams("hello", "world"))         # False

# First non-repeating character
def first_unique(s):
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None

print(first_unique("aabbcde"))                # c
'''),
        ("Naive pattern search and word reversal", r'''
def find_all(text, pattern):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions

print(find_all("abracadabra", "abra"))        # [0, 7]

# Reverse the order of words (not the characters)
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words("the quick brown fox"))   # fox brown quick the
'''),
    ],
    "gotchas": [
        "Strings are immutable — repeatedly doing `s += c` in a loop is O(n^2); build a list and join.",
        "Case and whitespace break naive comparisons; normalize with lower()/strip() first.",
        "`Counter(a) == Counter(b)` is the cleanest anagram test — no need to sort.",
        "Slicing inside a loop (`text[i:i+m]`) copies substrings; fine for learning, costly at scale.",
        "Beware Unicode: `len` counts code points, and case-folding can be subtle for non-ASCII text.",
    ],
    "exercises": [
        ("Reverse the string 'algorithms' without slicing.", "Build from the end.",
         r'''def rev(s):
    out = []
    for c in s:
        out.insert(0, c)
    return "".join(out)
print(rev("algorithms"))  # smhtirogla'''),
        ("Count vowels in 'Encyclopedia'.", "Membership in 'aeiou'.",
         r'''s = "Encyclopedia"
print(sum(1 for c in s.lower() if c in "aeiou"))  # 5'''),
        ("Check if 'Dormitory' and 'Dirty Room' are anagrams (ignore case/space).", "Counter.",
         r'''from collections import Counter
def anag(a, b):
    norm = lambda x: Counter(x.replace(" ", "").lower())
    return norm(a) == norm(b)
print(anag("Dormitory", "Dirty Room"))  # True'''),
        ("Return the most frequent character in 'mississippi'.", "Counter.most_common.",
         r'''from collections import Counter
print(Counter("mississippi").most_common(1)[0][0])  # i or s -> 's'? -> 'i'''),
        ("Find all starting indices of 'ana' in 'banana'.", "Naive scan.",
         r'''def find(t, p):
    return [i for i in range(len(t) - len(p) + 1) if t[i:i+len(p)] == p]
print(find("banana", "ana"))  # [1, 3]'''),
        ("Compress 'aaabbc' to 'a3b2c1' (run-length encoding).", "Count consecutive runs.",
         r'''def rle(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(f"{s[i]}{j - i}")
        i = j
    return "".join(out)
print(rle("aaabbc"))  # a3b2c1'''),
        ("Check if 'abc' is a subsequence of 'aXbYcZ'.", "Two pointers.",
         r'''def is_subseq(sub, s):
    it = iter(s)
    return all(c in it for c in sub)
print(is_subseq("abc", "aXbYcZ"))  # True'''),
        ("Find the longest substring without repeating characters in 'abcabcbb'.", "Sliding window.",
         r'''def longest_unique(s):
    seen = {}; start = best = 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        best = max(best, i - start + 1)
    return best
print(longest_unique("abcabcbb"))  # 3'''),
    ],
}

CONTENT["linked-lists"] = {
    "what": (
        "A **linked list** stores items in **nodes**, each holding a value and a reference to the "
        "next node. Unlike arrays, the items aren't contiguous — to reach the 5th item you follow 5 "
        "links (O(n)). The payoff: inserting/removing at a known position is O(1) (just rewire "
        "pointers). Variants: **singly** (next only), **doubly** (prev+next), **circular**."
    ),
    "why": (
        "Linked lists teach pointer/reference thinking that underlies trees, graphs, and many "
        "structures. They're ideal when you insert/delete a lot and rarely random-access, and they "
        "appear constantly in interviews (reverse a list, detect a cycle, merge two lists)."
    ),
    "concepts": [
        ("Node", "An object with `.value` and `.next` (and `.prev` for doubly)."),
        ("Head", "Reference to the first node; `None` means empty."),
        ("Traversal", "Walk node.next until None — O(n)."),
        ("Insert/delete", "O(1) once you have the node, but O(n) to FIND the spot."),
        ("No random access", "`list[i]` doesn't exist — you must traverse."),
        ("Cycle detection", "Floyd's fast/slow pointers find loops in O(1) space."),
    ],
    "examples": [
        ("A singly linked list class", r'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):           # add to the end -> O(n)
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):                 # for easy printing
        out, cur = [], self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

ll = LinkedList()
for x in [1, 2, 3]:
    ll.append(x)
print(ll.to_list())     # [1, 2, 3]
'''),
        ("Prepend, search, and delete by value", r'''
class Node:
    def __init__(self, v): self.value = v; self.next = None

class LinkedList:
    def __init__(self): self.head = None
    def prepend(self, v):              # add to front -> O(1)
        node = Node(v); node.next = self.head; self.head = node
    def find(self, v):                 # O(n) search
        cur = self.head
        while cur:
            if cur.value == v: return True
            cur = cur.next
        return False
    def delete(self, v):               # remove first node with value v
        if self.head and self.head.value == v:
            self.head = self.head.next; return
        cur = self.head
        while cur and cur.next:
            if cur.next.value == v:
                cur.next = cur.next.next; return
            cur = cur.next
    def to_list(self):
        out, cur = [], self.head
        while cur: out.append(cur.value); cur = cur.next
        return out

ll = LinkedList()
for x in [3, 2, 1]: ll.prepend(x)
print(ll.to_list())     # [1, 2, 3]
print(ll.find(2))       # True
ll.delete(2)
print(ll.to_list())     # [1, 3]
'''),
        ("Reverse a linked list and detect a cycle", r'''
class Node:
    def __init__(self, v): self.value = v; self.next = None

def build(values):
    head = None
    for v in reversed(values):
        n = Node(v); n.next = head; head = n
    return head

def reverse(head):
    prev = None
    while head:
        nxt = head.next     # save next
        head.next = prev    # flip the pointer
        prev = head         # advance prev
        head = nxt          # advance head
    return prev

def to_list(head):
    out = []
    while head: out.append(head.value); head = head.next
    return out

h = build([1, 2, 3, 4])
print(to_list(reverse(h)))   # [4, 3, 2, 1]

def has_cycle(head):         # Floyd's tortoise and hare
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

a = Node(1); b = Node(2); c = Node(3)
a.next = b; b.next = c; c.next = b   # cycle!
print(has_cycle(a))          # True
'''),
    ],
    "gotchas": [
        "Losing the `next` pointer before reattaching loses the rest of the list — save it first when reversing.",
        "Forgetting the empty-list (`head is None`) and single-node edge cases causes crashes.",
        "Deleting the head needs special handling (move head forward) vs deleting a middle node.",
        "No O(1) indexing: reaching position k is O(k); don't treat it like an array.",
        "Accidental cycles make traversal loop forever — be careful when rewiring pointers.",
    ],
    "exercises": [
        ("Build a Node class and link three nodes 1->2->3, then print all values.", "node.next chaining.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
a = Node(1); a.next = Node(2); a.next.next = Node(3)
cur = a
while cur: print(cur.value, end=" "); cur = cur.next
print()'''),
        ("Count the number of nodes in a linked list.", "Traverse and tally.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
def length(head):
    n = 0
    while head: n += 1; head = head.next
    return n
a = Node(1); a.next = Node(2)
print(length(a))  # 2'''),
        ("Find the maximum value in a linked list.", "Traverse tracking max.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
def max_val(head):
    best = head.value
    while head:
        best = max(best, head.value); head = head.next
    return best
a = Node(3); a.next = Node(9); a.next.next = Node(1)
print(max_val(a))  # 9'''),
        ("Reverse a linked list iteratively.", "Three pointers.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
a = Node(1); a.next = Node(2); a.next.next = Node(3)
r = reverse(a)
while r: print(r.value, end=" "); r = r.next
print()  # 3 2 1'''),
        ("Find the middle node using fast/slow pointers (return its value).", "Hare moves twice as fast.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
    return slow.value
h = Node(1); h.next = Node(2); h.next.next = Node(3)
print(middle(h))  # 2'''),
        ("Detect whether a linked list has a cycle.", "Floyd's algorithm.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: return True
    return False
a = Node(1); b = Node(2); a.next = b; b.next = a
print(has_cycle(a))  # True'''),
        ("Get the nth value from the end (n=1 is last).", "Two pointers k apart.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
def nth_from_end(head, n):
    lead = head
    for _ in range(n): lead = lead.next
    while lead:
        lead = lead.next; head = head.next
    return head.value
h = Node(1); h.next = Node(2); h.next.next = Node(3)
print(nth_from_end(h, 1))  # 3'''),
        ("Merge two sorted linked lists into one sorted list (return values).", "Compare heads.",
         r'''class Node:
    def __init__(self, v): self.value = v; self.next = None
def build(vals):
    head = None
    for v in reversed(vals):
        n = Node(v); n.next = head; head = n
    return head
def merge(a, b):
    dummy = tail = Node(0)
    while a and b:
        if a.value <= b.value: tail.next, a = a, a.next
        else: tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    out = []
    cur = dummy.next
    while cur: out.append(cur.value); cur = cur.next
    return out
print(merge(build([1, 3, 5]), build([2, 4])))  # [1,2,3,4,5]'''),
    ],
}

CONTENT["stacks"] = {
    "what": (
        "A **stack** is a **LIFO** (Last-In, First-Out) collection: you add (`push`) and remove "
        "(`pop`) from the same end, the **top**. Think of a stack of plates — you take the last one "
        "you put down. In Python a plain `list` is a perfect stack: `append` to push and `pop()` to "
        "pop, both O(1)."
    ),
    "why": (
        "Stacks model 'undo', function call frames, expression evaluation, balanced-bracket checks, "
        "and depth-first traversal. Recognizing 'I need the most recent unfinished thing' is a core "
        "interview pattern."
    ),
    "concepts": [
        ("push", "Add to the top — `stack.append(x)` (O(1))."),
        ("pop", "Remove and return the top — `stack.pop()` (O(1))."),
        ("peek/top", "Look at the top without removing — `stack[-1]`."),
        ("LIFO order", "Last item pushed is the first popped."),
        ("Underflow", "Popping an empty stack errors — check `if stack` first."),
        ("Uses", "Bracket matching, undo, DFS, call stack, expression parsing."),
    ],
    "examples": [
        ("A Stack class wrapping a list", r'''
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)       # O(1)
    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()    # O(1) from the end
    def peek(self):
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0
    def __len__(self):
        return len(self._items)

s = Stack()
for x in [1, 2, 3]:
    s.push(x)
print("top:", s.peek())     # 3
print("pop:", s.pop())      # 3
print("pop:", s.pop())      # 2
print("size:", len(s))      # 1
'''),
        ("Balanced brackets checker (classic stack use)", r'''
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)            # opening -> push
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False            # mismatch or nothing to match
    return not stack                    # leftover opens -> unbalanced

for expr in ["(a[b]{c})", "([)]", "(((", "{[()]}"]:
    print(f"{expr:10} -> {is_balanced(expr)}")
'''),
        ("Evaluate Reverse Polish Notation with a stack", r'''
def eval_rpn(tokens):
    stack = []
    ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
           "*": lambda a, b: a * b, "/": lambda a, b: int(a / b)}
    for tok in tokens:
        if tok in ops:
            b = stack.pop(); a = stack.pop()    # order matters!
            stack.append(ops[tok](a, b))
        else:
            stack.append(int(tok))
    return stack.pop()

# (2 + 1) * 3  ->  "2 1 + 3 *"
print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 4 + (13//5) = 6
'''),
    ],
    "gotchas": [
        "Popping an empty stack raises IndexError — guard with `if stack:` or catch it.",
        "`list.pop(0)` is O(n)! A stack pops from the END with `pop()` (no argument).",
        "Order matters in binary ops: pop the right operand first, then the left.",
        "Don't use a stack when you need FIFO order — that's a queue.",
        "`peek` on an empty list (`stack[-1]`) also errors — check emptiness first.",
    ],
    "exercises": [
        ("Implement push, pop, and peek using a list.", "append/pop/[-1].",
         r'''st = []
st.append(1); st.append(2)
print(st[-1])      # peek -> 2
print(st.pop())    # 2
print(st)          # [1]'''),
        ("Reverse the string 'stack' using a stack.", "Push all, then pop all.",
         r'''def reverse(s):
    st = list(s)
    out = []
    while st:
        out.append(st.pop())
    return "".join(out)
print(reverse("stack"))  # kcats'''),
        ("Check if '(()())' has balanced parentheses.", "Push '(' , pop on ')'.",
         r'''def balanced(s):
    n = 0
    for c in s:
        if c == "(": n += 1
        elif c == ")":
            n -= 1
            if n < 0: return False
    return n == 0
print(balanced("(()())"))  # True'''),
        ("Use a stack to decide if 'abba' reads the same backward.", "Compare with popped half.",
         r'''def is_pal(s):
    st = list(s)
    for c in s:
        if c != st.pop(): return False
    return True
print(is_pal("abba"))  # True'''),
        ("Evaluate the RPN expression '5 1 2 + 4 * + 3 -'.", "Stack of operands.",
         r'''def rpn(tokens):
    st = []
    for t in tokens.split():
        if t in "+-*/":
            b, a = st.pop(), st.pop()
            st.append({"+":a+b,"-":a-b,"*":a*b,"/":a//b}[t])
        else:
            st.append(int(t))
    return st.pop()
print(rpn("5 1 2 + 4 * + 3 -"))  # 14'''),
        ("Find the next greater element for each item in [2,1,2,4,3].", "Monotonic stack.",
         r'''def next_greater(a):
    res = [-1] * len(a)
    st = []                      # holds indices, values decreasing
    for i, x in enumerate(a):
        while st and a[st[-1]] < x:
            res[st.pop()] = x
        st.append(i)
    return res
print(next_greater([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]'''),
        ("Implement a stack with a max() operation in O(1).", "Track maxes alongside.",
         r'''class MaxStack:
    def __init__(self):
        self.data = []; self.maxes = []
    def push(self, x):
        self.data.append(x)
        self.maxes.append(x if not self.maxes else max(x, self.maxes[-1]))
    def pop(self):
        self.maxes.pop(); return self.data.pop()
    def get_max(self):
        return self.maxes[-1]
s = MaxStack()
for x in [3, 1, 5, 2]: s.push(x)
print(s.get_max())  # 5'''),
        ("Decode '3[ab]2[c]' -> 'abababcc' using a stack.", "Push counts and partial strings.",
         r'''def decode(s):
    num = 0; cur = ""; stack = []
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num)); cur = ""; num = 0
        elif ch == "]":
            prev, k = stack.pop(); cur = prev + cur * k
        else:
            cur += ch
    return cur
print(decode("3[ab]2[c]"))  # abababcc'''),
    ],
}

CONTENT["queues"] = {
    "what": (
        "A **queue** is a **FIFO** (First-In, First-Out) collection: you add at the **rear** "
        "(`enqueue`) and remove from the **front** (`dequeue`) — like a line at a checkout. Use "
        "`collections.deque`, which supports O(1) `append` and `popleft`. A plain list's `pop(0)` is "
        "O(n), so avoid it. Variants: **circular queue**, **priority queue** (heap), **deque** "
        "(double-ended)."
    ),
    "why": (
        "Queues model fair, in-order processing: task schedulers, print spoolers, breadth-first "
        "search, and producer/consumer pipelines. BFS — one of the most important graph algorithms "
        "— is just a queue."
    ),
    "concepts": [
        ("enqueue", "Add to the rear — `deque.append(x)` (O(1))."),
        ("dequeue", "Remove from the front — `deque.popleft()` (O(1))."),
        ("FIFO order", "First item added is the first removed."),
        ("deque", "Double-ended queue: O(1) at BOTH ends; the right tool in Python."),
        ("Why not list.pop(0)", "Removing the front of a list shifts everything — O(n)."),
        ("Priority queue", "Removes the smallest/largest first — use `heapq`, not plain FIFO."),
    ],
    "examples": [
        ("A queue with collections.deque", r'''
from collections import deque

q = deque()
q.append("a")          # enqueue at rear
q.append("b")
q.append("c")
print("front:", q[0])  # a
print("dequeue:", q.popleft())   # a  (O(1))
print("dequeue:", q.popleft())   # b
print("remaining:", list(q))     # ['c']
print("size:", len(q))           # 1
'''),
        ("A Queue class and why deque beats list", r'''
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, x):
        self._items.append(x)        # O(1)
    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft() # O(1) from the front
    def peek(self):
        return self._items[0]
    def __len__(self):
        return len(self._items)

q = Queue()
for task in ["build", "test", "deploy"]:
    q.enqueue(task)
while len(q):
    print("processing:", q.dequeue())   # build, test, deploy (in order)
'''),
        ("BFS level-order on a tree uses a queue", r'''
from collections import deque

# tree as dict: node -> list of children
tree = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}

def bfs(root):
    order = []
    q = deque([root])
    while q:
        node = q.popleft()       # FIFO -> visit level by level
        order.append(node)
        for child in tree[node]:
            q.append(child)
    return order

print(bfs(1))   # [1, 2, 3, 4, 5, 6]
'''),
    ],
    "gotchas": [
        "Don't use `list.pop(0)` for a queue — it's O(n). Use `collections.deque.popleft()`.",
        "`deque[i]` indexing in the middle is O(n); deques are optimized for the ends.",
        "A queue is FIFO; a stack is LIFO — picking the wrong one reverses your order.",
        "`popleft()`/`pop()` on an empty deque raises IndexError — check `if q:` first.",
        "A priority queue is NOT a plain FIFO — use `heapq` when order depends on priority.",
    ],
    "exercises": [
        ("Create a queue with deque, enqueue 1,2,3, then dequeue once.", "append + popleft.",
         r'''from collections import deque
q = deque([1, 2, 3])
print(q.popleft())  # 1
print(list(q))      # [2, 3]'''),
        ("Why is list.pop(0) a bad queue? State the complexity.", "Front removal shifts.",
         r'''#md
`list.pop(0)` is **O(n)** because every remaining element shifts left one slot.
`deque.popleft()` is **O(1)**.'''),
        ("Use a deque as a double-ended queue: add to both ends.", "appendleft/append.",
         r'''from collections import deque
d = deque([1])
d.appendleft(0)   # front
d.append(2)       # rear
print(list(d))    # [0, 1, 2]'''),
        ("Reverse the first k=2 elements of a queue [1,2,3,4].", "Stack + queue.",
         r'''from collections import deque
def reverse_first_k(q, k):
    stack = [q.popleft() for _ in range(k)]
    for _ in range(k): q.appendleft(stack[_])  # noqa
    return q
q = deque([1, 2, 3, 4])
print(list(reverse_first_k(q, 2)))  # [2, 1, 3, 4]'''),
        ("Implement a queue using two stacks.", "Amortized O(1) dequeue.",
         r'''class QueueTwoStacks:
    def __init__(self):
        self.inb = []; self.out = []
    def enqueue(self, x):
        self.inb.append(x)
    def dequeue(self):
        if not self.out:
            while self.inb:
                self.out.append(self.inb.pop())
        return self.out.pop()
q = QueueTwoStacks()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
print(q.dequeue(), q.dequeue())  # 1 2'''),
        ("Generate binary numbers 1..5 as strings using a queue.", "BFS-style generation.",
         r'''from collections import deque
def binaries(n):
    out, q = [], deque(["1"])
    for _ in range(n):
        cur = q.popleft()
        out.append(cur)
        q.append(cur + "0"); q.append(cur + "1")
    return out
print(binaries(5))  # ['1','10','11','100','101']'''),
        ("Find the first non-repeating char in a stream 'aabc' at each step.", "Queue of candidates.",
         r'''from collections import deque, Counter
def stream_first_unique(s):
    counts = Counter(); q = deque(); res = []
    for ch in s:
        counts[ch] += 1; q.append(ch)
        while q and counts[q[0]] > 1:
            q.popleft()
        res.append(q[0] if q else "#")
    return res
print(stream_first_unique("aabc"))  # ['a','#','b','b']'''),
        ("Simulate a circular queue of capacity 3: enqueue 1,2,3,4 (4 should fail).", "Track size vs capacity.",
         r'''from collections import deque
class CircularQueue:
    def __init__(self, cap):
        self.q = deque(); self.cap = cap
    def enqueue(self, x):
        if len(self.q) >= self.cap: return False
        self.q.append(x); return True
cq = CircularQueue(3)
print([cq.enqueue(x) for x in [1, 2, 3, 4]])  # [True, True, True, False]'''),
    ],
}

CONTENT["hashing-and-hash-tables"] = {
    "what": (
        "A **hash table** stores key→value pairs and finds any key in **O(1) average** time. A "
        "**hash function** turns a key into an array index; collisions (two keys, same index) are "
        "resolved by **chaining** (a list per bucket) or **open addressing** (probe for a free slot). "
        "Python's `dict` and `set` are highly optimized hash tables."
    ),
    "why": (
        "Hashing turns slow O(n) searches into O(1) lookups — the single biggest speedup tool in "
        "everyday coding. Counting, de-duplication, caching, and 'have I seen this?' problems all "
        "lean on it."
    ),
    "concepts": [
        ("Hash function", "Maps a key to a bucket index; good ones spread keys evenly."),
        ("Bucket", "A slot in the underlying array where entries live."),
        ("Collision", "Two keys hashing to the same bucket — must be handled."),
        ("Chaining", "Each bucket holds a list of entries that collided."),
        ("Load factor", "entries / buckets; when high, the table resizes (rehash)."),
        ("Hashable keys", "Keys must be immutable (str, int, tuple) — lists can't be keys."),
    ],
    "examples": [
        ("dict and set as hash tables", r'''
# dict: O(1) average insert, lookup, delete
phone = {"alice": 123, "bob": 456}
phone["carol"] = 789
print(phone["bob"])          # 456  -> O(1)
print("alice" in phone)      # True -> O(1) key check
print(phone.get("dave", -1)) # -1   -> default if missing

# set: membership in O(1) (vs O(n) for a list)
seen = set()
for x in [1, 2, 2, 3, 1]:
    if x in seen:
        print("duplicate:", x)
    seen.add(x)
print("unique:", seen)       # {1, 2, 3}
'''),
        ("Build a hash table from scratch (chaining)", r'''
class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]   # each bucket is a list

    def _index(self, key):
        return hash(key) % self.size               # hash -> bucket index

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:                           # update existing
                bucket[i] = (key, value)
                return
        bucket.append((key, value))                # insert new

    def get(self, key, default=None):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return default

ht = HashTable()
ht.put("apple", 3)
ht.put("banana", 5)
ht.put("apple", 9)            # updates
print(ht.get("apple"))       # 9
print(ht.get("banana"))      # 5
print(ht.get("cherry", 0))   # 0
'''),
        ("Counting and grouping with hashing", r'''
from collections import Counter, defaultdict

words = "the cat sat on the mat the cat".split()

# Count frequencies in O(n)
print(Counter(words))        # {'the': 3, 'cat': 2, ...}

# Group words by their length using a dict of lists
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))          # {3: ['the','cat','sat',...]}

# Two-sum: find indices that add to target — O(n) with a hash map
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return (seen[target - n], i)
        seen[n] = i
    return None
print(two_sum([2, 7, 11, 15], 9))   # (0, 1)
'''),
    ],
    "gotchas": [
        "Only immutable (hashable) values can be keys — `{[1,2]: 'x'}` raises TypeError.",
        "Hash order is not sorted; dict preserves INSERTION order, not key order.",
        "A bad hash function clusters keys into few buckets, degrading to O(n).",
        "Mutating an object after using it as a key corrupts lookups — keep keys immutable.",
        "`d[missing]` raises KeyError; use `d.get(k, default)` or `defaultdict` to avoid it.",
    ],
    "exercises": [
        ("Count how many times each char appears in 'banana' using a dict.", "get with default.",
         r'''counts = {}
for c in "banana":
    counts[c] = counts.get(c, 0) + 1
print(counts)  # {'b':1,'a':3,'n':2}'''),
        ("Use a set to remove duplicates from [1,2,2,3,3,3].", "set() then list.",
         r'''print(sorted(set([1, 2, 2, 3, 3, 3])))  # [1, 2, 3]'''),
        ("Check if two strings are anagrams using a frequency dict.", "Compare counts.",
         r'''from collections import Counter
print(Counter("listen") == Counter("silent"))  # True'''),
        ("Find the first repeated element in [3,1,4,1,5].", "Track seen in a set.",
         r'''def first_repeat(a):
    seen = set()
    for x in a:
        if x in seen: return x
        seen.add(x)
    return None
print(first_repeat([3, 1, 4, 1, 5]))  # 1'''),
        ("Implement two-sum: return indices summing to 6 in [1,4,5,2].", "Complement in a map.",
         r'''def two_sum(a, t):
    seen = {}
    for i, x in enumerate(a):
        if t - x in seen: return (seen[t - x], i)
        seen[x] = i
print(two_sum([1, 4, 5, 2], 6))  # (1, 4)? -> (1, 2)'''),
        ("Group ['eat','tea','tan','ate'] into anagram groups.", "Sorted word as key.",
         r'''from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())
print(group_anagrams(["eat", "tea", "tan", "ate"]))
# [['eat','tea','ate'], ['tan']]'''),
        ("Find the element appearing more than n/2 times in [2,2,1,2,3].", "Count then check.",
         r'''from collections import Counter
def majority(a):
    c = Counter(a)
    for k, v in c.items():
        if v > len(a) // 2: return k
print(majority([2, 2, 1, 2, 3]))  # 2'''),
        ("Build a tiny LRU-ish cache: keep only the last 2 distinct keys inserted.", "dict order.",
         r'''def make_cache(limit=2):
    store = {}
    def put(k, v):
        if k in store: del store[k]
        store[k] = v
        while len(store) > limit:
            oldest = next(iter(store))
            del store[oldest]
    return store, put
store, put = make_cache()
for k, v in [("a",1),("b",2),("c",3)]: put(k, v)
print(list(store))  # ['b', 'c']'''),
    ],
}

CONTENT["linear-and-binary-search"] = {
    "what": (
        "**Searching** finds where (or whether) a value exists in a collection. **Linear search** "
        "scans every element — O(n) — and works on any list. **Binary search** repeatedly halves a "
        "**sorted** list by comparing with the middle — O(log n) — turning a million-item search "
        "into ~20 steps. Python's `bisect` module gives binary search out of the box."
    ),
    "why": (
        "Binary search is the canonical O(log n) algorithm and the gateway to 'search the answer "
        "space' techniques used across DSA. Knowing when data is sorted (so you can binary-search) "
        "is a major efficiency win."
    ),
    "concepts": [
        ("Linear search", "Check each element in turn — O(n), no ordering needed."),
        ("Binary search", "Halve a SORTED range each step — O(log n)."),
        ("lo/mid/hi", "Track the search window; `mid = (lo + hi) // 2`."),
        ("Sorted precondition", "Binary search is wrong on unsorted data."),
        ("bisect module", "`bisect_left`/`insort` for fast search & ordered insert."),
        ("Search the answer", "Binary-search over a value range, not just an array."),
    ],
    "examples": [
        ("Linear vs binary search", r'''
def linear_search(arr, target):       # O(n)
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

def binary_search(arr, target):       # O(log n) — arr MUST be sorted
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1              # search right half
        else:
            hi = mid - 1              # search left half
    return -1

data = [1, 3, 5, 7, 9, 11, 13]
print(linear_search(data, 9))   # 4
print(binary_search(data, 9))   # 4
print(binary_search(data, 8))   # -1 (not found)
'''),
        ("Recursive binary search and step count", r'''
def binary_search_rec(arr, target, lo=0, hi=None, steps=0):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1, steps
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid, steps + 1
    if arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, hi, steps + 1)
    return binary_search_rec(arr, target, lo, mid - 1, steps + 1)

big = list(range(0, 1_000_000, 2))   # 500k sorted evens
idx, steps = binary_search_rec(big, 999_998)
print(f"found at index {idx} in just {steps} steps")  # ~19 steps
'''),
        ("Using the bisect module", r'''
import bisect

scores = [10, 20, 30, 40, 50]

# Where would 35 be inserted to keep order?
print(bisect.bisect_left(scores, 35))   # 3

# Insert while keeping the list sorted
bisect.insort(scores, 35)
print(scores)                           # [10, 20, 30, 35, 40, 50]

# Membership test in O(log n)
def contains(sorted_list, x):
    i = bisect.bisect_left(sorted_list, x)
    return i < len(sorted_list) and sorted_list[i] == x

print(contains(scores, 35))             # True
print(contains(scores, 36))             # False
'''),
    ],
    "gotchas": [
        "Binary search REQUIRES a sorted list — on unsorted data it returns wrong answers.",
        "`mid = (lo + hi) // 2` then move to `mid + 1` / `mid - 1`, or you can loop forever.",
        "Sorting first costs O(n log n); for a single search, linear O(n) may be cheaper.",
        "Off-by-one bugs are common — decide `<=` vs `<` for the `while` condition and stick to it.",
        "`list.index(x)` is linear O(n); for sorted data use `bisect` for O(log n).",
    ],
    "exercises": [
        ("Write a linear search returning the index of 7 in [4,7,1,7].", "First match.",
         r'''def find(a, t):
    for i, x in enumerate(a):
        if x == t: return i
    return -1
print(find([4, 7, 1, 7], 7))  # 1'''),
        ("Binary-search for 23 in [2,5,8,12,16,23,38].", "lo/mid/hi loop.",
         r'''def bsearch(a, t):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == t: return mid
        if a[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return -1
print(bsearch([2, 5, 8, 12, 16, 23, 38], 23))  # 5'''),
        ("Count steps binary search takes to find 1 in range(0,1000).", "Increment a counter.",
         r'''def steps_to_find(a, t):
    lo, hi, steps = 0, len(a) - 1, 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if a[mid] == t: return steps
        if a[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return steps
print(steps_to_find(list(range(1000)), 1))  # ~9'''),
        ("Find the first index where you could insert 6 into [1,3,5,7].", "bisect_left.",
         r'''import bisect
print(bisect.bisect_left([1, 3, 5, 7], 6))  # 3'''),
        ("Find the leftmost position of a duplicate value 2 in [1,2,2,2,3].", "bisect_left.",
         r'''import bisect
print(bisect.bisect_left([1, 2, 2, 2, 3], 2))  # 1'''),
        ("Find the square root of 36 using binary search (integer).", "Search 0..n.",
         r'''def isqrt(n):
    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid == n: return mid
        if mid * mid < n: lo = mid + 1
        else: hi = mid - 1
    return hi
print(isqrt(36))  # 6'''),
        ("Find the peak index in [1,3,7,4,2] (an element bigger than neighbors).", "Binary search on slope.",
         r'''def peak(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < a[mid + 1]: lo = mid + 1
        else: hi = mid
    return lo
print(peak([1, 3, 7, 4, 2]))  # 2'''),
        ("Search a rotated sorted array [4,5,6,7,0,1,2] for 0.", "Decide which half is sorted.",
         r'''def search_rotated(a, t):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == t: return mid
        if a[lo] <= a[mid]:                # left half sorted
            if a[lo] <= t < a[mid]: hi = mid - 1
            else: lo = mid + 1
        else:                              # right half sorted
            if a[mid] < t <= a[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4'''),
    ],
}

CONTENT["basic-sorts"] = {
    "what": (
        "The three **basic sorts** are simple O(n^2) algorithms great for learning: **bubble sort** "
        "repeatedly swaps adjacent out-of-order pairs; **selection sort** repeatedly finds the "
        "smallest remaining item and places it; **insertion sort** grows a sorted prefix by "
        "inserting each new item into place. Insertion sort is genuinely fast on small or "
        "nearly-sorted data."
    ),
    "why": (
        "They build core intuition about comparisons, swaps, in-place work, and stability — the "
        "vocabulary you'll reuse for the fast O(n log n) sorts. Insertion sort also powers the "
        "small-array base case inside real-world hybrid sorts like Timsort."
    ),
    "concepts": [
        ("Bubble sort", "Swap adjacent pairs; biggest 'bubbles' to the end each pass."),
        ("Selection sort", "Select the min of the unsorted part; swap it to the front."),
        ("Insertion sort", "Insert each element into the growing sorted prefix."),
        ("In-place", "All three sort the list without extra arrays — O(1) space."),
        ("Stability", "Bubble & insertion are stable; selection sort is not."),
        ("Best case", "Insertion sort is O(n) on already-sorted input (early exit)."),
    ],
    "examples": [
        ("Bubble sort with early-exit optimization", r'''
def bubble_sort(arr):
    a = arr[:]                       # copy so we don't mutate the input
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):   # last i items already in place
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:              # no swaps -> already sorted
            break
    return a

print(bubble_sort([5, 2, 9, 1, 5, 6]))   # [1, 2, 5, 5, 6, 9]
print(bubble_sort([1, 2, 3]))            # one pass, then exits
'''),
        ("Selection sort", r'''
def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):    # find smallest in the rest
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]   # swap it into place
    return a

print(selection_sort([64, 25, 12, 22, 11]))   # [11, 12, 22, 25, 64]
'''),
        ("Insertion sort (fast on nearly-sorted data)", r'''
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:  # shift bigger items right
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key                # drop key into the gap
    return a

print(insertion_sort([12, 11, 13, 5, 6]))   # [5, 6, 11, 12, 13]
print(insertion_sort([1, 2, 3, 5, 4]))      # nearly sorted -> few shifts
'''),
    ],
    "gotchas": [
        "All three are O(n^2) — fine for learning or tiny lists, too slow for large data.",
        "Selection sort is NOT stable: equal keys can be reordered.",
        "For real code just use `sorted()` / `list.sort()` (Timsort, O(n log n) and stable).",
        "Forgetting the early-exit flag makes bubble sort do useless passes on sorted input.",
        "Off-by-one in the inner range (`n-1-i`) either skips the last pair or indexes out of range.",
    ],
    "exercises": [
        ("Sort [3,1,2] with bubble sort and print it.", "Swap adjacent pairs.",
         r'''def bubble(a):
    a = a[:]
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
print(bubble([3, 1, 2]))  # [1, 2, 3]'''),
        ("Sort [5,3,8,1] in DESCENDING order with selection sort.", "Find the max instead.",
         r'''def sel_desc(a):
    a = a[:]
    for i in range(len(a)):
        mx = i
        for j in range(i + 1, len(a)):
            if a[j] > a[mx]: mx = j
        a[i], a[mx] = a[mx], a[i]
    return a
print(sel_desc([5, 3, 8, 1]))  # [8, 5, 3, 1]'''),
        ("Use insertion sort to sort ['pear','fig','apple'] alphabetically.", "Same logic, string compare.",
         r'''def insert_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]; j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]; j -= 1
        a[j + 1] = key
    return a
print(insert_sort(["pear", "fig", "apple"]))  # ['apple','fig','pear']'''),
        ("Count the number of swaps bubble sort makes on [2,1,3,1].", "Increment on each swap.",
         r'''def count_swaps(a):
    a = a[:]; swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]; swaps += 1
    return swaps
print(count_swaps([2, 1, 3, 1]))  # 2'''),
        ("Make insertion sort return early-sorted detection (was it already sorted?).", "Track any shift.",
         r'''def insert_sorted_flag(a):
    a = a[:]; moved = False
    for i in range(1, len(a)):
        key = a[i]; j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]; j -= 1; moved = True
        a[j + 1] = key
    return a, (not moved)
print(insert_sorted_flag([1, 2, 3]))  # ([1,2,3], True)'''),
        ("Sort a list of (name, age) tuples by age using insertion sort.", "Compare the second item.",
         r'''def by_age(people):
    a = people[:]
    for i in range(1, len(a)):
        key = a[i]; j = i - 1
        while j >= 0 and a[j][1] > key[1]:
            a[j + 1] = a[j]; j -= 1
        a[j + 1] = key
    return a
print(by_age([("ann", 30), ("bo", 20), ("cy", 25)]))
# [('bo',20),('cy',25),('ann',30)]'''),
        ("Demonstrate that selection sort is unstable with [(1,'a'),(1,'b'),(0,'c')].", "Watch equal keys.",
         r'''#md
Sorting by the first element, selection sort may swap the two `1`s out of their
original `a`,`b` order because it swaps the found minimum into place regardless of
ties — so the result can be `[(0,'c'),(1,'b'),(1,'a')]`. A **stable** sort would
keep `(1,'a')` before `(1,'b')`.'''),
        ("Implement a 'cocktail' (bidirectional bubble) sort on [3,1,2,5,4].", "Bubble both directions.",
         r'''def cocktail(a):
    a = a[:]; lo, hi = 0, len(a) - 1
    while lo < hi:
        for j in range(lo, hi):
            if a[j] > a[j + 1]: a[j], a[j + 1] = a[j + 1], a[j]
        hi -= 1
        for j in range(hi, lo, -1):
            if a[j] < a[j - 1]: a[j], a[j - 1] = a[j - 1], a[j]
        lo += 1
    return a
print(cocktail([3, 1, 2, 5, 4]))  # [1, 2, 3, 4, 5]'''),
    ],
}

CONTENT["merge-sort"] = {
    "what": (
        "**Merge sort** is a **divide-and-conquer** algorithm: split the list in half, recursively "
        "sort each half, then **merge** the two sorted halves into one. It runs in **O(n log n)** in "
        "all cases and is **stable**, but uses O(n) extra space. The clever part is the linear-time "
        "merge of two already-sorted lists with two pointers."
    ),
    "why": (
        "It's the textbook introduction to divide-and-conquer and to provably O(n log n) sorting. "
        "Its merge step reappears in external sorting, merging k sorted streams, and counting "
        "inversions."
    ),
    "concepts": [
        ("Divide", "Split the array into two halves at the midpoint."),
        ("Conquer", "Recursively sort each half (base case: length ≤ 1)."),
        ("Merge", "Combine two sorted halves in O(n) using two pointers."),
        ("O(n log n)", "log n levels of splitting × O(n) work to merge per level."),
        ("Stable", "Equal elements keep their original relative order."),
        ("Extra space", "Needs O(n) scratch space for the merge (not in-place)."),
    ],
    "examples": [
        ("Classic recursive merge sort", r'''
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:        # <= keeps it STABLE
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])            # leftovers (one side is empty)
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:                  # base case
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])       # sort each half
    right = merge_sort(arr[mid:])
    return merge(left, right)          # combine

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]
'''),
        ("Watch the divide-and-conquer recursion", r'''
def merge_sort_verbose(arr, depth=0):
    pad = "  " * depth
    print(f"{pad}split {arr}")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_verbose(arr[:mid], depth + 1)
    right = merge_sort_verbose(arr[mid:], depth + 1)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: merged.append(left[i]); i += 1
        else: merged.append(right[j]); j += 1
    merged += left[i:] + right[j:]
    print(f"{pad}merge -> {merged}")
    return merged

merge_sort_verbose([5, 2, 4, 1])
'''),
        ("Merging k sorted lists with heapq", r'''
import heapq

def merge_k(lists):
    return list(heapq.merge(*lists))   # heapq.merge merges sorted iterables

a = [1, 4, 7]
b = [2, 5, 8]
c = [3, 6, 9]
print(merge_k([a, b, c]))   # [1,2,3,4,5,6,7,8,9]

# Counting inversions as a side effect of merging
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, l_inv = count_inversions(arr[:mid])
    right, r_inv = count_inversions(arr[mid:])
    merged, split = [], 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            split += len(left) - i      # all remaining left items are inversions
    merged += left[i:] + right[j:]
    return merged, l_inv + r_inv + split

_, inv = count_inversions([2, 4, 1, 3, 5])
print("inversions:", inv)   # 3
'''),
    ],
    "gotchas": [
        "Use `<=` (not `<`) in the merge to keep the sort STABLE.",
        "Merge sort is NOT in-place — it needs O(n) extra memory.",
        "Forgetting to append the leftovers (`left[i:]`, `right[j:]`) drops elements.",
        "The base case is `len(arr) <= 1`; without it the recursion never stops.",
        "Slicing (`arr[:mid]`) copies — fine for learning, but adds overhead vs index-based merge.",
    ],
    "exercises": [
        ("Merge two sorted lists [1,4,6] and [2,3,5] into one.", "Two pointers.",
         r'''def merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 4, 6], [2, 3, 5]))  # [1,2,3,4,5,6]'''),
        ("Sort [9,3,7,1] with merge sort.", "Split, sort halves, merge.",
         r'''def msort(a):
    if len(a) <= 1: return a
    m = len(a) // 2
    L, R = msort(a[:m]), msort(a[m:])
    out, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: out.append(L[i]); i += 1
        else: out.append(R[j]); j += 1
    return out + L[i:] + R[j:]
print(msort([9, 3, 7, 1]))  # [1, 3, 7, 9]'''),
        ("How many levels of recursion for a list of 8 items?", "log2(n).",
         r'''#md
**3 levels** of splitting (8 → 4 → 2 → 1), i.e. log2(8) = 3, plus the merges back
up. In general merge sort has about **log2(n)** levels.'''),
        ("Merge while removing duplicates: [1,2,2] and [2,3].", "Skip equal to last.",
         r'''def merge_unique(a, b):
    out, i, j = [], 0, 0
    while i < len(a) or j < len(b):
        if j >= len(b) or (i < len(a) and a[i] <= b[j]):
            x = a[i]; i += 1
        else:
            x = b[j]; j += 1
        if not out or out[-1] != x: out.append(x)
    return out
print(merge_unique([1, 2, 2], [2, 3]))  # [1, 2, 3]'''),
        ("Count inversions in [2,3,1].", "Pairs out of order.",
         r'''def inversions(a):
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]: count += 1
    return count
print(inversions([2, 3, 1]))  # 2'''),
        ("Use heapq.merge to merge [1,5] and [2,3].", "It returns an iterator.",
         r'''import heapq
print(list(heapq.merge([1, 5], [2, 3])))  # [1, 2, 3, 5]'''),
        ("Write an iterative (bottom-up) merge sort on [4,3,2,1].", "Merge widths 1,2,4...",
         r'''def merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
def bottom_up(arr):
    width = 1; a = arr[:]
    while width < len(a):
        for i in range(0, len(a), 2 * width):
            a[i:i+2*width] = merge(a[i:i+width], a[i+width:i+2*width])
        width *= 2
    return a
print(bottom_up([4, 3, 2, 1]))  # [1, 2, 3, 4]'''),
        ("Merge sort a list of words by length, keeping stability.", "Compare len(), use <=.",
         r'''def msort_len(a):
    if len(a) <= 1: return a
    m = len(a) // 2
    L, R = msort_len(a[:m]), msort_len(a[m:])
    out, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if len(L[i]) <= len(R[j]): out.append(L[i]); i += 1
        else: out.append(R[j]); j += 1
    return out + L[i:] + R[j:]
print(msort_len(["bb", "a", "ccc", "dd"]))  # ['a','bb','dd','ccc']'''),
    ],
}

CONTENT["quick-sort"] = {
    "what": (
        "**Quick sort** is a divide-and-conquer sort that picks a **pivot**, **partitions** the list "
        "so smaller items go left and larger go right, then recursively sorts each side. Average "
        "time is **O(n log n)** and it sorts **in place** (O(log n) stack), which makes it very fast "
        "in practice. Worst case is O(n^2) (bad pivots), mitigated by random or median pivots."
    ),
    "why": (
        "It's one of the most-used sorts in the real world and the key example of partitioning — a "
        "technique that also solves quickselect (finding the k-th smallest in O(n) average). "
        "Understanding pivots and partitioning is interview gold."
    ),
    "concepts": [
        ("Pivot", "The element you partition around (first, last, random, or median)."),
        ("Partition", "Rearrange so left < pivot ≤ right; returns the pivot's final index."),
        ("In place", "Sorts within the array — O(log n) stack, O(1) extra data."),
        ("Average O(n log n)", "Balanced partitions give log n levels of O(n) work."),
        ("Worst O(n^2)", "Already-sorted data with a naive pivot makes lopsided splits."),
        ("Quickselect", "Partition-only search for the k-th smallest — O(n) average."),
    ],
    "examples": [
        ("Readable quick sort (extra-list partition)", r'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]                  # middle element as pivot
    left = [x for x in arr if x < pivot]        # smaller
    mid = [x for x in arr if x == pivot]        # equal (handles dupes)
    right = [x for x in arr if x > pivot]       # larger
    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([3, 6, 1, 8, 2, 9, 4]))   # [1, 2, 3, 4, 6, 8, 9]
print(quick_sort([5, 5, 5, 1, 9]))         # [1, 5, 5, 5, 9]
'''),
        ("In-place Lomuto partition scheme", r'''
def quick_sort_inplace(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort_inplace(arr, lo, p - 1)      # sort left of pivot
        quick_sort_inplace(arr, p + 1, hi)      # sort right of pivot
    return arr

def partition(arr, lo, hi):
    pivot = arr[hi]                             # last element as pivot
    i = lo - 1                                  # boundary of smaller region
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]     # swap smaller item left
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]   # pivot into place
    return i + 1

print(quick_sort_inplace([9, 3, 7, 1, 8, 2]))   # [1, 2, 3, 7, 8, 9]
'''),
        ("Quickselect: k-th smallest without full sort", r'''
import random

def quickselect(arr, k):                # k is 1-based: k=1 -> smallest
    if not 1 <= k <= len(arr):
        raise ValueError("k out of range")
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k <= len(lows):
        return quickselect(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot                    # k falls in the pivot block
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

data = [7, 2, 9, 4, 1, 8, 3]
print("3rd smallest:", quickselect(data, 3))   # 3
print("1st smallest:", quickselect(data, 1))   # 1
'''),
    ],
    "gotchas": [
        "Naive pivot (first/last) on sorted data gives O(n^2) — use a random or median-of-three pivot.",
        "Forgetting the `== pivot` group makes duplicates loop or vanish; handle equals explicitly.",
        "The in-place version mutates the input list; copy first if you must keep the original.",
        "Off-by-one in partition indices is the classic bug — return the pivot's final index carefully.",
        "Deep recursion on adversarial input can hit Python's recursion limit; recurse the smaller side first.",
    ],
    "exercises": [
        ("Quick-sort [4,2,6,1] with the list-comprehension version.", "Pivot + partition.",
         r'''def qsort(a):
    if len(a) <= 1: return a
    p = a[len(a) // 2]
    return (qsort([x for x in a if x < p]) +
            [x for x in a if x == p] +
            qsort([x for x in a if x > p]))
print(qsort([4, 2, 6, 1]))  # [1, 2, 4, 6]'''),
        ("Write a partition that returns (smaller, equal, larger) for pivot 5 on [3,5,8,5,1].", "Three lists.",
         r'''def partition(a, p):
    return ([x for x in a if x < p],
            [x for x in a if x == p],
            [x for x in a if x > p])
print(partition([3, 5, 8, 5, 1], 5))  # ([3,1],[5,5],[8])'''),
        ("Why is quicksort O(n^2) worst case? When does it happen?", "Lopsided partitions.",
         r'''#md
When every pivot is the smallest or largest element (e.g. already-sorted data with
a first/last pivot), each partition shrinks the problem by only **one** element, so
there are n levels of O(n) work → **O(n^2)**. Random/median pivots avoid this.'''),
        ("Find the 2nd smallest in [8,3,5,1,9] using quickselect.", "Recurse one side.",
         r'''def quickselect(a, k):
    p = a[len(a) // 2]
    lows = [x for x in a if x < p]
    eq = [x for x in a if x == p]
    if k <= len(lows): return quickselect(lows, k)
    if k <= len(lows) + len(eq): return p
    return quickselect([x for x in a if x > p], k - len(lows) - len(eq))
print(quickselect([8, 3, 5, 1, 9], 2))  # 3'''),
        ("Sort [3,1,2] in DESCENDING order with quicksort.", "Flip the comparisons.",
         r'''def qsort_desc(a):
    if len(a) <= 1: return a
    p = a[0]
    return (qsort_desc([x for x in a[1:] if x > p]) + [p] +
            qsort_desc([x for x in a[1:] if x <= p]))
print(qsort_desc([3, 1, 2]))  # [3, 2, 1]'''),
        ("Count partition operations (comparisons) sorting [2,1,3].", "Tally in partition.",
         r'''def qsort_count(a, c=[0]):
    if len(a) <= 1: return a
    p = a[len(a)//2]
    less, eq, more = [], [], []
    for x in a:
        c[0] += 1
        (less if x < p else eq if x == p else more).append(x)
    return qsort_count(less) + eq + qsort_count(more)
counter = [0]; qsort_count([2, 1, 3], counter)
print(counter[0])  # 5'''),
        ("Use median-of-three to pick a better pivot from [9,1,5].", "Median of first/mid/last.",
         r'''def median_of_three(a):
    first, mid, last = a[0], a[len(a)//2], a[-1]
    return sorted([first, mid, last])[1]
print(median_of_three([9, 1, 5]))  # 5'''),
        ("Implement the Dutch National Flag partition of [2,0,2,1,1,0] around 1.", "Three-way pointers.",
         r'''def three_way(a, pivot):
    a = a[:]; lo, mid, hi = 0, 0, len(a) - 1
    while mid <= hi:
        if a[mid] < pivot:
            a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1
        elif a[mid] > pivot:
            a[mid], a[hi] = a[hi], a[mid]; hi -= 1
        else:
            mid += 1
    return a
print(three_way([2, 0, 2, 1, 1, 0], 1))  # [0,0,1,1,2,2]'''),
    ],
}

CONTENT["heap-counting-radix-sort"] = {
    "what": (
        "Beyond comparison sorts there are **heap sort** (build a heap, repeatedly extract the min/"
        "max — O(n log n), in place) and the **non-comparison** sorts: **counting sort** tallies how "
        "many of each value exist (O(n + k) for values in range k), and **radix sort** sorts numbers "
        "digit by digit using counting sort as a subroutine (O(d·(n + b)))."
    ),
    "why": (
        "Counting and radix sort beat the O(n log n) comparison lower bound when keys are small "
        "integers or fixed-width — crucial for sorting huge integer/string datasets. Heap sort gives "
        "guaranteed O(n log n) with O(1) extra space."
    ),
    "concepts": [
        ("Heap sort", "heapify then pop the root n times — O(n log n), in place."),
        ("Counting sort", "Count occurrences, then rebuild — O(n + k), stable if done right."),
        ("Radix sort", "Sort by each digit (LSD→MSD) using a stable counting sort."),
        ("Non-comparison", "These don't compare pairs, so they dodge the n log n bound."),
        ("Range matters", "Counting sort is great when k (value range) is small, bad when huge."),
        ("Stability", "Radix sort REQUIRES a stable inner sort to work correctly."),
    ],
    "examples": [
        ("Heap sort using heapq", r'''
import heapq

def heap_sort(arr):
    h = arr[:]            # copy
    heapq.heapify(h)      # O(n) build a min-heap
    return [heapq.heappop(h) for _ in range(len(h))]   # pop smallest n times

print(heap_sort([5, 3, 8, 1, 9, 2]))   # [1, 2, 3, 5, 8, 9]

# Manual sift-down heap sort (in place, max-heap)
def heapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[largest]: largest = l
    if r < n and a[r] > a[largest]: largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort_inplace(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):     # build max-heap
        heapify(a, n, i)
    for end in range(n - 1, 0, -1):         # pop max to the end
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)
    return a

print(heap_sort_inplace([4, 10, 3, 5, 1]))   # [1, 3, 4, 5, 10]
'''),
        ("Counting sort for small-range integers", r'''
def counting_sort(arr):
    if not arr:
        return arr
    lo, hi = min(arr), max(arr)
    counts = [0] * (hi - lo + 1)
    for x in arr:
        counts[x - lo] += 1          # tally each value
    out = []
    for i, c in enumerate(counts):
        out.extend([i + lo] * c)     # rebuild in order
    return out

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))   # [1, 2, 2, 3, 3, 4, 8]
print(counting_sort([0, -3, -1, 2, -3]))      # handles negatives via offset
'''),
        ("LSD radix sort for non-negative integers", r'''
def counting_sort_by_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for x in arr:
        count[(x // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]            # prefix sums -> positions
    for x in reversed(arr):                 # reversed keeps it STABLE
        d = (x // exp) % 10
        count[d] -= 1
        output[count[d]] = x
    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:                # one pass per digit
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

print(radix_sort([170, 45, 75, 90, 2, 802, 24, 66]))
# [2, 24, 45, 66, 75, 90, 170, 802]
'''),
    ],
    "gotchas": [
        "Counting sort needs a small value range k — for huge ranges its O(k) memory explodes.",
        "Radix sort's inner counting sort MUST be stable, or digits clobber each other.",
        "Plain counting/radix sort assumes non-negative integers; negatives need an offset or split.",
        "`heapq` is a MIN-heap; for a max-heap push negated values or use `_heapify_max` tricks.",
        "Heap sort is not stable; counting/radix can be stable if you build output carefully.",
    ],
    "exercises": [
        ("Sort [3,1,2] using heapq (heapify + heappop).", "Min-heap pops smallest.",
         r'''import heapq
h = [3, 1, 2]; heapq.heapify(h)
print([heapq.heappop(h) for _ in range(3)])  # [1, 2, 3]'''),
        ("Counting-sort the digits [1,4,1,2,7,5,2].", "Tally then rebuild.",
         r'''def counting_sort(a):
    counts = [0] * (max(a) + 1)
    for x in a: counts[x] += 1
    out = []
    for v, c in enumerate(counts): out += [v] * c
    return out
print(counting_sort([1, 4, 1, 2, 7, 5, 2]))  # [1,1,2,2,4,5,7]'''),
        ("Find the 3 largest numbers in [5,1,8,2,9,3] with a heap.", "heapq.nlargest.",
         r'''import heapq
print(heapq.nlargest(3, [5, 1, 8, 2, 9, 3]))  # [9, 8, 5]'''),
        ("Why can radix sort beat O(n log n)? State its complexity.", "Digit passes.",
         r'''#md
Radix sort does **d** passes (one per digit), each a stable counting sort over n
items with base b → **O(d·(n + b))**. When d and b are small constants, that's
effectively **O(n)** — it never compares two keys, so it dodges the comparison
lower bound of O(n log n).'''),
        ("Use counting sort to sort the string 'dbca' alphabetically.", "Count chars.",
         r'''def sort_str(s):
    counts = [0] * 26
    for c in s: counts[ord(c) - 97] += 1
    return "".join(chr(i + 97) * n for i, n in enumerate(counts))
print(sort_str("dbca"))  # abcd'''),
        ("Build a max-heap behavior with heapq by negating values [3,1,2].", "Push negatives.",
         r'''import heapq
nums = [3, 1, 2]
h = [-x for x in nums]; heapq.heapify(h)
print(-heapq.heappop(h))  # 3 (largest)'''),
        ("Radix-sort [170,45,75,90,802,24].", "LSD digit passes.",
         r'''def radix(a):
    a = a[:]; exp = 1; mx = max(a)
    while mx // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a: buckets[(x // exp) % 10].append(x)
        a = [x for b in buckets for x in b]
        exp *= 10
    return a
print(radix([170, 45, 75, 90, 802, 24]))  # [24,45,75,90,170,802]'''),
        ("Use counting sort to find the most frequent value in [2,3,3,3,1,2].", "Max count.",
         r'''def most_frequent(a):
    counts = [0] * (max(a) + 1)
    for x in a: counts[x] += 1
    return counts.index(max(counts))
print(most_frequent([2, 3, 3, 3, 1, 2]))  # 3'''),
    ],
}

CONTENT["trees-and-bst"] = {
    "what": (
        "A **tree** is a hierarchy of **nodes**: one **root** at the top, each node pointing to "
        "**children**, no cycles. A **binary tree** limits each node to ≤ 2 children (left/right). A "
        "**binary search tree (BST)** adds an ordering rule: every left descendant is smaller and "
        "every right descendant is larger than the node. That rule makes search, insert, and delete "
        "O(log n) on a balanced tree."
    ),
    "why": (
        "Trees model hierarchy everywhere — file systems, the DOM, parse trees, decision trees. BSTs "
        "give ordered O(log n) operations and underpin databases/indexes (B-trees) and ordered "
        "containers."
    ),
    "concepts": [
        ("Root / leaf", "Root has no parent; a leaf has no children."),
        ("Depth / height", "Depth = distance from root; height = longest path to a leaf."),
        ("Binary tree", "Each node has at most a left and a right child."),
        ("BST property", "left subtree < node < right subtree, recursively."),
        ("Search O(h)", "Compare and go left/right; O(log n) if balanced, O(n) if skewed."),
        ("Insert/delete", "Follow the BST rule; delete has a three-case fix-up."),
    ],
    "examples": [
        ("A BST with insert and search", r'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)        # found the spot
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node                       # duplicates ignored

    def search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

bst = BST()
for v in [5, 3, 8, 1, 4, 7, 9]:
    bst.insert(v)
print(bst.search(7))    # True
print(bst.search(6))    # False
'''),
        ("In-order traversal of a BST yields sorted order", r'''
class TreeNode:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

def insert(root, v):
    if root is None: return TreeNode(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def in_order(node, out):
    if node:
        in_order(node.left, out)    # left
        out.append(node.value)      # node
        in_order(node.right, out)   # right

root = None
for v in [5, 3, 8, 1, 4, 7, 9]:
    root = insert(root, v)
result = []
in_order(root, result)
print(result)   # [1, 3, 4, 5, 7, 8, 9] -> SORTED!
'''),
        ("Height, node count, and min/max of a BST", r'''
class TreeNode:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

def insert(root, v):
    if root is None: return TreeNode(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def height(node):
    if node is None:
        return -1                       # empty tree has height -1
    return 1 + max(height(node.left), height(node.right))

def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)

def find_min(node):
    while node.left:                    # smallest is leftmost
        node = node.left
    return node.value

root = None
for v in [5, 3, 8, 1, 4, 7, 9]:
    root = insert(root, v)
print("height:", height(root))   # 2
print("nodes :", count(root))    # 7
print("min   :", find_min(root)) # 1
'''),
    ],
    "gotchas": [
        "An unbalanced BST (e.g. inserting sorted data) degrades to a linked list — O(n) operations.",
        "Forgetting the `node is None` base case in recursion causes AttributeError on `.left`.",
        "Deleting a node with two children needs the in-order successor/predecessor swap.",
        "Height of an empty tree is -1 (or 0 for one node) — pick a convention and be consistent.",
        "Duplicate handling is a design choice — ignore, count, or always go right; decide up front.",
    ],
    "exercises": [
        ("Create a TreeNode class and build root=10 with children 5 and 15.", "left/right attrs.",
         r'''class TreeNode:
    def __init__(self, v): self.value = v; self.left = None; self.right = None
root = TreeNode(10)
root.left = TreeNode(5); root.right = TreeNode(15)
print(root.left.value, root.right.value)  # 5 15'''),
        ("Insert [4,2,6,1,3] into a BST and search for 3.", "Recursive insert.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def insert(root, v):
    if not root: return N(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root
def search(root, v):
    while root:
        if root.value == v: return True
        root = root.left if v < root.value else root.right
    return False
r = None
for v in [4, 2, 6, 1, 3]: r = insert(r, v)
print(search(r, 3))  # True'''),
        ("Count the nodes in a binary tree recursively.", "1 + left + right.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def count(n):
    return 0 if n is None else 1 + count(n.left) + count(n.right)
root = N(1); root.left = N(2); root.right = N(3)
print(count(root))  # 3'''),
        ("Find the height of a tree (edges on the longest root-to-leaf path).", "1 + max(children).",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))
root = N(1); root.left = N(2); root.left.left = N(3)
print(height(root))  # 2'''),
        ("Find the minimum value in a BST.", "Go left until None.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def insert(r, v):
    if not r: return N(v)
    if v < r.value: r.left = insert(r.left, v)
    else: r.right = insert(r.right, v)
    return r
def find_min(r):
    while r.left: r = r.left
    return r.value
r = None
for v in [5, 3, 8, 1]: r = insert(r, v)
print(find_min(r))  # 1'''),
        ("Sum all values in a binary tree.", "Recursive sum.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def tree_sum(n):
    return 0 if n is None else n.value + tree_sum(n.left) + tree_sum(n.right)
root = N(1); root.left = N(2); root.right = N(3)
print(tree_sum(root))  # 6'''),
        ("Validate whether a tree is a BST.", "Pass min/max bounds down.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def is_bst(n, lo=float("-inf"), hi=float("inf")):
    if n is None: return True
    if not (lo < n.value < hi): return False
    return is_bst(n.left, lo, n.value) and is_bst(n.right, n.value, hi)
root = N(2); root.left = N(1); root.right = N(3)
print(is_bst(root))  # True'''),
        ("Find the lowest common ancestor of 1 and 4 in a BST.", "Use the ordering.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def insert(r, v):
    if not r: return N(v)
    if v < r.value: r.left = insert(r.left, v)
    else: r.right = insert(r.right, v)
    return r
def lca(root, a, b):
    while root:
        if a < root.value and b < root.value: root = root.left
        elif a > root.value and b > root.value: root = root.right
        else: return root.value
r = None
for v in [5, 3, 8, 1, 4]: r = insert(r, v)
print(lca(r, 1, 4))  # 3'''),
    ],
}

CONTENT["tree-traversals"] = {
    "what": (
        "A **traversal** visits every node of a tree in some order. The **depth-first** orders differ "
        "by when you visit the node relative to its children: **pre-order** (node, left, right), "
        "**in-order** (left, node, right — sorted for a BST), **post-order** (left, right, node). "
        "**Level-order** (breadth-first) visits the tree row by row using a queue."
    ),
    "why": (
        "Different tasks need different orders: in-order to read a BST sorted, pre-order to copy/"
        "serialize, post-order to delete/evaluate (children before parent), level-order for shortest "
        "paths and 'by depth' processing."
    ),
    "concepts": [
        ("Pre-order", "Node → Left → Right. Good for copying/serializing a tree."),
        ("In-order", "Left → Node → Right. Sorted output for a BST."),
        ("Post-order", "Left → Right → Node. Good for deletion/expression evaluation."),
        ("Level-order", "Row by row using a queue (BFS)."),
        ("Recursive DFS", "Simple, but uses the call stack (O(h))."),
        ("Iterative DFS", "Use an explicit stack to avoid recursion limits."),
    ],
    "examples": [
        ("All three depth-first traversals (recursive)", r'''
class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

#        1
#       / \
#      2   3
#     / \
#    4   5
root = N(1)
root.left = N(2); root.right = N(3)
root.left.left = N(4); root.left.right = N(5)

def pre(n, out):
    if n: out.append(n.value); pre(n.left, out); pre(n.right, out)

def ino(n, out):
    if n: ino(n.left, out); out.append(n.value); ino(n.right, out)

def post(n, out):
    if n: post(n.left, out); post(n.right, out); out.append(n.value)

a = []; pre(root, a);  print("pre  :", a)   # [1, 2, 4, 5, 3]
b = []; ino(root, b);  print("in   :", b)   # [4, 2, 5, 1, 3]
c = []; post(root, c); print("post :", c)   # [4, 5, 2, 3, 1]
'''),
        ("Level-order (BFS) with a queue", r'''
from collections import deque

class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

root = N(1)
root.left = N(2); root.right = N(3)
root.left.left = N(4); root.right.right = N(5)

def level_order(root):
    if not root:
        return []
    rows, q = [], deque([root])
    while q:
        row = []
        for _ in range(len(q)):        # process one full level
            node = q.popleft()
            row.append(node.value)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        rows.append(row)
    return rows

print(level_order(root))   # [[1], [2, 3], [4, 5]]
'''),
        ("Iterative pre-order with an explicit stack", r'''
class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

root = N(1)
root.left = N(2); root.right = N(3)
root.left.left = N(4); root.left.right = N(5)

def pre_order_iter(root):
    if not root:
        return []
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        out.append(node.value)
        if node.right: stack.append(node.right)   # push right FIRST
        if node.left:  stack.append(node.left)    # so left is popped first
    return out

print(pre_order_iter(root))   # [1, 2, 4, 5, 3]
'''),
    ],
    "gotchas": [
        "In-order gives sorted output ONLY for a binary SEARCH tree, not any binary tree.",
        "In iterative pre-order, push the RIGHT child before the left so left is visited first.",
        "Deep recursive traversal can exceed Python's recursion limit on tall trees — go iterative.",
        "Level-order needs a queue (FIFO); using a stack turns it into DFS.",
        "Don't forget the `if node:` guard — recursing into None throws AttributeError.",
    ],
    "exercises": [
        ("Pre-order traverse a tree root=1,left=2,right=3.", "Node, left, right.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(1); root.left = N(2); root.right = N(3)
def pre(n, out):
    if n: out.append(n.value); pre(n.left, out); pre(n.right, out)
o = []; pre(root, o); print(o)  # [1, 2, 3]'''),
        ("In-order traverse the same tree.", "Left, node, right.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(2); root.left = N(1); root.right = N(3)
def ino(n, out):
    if n: ino(n.left, out); out.append(n.value); ino(n.right, out)
o = []; ino(root, o); print(o)  # [1, 2, 3]'''),
        ("Post-order traverse a tree.", "Left, right, node.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(1); root.left = N(2); root.right = N(3)
def post(n, out):
    if n: post(n.left, out); post(n.right, out); out.append(n.value)
o = []; post(root, o); print(o)  # [2, 3, 1]'''),
        ("Level-order traverse into a flat list.", "Queue + popleft.",
         r'''from collections import deque
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(1); root.left = N(2); root.right = N(3)
def bfs(r):
    out, q = [], deque([r])
    while q:
        n = q.popleft(); out.append(n.value)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return out
print(bfs(root))  # [1, 2, 3]'''),
        ("Count leaf nodes (no children) in a tree.", "Both children None.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def leaves(n):
    if n is None: return 0
    if not n.left and not n.right: return 1
    return leaves(n.left) + leaves(n.right)
root = N(1); root.left = N(2); root.right = N(3)
print(leaves(root))  # 2'''),
        ("Find the maximum depth (number of levels) of a tree.", "1 + max child depth.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def depth(n):
    return 0 if n is None else 1 + max(depth(n.left), depth(n.right))
root = N(1); root.left = N(2); root.left.left = N(3)
print(depth(root))  # 3'''),
        ("Return the right-side view (rightmost node per level).", "BFS, take last per level.",
         r'''from collections import deque
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def right_view(root):
    if not root: return []
    out, q = [], deque([root])
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == n - 1: out.append(node.value)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return out
r = N(1); r.left = N(2); r.right = N(3); r.left.left = N(4)
print(right_view(r))  # [1, 3, 4]'''),
        ("Reconstruct in-order WITHOUT recursion using a stack.", "Push lefts, pop, go right.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def inorder_iter(root):
    out, stack, cur = [], [], root
    while stack or cur:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop(); out.append(cur.value); cur = cur.right
    return out
r = N(2); r.left = N(1); r.right = N(3)
print(inorder_iter(r))  # [1, 2, 3]'''),
    ],
}

CONTENT["avl-and-balanced-trees"] = {
    "what": (
        "A plain BST can degenerate into a linked list (O(n)) if you insert sorted data. **Balanced "
        "trees** keep the height ~log n automatically. An **AVL tree** is a BST where every node's "
        "**balance factor** (height of left − height of right) stays in {-1, 0, +1}; after each "
        "insert/delete it restores balance with **rotations** (LL, RR, LR, RL). Result: guaranteed "
        "O(log n) search/insert/delete."
    ),
    "why": (
        "Balancing is what makes tree-based maps/sets reliably fast. AVL trees teach rotations — the "
        "mechanism behind red-black trees (used in many language libraries) and database B-trees."
    ),
    "concepts": [
        ("Balance factor", "height(left) − height(right); must stay in [-1, 1]."),
        ("Rotation", "Local re-link of 2–3 nodes that rebalances while preserving BST order."),
        ("LL / RR", "Single rotation (right / left) for straight-line imbalance."),
        ("LR / RL", "Double rotation for 'zig-zag' imbalance."),
        ("Height tracking", "Each node caches its height to compute balance in O(1)."),
        ("Guarantee", "Height stays O(log n), so all operations are O(log n)."),
    ],
    "examples": [
        ("Why an unbalanced BST is bad", r'''
class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

def insert(root, v):
    if root is None: return N(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))

# Inserting SORTED data makes a right-leaning 'stick'
root = None
for v in [1, 2, 3, 4, 5]:
    root = insert(root, v)
print("height of skewed tree:", height(root))   # 4 -> O(n), not O(log n)!
# A balanced tree of 5 nodes would have height 2.
'''),
        ("A self-balancing AVL tree", r'''
class N:
    def __init__(self, v):
        self.value = v; self.left = None; self.right = None; self.height = 1

def h(n):       return n.height if n else 0
def balance(n): return h(n.left) - h(n.right) if n else 0
def update(n):  n.height = 1 + max(h(n.left), h(n.right))

def rotate_right(y):
    x = y.left; y.left = x.right; x.right = y
    update(y); update(x)
    return x

def rotate_left(x):
    y = x.right; x.right = y.left; y.left = x
    update(x); update(y)
    return y

def insert(node, v):
    if node is None:
        return N(v)
    if v < node.value: node.left = insert(node.left, v)
    else:              node.right = insert(node.right, v)
    update(node)
    bf = balance(node)
    if bf > 1 and v < node.left.value:                 # LL
        return rotate_right(node)
    if bf < -1 and v > node.right.value:               # RR
        return rotate_left(node)
    if bf > 1 and v > node.left.value:                 # LR
        node.left = rotate_left(node.left); return rotate_right(node)
    if bf < -1 and v < node.right.value:               # RL
        node.right = rotate_right(node.right); return rotate_left(node)
    return node

root = None
for v in [1, 2, 3, 4, 5]:        # same sorted data as before
    root = insert(root, v)
print("AVL root:", root.value)   # 2  (rebalanced!)
print("AVL height:", root.height)   # 3 levels -> stays ~log n
'''),
        ("Verify the tree stays balanced", r'''
class N:
    def __init__(self, v):
        self.value = v; self.left = None; self.right = None; self.height = 1

def h(n): return n.height if n else 0
def update(n): n.height = 1 + max(h(n.left), h(n.right))
def balance(n): return h(n.left) - h(n.right) if n else 0

def rot_r(y):
    x = y.left; y.left = x.right; x.right = y; update(y); update(x); return x
def rot_l(x):
    y = x.right; x.right = y.left; y.left = x; update(x); update(y); return y

def insert(node, v):
    if node is None: return N(v)
    if v < node.value: node.left = insert(node.left, v)
    else: node.right = insert(node.right, v)
    update(node); bf = balance(node)
    if bf > 1 and v < node.left.value: return rot_r(node)
    if bf < -1 and v > node.right.value: return rot_l(node)
    if bf > 1 and v > node.left.value:
        node.left = rot_l(node.left); return rot_r(node)
    if bf < -1 and v < node.right.value:
        node.right = rot_r(node.right); return rot_l(node)
    return node

def is_balanced(n):
    if n is None: return True
    return abs(balance(n)) <= 1 and is_balanced(n.left) and is_balanced(n.right)

root = None
for v in range(1, 16):          # 15 sorted inserts
    root = insert(root, v)
print("balanced?", is_balanced(root))   # True
print("height   :", h(root))            # 4 (log2(15) ~ 3.9)
'''),
    ],
    "gotchas": [
        "Forgetting to UPDATE node heights after a rotation corrupts every later balance check.",
        "Mixing up the four cases (LL/RR/LR/RL) rotates the wrong way and breaks BST order.",
        "Rotations must preserve the BST property — re-link children in the exact documented order.",
        "Balance factor uses HEIGHTS, not node counts; an off-by-one in height breaks balancing.",
        "Deletion rebalancing is trickier than insertion — you may need rotations up the whole path.",
    ],
    "exercises": [
        ("Compute the balance factor of a node given left height 2, right height 0.", "left - right.",
         r'''left_h, right_h = 2, 0
print(left_h - right_h)  # 2  -> unbalanced (needs rotation)'''),
        ("Show a skewed BST's height for sorted inserts [1,2,3,4].", "Each goes right.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def insert(r, v):
    if not r: return N(v)
    if v < r.value: r.left = insert(r.left, v)
    else: r.right = insert(r.right, v)
    return r
def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))
r = None
for v in [1, 2, 3, 4]: r = insert(r, v)
print(height(r))  # 3 (a stick)'''),
        ("Implement a right rotation on three nodes.", "Promote the left child.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def rotate_right(y):
    x = y.left; y.left = x.right; x.right = y
    return x
y = N(3); y.left = N(2); y.left.left = N(1)
new_root = rotate_right(y)
print(new_root.value)  # 2'''),
        ("Implement a left rotation on three nodes.", "Promote the right child.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def rotate_left(x):
    y = x.right; x.right = y.left; y.left = x
    return y
x = N(1); x.right = N(2); x.right.right = N(3)
new_root = rotate_left(x)
print(new_root.value)  # 2'''),
        ("Decide which rotation an LL imbalance needs.", "Heavy on left-left.",
         r'''#md
An **LL** case (inserted into the left subtree's left side) is fixed with a single
**right rotation** at the unbalanced node.'''),
        ("Check if a tree is height-balanced (|bf| ≤ 1 everywhere).", "Recurse heights.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def check(n):
    if n is None: return 0, True
    lh, lb = check(n.left); rh, rb = check(n.right)
    bal = lb and rb and abs(lh - rh) <= 1
    return 1 + max(lh, rh), bal
root = N(1); root.left = N(2); root.left.left = N(3)
print(check(root)[1])  # False'''),
        ("Identify the case (LL/RR/LR/RL) when bf=-2 and the new value went left of the right child.", "Zig-zag.",
         r'''#md
bf = −2 means **right-heavy**; the value landing on the right child's **left** side
is the **RL** case → fix with a **right rotation on the right child, then a left
rotation** on the node.'''),
        ("Insert [10,20,30] into an AVL tree and report the new root.", "RR triggers left rotation.",
         r'''class N:
    def __init__(self, v):
        self.value = v; self.left = self.right = None; self.height = 1
def h(n): return n.height if n else 0
def upd(n): n.height = 1 + max(h(n.left), h(n.right))
def bf(n): return h(n.left) - h(n.right) if n else 0
def rl(x):
    y = x.right; x.right = y.left; y.left = x; upd(x); upd(y); return y
def insert(n, v):
    if not n: return N(v)
    if v < n.value: n.left = insert(n.left, v)
    else: n.right = insert(n.right, v)
    upd(n)
    if bf(n) < -1 and v > n.right.value: return rl(n)
    return n
r = None
for v in [10, 20, 30]: r = insert(r, v)
print(r.value)  # 20'''),
    ],
}

CONTENT["heaps"] = {
    "what": (
        "A **heap** is a complete binary tree stored in an array that keeps the smallest (min-heap) "
        "or largest (max-heap) element at the root. It gives **O(1)** peek at the extreme, **O(log "
        "n)** push and pop, and **O(n)** to build from a list. Python's `heapq` module implements a "
        "min-heap on a plain list — the backbone of **priority queues**."
    ),
    "why": (
        "Heaps power priority queues: schedulers, Dijkstra's shortest path, A* search, event "
        "simulation, and 'top-k / k-th largest' problems. When you need the best item repeatedly "
        "without fully sorting, reach for a heap."
    ),
    "concepts": [
        ("Heap property", "Every parent ≤ (min-heap) or ≥ (max-heap) its children."),
        ("Array layout", "children of i are 2i+1 and 2i+2; parent is (i-1)//2."),
        ("push / pop", "O(log n): sift-up on insert, sift-down on removal."),
        ("peek", "O(1) — the root is `heap[0]`."),
        ("heapify", "Turn a list into a heap in O(n)."),
        ("Priority queue", "Pop items in priority order; store (priority, item) tuples."),
    ],
    "examples": [
        ("heapq basics: push, pop, peek, heapify", r'''
import heapq

h = []
for x in [5, 3, 8, 1, 9, 2]:
    heapq.heappush(h, x)         # O(log n) each
print("min (peek):", h[0])       # 1  -> root is always the smallest
print("pop:", heapq.heappop(h))  # 1
print("pop:", heapq.heappop(h))  # 2

# Build a heap from a list in O(n)
data = [9, 4, 7, 1, 2, 6]
heapq.heapify(data)
print("heapified:", data)        # [1, 2, 6, 9, 4, 7] (heap order)
print("3 smallest:", heapq.nsmallest(3, [9, 4, 7, 1, 2, 6]))   # [1, 2, 4]
print("3 largest :", heapq.nlargest(3, [9, 4, 7, 1, 2, 6]))    # [9, 7, 6]
'''),
        ("Priority queue with (priority, task) tuples", r'''
import heapq

pq = []
heapq.heappush(pq, (2, "write tests"))
heapq.heappush(pq, (1, "fix bug"))        # lower number = higher priority
heapq.heappush(pq, (3, "deploy"))
heapq.heappush(pq, (1, "security patch"))

while pq:
    priority, task = heapq.heappop(pq)
    print(f"[p{priority}] {task}")
# fix bug, security patch (both p1, tie-broken by text), then p2, p3
'''),
        ("Max-heap and k-th largest", r'''
import heapq

# Python only has a MIN-heap; negate values for a max-heap
nums = [5, 3, 8, 1, 9, 2]
max_heap = [-x for x in nums]
heapq.heapify(max_heap)
print("max:", -heapq.heappop(max_heap))   # 9

# k-th largest using a size-k min-heap (efficient, O(n log k))
def kth_largest(arr, k):
    h = arr[:k]
    heapq.heapify(h)
    for x in arr[k:]:
        if x > h[0]:                # bigger than the smallest of our top-k
            heapq.heapreplace(h, x) # pop smallest, push x
    return h[0]

print("2nd largest:", kth_largest([3, 2, 1, 5, 6, 4], 2))   # 5
'''),
    ],
    "gotchas": [
        "`heapq` is a MIN-heap only; negate values (or wrap) for max-heap behavior.",
        "`heap[0]` peeks the min, but the rest of the list is NOT sorted — don't read it as sorted.",
        "Pushing non-comparable items (e.g. dicts) errors on ties; use a (priority, counter, item) tuple.",
        "Mutating the underlying list directly breaks the heap invariant — only use heapq functions.",
        "`sorted(heap)` is O(n log n); if you only need the top-k, use nlargest/nsmallest or a size-k heap.",
    ],
    "exercises": [
        ("Push 4,1,7,3 into a min-heap and pop the smallest.", "heappush/heappop.",
         r'''import heapq
h = []
for x in [4, 1, 7, 3]: heapq.heappush(h, x)
print(heapq.heappop(h))  # 1'''),
        ("Find the 3 smallest of [8,2,5,1,9,3].", "heapq.nsmallest.",
         r'''import heapq
print(heapq.nsmallest(3, [8, 2, 5, 1, 9, 3]))  # [1, 2, 3]'''),
        ("Turn [5,2,8,1] into a max-heap and read the max.", "Negate values.",
         r'''import heapq
nums = [5, 2, 8, 1]
h = [-x for x in nums]; heapq.heapify(h)
print(-h[0])  # 8'''),
        ("Build a priority queue: pop tasks (3,'c'),(1,'a'),(2,'b') in order.", "Tuples sort by first.",
         r'''import heapq
pq = []
for item in [(3, "c"), (1, "a"), (2, "b")]:
    heapq.heappush(pq, item)
print([heapq.heappop(pq)[1] for _ in range(3)])  # ['a','b','c']'''),
        ("Merge sorted lists [1,4] and [2,3] with a heap.", "heapq.merge.",
         r'''import heapq
print(list(heapq.merge([1, 4], [2, 3])))  # [1, 2, 3, 4]'''),
        ("Find the k=2 largest in a stream using a size-k heap.", "Keep only k items.",
         r'''import heapq
def two_largest(stream):
    h = []
    for x in stream:
        heapq.heappush(h, x)
        if len(h) > 2: heapq.heappop(h)
    return sorted(h, reverse=True)
print(two_largest([4, 1, 7, 3, 8, 5]))  # [8, 7]'''),
        ("Compute the array index of the parent of node at index 5.", "(i-1)//2.",
         r'''i = 5
print((i - 1) // 2)  # 2'''),
        ("Use a heap to sort [3,1,4,1,5] ascending (heap sort).", "heapify + pop all.",
         r'''import heapq
def heap_sort(a):
    h = a[:]; heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
print(heap_sort([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]'''),
    ],
}

CONTENT["tries"] = {
    "what": (
        "A **trie** (prefix tree) stores strings by their characters: each node represents one "
        "character, and a path from the root spells a prefix. Words sharing a prefix share nodes. "
        "Insert and search are **O(L)** where L is the word length — independent of how many words "
        "are stored. A flag marks where complete words end."
    ),
    "why": (
        "Tries make prefix queries fast: autocomplete, spell-check, dictionary lookups, IP routing, "
        "and 'does any word start with…?'. They beat hash sets when you need PREFIX matching, not "
        "just exact membership."
    ),
    "concepts": [
        ("Node", "Holds a map child-char → child-node and an 'is end of word' flag."),
        ("Insert O(L)", "Walk/create one node per character of the word."),
        ("Search O(L)", "Follow characters; require the end flag for a full word."),
        ("startsWith", "Same walk but no end-flag needed — that's the trie's superpower."),
        ("Shared prefixes", "'car' and 'cart' reuse the 'c-a-r' path — saves space."),
        ("Alphabet", "Children keyed by a dict (flexible) or a fixed-size array (fast)."),
    ],
    "examples": [
        ("A Trie class with insert, search, startsWith", r'''
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
'''),
        ("Autocomplete: all words with a given prefix", r'''
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
'''),
        ("Counting words and longest common prefix", r'''
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
'''),
    ],
    "gotchas": [
        "Forgetting the `is_end` flag makes 'car' match when only 'card' was inserted.",
        "Searching a prefix with `search()` (needs is_end) vs `starts_with()` are different questions.",
        "Tries can use lots of memory for sparse data — many nodes with single children.",
        "Use `setdefault`/`defaultdict` to create child nodes; manual `if ch not in` is error-prone.",
        "Deletion is fiddly — you must avoid removing nodes still shared by other words.",
    ],
    "exercises": [
        ("Insert 'hi' into a trie and confirm search('hi') is True.", "Walk chars, set is_end.",
         r'''class Node:
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
insert("hi"); print(search("hi"))  # True'''),
        ("After inserting 'cat', is search('ca') True or False? Why?", "is_end flag.",
         r'''#md
**False.** 'ca' is only a prefix; the `is_end` flag is set on the 'cat' node, not
the 'a' node. Use `starts_with('ca')` to test for the prefix instead.'''),
        ("Implement starts_with('ap') after inserting 'apple'.", "Walk, ignore is_end.",
         r'''class Node:
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
insert("apple"); print(starts_with("ap"))  # True'''),
        ("Count how many words are stored in a trie.", "DFS counting is_end nodes.",
         r'''class Node:
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
print(count(root))  # 3'''),
        ("List all words in a trie via DFS.", "Accumulate the path.",
         r'''class Node:
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
out = []; words(root, "", out); print(out)  # ['tea','ted','to']'''),
        ("Find the longest word in a trie.", "Track max-length is_end path.",
         r'''class Node:
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
print(longest(root, ""))  # abc'''),
        ("Check if any inserted word is a prefix of 'apple' (e.g. 'app').", "Stop at any is_end.",
         r'''class Node:
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
insert("app"); print(has_prefix_word("apple"))  # True'''),
        ("Build a trie and return the number of words sharing prefix 'ca'.", "Walk then DFS count.",
         r'''class Node:
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
print(count_from(n))  # 3'''),
    ],
}

CONTENT["graphs"] = {
    "what": (
        "A **graph** is a set of **vertices** (nodes) connected by **edges**. Edges can be "
        "**directed** (one-way) or **undirected**, and **weighted** (carry a cost) or not. Common "
        "representations: an **adjacency list** (dict: node → neighbors, space-efficient for sparse "
        "graphs) or an **adjacency matrix** (2D grid, O(1) edge lookup, O(V²) space)."
    ),
    "why": (
        "Graphs model networks of every kind: social connections, maps/roads, the web, dependencies, "
        "state machines. Most 'find a path / reach / connect / order' problems are graph problems in "
        "disguise."
    ),
    "concepts": [
        ("Vertex / edge", "Nodes and the connections between them."),
        ("Directed vs undirected", "One-way edges vs symmetric connections."),
        ("Weighted", "Edges carry a cost/distance."),
        ("Adjacency list", "dict {node: [neighbors]} — great for sparse graphs."),
        ("Adjacency matrix", "matrix[i][j] = edge — O(1) lookup, O(V²) space."),
        ("Degree", "Number of edges at a vertex (in/out for directed)."),
    ],
    "examples": [
        ("Build a graph as an adjacency list", r'''
from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)     # undirected -> both ways

    def neighbors(self, u):
        return self.adj[u]

    def __str__(self):
        return "\n".join(f"{n}: {nbrs}" for n, nbrs in self.adj.items())

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
print(g)
print("neighbors of A:", g.neighbors("A"))   # ['B', 'C']
'''),
        ("Adjacency list vs adjacency matrix", r'''
# Same graph, two representations
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
n = 4

# Adjacency list
adj_list = {i: [] for i in range(n)}
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
print("list  :", adj_list)

# Adjacency matrix
matrix = [[0] * n for _ in range(n)]
for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1
print("matrix:")
for row in matrix:
    print(" ", row)

# O(1) edge lookup with a matrix
print("edge 0-3?", bool(matrix[0][3]))   # False
print("edge 2-3?", bool(matrix[2][3]))   # True
'''),
        ("Weighted graph and degree counting", r'''
from collections import defaultdict

# Weighted adjacency list: node -> list of (neighbor, weight)
graph = defaultdict(list)
roads = [("A", "B", 5), ("A", "C", 2), ("B", "C", 1), ("C", "D", 7)]
for u, v, w in roads:
    graph[u].append((v, w))
    graph[v].append((u, w))

for node in ["A", "B", "C", "D"]:
    print(f"{node}: {graph[node]}")

# Degree = number of edges touching a node
print("degree of C:", len(graph["C"]))   # 3

# Total weight of all unique edges
total = sum(w for _, _, w in roads)
print("total road length:", total)       # 15
'''),
    ],
    "gotchas": [
        "Undirected edges must be added in BOTH directions — forgetting one breaks traversal.",
        "Adjacency matrix uses O(V²) memory; wasteful for sparse graphs (use a list instead).",
        "`defaultdict(list)` avoids KeyError, but reading a missing node CREATES an empty entry.",
        "Self-loops and parallel/duplicate edges may need explicit handling depending on the problem.",
        "Directed graphs: in-degree ≠ out-degree; don't assume edges are symmetric.",
    ],
    "exercises": [
        ("Build an adjacency list for edges (1,2),(1,3),(2,3).", "dict of lists.",
         r'''from collections import defaultdict
adj = defaultdict(list)
for u, v in [(1, 2), (1, 3), (2, 3)]:
    adj[u].append(v); adj[v].append(u)
print(dict(adj))  # {1:[2,3],2:[1,3],3:[1,2]}'''),
        ("Count the degree of node 1 in that graph.", "len(neighbors).",
         r'''from collections import defaultdict
adj = defaultdict(list)
for u, v in [(1, 2), (1, 3), (2, 3)]:
    adj[u].append(v); adj[v].append(u)
print(len(adj[1]))  # 2'''),
        ("Build a 3x3 adjacency matrix for edges (0,1),(1,2).", "2D list of 0/1.",
         r'''n = 3
m = [[0] * n for _ in range(n)]
for u, v in [(0, 1), (1, 2)]:
    m[u][v] = 1; m[v][u] = 1
for row in m: print(row)'''),
        ("Check whether edge (0,2) exists in the matrix above.", "Index lookup.",
         r'''n = 3
m = [[0] * n for _ in range(n)]
for u, v in [(0, 1), (1, 2)]:
    m[u][v] = 1; m[v][u] = 1
print(bool(m[0][2]))  # False'''),
        ("Build a DIRECTED graph and list out-neighbors of A: A->B, A->C, B->C.", "One direction only.",
         r'''from collections import defaultdict
g = defaultdict(list)
for u, v in [("A", "B"), ("A", "C"), ("B", "C")]:
    g[u].append(v)
print(g["A"])  # ['B', 'C']'''),
        ("Find all nodes in a graph (the vertex set).", "Collect keys + neighbors.",
         r'''edges = [(1, 2), (2, 3), (4, 5)]
nodes = set()
for u, v in edges:
    nodes.add(u); nodes.add(v)
print(sorted(nodes))  # [1, 2, 3, 4, 5]'''),
        ("Detect whether the undirected graph {1:[2],2:[1,3],3:[2]} has a node of degree 2.", "Scan degrees.",
         r'''graph = {1: [2], 2: [1, 3], 3: [2]}
print(any(len(nbrs) == 2 for nbrs in graph.values()))  # True'''),
        ("Convert an edge list [(0,1),(1,2),(0,2)] to an adjacency-list string.", "Format dict.",
         r'''from collections import defaultdict
adj = defaultdict(list)
for u, v in [(0, 1), (1, 2), (0, 2)]:
    adj[u].append(v); adj[v].append(u)
for node in sorted(adj):
    print(node, "->", adj[node])'''),
    ],
}

CONTENT["bfs-and-dfs"] = {
    "what": (
        "**BFS** (breadth-first search) and **DFS** (depth-first search) are the two ways to explore "
        "a graph. BFS uses a **queue** to fan out level by level — it finds the **shortest path in "
        "an unweighted graph**. DFS uses a **stack** (or recursion) to plunge deep before "
        "backtracking — great for cycle detection, topological sort, and connectivity. Both are "
        "**O(V + E)** and need a **visited** set to avoid loops."
    ),
    "why": (
        "These two traversals underlie a huge fraction of graph algorithms: shortest paths, "
        "connected components, maze solving, dependency resolution, flood fill. Master them and most "
        "graph problems become approachable."
    ),
    "concepts": [
        ("BFS = queue", "Explore nearest-first; shortest path in unweighted graphs."),
        ("DFS = stack/recursion", "Explore deepest-first; natural for backtracking."),
        ("visited set", "Mark nodes seen so you never revisit (prevents infinite loops)."),
        ("O(V + E)", "Each vertex and edge is processed once."),
        ("Shortest path", "BFS layer count = fewest edges from the source."),
        ("Components", "Run a traversal from each unvisited node to count islands."),
    ],
    "examples": [
        ("BFS and DFS on the same graph", r'''
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"], "E": ["B", "F"], "F": ["C", "E"],
}

def bfs(start):
    visited, order = {start}, []
    q = deque([start])
    while q:
        node = q.popleft()           # FIFO -> nearest first
        order.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)
    return order

def dfs(start, visited=None, order=None):
    if visited is None: visited, order = set(), []
    visited.add(start); order.append(start)
    for nbr in graph[start]:
        if nbr not in visited:
            dfs(nbr, visited, order)
    return order

print("BFS:", bfs("A"))   # A B C D E F
print("DFS:", dfs("A"))   # A B D E F C
'''),
        ("BFS finds the shortest (fewest-edge) path", r'''
from collections import deque

graph = {
    1: [2, 3], 2: [1, 4], 3: [1, 4, 5],
    4: [2, 3, 6], 5: [3, 6], 6: [4, 5],
}

def shortest_path(start, goal):
    q = deque([[start]])             # queue of PATHS
    visited = {start}
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal:
            return path              # first time we reach goal = shortest
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(path + [nbr])
    return None

print(shortest_path(1, 6))   # [1, 3, 5, 6] or [1, 2, 4, 6] (length 4)
'''),
        ("Iterative DFS and counting connected components", r'''
def dfs_iter(graph, start):
    visited, order = set(), []
    stack = [start]
    while stack:
        node = stack.pop()           # LIFO -> go deep
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nbr in reversed(graph[node]):   # reversed = natural order
            if nbr not in visited:
                stack.append(nbr)
    return order

graph = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3], 5: []}
print("DFS from 0:", dfs_iter(graph, 0))   # [0, 1, 2]

def count_components(graph):
    seen, count = set(), 0
    for node in graph:
        if node not in seen:
            count += 1
            for v in dfs_iter(graph, node):  # mark the whole component
                seen.add(v)
    return count

print("components:", count_components(graph))   # 3  ({0,1,2},{3,4},{5})
'''),
    ],
    "gotchas": [
        "Without a `visited` set, cycles make traversal loop forever.",
        "BFS gives the shortest path ONLY in unweighted graphs — use Dijkstra when edges have weights.",
        "Mark a node visited when you ENQUEUE it (BFS), not when you dequeue, or you add duplicates.",
        "Recursive DFS can hit the recursion limit on deep/large graphs — switch to an explicit stack.",
        "BFS uses a queue (popleft); using pop() turns it into DFS and breaks shortest-path guarantees.",
    ],
    "exercises": [
        ("BFS-traverse {A:[B,C],B:[D],C:[],D:[]} from A.", "Queue + visited.",
         r'''from collections import deque
g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
def bfs(s):
    seen, out, q = {s}, [], deque([s])
    while q:
        n = q.popleft(); out.append(n)
        for x in g[n]:
            if x not in seen: seen.add(x); q.append(x)
    return out
print(bfs("A"))  # ['A','B','C','D']'''),
        ("DFS-traverse the same graph recursively.", "Recurse neighbors.",
         r'''g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
def dfs(n, seen=None, out=None):
    if seen is None: seen, out = set(), []
    seen.add(n); out.append(n)
    for x in g[n]:
        if x not in seen: dfs(x, seen, out)
    return out
print(dfs("A"))  # ['A','B','D','C']'''),
        ("Check if node D is reachable from A.", "Traverse and test membership.",
         r'''g = {"A": ["B"], "B": ["C"], "C": ["D"], "D": []}
def reachable(s, t):
    seen, stack = set(), [s]
    while stack:
        n = stack.pop()
        if n == t: return True
        seen.add(n)
        stack += [x for x in g[n] if x not in seen]
    return False
print(reachable("A", "D"))  # True'''),
        ("Find the shortest path length from 1 to 4 in {1:[2,3],2:[4],3:[4],4:[]}.", "BFS depth.",
         r'''from collections import deque
g = {1: [2, 3], 2: [4], 3: [4], 4: []}
def dist(s, t):
    q = deque([(s, 0)]); seen = {s}
    while q:
        n, d = q.popleft()
        if n == t: return d
        for x in g[n]:
            if x not in seen: seen.add(x); q.append((x, d + 1))
    return -1
print(dist(1, 4))  # 2'''),
        ("Count connected components in {0:[1],1:[0],2:[],3:[4],4:[3]}.", "Traverse from each.",
         r'''g = {0: [1], 1: [0], 2: [], 3: [4], 4: [3]}
def components(g):
    seen, count = set(), 0
    for start in g:
        if start in seen: continue
        count += 1; stack = [start]
        while stack:
            n = stack.pop(); seen.add(n)
            stack += [x for x in g[n] if x not in seen]
    return count
print(components(g))  # 3'''),
        ("Detect a cycle in an undirected graph {0:[1],1:[0,2],2:[1,0]}.", "Track parent.",
         r'''g = {0: [1, 2], 1: [0, 2], 2: [1, 0]}
def has_cycle(g):
    seen = set()
    def dfs(n, parent):
        seen.add(n)
        for x in g[n]:
            if x not in seen:
                if dfs(x, n): return True
            elif x != parent:
                return True
        return False
    return any(dfs(n, -1) for n in g if n not in seen)
print(has_cycle(g))  # True'''),
        ("Flood-fill a grid: count cells reachable from (0,0) that equal 1.", "DFS on a matrix.",
         r'''grid = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
def flood(r, c):
    if not (0 <= r < 3 and 0 <= c < 3) or grid[r][c] != 1:
        return 0
    grid[r][c] = 2                # mark visited
    return 1 + flood(r+1, c) + flood(r-1, c) + flood(r, c+1) + flood(r, c-1)
print(flood(0, 0))  # 3'''),
        ("Return BFS levels (list of lists) of {A:[B,C],B:[D],C:[D],D:[]} from A.", "Process per level.",
         r'''from collections import deque
g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
def levels(s):
    seen, out, q = {s}, [], deque([s])
    while q:
        row = []
        for _ in range(len(q)):
            n = q.popleft(); row.append(n)
            for x in g[n]:
                if x not in seen: seen.add(x); q.append(x)
        out.append(row)
    return out
print(levels("A"))  # [['A'], ['B','C'], ['D']]'''),
    ],
}

CONTENT["recursion-and-backtracking"] = {
    "what": (
        "**Recursion** solves a problem by calling itself on smaller inputs until a **base case**. "
        "**Backtracking** is recursion that **builds candidates incrementally and undoes** (backs "
        "out of) choices that can't lead to a solution — a systematic DFS over the space of "
        "possibilities. It's the engine behind permutations, combinations, subsets, N-Queens, "
        "Sudoku, and maze solving."
    ),
    "why": (
        "Backtracking turns 'try every valid arrangement' into clean recursive code with pruning. "
        "It's a staple of interviews and the natural tool whenever you must enumerate or search "
        "combinatorial choices."
    ),
    "concepts": [
        ("Base case", "The smallest input you answer directly — stops the recursion."),
        ("Recursive case", "Reduce toward the base case and combine sub-results."),
        ("Choose / explore / un-choose", "Make a choice, recurse, then undo it."),
        ("Pruning", "Abandon a branch early when it can't possibly work."),
        ("State", "Pass partial solutions down (path) and collect complete ones."),
        ("Exponential space", "Permutations/subsets grow fast — backtracking searches smartly."),
    ],
    "examples": [
        ("Subsets and permutations by backtracking", r'''
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])           # record current subset
        for i in range(start, len(nums)):
            path.append(nums[i])         # choose
            backtrack(i + 1, path)       # explore
            path.pop()                   # un-choose (backtrack)
    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

def permutations(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:                # base case: nothing left to place
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], nums)
    return result

print(permutations([1, 2, 3]))   # 6 permutations
'''),
        ("Generate balanced parentheses (with pruning)", r'''
def generate_parens(n):
    result = []
    def backtrack(path, open_count, close_count):
        if len(path) == 2 * n:           # used all n pairs
            result.append("".join(path))
            return
        if open_count < n:               # can still open
            path.append("("); backtrack(path, open_count + 1, close_count); path.pop()
        if close_count < open_count:     # only close if it stays valid (pruning)
            path.append(")"); backtrack(path, open_count, close_count + 1); path.pop()
    backtrack([], 0, 0)
    return result

print(generate_parens(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
'''),
        ("N-Queens: count solutions with backtracking + pruning", r'''
def solve_n_queens(n):
    solutions = []
    cols, diag1, diag2 = set(), set(), set()   # attacked columns/diagonals

    def backtrack(row, placement):
        if row == n:                     # placed a queen in every row
            solutions.append(placement[:])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue                 # pruning: square is attacked
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            placement.append(col)
            backtrack(row + 1, placement)
            cols.discard(col); diag1.discard(row - col); diag2.discard(row + col)
            placement.pop()              # backtrack

    backtrack(0, [])
    return solutions

sols = solve_n_queens(4)
print("4-Queens solutions:", len(sols))   # 2
print("one solution (col per row):", sols[0])   # e.g. [1, 3, 0, 2]
'''),
    ],
    "gotchas": [
        "Append a COPY (`path[:]`) when recording results — appending the live list records mutations.",
        "Always undo your choice (`path.pop()`) after recursing, or state leaks across branches.",
        "Missing/incorrect base case → infinite recursion and RecursionError.",
        "Without pruning, backtracking explores exponentially many dead branches — add checks early.",
        "Default mutable arguments (`def f(path=[])`) are shared across calls — pass state explicitly.",
    ],
    "exercises": [
        ("Compute factorial(5) recursively.", "n * factorial(n-1).",
         r'''def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))  # 120'''),
        ("Generate all subsets of [1,2].", "Choose/skip each.",
         r'''def subsets(nums):
    out = []
    def bt(i, path):
        if i == len(nums):
            out.append(path[:]); return
        bt(i + 1, path)               # skip
        path.append(nums[i]); bt(i + 1, path); path.pop()  # take
    bt(0, [])
    return out
print(subsets([1, 2]))  # [[], [2], [1], [1,2]]'''),
        ("Generate all permutations of 'ab'.", "Place each remaining char.",
         r'''def perms(s):
    if len(s) <= 1: return [s]
    out = []
    for i, c in enumerate(s):
        for p in perms(s[:i] + s[i+1:]):
            out.append(c + p)
    return out
print(perms("ab"))  # ['ab', 'ba']'''),
        ("Sum a nested list [1,[2,[3,4]],5] recursively.", "Recurse into sublists.",
         r'''def deep_sum(x):
    total = 0
    for item in x:
        total += deep_sum(item) if isinstance(item, list) else item
    return total
print(deep_sum([1, [2, [3, 4]], 5]))  # 15'''),
        ("Count the ways to climb n=4 stairs taking 1 or 2 steps.", "Fib-like recursion.",
         r'''def climb(n):
    if n <= 2: return n
    return climb(n - 1) + climb(n - 2)
print(climb(4))  # 5'''),
        ("Generate all combinations of 2 from [1,2,3].", "Start index advances.",
         r'''def combos(nums, k):
    out = []
    def bt(start, path):
        if len(path) == k:
            out.append(path[:]); return
        for i in range(start, len(nums)):
            path.append(nums[i]); bt(i + 1, path); path.pop()
    bt(0, [])
    return out
print(combos([1, 2, 3], 2))  # [[1,2],[1,3],[2,3]]'''),
        ("Solve: can subset of [3,34,4,12] sum to 9? (subset-sum)", "Include/exclude recursion.",
         r'''def subset_sum(nums, target, i=0):
    if target == 0: return True
    if i >= len(nums) or target < 0: return False
    return (subset_sum(nums, target - nums[i], i + 1) or
            subset_sum(nums, target, i + 1))
print(subset_sum([3, 34, 4, 12], 9))  # False'''),
        ("Find all root-to-leaf paths summing to 8 in a small tree.", "Carry path + remaining sum.",
         r'''class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(5); root.left = N(3); root.right = N(3)
root.left.left = N(0)        # 5+3+0 = 8
def paths(node, target, path, out):
    if node is None: return
    path.append(node.value)
    if not node.left and not node.right and sum(path) == target:
        out.append(path[:])
    paths(node.left, target, path, out)
    paths(node.right, target, path, out)
    path.pop()
out = []; paths(root, 8, [], out); print(out)  # [[5, 3, 0]]'''),
    ],
}

CONTENT["two-pointers-and-sliding-window"] = {
    "what": (
        "**Two pointers** uses two indices that move through a sequence — toward each other (from "
        "both ends) or in the same direction (fast/slow) — to solve problems in O(n) that would be "
        "O(n²) with nested loops. A **sliding window** is a two-pointer pattern where a contiguous "
        "range `[left, right]` grows and shrinks to satisfy a constraint (longest/shortest "
        "subarray, sums, distinct counts)."
    ),
    "why": (
        "These patterns turn many array/string problems from quadratic to linear. Recognizing 'pair "
        "summing to target', 'longest substring with…', or 'subarray of size k' as two-pointer/"
        "window problems is a huge interview and performance win."
    ),
    "concepts": [
        ("Opposite ends", "left=0, right=n-1 moving inward (sorted-pair sums, palindromes)."),
        ("Fast/slow", "Same direction at different speeds (cycle detection, dedup)."),
        ("Fixed window", "A window of constant size k slides across the array."),
        ("Variable window", "Grow right; shrink left until the constraint holds again."),
        ("Window state", "Maintain a running sum/count/dict as the window moves."),
        ("O(n)", "Each pointer moves forward at most n times total."),
    ],
    "examples": [
        ("Two pointers from both ends (sorted two-sum)", r'''
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1            # need a bigger sum -> move left up
        else:
            right -= 1           # need a smaller sum -> move right down
    return None

print(two_sum_sorted([1, 2, 4, 7, 11, 15], 15))   # (3, 4) -> 4 + 11
print(two_sum_sorted([2, 3, 4], 6))               # (0, 2) -> 2 + 4
'''),
        ("Fixed-size sliding window (max sum of k)", r'''
def max_sum_window(arr, k):
    window = sum(arr[:k])        # first window
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]   # add new, drop old -> O(1) slide
        best = max(best, window)
    return best

print(max_sum_window([2, 1, 5, 1, 3, 2], 3))   # 9  (5+1+3)
print(max_sum_window([1, 1, 1, 1], 2))         # 2
'''),
        ("Variable sliding window (longest substring no repeats)", r'''
def longest_unique(s):
    seen = {}                    # char -> last index
    left = best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1  # shrink window past the duplicate
        seen[ch] = right
        best = max(best, right - left + 1)
    return best

print(longest_unique("abcabcbb"))   # 3  ("abc")
print(longest_unique("bbbbb"))      # 1
print(longest_unique("pwwkew"))     # 3  ("wke")

# Smallest subarray with sum >= target
def min_subarray_len(target, nums):
    left = total = 0
    best = float("inf")
    for right, x in enumerate(nums):
        total += x
        while total >= target:          # shrink while still valid
            best = min(best, right - left + 1)
            total -= nums[left]; left += 1
    return 0 if best == float("inf") else best

print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))   # 2  ([4,3])
'''),
    ],
    "gotchas": [
        "Two-pointer-from-ends needs SORTED data; on unsorted input it gives wrong answers.",
        "Slide the window in O(1) (add new, subtract old) — recomputing the sum makes it O(n·k).",
        "For variable windows, shrink with a `while` (not `if`) so the constraint is fully restored.",
        "Off-by-one in window length: it's `right - left + 1`, not `right - left`.",
        "Update window state (dict/sum) consistently when BOTH adding right and removing left.",
    ],
    "exercises": [
        ("Check if 'racecar' is a palindrome with two pointers.", "Compare ends inward.",
         r'''def is_pal(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]: return False
        i += 1; j -= 1
    return True
print(is_pal("racecar"))  # True'''),
        ("Find a pair in sorted [1,3,5,7] summing to 8.", "Move pointers by sum.",
         r'''def pair(a, t):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == t: return (a[i], a[j])
        if s < t: i += 1
        else: j -= 1
a = [1, 3, 5, 7]
print(pair(a, 8))  # (1, 7) or (3, 5) -> (1, 7)'''),
        ("Max sum of any 2 consecutive elements in [1,4,2,10,2].", "Window of size 2.",
         r'''def max2(a):
    best = a[0] + a[1]
    for i in range(2, len(a)):
        best = max(best, a[i] + a[i - 1])
    return best
print(max2([1, 4, 2, 10, 2]))  # 12'''),
        ("Remove duplicates in-place from sorted [1,1,2,3,3] (return new length).", "Slow/fast pointers.",
         r'''def dedup(a):
    if not a: return 0
    slow = 0
    for fast in range(1, len(a)):
        if a[fast] != a[slow]:
            slow += 1; a[slow] = a[fast]
    return slow + 1
print(dedup([1, 1, 2, 3, 3]))  # 3'''),
        ("Longest substring without repeats in 'abba'.", "Variable window + last-seen map.",
         r'''def longest(s):
    seen = {}; left = best = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = r
        best = max(best, r - left + 1)
    return best
print(longest("abba"))  # 2'''),
        ("Count subarrays of [1,2,3] with sum exactly 3.", "Sliding window on positives.",
         r'''def count_sum(a, target):
    left = total = count = 0
    for right in range(len(a)):
        total += a[right]
        while total > target and left <= right:
            total -= a[left]; left += 1
        if total == target: count += 1
    return count
print(count_sum([1, 2, 3], 3))  # 2  ([1,2] and [3])'''),
        ("Move all zeros to the end of [0,1,0,3,12] in place.", "Slow pointer for non-zeros.",
         r'''def move_zeros(a):
    slow = 0
    for fast in range(len(a)):
        if a[fast] != 0:
            a[slow], a[fast] = a[fast], a[slow]; slow += 1
    return a
print(move_zeros([0, 1, 0, 3, 12]))  # [1,3,12,0,0]'''),
        ("Find the smallest window in [2,3,1,2,4,3] with sum >= 7.", "Shrink-from-left window.",
         r'''def min_window(target, a):
    left = total = 0; best = float("inf")
    for right in range(len(a)):
        total += a[right]
        while total >= target:
            best = min(best, right - left + 1)
            total -= a[left]; left += 1
    return 0 if best == float("inf") else best
print(min_window(7, [2, 3, 1, 2, 4, 3]))  # 2'''),
    ],
}

CONTENT["greedy-algorithms"] = {
    "what": (
        "A **greedy algorithm** builds a solution one step at a time, always taking the choice that "
        "looks best **right now** (a local optimum), hoping it leads to a global optimum. When the "
        "problem has the **greedy-choice property** and **optimal substructure**, greedy is both "
        "correct and fast — often O(n log n) (a sort) plus one pass. When it doesn't, greedy gives a "
        "wrong answer and you need DP."
    ),
    "why": (
        "Greedy solves classic problems optimally and quickly: interval scheduling, Huffman coding, "
        "Dijkstra/Prim/Kruskal, coin change (canonical systems), fractional knapsack. Knowing when "
        "greedy IS and ISN'T valid is a key algorithmic skill."
    ),
    "concepts": [
        ("Greedy choice", "Pick the locally optimal option at each step."),
        ("Optimal substructure", "An optimal solution contains optimal sub-solutions."),
        ("Sort first", "Most greedy algorithms start by sorting by some key."),
        ("Exchange argument", "Prove correctness by showing swaps never hurt."),
        ("When it fails", "0/1 knapsack, general coin change — greedy can be suboptimal."),
        ("Speed", "Usually O(n log n) — far faster than exhaustive search or DP."),
    ],
    "examples": [
        ("Activity selection (interval scheduling)", r'''
def max_activities(intervals):
    # Greedy: always take the activity that FINISHES earliest
    intervals.sort(key=lambda x: x[1])      # sort by end time
    chosen = []
    last_end = float("-inf")
    for start, end in intervals:
        if start >= last_end:               # no overlap -> take it
            chosen.append((start, end))
            last_end = end
    return chosen

acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
result = max_activities(acts)
print("count:", len(result))    # 4
print(result)                   # [(1,4),(5,7),(8,11)] (+one more)
'''),
        ("Coin change (greedy works for canonical coins)", r'''
def greedy_coins(amount, coins):
    coins = sorted(coins, reverse=True)     # biggest first
    used = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            used.append(coin)
    return used if amount == 0 else None

print(greedy_coins(63, [25, 10, 5, 1]))   # [25, 25, 10, 1, 1, 1]
print("coins used:", len(greedy_coins(63, [25, 10, 5, 1])))   # 6

# WARNING: greedy can FAIL on non-canonical coin sets:
# amount=6, coins=[1,3,4] -> greedy gives 4+1+1 (3 coins),
# but optimal is 3+3 (2 coins). Use DP there.
'''),
        ("Fractional knapsack (greedy by value/weight ratio)", r'''
def fractional_knapsack(capacity, items):
    # items: list of (value, weight); we may take FRACTIONS
    items = sorted(items, key=lambda it: it[0] / it[1], reverse=True)
    total = 0.0
    for value, weight in items:
        if capacity >= weight:
            capacity -= weight              # take all of it
            total += value
        else:
            total += value * (capacity / weight)   # take the fraction
            break
    return total

items = [(60, 10), (100, 20), (120, 30)]   # (value, weight)
print(fractional_knapsack(50, items))      # 240.0
'''),
    ],
    "gotchas": [
        "Greedy is NOT always optimal — prove the greedy-choice property or you'll get wrong answers.",
        "0/1 knapsack and general coin change need DP, not greedy.",
        "Most greedy algorithms depend on sorting by the RIGHT key — choosing the wrong key fails.",
        "Activity selection sorts by END time, not start time or duration — a classic mistake.",
        "Fractional knapsack allows fractions; the 0/1 version (whole items only) is a different, harder problem.",
    ],
    "exercises": [
        ("Make change for 41 with coins [25,10,5,1], fewest coins.", "Biggest first.",
         r'''def change(amount, coins):
    coins = sorted(coins, reverse=True); used = []
    for c in coins:
        while amount >= c:
            amount -= c; used.append(c)
    return used
print(change(41, [25, 10, 5, 1]))  # [25, 10, 5, 1]'''),
        ("Select the max non-overlapping intervals from [(1,3),(2,4),(3,5)].", "Sort by end.",
         r'''def select(iv):
    iv.sort(key=lambda x: x[1]); out = []; end = float("-inf")
    for s, e in iv:
        if s >= end: out.append((s, e)); end = e
    return out
print(select([(1, 3), (2, 4), (3, 5)]))  # [(1,3),(3,5)]'''),
        ("Given [1,3,4] coins, show greedy is NOT optimal for amount 6.", "Compare counts.",
         r'''#md
Greedy takes 4 then 1+1 = **3 coins**. The optimal is 3+3 = **2 coins**. Because
this coin set isn't canonical, greedy fails and you must use **dynamic
programming** for the true minimum.'''),
        ("Maximize value in fractional knapsack: cap=10, items=[(60,10),(100,20)].", "Ratio sort.",
         r'''def knap(cap, items):
    items.sort(key=lambda it: it[0] / it[1], reverse=True)
    total = 0
    for v, w in items:
        take = min(w, cap); total += v * (take / w); cap -= take
        if cap == 0: break
    return total
print(knap(10, [(60, 10), (100, 20)]))  # 60.0'''),
        ("Assign the fewest meeting rooms for [(0,30),(5,10),(15,20)].", "Sort starts/ends.",
         r'''def min_rooms(meetings):
    starts = sorted(m[0] for m in meetings)
    ends = sorted(m[1] for m in meetings)
    rooms = used = 0; i = j = 0
    while i < len(starts):
        if starts[i] < ends[j]:
            used += 1; i += 1; rooms = max(rooms, used)
        else:
            used -= 1; j += 1
    return rooms
print(min_rooms([(0, 30), (5, 10), (15, 20)]))  # 2'''),
        ("Find the minimum number of jumps to reach the end of [2,3,1,1,4].", "Greedy farthest reach.",
         r'''def jumps(a):
    jumps = end = farthest = 0
    for i in range(len(a) - 1):
        farthest = max(farthest, i + a[i])
        if i == end:
            jumps += 1; end = farthest
    return jumps
print(jumps([2, 3, 1, 1, 4]))  # 2'''),
        ("Buy/sell stock for max profit with many transactions: [7,1,5,3,6,4].", "Sum upward steps.",
         r'''def max_profit(prices):
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
print(max_profit([7, 1, 5, 3, 6, 4]))  # 7'''),
        ("Arrange [3,30,34,5,9] to form the largest number string.", "Custom comparator.",
         r'''from functools import cmp_to_key
def largest(nums):
    s = list(map(str, nums))
    s.sort(key=cmp_to_key(lambda a, b: (a + b < b + a) - (a + b > b + a)))
    return "".join(s)
print(largest([3, 30, 34, 5, 9]))  # 9534330'''),
    ],
}

CONTENT["divide-and-conquer"] = {
    "what": (
        "**Divide and conquer** solves a problem by (1) **dividing** it into smaller subproblems of "
        "the same type, (2) **conquering** them recursively, and (3) **combining** their answers. "
        "Merge sort, quick sort, binary search, fast exponentiation, and Karatsuba multiplication "
        "all follow this template. The cost is captured by a **recurrence** like T(n) = 2T(n/2) + "
        "O(n)."
    ),
    "why": (
        "It's a fundamental design paradigm that yields elegant O(n log n) and O(log n) algorithms, "
        "and it parallelizes naturally. Recognizing a problem as 'split, solve halves, merge' is a "
        "powerful, reusable mental model."
    ),
    "concepts": [
        ("Divide", "Break the input into smaller subproblems (often halves)."),
        ("Conquer", "Solve each subproblem recursively (base case stops it)."),
        ("Combine", "Merge sub-answers into the full answer."),
        ("Recurrence", "T(n) = a·T(n/b) + f(n) describes the running time."),
        ("Master theorem", "A formula to solve common divide-and-conquer recurrences."),
        ("Examples", "Merge/quick sort, binary search, power, maximum subarray."),
    ],
    "examples": [
        ("Fast exponentiation in O(log n)", r'''
def power(base, exp):
    if exp == 0:                  # base case
        return 1
    half = power(base, exp // 2)  # conquer once, reuse
    if exp % 2 == 0:
        return half * half        # combine: x^n = (x^(n/2))^2
    else:
        return half * half * base

print(power(2, 10))   # 1024
print(power(3, 5))    # 243
# Only ~log2(exp) multiplications instead of exp-1.
'''),
        ("Maximum subarray via divide and conquer", r'''
def max_subarray(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo == hi:                  # base case: single element
        return arr[lo]
    mid = (lo + hi) // 2
    left = max_subarray(arr, lo, mid)        # best in left half
    right = max_subarray(arr, mid + 1, hi)   # best in right half

    # best crossing the midpoint
    left_sum = float("-inf"); total = 0
    for i in range(mid, lo - 1, -1):
        total += arr[i]; left_sum = max(left_sum, total)
    right_sum = float("-inf"); total = 0
    for i in range(mid + 1, hi + 1):
        total += arr[i]; right_sum = max(right_sum, total)
    cross = left_sum + right_sum

    return max(left, right, cross)

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
'''),
        ("Count occurrences and find max with divide and conquer", r'''
def find_max(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo == hi:                  # one element
        return arr[lo]
    mid = (lo + hi) // 2
    return max(find_max(arr, lo, mid), find_max(arr, mid + 1, hi))

print(find_max([3, 7, 1, 9, 2, 8]))   # 9

# Karatsuba-style idea: multiply by splitting (shown simply here)
def sum_divide(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    return sum_divide(arr[:mid]) + sum_divide(arr[mid:])

print(sum_divide([1, 2, 3, 4, 5]))    # 15
'''),
    ],
    "gotchas": [
        "Always define a base case (smallest subproblem) or recursion never terminates.",
        "The 'combine' step often dominates the cost — analyze it to get the recurrence right.",
        "Slicing (`arr[:mid]`) copies data; pass lo/hi indices to avoid O(n) copies per call.",
        "Not every split is balanced — lopsided division can degrade O(n log n) to O(n²).",
        "Deep recursion risks stack overflow; consider iterative versions for very large n.",
    ],
    "exercises": [
        ("Compute 2^16 with fast exponentiation.", "Square the half-power.",
         r'''def power(b, e):
    if e == 0: return 1
    half = power(b, e // 2)
    return half * half * (b if e % 2 else 1)
print(power(2, 16))  # 65536'''),
        ("Find the max of [4,2,9,7] using divide and conquer.", "Max of halves.",
         r'''def find_max(a):
    if len(a) == 1: return a[0]
    mid = len(a) // 2
    return max(find_max(a[:mid]), find_max(a[mid:]))
print(find_max([4, 2, 9, 7]))  # 9'''),
        ("Sum [1,2,3,4] by splitting in halves.", "Recurse and add.",
         r'''def s(a):
    if len(a) == 1: return a[0]
    m = len(a) // 2
    return s(a[:m]) + s(a[m:])
print(s([1, 2, 3, 4]))  # 10'''),
        ("Count elements equal to target 2 in [2,1,2,3,2] by divide and conquer.", "Combine counts.",
         r'''def count(a, t):
    if not a: return 0
    if len(a) == 1: return 1 if a[0] == t else 0
    m = len(a) // 2
    return count(a[:m], t) + count(a[m:], t)
print(count([2, 1, 2, 3, 2], 2))  # 3'''),
        ("State the recurrence for merge sort.", "Two halves plus a merge.",
         r'''#md
**T(n) = 2·T(n/2) + O(n)** — two subproblems of half the size, plus O(n) to merge.
By the master theorem this solves to **O(n log n)**.'''),
        ("Compute the number of digits of 12345 by repeatedly halving? No — count via // 10.", "Recursive count.",
         r'''def digits(n):
    return 1 if n < 10 else 1 + digits(n // 10)
print(digits(12345))  # 5'''),
        ("Multiply two numbers using recursion (a*b = a + a*(b-1)).", "Linear recursion.",
         r'''def mult(a, b):
    if b == 0: return 0
    return a + mult(a, b - 1)
print(mult(6, 7))  # 42'''),
        ("Find both min and max of [3,1,4,1,5] in one divide-and-conquer pass.", "Return a pair.",
         r'''def min_max(a, lo=0, hi=None):
    if hi is None: hi = len(a) - 1
    if lo == hi: return a[lo], a[lo]
    mid = (lo + hi) // 2
    lmin, lmax = min_max(a, lo, mid)
    rmin, rmax = min_max(a, mid + 1, hi)
    return min(lmin, rmin), max(lmax, rmax)
print(min_max([3, 1, 4, 1, 5]))  # (1, 5)'''),
    ],
}

CONTENT["dynamic-programming"] = {
    "what": (
        "**Dynamic programming (DP)** solves problems with **overlapping subproblems** and "
        "**optimal substructure** by solving each subproblem **once** and storing the result. Two "
        "styles: **top-down memoization** (recursion + a cache) and **bottom-up tabulation** "
        "(fill a table iteratively). DP turns exponential brute force into polynomial time — e.g. "
        "naive Fibonacci O(2ⁿ) becomes O(n)."
    ),
    "why": (
        "DP is the heavyweight technique for optimization and counting problems: knapsack, edit "
        "distance, longest common subsequence, coin change, path counting. It's notoriously common "
        "in interviews and powers real systems (diff tools, spell-checkers, bioinformatics)."
    ),
    "concepts": [
        ("Overlapping subproblems", "The same sub-answer is needed many times."),
        ("Optimal substructure", "Optimal answer builds from optimal sub-answers."),
        ("Memoization", "Top-down recursion that caches results (`@lru_cache`)."),
        ("Tabulation", "Bottom-up: fill a DP table from base cases upward."),
        ("State & transition", "Define what dp[i] means and how it builds from earlier states."),
        ("Space optimization", "Often only the last row/few values are needed."),
    ],
    "examples": [
        ("Fibonacci: naive vs memoized vs tabulated", r'''
from functools import lru_cache

# Memoized (top-down) — O(n)
@lru_cache(maxsize=None)
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# Tabulated (bottom-up) — O(n) time, O(1) space
def fib_tab(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print([fib_memo(i) for i in range(10)])   # 0..34
print("fib(50) =", fib_tab(50))           # 12586269025
'''),
        ("Coin change: fewest coins (bottom-up DP)", r'''
def coin_change(coins, amount):
    # dp[x] = fewest coins to make x; INF means impossible
    INF = float("inf")
    dp = [0] + [INF] * amount
    for x in range(1, amount + 1):
        for coin in coins:
            if coin <= x and dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
    return dp[amount] if dp[amount] != INF else -1

print(coin_change([1, 3, 4], 6))    # 2  (3 + 3) -> greedy would say 3!
print(coin_change([2], 3))          # -1 (impossible)
print(coin_change([1, 2, 5], 11))   # 3  (5 + 5 + 1)
'''),
        ("0/1 knapsack and longest common subsequence", r'''
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][c] = best value using first i items with capacity c
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]                    # skip item i
            if weights[i - 1] <= c:                    # or take it
                dp[i][c] = max(dp[i][c],
                               dp[i - 1][c - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]

print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))   # 9

def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(lcs("ABCBDAB", "BDCAB"))   # 4  ("BCAB")
'''),
    ],
    "gotchas": [
        "DP needs BOTH overlapping subproblems and optimal substructure — otherwise use greedy/D&C.",
        "Define your state precisely (what dp[i] MEANS) before writing the transition.",
        "Initialize base cases correctly — a wrong dp[0] poisons the whole table.",
        "Watch index off-by-ones: dp tables are often sized n+1 with a 1-based shift.",
        "Memoize on hashable args; `@lru_cache` won't work if you pass lists/dicts as arguments.",
    ],
    "exercises": [
        ("Compute fib(10) with memoization.", "Cache recursive calls.",
         r'''from functools import lru_cache
@lru_cache(None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(10))  # 55'''),
        ("Count ways to climb 5 stairs taking 1 or 2 steps (DP).", "dp[i]=dp[i-1]+dp[i-2].",
         r'''def climb(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(climb(5))  # 8'''),
        ("Fewest coins to make 6 from [1,3,4].", "Bottom-up min.",
         r'''def coin(coins, amt):
    dp = [0] + [float("inf")] * amt
    for x in range(1, amt + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amt]
print(coin([1, 3, 4], 6))  # 2'''),
        ("Longest common subsequence of 'abcde' and 'ace'.", "2D table.",
         r'''def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = (dp[i-1][j-1] + 1 if a[i-1] == b[j-1]
                        else max(dp[i-1][j], dp[i][j-1]))
    return dp[-1][-1]
print(lcs("abcde", "ace"))  # 3'''),
        ("Max sum of non-adjacent elements in [2,7,9,3,1] (house robber).", "Take or skip.",
         r'''def rob(a):
    prev = cur = 0
    for x in a:
        prev, cur = cur, max(cur, prev + x)
    return cur
print(rob([2, 7, 9, 3, 1]))  # 12'''),
        ("Count unique paths in a 3x3 grid (only right/down moves).", "dp[i][j]=up+left.",
         r'''def paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
print(paths(3, 3))  # 6'''),
        ("Edit distance between 'cat' and 'cut'.", "Insert/delete/replace table.",
         r'''def edit(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1]
            else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
print(edit("cat", "cut"))  # 1'''),
        ("Length of the longest increasing subsequence of [10,9,2,5,3,7,101,18].", "O(n^2) DP.",
         r'''def lis(a):
    if not a: return 0
    dp = [1] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4'''),
    ],
}

CONTENT["graph-algorithms"] = {
    "what": (
        "Beyond BFS/DFS, **graph algorithms** solve weighted and structural problems: **Dijkstra's** "
        "shortest path (non-negative weights), **topological sort** (ordering a DAG by dependencies), "
        "**Union-Find** for connectivity, and **minimum spanning trees** (Kruskal/Prim). They combine "
        "traversals with heaps, sorting, and clever bookkeeping."
    ),
    "why": (
        "These are the workhorses of routing (maps, networks), scheduling (build systems, course "
        "prerequisites), clustering, and network design. They appear constantly in real systems and "
        "harder interviews."
    ),
    "concepts": [
        ("Dijkstra", "Shortest paths from a source with a min-heap; non-negative weights only."),
        ("Topological sort", "Linear order of a DAG so every edge points forward."),
        ("Union-Find", "Near-O(1) union/find for connectivity and cycle detection."),
        ("MST", "Cheapest set of edges connecting all nodes (Kruskal/Prim)."),
        ("Relaxation", "Update a node's best-known distance via a neighbor."),
        ("DAG", "Directed acyclic graph — required for topological sort."),
    ],
    "examples": [
        ("Dijkstra's shortest path with a heap", r'''
import heapq

def dijkstra(graph, start):
    # graph: node -> list of (neighbor, weight)
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]                  # (distance, node)
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue                   # stale entry, skip
        for nbr, weight in graph[node]:
            nd = d + weight
            if nd < dist[nbr]:         # relaxation
                dist[nbr] = nd
                heapq.heappush(pq, (nd, nbr))
    return dist

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}
print(dijkstra(graph, "A"))   # {'A':0,'B':1,'C':3,'D':4}
'''),
        ("Topological sort of a DAG (Kahn's algorithm)", r'''
from collections import deque

def topological_sort(graph):
    indegree = {n: 0 for n in graph}
    for n in graph:
        for nbr in graph[n]:
            indegree[nbr] += 1
    # start with all zero-indegree nodes
    q = deque([n for n in graph if indegree[n] == 0])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nbr in graph[node]:
            indegree[nbr] -= 1         # 'remove' the edge
            if indegree[nbr] == 0:
                q.append(nbr)
    return order if len(order) == len(graph) else None   # None = cycle

# course prerequisites: must do 0 before 1 and 2, etc.
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(topological_sort(graph))   # [0, 1, 2, 3]
'''),
        ("Union-Find (Disjoint Set Union)", r'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # each node is its own root
        self.rank = [0] * n

    def find(self, x):                 # with path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):             # union by rank
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False               # already connected (cycle if adding edge)
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

uf = UnionFind(5)
uf.union(0, 1); uf.union(1, 2); uf.union(3, 4)
print(uf.find(0) == uf.find(2))   # True  (0,1,2 connected)
print(uf.find(0) == uf.find(4))   # False (different component)

# Count connected components
roots = {uf.find(i) for i in range(5)}
print("components:", len(roots))  # 2
'''),
    ],
    "gotchas": [
        "Dijkstra requires NON-NEGATIVE weights — use Bellman-Ford if edges can be negative.",
        "Skip stale heap entries (`if d > dist[node]: continue`) or you'll process nodes twice.",
        "Topological sort only works on a DAG; a cycle means no valid ordering (detect it!).",
        "Union-Find without path compression / union by rank degrades toward O(n) per op.",
        "For an unweighted shortest path, plain BFS is enough — Dijkstra is overkill.",
    ],
    "exercises": [
        ("Run Dijkstra from A on A->B(1), B->C(2), A->C(4).", "Relax with a heap.",
         r'''import heapq
g = {"A": [("B", 1), ("C", 4)], "B": [("C", 2)], "C": []}
def dijkstra(g, s):
    dist = {n: float("inf") for n in g}; dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, n = heapq.heappop(pq)
        for nb, w in g[n]:
            if d + w < dist[nb]:
                dist[nb] = d + w; heapq.heappush(pq, (d + w, nb))
    return dist
print(dijkstra(g, "A"))  # {'A':0,'B':1,'C':3}'''),
        ("Topologically sort {0:[1],1:[2],2:[]}.", "Zero-indegree first.",
         r'''from collections import deque
g = {0: [1], 1: [2], 2: []}
def topo(g):
    indeg = {n: 0 for n in g}
    for n in g:
        for m in g[n]: indeg[m] += 1
    q = deque(n for n in g if indeg[n] == 0); out = []
    while q:
        n = q.popleft(); out.append(n)
        for m in g[n]:
            indeg[m] -= 1
            if indeg[m] == 0: q.append(m)
    return out
print(topo(g))  # [0, 1, 2]'''),
        ("Use Union-Find to test if 0 and 3 are connected after union(0,1),(1,3).", "find roots.",
         r'''parent = list(range(4))
def find(x):
    while parent[x] != x: x = parent[x]
    return x
def union(a, b): parent[find(a)] = find(b)
union(0, 1); union(1, 3)
print(find(0) == find(3))  # True'''),
        ("Detect a cycle in a directed graph {0:[1],1:[2],2:[0]}.", "Topo sort fails.",
         r'''from collections import deque
g = {0: [1], 1: [2], 2: [0]}
def has_cycle(g):
    indeg = {n: 0 for n in g}
    for n in g:
        for m in g[n]: indeg[m] += 1
    q = deque(n for n in g if indeg[n] == 0); count = 0
    while q:
        n = q.popleft(); count += 1
        for m in g[n]:
            indeg[m] -= 1
            if indeg[m] == 0: q.append(m)
    return count != len(g)
print(has_cycle(g))  # True'''),
        ("Count connected components of 5 nodes with edges (0,1),(2,3).", "Union then count roots.",
         r'''parent = list(range(5))
def find(x):
    while parent[x] != x: x = parent[x]
    return x
def union(a, b): parent[find(a)] = find(b)
for a, b in [(0, 1), (2, 3)]: union(a, b)
print(len({find(i) for i in range(5)}))  # 3'''),
        ("Find the shortest distance to all nodes from 0 in an unweighted graph with BFS.", "Layer count.",
         r'''from collections import deque
g = {0: [1, 2], 1: [3], 2: [3], 3: []}
def bfs_dist(g, s):
    dist = {s: 0}; q = deque([s])
    while q:
        n = q.popleft()
        for m in g[n]:
            if m not in dist:
                dist[m] = dist[n] + 1; q.append(m)
    return dist
print(bfs_dist(g, 0))  # {0:0,1:1,2:1,3:2}'''),
        ("Build an MST weight with Kruskal on edges (0,1,1),(1,2,2),(0,2,3).", "Sort + union.",
         r'''edges = [(1, 0, 1), (2, 1, 2), (3, 0, 2)]  # (weight,u,v)
parent = list(range(3))
def find(x):
    while parent[x] != x: x = parent[x]
    return x
total = 0
for w, u, v in sorted(edges):
    if find(u) != find(v):
        parent[find(u)] = find(v); total += w
print(total)  # 3'''),
        ("Return a valid course order for prereqs {0:[],1:[0],2:[0,1]}.", "Topo sort.",
         r'''from collections import deque
g = {0: [], 1: [0], 2: [0, 1]}  # node -> prereqs
# Build forward graph
fwd = {n: [] for n in g}; indeg = {n: 0 for n in g}
for n in g:
    for pre in g[n]:
        fwd[pre].append(n); indeg[n] += 1
q = deque(n for n in g if indeg[n] == 0); order = []
while q:
    n = q.popleft(); order.append(n)
    for m in fwd[n]:
        indeg[m] -= 1
        if indeg[m] == 0: q.append(m)
print(order)  # [0, 1, 2]'''),
    ],
}

CONTENT["bit-manipulation"] = {
    "what": (
        "**Bit manipulation** works directly on the binary representation of integers using bitwise "
        "operators: **AND** `&`, **OR** `|`, **XOR** `^`, **NOT** `~`, and **shifts** `<<`/`>>`. "
        "These let you set, clear, toggle, and test individual bits, and unlock fast tricks: "
        "check even/odd, multiply/divide by powers of two, swap without a temp, and use integers as "
        "compact sets (bitmasks)."
    ),
    "why": (
        "Bit tricks give O(1) operations and tiny memory footprints, crucial in low-level code, "
        "graphics, cryptography, and competitive programming. Bitmask DP and subset enumeration "
        "are powerful interview tools."
    ),
    "concepts": [
        ("AND / OR / XOR", "& tests/masks, | sets, ^ toggles/finds differences."),
        ("Shifts", "x << n multiplies by 2ⁿ; x >> n divides by 2ⁿ."),
        ("Get/set/clear bit", "Use masks `1 << i` with &, |, and & ~."),
        ("XOR properties", "x ^ x = 0, x ^ 0 = x — finds the unique unpaired value."),
        ("Bitmask as a set", "Bit i set means element i is present."),
        ("x & (x-1)", "Clears the lowest set bit — counts bits / tests power of two."),
    ],
    "examples": [
        ("Core bitwise operations", r'''
a, b = 0b1100, 0b1010      # 12 and 10
print(bin(a & b))    # 0b1000  AND -> bits set in BOTH (8)
print(bin(a | b))    # 0b1110  OR  -> bits set in EITHER (14)
print(bin(a ^ b))    # 0b0110  XOR -> bits set in exactly one (6)
print(a << 1)        # 24  left shift = multiply by 2
print(a >> 1)        # 6   right shift = integer divide by 2

# Even/odd via the lowest bit
for n in [4, 7, 10, 13]:
    print(n, "is", "odd" if n & 1 else "even")
'''),
        ("Get, set, clear, and toggle a specific bit", r'''
def get_bit(x, i):    return (x >> i) & 1        # is bit i set?
def set_bit(x, i):    return x | (1 << i)        # turn bit i ON
def clear_bit(x, i):  return x & ~(1 << i)       # turn bit i OFF
def toggle_bit(x, i): return x ^ (1 << i)        # flip bit i

x = 0b1010                 # 10
print(get_bit(x, 1))       # 1
print(get_bit(x, 0))       # 0
print(bin(set_bit(x, 0)))  # 0b1011 (11)
print(bin(clear_bit(x, 1)))# 0b1000 (8)
print(bin(toggle_bit(x, 3)))# 0b0010 (2)
'''),
        ("Classic bit tricks", r'''
# Count set bits (Brian Kernighan's algorithm)
def count_bits(x):
    count = 0
    while x:
        x &= x - 1          # clears the lowest set bit each loop
        count += 1
    return count
print(count_bits(0b10110110))   # 5

# Is a power of two? (exactly one bit set)
def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0
print(is_power_of_two(16))   # True
print(is_power_of_two(18))   # False

# Find the single number where every other value appears twice
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n         # pairs cancel out, leaving the unique one
    return result
print(single_number([4, 1, 2, 1, 2]))   # 4

# Swap two numbers without a temporary variable
p, q = 5, 9
p ^= q; q ^= p; p ^= q
print(p, q)                  # 9 5
'''),
    ],
    "gotchas": [
        "Operator precedence: `&`, `|`, `^` bind LOOSER than `==`/`+` — wrap them in parentheses.",
        "Python ints are arbitrary precision; `~x` is `-x-1`, not a fixed-width complement.",
        "Shifting by a negative amount raises ValueError; shifting a negative number sign-extends.",
        "`x & 1` tests odd/even; don't confuse `&` (bitwise) with `and` (logical).",
        "Bitmask indices are 0-based: element i corresponds to `1 << i`, not `1 << (i-1)`.",
    ],
    "exercises": [
        ("Check if 42 is even using a bit operation.", "Lowest bit.",
         r'''n = 42
print(n & 1 == 0)  # True (even)'''),
        ("Set the 3rd bit (index 2) of 0b1001.", "OR with a mask.",
         r'''x = 0b1001
print(bin(x | (1 << 2)))  # 0b1101'''),
        ("Count the number of 1 bits in 29 (0b11101).", "Kernighan or bin().",
         r'''def count(x):
    c = 0
    while x: x &= x - 1; c += 1
    return c
print(count(29))  # 4'''),
        ("Check if 64 is a power of two.", "x & (x-1) == 0.",
         r'''def is_pow2(x):
    return x > 0 and (x & (x - 1)) == 0
print(is_pow2(64))  # True'''),
        ("Find the unique number in [2,3,2,4,4] using XOR.", "Pairs cancel.",
         r'''def unique(a):
    r = 0
    for x in a: r ^= x
    return r
print(unique([2, 3, 2, 4, 4]))  # 3'''),
        ("Multiply 6 by 8 using only a bit shift.", "8 = 2^3.",
         r'''print(6 << 3)  # 48'''),
        ("Toggle the lowest bit of 0b1011 and print the result.", "XOR with 1.",
         r'''x = 0b1011
print(bin(x ^ 1))  # 0b1010'''),
        ("Generate all subsets of [1,2,3] using bitmasks.", "Iterate 0..2^n-1.",
         r'''def subsets(nums):
    n = len(nums); out = []
    for mask in range(1 << n):
        out.append([nums[i] for i in range(n) if mask & (1 << i)])
    return out
print(subsets([1, 2, 3]))
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]'''),
    ],
}

# ===== APPEND-POINT (do not remove) =====
