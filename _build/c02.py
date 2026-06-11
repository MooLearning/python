# -*- coding: utf-8 -*-
"""Phase 2 — Intermediate Python content."""

CONTENT = {}

CONTENT["oop-classes-and-objects"] = {
    "what": (
        "**Object-Oriented Programming (OOP)** organizes code around **objects** — bundles of data "
        "(**attributes**) and behavior (**methods**). A **class** is the blueprint; an **object** "
        "(or instance) is a concrete thing built from it. `__init__` is the setup method that runs "
        "when you create an instance, and `self` refers to the specific instance."
    ),
    "why": (
        "OOP models real-world things naturally (a BankAccount, a User, a Model). It groups related "
        "data and functions, prevents global-variable spaghetti, and underpins almost every Python "
        "library you'll use — scikit-learn estimators, PyTorch modules, etc."
    ),
    "concepts": [
        ("class", "A blueprint: `class Dog:`. Convention: ClassNames use CapWords."),
        ("object / instance", "A specific thing made from a class: `d = Dog()`."),
        ("__init__", "The initializer; sets up attributes when an instance is created."),
        ("self", "The first parameter of every method; refers to the current instance."),
        ("Instance attribute", "Data unique to each object: `self.name`."),
        ("Class attribute", "Data shared by ALL instances, defined in the class body."),
    ],
    "examples": [
        ("Defining a class and creating objects", r'''
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
'''),
        ("Methods that change state", r'''
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
'''),
        ("Class vs instance attributes (a common gotcha)", r'''
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
'''),
    ],
    "gotchas": [
        "Forgetting `self` as the first method parameter -> 'takes 0 positional arguments but 1 was given'.",
        "Mutable class attributes (e.g. a shared list) are shared by ALL instances — usually you want it in __init__.",
        "`__init__` doesn't 'return' the object; it just configures `self`. Returning anything but None raises an error.",
        "Setting `instance.attr = x` creates an instance attribute that shadows a class attribute of the same name.",
        "Accessing an attribute that was never set raises AttributeError — initialize everything in __init__.",
    ],
    "exercises": [
        ("Create a class Circle with radius, and a method area() returning pi*r*r. Test radius 2.",
         "Use 3.14159 or math.pi.",
         r'''import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
print(round(Circle(2).area(), 2))  # 12.57'''),
        ("Make a Person class with name and greet() returning 'Hi, I'm <name>'.", "f-string with self.name.",
         r'''class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hi, I'm {self.name}"
print(Person("Ada").greet())'''),
        ("Build a Rectangle class with width/height and methods area() and perimeter().", "Two methods.",
         r'''class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
r = Rectangle(3, 4)
print(r.area(), r.perimeter())  # 12 14'''),
        ("Give Dog a class attribute legs=4 and show two instances share it.", "Class attribute.",
         r'''class Dog:
    legs = 4
a, b = Dog(), Dog()
print(a.legs, b.legs)  # 4 4'''),
        ("Create a Stack class with push, pop, and is_empty using an internal list.", "Wrap a list.",
         r'''class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        return self._items.pop()
    def is_empty(self):
        return len(self._items) == 0
s = Stack(); s.push(1); s.push(2)
print(s.pop(), s.is_empty())  # 2 False'''),
        ("Add a method to BankAccount that returns a formatted string '<owner>: $<balance>'.", "f-string.",
         r'''class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance
    def summary(self):
        return f"{self.owner}: ${self.balance}"
print(BankAccount("Bo", 50).summary())'''),
        ("Make a Counter class whose increment() bumps an instance count and value() returns it.",
         "Instance attribute.",
         r'''class Counter:
    def __init__(self):
        self.n = 0
    def increment(self):
        self.n += 1
    def value(self):
        return self.n
c = Counter(); c.increment(); c.increment()
print(c.value())  # 2'''),
        ("Create a Temperature class storing celsius and a method to_fahrenheit().", "F = C*9/5+32.",
         r'''class Temperature:
    def __init__(self, c):
        self.c = c
    def to_fahrenheit(self):
        return self.c * 9 / 5 + 32
print(Temperature(100).to_fahrenheit())  # 212.0'''),
    ],
}

CONTENT["inheritance-polymorphism-encapsulation"] = {
    "what": (
        "The three classic OOP pillars (beyond classes themselves): **Inheritance** lets a child "
        "class reuse and extend a parent (`class Cat(Animal):`). **Polymorphism** lets different "
        "classes respond to the same method name in their own way. **Encapsulation** hides internal "
        "details behind a clean interface (using `_protected` and `__private` naming, and "
        "properties). **Abstraction** exposes only what matters."
    ),
    "why": (
        "These pillars let you build large systems without repeating code, swap implementations "
        "freely (polymorphism is why `len()` works on lists and strings), and protect invariants. "
        "Frameworks rely on you subclassing their base classes."
    ),
    "concepts": [
        ("Inheritance", "`class Child(Parent):` gets the parent's attributes/methods for free."),
        ("super()", "Call the parent's version of a method, e.g. `super().__init__(...)`."),
        ("Method overriding", "Redefine a parent method in the child to change behavior."),
        ("Polymorphism", "Same method name, different behavior per class — duck typing."),
        ("Encapsulation", "`_name` (protected by convention), `__name` (name-mangled), properties."),
        ("Abstraction", "Hide complex internals; expose a simple, stable interface."),
    ],
    "examples": [
        ("Inheritance and super()", r'''
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
'''),
        ("Polymorphism: same call, different behavior", r'''
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
'''),
        ("Encapsulation with private attributes and properties", r'''
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
'''),
    ],
    "gotchas": [
        "Always call `super().__init__()` in a child's __init__ if the parent needs setup, or its attributes won't exist.",
        "`_single_underscore` is only a convention ('please don't touch'); `__double` triggers name mangling.",
        "Python uses duck typing — you don't need a shared base class for polymorphism, just the same method name.",
        "Deep inheritance trees get confusing fast; prefer composition (has-a) over inheritance (is-a) when unsure.",
        "Overriding a method but forgetting to call `super()` can skip important parent behavior.",
    ],
    "exercises": [
        ("Create Shape with area() returning 0, and Square(Shape) overriding area().", "Override.",
         r'''class Shape:
    def area(self): return 0
class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
print(Square(4).area())  # 16'''),
        ("Make Vehicle with __init__(wheels) and Car that calls super().__init__(4).", "super().",
         r'''class Vehicle:
    def __init__(self, wheels): self.wheels = wheels
class Car(Vehicle):
    def __init__(self): super().__init__(4)
print(Car().wheels)  # 4'''),
        ("Write three classes with a sound() method and loop calling it (polymorphism).", "Duck typing.",
         r'''class A:
    def sound(self): return "a"
class B:
    def sound(self): return "b"
for o in [A(), B()]:
    print(o.sound())'''),
        ("Use isinstance to check a Dog instance is also an Animal.", "isinstance(obj, Cls).",
         r'''class Animal: pass
class Dog(Animal): pass
print(isinstance(Dog(), Animal))  # True'''),
        ("Add a read-only property full_name to a Person with first and last names.", "@property.",
         r'''class Person:
    def __init__(self, f, l): self.f, self.l = f, l
    @property
    def full_name(self): return f"{self.f} {self.l}"
print(Person("Ada", "Lovelace").full_name)'''),
        ("Make Employee(Person) that adds a salary and a raise_pay(pct) method.", "Inherit + extend.",
         r'''class Person:
    def __init__(self, name): self.name = name
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name); self.salary = salary
    def raise_pay(self, pct): self.salary *= 1 + pct / 100
e = Employee("Bo", 100); e.raise_pay(10)
print(e.salary)  # 110.0'''),
        ("Encapsulate a private __pin in a Card class; expose check_pin(guess).", "__name mangling.",
         r'''class Card:
    def __init__(self, pin): self.__pin = pin
    def check_pin(self, guess): return guess == self.__pin
print(Card(1234).check_pin(1234))  # True'''),
        ("Override __init__ in a child but keep the parent's attribute via super().", "super().__init__.",
         r'''class Base:
    def __init__(self): self.kind = "base"
class Child(Base):
    def __init__(self):
        super().__init__()
        self.extra = 1
c = Child()
print(c.kind, c.extra)  # base 1'''),
    ],
}

