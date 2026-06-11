# ======================================================================
# 07 — Loops  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: for loops and range()
# ----------------------------------------------------------------------
print("\n--- Example 1: for loops and range() ---")
# Iterate directly over items
for fruit in ["apple", "banana", "cherry"]:
    print("I like", fruit)

# range(stop): 0,1,2,3,4
total = 0
for i in range(5):
    total += i
print("sum 0..4 =", total)   # 10

# range(start, stop, step)
for n in range(2, 11, 2):     # 2,4,6,8,10
    print(n, end=" ")
print()

# ----------------------------------------------------------------------
# Example 2: while loops, break and continue
# ----------------------------------------------------------------------
print("\n--- Example 2: while loops, break and continue ---")
# while: repeat until a condition changes
count = 3
while count > 0:
    print("countdown:", count)
    count -= 1          # WITHOUT this line it would loop forever!
print("liftoff!")

# break stops the loop; continue skips one iteration
for n in range(1, 10):
    if n == 5:
        break           # stop entirely when we reach 5
    if n % 2 == 0:
        continue        # skip even numbers
    print("odd before 5:", n)   # 1, 3

# ----------------------------------------------------------------------
# Example 3: enumerate and the loop-else
# ----------------------------------------------------------------------
print("\n--- Example 3: enumerate and the loop-else ---")
names = ["Ada", "Linus", "Grace"]
for index, name in enumerate(names, start=1):
    print(index, name)

# loop-else: runs only if no break happened (great for "search and report")
target = 7
for n in [2, 4, 6, 8]:
    if n == target:
        print("found!")
        break
else:
    print("not found")   # this prints, because we never broke

print("\nDone! Tip: change values above and run again to learn by experiment.")
