# 52 — Greedy Algorithms

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **greedy algorithm** builds a solution one step at a time, always taking the choice that looks best **right now** (a local optimum), hoping it leads to a global optimum. When the problem has the **greedy-choice property** and **optimal substructure**, greedy is both correct and fast — often O(n log n) (a sort) plus one pass. When it doesn't, greedy gives a wrong answer and you need DP.

## Why it matters

Greedy solves classic problems optimally and quickly: interval scheduling, Huffman coding, Dijkstra/Prim/Kruskal, coin change (canonical systems), fractional knapsack. Knowing when greedy IS and ISN'T valid is a key algorithmic skill.

## Key concepts

- **Greedy choice** — Pick the locally optimal option at each step.
- **Optimal substructure** — An optimal solution contains optimal sub-solutions.
- **Sort first** — Most greedy algorithms start by sorting by some key.
- **Exchange argument** — Prove correctness by showing swaps never hurt.
- **When it fails** — 0/1 knapsack, general coin change — greedy can be suboptimal.
- **Speed** — Usually O(n log n) — far faster than exhaustive search or DP.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Greedy is NOT always optimal — prove the greedy-choice property or you'll get wrong answers.
- ⚠️ 0/1 knapsack and general coin change need DP, not greedy.
- ⚠️ Most greedy algorithms depend on sorting by the RIGHT key — choosing the wrong key fails.
- ⚠️ Activity selection sorts by END time, not start time or duration — a classic mistake.
- ⚠️ Fractional knapsack allows fractions; the 0/1 version (whole items only) is a different, harder problem.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

