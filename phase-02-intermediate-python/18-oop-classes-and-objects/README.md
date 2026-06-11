# 18 — OOP: Classes and Objects

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Object-Oriented Programming (OOP)** organizes code around **objects** — bundles of data (**attributes**) and behavior (**methods**). A **class** is the blueprint; an **object** (or instance) is a concrete thing built from it. `__init__` is the setup method that runs when you create an instance, and `self` refers to the specific instance.

## Why it matters

OOP models real-world things naturally (a BankAccount, a User, a Model). It groups related data and functions, prevents global-variable spaghetti, and underpins almost every Python library you'll use — scikit-learn estimators, PyTorch modules, etc.

## Key concepts

- **class** — A blueprint: `class Dog:`. Convention: ClassNames use CapWords.
- **object / instance** — A specific thing made from a class: `d = Dog()`.
- **__init__** — The initializer; sets up attributes when an instance is created.
- **self** — The first parameter of every method; refers to the current instance.
- **Instance attribute** — Data unique to each object: `self.name`.
- **Class attribute** — Data shared by ALL instances, defined in the class body.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Forgetting `self` as the first method parameter -> 'takes 0 positional arguments but 1 was given'.
- ⚠️ Mutable class attributes (e.g. a shared list) are shared by ALL instances — usually you want it in __init__.
- ⚠️ `__init__` doesn't 'return' the object; it just configures `self`. Returning anything but None raises an error.
- ⚠️ Setting `instance.attr = x` creates an instance attribute that shadows a class attribute of the same name.
- ⚠️ Accessing an attribute that was never set raises AttributeError — initialize everything in __init__.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

