# 01 — Installation and Setup: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Print the exact text `Hello, World!` to the screen.

*Hint: Use the print() function.*

<details>
<summary>✅ Solution</summary>

```python
print("Hello, World!")
```

</details>

## Exercise 2

Print the version of Python you are running (just the number, e.g. 3.14.5).

*Hint: sys.version starts with the number.*

<details>
<summary>✅ Solution</summary>

```python
import sys
print(sys.version.split()[0])
```

</details>

## Exercise 3

Print the name of your operating system.

*Hint: platform.system()*

<details>
<summary>✅ Solution</summary>

```python
import platform
print(platform.system())
```

</details>

## Exercise 4

Print three separate lines of text using a single print() call.

*Hint: The newline character is \n.*

<details>
<summary>✅ Solution</summary>

```python
print("line 1\nline 2\nline 3")
```

</details>

## Exercise 5

Explain (in words) the difference between the REPL and a script.

<details>
<summary>✅ Solution</summary>

**REPL** = interactive shell (`python` with no file). You type one line, press
Enter, and instantly see the result — great for quick experiments. **Script** =
a saved `.py` file you run with `python file.py`; it executes top to bottom and
is what you use for real programs.

</details>

## Exercise 6

Print where Python's `os` module lives on disk.

*Hint: Modules have a __file__ attribute.*

<details>
<summary>✅ Solution</summary>

```python
import os
print(os.__file__)
```

</details>

## Exercise 7

Use Python as a calculator in code: print the result of 17 * 23 + 4.

<details>
<summary>✅ Solution</summary>

```python
print(17 * 23 + 4)
```

</details>

## Exercise 8

Print the full path of the Python executable running your script.

*Hint: sys.executable*

<details>
<summary>✅ Solution</summary>

```python
import sys
print(sys.executable)
```

</details>

