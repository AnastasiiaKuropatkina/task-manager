# Task manager

The simple CLI task manager. Users should be able to add/remove tasks, mark tasks as Done and before exiting there should be a possibility to **save tasks to Excel spreadsheet**.

## Steps

Let's decompose the task into the following phases:

### Phase 1: Project setup

1. Create repository and set up environment.
2. POC: dummy CLI app.
3. Project structure

### Phase 2: Develop logic

Write code to handle app logic:
   1. Storage
   2. CLI interface
   3. How do we export tasks to excel?

### Phase 3: Maintainance

Tests (covered in later sections of the course)
Code style
   1. [mypy](https://pypi.org/project/mypy/)
   2. [flake8](https://pypi.org/project/flake8/)
Add README
Upload repository to Github

## Init

```bash
git init
python3 -m venv .venv
./.venv/bin/activate
```
Install openpyxl - the Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
```bash
pip install openpyxl
```
or
```bash
pip install -r requirements.txt
```

