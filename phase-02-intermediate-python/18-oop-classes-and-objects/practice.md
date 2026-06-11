# 18 — OOP: Classes and Objects: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create a class Circle with radius, and a method area() returning pi*r*r. Test radius 2.

*Hint: Use 3.14159 or math.pi.*

<details>
<summary>✅ Solution</summary>

```python
import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
print(round(Circle(2).area(), 2))  # 12.57
```

</details>

## Exercise 2

Make a Person class with name and greet() returning 'Hi, I'm <name>'.

*Hint: f-string with self.name.*

<details>
<summary>✅ Solution</summary>

```python
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hi, I'm {self.name}"
print(Person("Ada").greet())
```

</details>

## Exercise 3

Build a Rectangle class with width/height and methods area() and perimeter().

*Hint: Two methods.*

<details>
<summary>✅ Solution</summary>

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
r = Rectangle(3, 4)
print(r.area(), r.perimeter())  # 12 14
```

</details>

## Exercise 4

Give Dog a class attribute legs=4 and show two instances share it.

*Hint: Class attribute.*

<details>
<summary>✅ Solution</summary>

```python
class Dog:
    legs = 4
a, b = Dog(), Dog()
print(a.legs, b.legs)  # 4 4
```

</details>

## Exercise 5

Create a Stack class with push, pop, and is_empty using an internal list.

*Hint: Wrap a list.*

<details>
<summary>✅ Solution</summary>

```python
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        return self._items.pop()
    def is_empty(self):
        return len(self._items) == 0
s = Stack(); s.push(1); s.push(2)
print(s.pop(), s.is_empty())  # 2 False
```

</details>

## Exercise 6

Add a method to BankAccount that returns a formatted string '<owner>: $<balance>'.

*Hint: f-string.*

<details>
<summary>✅ Solution</summary>

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance
    def summary(self):
        return f"{self.owner}: ${self.balance}"
print(BankAccount("Bo", 50).summary())
```

</details>

## Exercise 7

Make a Counter class whose increment() bumps an instance count and value() returns it.

*Hint: Instance attribute.*

<details>
<summary>✅ Solution</summary>

```python
class Counter:
    def __init__(self):
        self.n = 0
    def increment(self):
        self.n += 1
    def value(self):
        return self.n
c = Counter(); c.increment(); c.increment()
print(c.value())  # 2
```

</details>

## Exercise 8

Create a Temperature class storing celsius and a method to_fahrenheit().

*Hint: F = C*9/5+32.*

<details>
<summary>✅ Solution</summary>

```python
class Temperature:
    def __init__(self, c):
        self.c = c
    def to_fahrenheit(self):
        return self.c * 9 / 5 + 32
print(Temperature(100).to_fahrenheit())  # 212.0
```

</details>

