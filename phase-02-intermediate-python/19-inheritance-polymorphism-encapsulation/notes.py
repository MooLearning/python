# ======================================================================
# 19 — Inheritance, Polymorphism and Encapsulation  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Inheritance and super()
# ----------------------------------------------------------------------
print("\n--- Example 1: Inheritance and super() ---")
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "(some sound)"

class Dog(Animal):              # Dog inherits from Animal
    def speak(self):            # override the parent method
        return "Woof"

class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)  # reuse Animal's __init__
        self.age = age

d = Dog("Rex")
p = Puppy("Fido", 1)
print(d.name, d.speak())        # Rex Woof
print(p.name, p.age, p.speak()) # Fido 1 Woof  (inherited from Dog)
print(isinstance(p, Animal))    # True (a Puppy IS an Animal)

# ----------------------------------------------------------------------
# Example 2: Polymorphism: same call, different behavior
# ----------------------------------------------------------------------
print("\n--- Example 2: Polymorphism: same call, different behavior ---")
class Cat:
    def speak(self): return "Meow"
class Cow:
    def speak(self): return "Moo"
class Duck:
    def speak(self): return "Quack"

# One loop handles every type -- they just need a .speak() method
for animal in [Cat(), Cow(), Duck()]:
    print(animal.speak())

# Built-in polymorphism: len() works on many types
for obj in ["hello", [1, 2, 3], {"a": 1}]:
    print(len(obj), end=" ")
print()

# ----------------------------------------------------------------------
# Example 3: Encapsulation with private attributes and properties
# ----------------------------------------------------------------------
print("\n--- Example 3: Encapsulation with private attributes and properties ---")
class Account:
    def __init__(self, balance):
        self.__balance = balance          # __ name-mangled -> "private"

    @property
    def balance(self):                    # read access via .balance
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.__balance += amount

acc = Account(100)
acc.deposit(50)
print(acc.balance)        # 150  (read-only from outside)
# acc.balance = 999       # would raise AttributeError (no setter)
print(hasattr(acc, "__balance"))   # False -> it's name-mangled and hidden

print("\nDone! Tip: change values above and run again to learn by experiment.")
