# 50 — Recursion and Backtracking

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Recursion** solves a problem by calling itself on smaller inputs until a **base case**. **Backtracking** is recursion that **builds candidates incrementally and undoes** (backs out of) choices that can't lead to a solution — a systematic DFS over the space of possibilities. It's the engine behind permutations, combinations, subsets, N-Queens, Sudoku, and maze solving.

## Why it matters

Backtracking turns 'try every valid arrangement' into clean recursive code with pruning. It's a staple of interviews and the natural tool whenever you must enumerate or search combinatorial choices.

## Key concepts

- **Base case** — The smallest input you answer directly — stops the recursion.
- **Recursive case** — Reduce toward the base case and combine sub-results.
- **Choose / explore / un-choose** — Make a choice, recurse, then undo it.
- **Pruning** — Abandon a branch early when it can't possibly work.
- **State** — Pass partial solutions down (path) and collect complete ones.
- **Exponential space** — Permutations/subsets grow fast — backtracking searches smartly.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Append a COPY (`path[:]`) when recording results — appending the live list records mutations.
- ⚠️ Always undo your choice (`path.pop()`) after recursing, or state leaks across branches.
- ⚠️ Missing/incorrect base case → infinite recursion and RecursionError.
- ⚠️ Without pruning, backtracking explores exponentially many dead branches — add checks early.
- ⚠️ Default mutable arguments (`def f(path=[])`) are shared across calls — pass state explicitly.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

