# ======================================================================
# 111 — DSA Practice  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A problem-solving framework on Two Sum
# ----------------------------------------------------------------------
print("\n--- Example 1: A problem-solving framework on Two Sum ---")
# Problem: return indices of two numbers that add up to target.
nums, target = [2, 7, 11, 15], 9

# Step 1 - BRUTE FORCE: check all pairs -> O(n^2)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
print("brute force:", two_sum_brute(nums, target))

# Step 2 - OPTIMIZE with a hash map -> O(n)
def two_sum_fast(nums, target):
    seen = {}                          # value -> index
    for i, n in enumerate(nums):
        if target - n in seen:
            return (seen[target - n], i)
        seen[n] = i
print("optimized :", two_sum_fast(nums, target))
print("complexity: brute O(n^2) -> hashmap O(n) time, O(n) space")

# ----------------------------------------------------------------------
# Example 2: Recognizing patterns: window, two-pointer, hashing
# ----------------------------------------------------------------------
print("\n--- Example 2: Recognizing patterns: window, two-pointer, hashing ---")
# SLIDING WINDOW: max sum of k consecutive elements
def max_window(a, k):
    window = sum(a[:k]); best = window
    for i in range(k, len(a)):
        window += a[i] - a[i - k]
        best = max(best, window)
    return best
print("window  :", max_window([1, 4, 2, 10, 2, 3], 3))   # 16

# TWO POINTERS: pair summing to target in a sorted array
def pair_sum(a, t):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == t: return (a[i], a[j])
        i, j = (i + 1, j) if s < t else (i, j - 1)
print("2-pointer:", pair_sum([1, 2, 4, 7, 11], 9))        # (2, 7)

# HASHING: first non-repeating character
from collections import Counter
def first_unique(s):
    c = Counter(s)
    return next((ch for ch in s if c[ch] == 1), None)
print("hashing :", first_unique("aabbcde"))               # c

# ----------------------------------------------------------------------
# Example 3: A study plan and worked complexity analysis
# ----------------------------------------------------------------------
print("\n--- Example 3: A study plan and worked complexity analysis ---")
# Worked example: valid parentheses (stack) — O(n) time, O(n) space
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack

for test in ["()[]{}", "(]", "([{}])"]:
    print(f"{test:8} -> {is_valid(test)}")

print("\nSuggested 8-week plan (1-2 problems/day):")
plan = ["Arrays & Hashing", "Two Pointers & Sliding Window", "Stack & Queue",
        "Binary Search", "Linked Lists", "Trees & BFS/DFS",
        "Backtracking & Recursion", "Dynamic Programming"]
for week, topic in enumerate(plan, 1):
    print(f"  week {week}: {topic}")

print("\nDone! Tip: change values above and run again to learn by experiment.")
