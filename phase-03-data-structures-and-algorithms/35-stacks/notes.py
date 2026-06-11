# ======================================================================
# 35 — Stacks  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A Stack class wrapping a list
# ----------------------------------------------------------------------
print("\n--- Example 1: A Stack class wrapping a list ---")
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)       # O(1)
    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()    # O(1) from the end
    def peek(self):
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0
    def __len__(self):
        return len(self._items)

s = Stack()
for x in [1, 2, 3]:
    s.push(x)
print("top:", s.peek())     # 3
print("pop:", s.pop())      # 3
print("pop:", s.pop())      # 2
print("size:", len(s))      # 1

# ----------------------------------------------------------------------
# Example 2: Balanced brackets checker (classic stack use)
# ----------------------------------------------------------------------
print("\n--- Example 2: Balanced brackets checker (classic stack use) ---")
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)            # opening -> push
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False            # mismatch or nothing to match
    return not stack                    # leftover opens -> unbalanced

for expr in ["(a[b]{c})", "([)]", "(((", "{[()]}"]:
    print(f"{expr:10} -> {is_balanced(expr)}")

# ----------------------------------------------------------------------
# Example 3: Evaluate Reverse Polish Notation with a stack
# ----------------------------------------------------------------------
print("\n--- Example 3: Evaluate Reverse Polish Notation with a stack ---")
def eval_rpn(tokens):
    stack = []
    ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
           "*": lambda a, b: a * b, "/": lambda a, b: int(a / b)}
    for tok in tokens:
        if tok in ops:
            b = stack.pop(); a = stack.pop()    # order matters!
            stack.append(ops[tok](a, b))
        else:
            stack.append(int(tok))
    return stack.pop()

# (2 + 1) * 3  ->  "2 1 + 3 *"
print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 4 + (13//5) = 6

print("\nDone! Tip: change values above and run again to learn by experiment.")