CONTENT["dunder-methods"] = {
    "what": (
        "**Dunder** (double-underscore) methods, also called **magic** or **special** methods, let "
        "your objects work with Python's built-in syntax. Define `__str__` for `print()`, `__len__` "
        "for `len()`, `__eq__` for `==`, `__add__` for `+`, `__getitem__` for `obj[i]`, and more. "
        "They're how you make custom classes feel native."
    ),
    "why": (
        "Dunder methods turn your objects into first-class citizens: comparable, printable, "
        "iterable, addable. They're the secret behind why NumPy arrays support `+` and why a "
        "DataFrame supports `df[col]`. Implementing a few makes your classes intuitive to use."
    ),
    "concepts": [
        ("__init__", "Constructor/initializer (you already know this one)."),
        ("__str__ / __repr__", "Human-readable string vs unambiguous developer string."),
        ("__len__", "Makes `len(obj)` work."),
        ("__eq__ / __lt__", "Define `==` and `<` so objects compare and sort."),
        ("__add__", "Define `obj1 + obj2`."),
        ("__getitem__", "Define `obj[key]` indexing; also enables iteration as a fallback."),
    ],
    "examples": [
        ("__str__ and __repr__", r'''
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
'''),
        ("Operator overloading: __add__, __eq__, __len__", r'''
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
'''),
        ("__getitem__ and making objects sortable with __lt__", r'''
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
'''),
    ],
    "gotchas": [
        "If you define `__eq__`, also define `__hash__` (or set it) if you want objects usable in sets/dicts.",
        "`__repr__` should be unambiguous (ideally valid code); `__str__` is for friendly display. Define __repr__ at least.",
        "`__add__` should return a NEW object, not mutate self — match how numbers behave.",
        "Forgetting `__repr__` makes debugging painful (you see `<object at 0x...>`).",
        "Comparison dunders should return NotImplemented for unsupported types, not raise — lets Python try the reflected op.",
    ],
    "exercises": [
        ("Give a class a __str__ so print(obj) shows 'Item(<name>)'.", "Return an f-string.",
         r'''class Item:
    def __init__(self, name): self.name = name
    def __str__(self): return f"Item({self.name})"
print(Item("pen"))  # Item(pen)'''),
        ("Implement __len__ so len(box) returns the number of items it holds.", "Wrap a list.",
         r'''class Box:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)
print(len(Box([1, 2, 3])))  # 3'''),
        ("Add __eq__ so two Coord(1,2) objects compare equal.", "Compare attributes.",
         r'''class Coord:
    def __init__(self, x, y): self.x, self.y = x, y
    def __eq__(self, o): return (self.x, self.y) == (o.x, o.y)
print(Coord(1, 2) == Coord(1, 2))  # True'''),
        ("Implement __add__ so Money(100)+Money(50) gives Money(150).", "Return new instance.",
         r'''class Money:
    def __init__(self, c): self.c = c
    def __add__(self, o): return Money(self.c + o.c)
    def __repr__(self): return f"Money({self.c})"
print(Money(100) + Money(50))  # Money(150)'''),
        ("Make objects sortable by defining __lt__ on a class with a 'score'.", "Compare score.",
         r'''class P:
    def __init__(self, s): self.s = s
    def __lt__(self, o): return self.s < o.s
    def __repr__(self): return f"P({self.s})"
print(sorted([P(3), P(1), P(2)]))'''),
        ("Implement __getitem__ so playlist[0] returns the first song.", "Index into a list.",
         r'''class Playlist:
    def __init__(self, songs): self.songs = songs
    def __getitem__(self, i): return self.songs[i]
print(Playlist(["a", "b"])[0])  # a'''),
        ("Add __repr__ that returns valid constructor code for a Point.", "Return 'Point(x, y)'.",
         r'''class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f"Point({self.x}, {self.y})"
print(repr(Point(1, 2)))  # Point(1, 2)'''),
        ("Make a class callable with __call__ so obj(5) returns 5 squared.", "Define __call__.",
         r'''class Square:
    def __call__(self, x): return x * x
sq = Square()
print(sq(5))  # 25'''),
    ],
}

CONTENT["decorators"] = {
    "what": (
        "A **decorator** is a function that takes another function and returns a new, enhanced "
        "version of it — without changing the original's code. You apply one with the `@decorator` "
        "syntax above a function. They're used for logging, timing, caching, access control, and "
        "registering functions."
    ),
    "why": (
        "Decorators let you add behavior to many functions in a reusable, declarative way. You'll "
        "meet them constantly: `@property`, `@staticmethod`, `@app.route` in Flask, `@lru_cache`, "
        "and `@pytest.fixture`. Understanding them demystifies a lot of 'magic'."
    ),
    "concepts": [
        ("Functions are objects", "You can pass them around, return them, and store them in variables."),
        ("Wrapper function", "An inner function that runs code before/after calling the original."),
        ("@decorator syntax", "`@deco` above `def f` is sugar for `f = deco(f)`."),
        ("functools.wraps", "Preserves the original function's name/docstring on the wrapper."),
        ("Decorators with arguments", "A decorator factory: a function returning a decorator."),
        ("*args, **kwargs", "Wrappers use them to forward any arguments to the wrapped function."),
    ],
    "examples": [
        ("Your first decorator", r'''
import functools

def shout(func):
    @functools.wraps(func)            # keep func's name/docstring
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) # call the original
        return result.upper() + "!"   # enhance the result
    return wrapper

@shout                                 # same as greet = shout(greet)
def greet(name):
    return f"hello {name}"

print(greet("ada"))     # HELLO ADA!
print(greet.__name__)   # greet  (thanks to functools.wraps)
'''),
        ("A timing decorator (logs how long a function takes)", r'''
import functools, time

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed*1000:.2f} ms")
        return result
    return wrapper

@timed
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))   # prints timing, then the result
'''),
        ("Decorator with arguments (a factory)", r'''
import functools

def repeat(times):                     # outer: takes the argument
    def decorator(func):               # middle: takes the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # inner: does the work
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def ping():
    print("ping")

ping()    # prints ping three times

# Built-in caching decorator -- memoization for free:
from functools import lru_cache
@lru_cache
def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
print(fib(30))   # fast
'''),
    ],
    "gotchas": [
        "Always use `@functools.wraps(func)` on the wrapper, or you lose the original name, docstring, and help().",
        "A wrapper must accept `*args, **kwargs` and forward them, or it breaks functions with different signatures.",
        "Remember to RETURN the wrapped function's result, or every decorated function silently returns None.",
        "Decorators run at definition time (when the `@` line is reached), not when the function is called.",
        "Stacked decorators apply bottom-up: the one nearest the def wraps first.",
    ],
    "exercises": [
        ("Write a decorator that prints 'calling' before running any function. Decorate hi().", "wrapper prints then calls.",
         r'''def announce(f):
    def w(*a, **k):
        print("calling")
        return f(*a, **k)
    return w
@announce
def hi(): print("hi")
hi()'''),
        ("Write a decorator double that doubles the numeric return value of a function.", "Return f()*2.",
         r'''def double(f):
    def w(*a, **k): return f(*a, **k) * 2
    return w
@double
def five(): return 5
print(five())  # 10'''),
        ("Use functools.wraps and confirm the wrapped function keeps its name.", "wraps.",
         r'''import functools
def deco(f):
    @functools.wraps(f)
    def w(*a, **k): return f(*a, **k)
    return w
@deco
def hello(): pass
print(hello.__name__)  # hello'''),
        ("Write a decorator that counts how many times a function was called.", "Use an attribute.",
         r'''def counter(f):
    def w(*a, **k):
        w.calls += 1
        return f(*a, **k)
    w.calls = 0
    return w
@counter
def go(): pass
go(); go()
print(go.calls)  # 2'''),
        ("Write a parametrized decorator repeat(n) that runs a function n times.", "Factory pattern.",
         r'''def repeat(n):
    def deco(f):
        def w(*a, **k):
            for _ in range(n): r = f(*a, **k)
            return r
        return w
    return deco
@repeat(2)
def beep(): print("beep")
beep()'''),
        ("Cache an expensive function with functools.lru_cache and call it twice.", "@lru_cache.",
         r'''from functools import lru_cache
@lru_cache
def square(n):
    print("computing")
    return n * n
print(square(4)); print(square(4))  # computes once'''),
        ("Write a decorator that catches exceptions and returns None instead of crashing.", "try/except in wrapper.",
         r'''def safe(f):
    def w(*a, **k):
        try: return f(*a, **k)
        except Exception: return None
    return w
@safe
def bad(): return 1 / 0
print(bad())  # None'''),
        ("Stack two decorators (upper then exclaim) and observe the order.", "Bottom-up application.",
         r'''def upper(f):
    def w(*a, **k): return f(*a, **k).upper()
    return w
def exclaim(f):
    def w(*a, **k): return f(*a, **k) + "!"
    return w
@exclaim
@upper
def hi(): return "hi"
print(hi())  # HI!'''),
    ],
}

