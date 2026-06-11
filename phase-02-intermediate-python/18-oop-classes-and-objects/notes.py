# ======================================================================
# 18 — OOP: Classes and Objects  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Defining a class and creating objects
# ----------------------------------------------------------------------
print("\n--- Example 1: Defining a class and creating objects ---")
class Dog:
    species = "Canis familiaris"     # class attribute: shared by ALL dogs

    def __init__(self, name, age):   # runs when you create a Dog
        self.name = name             # instance attribute: unique per dog
        self.age = age

    def bark(self):                  # a method (a function inside a class)
        return f"{self.name} says woof!"

rex = Dog("Rex", 3)                  # create an instance
fido = Dog("Fido", 5)
print(rex.bark())                    # Rex says woof!
print(fido.name, fido.age)           # Fido 5
print(rex.species, fido.species)     # both share the class attribute

# ----------------------------------------------------------------------
# Example 2: Methods that change state
# ----------------------------------------------------------------------
print("\n--- Example 2: Methods that change state ---")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

acc = BankAccount("Ada", 100)
print(acc.deposit(50))    # 150
print(acc.withdraw(30))   # 120
print(acc.withdraw(999))  # Insufficient funds
print(acc.owner, acc.balance)

# ----------------------------------------------------------------------
# Example 3: Class vs instance attributes (a common gotcha)
# ----------------------------------------------------------------------
print("\n--- Example 3: Class vs instance attributes (a common gotcha) ---")
class Counter:
    count = 0                # class attribute (shared)

    def __init__(self):
        Counter.count += 1   # increment the SHARED counter on each creation
        self.id = Counter.count

a = Counter()
b = Counter()
c = Counter()
print("total created:", Counter.count)   # 3
print("ids:", a.id, b.id, c.id)          # 1 2 3

print("\nDone! Tip: change values above and run again to learn by experiment.")
