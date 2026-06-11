# 51 — Two Pointers and Sliding Window

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Two pointers** uses two indices that move through a sequence — toward each other (from both ends) or in the same direction (fast/slow) — to solve problems in O(n) that would be O(n²) with nested loops. A **sliding window** is a two-pointer pattern where a contiguous range `[left, right]` grows and shrinks to satisfy a constraint (longest/shortest subarray, sums, distinct counts).

## Why it matters

These patterns turn many array/string problems from quadratic to linear. Recognizing 'pair summing to target', 'longest substring with…', or 'subarray of size k' as two-pointer/window problems is a huge interview and performance win.

## Key concepts

- **Opposite ends** — left=0, right=n-1 moving inward (sorted-pair sums, palindromes).
- **Fast/slow** — Same direction at different speeds (cycle detection, dedup).
- **Fixed window** — A window of constant size k slides across the array.
- **Variable window** — Grow right; shrink left until the constraint holds again.
- **Window state** — Maintain a running sum/count/dict as the window moves.
- **O(n)** — Each pointer moves forward at most n times total.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Two-pointer-from-ends needs SORTED data; on unsorted input it gives wrong answers.
- ⚠️ Slide the window in O(1) (add new, subtract old) — recomputing the sum makes it O(n·k).
- ⚠️ For variable windows, shrink with a `while` (not `if`) so the constraint is fully restored.
- ⚠️ Off-by-one in window length: it's `right - left + 1`, not `right - left`.
- ⚠️ Update window state (dict/sum) consistently when BOTH adding right and removing left.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

