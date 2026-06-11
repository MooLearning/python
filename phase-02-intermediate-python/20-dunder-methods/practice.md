# 20 — Dunder (Magic) Methods: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Give a class a __str__ so print(obj) shows 'Item(<name>)'.

*Hint: Return an f-string.*

<details>
<summary>✅ Solution</summary>

```python
class Item:
    def __init__(self, name): self.name = name
    def __str__(self): return f"Item({self.name})"
print(Item("pen"))  # Item(pen)
```

</details>

## Exercise 2

Implement __len__ so len(box) returns the number of items it holds.

*Hint: Wrap a list.*

<details>
<summary>✅ Solution</summary>

```python
class Box:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)
print(len(Box([1, 2, 3])))  # 3
```

</details>

## Exercise 3

Add __eq__ so two Coord(1,2) objects compare equal.

*Hint: Compare attributes.*

<details>
<summary>✅ Solution</summary>

```python
class Coord:
    def __init__(self, x, y): self.x, self.y = x, y
    def __eq__(self, o): return (self.x, self.y) == (o.x, o.y)
print(Coord(1, 2) == Coord(1, 2))  # True
```

</details>

## Exercise 4

Implement __add__ so Money(100)+Money(50) gives Money(150).

*Hint: Return new instance.*

<details>
<summary>✅ Solution</summary>

```python
class Money:
    def __init__(self, c): self.c = c
    def __add__(self, o): return Money(self.c + o.c)
    def __repr__(self): return f"Money({self.c})"
print(Money(100) + Money(50))  # Money(150)
```

</details>

## Exercise 5

Make objects sortable by defining __lt__ on a class with a 'score'.

*Hint: Compare score.*

<details>
<summary>✅ Solution</summary>

```python
class P:
    def __init__(self, s): self.s = s
    def __lt__(self, o): return self.s < o.s
    def __repr__(self): return f"P({self.s})"
print(sorted([P(3), P(1), P(2)]))
```

</details>

## Exercise 6

Implement __getitem__ so playlist[0] returns the first song.

*Hint: Index into a list.*

<details>
<summary>✅ Solution</summary>

```python
class Playlist:
    def __init__(self, songs): self.songs = songs
    def __getitem__(self, i): return self.songs[i]
print(Playlist(["a", "b"])[0])  # a
```

</details>

## Exercise 7

Add __repr__ that returns valid constructor code for a Point.

*Hint: Return 'Point(x, y)'.*

<details>
<summary>✅ Solution</summary>

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f"Point({self.x}, {self.y})"
print(repr(Point(1, 2)))  # Point(1, 2)
```

</details>

## Exercise 8

Make a class callable with __call__ so obj(5) returns 5 squared.

*Hint: Define __call__.*

<details>
<summary>✅ Solution</summary>

```python
class Square:
    def __call__(self, x): return x * x
sq = Square()
print(sq(5))  # 25
```

</details>

