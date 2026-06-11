# ======================================================================
# 25 — Regular Expressions  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Searching and extracting
# ----------------------------------------------------------------------
print("\n--- Example 1: Searching and extracting ---")
import re

text = "Order 12345 shipped on 2026-06-09 for $42.50"

# search: find the FIRST match anywhere
m = re.search(r"\d+", text)
print(m.group())          # 12345

# findall: get ALL matches as a list
print(re.findall(r"\d+", text))   # ['12345', '2026', '06', '09', '42', '50']

# Capture groups: extract structured pieces (year, month, day)
date = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print(date.groups())      # ('2026', '06', '09')
print("year:", date.group(1))

# ----------------------------------------------------------------------
# Example 2: Validating and replacing
# ----------------------------------------------------------------------
print("\n--- Example 2: Validating and replacing ---")
import re

def is_email(s):
    # A simple (not RFC-perfect) email check
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return re.match(pattern, s) is not None

print(is_email("ada@example.com"))   # True
print(is_email("not-an-email"))      # False

# sub: replace matches. Here, mask all digits with #
print(re.sub(r"\d", "#", "PIN 1234, code 5678"))   # PIN ####, code ####

# split on one-or-more non-word characters
print(re.split(r"\W+", "hello, world!  bye"))      # ['hello', 'world', 'bye']

# ----------------------------------------------------------------------
# Example 3: Groups, named groups, and compiling
# ----------------------------------------------------------------------
print("\n--- Example 3: Groups, named groups, and compiling ---")
import re

# Named groups make matches self-documenting
pattern = re.compile(r"(?P<user>\w+)@(?P<domain>[\w.]+)")
m = pattern.search("contact ada@data.org please")
print(m.group("user"))     # ada
print(m.group("domain"))   # data.org

# Compile once, reuse many times (faster in loops)
word = re.compile(r"\b\w{4}\b")    # exactly-4-letter words
print(word.findall("this is a test of word sizes"))   # ['this', 'test', 'word']

# Non-greedy: match as little as possible
print(re.findall(r"<(.+?)>", "<a><b><c>"))   # ['a', 'b', 'c']

print("\nDone! Tip: change values above and run again to learn by experiment.")
