# 17 — Virtual Environments: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write code that prints whether the current Python is inside a virtual environment.

*Hint: Compare sys.prefix and sys.base_prefix.*

<details>
<summary>✅ Solution</summary>

```python
import sys
print(sys.prefix != sys.base_prefix)
```

</details>

## Exercise 2

List the shell commands to create and activate a venv on Linux.

<details>
<summary>✅ Solution</summary>

```bash
python -m venv .venv
source .venv/bin/activate
```

</details>

## Exercise 3

What command records your installed packages to requirements.txt?

<details>
<summary>✅ Solution</summary>

```bash
pip freeze > requirements.txt
```

</details>

## Exercise 4

What single command reinstalls everything listed in requirements.txt?

<details>
<summary>✅ Solution</summary>

```bash
pip install -r requirements.txt
```

</details>

## Exercise 5

Print the value of the VIRTUAL_ENV environment variable (or a default).

*Hint: os.environ.get.*

<details>
<summary>✅ Solution</summary>

```python
import os
print(os.environ.get("VIRTUAL_ENV", "no venv active"))
```

</details>

## Exercise 6

Why should .venv/ be in .gitignore?

<details>
<summary>✅ Solution</summary>

The environment is large, machine-specific, and fully reproducible from
`requirements.txt`. Committing it bloats the repo and breaks on other OSes.
Commit the requirements file, not the environment.

</details>

## Exercise 7

Print the Python executable path so you can confirm which environment is active.

*Hint: sys.executable.*

<details>
<summary>✅ Solution</summary>

```python
import sys
print(sys.executable)
```

</details>

## Exercise 8

Name the activation command on Windows PowerShell.

<details>
<summary>✅ Solution</summary>

```powershell
.venv\Scripts\Activate.ps1
```

</details>

