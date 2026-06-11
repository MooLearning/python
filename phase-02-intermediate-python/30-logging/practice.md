# 30 — Logging: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Configure logging at INFO level and log an info message.

*Hint: basicConfig + logging.info.*

<details>
<summary>✅ Solution</summary>

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("hello logs")
```

</details>

## Exercise 2

Show that a debug message is hidden when level is WARNING.

*Hint: Set level high.*

<details>
<summary>✅ Solution</summary>

```python
import logging
logging.basicConfig(level=logging.WARNING, force=True)
logging.debug("hidden")
logging.warning("shown")
```

</details>

## Exercise 3

Create a named logger 'app' and log a warning through it.

*Hint: getLogger.*

<details>
<summary>✅ Solution</summary>

```python
import logging
logging.basicConfig(level=logging.WARNING, force=True)
log = logging.getLogger("app")
log.warning("careful")
```

</details>

## Exercise 4

Use a custom format showing only LEVEL: message.

*Hint: format=.*

<details>
<summary>✅ Solution</summary>

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", force=True)
logging.info("formatted")
```

</details>

## Exercise 5

Log an exception with traceback inside an except block.

*Hint: log.exception.*

<details>
<summary>✅ Solution</summary>

```python
import logging
logging.basicConfig(level=logging.ERROR, force=True)
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("boom")
```

</details>

## Exercise 6

Use lazy %-style arguments to log a value.

*Hint: log.info('x=%s', x).*

<details>
<summary>✅ Solution</summary>

```python
import logging
logging.basicConfig(level=logging.INFO, force=True)
x = 42
logging.info("x = %s", x)
```

</details>

## Exercise 7

List the five standard logging levels from lowest to highest.

<details>
<summary>✅ Solution</summary>

**DEBUG → INFO → WARNING → ERROR → CRITICAL.** Setting the level to one value
shows that level and everything more severe; less severe messages are dropped.

</details>

## Exercise 8

Log to a file instead of the console.

*Hint: filename= in basicConfig.*

<details>
<summary>✅ Solution</summary>

```python
import logging, os
logging.basicConfig(filename="app.log", level=logging.INFO, force=True)
logging.info("to file")
logging.shutdown()
print(os.path.exists("app.log"))  # True
os.remove("app.log")
```

</details>

