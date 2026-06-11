# 19 — Inheritance, Polymorphism and Encapsulation

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

The three classic OOP pillars (beyond classes themselves): **Inheritance** lets a child class reuse and extend a parent (`class Cat(Animal):`). **Polymorphism** lets different classes respond to the same method name in their own way. **Encapsulation** hides internal details behind a clean interface (using `_protected` and `__private` naming, and properties). **Abstraction** exposes only what matters.

## Why it matters

These pillars let you build large systems without repeating code, swap implementations freely (polymorphism is why `len()` works on lists and strings), and protect invariants. Frameworks rely on you subclassing their base classes.

## Key concepts

- **Inheritance** — `class Child(Parent):` gets the parent's attributes/methods for free.
- **super()** — Call the parent's version of a method, e.g. `super().__init__(...)`.
- **Method overriding** — Redefine a parent method in the child to change behavior.
- **Polymorphism** — Same method name, different behavior per class — duck typing.
- **Encapsulation** — `_name` (protected by convention), `__name` (name-mangled), properties.
- **Abstraction** — Hide complex internals; expose a simple, stable interface.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Always call `super().__init__()` in a child's __init__ if the parent needs setup, or its attributes won't exist.
- ⚠️ `_single_underscore` is only a convention ('please don't touch'); `__double` triggers name mangling.
- ⚠️ Python uses duck typing — you don't need a shared base class for polymorphism, just the same method name.
- ⚠️ Deep inheritance trees get confusing fast; prefer composition (has-a) over inheritance (is-a) when unsure.
- ⚠️ Overriding a method but forgetting to call `super()` can skip important parent behavior.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