CONTENT["generators-and-iterators"] = {
    "what": (
        "An **iterator** is an object you can step through one item at a time with `next()`. A "
        "**generator** is the easy way to create one: write a normal function but use `yield` "
        "instead of `return`. Generators produce values **lazily** (on demand), so they can "
        "represent huge or even infinite sequences without using much memory."
    ),
    "why": (
        "Lazy evaluation is a superpower for data: stream a multi-gigabyte file line by line, "
        "generate an infinite sequence, or build efficient pipelines that compute only what's "
        "needed. Generators make memory-light, composable code."
    ),
    "concepts": [
        ("iterable vs iterator", "Iterable = can be looped (list); iterator = produces items via next()."),
        ("yield", "Pauses the function, returns a value, and resumes where it left off next time."),
        ("Lazy evaluation", "Values are produced one at a time, only when requested."),
        ("Generator expression", "`(x*x for x in range(10))` — like a comprehension but lazy."),
        ("Infinite generators", "A `while True: yield` loop can run forever; take only what you need."),
        ("next() / StopIteration", "next() pulls the next value; raises StopIteration when exhausted."),
    ],
    "examples": [
        ("A generator function with yield", r'''
def countdown(n):
    while n > 0:
        yield n          # pause here and hand back n
        n -= 1           # resume here on the next call

gen = countdown(3)
print(next(gen))   # 3
print(next(gen))   # 2
for x in gen:      # continue from where next() left off
    print("loop:", x)   # 1

# Generators are single-use: once exhausted, they're done
print(list(countdown(4)))   # [4, 3, 2, 1]
'''),
        ("Lazy = memory efficient (infinite sequences)", r'''
def naturals():
    n = 1
    while True:        # infinite! safe because it's lazy
        yield n
        n += 1

import itertools
first_five = list(itertools.islice(naturals(), 5))
print(first_five)      # [1, 2, 3, 4, 5]

# Generator expression: like a comprehension but lazy (parentheses, not brackets)
squares = (x * x for x in range(1, 1_000_000))
print(next(squares), next(squares))   # 1 4  (only computes what we ask for)
print(sum(x for x in range(1_000_000)))   # streamed, low memory
'''),
        ("Building a pipeline of generators", r'''
def read_lines():
    data = "apple,3\nbanana,7\ncherry,2\n"
    for line in data.strip().split("\n"):
        yield line

def parse(lines):
    for line in lines:
        name, count = line.split(",")
        yield name, int(count)

def only_big(pairs, threshold):
    for name, count in pairs:
        if count >= threshold:
            yield name

# Chain them -- nothing runs until we iterate the final result
pipeline = only_big(parse(read_lines()), threshold=3)
print(list(pipeline))   # ['apple', 'banana']
'''),
    ],
    "gotchas": [
        "A generator is exhausted after ONE full pass — iterate it again and you get nothing. Recreate it.",
        "`yield` makes the WHOLE function a generator; calling it runs no code until you iterate it.",
        "Don't call `list()` on an infinite generator — it never ends. Use itertools.islice or a break.",
        "Generator expressions use parentheses `()`; brackets `[]` build a full list eagerly in memory.",
        "You can't index a generator (`gen[0]` fails) — convert to a list first if you need random access.",
    ],
    "exercises": [
        ("Write a generator that yields the squares of 1..5.", "yield in a loop.",
         r'''def squares():
    for i in range(1, 6):
        yield i * i
print(list(squares()))  # [1, 4, 9, 16, 25]'''),
        ("Use a generator expression to sum the squares of 0..9 lazily.", "(x*x for x in ...).",
         r'''print(sum(x * x for x in range(10)))  # 285'''),
        ("Write a generator that yields the Fibonacci numbers, take the first 8.", "Track two values.",
         r'''def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
import itertools
print(list(itertools.islice(fib(), 8)))  # [0,1,1,2,3,5,8,13]'''),
        ("Use next() three times on a generator and observe the values.", "next().",
         r'''def g():
    yield "a"; yield "b"; yield "c"
it = g()
print(next(it), next(it), next(it))  # a b c'''),
        ("Write a generator that yields only even numbers from a list.", "yield with if.",
         r'''def evens(seq):
    for x in seq:
        if x % 2 == 0:
            yield x
print(list(evens([1, 2, 3, 4, 5, 6])))  # [2, 4, 6]'''),
        ("Create an infinite counter generator and take the first 4 values with islice.", "while True.",
         r'''import itertools
def count_from(n):
    while True:
        yield n; n += 1
print(list(itertools.islice(count_from(10), 4)))  # [10,11,12,13]'''),
        ("Show that a generator is empty on a second pass.", "Iterate twice.",
         r'''def g():
    yield 1; yield 2
it = g()
print(list(it))  # [1, 2]
print(list(it))  # [] -> exhausted'''),
        ("Chain two generators: one yields 1..5, the next yields only those >2.", "Pipeline.",
         r'''def nums():
    yield from range(1, 6)
def big(src):
    for x in src:
        if x > 2: yield x
print(list(big(nums())))  # [3, 4, 5]'''),
    ],
}

