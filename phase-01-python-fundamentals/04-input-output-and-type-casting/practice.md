# 04 — Input, Output and Type Casting: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Print `Name: Sam | Age: 20` using an f-string with variables name='Sam', age=20.

*Hint: f"...{name}...{age}..."*

<details>
<summary>✅ Solution</summary>

```python
name, age = "Sam", 20
print(f"Name: {name} | Age: {age}")
```

</details>

## Exercise 2

Ask for two numbers and print their sum (simulate input as '4' and '5').

*Hint: Cast both with int().*

<details>
<summary>✅ Solution</summary>

```python
a = int("4")
b = int("5")
print(a + b)  # 9
```

</details>

## Exercise 3

Print the floats 1, 2.5, 3.14159 each rounded to 1 decimal place.

*Hint: Use :.1f in f-strings.*

<details>
<summary>✅ Solution</summary>

```python
for x in (1, 2.5, 3.14159):
    print(f"{x:.1f}")
```

</details>

## Exercise 4

Convert the string '3.75' to a float and print double its value.

*Hint: float() then * 2.*

<details>
<summary>✅ Solution</summary>

```python
print(float("3.75") * 2)  # 7.5
```

</details>

## Exercise 5

Print 'a', 'b', 'c' on one line separated by commas using print's sep argument.

*Hint: sep=', '*

<details>
<summary>✅ Solution</summary>

```python
print("a", "b", "c", sep=", ")
```

</details>

## Exercise 6

Show that int('7') + int('8') is 15 but '7' + '8' is '78'.

*Hint: One casts, one concatenates.*

<details>
<summary>✅ Solution</summary>

```python
print(int("7") + int("8"))  # 15
print("7" + "8")            # 78
```

</details>

## Exercise 7

Turn the integer 2026 into the string 'Year 2026'.

*Hint: str() and concatenation or f-string.*

<details>
<summary>✅ Solution</summary>

```python
year = 2026
print("Year " + str(year))   # or: print(f"Year {year}")
```

</details>

## Exercise 8

Round 9.9 down to 9 with int(), and to 10 with round(); print both.

*Hint: int truncates, round rounds.*

<details>
<summary>✅ Solution</summary>

```python
print(int(9.9))    # 9
print(round(9.9))  # 10
```

</details>

