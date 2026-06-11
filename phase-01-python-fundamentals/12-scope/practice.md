# 12 — Scope (local, global, nonlocal): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Predict the output: define x=5 globally, a function that sets x=10 locally and prints it, then print x outside.

*Hint: Local assignment shadows global.*

<details>
<summary>✅ Solution</summary>

```python
x = 5
def f():
    x = 10
    print(x)  # 10
f()
print(x)      # 5
```

</details>

## Exercise 2

Use global to make a function increase a module-level count by 1.

*Hint: global count.*

<details>
<summary>✅ Solution</summary>

```python
count = 0
def inc():
    global count
    count += 1
inc(); inc()
print(count)  # 2
```

</details>

## Exercise 3

Write a counter using a closure and nonlocal that returns 1, 2, 3 on successive calls.

*Hint: nonlocal in a nested function.*

<details>
<summary>✅ Solution</summary>

```python
def make_counter():
    n = 0
    def step():
        nonlocal n
        n += 1
        return n
    return step
c = make_counter()
print(c(), c(), c())  # 1 2 3
```

</details>

## Exercise 4

Explain why reading then assigning a global inside a function (without 'global') errors.

<details>
<summary>✅ Solution</summary>

Assigning to the name anywhere in the function marks it **local for the entire
function body**. So the earlier read happens before the local is assigned →
`UnboundLocalError`. Declare `global name` (or don't reassign it) to fix.

</details>

## Exercise 5

Show that you can READ a global inside a function without the global keyword.

*Hint: Just reference it.*

<details>
<summary>✅ Solution</summary>

```python
msg = "hi"
def show():
    print(msg)  # reading is fine
show()  # hi
```

</details>

## Exercise 6

What does the built-in `len` refer to inside a function — which letter of LEGB?

*Hint: B.*

<details>
<summary>✅ Solution</summary>

**B (Built-in).** `len` isn't local, enclosing, or global in your file, so Python
finds it last in the built-in scope. (Don't create a variable named `len` or you
shadow it!)

</details>

## Exercise 7

Demonstrate a loop variable still existing after the loop ends.

*Hint: Print i after the for loop.*

<details>
<summary>✅ Solution</summary>

```python
for i in range(3):
    pass
print(i)  # 2  -> the loop variable leaks out
```

</details>

## Exercise 8

Refactor a global-counter function into one that takes the count and returns count+1 (no global).

*Hint: Pure function style.*

<details>
<summary>✅ Solution</summary>

```python
def inc(count):
    return count + 1
c = 0
c = inc(c)
c = inc(c)
print(c)  # 2
```

</details>