CONTENT["closures"] = {
    "what": (
        "A **closure** is a function that 'remembers' variables from the scope where it was "
        "created, even after that outer scope has finished. You make one by defining a function "
        "**inside** another function and returning the inner one. The inner function 'closes over' "
        "the outer variables."
    ),
    "why": (
        "Closures let you create configured, stateful functions without classes — function "
        "factories, callbacks, and the machinery behind decorators. They're a clean way to attach "
        "data to behavior."
    ),
    "concepts": [
        ("Nested functions", "A function defined inside another function."),
        ("Free variables", "Variables used by the inner function but defined in the enclosing one."),
        ("Returning a function", "The outer returns the inner, which keeps access to those variables."),
        ("State without classes", "Closures can hold mutable state via `nonlocal`."),
        ("__closure__", "Shows the captured cells; mostly for curiosity/debugging."),
        ("Late binding", "Closures capture VARIABLES, not values — a classic loop gotcha."),
    ],
    "examples": [
        ("A function factory (the canonical closure)", r'''
def make_multiplier(factor):
    def multiply(x):
        return x * factor     # 'factor' is remembered from the enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))   # 20
print(triple(10))   # 30
# Each closure remembers its OWN factor:
print(double.__closure__[0].cell_contents)   # 2
'''),
        ("Closures that hold state with nonlocal", r'''
def make_counter():
    count = 0
    def increment():
        nonlocal count        # modify the enclosing variable
        count += 1
        return count
    return increment

c1 = make_counter()
c2 = make_counter()          # independent state
print(c1(), c1(), c1())      # 1 2 3
print(c2())                  # 1  (separate counter)
'''),
        ("The late-binding loop trap (and the fix)", r'''
# BUG: all functions share the SAME variable i (captured by reference)
funcs_bug = []
for i in range(3):
    funcs_bug.append(lambda: i)
print([f() for f in funcs_bug])   # [2, 2, 2]  -- not [0,1,2]!

# FIX: capture the current value via a default argument
funcs_fixed = []
for i in range(3):
    funcs_fixed.append(lambda i=i: i)
print([f() for f in funcs_fixed]) # [0, 1, 2]
'''),
    ],
    "gotchas": [
        "Late binding: a closure captures the VARIABLE, not its value at creation. In loops, use a default arg to freeze it.",
        "To MODIFY an enclosing variable you need `nonlocal`; reading it works without.",
        "Each call to the factory creates a NEW, independent closure with its own captured variables.",
        "Closures keep their captured objects alive (can't be garbage-collected) — watch memory with large captures.",
        "If you find yourself adding lots of state to a closure, a class may be clearer.",
    ],
    "exercises": [
        ("Write make_adder(n) returning a function that adds n to its argument.", "Return inner function.",
         r'''def make_adder(n):
    def add(x): return x + n
    return add
print(make_adder(5)(10))  # 15'''),
        ("Create a power factory: make_power(exp) so make_power(2)(5)==25.", "x ** exp.",
         r'''def make_power(exp):
    def p(x): return x ** exp
    return p
print(make_power(2)(5))  # 25'''),
        ("Build a counter closure that returns 1,2,3 on successive calls.", "nonlocal.",
         r'''def counter():
    n = 0
    def step():
        nonlocal n; n += 1; return n
    return step
c = counter()
print(c(), c(), c())  # 1 2 3'''),
        ("Show two counters from the same factory are independent.", "Two instances.",
         r'''def counter():
    n = 0
    def step():
        nonlocal n; n += 1; return n
    return step
a, b = counter(), counter()
print(a(), a(), b())  # 1 2 1'''),
        ("Demonstrate the late-binding bug with lambdas in a loop.", "Capture by reference.",
         r'''fs = [lambda: i for i in range(3)]
print([f() for f in fs])  # [2, 2, 2]'''),
        ("Fix the late-binding bug using default arguments.", "lambda i=i.",
         r'''fs = [lambda i=i: i for i in range(3)]
print([f() for f in fs])  # [0, 1, 2]'''),
        ("Write make_accumulator() that keeps a running total across calls.", "nonlocal total.",
         r'''def make_accumulator():
    total = 0
    def add(x):
        nonlocal total; total += x; return total
    return add
acc = make_accumulator()
print(acc(10), acc(5))  # 10 15'''),
        ("Write a closure that remembers a greeting prefix and greets names.", "Capture prefix.",
         r'''def greeter(prefix):
    def greet(name): return f"{prefix}, {name}!"
    return greet
hi = greeter("Hello")
print(hi("Ada"))  # Hello, Ada!'''),
    ],
}

CONTENT["context-managers"] = {
    "what": (
        "A **context manager** is the object behind the `with` statement. It guarantees setup and "
        "**cleanup** happen around a block of code — even if an error occurs. `with open(...)` is "
        "the famous example (it always closes the file). You can write your own with a class "
        "(`__enter__`/`__exit__`) or, more simply, with `@contextmanager`."
    ),
    "why": (
        "Resource leaks (unclosed files, sockets, database connections, unreleased locks) are a "
        "common source of bugs. Context managers make 'always clean up' automatic and readable. "
        "They also handle setup/teardown for timers, temporary settings, and transactions."
    ),
    "concepts": [
        ("with statement", "Runs setup, yields control to the block, then runs cleanup."),
        ("__enter__ / __exit__", "The class protocol: enter returns the resource, exit cleans up."),
        ("@contextmanager", "Decorator that turns a generator (with one yield) into a context manager."),
        ("Cleanup on error", "__exit__ runs even when the block raises — perfect for closing things."),
        ("Multiple managers", "`with a() as x, b() as y:` manages several at once."),
        ("contextlib", "Helpers like suppress, redirect_stdout, closing."),
    ],
    "examples": [
        ("Why 'with' beats manual cleanup", r'''
# Manual way -- easy to forget close(), and a crash skips it:
f = open("demo.txt", "w", encoding="utf-8")
f.write("hi")
f.close()

# The 'with' way -- close() is GUARANTEED, even on error:
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())     # hi
# file is now closed automatically
print("closed?", f.closed)   # True

import os
os.remove("demo.txt")
'''),
        ("Writing a context manager with a class", r'''
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self                      # value bound to 'as'
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Block took {self.elapsed*1000:.2f} ms")
        return False                     # False = don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
print("result:", total)
'''),
        ("The easy way: @contextmanager", r'''
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")     # setup (everything before yield)
    yield                  # the 'with' block runs here
    print(f"</{name}>")    # cleanup (everything after yield)

with tag("p"):
    print("hello")
# Output:
# <p>
# hello
# </p>

# Cleanup still runs if the block raises -- wrap yield in try/finally for that:
@contextmanager
def safe_open(path, mode):
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()          # always runs

with safe_open("t.txt", "w") as f:
    f.write("data")
import os; os.remove("t.txt")
'''),
    ],
    "gotchas": [
        "In a class manager, `__exit__` returning True SUPPRESSES the exception — usually you want False/None.",
        "With @contextmanager, put `yield` inside try/finally so cleanup runs even when the block raises.",
        "The value after `as` comes from what `__enter__` returns (or what you `yield`), not the manager itself.",
        "`with` is for resource lifetimes, not general flow control — don't abuse it.",
        "Opening multiple resources? Use one `with a, b:` so all get cleaned up correctly.",
    ],
    "exercises": [
        ("Use 'with' to write 'hello' to a file and confirm it is closed afterward.", "f.closed.",
         r'''import os
with open("h.txt", "w", encoding="utf-8") as f:
    f.write("hello")
print(f.closed)  # True
os.remove("h.txt")'''),
        ("Write a context manager class that prints 'enter' and 'exit' around a block.", "__enter__/__exit__.",
         r'''class CM:
    def __enter__(self): print("enter"); return self
    def __exit__(self, *a): print("exit")
with CM():
    print("inside")'''),
        ("Use @contextmanager to make a manager that yields the string 'resource'.", "yield value.",
         r'''from contextlib import contextmanager
@contextmanager
def res():
    yield "resource"
with res() as r:
    print(r)  # resource'''),
        ("Make a Timer context manager that prints elapsed time for a block.", "time.perf_counter.",
         r'''import time
from contextlib import contextmanager
@contextmanager
def timer():
    s = time.perf_counter()
    yield
    print(f"{(time.perf_counter()-s)*1000:.1f} ms")
with timer():
    sum(range(100000))'''),
        ("Ensure cleanup runs even if the block raises (use try/finally in @contextmanager).", "finally.",
         r'''from contextlib import contextmanager
@contextmanager
def guard():
    try:
        yield
    finally:
        print("cleanup")
try:
    with guard():
        raise ValueError("boom")
except ValueError:
    print("caught")'''),
        ("Use contextlib.suppress to ignore a FileNotFoundError.", "suppress.",
         r'''from contextlib import suppress
import os
with suppress(FileNotFoundError):
    os.remove("not_here.txt")
print("done")'''),
        ("Open two files in a single with statement.", "with a, b:.",
         r'''import os
with open("a.txt", "w") as a, open("b.txt", "w") as b:
    a.write("A"); b.write("B")
print("written")
os.remove("a.txt"); os.remove("b.txt")'''),
        ("Write a manager that temporarily appends to a list and removes the item on exit.", "Mutate then undo.",
         r'''from contextlib import contextmanager
@contextmanager
def temp_item(lst, item):
    lst.append(item)
    try:
        yield lst
    finally:
        lst.remove(item)
data = [1, 2]
with temp_item(data, 99) as d:
    print(d)  # [1, 2, 99]
print(data)   # [1, 2]'''),
    ],
}

