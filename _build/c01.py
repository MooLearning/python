# -*- coding: utf-8 -*-
"""Phase 1 — Python Fundamentals content."""

CONTENT = {}

CONTENT["installation-and-setup"] = {
    "what": (
        "Before you can write Python, you need three things on your computer: the "
        "**Python interpreter** (the program that runs your code), a **code editor** "
        "(most people use VS Code), and **pip** (Python's package installer, which comes "
        "bundled with modern Python). You write code in `.py` files and run them, or you "
        "type code line-by-line in the interactive shell (the REPL)."
    ),
    "why": (
        "Everything in this entire roadmap depends on a working Python install. Getting "
        "comfortable with running scripts, using the REPL, and installing packages with pip "
        "now will save you hours of confusion later."
    ),
    "concepts": [
        ("Interpreter", "The `python`/`python3` program that reads and executes your code."),
        ("REPL", "Read-Eval-Print-Loop: type `python` with no file to get an interactive shell."),
        ("Script", "A `.py` file you run with `python myfile.py`."),
        ("pip", "Installs third-party packages: `pip install numpy`."),
        ("PATH", "The OS setting that lets you type `python` from any folder."),
        ("IDE / VS Code", "An editor with autocompletion, debugging and a built-in terminal."),
    ],
    "examples": [
        ("Inspect your Python installation", r'''
import sys       # info about the Python interpreter
import platform  # info about your operating system

# sys.version is a string describing the running interpreter
print("Python version:", sys.version.split()[0])

# Where is the python executable that is running this file?
print("Interpreter path:", sys.executable)

# What OS are you on?
print("Operating system:", platform.system(), platform.release())
'''),
        ("Your first script", r'''
# Save this in a file called hello.py and run: python hello.py
name = "learner"
print("Hello,", name + "!")
print("You just ran a Python script.")
'''),
        ("Confirm a standard-library module loads", r'''
import math        # math ships WITH Python (no pip needed)
import statistics  # another standard-library module

# Some stdlib modules are written in Python and live in a file on disk:
print("statistics module file:", statistics.__file__)
# math is built INTO the interpreter (written in C), so it has no __file__:
print("math is built-in (no file)?", not hasattr(math, "__file__"))
print("Square root of 144 is:", math.sqrt(144))
# Third-party packages (like numpy) would need: pip install numpy
'''),
    ],
    "gotchas": [
        "On macOS/Linux the command is often `python3` (and `pip3`), not `python`. On Windows use `py`.",
        "`pip install x` installs for ONE Python. If you have several Pythons, packages can 'go missing'. Use `python -m pip install x` to be sure.",
        "Forgetting to SAVE the file before running it — you then run the old version.",
        "‘python’ not found usually means Python isn't on your PATH; re-run the installer and tick 'Add to PATH'.",
        "Don't name your file the same as a module you import (e.g. `random.py`) — Python will import your file instead of the real module.",
    ],
    "exercises": [
        ("Print the exact text `Hello, World!` to the screen.", "Use the print() function.",
         r'''print("Hello, World!")'''),
        ("Print the version of Python you are running (just the number, e.g. 3.14.5).",
         "sys.version starts with the number.",
         r'''import sys
print(sys.version.split()[0])'''),
        ("Print the name of your operating system.", "platform.system()",
         r'''import platform
print(platform.system())'''),
        ("Print three separate lines of text using a single print() call.",
         "The newline character is \\n.",
         r'''print("line 1\nline 2\nline 3")'''),
        ("Explain (in words) the difference between the REPL and a script.", "",
         r'''#md
**REPL** = interactive shell (`python` with no file). You type one line, press
Enter, and instantly see the result — great for quick experiments. **Script** =
a saved `.py` file you run with `python file.py`; it executes top to bottom and
is what you use for real programs.'''),
        ("Print where Python's `os` module lives on disk.", "Modules have a __file__ attribute.",
         r'''import os
print(os.__file__)'''),
        ("Use Python as a calculator in code: print the result of 17 * 23 + 4.", "",
         r'''print(17 * 23 + 4)'''),
        ("Print the full path of the Python executable running your script.", "sys.executable",
         r'''import sys
print(sys.executable)'''),
    ],
}

CONTENT["variables-and-data-types"] = {
    "what": (
        "A **variable** is a name that points to a value, created with `=`. Python figures "
        "out the **type** automatically. The core built-in types you'll use constantly are "
        "`int` (whole numbers), `float` (decimals), `str` (text), `bool` (True/False), and "
        "`NoneType` (the special value `None`). You never declare a type — you just assign."
    ),
    "why": (
        "Variables and types are the atoms of every program. Knowing how Python stores values "
        "and how types behave (and convert) prevents a huge class of beginner bugs, like adding "
        "a string to a number."
    ),
    "concepts": [
        ("Variable", "A label for a value: `x = 10`. Re-assigning just re-points the label."),
        ("Dynamic typing", "A variable can hold an int now and a string later — Python doesn't mind."),
        ("int / float", "Whole numbers vs decimals. `3` is int, `3.0` is float."),
        ("str", "Text in quotes: `'hi'` or \"hi\"."),
        ("bool", "`True` or `False` (note the capital letters)."),
        ("None", "Represents 'no value yet'; its type is NoneType."),
        ("type()", "Ask Python the type of any value: `type(3.0)`."),
    ],
    "examples": [
        ("Creating variables and checking their types", r'''
age = 25            # int  (whole number)
price = 19.99       # float (decimal)
name = "Ada"        # str  (text)
is_student = True   # bool (True/False)
nothing = None      # NoneType (absence of a value)

# type() tells you the data type of a value
print(age, "->", type(age))
print(price, "->", type(price))
print(name, "->", type(name))
print(is_student, "->", type(is_student))
print(nothing, "->", type(nothing))
'''),
        ("Variables are dynamic and can be reassigned", r'''
x = 10
print(x, type(x))   # int

x = "now I am text"
print(x, type(x))   # str  -- same name, new type, no error

# Multiple assignment at once
a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

# Swap values without a temp variable (a classic Python trick)
a, b = b, a
print("after swap:", a, b)
'''),
        ("Numbers behave like math; watch int vs float", r'''
print(7 + 3)      # 10   (int + int -> int)
print(7 / 2)      # 3.5  (/ ALWAYS gives a float)
print(7 // 2)     # 3    (// is floor division -> int here)
print(2 ** 10)    # 1024 (** is power)
print(0.1 + 0.2)  # 0.30000000000000004  (floats are approximate!)
'''),
    ],
    "gotchas": [
        "`True`/`False`/`None` are capitalized. `true` or `null` will raise a NameError.",
        "`=` assigns a value; `==` compares two values. Mixing them up is the #1 beginner bug.",
        "Floats are approximate: `0.1 + 0.2 != 0.3`. Use `round()` or `math.isclose()` to compare.",
        "Variable names can't start with a digit and can't contain spaces. Use snake_case: `my_score`.",
        "Assigning to a name doesn't copy the value for lists/objects — it points to the SAME object (more on this later).",
    ],
    "exercises": [
        ("Create variables for your name (str), age (int) and height in metres (float), then print all three.",
         "Three assignments, one print.",
         r'''name = "Sam"
age = 20
height = 1.75
print(name, age, height)'''),
        ("Print the type of the value 42, of 4.2, and of '42'.", "Use type().",
         r'''print(type(42))
print(type(4.2))
print(type("42"))'''),
        ("Swap the values of a = 5 and b = 9 without using a third variable.", "a, b = b, a",
         r'''a, b = 5, 9
a, b = b, a
print(a, b)  # 9 5'''),
        ("Predict then verify: what is 7 // 2 and what is 7 / 2?", "// floors, / makes a float.",
         r'''print(7 // 2)  # 3
print(7 / 2)   # 3.5'''),
        ("Compute 2 to the power 10 and print it.", "Use **.",
         r'''print(2 ** 10)  # 1024'''),
        ("Assign 1, 2, 3 to x, y, z in a single line and print their sum.", "Multiple assignment.",
         r'''x, y, z = 1, 2, 3
print(x + y + z)  # 6'''),
        ("Show that 0.1 + 0.2 is not exactly 0.3, then compare them safely.", "math.isclose",
         r'''import math
print(0.1 + 0.2)                       # 0.30000000000000004
print(math.isclose(0.1 + 0.2, 0.3))    # True'''),
        ("Create a variable set to None, then change it to 100 and print its type before and after.",
         "type() twice.",
         r'''v = None
print(type(v))   # <class 'NoneType'>
v = 100
print(type(v))   # <class 'int'>'''),
    ],
}

