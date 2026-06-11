# ======================================================================
# 20 — Dunder (Magic) Methods  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: __str__ and __repr__
# ----------------------------------------------------------------------
print("\n--- Example 1: __str__ and __repr__ ---")
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):           # for developers / the REPL / debugging
        return f"Point(x={self.x}, y={self.y})"
    def __str__(self):            # for end users / print()
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)          # (3, 4)        -> uses __str__
print(str(p))     # (3, 4)
print(repr(p))    # Point(x=3, y=4) -> uses __repr__
print([p, p])     # lists show __repr__ of items

# ----------------------------------------------------------------------
# Example 2: Operator overloading: __add__, __eq__, __len__
# ----------------------------------------------------------------------
print("\n--- Example 2: Operator overloading: __add__, __eq__, __len__ ---")
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):              # enables v1 + v2
        return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other):               # enables v1 == v2
        return self.x == other.x and self.y == other.y
    def __len__(self):                     # enables len(v) -> we'll return dimension
        return 2
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))   # Vector(4, 6)
print(Vector(1, 2) == Vector(1, 2))  # True
print(len(Vector(1, 2)))             # 2

# ----------------------------------------------------------------------
# Example 3: __getitem__ and making objects sortable with __lt__
# ----------------------------------------------------------------------
print("\n--- Example 3: __getitem__ and making objects sortable with __lt__ ---")
from functools import total_ordering

@total_ordering                      # fills in <=, >, >= from __eq__ and __lt__
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other): return self.cents == other.cents
    def __lt__(self, other): return self.cents < other.cents
    def __repr__(self): return f"${self.cents/100:.2f}"

prices = [Money(250), Money(99), Money(1000)]
print(sorted(prices))      # [$0.99, $2.50, $10.00]

class Deck:
    def __init__(self): self.cards = ["A", "K", "Q", "J"]
    def __getitem__(self, i): return self.cards[i]   # enables deck[0] AND iteration
    def __len__(self): return len(self.cards)

deck = Deck()
print(deck[0], deck[-1])   # A J
for card in deck:          # works because of __getitem__
    print(card, end=" ")
print()

print("\nDone! Tip: change values above and run again to learn by experiment.")
