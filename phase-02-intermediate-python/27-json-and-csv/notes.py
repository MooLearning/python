# ======================================================================
# 27 — JSON and CSV  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: JSON: strings and files
# ----------------------------------------------------------------------
print("\n--- Example 1: JSON: strings and files ---")
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

# ----------------------------------------------------------------------
# Example 2: CSV with the csv module
# ----------------------------------------------------------------------
print("\n--- Example 2: CSV with the csv module ---")
import csv, io

rows = [["name", "age"], ["Ada", "36"], ["Bo", "19"]]

# Write CSV to an in-memory buffer (works just like a file)
buf = io.StringIO()
writer = csv.writer(buf)
writer.writerows(rows)
print(buf.getvalue())     # name,age\nAda,36\nBo,19

# Read it back
buf.seek(0)
for record in csv.reader(buf):
    print(record)         # ['name', 'age'], then ['Ada', '36'], ...

# ----------------------------------------------------------------------
# Example 3: CSV as dictionaries (DictReader / DictWriter)
# ----------------------------------------------------------------------
print("\n--- Example 3: CSV as dictionaries (DictReader / DictWriter) ---")
import csv, io

text = "name,score\nAda,95\nBo,80\n"

# DictReader: each row becomes a dict keyed by the header
reader = csv.DictReader(io.StringIO(text))
for row in reader:
    print(row["name"], "->", int(row["score"]))

# DictWriter: write dicts back out
buf = io.StringIO()
writer = csv.DictWriter(buf, fieldnames=["name", "score"])
writer.writeheader()
writer.writerow({"name": "Cy", "score": 100})
print(buf.getvalue())

print("\nDone! Tip: change values above and run again to learn by experiment.")
