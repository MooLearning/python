# ======================================================================
# 33 — String Algorithms  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Palindrome check with two pointers
# ----------------------------------------------------------------------
print("\n--- Example 1: Palindrome check with two pointers ---")
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

# ----------------------------------------------------------------------
# Example 2: Anagrams and character frequency
# ----------------------------------------------------------------------
print("\n--- Example 2: Anagrams and character frequency ---")
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

# ----------------------------------------------------------------------
# Example 3: Naive pattern search and word reversal
# ----------------------------------------------------------------------
print("\n--- Example 3: Naive pattern search and word reversal ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")