CONTENT["operators"] = {
    "what": (
        "**Operators** are symbols that perform actions on values. Python groups them into "
        "**arithmetic** (`+ - * / // % **`), **comparison** (`== != < > <= >=`), **logical** "
        "(`and or not`), **assignment** (`= += -=` …) and **bitwise** (`& | ^ ~ << >>`). "
        "Comparisons and logical operators always produce a `bool`."
    ),
    "why": (
        "Operators are how you compute, compare and make decisions. Logical and comparison "
        "operators in particular power every `if` statement and loop condition you'll ever write."
    ),
    "concepts": [
        ("Arithmetic", "`+ - * /` plus `//` (floor div), `%` (remainder), `**` (power)."),
        ("Comparison", "`==` equal, `!=` not equal, `< > <= >=`. Returns True/False."),
        ("Logical", "`and`, `or`, `not` combine boolean expressions."),
        ("Assignment shortcuts", "`x += 1` means `x = x + 1`. Also -=, *=, /=, //=, **=, %=."),
        ("Bitwise", "Operate on the binary bits of integers: & | ^ ~ << >>."),
        ("Operator precedence", "`**` before `* /` before `+ -`; use parentheses when unsure."),
    ],
    "examples": [
        ("Arithmetic operators", r'''
a, b = 17, 5
print("add ", a + b)    # 22
print("sub ", a - b)    # 12
print("mul ", a * b)    # 85
print("div ", a / b)    # 3.4   (float)
print("floor", a // b)  # 3     (drops the decimal)
print("mod ", a % b)    # 2     (remainder)
print("pow ", a ** b)   # 1419857
'''),
        ("Comparison and logical operators", r'''
x = 7
# Comparisons return booleans
print(x > 5)          # True
print(x == 10)        # False

# Combine conditions with and / or / not
print(x > 5 and x < 10)   # True  (both must be true)
print(x < 0 or x > 100)   # False (neither is true)
print(not (x == 7))       # False

# Python lets you "chain" comparisons like math
print(0 < x < 10)         # True
'''),
        ("Assignment shortcuts and bitwise basics", r'''
score = 0
score += 10   # same as score = score + 10
score *= 2    # now 20
print("score:", score)

# Bitwise works on binary representations
print(5 & 3)   # 1   (101 & 011 = 001)
print(5 | 3)   # 7   (101 | 011 = 111)
print(5 ^ 3)   # 6   (XOR)
print(1 << 4)  # 16  (shift bits left = multiply by 2**4)
'''),
    ],
    "gotchas": [
        "`/` always returns a float, even `4 / 2` gives `2.0`. Use `//` for integer division.",
        "`%` of negative numbers may surprise you: `-7 % 3` is `2` in Python, not `-1`.",
        "`and`/`or` return one of the operands, not always True/False: `0 or 'x'` is `'x'`.",
        "Don't confuse `&`/`|` (bitwise) with `and`/`or` (logical). `5 and 3` is `3`, but `5 & 3` is `1`.",
        "Precedence traps: `2 + 3 * 4` is 14, not 20. Use parentheses to be explicit.",
    ],
    "exercises": [
        ("Print the quotient and remainder of 29 divided by 6.", "Use // and %.",
         r'''print(29 // 6)  # 4
print(29 % 6)   # 5'''),
        ("Check whether 50 is between 10 and 100 (inclusive) using a chained comparison.", "10 <= x <= 100",
         r'''x = 50
print(10 <= x <= 100)  # True'''),
        ("Given temp = 30, print True if it is warm (20 <= temp <= 35).", "Logical and / chaining.",
         r'''temp = 30
print(20 <= temp <= 35)  # True'''),
        ("Use a compound assignment to triple the value of n = 7, then print it.", "n *= 3",
         r'''n = 7
n *= 3
print(n)  # 21'''),
        ("Is a number even? Print True if 12 is even using the modulo operator.", "even means % 2 == 0",
         r'''print(12 % 2 == 0)  # True'''),
        ("Evaluate and explain: 2 + 3 * 4 ** 2. What is the order?", "** first, then *, then +.",
         r'''print(2 + 3 * 4 ** 2)  # 4**2=16, *3=48, +2=50 -> 50'''),
        ("Use bitwise AND to test if 6 has its lowest bit set (i.e., is it odd?).", "6 & 1",
         r'''print(6 & 1)        # 0  -> lowest bit not set
print(6 & 1 == 1)   # False -> 6 is even'''),
        ("Without using **, multiply 7 by 8 using a bit shift where possible, else explain why not.",
         "Shifts only multiply by powers of 2.",
         r'''#md
8 is `2**3`, so `7 << 3` equals `7 * 8 = 56`.
```python
print(7 << 3)  # 56
```
You can only use a shift when one factor is a power of two.'''),
    ],
}

CONTENT["input-output-and-type-casting"] = {
    "what": (
        "`print()` sends text **out** to the screen; `input()` reads text **in** from the user. "
        "Crucially, `input()` ALWAYS returns a `str`, so to do math you must **cast** (convert) "
        "it with `int()` or `float()`. Casting also goes the other way: `str(42)` turns a number "
        "into text."
    ),
    "why": (
        "Almost every interactive program reads input and prints output. Understanding that input "
        "is always text — and how to convert between types — fixes the classic `'10' + 5` crash."
    ),
    "concepts": [
        ("print()", "Outputs values; `sep=` and `end=` control separators and line endings."),
        ("input(prompt)", "Pauses and returns whatever the user types — as a string."),
        ("int() / float()", "Convert a string (or number) to an integer / decimal."),
        ("str()", "Convert any value to its text form."),
        ("f-strings", "`f\"{name} is {age}\"` embeds values directly in text — the modern way to format."),
    ],
    "examples": [
        ("print with sep, end, and f-strings", r'''
name = "Ada"
age = 36

# f-strings: put variables inside {curly braces}
print(f"{name} is {age} years old.")

# sep controls what goes BETWEEN items; end controls what goes at the END
print("a", "b", "c", sep="-")        # a-b-c
print("no newline here ->", end=" ")
print("...continued on same line")

# Format numbers: 2 decimal places
pi = 3.14159
print(f"pi is about {pi:.2f}")        # pi is about 3.14
'''),
        ("Reading input is always a string", r'''
# NOTE: input() pauses for typing. Here we simulate it so the file runs anywhere.
def input(_prompt=""):           # remove this line to use real keyboard input
    return "42"                  # pretend the user typed 42

raw = input("Enter a number: ")
print("raw value:", raw, "type:", type(raw))   # it's a str!

number = int(raw)                # cast text -> integer
print("number + 8 =", number + 8)              # now math works
'''),
        ("Casting between types (and what breaks)", r'''
print(int("100") + 1)     # 101  -> str of digits -> int
print(float("3.5") * 2)   # 7.0  -> str -> float
print(str(2026) + "!")    # 2026! -> int -> str so we can concatenate
print(int(9.9))           # 9    -> float -> int TRUNCATES (does not round)
print(bool(0), bool(""), bool(3))  # False False True
'''),
    ],
    "gotchas": [
        "`input()` returns a string ALWAYS. `input() + 1` crashes; cast with `int()` first.",
        "`int(\"3.5\")` raises ValueError — you can't int() a decimal string. Use `int(float(\"3.5\"))`.",
        "`int(9.9)` gives `9` (it truncates toward zero); it does NOT round. Use `round()` to round.",
        "You can't do `\"age: \" + 30` — concatenate strings only. Use an f-string or `str(30)`.",
        "Empty string, 0, 0.0, None and empty containers are all 'falsy' — `bool()` of them is False.",
    ],
    "exercises": [
        ("Print `Name: Sam | Age: 20` using an f-string with variables name='Sam', age=20.",
         "f\"...{name}...{age}...\"",
         r'''name, age = "Sam", 20
print(f"Name: {name} | Age: {age}")'''),
        ("Ask for two numbers and print their sum (simulate input as '4' and '5').",
         "Cast both with int().",
         r'''a = int("4")
b = int("5")
print(a + b)  # 9'''),
        ("Print the floats 1, 2.5, 3.14159 each rounded to 1 decimal place.", "Use :.1f in f-strings.",
         r'''for x in (1, 2.5, 3.14159):
    print(f"{x:.1f}")'''),
        ("Convert the string '3.75' to a float and print double its value.", "float() then * 2.",
         r'''print(float("3.75") * 2)  # 7.5'''),
        ("Print 'a', 'b', 'c' on one line separated by commas using print's sep argument.", "sep=', '",
         r'''print("a", "b", "c", sep=", ")'''),
        ("Show that int('7') + int('8') is 15 but '7' + '8' is '78'.", "One casts, one concatenates.",
         r'''print(int("7") + int("8"))  # 15
print("7" + "8")            # 78'''),
        ("Turn the integer 2026 into the string 'Year 2026'.", "str() and concatenation or f-string.",
         r'''year = 2026
print("Year " + str(year))   # or: print(f"Year {year}")'''),
        ("Round 9.9 down to 9 with int(), and to 10 with round(); print both.",
         "int truncates, round rounds.",
         r'''print(int(9.9))    # 9
print(round(9.9))  # 10'''),
    ],
}

