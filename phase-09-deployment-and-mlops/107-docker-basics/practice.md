# 107 — Docker Basics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

What's the difference between an image and a container?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

An **image** is a static, read-only template; a **container** is a **running
instance** of that image (you can run many containers from one image).

</details>

## Exercise 2

Which Dockerfile instruction sets the startup command?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**CMD** (or ENTRYPOINT) — it defines the process that runs when the container
starts.

</details>

## Exercise 3

Why copy requirements.txt before the app code?

*Hint: Caching.*

<details>
<summary>✅ Solution</summary>

So the dependency-install layer is **cached** and reused; it only re-runs when
requirements change, not on every code edit — much faster rebuilds.

</details>

## Exercise 4

Map host port 5000 to container port 8000: which flag?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**`-p 5000:8000`** (host:container) on `docker run` — host port 5000 forwards to
the container's 8000.

</details>

## Exercise 5

What address should a containerized server bind to?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**0.0.0.0** (all interfaces) — binding to 127.0.0.1 makes it reachable only inside
the container, not from the host.

</details>

## Exercise 6

Name one thing to put in .dockerignore.

*Hint: Any valid.*

<details>
<summary>✅ Solution</summary>

Things like **.venv/, __pycache__/, data/, .git/, .env** — they bloat the image
and may leak secrets; excluding them keeps builds small and safe.

</details>

## Exercise 7

Why pin a base image tag instead of 'latest'?

*Hint: Reproducibility.*

<details>
<summary>✅ Solution</summary>

'latest' changes over time, so builds aren't **reproducible**. Pinning (e.g.
python:3.11-slim) guarantees the same base every build.

</details>

## Exercise 8

Which command lists running containers?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**`docker ps`** (add `-a` to also show stopped containers).

</details>