CONTENT["regular-expressions"] = {
    "what": (
        "**Regular expressions** (regex) are a mini-language for describing text patterns. With the "
        "`re` module you can search, match, extract, and replace based on patterns like 'one or more "
        "digits' (`\\d+`) or 'an email-ish string'. Patterns are best written as **raw strings** "
        "(`r\"...\"`) so backslashes survive."
    ),
    "why": (
        "Validating input (emails, phone numbers), scraping data out of text, cleaning datasets, and "
        "tokenizing for NLP all lean on regex. A little regex replaces a lot of fiddly string code."
    ),
    "concepts": [
        ("Character classes", "`\\d` digit, `\\w` word char, `\\s` whitespace; `[abc]` a set; `.` any char."),
        ("Quantifiers", "`*` 0+, `+` 1+, `?` 0/1, `{2,4}` a range. Add `?` for non-greedy."),
        ("Anchors", "`^` start, `$` end, `\\b` word boundary."),
        ("Groups", "`( )` capture; `re.findall`/`group()` retrieve captured parts."),
        ("Key functions", "re.search, re.match, re.findall, re.sub, re.split, re.compile."),
        ("Raw strings", "Use `r\"\\d+\"` so Python doesn't eat the backslashes."),
    ],
    "examples": [
        ("Searching and extracting", r'''
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
'''),
        ("Validating and replacing", r'''
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
'''),
        ("Groups, named groups, and compiling", r'''
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
'''),
    ],
    "gotchas": [
        "Always write patterns as raw strings (`r\"\\d+\"`) — otherwise Python interprets `\\d` etc. first.",
        "`re.match` anchors at the START of the string; `re.search` looks anywhere. Mixing them up is common.",
        "`.` does NOT match a newline by default; add the `re.DOTALL` flag if you need it to.",
        "Quantifiers are greedy by default (`.*` grabs as much as possible); add `?` to make them lazy.",
        "`findall` returns the GROUPS if your pattern has capturing parentheses, not the whole match — watch out.",
    ],
    "exercises": [
        ("Extract all numbers from 'a1b22c333' as a list of strings.", "findall with \\d+.",
         r'''import re
print(re.findall(r"\d+", "a1b22c333"))  # ['1', '22', '333']'''),
        ("Check whether 'Hello123' contains any digit.", "search \\d.",
         r'''import re
print(re.search(r"\d", "Hello123") is not None)  # True'''),
        ("Replace every whitespace run in 'a  b   c' with a single space.", "sub \\s+.",
         r'''import re
print(re.sub(r"\s+", " ", "a  b   c"))  # 'a b c' '''),
        ("Validate a simple phone format like 123-456-7890.", "Anchors + {n}.",
         r'''import re
print(re.match(r"^\d{3}-\d{3}-\d{4}$", "123-456-7890") is not None)  # True'''),
        ("Split 'one,two;three four' on commas, semicolons, or spaces.", "split with a class.",
         r'''import re
print(re.split(r"[,; ]+", "one,two;three four"))  # ['one','two','three','four']'''),
        ("Capture the year and month from '2026-06'.", "Two groups.",
         r'''import re
m = re.search(r"(\d{4})-(\d{2})", "2026-06")
print(m.groups())  # ('2026', '06')'''),
        ("Find all words starting with a capital letter in 'The Quick Brown fox'.", "[A-Z]\\w*.",
         r'''import re
print(re.findall(r"\b[A-Z]\w*", "The Quick Brown fox"))  # ['The','Quick','Brown']'''),
        ("Use a non-greedy match to pull 'a' and 'b' from '(a)(b)'.", "\\((.+?)\\).",
         r'''import re
print(re.findall(r"\((.+?)\)", "(a)(b)"))  # ['a', 'b']'''),
    ],
}

CONTENT["datetime"] = {
    "what": (
        "The `datetime` module handles dates and times. Key types: `date` (year/month/day), `time` "
        "(hour/minute/second), `datetime` (both), and `timedelta` (a DURATION you can add/subtract). "
        "You convert between text and datetimes with `strftime` (format to string) and `strptime` "
        "(parse from string)."
    ),
    "why": (
        "Timestamps are everywhere: logs, transactions, time-series data, scheduling. Doing date "
        "math by hand is error-prone (leap years, month lengths, time zones). datetime gets it right."
    ),
    "concepts": [
        ("date / datetime", "Calendar date vs date+time. `datetime.now()` gives the current moment."),
        ("timedelta", "A span of time; add/subtract to shift dates: `today + timedelta(days=7)`."),
        ("strftime", "datetime -> string using format codes (%Y, %m, %d, %H, %M)."),
        ("strptime", "string -> datetime by giving the matching format."),
        ("Difference", "`d2 - d1` returns a timedelta; use `.days` / `.total_seconds()`."),
        ("ISO format", "`.isoformat()` and `date.fromisoformat()` for the standard YYYY-MM-DD."),
    ],
    "examples": [
        ("Creating and inspecting dates", r'''
from datetime import date, datetime, timedelta

today = date(2026, 6, 9)            # a fixed date so output is stable
print("today:", today)
print("year/month/day:", today.year, today.month, today.day)
print("weekday (Mon=0):", today.weekday())   # 1 -> Tuesday

now = datetime(2026, 6, 9, 14, 30, 0)
print("datetime:", now)
print("hour:minute:", now.hour, now.minute)
print("current real time exists too: datetime.now()")
'''),
        ("Date math with timedelta", r'''
from datetime import date, timedelta

start = date(2026, 1, 1)
print("a week later:", start + timedelta(days=7))     # 2026-01-08
print("30 days before:", start - timedelta(days=30))

# Difference between two dates
d1 = date(2026, 6, 9)
d2 = date(2026, 1, 1)
gap = d1 - d2
print("days between:", gap.days)     # 159

# How many days until a deadline?
deadline = date(2026, 12, 25)
print("days to deadline:", (deadline - d1).days)
'''),
        ("Formatting and parsing strings", r'''
from datetime import datetime

dt = datetime(2026, 6, 9, 14, 30)

# strftime: datetime -> formatted string
print(dt.strftime("%Y-%m-%d %H:%M"))     # 2026-06-09 14:30
print(dt.strftime("%A, %B %d, %Y"))      # Tuesday, June 09, 2026

# strptime: string -> datetime (you supply the format)
parsed = datetime.strptime("2026-06-09 14:30", "%Y-%m-%d %H:%M")
print(parsed.year, parsed.hour)          # 2026 14

# ISO 8601 is the safe interchange format
print(dt.isoformat())                    # 2026-06-09T14:30:00
print(datetime.fromisoformat("2026-06-09T14:30:00"))
'''),
    ],
    "gotchas": [
        "strftime/strptime format codes are case-sensitive: %M is minutes, %m is month; %y is 2-digit, %Y is 4-digit.",
        "strptime raises ValueError if the string doesn't EXACTLY match your format string.",
        "Naive datetimes have no time zone. For real apps use timezone-aware datetimes (datetime.now(timezone.utc)).",
        "You can't add an int to a date — you must add a `timedelta`.",
        "Months and years aren't fixed-length, so `timedelta(months=1)` doesn't exist; use libraries (dateutil) for that.",
    ],
    "exercises": [
        ("Print today's date using date.today() (any date is fine).", "date.today().",
         r'''from datetime import date
print(date.today())'''),
        ("Compute the date 100 days after 2026-01-01.", "timedelta(days=100).",
         r'''from datetime import date, timedelta
print(date(2026, 1, 1) + timedelta(days=100))  # 2026-04-11'''),
        ("How many days are between 2026-01-01 and 2026-12-31?", "Subtract dates.",
         r'''from datetime import date
print((date(2026, 12, 31) - date(2026, 1, 1)).days)  # 364'''),
        ("Format datetime(2026,6,9,9,5) as 'YYYY-MM-DD HH:MM'.", "strftime.",
         r'''from datetime import datetime
print(datetime(2026, 6, 9, 9, 5).strftime("%Y-%m-%d %H:%M"))  # 2026-06-09 09:05'''),
        ("Parse '09/06/2026' (DD/MM/YYYY) into a date object.", "strptime with %d/%m/%Y.",
         r'''from datetime import datetime
print(datetime.strptime("09/06/2026", "%d/%m/%Y").date())  # 2026-06-09'''),
        ("Find the weekday name of 2026-06-09.", "strftime %A.",
         r'''from datetime import date
print(date(2026, 6, 9).strftime("%A"))  # Tuesday'''),
        ("Given a birthdate 2000-06-09, compute age in whole years as of 2026-06-09.", "Year diff with adjustment.",
         r'''from datetime import date
b, t = date(2000, 6, 9), date(2026, 6, 9)
age = t.year - b.year - ((t.month, t.day) < (b.month, b.day))
print(age)  # 26'''),
        ("Convert datetime(2026,6,9,14,30) to ISO format and back.", "isoformat / fromisoformat.",
         r'''from datetime import datetime
s = datetime(2026, 6, 9, 14, 30).isoformat()
print(s, "->", datetime.fromisoformat(s))'''),
    ],
}