CONTENT["strings-and-methods"] = {
    "what": (
        "A **string** is an ordered sequence of characters in quotes. Strings are **immutable** "
        "(you can't change them in place — every 'edit' makes a new string). They come with dozens "
        "of handy **methods** like `.upper()`, `.strip()`, `.split()`, `.replace()`, and `.find()`, "
        "and they support **indexing** (`s[0]`) and **slicing** (`s[1:4]`)."
    ),
    "why": (
        "Text is everywhere — file names, user input, CSV rows, API responses, NLP data. String "
        "slicing and methods are some of the most-used tools in all of Python."
    ),
    "concepts": [
        ("Indexing", "`s[0]` is the first char, `s[-1]` the last. Counting starts at 0."),
        ("Slicing", "`s[start:stop:step]`; stop is excluded. `s[::-1]` reverses."),
        ("Immutability", "`s[0] = 'x'` is illegal. Build a new string instead."),
        ("Common methods", ".upper/.lower/.strip/.split/.join/.replace/.find/.startswith."),
        ("f-strings", "Format values into text: `f\"{x:>5}\"` right-aligns in width 5."),
        ("in operator", "`'cat' in 'concatenate'` checks for a substring."),
    ],
    "examples": [
        ("Indexing and slicing", r'''
s = "Python"
print(s[0])     # P    (first character, index 0)
print(s[-1])    # n    (last character)
print(s[0:3])   # Pyt  (indices 0,1,2 -- stop is excluded)
print(s[2:])    # thon (from index 2 to the end)
print(s[:2])    # Py   (start to index 1)
print(s[::-1])  # nohtyP (reverse using step -1)
print(len(s))   # 6    (number of characters)
'''),
        ("Essential string methods", r'''
text = "   Hello, World!   "
print(text.strip())             # 'Hello, World!'  (trim whitespace)
print(text.strip().upper())     # 'HELLO, WORLD!'
print("a,b,c".split(","))       # ['a', 'b', 'c']
print("-".join(["2026", "06", "09"]))  # '2026-06-09'
print("banana".replace("a", "o"))      # 'bonono'
print("hello".find("l"))        # 2  (index of first 'l', -1 if absent)
print("data.csv".endswith(".csv"))     # True
'''),
        ("Building and formatting strings", r'''
name = "Ada"
score = 95.5

# f-strings are the cleanest way to format
print(f"{name} scored {score:.1f}%")

# Alignment and padding inside a width
for item in ["egg", "milk", "bread"]:
    print(f"{item:<8}| ${len(item):>2}")  # left/right aligned columns

# Strings are immutable: this makes a NEW string
greeting = "hi"
louder = greeting + "!!!"
print(greeting, louder)   # original unchanged
'''),
    ],
    "gotchas": [
        "Strings are immutable: `s[0] = 'X'` raises TypeError. Create a new string instead.",
        "Indexing past the end (`s[100]`) raises IndexError, but SLICING past the end is safe.",
        "`.find()` returns -1 when not found (no error); `.index()` raises ValueError. Pick deliberately.",
        "`.split()` with no argument splits on ANY whitespace and drops empties — different from `.split(' ')`.",
        "Methods return NEW strings; `s.upper()` alone does nothing unless you store the result.",
    ],
    "exercises": [
        ("Print the first and last character of the string 'algorithm'.", "Index 0 and -1.",
         r'''s = "algorithm"
print(s[0], s[-1])  # a m'''),
        ("Reverse the string 'stressed' and print it.", "Slice with step -1.",
         r'''print("stressed"[::-1])  # desserts'''),
        ("Count how many characters are in 'antidisestablishmentarianism'.", "len().",
         r'''print(len("antidisestablishmentarianism"))  # 28'''),
        ("Split the CSV line 'name,age,city' into a list of fields.", "split(',').",
         r'''print("name,age,city".split(","))  # ['name', 'age', 'city']'''),
        ("Turn ['2026','06','09'] into the date string '2026/06/09'.", "'/'.join(...).",
         r'''print("/".join(["2026", "06", "09"]))  # 2026/06/09'''),
        ("Check (case-insensitively) whether 'Hello World' contains the word 'world'.", "lower() then in.",
         r'''text = "Hello World"
print("world" in text.lower())  # True'''),
        ("Given '  spaced out  ', remove leading/trailing spaces and make it uppercase.",
         "strip() then upper().",
         r'''print("  spaced out  ".strip().upper())  # SPACED OUT'''),
        ("Check if 'racecar' is a palindrome (same forwards and backwards).", "Compare to its reverse.",
         r'''w = "racecar"
print(w == w[::-1])  # True'''),
    ],
}

CONTENT["conditional-statements"] = {
    "what": (
        "Conditional statements let your program **make decisions**. `if` runs a block when a "
        "condition is True; `elif` ('else if') checks another condition; `else` is the fallback. "
        "Python uses **indentation** (not braces) to mark which lines belong to each branch."
    ),
    "why": (
        "Decision-making is the heart of logic. Validating input, branching on cases, and reacting "
        "to data all rely on conditionals. Get the indentation and truthiness rules right and the "
        "rest of programming opens up."
    ),
    "concepts": [
        ("if / elif / else", "Check conditions in order; the FIRST true branch runs, the rest are skipped."),
        ("Indentation", "4 spaces define a block. Consistency is mandatory — Python enforces it."),
        ("Truthiness", "Non-zero numbers, non-empty strings/lists are 'truthy'; 0, '', [], None are 'falsy'."),
        ("Comparison chaining", "`if 0 < x < 10:` is valid and reads like math."),
        ("Ternary expression", "`label = 'even' if n % 2 == 0 else 'odd'` — a one-line if/else."),
    ],
    "examples": [
        ("Basic if / elif / else", r'''
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:        # only checked if the previous test was False
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)   # B
'''),
        ("Truthiness and combined conditions", r'''
name = ""          # empty string is "falsy"
items = [1, 2, 3]  # non-empty list is "truthy"

if not name:
    print("Please enter your name.")

if items:
    print("You have", len(items), "items.")

age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("Welcome in!")
'''),
        ("Ternary expression (one-line if/else)", r'''
for n in range(1, 6):
    label = "even" if n % 2 == 0 else "odd"
    print(n, "is", label)

# Useful for choosing a value inline
temp = 30
status = "hot" if temp > 28 else "comfortable"
print(status)   # hot
'''),
    ],
    "gotchas": [
        "Use `==` to compare, not `=` (which assigns). `if x = 5:` is a SyntaxError.",
        "Indentation must be consistent (4 spaces is standard). Mixing tabs and spaces causes errors.",
        "Every `if`/`elif`/`else` line ends with a colon `:` — forgetting it is a SyntaxError.",
        "`elif` only runs if earlier conditions were False. Order your branches from most to least specific.",
        "`if items == True:` is fragile — just write `if items:` to test truthiness.",
    ],
    "exercises": [
        ("Print 'positive', 'negative', or 'zero' for the number n = -4.", "Three branches.",
         r'''n = -4
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")'''),
        ("Print 'even' or 'odd' for 17 using a ternary expression.", "x if cond else y.",
         r'''n = 17
print("even" if n % 2 == 0 else "odd")  # odd'''),
        ("Given age = 70, print 'child' (<13), 'adult' (13-64) or 'senior' (65+).", "Order branches.",
         r'''age = 70
if age < 13:
    print("child")
elif age <= 64:
    print("adult")
else:
    print("senior")'''),
        ("Check if the string s = '' is empty using truthiness (not len).", "if not s:",
         r'''s = ""
if not s:
    print("empty")'''),
        ("Print 'leap' if year 2024 is a leap year, else 'common'.",
         "Divisible by 4 and (not by 100 or by 400).",
         r'''y = 2024
if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    print("leap")
else:
    print("common")'''),
        ("Given a number, print 'FizzBuzz' if divisible by both 3 and 5, else the number. Test 15.",
         "Check %3==0 and %5==0.",
         r'''n = 15
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
else:
    print(n)'''),
        ("Grade 0-100 into A/B/C/D/F bands and print the grade for 67.", "Cascading elifs.",
         r'''s = 67
if s >= 90: print("A")
elif s >= 80: print("B")
elif s >= 70: print("C")
elif s >= 60: print("D")
else: print("F")  # D'''),
        ("Given username and password, print 'access granted' only if username=='admin' and password=='1234'.",
         "Combine with and.",
         r'''username, password = "admin", "1234"
if username == "admin" and password == "1234":
    print("access granted")
else:
    print("denied")'''),
    ],
}

CONTENT["loops"] = {
    "what": (
        "**Loops** repeat work. A `for` loop iterates over a sequence (a list, a string, a "
        "`range`). A `while` loop repeats as long as a condition stays True. `break` exits a loop "
        "early, `continue` skips to the next iteration, and the loop's `else` runs if the loop "
        "finished without breaking."
    ),
    "why": (
        "Computers shine at repetition. Processing every item in a dataset, retrying until success, "
        "or summing a list — all loops. `for` + `range` and `for` over collections are everyday tools."
    ),
    "concepts": [
        ("for loop", "Repeats once per item: `for x in [1,2,3]:`."),
        ("range(start, stop, step)", "Generates numbers; stop is excluded. `range(5)` -> 0..4."),
        ("while loop", "Repeats while a condition is True. Make sure it eventually becomes False!"),
        ("break / continue", "Exit the loop entirely / skip to the next iteration."),
        ("enumerate()", "Loop with an index AND the item: `for i, x in enumerate(seq):`."),
        ("loop else", "Runs only if the loop didn't hit `break` — handy for search loops."),
    ],
    "examples": [
        ("for loops and range()", r'''
# Iterate directly over items
for fruit in ["apple", "banana", "cherry"]:
    print("I like", fruit)

# range(stop): 0,1,2,3,4
total = 0
for i in range(5):
    total += i
print("sum 0..4 =", total)   # 10

# range(start, stop, step)
for n in range(2, 11, 2):     # 2,4,6,8,10
    print(n, end=" ")
print()
'''),
        ("while loops, break and continue", r'''
# while: repeat until a condition changes
count = 3
while count > 0:
    print("countdown:", count)
    count -= 1          # WITHOUT this line it would loop forever!
print("liftoff!")

# break stops the loop; continue skips one iteration
for n in range(1, 10):
    if n == 5:
        break           # stop entirely when we reach 5
    if n % 2 == 0:
        continue        # skip even numbers
    print("odd before 5:", n)   # 1, 3
'''),
        ("enumerate and the loop-else", r'''
names = ["Ada", "Linus", "Grace"]
for index, name in enumerate(names, start=1):
    print(index, name)

# loop-else: runs only if no break happened (great for "search and report")
target = 7
for n in [2, 4, 6, 8]:
    if n == target:
        print("found!")
        break
else:
    print("not found")   # this prints, because we never broke
'''),
    ],
    "gotchas": [
        "`range(5)` is 0,1,2,3,4 — it STOPS before 5. Off-by-one errors come from forgetting this.",
        "A `while` loop with a condition that never becomes False runs forever. Always update the variable.",
        "Modifying a list while looping over it causes skipped/duplicated items. Loop over a copy instead.",
        "`for i in range(len(seq))` then `seq[i]` is clumsy — prefer iterating items directly or `enumerate`.",
        "`break` only exits the INNERMOST loop, not all nested loops.",
    ],
    "exercises": [
        ("Print the numbers 1 to 5, each on its own line.", "range(1, 6).",
         r'''for i in range(1, 6):
    print(i)'''),
        ("Sum the numbers from 1 to 100 and print the total.", "range(1, 101) and a running sum.",
         r'''total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050'''),
        ("Print only the even numbers from 1 to 20 using continue.", "Skip when n % 2 != 0.",
         r'''for n in range(1, 21):
    if n % 2 != 0:
        continue
    print(n, end=" ")
print()'''),
        ("Use a while loop to count down from 5 to 1.", "Decrement each pass.",
         r'''n = 5
while n >= 1:
    print(n)
    n -= 1'''),
        ("Print each fruit with its 1-based position using enumerate.", "enumerate(..., start=1).",
         r'''for i, f in enumerate(["apple", "pear", "fig"], start=1):
    print(i, f)'''),
        ("Find the first number divisible by 7 between 20 and 40 and stop.", "break when found.",
         r'''for n in range(20, 41):
    if n % 7 == 0:
        print(n)  # 21
        break'''),
        ("Print the multiplication table (1-5) for 3, e.g. '3 x 1 = 3'.", "Loop 1..5.",
         r'''for i in range(1, 6):
    print(f"3 x {i} = {3 * i}")'''),
        ("Print a 3x3 grid of '*' using nested loops.", "A loop inside a loop.",
         r'''for row in range(3):
    for col in range(3):
        print("*", end="")
    print()'''),
    ],
}

