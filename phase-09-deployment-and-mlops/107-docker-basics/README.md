# 107 — Docker Basics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Docker** packages your app and ALL its dependencies into a **container** — a lightweight, isolated, reproducible unit that runs identically anywhere. A **Dockerfile** is the recipe (base image, copy code, install deps, run command); building it produces an **image**; running the image creates a **container**. This solves 'works on my machine' and is the standard way to ship ML services.

## Why it matters

Containers guarantee the same environment in dev, test, and production — crucial for ML where library versions matter. They're the unit of deployment for cloud, Kubernetes, and CI/CD pipelines.

## Key concepts

- **Image** — A read-only template (base + your app + deps).
- **Container** — A running instance of an image.
- **Dockerfile** — The build recipe, one instruction per layer.
- **Layers** — Each instruction caches a layer; order them for cache reuse.
- **Ports & volumes** — Expose ports and mount data into the container.
- **.dockerignore** — Exclude files (venv, data) from the build context.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
dockerfile = """\
# Start from a small official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies FIRST (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Document the port the app listens on
EXPOSE 8000

# Command to run when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""
print(dockerfile)
print("Build:  docker build -t my-model-api .")
print("Run  :  docker run -p 8000:8000 my-model-api")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Bind to 0.0.0.0 inside the container, not 127.0.0.1, or it's unreachable from the host.
- ⚠️ Copy requirements.txt and install BEFORE copying code, so deps stay cached across edits.
- ⚠️ Use slim/specific base tags (python:3.11-slim), not 'latest' — reproducibility.
- ⚠️ Never bake secrets into the image — pass them as env vars/secrets at runtime.
- ⚠️ Add a .dockerignore (venv, data, .git) or images balloon and may leak files.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