CONTENT["json-and-csv"] = {
    "what": (
        "**JSON** and **CSV** are the two most common data interchange formats. JSON (JavaScript "
        "Object Notation) maps cleanly to Python dicts/lists — use `json.dumps`/`loads` for "
        "strings and `json.dump`/`load` for files. CSV (comma-separated values) is tabular text — "
        "use the `csv` module (or pandas later) to read/write rows."
    ),
    "why": (
        "APIs speak JSON; spreadsheets and datasets ship as CSV. Reading and writing both is a daily "
        "task in data work — loading a dataset, saving results, or talking to a web service."
    ),
    "concepts": [
        ("json.dumps / loads", "Python object <-> JSON STRING."),
        ("json.dump / load", "Python object <-> JSON FILE (note: no 's')."),
        ("Type mapping", "dict<->object, list<->array, str/int/float/bool/None map naturally."),
        ("csv.reader / writer", "Row-by-row lists; remember newline='' when opening files."),
        ("csv.DictReader / DictWriter", "Treat rows as dicts keyed by the header row."),
        ("Pretty printing", "json.dumps(obj, indent=2) for readable output."),
    ],
    "examples": [
        ("JSON: strings and files", r'''
import json

data = {"name": "Ada", "skills": ["python", "math"], "age": 36, "active": True}

# Object -> JSON string
text = json.dumps(data)
print(text)                          # {"name": "Ada", ...}
print(json.dumps(data, indent=2))    # pretty, multi-line

# JSON string -> object
back = json.loads(text)
print(back["skills"][0])             # python
print(type(back))                    # <class 'dict'>

# Save to / load from a file
import os
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
with open("data.json", "r", encoding="utf-8") as f:
    print(json.load(f)["name"])      # Ada
os.remove("data.json")
'''),
        ("CSV with the csv module", r'''
import csv, io

rows = [["name", "age"], ["Ada", "36"], ["Bo", "19"]]

# Write CSV to an in-memory buffer (works just like a file)
buf = io.StringIO()
writer = csv.writer(buf)
writer.writerows(rows)
print(buf.getvalue())     # name,age\nAda,36\nBo,19

# Read it back
buf.seek(0)
for record in csv.reader(buf):
    print(record)         # ['name', 'age'], then ['Ada', '36'], ...
'''),
        ("CSV as dictionaries (DictReader / DictWriter)", r'''
import csv, io

text = "name,score\nAda,95\nBo,80\n"

# DictReader: each row becomes a dict keyed by the header
reader = csv.DictReader(io.StringIO(text))
for row in reader:
    print(row["name"], "->", int(row["score"]))

# DictWriter: write dicts back out
buf = io.StringIO()
writer = csv.DictWriter(buf, fieldnames=["name", "score"])
writer.writeheader()
writer.writerow({"name": "Cy", "score": 100})
print(buf.getvalue())
'''),
    ],
    "gotchas": [
        "`json.dump`/`load` work with FILES; `json.dumps`/`loads` work with STRINGS (the 's' = string).",
        "JSON keys are always strings: `json.loads('{\"1\": 2}')` gives key '1', not int 1.",
        "JSON has no tuples, sets, or datetimes — convert them (e.g. list, isoformat) before dumping.",
        "When opening CSV files, pass `newline=''` or you may get blank lines between rows on Windows.",
        "CSV values are all strings — cast numbers yourself (`int(row['score'])`).",
    ],
    "exercises": [
        ("Convert the dict {'a':1,'b':[2,3]} to a JSON string.", "json.dumps.",
         r'''import json
print(json.dumps({"a": 1, "b": [2, 3]}))  # {"a": 1, "b": [2, 3]}'''),
        ("Parse the JSON string '{\"x\": 10}' and print x.", "json.loads.",
         r'''import json
print(json.loads('{"x": 10}')["x"])  # 10'''),
        ("Pretty-print {'name':'Ada','age':36} with 2-space indentation.", "indent=2.",
         r'''import json
print(json.dumps({"name": "Ada", "age": 36}, indent=2))'''),
        ("Write a dict to data.json and read it back.", "dump/load.",
         r'''import json, os
with open("d.json", "w") as f:
    json.dump({"ok": True}, f)
with open("d.json") as f:
    print(json.load(f))
os.remove("d.json")'''),
        ("Write two rows ['a','b'] and ['1','2'] to a CSV string.", "csv.writer + StringIO.",
         r'''import csv, io
buf = io.StringIO()
csv.writer(buf).writerows([["a", "b"], ["1", "2"]])
print(buf.getvalue())'''),
        ("Read CSV text 'x,y\\n1,2\\n3,4' and sum all the numbers.", "csv.reader, skip header.",
         r'''import csv, io
text = "x,y\n1,2\n3,4"
r = csv.reader(io.StringIO(text))
next(r)  # skip header
print(sum(int(c) for row in r for c in row))  # 10'''),
        ("Use DictReader to read 'name,age\\nAda,36' and print the name.", "DictReader.",
         r'''import csv, io
r = csv.DictReader(io.StringIO("name,age\nAda,36"))
print(next(r)["name"])  # Ada'''),
        ("Round-trip a list of dicts through JSON (dumps then loads).", "dumps/loads.",
         r'''import json
data = [{"id": 1}, {"id": 2}]
print(json.loads(json.dumps(data)) == data)  # True'''),
    ],
}