CONTENT["lists-tuples-sets-dictionaries"] = {
    "what": (
        "Python's four core **collections**: a **list** `[]` is an ordered, changeable sequence; a "
        "**tuple** `()` is an ordered but **immutable** sequence; a **set** `{}` is an unordered "
        "collection of **unique** items; a **dictionary** `{key: value}` maps keys to values for "
        "instant lookup. Choosing the right one is half of writing clean Python."
    ),
    "why": (
        "These four structures store and organize almost all data you'll handle. Lists for sequences, "
        "tuples for fixed records, sets for uniqueness/membership, dicts for labelled data and fast "
        "lookups — they're the workhorses of every program and the basis for DSA later."
    ),
    "concepts": [
        ("list", "Ordered, mutable: `nums = [1,2,3]`. Use .append, .pop, indexing, slicing."),
        ("tuple", "Ordered, immutable: `point = (3, 4)`. Great for fixed groups / dict keys."),
        ("set", "Unordered, unique: `{1,2,2}` becomes `{1,2}`. Fast `in` checks; supports union/intersection."),
        ("dict", "Key→value map: `ages = {'Ada': 36}`. O(1) lookup by key; keys must be unique."),
        ("Mutability", "Lists/sets/dicts can change in place; tuples and strings cannot."),
        ("Membership", "`x in collection` checks presence; very fast for sets and dicts."),
    ],
    "examples": [
        ("Lists: ordered and mutable", r'''
nums = [3, 1, 2]
nums.append(4)         # add to end -> [3, 1, 2, 4]
nums.sort()            # sort in place -> [1, 2, 3, 4]
print(nums, "len", len(nums))
print("first/last:", nums[0], nums[-1])
print("slice:", nums[1:3])     # [2, 3]
nums.remove(2)         # remove first matching value
print("after remove:", nums)
'''),
        ("Tuples and sets", r'''
# Tuple: fixed, immutable -> safe for coordinates, records
point = (3, 4)
x, y = point           # unpacking
print("x,y =", x, y)
# point[0] = 9         # would raise TypeError (immutable)

# Set: unique items, fast membership, set algebra
a = {1, 2, 3, 3, 2}
print("unique:", a)            # {1, 2, 3}
b = {3, 4, 5}
print("union:", a | b)         # {1,2,3,4,5}
print("intersection:", a & b)  # {3}
print("3 in a?", 3 in a)       # True (very fast)
'''),
        ("Dictionaries: key-value lookups", r'''
ages = {"Ada": 36, "Linus": 54}
ages["Grace"] = 85             # add / update
print(ages["Ada"])            # 36
print(ages.get("Nobody", "?")) # safe lookup with default -> '?'

# Iterate keys, values, or both
for name, age in ages.items():
    print(f"{name} is {age}")

print("keys:", list(ages.keys()))
print("Ada known?", "Ada" in ages)   # checks KEYS
'''),
    ],
    "gotchas": [
        "`b = a` for a list does NOT copy it — both names point to the same list. Use `a.copy()` or `a[:]`.",
        "Tuples are immutable: `t[0] = 5` raises TypeError. To 'change' one, build a new tuple.",
        "Sets are unordered — don't rely on their printing order, and you can't index `s[0]`.",
        "Accessing a missing dict key with `d['x']` raises KeyError; use `d.get('x', default)` to be safe.",
        "A single-element tuple needs a trailing comma: `(5,)`. `(5)` is just the integer 5.",
    ],
    "exercises": [
        ("Create a list of 3 colors, append a 4th, and print the list and its length.", ".append, len.",
         r'''colors = ["red", "green", "blue"]
colors.append("yellow")
print(colors, len(colors))'''),
        ("From [5, 3, 9, 1] print the largest and smallest values.", "max() and min().",
         r'''nums = [5, 3, 9, 1]
print(max(nums), min(nums))  # 9 1'''),
        ("Remove duplicates from [1,2,2,3,3,3] and print the unique count.", "Convert to a set.",
         r'''data = [1, 2, 2, 3, 3, 3]
print(len(set(data)))  # 3'''),
        ("Make a dict mapping 'a'->1, 'b'->2, then print the value for 'b'.", "{} literal.",
         r'''d = {"a": 1, "b": 2}
print(d["b"])  # 2'''),
        ("Given two sets {1,2,3} and {2,3,4}, print items in BOTH and items in EITHER.", "& and |.",
         r'''a, b = {1, 2, 3}, {2, 3, 4}
print(a & b)  # {2, 3}
print(a | b)  # {1, 2, 3, 4}'''),
        ("Unpack the tuple (10, 20, 30) into three variables and print their sum.", "x, y, z = t.",
         r'''x, y, z = (10, 20, 30)
print(x + y + z)  # 60'''),
        ("Count word frequencies in 'a b a c b a' using a dict.", "Split, then use get().",
         r'''text = "a b a c b a"
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
print(counts)  # {'a': 3, 'b': 2, 'c': 1}'''),
        ("Safely get the value for a missing key 'z' from {'a':1} returning 0 instead of crashing.",
         "dict.get with default.",
         r'''d = {"a": 1}
print(d.get("z", 0))  # 0'''),
    ],
}

CONTENT["comprehensions"] = {
    "what": (
        "A **comprehension** builds a list, set, or dict in a single readable line by describing "
        "*what you want* rather than writing a manual loop. List form: "
        "`[expr for item in iterable if condition]`. There are set `{...}` and dict "
        "`{k: v for ...}` versions too."
    ),
    "why": (
        "Comprehensions are concise, fast, and extremely common in real Python and data work. "
        "Reading and writing them fluently makes your code shorter and clearer than equivalent loops."
    ),
    "concepts": [
        ("List comprehension", "`[x*x for x in range(5)]` -> [0,1,4,9,16]."),
        ("Filtering", "Add `if`: `[x for x in nums if x > 0]`."),
        ("Transform + filter", "`[f(x) for x in data if cond(x)]` in one line."),
        ("Dict comprehension", "`{k: v for k, v in pairs}` builds a dict."),
        ("Set comprehension", "`{x % 3 for x in nums}` builds a set of unique results."),
        ("Nested / conditional expr", "`[a if a>0 else 0 for a in xs]` puts the if/else BEFORE for."),
    ],
    "examples": [
        ("List comprehensions vs loops", r'''
# The loop way
squares = []
for x in range(6):
    squares.append(x * x)
print(squares)            # [0, 1, 4, 9, 16, 25]

# The comprehension way (same result, one line)
squares = [x * x for x in range(6)]
print(squares)

# With a filter: keep only evens, then square them
evens_sq = [x * x for x in range(10) if x % 2 == 0]
print(evens_sq)           # [0, 4, 16, 36, 64]
'''),
        ("Transforming text and conditional expressions", r'''
words = ["hi", "world", "ok", "python"]

# Uppercase every word
print([w.upper() for w in words])

# Keep only long words
print([w for w in words if len(w) > 2])

# if/else INSIDE the expression (note position: before 'for')
labels = ["long" if len(w) > 2 else "short" for w in words]
print(labels)             # ['short', 'long', 'short', 'long']
'''),
        ("Dict and set comprehensions", r'''
# Dict comprehension: number -> its square
sq_map = {n: n * n for n in range(1, 6)}
print(sq_map)             # {1:1, 2:4, 3:9, 4:16, 5:25}

# Invert a dict (swap keys and values)
prices = {"apple": 3, "pear": 5}
by_price = {v: k for k, v in prices.items()}
print(by_price)           # {3: 'apple', 5: 'pear'}

# Set comprehension: unique remainders
print({n % 3 for n in range(10)})   # {0, 1, 2}
'''),
    ],
    "gotchas": [
        "The filtering `if` goes at the END; the `if/else` *expression* goes at the FRONT (before `for`).",
        "Deeply nested comprehensions become unreadable — if it needs comments, use a real loop.",
        "`{}` alone is an empty DICT, not an empty set. Use `set()` for an empty set.",
        "A comprehension creates a brand-new list each time; it doesn't modify the source iterable.",
        "Don't call expensive functions twice; comprehensions evaluate the expression for every item.",
    ],
    "exercises": [
        ("Build a list of the cubes of 1..5 with a comprehension.", "[x**3 for x in ...].",
         r'''print([x ** 3 for x in range(1, 6)])  # [1, 8, 27, 64, 125]'''),
        ("From [-2,-1,0,1,2] keep only the positive numbers.", "Add an if filter.",
         r'''nums = [-2, -1, 0, 1, 2]
print([x for x in nums if x > 0])  # [1, 2]'''),
        ("Uppercase every word in ['cat','dog'] using a comprehension.", "w.upper().",
         r'''print([w.upper() for w in ["cat", "dog"]])  # ['CAT', 'DOG']'''),
        ("Make a dict mapping each of 1..4 to True if even else False.", "Dict comprehension.",
         r'''print({n: n % 2 == 0 for n in range(1, 5)})
# {1: False, 2: True, 3: False, 4: True}'''),
        ("From a sentence, build a list of word lengths.", "split then len.",
         r'''s = "the quick brown fox"
print([len(w) for w in s.split()])  # [3, 5, 5, 3]'''),
        ("Replace negatives with 0 in [3,-1,4,-5] using a conditional expression.", "if/else before for.",
         r'''print([x if x > 0 else 0 for x in [3, -1, 4, -5]])  # [3, 0, 4, 0]'''),
        ("Get the set of unique vowels in 'mississippi alabama'.", "Set comprehension over chars.",
         r'''s = "mississippi alabama"
print({c for c in s if c in "aeiou"})  # {'i', 'a'}'''),
        ("Flatten [[1,2],[3,4],[5]] into [1,2,3,4,5] with a nested comprehension.", "Two for clauses.",
         r'''nested = [[1, 2], [3, 4], [5]]
print([x for row in nested for x in row])  # [1, 2, 3, 4, 5]'''),
    ],
}

