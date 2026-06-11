# 19 — Inheritance, Polymorphism and Encapsulation: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create Shape with area() returning 0, and Square(Shape) overriding area().

*Hint: Override.*

<details>
<summary>✅ Solution</summary>

```python
class Shape:
    def area(self): return 0
class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
print(Square(4).area())  # 16
```

</details>

## Exercise 2

Make Vehicle with __init__(wheels) and Car that calls super().__init__(4).

*Hint: super().*

<details>
<summary>✅ Solution</summary>

```python
class Vehicle:
    def __init__(self, wheels): self.wheels = wheels
class Car(Vehicle):
    def __init__(self): super().__init__(4)
print(Car().wheels)  # 4
```

</details>

## Exercise 3

Write three classes with a sound() method and loop calling it (polymorphism).

*Hint: Duck typing.*

<details>
<summary>✅ Solution</summary>

```python
class A:
    def sound(self): return "a"
class B:
    def sound(self): return "b"
for o in [A(), B()]:
    print(o.sound())
```

</details>

## Exercise 4

Use isinstance to check a Dog instance is also an Animal.

*Hint: isinstance(obj, Cls).*

<details>
<summary>✅ Solution</summary>

```python
class Animal: pass
class Dog(Animal): pass
print(isinstance(Dog(), Animal))  # True
```

</details>

## Exercise 5

Add a read-only property full_name to a Person with first and last names.

*Hint: @property.*

<details>
<summary>✅ Solution</summary>

```python
class Person:
    def __init__(self, f, l): self.f, self.l = f, l
    @property
    def full_name(self): return f"{self.f} {self.l}"
print(Person("Ada", "Lovelace").full_name)
```

</details>

## Exercise 6

Make Employee(Person) that adds a salary and a raise_pay(pct) method.

*Hint: Inherit + extend.*

<details>
<summary>✅ Solution</summary>

```python
class Person:
    def __init__(self, name): self.name = name
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name); self.salary = salary
    def raise_pay(self, pct): self.salary *= 1 + pct / 100
e = Employee("Bo", 100); e.raise_pay(10)
print(e.salary)  # 110.0
```

</details>

## Exercise 7

Encapsulate a private __pin in a Card class; expose check_pin(guess).

*Hint: __name mangling.*

<details>
<summary>✅ Solution</summary>

```python
class Card:
    def __init__(self, pin): self.__pin = pin
    def check_pin(self, guess): return guess == self.__pin
print(Card(1234).check_pin(1234))  # True
```

</details>

## Exercise 8

Override __init__ in a child but keep the parent's attribute via super().

*Hint: super().__init__.*

<details>
<summary>✅ Solution</summary>

```python
class Base:
    def __init__(self): self.kind = "base"
class Child(Base):
    def __init__(self):
        super().__init__()
        self.extra = 1
c = Child()
print(c.kind, c.extra)  # base 1
```

</details>

