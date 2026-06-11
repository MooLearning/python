# ======================================================================
# 110 — Git and Version Control  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: The core Git workflow (commands)
# ----------------------------------------------------------------------
print("\n--- Example 1: The core Git workflow (commands) ---")
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

# ----------------------------------------------------------------------
# Example 2: Branching and merging
# ----------------------------------------------------------------------
print("\n--- Example 2: Branching and merging ---")
branching = [
    ("git branch", "List branches"),
    ("git checkout -b feature", "Create AND switch to a new branch"),
    ("git switch main", "Switch back to main"),
    ("git merge feature", "Merge 'feature' into the current branch"),
    ("git branch -d feature", "Delete a merged branch"),
]
for cmd, desc in branching:
    print(f"{cmd:26} # {desc}")

print("\nTypical feature workflow:")
for step in ["git checkout -b add-model", "  ...edit & commit...",
             "git push -u origin add-model", "open a Pull Request -> review -> merge"]:
    print("  " + step)

# ----------------------------------------------------------------------
# Example 3: A .gitignore for ML projects, and checking git
# ----------------------------------------------------------------------
print("\n--- Example 3: A .gitignore for ML projects, and checking git ---")
import subprocess

gitignore = """\
__pycache__/
*.pyc
.venv/
venv/
.env                 # secrets
data/                # large datasets (use DVC/cloud storage)
*.csv
models/*.pkl         # large model binaries
.ipynb_checkpoints/
"""
print(".gitignore for an ML project:")
print(gitignore)

try:
    version = subprocess.run(["git", "--version"],
                             capture_output=True, text=True, timeout=5)
    print("git available:", version.stdout.strip() or "yes")
except (FileNotFoundError, subprocess.SubprocessError):
    print("git not found — install it from https://git-scm.com")

print("\nDone! Tip: change values above and run again to learn by experiment.")