CONTENT["functions"] = {
    "what": (
        "A **function** is a reusable, named block of code defined with `def`. It can take "
        "**parameters** (inputs), do work, and `return` a result. Python supports **default "
        "values**, **keyword arguments**, and catch-all `*args` (extra positional) and `**kwargs` "
        "(extra keyword) parameters."
    ),
    "why": (
        "Functions are how you avoid repeating yourself and how you break big problems into small, "
        "testable pieces. Every library you'll use is just a collection of functions. Writing clear "
        "functions is the single biggest step from 'scripting' to 'programming'."
    ),
    "concepts": [
        ("def / return", "`def add(a, b): return a + b`. No return -> the function returns None."),
        ("Parameters vs arguments", "Parameters are names in the def; arguments are values you pass."),
        ("Default values", "`def greet(name='friend'):` makes name optional."),
        ("Keyword arguments", "Call with names for clarity: `area(width=3, height=4)`."),
        ("*args / **kwargs", "Accept any number of extra positional / keyword arguments."),
        ("Docstrings", "A string on the first line documents what the function does."),
    ],
    "examples": [
        ("Defining and calling functions", r'''
def add(a, b):
    "Return the sum of a and b."   # docstring
    return a + b

result = add(3, 4)
print("add(3, 4) =", result)       # 7

# A function with no return gives back None
def shout(text):
    print(text.upper() + "!")

value = shout("hello")             # prints HELLO!
print("shout returned:", value)    # None
'''),
        ("Default values and keyword arguments", r'''
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ada"))                    # Hello, Ada!
print(greet("Ada", "Welcome"))         # Welcome, Ada!
print(greet(greeting="Hi", name="Bo")) # keyword args -> order doesn't matter

def area(width, height):
    return width * height
print(area(height=4, width=3))         # 12
'''),
        ("*args and **kwargs for flexible functions", r'''
def total(*args):              # args is a tuple of everything passed
    return sum(args)
print(total(1, 2, 3, 4))       # 10

def describe(**kwargs):        # kwargs is a dict of named arguments
    for key, value in kwargs.items():
        print(f"{key} = {value}")
describe(name="Ada", role="pioneer")

# Returning multiple values (really returns a tuple)
def min_max(nums):
    return min(nums), max(nums)
low, high = min_max([4, 9, 1, 7])
print("low/high:", low, high)  # 1 9
'''),
    ],
    "gotchas": [
        "NEVER use a mutable default like `def f(items=[]):` — the SAME list is reused across calls. Use `None` and create inside.",
        "A function with no `return` returns `None`; `x = print('hi')` makes x None, not 'hi'.",
        "Positional arguments must come before keyword arguments in a call.",
        "Indentation defines the function body; a mis-indented line silently leaves the function.",
        "Shadowing built-ins (naming a function `list` or `sum`) breaks them for the rest of your code.",
    ],
    "exercises": [
        ("Write a function square(n) that returns n*n, and print square(6).", "return n*n.",
         r'''def square(n):
    return n * n
print(square(6))  # 36'''),
        ("Write greet(name, greeting='Hi') and call it both with and without the greeting.", "Default param.",
         r'''def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"
print(greet("Ada"))
print(greet("Ada", "Welcome"))'''),
        ("Write average(*nums) that returns the mean of any count of numbers.", "sum/len, guard empty.",
         r'''def average(*nums):
    return sum(nums) / len(nums) if nums else 0
print(average(2, 4, 6))  # 4.0'''),
        ("Write is_even(n) returning True/False and test 10 and 7.", "n % 2 == 0.",
         r'''def is_even(n):
    return n % 2 == 0
print(is_even(10), is_even(7))  # True False'''),
        ("Write min_max(lst) returning both the min and max as a tuple.", "Return two values.",
         r'''def min_max(lst):
    return min(lst), max(lst)
print(min_max([3, 8, 1]))  # (1, 8)'''),
        ("Write a function that counts vowels in a string.", "Loop and tally.",
         r'''def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
print(count_vowels("Education"))  # 5'''),
        ("Fix this buggy function that uses a mutable default to accumulate items.",
         "Use None as the default.",
         r'''def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b']  (not ['a','b']!)'''),
        ("Write describe(**kwargs) that prints each keyword argument as 'key: value'.", "Iterate items().",
         r'''def describe(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
describe(name="Ada", age=36)'''),
    ],
}

CONTENT["lambda-map-filter-reduce"] = {
    "what": (
        "A **lambda** is a tiny, anonymous one-line function: `lambda x: x*2`. It pairs naturally "
        "with **map** (apply a function to every item), **filter** (keep items that pass a test), "
        "and **reduce** (combine all items into one value). These are the building blocks of the "
        "'functional' style."
    ),
    "why": (
        "You'll see lambdas everywhere as `key=` arguments to `sorted()`, `min()`, and `max()`, and "
        "map/filter are concise ways to transform data. Understanding them helps you read others' "
        "code and write compact pipelines."
    ),
    "concepts": [
        ("lambda", "`lambda args: expression` — a function with no name and a single expression."),
        ("map(func, iterable)", "Applies func to each item; returns a lazy iterator (wrap in list())."),
        ("filter(func, iterable)", "Keeps items where func returns True."),
        ("reduce(func, iterable)", "From functools; folds items into one value (e.g., product)."),
        ("key= functions", "`sorted(data, key=lambda x: x[1])` sorts by a computed value."),
    ],
    "examples": [
        ("lambda and sorting with key=", r'''
double = lambda x: x * 2          # same as: def double(x): return x*2
print(double(5))                  # 10

# Real-world use: sort by a computed key
people = [("Ada", 36), ("Bo", 19), ("Cy", 54)]
by_age = sorted(people, key=lambda person: person[1])
print(by_age)                     # sorted by the age (2nd item)

words = ["banana", "kiwi", "apple"]
print(sorted(words, key=len))     # shortest to longest
'''),
        ("map and filter", r'''
nums = [1, 2, 3, 4, 5, 6]

# map: transform every item (remember to wrap in list to see it)
squares = list(map(lambda x: x * x, nums))
print(squares)                    # [1, 4, 9, 16, 25, 36]

# filter: keep items that pass the test
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                      # [2, 4, 6]

# Often a comprehension is clearer than map/filter:
print([x * x for x in nums if x % 2 == 0])   # [4, 16, 36]
'''),
        ("reduce for folding values", r'''
from functools import reduce

nums = [1, 2, 3, 4, 5]

# reduce(func, iterable): combine left-to-right into a single value
product = reduce(lambda acc, x: acc * x, nums)
print("product:", product)        # 120  (1*2*3*4*5)

total = reduce(lambda acc, x: acc + x, nums, 0)  # 0 is the start value
print("sum:", total)              # 15  (but just use sum(nums)!)

longest = reduce(lambda a, b: a if len(a) >= len(b) else b,
                 ["hi", "hello", "hey"])
print("longest:", longest)        # hello
'''),
    ],
    "gotchas": [
        "`map`/`filter` return lazy ITERATORS in Python 3 — print them and you get `<map object>`. Wrap in `list()`.",
        "A lambda can only hold ONE expression — no statements, loops, or assignments inside.",
        "Don't assign a lambda to a name (`f = lambda x: ...`); just use `def` — it's clearer and debuggable.",
        "`reduce` must be imported from functools; it's not a built-in. For sums/products prefer `sum()` / `math.prod()`.",
        "Overusing map/filter/lambda can be less readable than a simple comprehension — pick the clearer one.",
    ],
    "exercises": [
        ("Use map to triple every number in [1,2,3,4].", "list(map(lambda x: x*3, ...)).",
         r'''print(list(map(lambda x: x * 3, [1, 2, 3, 4])))  # [3, 6, 9, 12]'''),
        ("Use filter to keep words longer than 3 letters from ['hi','tree','no','code'].", "len > 3.",
         r'''words = ["hi", "tree", "no", "code"]
print(list(filter(lambda w: len(w) > 3, words)))  # ['tree', 'code']'''),
        ("Sort ['bb','a','ccc'] by length using sorted with a key.", "key=len.",
         r'''print(sorted(["bb", "a", "ccc"], key=len))  # ['a', 'bb', 'ccc']'''),
        ("Use reduce to compute the product of [2,3,4].", "functools.reduce.",
         r'''from functools import reduce
print(reduce(lambda a, x: a * x, [2, 3, 4]))  # 24'''),
        ("Find the person with the max age from [('A',30),('B',45)] using max and a key.", "key=lambda p: p[1].",
         r'''people = [("A", 30), ("B", 45)]
print(max(people, key=lambda p: p[1]))  # ('B', 45)'''),
        ("Use map to convert ['1','2','3'] to integers and sum them.", "map(int, ...).",
         r'''print(sum(map(int, ["1", "2", "3"])))  # 6'''),
        ("Rewrite list(map(lambda x: x+1, nums)) as a list comprehension.", "[x+1 for x in nums].",
         r'''nums = [10, 20, 30]
print([x + 1 for x in nums])  # [11, 21, 31]'''),
        ("Sort a list of dicts [{'n':'A','s':3},{'n':'B','s':9}] by 's' descending.",
         "key + reverse=True.",
         r'''data = [{"n": "A", "s": 3}, {"n": "B", "s": 9}]
print(sorted(data, key=lambda d: d["s"], reverse=True))'''),
    ],
}

