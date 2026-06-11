# 27 — JSON and CSV

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**JSON** and **CSV** are the two most common data interchange formats. JSON (JavaScript Object Notation) maps cleanly to Python dicts/lists — use `json.dumps`/`loads` for strings and `json.dump`/`load` for files. CSV (comma-separated values) is tabular text — use the `csv` module (or pandas later) to read/write rows.

## Why it matters

APIs speak JSON; spreadsheets and datasets ship as CSV. Reading and writing both is a daily task in data work — loading a dataset, saving results, or talking to a web service.

## Key concepts

- **json.dumps / loads** — Python object <-> JSON STRING.
- **json.dump / load** — Python object <-> JSON FILE (note: no 's').
- **Type mapping** — dict<->object, list<->array, str/int/float/bool/None map naturally.
- **csv.reader / writer** — Row-by-row lists; remember newline='' when opening files.
- **csv.DictReader / DictWriter** — Treat rows as dicts keyed by the header row.
- **Pretty printing** — json.dumps(obj, indent=2) for readable output.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import json

data = {"name": "Ada", "skills": ["python", "math"], "age": 36, "active": True}

# Object -> JSON string
text = json.dumps(data)
print(text)                          # {"name": "Ada", ...}
print(json.dumps(data, indent=2))    # pretty, multi-line

# JSON string -> object
back = json.loads(text)
print(back["skills"][0])             # python
print(type(back))                    # <class 'dict'>

# Save to / load from a file
import os
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
with open("data.json", "r", encoding="utf-8") as f:
    print(json.load(f)["name"])      # Ada
os.remove("data.json")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `json.dump`/`load` work with FILES; `json.dumps`/`loads` work with STRINGS (the 's' = string).
- ⚠️ JSON keys are always strings: `json.loads('{"1": 2}')` gives key '1', not int 1.
- ⚠️ JSON has no tuples, sets, or datetimes — convert them (e.g. list, isoformat) before dumping.
- ⚠️ When opening CSV files, pass `newline=''` or you may get blank lines between rows on Windows.
- ⚠️ CSV values are all strings — cast numbers yourself (`int(row['score'])`).

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

