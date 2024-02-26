# Task manager

## Projecto description:

We will create a simple CLI task manager. Users should be able to add/remove tasks, mark tasks as Done and before exiting there should be a possibility to **save tasks to Excel spreadsheet**.

## Steps

Let's decompose the task into the following phases:

Phase 1: Project setup

1. Create repository and set up environment.
2. POC: dummy CLI app.
3. Project structure

Phase 2: Develop logic

4. Write code to handle app logic
   1. Storage
   2. CLI interface
   3. How do we export tasks to excel?

Phase 3: Maintainance

5. Tests (covered in later sections of the course)
6. Code style
   1. [mypy](https://pypi.org/project/mypy/)
   2. [flake8](https://pypi.org/project/flake8/)
7. Add README
8. Upload repository to Github

## Init
активація invertment<br>
``
git init
python3 -m venv .venv
./.venv/bin/activate
``

``
pip install openpyxl
pip install -r requirements.txt
``

