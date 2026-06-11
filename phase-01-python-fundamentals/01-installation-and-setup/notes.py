# ======================================================================
# 01 — Installation and Setup  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Inspect your Python installation
# ----------------------------------------------------------------------
print("\n--- Example 1: Inspect your Python installation ---")
import sys       # info about the Python interpreter
import platform  # info about your operating system

# sys.version is a string describing the running interpreter
print("Python version:", sys.version.split()[0])

# Where is the python executable that is running this file?
print("Interpreter path:", sys.executable)

# What OS are you on?
print("Operating system:", platform.system(), platform.release())

# ----------------------------------------------------------------------
# Example 2: Your first script
# ----------------------------------------------------------------------
print("\n--- Example 2: Your first script ---")
# Save this in a file called hello.py and run: python hello.py
name = "learner"
print("Hello,", name + "!")
print("You just ran a Python script.")

# ----------------------------------------------------------------------
# Example 3: Confirm a standard-library module loads
# ----------------------------------------------------------------------
print("\n--- Example 3: Confirm a standard-library module loads ---")
import math        # math ships WITH Python (no pip needed)
import statistics  # another standard-library module

# Some stdlib modules are written in Python and live in a file on disk:
print("statistics module file:", statistics.__file__)
# math is built INTO the interpreter (written in C), so it has no __file__:
print("math is built-in (no file)?", not hasattr(math, "__file__"))
print("Square root of 144 is:", math.sqrt(144))
# Third-party packages (like numpy) would need: pip install numpy

print("\nDone! Tip: change values above and run again to learn by experiment.")