CONTENT["apis-with-requests"] = {
    "what": (
        "Web **APIs** let your program talk to services over HTTP. You send a **request** (usually "
        "GET to read or POST to send data) to a URL and get back a **response** (often JSON). The "
        "`requests` library is the most popular way to do this; Python's built-in `urllib` works "
        "too. Key ideas: status codes, query parameters, headers, and JSON bodies."
    ),
    "why": (
        "Almost every real app integrates with APIs: weather, payments, maps, LLMs, databases. "
        "Knowing how to call them, pass parameters, handle errors, and parse JSON responses is a "
        "core practical skill."
    ),
    "deps": ["requests"],
    "concepts": [
        ("HTTP methods", "GET (read), POST (create/send), PUT/PATCH (update), DELETE (remove)."),
        ("Status codes", "2xx success, 3xx redirect, 4xx your fault, 5xx server's fault. 200 = OK, 404 = not found."),
        ("Query parameters", "`?key=value` extras; pass as `params={...}`."),
        ("Headers", "Metadata like auth tokens and content type."),
        ("JSON body", "`response.json()` parses the response; `json=...` sends a JSON body."),
        ("Error handling", "Check `response.status_code` or call `raise_for_status()`; handle timeouts."),
    ],
    "examples": [
        ("Anatomy of an API call (offline-safe demo)", r'''
# The SHAPE of a typical requests call (no network needed to learn it).
# When online with `pip install requests`, you would write:
#
#   import requests
#   resp = requests.get("https://api.github.com", timeout=10)
#   print(resp.status_code)          # 200 if OK
#   print(resp.headers["content-type"])
#   data = resp.json()               # parse JSON body into a dict
#   print(data["current_user_url"])
#
# Every API call has these parts:
for part in ["URL", "method (GET/POST)", "status code", "JSON body"]:
    print("part:", part)
'''),
        ("Make a real request if possible, else explain (fully runnable)", r'''
import json

def fetch_json(url, timeout=10):
    """Try requests; fall back to urllib; never crash if offline."""
    try:
        try:
            import requests
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()       # raise on 4xx/5xx
            return r.json()
        except ImportError:
            # requests not installed -> use the standard library
            from urllib.request import urlopen
            with urlopen(url, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": type(e).__name__}   # offline / blocked / bad URL / not JSON

result = fetch_json("https://httpbin.org/json")
print(type(result).__name__)
print(list(result)[:3] if isinstance(result, dict) else result)
'''),
        ("Sending parameters, headers, and POST bodies (shown as data)", r'''
# Building the pieces of a request (no network needed to learn the structure):
params = {"q": "python", "page": 2}        # -> ?q=python&page=2
headers = {"Authorization": "Bearer TOKEN", "Accept": "application/json"}
payload = {"title": "hello", "done": False}

from urllib.parse import urlencode
print("query string:", urlencode(params))   # q=python&page=2
print("headers:", headers)
print("json body:", payload)

# With requests you would write:
#   requests.get(url, params=params, headers=headers, timeout=10)
#   requests.post(url, json=payload, headers=headers, timeout=10)
print("Remember: always pass timeout=, and check status_code / raise_for_status().")
'''),
    ],
    "gotchas": [
        "ALWAYS pass a `timeout=` — without it a hung server freezes your program forever.",
        "A 200 response can still contain an error payload; check the body, not just the status code.",
        "`response.json()` raises if the body isn't valid JSON — wrap it or check the content-type.",
        "Don't hardcode API keys in code you share; load them from environment variables.",
        "Respect rate limits and add retries/backoff for production calls; hammering an API gets you blocked.",
    ],
    "exercises": [
        ("Build the query string for params {'q':'cats','limit':5} using urllib.", "urlencode.",
         r'''from urllib.parse import urlencode
print(urlencode({"q": "cats", "limit": 5}))  # q=cats&limit=5'''),
        ("Write a function that returns 'ok' for status 200 and 'error' otherwise.", "Compare to 200.",
         r'''def check(status):
    return "ok" if status == 200 else "error"
print(check(200), check(404))  # ok error'''),
        ("Parse this API JSON string and print the user's name: '{\"user\":{\"name\":\"Ada\"}}'.", "json.loads.",
         r'''import json
data = json.loads('{"user": {"name": "Ada"}}')
print(data["user"]["name"])  # Ada'''),
        ("Categorize a status code into a class (2xx/3xx/4xx/5xx). Test 404.", "code // 100.",
         r'''def klass(code):
    return f"{code // 100}xx"
print(klass(404))  # 4xx'''),
        ("Write fetch that returns {'error': ...} instead of raising on failure.", "try/except.",
         r'''def fetch(fn):
    try:
        return fn()
    except Exception as e:
        return {"error": str(e)}
print(fetch(lambda: 1 / 0))'''),
        ("Read an API key from the environment variable API_KEY (default 'missing').", "os.environ.get.",
         r'''import os
print(os.environ.get("API_KEY", "missing"))'''),
        ("Given a dict response, safely get response['data']['items'] or [].", "Nested get.",
         r'''resp = {"data": {}}
print(resp.get("data", {}).get("items", []))  # []'''),
        ("Make a real GET request if requests is installed and network is up; else print a message.", "Guarded.",
         r'''try:
    import requests
    r = requests.get("https://httpbin.org/get", timeout=5)
    print("status:", r.status_code)
except Exception as e:
    print("skipped:", type(e).__name__)'''),
    ],
}

