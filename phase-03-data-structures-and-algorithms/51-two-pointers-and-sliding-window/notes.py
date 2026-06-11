# ======================================================================
# 51 — Two Pointers and Sliding Window  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Two pointers from both ends (sorted two-sum)
# ----------------------------------------------------------------------
print("\n--- Example 1: Two pointers from both ends (sorted two-sum) ---")
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

# ----------------------------------------------------------------------
# Example 2: Fixed-size sliding window (max sum of k)
# ----------------------------------------------------------------------
print("\n--- Example 2: Fixed-size sliding window (max sum of k) ---")
def max_sum_window(arr, k):
    window = sum(arr[:k])        # first window
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]   # add new, drop old -> O(1) slide
        best = max(best, window)
    return best

print(max_sum_window([2, 1, 5, 1, 3, 2], 3))   # 9  (5+1+3)
print(max_sum_window([1, 1, 1, 1], 2))         # 2

# ----------------------------------------------------------------------
# Example 3: Variable sliding window (longest substring no repeats)
# ----------------------------------------------------------------------
print("\n--- Example 3: Variable sliding window (longest substring no repeats) ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")
