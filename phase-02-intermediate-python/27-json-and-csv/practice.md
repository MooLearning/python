# 27 — JSON and CSV: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Convert the dict {'a':1,'b':[2,3]} to a JSON string.

*Hint: json.dumps.*

<details>
<summary>✅ Solution</summary>

```python
import json
print(json.dumps({"a": 1, "b": [2, 3]}))  # {"a": 1, "b": [2, 3]}
```

</details>

## Exercise 2

Parse the JSON string '{"x": 10}' and print x.

*Hint: json.loads.*

<details>
<summary>✅ Solution</summary>

```python
import json
print(json.loads('{"x": 10}')["x"])  # 10
```

</details>

## Exercise 3

Pretty-print {'name':'Ada','age':36} with 2-space indentation.

*Hint: indent=2.*

<details>
<summary>✅ Solution</summary>

```python
import json
print(json.dumps({"name": "Ada", "age": 36}, indent=2))
```

</details>

## Exercise 4

Write a dict to data.json and read it back.

*Hint: dump/load.*

<details>
<summary>✅ Solution</summary>

```python
import json, os
with open("d.json", "w") as f:
    json.dump({"ok": True}, f)
with open("d.json") as f:
    print(json.load(f))
os.remove("d.json")
```

</details>

## Exercise 5

Write two rows ['a','b'] and ['1','2'] to a CSV string.

*Hint: csv.writer + StringIO.*

<details>
<summary>✅ Solution</summary>

```python
import csv, io
buf = io.StringIO()
csv.writer(buf).writerows([["a", "b"], ["1", "2"]])
print(buf.getvalue())
```

</details>

## Exercise 6

Read CSV text 'x,y\n1,2\n3,4' and sum all the numbers.

*Hint: csv.reader, skip header.*

<details>
<summary>✅ Solution</summary>

```python
import csv, io
text = "x,y\n1,2\n3,4"
r = csv.reader(io.StringIO(text))
next(r)  # skip header
print(sum(int(c) for row in r for c in row))  # 10
```

</details>

## Exercise 7

Use DictReader to read 'name,age\nAda,36' and print the name.

*Hint: DictReader.*

<details>
<summary>✅ Solution</summary>

```python
import csv, io
r = csv.DictReader(io.StringIO("name,age\nAda,36"))
print(next(r)["name"])  # Ada
```

</details>

## Exercise 8

Round-trip a list of dicts through JSON (dumps then loads).

*Hint: dumps/loads.*

<details>
<summary>✅ Solution</summary>

```python
import json
data = [{"id": 1}, {"id": 2}]
print(json.loads(json.dumps(data)) == data)  # True
```

</details>

