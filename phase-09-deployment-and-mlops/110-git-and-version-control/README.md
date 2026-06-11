# 110 — Git and Version Control

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Git** is a distributed **version control** system that tracks every change to your code, lets you **branch** to work in isolation, **merge** work together, and collaborate via remotes (GitHub/GitLab). The core loop: edit files → **stage** (`git add`) → **commit** (`git commit`) a snapshot → **push** to a remote. Branches enable parallel work and pull requests enable review.

## Why it matters

Git is non-negotiable in software and ML: it's your undo history, collaboration backbone, and the basis of CI/CD. Versioning code (and, with tools like DVC, data/models) makes work reproducible and team-friendly.

## Key concepts

- **Repository** — A project tracked by Git (its full history).
- **Stage & commit** — git add selects changes; git commit snapshots them.
- **Branch** — An independent line of work; merge it back when ready.
- **Remote** — A hosted copy (origin) you push to / pull from.
- **Merge / pull request** — Combine branches; PRs add review.
- **.gitignore** — Patterns of files Git should not track.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
workflow = [
    ("git init", "Start tracking a new project"),
    ("git clone <url>", "Copy an existing remote repo"),
    ("git status", "See what's changed / staged"),
    ("git add file.py", "Stage a change for the next commit"),
    ("git add .", "Stage ALL changes"),
    ("git commit -m 'msg'", "Snapshot staged changes with a message"),
    ("git push", "Upload commits to the remote"),
    ("git pull", "Download + merge remote changes"),
    ("git log --oneline", "View commit history compactly"),
]
for cmd, desc in workflow:
    print(f"{cmd:22} # {desc}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Don't commit secrets (.env, keys) or large data/models — add them to .gitignore.
- ⚠️ Write clear, present-tense commit messages ('Add X', not 'added stuff').
- ⚠️ Commit small and often; giant commits are hard to review and revert.
- ⚠️ `git push --force` can overwrite teammates' work — avoid it on shared branches.
- ⚠️ Pull/merge frequently to avoid painful conflicts from long-lived branches.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

