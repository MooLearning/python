#!/usr/bin/env python3
"""Progress checker: a topic counts as 'done' when it contains a my_solution.py file.

Run from the python/ folder:   python3 progress.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
total = done = 0
done_list, todo_list = [], []

for entry in sorted(os.listdir(HERE)):
    if not entry.startswith("phase-"):
        continue
    phase = os.path.join(HERE, entry)
    if not os.path.isdir(phase):
        continue
    for topic in sorted(os.listdir(phase)):
        tdir = os.path.join(phase, topic)
        if not os.path.isdir(tdir):
            continue
        total += 1
        rel = os.path.join(entry, topic)
        if os.path.exists(os.path.join(tdir, "my_solution.py")):
            done += 1
            done_list.append(rel)
        else:
            todo_list.append(rel)

print(f"Progress: {done}/{total} topics with my_solution.py")
if todo_list:
    print("\nNext up (first 5):")
    for t in todo_list[:5]:
        print(f"  [ ] {t}")
if done_list:
    print(f"\nDone ({len(done_list)}):")
    for t in done_list[-10:]:
        print(f"  [x] {t}")
