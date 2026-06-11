# ======================================================================
# 50 — Recursion and Backtracking  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Subsets and permutations by backtracking
# ----------------------------------------------------------------------
print("\n--- Example 1: Subsets and permutations by backtracking ---")
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

# ----------------------------------------------------------------------
# Example 2: Generate balanced parentheses (with pruning)
# ----------------------------------------------------------------------
print("\n--- Example 2: Generate balanced parentheses (with pruning) ---")
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

# ----------------------------------------------------------------------
# Example 3: N-Queens: count solutions with backtracking + pruning
# ----------------------------------------------------------------------
print("\n--- Example 3: N-Queens: count solutions with backtracking + pruning ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")
