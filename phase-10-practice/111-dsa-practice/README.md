# 111 — DSA Practice

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**DSA practice** is the deliberate, repeated solving of data-structure and algorithm problems (LeetCode/HackerRank style) to build pattern recognition and interview fluency. The skill isn't memorizing solutions — it's recognizing which **pattern** a problem fits (two pointers, sliding window, hashing, BFS/DFS, DP) and reasoning about **time/space complexity** out loud.

## Why it matters

Coding interviews at most companies are DSA-based, and the problem-solving muscle transfers to writing efficient real code. Consistent practice with reflection beats cramming.

## Key concepts

- **Pattern recognition** — Map a new problem to a known technique.
- **Brute force first** — Get a correct solution, THEN optimize.
- **Complexity analysis** — State time/space Big-O for every solution.
- **Edge cases** — Empty input, one element, duplicates, negatives.
- **Spaced repetition** — Re-solve missed problems after a few days.
- **Think aloud** — Communicate your approach — interviews test reasoning.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Don't memorize solutions — practice RECOGNIZING the pattern, or new problems stump you.
- ⚠️ Always analyze time/space complexity; a working but O(n²) answer may not pass.
- ⚠️ Test edge cases (empty, single, duplicates, negatives) before declaring it done.
- ⚠️ Re-solve problems you missed a few days later — spaced repetition cements them.
- ⚠️ In interviews, explain your thinking out loud; silence reads as being stuck.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