CONTENT["multithreading-and-multiprocessing"] = {
    "what": (
        "Two ways to do more than one thing at once. **Threads** share memory and are great for "
        "**I/O-bound** work (waiting on files, network) — but Python's **GIL** means threads don't "
        "speed up pure CPU work. **Processes** each have their own Python interpreter, so they DO "
        "use multiple CPU cores — ideal for **CPU-bound** work. `concurrent.futures` gives a simple, "
        "unified interface to both."
    ),
    "why": (
        "Downloading 100 URLs, reading many files, or crunching numbers across cores: concurrency "
        "can turn minutes into seconds. Knowing the I/O-bound (threads) vs CPU-bound (processes) "
        "distinction is the key to choosing the right tool."
    ),
    "concepts": [
        ("GIL", "Global Interpreter Lock: only one thread runs Python bytecode at a time."),
        ("I/O-bound vs CPU-bound", "Waiting (network/disk) vs computing (math). Threads help the first; processes the second."),
        ("Thread", "Lightweight, shares memory; use threading or ThreadPoolExecutor."),
        ("Process", "Separate memory and interpreter; use multiprocessing or ProcessPoolExecutor."),
        ("concurrent.futures", "Executor.map / submit -> futures; the easiest high-level API."),
        ("Race conditions", "Shared mutable state across threads needs a Lock to stay consistent."),
    ],
    "examples": [
        ("Threads for I/O-bound work (ThreadPoolExecutor)", r'''
import time
from concurrent.futures import ThreadPoolExecutor

def fake_download(url):
    time.sleep(0.2)                 # pretend we're waiting on the network
    return f"{url} -> 200"

urls = [f"site{i}.com" for i in range(5)]

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fake_download, urls))   # run concurrently
print(results)
print(f"threaded: {time.perf_counter() - start:.2f}s (≈0.2s, not 1.0s)")
'''),
        ("Processes for CPU-bound work (ProcessPoolExecutor)", r'''
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))   # pure CPU work

if __name__ == "__main__":          # required guard for multiprocessing
    tasks = [200_000, 200_000, 200_000, 200_000]
    with ProcessPoolExecutor() as pool:
        results = list(pool.map(heavy, tasks))
    print("sums:", results[0], "(x4)")
    print("Processes use multiple CPU cores, sidestepping the GIL.")
'''),
        ("Threads + a Lock to avoid race conditions", r'''
import threading

counter = 0
lock = threading.Lock()

def increment_many():
    global counter
    for _ in range(100_000):
        with lock:                  # only one thread updates at a time
            counter += 1

threads = [threading.Thread(target=increment_many) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()          # wait for all to finish
print("counter:", counter)          # 400000 (correct, thanks to the lock)
'''),
    ],
    "gotchas": [
        "Threads do NOT speed up CPU-bound Python code because of the GIL — use processes for that.",
        "multiprocessing code must be guarded by `if __name__ == '__main__':` (especially on Windows/macOS).",
        "Shared mutable state across threads without a Lock causes race conditions (lost updates).",
        "Always `join()` threads/processes (or use a `with` executor) so the program waits for them.",
        "Processes don't share memory — data is pickled to/from them, which has overhead and requires picklable objects.",
    ],
    "exercises": [
        ("Use ThreadPoolExecutor.map to square [1,2,3,4] concurrently.", "pool.map.",
         r'''from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor() as p:
    print(list(p.map(lambda x: x * x, [1, 2, 3, 4])))  # [1,4,9,16]'''),
        ("Run a function in a single thread and join it.", "threading.Thread.",
         r'''import threading
def task(): print("working")
t = threading.Thread(target=task)
t.start(); t.join()'''),
        ("Decide: would you use threads or processes for downloading 50 files? Why?", "",
         r'''#md
**Threads.** Downloading is **I/O-bound** (mostly waiting on the network), so the
GIL is released during the wait and many threads overlap their waiting. Processes
would add overhead for no benefit here.'''),
        ("Decide: threads or processes for multiplying huge matrices? Why?", "",
         r'''#md
**Processes.** That's **CPU-bound** work. The GIL prevents threads from running
Python bytecode in parallel, so only processes (separate interpreters) use
multiple cores.'''),
        ("Protect a shared counter with a Lock across two threads.", "with lock.",
         r'''import threading
n, lock = 0, threading.Lock()
def add():
    global n
    for _ in range(10000):
        with lock: n += 1
ts = [threading.Thread(target=add) for _ in range(2)]
[t.start() for t in ts]; [t.join() for t in ts]
print(n)  # 20000'''),
        ("Use ProcessPoolExecutor to compute squares of [1,2,3] (guard with __main__).", "ProcessPool.",
         r'''from concurrent.futures import ProcessPoolExecutor
def sq(x): return x * x
if __name__ == "__main__":
    with ProcessPoolExecutor() as p:
        print(list(p.map(sq, [1, 2, 3])))  # [1, 4, 9]'''),
        ("Submit a single task with executor.submit and get its result via future.result().", "submit.",
         r'''from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor() as p:
    fut = p.submit(pow, 2, 10)
    print(fut.result())  # 1024'''),
        ("Time how much faster 4 concurrent 0.1s sleeps are vs sequential.", "Compare timings.",
         r'''import time
from concurrent.futures import ThreadPoolExecutor
def wait(_): time.sleep(0.1)
s = time.perf_counter()
with ThreadPoolExecutor(4) as p: list(p.map(wait, range(4)))
print(f"~{time.perf_counter()-s:.2f}s (≈0.1, not 0.4)")'''),
    ],
}

CONTENT["logging"] = {
    "what": (
        "**Logging** records what your program does while it runs. It's far better than scattering "
        "`print()` calls: you get **severity levels** (DEBUG, INFO, WARNING, ERROR, CRITICAL), "
        "timestamps, the source module, and you can route messages to files, the console, or both — "
        "and turn the detail up or down without editing your code."
    ),
    "why": (
        "When something breaks in production (or in a long training run), logs are how you find out "
        "what happened. Good logging turns 'it crashed somehow' into 'here's exactly where and why'. "
        "It's a habit that separates hobby scripts from real software."
    ),
    "concepts": [
        ("Levels", "DEBUG < INFO < WARNING < ERROR < CRITICAL; set a threshold and below it is hidden."),
        ("Logger", "Get one with `logging.getLogger(__name__)`; don't just use the root logger."),
        ("Handlers", "Where logs go: StreamHandler (console), FileHandler (file), etc."),
        ("Formatter", "Controls the layout: time, level, name, message."),
        ("basicConfig", "Quick one-call setup for simple scripts."),
        ("exception()", "Logs an ERROR plus the full traceback inside an except block."),
    ],
    "examples": [
        ("Quick start with basicConfig", r'''
import logging

logging.basicConfig(
    level=logging.DEBUG,                                   # show DEBUG and above
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
    force=True,                                            # re-apply config
)

logging.debug("detailed info for diagnosing problems")
logging.info("things are working as expected")
logging.warning("something unexpected, but we continue")
logging.error("a serious problem occurred")
# Output goes to the console (stderr) with timestamp and level
'''),
        ("Levels and why print() loses", r'''
import logging
logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s", force=True)

# With the threshold at WARNING, DEBUG and INFO are silently skipped...
logging.debug("you will NOT see this")
logging.info("you will NOT see this either")
logging.warning("you WILL see this")     # WARNING: ...
logging.error("and this")                # ERROR: ...

# The win: change ONE line (level=...) to get more/less detail,
# no need to delete print() statements all over your code.
'''),
        ("Named loggers and logging exceptions with tracebacks", r'''
import logging
logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s: %(message)s", force=True)

log = logging.getLogger("myapp")        # named logger (best practice)

def divide(a, b):
    log.info("dividing %s by %s", a, b)  # lazy %-formatting (efficient)
    try:
        return a / b
    except ZeroDivisionError:
        log.exception("division failed")  # logs ERROR + full traceback
        return None

print(divide(10, 2))   # 5.0
print(divide(1, 0))    # logs the traceback, returns None
'''),
    ],
    "gotchas": [
        "Call `basicConfig` ONCE, early; later calls do nothing if logging is already configured.",
        "Use lazy formatting: `log.info('x=%s', x)` not `log.info(f'x={x}')` — args are only formatted if the level is active.",
        "Default level is WARNING, so INFO/DEBUG messages won't show until you lower the threshold.",
        "Use `log.exception(...)` inside `except` blocks to capture the traceback automatically.",
        "Don't use logging to print normal program OUTPUT for users — that's what print() is for; logging is for diagnostics.",
    ],
    "exercises": [
        ("Configure logging at INFO level and log an info message.", "basicConfig + logging.info.",
         r'''import logging
logging.basicConfig(level=logging.INFO)
logging.info("hello logs")'''),
        ("Show that a debug message is hidden when level is WARNING.", "Set level high.",
         r'''import logging
logging.basicConfig(level=logging.WARNING, force=True)
logging.debug("hidden")
logging.warning("shown")'''),
        ("Create a named logger 'app' and log a warning through it.", "getLogger.",
         r'''import logging
logging.basicConfig(level=logging.WARNING, force=True)
log = logging.getLogger("app")
log.warning("careful")'''),
        ("Use a custom format showing only LEVEL: message.", "format=.",
         r'''import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", force=True)
logging.info("formatted")'''),
        ("Log an exception with traceback inside an except block.", "log.exception.",
         r'''import logging
logging.basicConfig(level=logging.ERROR, force=True)
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("boom")'''),
        ("Use lazy %-style arguments to log a value.", "log.info('x=%s', x).",
         r'''import logging
logging.basicConfig(level=logging.INFO, force=True)
x = 42
logging.info("x = %s", x)'''),
        ("List the five standard logging levels from lowest to highest.", "",
         r'''#md
**DEBUG → INFO → WARNING → ERROR → CRITICAL.** Setting the level to one value
shows that level and everything more severe; less severe messages are dropped.'''),
        ("Log to a file instead of the console.", "filename= in basicConfig.",
         r'''import logging, os
logging.basicConfig(filename="app.log", level=logging.INFO, force=True)
logging.info("to file")
logging.shutdown()
print(os.path.exists("app.log"))  # True
os.remove("app.log")'''),
    ],
}
