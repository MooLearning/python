# 110 — Git and Version Control: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Which command stages all changes?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**`git add .`** stages every modified/new file in the current directory tree for the
next commit.

</details>

## Exercise 2

Create and switch to a branch 'dev' in one command.

*Hint: checkout -b.*

<details>
<summary>✅ Solution</summary>

**`git checkout -b dev`** (or the newer `git switch -c dev`).

</details>

## Exercise 3

What does git commit do?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

Records a **snapshot** of the currently **staged** changes into the repository
history, with a message describing them.

</details>

## Exercise 4

Name two things to put in .gitignore for ML.

*Hint: Any valid.*

<details>
<summary>✅ Solution</summary>

For example **.env (secrets)** and **data/ or *.pkl (large datasets/models)** —
plus __pycache__/, .venv/, .ipynb_checkpoints/.

</details>

## Exercise 5

What's the command to upload commits to the remote?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**`git push`** — sends your local commits to the remote (e.g. origin/GitHub).

</details>

## Exercise 6

Why avoid git push --force on shared branches?

*Hint: Overwrites.*

<details>
<summary>✅ Solution</summary>

It can **overwrite/rewrite history** that teammates already based work on, causing
lost commits and conflicts. Use it only on your own private branches.

</details>

## Exercise 7

Combine branch 'feature' into the current branch.

*Hint: merge.*

<details>
<summary>✅ Solution</summary>

**`git merge feature`** — integrates the commits from `feature` into the branch
you currently have checked out.

</details>

## Exercise 8

Write a good commit message style for adding a function.

*Hint: Imperative.*

<details>
<summary>✅ Solution</summary>

Imperative, present tense and specific — e.g. **"Add predict() endpoint to API"**,
not "added stuff" or "fixes".

</details>

