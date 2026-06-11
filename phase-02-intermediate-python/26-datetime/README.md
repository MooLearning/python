# 26 — Datetime

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

The `datetime` module handles dates and times. Key types: `date` (year/month/day), `time` (hour/minute/second), `datetime` (both), and `timedelta` (a DURATION you can add/subtract). You convert between text and datetimes with `strftime` (format to string) and `strptime` (parse from string).

## Why it matters

Timestamps are everywhere: logs, transactions, time-series data, scheduling. Doing date math by hand is error-prone (leap years, month lengths, time zones). datetime gets it right.

## Key concepts

- **date / datetime** — Calendar date vs date+time. `datetime.now()` gives the current moment.
- **timedelta** — A span of time; add/subtract to shift dates: `today + timedelta(days=7)`.
- **strftime** — datetime -> string using format codes (%Y, %m, %d, %H, %M).
- **strptime** — string -> datetime by giving the matching format.
- **Difference** — `d2 - d1` returns a timedelta; use `.days` / `.total_seconds()`.
- **ISO format** — `.isoformat()` and `date.fromisoformat()` for the standard YYYY-MM-DD.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
from datetime import date, datetime, timedelta

today = date(2026, 6, 9)            # a fixed date so output is stable
print("today:", today)
print("year/month/day:", today.year, today.month, today.day)
print("weekday (Mon=0):", today.weekday())   # 1 -> Tuesday

now = datetime(2026, 6, 9, 14, 30, 0)
print("datetime:", now)
print("hour:minute:", now.hour, now.minute)
print("current real time exists too: datetime.now()")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ strftime/strptime format codes are case-sensitive: %M is minutes, %m is month; %y is 2-digit, %Y is 4-digit.
- ⚠️ strptime raises ValueError if the string doesn't EXACTLY match your format string.
- ⚠️ Naive datetimes have no time zone. For real apps use timezone-aware datetimes (datetime.now(timezone.utc)).
- ⚠️ You can't add an int to a date — you must add a `timedelta`.
- ⚠️ Months and years aren't fixed-length, so `timedelta(months=1)` doesn't exist; use libraries (dateutil) for that.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

