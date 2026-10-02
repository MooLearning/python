# 🐍 START HERE — Learn Python by Doing

This folder is already built for exactly the style you asked for:
**short doc → 2–3 runnable examples → you write code.**

Every one of the **114 topics** follows the same 3-file loop:

| Step | File | What you do |
|------|------|-------------|
| 1. Read | `README.md` | Short, moderate doc: what it is, why it matters, key ideas, 1 example, gotchas (5 min) |
| 2. Run & tinker | `notes.py` | 3 heavily-commented runnable examples. Run, then **change values and re-run** |
| 3. Do | `practice.md` | 8 exercises (easy → hard). **Type your answer in `my_solution.py` first**, then expand the hidden solution |

## The loop (do this for every topic)

```bash
# Example: lists, tuples, sets, dicts (Topic 08)
cd phase-01-python-fundamentals/08-lists-tuples-sets-dictionaries/

cat README.md        # 1. read (short doc)
python3 notes.py     # 2. run the 3 examples
cp ../../my_solution_template.py my_solution.py  # 3. your workspace (once per topic)
# open practice.md, solve Exercise 1 in my_solution.py, run it:
python3 my_solution.py
```

> Rule: **never open the ✅ Solution before running your own code.** Predicting → running → fixing is where learning happens.

## Where to start (AI / Python career path)

1. **Phase 1–2 (Topics 01–30)** — mandatory. Python fundamentals + intermediate. Don't skip.
2. **Phase 3 (Topics 31–56)** — DSA. Do in parallel with the next line once Phase 1 is done. Needed for interviews.
3. **Phases 4–6 (Topics 57–89)** — Math + NumPy/pandas + ML. This is the AI-career core. NumPy (61) and pandas (62) are the two libraries you named — start there after Phase 2.
4. **Phases 7–9 (Topics 90–110)** — Deep learning + deployment. Only after ML basics.
5. **Phase 10 (Topics 111–114)** — projects + portfolio. Start early, even a tiny Kaggle notebook counts.

Check your progress anytime:

```bash
python3 ../../progress.py          # from any topic folder, or:
python3 progress.py                # from the python/ folder
```

## Worked example: lists (Topic 08)

1. Read: `phase-01-python-fundamentals/08-lists-tuples-sets-dictionaries/README.md`
   — 5-min doc on list vs tuple vs set vs dict.
2. Run: `python3 notes.py` — you will see 3 examples (lists / tuples+sets / dicts).
3. Do: open `practice.md`, Exercise 3 says *"Remove duplicates from [1,2,2,3,3,3]"*.
   Write in `my_solution.py`:
   ```python
   data = [1, 2, 2, 3, 3, 3]
   print(len(set(data)))  # your guess before running?
   ```
   Run it, then compare with the hidden solution.

## Files in this folder

- `README.md` — full 114-topic roadmap with checkboxes.
- `START_HERE.md` — this file.
- `my_solution_template.py` — copy into any topic as `my_solution.py` and write your answers there.
- `progress.py` — prints what's done (a topic counts as done when it has a `my_solution.py`).
- `phase-*/NN-topic/{README.md, notes.py, practice.md}` — the 114 lessons (343 files, all verified runnable).
- `_build/` — generator scripts (`c01.py`…`c10.py` + `build.py`). Don't edit lessons by hand; edit `_build/cXX.py` and re-run `python3 _build/build.py`.

## Requirements

- Phases 1–3: Python 3.10+, standard library only — everything runs with `python3 notes.py`.
- Phase 4+: `pip install numpy pandas matplotlib seaborn scikit-learn requests flask fastapi uvicorn streamlit`
  (each topic README also lists its own `pip install` line).
