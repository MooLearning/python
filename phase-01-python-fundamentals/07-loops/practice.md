# 07 — Loops: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Print the numbers 1 to 5, each on its own line.

*Hint: range(1, 6).*

<details>
<summary>✅ Solution</summary>

```python
for i in range(1, 6):
    print(i)
```

</details>

## Exercise 2

Sum the numbers from 1 to 100 and print the total.

*Hint: range(1, 101) and a running sum.*

<details>
<summary>✅ Solution</summary>

```python
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050
```

</details>

## Exercise 3

Print only the even numbers from 1 to 20 using continue.

*Hint: Skip when n % 2 != 0.*

<details>
<summary>✅ Solution</summary>

```python
for n in range(1, 21):
    if n % 2 != 0:
        continue
    print(n, end=" ")
print()
```

</details>

## Exercise 4

Use a while loop to count down from 5 to 1.

*Hint: Decrement each pass.*

<details>
<summary>✅ Solution</summary>

```python
n = 5
while n >= 1:
    print(n)
    n -= 1
```

</details>

## Exercise 5

Print each fruit with its 1-based position using enumerate.

*Hint: enumerate(..., start=1).*

<details>
<summary>✅ Solution</summary>

```python
for i, f in enumerate(["apple", "pear", "fig"], start=1):
    print(i, f)
```

</details>

## Exercise 6

Find the first number divisible by 7 between 20 and 40 and stop.

*Hint: break when found.*

<details>
<summary>✅ Solution</summary>

```python
for n in range(20, 41):
    if n % 7 == 0:
        print(n)  # 21
        break
```

</details>

## Exercise 7

Print the multiplication table (1-5) for 3, e.g. '3 x 1 = 3'.

*Hint: Loop 1..5.*

<details>
<summary>✅ Solution</summary>

```python
for i in range(1, 6):
    print(f"3 x {i} = {3 * i}")
```

</details>

## Exercise 8

Print a 3x3 grid of '*' using nested loops.

*Hint: A loop inside a loop.*

<details>
<summary>✅ Solution</summary>

```python
for row in range(3):
    for col in range(3):
        print("*", end="")
    print()
```

</details>