CONTENT["scope"] = {
    "what": (
        "**Scope** is the region of code where a name is visible. Python uses the **LEGB** rule to "
        "find names: **L**ocal (inside the current function), **E**nclosing (an outer function), "
        "**G**lobal (the module/file level), then **B**uilt-in. The `global` and `nonlocal` keywords "
        "let you reassign names from outer scopes."
    ),
    "why": (
        "Scope explains why a variable 'disappears' outside a function, why you sometimes get "
        "surprising `UnboundLocalError`s, and how closures work. Knowing LEGB removes a whole "
        "category of confusing bugs."
    ),
    "concepts": [
        ("Local", "Names assigned inside a function — invisible outside it."),
        ("Enclosing", "The scope of an outer function around a nested one."),
        ("Global", "Names at the top level of the file."),
        ("Built-in", "Names Python provides (print, len, range...)."),
        ("global keyword", "Lets a function REASSIGN a module-level variable."),
        ("nonlocal keyword", "Lets a nested function REASSIGN a variable in its enclosing function."),
    ],
    "examples": [
        ("Local vs global", r'''
x = "global"

def show():
    x = "local"          # a NEW local variable, separate from the global
    print("inside:", x)  # local

show()
print("outside:", x)     # global  -- unchanged

def reader():
    print("reading global:", x)   # OK to READ the global without 'global'
reader()
'''),
        ("global and nonlocal", r'''
counter = 0

def increment():
    global counter        # without this, the next line creates a local!
    counter += 1

increment()
increment()
print("counter:", counter)   # 2

def make_adder():
    total = 0
    def add(n):
        nonlocal total     # reassign the ENCLOSING total, not a new local
        total += n
        return total
    return add

acc = make_adder()
print(acc(10))   # 10
print(acc(5))    # 15  (state remembered via the enclosing scope)
'''),
        ("The classic UnboundLocalError trap", r'''
value = 100

def buggy():
    # Because we ASSIGN to value below, Python treats it as LOCAL everywhere
    # in this function -> reading it first raises UnboundLocalError.
    try:
        print(value)      # error: local 'value' used before assignment
        value = 1
    except UnboundLocalError as e:
        print("Caught:", e)

buggy()

def fixed():
    global value
    print(value)          # now refers to the global -> 100
    value = 1
fixed()
'''),
    ],
    "gotchas": [
        "Assigning to a name ANYWHERE in a function makes it local for the WHOLE function — causing UnboundLocalError if you read it first.",
        "Overusing `global` makes code hard to follow and test. Prefer passing values in and returning them out.",
        "`nonlocal` targets the nearest enclosing FUNCTION scope, not the global scope.",
        "You can READ a global inside a function without declaring it; you only need `global` to REASSIGN it.",
        "Loop variables (`for i in ...`) leak into the surrounding scope after the loop — they aren't function-scoped.",
    ],
    "exercises": [
        ("Predict the output: define x=5 globally, a function that sets x=10 locally and prints it, then print x outside.",
         "Local assignment shadows global.",
         r'''x = 5
def f():
    x = 10
    print(x)  # 10
f()
print(x)      # 5'''),
        ("Use global to make a function increase a module-level count by 1.", "global count.",
         r'''count = 0
def inc():
    global count
    count += 1
inc(); inc()
print(count)  # 2'''),
        ("Write a counter using a closure and nonlocal that returns 1, 2, 3 on successive calls.",
         "nonlocal in a nested function.",
         r'''def make_counter():
    n = 0
    def step():
        nonlocal n
        n += 1
        return n
    return step
c = make_counter()
print(c(), c(), c())  # 1 2 3'''),
        ("Explain why reading then assigning a global inside a function (without 'global') errors.",
         "",
         r'''#md
Assigning to the name anywhere in the function marks it **local for the entire
function body**. So the earlier read happens before the local is assigned →
`UnboundLocalError`. Declare `global name` (or don't reassign it) to fix.'''),
        ("Show that you can READ a global inside a function without the global keyword.", "Just reference it.",
         r'''msg = "hi"
def show():
    print(msg)  # reading is fine
show()  # hi'''),
        ("What does the built-in `len` refer to inside a function — which letter of LEGB?", "B.",
         r'''#md
**B (Built-in).** `len` isn't local, enclosing, or global in your file, so Python
finds it last in the built-in scope. (Don't create a variable named `len` or you
shadow it!)'''),
        ("Demonstrate a loop variable still existing after the loop ends.", "Print i after the for loop.",
         r'''for i in range(3):
    pass
print(i)  # 2  -> the loop variable leaks out'''),
        ("Refactor a global-counter function into one that takes the count and returns count+1 (no global).",
         "Pure function style.",
         r'''def inc(count):
    return count + 1
c = 0
c = inc(c)
c = inc(c)
print(c)  # 2'''),
    ],
}

CONTENT["recursion-basics"] = {
    "what": (
        "**Recursion** is when a function calls itself to solve a smaller version of the same "
        "problem. Every recursive function needs a **base case** (when to stop) and a **recursive "
        "case** (call itself on something smaller, moving toward the base case). Classic examples: "
        "factorial, Fibonacci, and summing a list."
    ),
    "why": (
        "Recursion is the natural way to express problems with self-similar structure: trees, "
        "graphs, divide-and-conquer sorting, and backtracking. It's a core mental model you'll use "
        "heavily in DSA (Phase 3)."
    ),
    "concepts": [
        ("Base case", "The simplest input where the answer is known directly — stops the recursion."),
        ("Recursive case", "Solve a smaller subproblem and combine: `n * factorial(n-1)`."),
        ("Call stack", "Each call waits for its sub-call; too deep -> RecursionError."),
        ("Progress toward base", "Each call MUST get closer to the base case or it loops forever."),
        ("Recursion vs iteration", "Anything recursive can be written as a loop; pick the clearer one."),
    ],
    "examples": [
        ("Factorial: the 'hello world' of recursion", r'''
def factorial(n):
    if n <= 1:               # base case: 0! and 1! are 1
        return 1
    return n * factorial(n - 1)   # recursive case: shrink toward the base

print(factorial(5))   # 120  (5*4*3*2*1)

# Trace: factorial(3) = 3*factorial(2) = 3*2*factorial(1) = 3*2*1 = 6
print(factorial(3))   # 6
'''),
        ("Sum a list and reverse a string recursively", r'''
def sum_list(items):
    if not items:            # base case: empty list sums to 0
        return 0
    return items[0] + sum_list(items[1:])   # first + sum of the rest

print(sum_list([1, 2, 3, 4]))   # 10

def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]   # reverse the tail, put first char at the end

print(reverse("hello"))   # olleh
'''),
        ("Fibonacci, and why naive recursion can be slow", r'''
def fib(n):
    if n < 2:                # base cases: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])   # 0 1 1 2 3 5 8 13 21 34

# The naive version recomputes the same values exponentially.
# 'memoization' caches results to make it fast:
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_fast(n):
    return n if n < 2 else fib_fast(n - 1) + fib_fast(n - 2)

print(fib_fast(50))   # 12586269025  (instant, thanks to caching)
'''),
    ],
    "gotchas": [
        "Forgetting the base case (or never reaching it) causes infinite recursion -> RecursionError.",
        "Python's default recursion limit is ~1000; very deep recursion crashes. Use iteration for huge depths.",
        "Naive recursive Fibonacci is exponential — add memoization (`@lru_cache`) or use a loop.",
        "Slicing (`items[1:]`) copies the list each call — fine for learning, costly for big inputs.",
        "Each recursive call uses stack memory; recursion isn't free even when correct.",
    ],
    "exercises": [
        ("Write factorial(n) recursively and print factorial(6).", "Base case n<=1.",
         r'''def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
print(factorial(6))  # 720'''),
        ("Write a recursive function to sum numbers from 1 to n. Test n=5.", "n + sum(n-1).",
         r'''def s(n):
    return 0 if n == 0 else n + s(n - 1)
print(s(5))  # 15'''),
        ("Recursively count down from n to 1, printing each. Test n=4.", "Print then recurse.",
         r'''def countdown(n):
    if n < 1:
        return
    print(n)
    countdown(n - 1)
countdown(4)'''),
        ("Write a recursive power(base, exp) (exp>=0). Test power(2,8).", "base * power(base, exp-1).",
         r'''def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp - 1)
print(power(2, 8))  # 256'''),
        ("Recursively reverse the string 'recursion'.", "tail + first char.",
         r'''def rev(s):
    return s if len(s) <= 1 else rev(s[1:]) + s[0]
print(rev("recursion"))  # noisrucer'''),
        ("Write recursive fib(n) and print the 10th Fibonacci number (fib(10)).", "fib(n-1)+fib(n-2).",
         r'''def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(10))  # 55'''),
        ("Count the number of digits in an integer recursively. Test 9043.", "n//10 each step.",
         r'''def digits(n):
    n = abs(n)
    return 1 if n < 10 else 1 + digits(n // 10)
print(digits(9043))  # 4'''),
        ("Speed up your fib with @lru_cache and compute fib(40).", "from functools import lru_cache.",
         r'''from functools import lru_cache
@lru_cache(None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(40))  # 102334155'''),
    ],
}

