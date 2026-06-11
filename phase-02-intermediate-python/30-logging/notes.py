# ======================================================================
# 30 — Logging  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Quick start with basicConfig
# ----------------------------------------------------------------------
print("\n--- Example 1: Quick start with basicConfig ---")
import logging

logging.basicConfig(
    level=logging.DEBUG,                                   # show DEBUG and above
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
    force=True,                                            # re-apply config
)

logging.debug("detailed info for diagnosing problems")
logging.info("things are working as expected")
logging.warning("something unexpected, but we continue")
logging.error("a serious problem occurred")
# Output goes to the console (stderr) with timestamp and level

# ----------------------------------------------------------------------
# Example 2: Levels and why print() loses
# ----------------------------------------------------------------------
print("\n--- Example 2: Levels and why print() loses ---")
import logging
logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s", force=True)

# With the threshold at WARNING, DEBUG and INFO are silently skipped...
logging.debug("you will NOT see this")
logging.info("you will NOT see this either")
logging.warning("you WILL see this")     # WARNING: ...
logging.error("and this")                # ERROR: ...

# The win: change ONE line (level=...) to get more/less detail,
# no need to delete print() statements all over your code.

# ----------------------------------------------------------------------
# Example 3: Named loggers and logging exceptions with tracebacks
# ----------------------------------------------------------------------
print("\n--- Example 3: Named loggers and logging exceptions with tracebacks ---")
import logging
logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s: %(message)s", force=True)

log = logging.getLogger("myapp")        # named logger (best practice)

def divide(a, b):
    log.info("dividing %s by %s", a, b)  # lazy %-formatting (efficient)
    try:
        return a / b
    except ZeroDivisionError:
        log.exception("division failed")  # logs ERROR + full traceback
        return None

print(divide(10, 2))   # 5.0
print(divide(1, 0))    # logs the traceback, returns None

print("\nDone! Tip: change values above and run again to learn by experiment.")
