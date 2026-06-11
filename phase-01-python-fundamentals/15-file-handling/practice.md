# 15 — File Handling: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write 'Hello file' to greeting.txt, then read and print it. Clean up after.

*Hint: with open, 'w' then 'r'.*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("greeting.txt", "w", encoding="utf-8") as f:
    f.write("Hello file")
with open("greeting.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("greeting.txt")
```

</details>

## Exercise 2

Append two new lines to a file that already has one line, then print all lines.

*Hint: mode 'a'.*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("f.txt", "w", encoding="utf-8") as f:
    f.write("one\n")
with open("f.txt", "a", encoding="utf-8") as f:
    f.write("two\nthree\n")
with open("f.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("f.txt")
```

</details>

## Exercise 3

Count the number of lines in a file you create with 4 lines.

*Hint: Iterate and count, or len(readlines).*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("c.txt", "w", encoding="utf-8") as f:
    f.write("a\nb\nc\nd\n")
with open("c.txt", encoding="utf-8") as f:
    print(sum(1 for _ in f))  # 4
os.remove("c.txt")
```

</details>

## Exercise 4

Read a file of numbers (one per line) and print their sum.

*Hint: int(line) in a comprehension.*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("n.txt", "w", encoding="utf-8") as f:
    f.write("3\n4\n5\n")
with open("n.txt", encoding="utf-8") as f:
    print(sum(int(x) for x in f))  # 12
os.remove("n.txt")
```

</details>

## Exercise 5

Read a missing file and print 'not found' instead of crashing.

*Hint: FileNotFoundError.*

<details>
<summary>✅ Solution</summary>

```python
try:
    open("nope.txt", encoding="utf-8")
except FileNotFoundError:
    print("not found")
```

</details>

## Exercise 6

Write a list ['a','b','c'] to a file, one item per line.

*Hint: Join with newlines or loop.*

<details>
<summary>✅ Solution</summary>

```python
import os
items = ["a", "b", "c"]
with open("l.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(items))
with open("l.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("l.txt")
```

</details>

## Exercise 7

Copy the contents of one file into another.

*Hint: Read from one, write to the other.*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("src.txt", "w", encoding="utf-8") as f:
    f.write("copy me")
with open("src.txt", encoding="utf-8") as src, open("dst.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())
with open("dst.txt", encoding="utf-8") as f:
    print(f.read())
os.remove("src.txt"); os.remove("dst.txt")
```

</details>

## Exercise 8

Read a file and print only the lines that contain the word 'error'.

*Hint: Check 'error' in line.*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("ok\nerror: disk\nfine\nerror: net\n")
with open("log.txt", encoding="utf-8") as f:
    for line in f:
        if "error" in line:
            print(line.strip())
os.remove("log.txt")
```

</details>