CONTENT["exception-handling"] = {
    "what": (
        "**Exceptions** are errors that happen while a program runs (dividing by zero, a missing "
        "file, bad input). Instead of crashing, you can **catch** them with `try`/`except`. `else` "
        "runs when no error occurred, `finally` always runs (great for cleanup), and `raise` lets "
        "you signal your own errors."
    ),
    "why": (
        "Real programs face messy input and unreliable resources. Graceful error handling is the "
        "difference between a program that crashes and one that recovers, logs the problem, and "
        "keeps going. It's essential for files, networks, and APIs."
    ),
    "concepts": [
        ("try / except", "Run risky code; if it raises, jump to the matching except block."),
        ("Specific exceptions", "Catch `ValueError`, `KeyError`, etc. — not bare `except:`."),
        ("else", "Runs only if the try block succeeded with no exception."),
        ("finally", "Always runs (success or failure) — perfect for closing resources."),
        ("raise", "Trigger an exception yourself: `raise ValueError('bad input')`."),
        ("Exception object", "`except ValueError as e:` lets you inspect the message."),
    ],
    "examples": [
        ("Catching specific exceptions", r'''
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # message, then None

# Catch different errors differently
for value in ["42", "oops"]:
    try:
        print("parsed:", int(value))
    except ValueError as e:
        print("Bad number:", e)
'''),
        ("else and finally", r'''
def read_config(text):
    try:
        number = int(text)
    except ValueError:
        print("Not a valid integer")
    else:
        print("Success! Got", number)   # only if no exception
    finally:
        print("done checking")           # always runs

read_config("100")
print("---")
read_config("nope")
'''),
        ("Raising your own exceptions", r'''
def set_age(age):
    if age < 0:
        raise ValueError(f"age can't be negative: {age}")
    return age

print(set_age(30))     # 30
try:
    set_age(-5)
except ValueError as e:
    print("Rejected:", e)

# You can catch multiple types at once
try:
    data = {"a": 1}
    print(data["z"])
except (KeyError, TypeError) as e:
    print("Lookup failed:", repr(e))
'''),
    ],
    "gotchas": [
        "Avoid bare `except:` — it hides bugs and even catches Ctrl-C. Catch specific exceptions.",
        "Don't put a huge block in `try`; wrap only the line(s) that can actually fail.",
        "`except` order matters: put specific exceptions before general ones (Exception last).",
        "Swallowing errors silently (`except: pass`) makes debugging miserable — at least log them.",
        "`finally` runs even if you `return` inside try — use it for cleanup, not for return values.",
    ],
    "exercises": [
        ("Safely convert the string 'abc' to int, printing 'invalid' instead of crashing.", "Catch ValueError.",
         r'''try:
    int("abc")
except ValueError:
    print("invalid")'''),
        ("Write divide(a,b) that returns None and prints a message on division by zero.", "ZeroDivisionError.",
         r'''def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("nope")
        return None
print(divide(6, 0))'''),
        ("Look up a missing key 'x' in {'a':1} and print 'missing' instead of raising.", "KeyError.",
         r'''d = {"a": 1}
try:
    print(d["x"])
except KeyError:
    print("missing")'''),
        ("Use finally to always print 'cleanup' whether or not an error happens.", "try/finally.",
         r'''try:
    x = 1 / 1
finally:
    print("cleanup")'''),
        ("Raise a ValueError if a withdrawal amount is greater than balance 100.", "raise.",
         r'''def withdraw(amount, balance=100):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
try:
    withdraw(150)
except ValueError as e:
    print(e)'''),
        ("Catch both KeyError and IndexError with one except clause.", "except (A, B).",
         r'''try:
    [][5]
except (KeyError, IndexError) as e:
    print("caught", type(e).__name__)'''),
        ("Loop over ['10','x','5'], summing only the valid integers; skip bad ones.", "try inside loop.",
         r'''total = 0
for v in ["10", "x", "5"]:
    try:
        total += int(v)
    except ValueError:
        continue
print(total)  # 15'''),
        ("Use try/except/else: parse '7', and only if it succeeds print its square.", "else block.",
         r'''try:
    n = int("7")
except ValueError:
    print("bad")
else:
    print(n ** 2)  # 49'''),
    ],
}

CONTENT["file-handling"] = {
    "what": (
        "File handling lets your program **read from** and **write to** files on disk. The modern "
        "way is the `with open(path, mode) as f:` block, which automatically closes the file for "
        "you. Modes: `'r'` read, `'w'` write (overwrites!), `'a'` append, `'r+'` read/write. Always "
        "pass `encoding='utf-8'` for text."
    ),
    "why": (
        "Programs need to persist data — config, logs, datasets, results. Reading CSVs for data "
        "science, saving model outputs, processing text files: all start with file handling. The "
        "`with` pattern prevents the classic 'forgot to close the file' resource leak."
    ),
    "concepts": [
        ("open(path, mode)", "Opens a file; returns a file object. Pair with `with` to auto-close."),
        ("with statement", "`with open(...) as f:` closes the file even if an error occurs."),
        ("Modes", "'r' read, 'w' overwrite, 'a' append, 'x' create-new, add 'b' for binary."),
        ("read / readline / readlines", "Whole file / one line / list of lines. Or just iterate the file."),
        ("write / writelines", "Write a string / a list of strings (you add newlines yourself)."),
        ("encoding", "Use encoding='utf-8' for text to avoid platform-dependent bugs."),
    ],
    "examples": [
        ("Writing and reading a text file", r'''
import os
path = "demo.txt"

# WRITE mode 'w' creates (or OVERWRITES) the file
with open(path, "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")

# READ the whole file
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

os.remove(path)   # clean up the demo file
'''),
        ("Appending and reading line by line", r'''
import os
path = "log.txt"

with open(path, "w", encoding="utf-8") as f:
    f.write("line 1\n")

# APPEND mode 'a' adds to the end without erasing
with open(path, "a", encoding="utf-8") as f:
    f.write("line 2\n")
    f.write("line 3\n")

# Iterating a file yields one line at a time (memory friendly)
with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())   # strip removes the trailing \n

os.remove(path)
'''),
        ("Safe reading with error handling", r'''
def read_or_default(path, default="(no file)"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default

print(read_or_default("does_not_exist.txt"))   # (no file)

# Read all lines into a list
import os
with open("nums.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\n30\n")
with open("nums.txt", "r", encoding="utf-8") as f:
    numbers = [int(line) for line in f]
print("sum:", sum(numbers))    # 60
os.remove("nums.txt")
'''),
    ],
    "gotchas": [
        "Mode `'w'` ERASES the file's contents immediately. Use `'a'` to add without losing data.",
        "Always use `with open(...)` so the file is closed automatically — even when an error occurs.",
        "`f.read()` loads the WHOLE file into memory; for big files iterate line by line instead.",
        "Lines from a file keep their trailing `\\n`; call `.strip()` when you don't want it.",
        "Without `encoding='utf-8'`, behavior differs across operating systems and can corrupt text.",
    ],
    "exercises": [
        ("Write 'Hello file' to greeting.txt, then read and print it. Clean up after.", "with open, 'w' then 'r'.",
         r'''import os
with open("greeting.txt", "w", encoding="utf-8") as f:
    f.write("Hello file")
with open("greeting.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("greeting.txt")'''),
        ("Append two new lines to a file that already has one line, then print all lines.", "mode 'a'.",
         r'''import os
with open("f.txt", "w", encoding="utf-8") as f:
    f.write("one\n")
with open("f.txt", "a", encoding="utf-8") as f:
    f.write("two\nthree\n")
with open("f.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("f.txt")'''),
        ("Count the number of lines in a file you create with 4 lines.", "Iterate and count, or len(readlines).",
         r'''import os
with open("c.txt", "w", encoding="utf-8") as f:
    f.write("a\nb\nc\nd\n")
with open("c.txt", encoding="utf-8") as f:
    print(sum(1 for _ in f))  # 4
os.remove("c.txt")'''),
        ("Read a file of numbers (one per line) and print their sum.", "int(line) in a comprehension.",
         r'''import os
with open("n.txt", "w", encoding="utf-8") as f:
    f.write("3\n4\n5\n")
with open("n.txt", encoding="utf-8") as f:
    print(sum(int(x) for x in f))  # 12
os.remove("n.txt")'''),
        ("Read a missing file and print 'not found' instead of crashing.", "FileNotFoundError.",
         r'''try:
    open("nope.txt", encoding="utf-8")
except FileNotFoundError:
    print("not found")'''),
        ("Write a list ['a','b','c'] to a file, one item per line.", "Join with newlines or loop.",
         r'''import os
items = ["a", "b", "c"]
with open("l.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(items))
with open("l.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("l.txt")'''),
        ("Copy the contents of one file into another.", "Read from one, write to the other.",
         r'''import os
with open("src.txt", "w", encoding="utf-8") as f:
    f.write("copy me")
with open("src.txt", encoding="utf-8") as src, open("dst.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())
with open("dst.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("src.txt"); os.remove("dst.txt")'''),
        ("Read a file and print only the lines that contain the word 'error'.", "Check 'error' in line.",
         r'''import os
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("ok\nerror: disk\nfine\nerror: net\n")
with open("log.txt", encoding="utf-8") as f:
    for line in f:
        if "error" in line:
            print(line.strip())
os.remove("log.txt")'''),
    ],
}

