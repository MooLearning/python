# ======================================================================
# 26 — Datetime  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Creating and inspecting dates
# ----------------------------------------------------------------------
print("\n--- Example 1: Creating and inspecting dates ---")
from datetime import date, datetime, timedelta

today = date(2026, 6, 9)            # a fixed date so output is stable
print("today:", today)
print("year/month/day:", today.year, today.month, today.day)
print("weekday (Mon=0):", today.weekday())   # 1 -> Tuesday

now = datetime(2026, 6, 9, 14, 30, 0)
print("datetime:", now)
print("hour:minute:", now.hour, now.minute)
print("current real time exists too: datetime.now()")

# ----------------------------------------------------------------------
# Example 2: Date math with timedelta
# ----------------------------------------------------------------------
print("\n--- Example 2: Date math with timedelta ---")
from datetime import date, timedelta

start = date(2026, 1, 1)
print("a week later:", start + timedelta(days=7))     # 2026-01-08
print("30 days before:", start - timedelta(days=30))

# Difference between two dates
d1 = date(2026, 6, 9)
d2 = date(2026, 1, 1)
gap = d1 - d2
print("days between:", gap.days)     # 159

# How many days until a deadline?
deadline = date(2026, 12, 25)
print("days to deadline:", (deadline - d1).days)

# ----------------------------------------------------------------------
# Example 3: Formatting and parsing strings
# ----------------------------------------------------------------------
print("\n--- Example 3: Formatting and parsing strings ---")
from datetime import datetime

dt = datetime(2026, 6, 9, 14, 30)

# strftime: datetime -> formatted string
print(dt.strftime("%Y-%m-%d %H:%M"))     # 2026-06-09 14:30
print(dt.strftime("%A, %B %d, %Y"))      # Tuesday, June 09, 2026

# strptime: string -> datetime (you supply the format)
parsed = datetime.strptime("2026-06-09 14:30", "%Y-%m-%d %H:%M")
print(parsed.year, parsed.hour)          # 2026 14

# ISO 8601 is the safe interchange format
print(dt.isoformat())                    # 2026-06-09T14:30:00
print(datetime.fromisoformat("2026-06-09T14:30:00"))

print("\nDone! Tip: change values above and run again to learn by experiment.")
