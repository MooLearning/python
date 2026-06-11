# ======================================================================
# 107 — Docker Basics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A Dockerfile for a Python ML service (template)
# ----------------------------------------------------------------------
print("\n--- Example 1: A Dockerfile for a Python ML service (template) ---")
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

# ----------------------------------------------------------------------
# Example 2: Common Docker commands
# ----------------------------------------------------------------------
print("\n--- Example 2: Common Docker commands ---")
commands = [
    ("docker build -t name:tag .", "Build an image from the Dockerfile here"),
    ("docker run -p 8000:8000 name", "Run a container, mapping host:container ports"),
    ("docker run -d name", "Run detached (in the background)"),
    ("docker ps", "List running containers"),
    ("docker images", "List local images"),
    ("docker logs <id>", "View a container's logs"),
    ("docker exec -it <id> bash", "Open a shell inside a running container"),
    ("docker stop <id>", "Stop a running container"),
    ("docker push name:tag", "Upload an image to a registry"),
]
for cmd, desc in commands:
    print(f"{cmd:34} # {desc}")

# ----------------------------------------------------------------------
# Example 3: Layer caching and .dockerignore
# ----------------------------------------------------------------------
print("\n--- Example 3: Layer caching and .dockerignore ---")
# Why copy requirements.txt before the code:
print("Layer caching tip:")
print("  COPY requirements.txt + RUN pip install   <- cached unless deps change")
print("  COPY . .                                  <- re-runs when code changes")
print("  => dependencies aren't reinstalled on every code edit.\n")

dockerignore = """\
__pycache__/
*.pyc
.venv/
venv/
data/
*.csv
.git/
.env
"""
print(".dockerignore (keep the image small & secrets out):")
print(dockerignore)

print("\nDone! Tip: change values above and run again to learn by experiment.")