CONTENT["modules-and-packages"] = {
    "what": (
        "A **module** is just a `.py` file you can import to reuse its code. A **package** is a "
        "folder of modules (historically marked by an `__init__.py`). Python ships a huge **standard "
        "library** (math, random, os, json, datetime...). You import with `import x`, `from x import "
        "y`, or `import x as alias`."
    ),
    "why": (
        "You don't write everything from scratch — you stand on the shoulders of the standard "
        "library and third-party packages. Organizing your own code into modules keeps projects "
        "maintainable as they grow."
    ),
    "concepts": [
        ("import x", "Loads a module; access its contents as `x.thing`."),
        ("from x import y", "Pulls a specific name into your namespace: use `y` directly."),
        ("import x as alias", "Rename on import: `import numpy as np`."),
        ("Standard library", "Batteries included: math, random, os, sys, json, datetime, collections..."),
        ("__name__ == '__main__'", "True only when the file is run directly, not imported."),
        ("Package", "A directory of modules; import submodules with dots: `pkg.module`."),
    ],
    "examples": [
        ("Importing from the standard library", r'''
import math
import random
from datetime import date

print(math.pi)                 # 3.141592653589793
print(math.factorial(5))       # 120

random.seed(0)                 # make randomness repeatable for demos
print(random.randint(1, 6))    # a dice roll
print(random.choice(["a", "b", "c"]))

print(date.today().year >= 2020)   # True
'''),
        ("Different import styles", r'''
# 1) import the whole module
import statistics
print(statistics.mean([2, 4, 6]))      # 4

# 2) import specific names (use them directly)
from statistics import median, mode
print(median([1, 3, 5, 7]))            # 4.0

# 3) import with an alias (very common in data science)
import json as J
print(J.dumps({"ok": True}))           # {"ok": true}

# Explore what a module offers
import string
print(string.ascii_lowercase)          # abcdefghijklmnopqrstuvwxyz
'''),
        ("The __name__ guard (module vs script)", r'''
# This pattern lets a file work BOTH as an importable module AND a script.
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Runs only when you do `python thisfile.py`,
    # NOT when another file does `import thisfile`.
    print(greet("world"))
    print("Running as a script.")
'''),
    ],
    "gotchas": [
        "`from module import *` dumps everything into your namespace and can clash — avoid it.",
        "Naming your file the same as a stdlib module (e.g. `random.py`) shadows the real one.",
        "Circular imports (A imports B which imports A) cause errors — restructure your modules.",
        "Forgetting `if __name__ == '__main__':` makes your demo code run when the file is imported.",
        "Re-importing doesn't re-run a module; Python caches it. Restart or use importlib.reload to refresh.",
    ],
    "exercises": [
        ("Import math and print the square root of 81.", "math.sqrt.",
         r'''import math
print(math.sqrt(81))  # 9.0'''),
        ("Use random (seeded with 0) to pick a random item from ['x','y','z'].", "random.choice.",
         r'''import random
random.seed(0)
print(random.choice(["x", "y", "z"]))'''),
        ("Import only mean from statistics and average [10,20,30].", "from statistics import mean.",
         r'''from statistics import mean
print(mean([10, 20, 30]))  # 20'''),
        ("Import json as J and turn {'a':1} into a JSON string.", "J.dumps.",
         r'''import json as J
print(J.dumps({"a": 1}))  # {"a": 1}'''),
        ("Use datetime to print today's year.", "date.today().year.",
         r'''from datetime import date
print(date.today().year)'''),
        ("Use collections.Counter to count letters in 'banana'.", "Counter(str).",
         r'''from collections import Counter
print(Counter("banana"))  # Counter({'a': 3, 'n': 2, 'b': 1})'''),
        ("Write the __main__ guard for a file with a function main() that prints 'run'.", "if __name__...",
         r'''def main():
    print("run")
if __name__ == "__main__":
    main()'''),
        ("Use os to print the current working directory.", "os.getcwd().",
         r'''import os
print(os.getcwd())'''),
    ],
}

CONTENT["virtual-environments"] = {
    "what": (
        "A **virtual environment** is an isolated, per-project copy of Python and its installed "
        "packages. You create one with `python -m venv .venv`, **activate** it, then `pip install` "
        "packages that live ONLY inside that project. This stops different projects from fighting "
        "over package versions."
    ),
    "why": (
        "Project A might need pandas 1.x while Project B needs 2.x. Installing globally creates "
        "conflicts and 'works on my machine' chaos. Virtual environments + a `requirements.txt` make "
        "your projects reproducible — essential for real ML work and collaboration."
    ),
    "concepts": [
        ("venv", "Built-in tool: `python -m venv .venv` creates an isolated environment folder."),
        ("Activation", "`source .venv/bin/activate` (mac/Linux) or `.venv\\Scripts\\activate` (Windows)."),
        ("pip freeze", "Lists installed packages with versions: `pip freeze > requirements.txt`."),
        ("requirements.txt", "A text list of dependencies; `pip install -r requirements.txt` reinstalls them."),
        ("Isolation", "Packages install into the active env, not system-wide."),
        ("sys.prefix", "Shows which environment Python is currently using."),
    ],
    "examples": [
        ("Detect whether you're in a virtual environment (runnable)", r'''
import sys
import os

# When a venv is active, sys.prefix differs from sys.base_prefix
in_venv = sys.prefix != sys.base_prefix
print("Running inside a virtual environment?", in_venv)
print("Environment path (sys.prefix):", sys.prefix)

# The VIRTUAL_ENV env var is set by activation scripts
print("VIRTUAL_ENV =", os.environ.get("VIRTUAL_ENV", "(not set)"))
'''),
        ("The typical workflow (these are shell commands, shown as text)", r'''
# This example just PRINTS the commands you would run in a terminal.
workflow = [
    "python -m venv .venv",                 # 1. create the environment
    "source .venv/bin/activate",            # 2. activate (mac/Linux)",
    "#  .venv\\Scripts\\activate           (Windows PowerShell)",
    "pip install requests pandas",          # 3. install into the env
    "pip freeze > requirements.txt",        # 4. record exact versions
    "deactivate",                           # 5. leave the environment
]
for step in workflow:
    print(step)
'''),
        ("Inspect installed packages from Python", r'''
import importlib.metadata as meta

# List a few installed distributions and their versions
seen = 0
for dist in meta.distributions():
    name = dist.metadata["Name"]
    print(name, dist.version)
    seen += 1
    if seen >= 5:        # just show the first few
        break
print("...")
'''),
    ],
    "gotchas": [
        "Creating a venv isn't enough — you must ACTIVATE it each new terminal session.",
        "If `pip install` seems to go to the wrong place, your venv probably isn't active; check `which python`.",
        "Add `.venv/` to `.gitignore` — never commit the environment; commit `requirements.txt` instead.",
        "`pip freeze` captures EXACT versions; great for reproducibility but pin thoughtfully for libraries.",
        "Activating in one terminal doesn't affect others — each shell needs its own activation.",
    ],
    "exercises": [
        ("Write code that prints whether the current Python is inside a virtual environment.",
         "Compare sys.prefix and sys.base_prefix.",
         r'''import sys
print(sys.prefix != sys.base_prefix)'''),
        ("List the shell commands to create and activate a venv on Linux.", "",
         r'''#md
```bash
python -m venv .venv
source .venv/bin/activate
```'''),
        ("What command records your installed packages to requirements.txt?", "",
         r'''#md
```bash
pip freeze > requirements.txt
```'''),
        ("What single command reinstalls everything listed in requirements.txt?", "",
         r'''#md
```bash
pip install -r requirements.txt
```'''),
        ("Print the value of the VIRTUAL_ENV environment variable (or a default).", "os.environ.get.",
         r'''import os
print(os.environ.get("VIRTUAL_ENV", "no venv active"))'''),
        ("Why should .venv/ be in .gitignore?", "",
         r'''#md
The environment is large, machine-specific, and fully reproducible from
`requirements.txt`. Committing it bloats the repo and breaks on other OSes.
Commit the requirements file, not the environment.'''),
        ("Print the Python executable path so you can confirm which environment is active.", "sys.executable.",
         r'''import sys
print(sys.executable)'''),
        ("Name the activation command on Windows PowerShell.", "",
         r'''#md
```powershell
.venv\Scripts\Activate.ps1
```'''),
    ],
}
