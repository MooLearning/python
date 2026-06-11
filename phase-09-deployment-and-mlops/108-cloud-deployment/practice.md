# 108 — Cloud Deployment: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Read an env var PORT with default 8000.

*Hint: os.environ.get.*

<details>
<summary>✅ Solution</summary>

```python
import os
print(int(os.environ.get("PORT", "8000")))  # 8000 if unset
```

</details>

## Exercise 2

Which option scales to zero between requests?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Serverless** (Lambda / Cloud Functions) — it runs only per request and scales
down to **zero** instances when idle (you pay per invocation).

</details>

## Exercise 3

Where should secrets like API keys come from?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Environment variables or a secrets manager** — never hard-coded in source or
baked into the image.

</details>

## Exercise 4

Why log to stdout in the cloud?

*Hint: Collection.*

<details>
<summary>✅ Solution</summary>

Cloud platforms automatically **collect stdout/stderr** into their logging systems.
Writing to local files inside an ephemeral container loses the logs.

</details>

## Exercise 5

What does a health-check endpoint do?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

It lets the platform/load balancer **check if the service is ready** to receive
traffic (returns 200 when healthy), and restart/replace it if not.

</details>

## Exercise 6

A serverless downside for big models?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Cold starts** (and size/time limits) — loading a large model on a fresh instance
adds latency, and serverless caps memory/runtime.

</details>

## Exercise 7

Build a config dict from env with default LOG_LEVEL=INFO.

*Hint: get default.*

<details>
<summary>✅ Solution</summary>

```python
import os
print(os.environ.get("LOG_LEVEL", "INFO"))  # INFO
```

</details>

## Exercise 8

Name the control trade-off: VM vs serverless.

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**VM = maximum control** but you manage OS/scaling/patching. **Serverless = minimal
ops** but least control (limits, cold starts). Containers sit in between.

</details>

