# ======================================================================
# 17 — Virtual Environments  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Detect whether you're in a virtual environment (runnable)
# ----------------------------------------------------------------------
print("\n--- Example 1: Detect whether you're in a virtual environment (runnable) ---")
import sys
import os

# When a venv is active, sys.prefix differs from sys.base_prefix
in_venv = sys.prefix != sys.base_prefix
print("Running inside a virtual environment?", in_venv)
print("Environment path (sys.prefix):", sys.prefix)

# The VIRTUAL_ENV env var is set by activation scripts
print("VIRTUAL_ENV =", os.environ.get("VIRTUAL_ENV", "(not set)"))

# ----------------------------------------------------------------------
# Example 2: The typical workflow (these are shell commands, shown as text)
# ----------------------------------------------------------------------
print("\n--- Example 2: The typical workflow (these are shell commands, shown as text) ---")
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

# ----------------------------------------------------------------------
# Example 3: Inspect installed packages from Python
# ----------------------------------------------------------------------
print("\n--- Example 3: Inspect installed packages from Python ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")
