# Python - Import & Modules

This project focuses on understanding how Python modules and imports work. You'll learn how to structure Python scripts, import functionality across files, handle command-line arguments, and follow style guidelines using `pycodestyle`.

---

## 📚 Resources

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/library/sys.html#sys.argv)
- [Pycodestyle – Style Guide for Python Code](https://pycodestyle.pycqa.org/en/latest/)
- `man` or `--help`:
  - `python3`

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

---

## ✅ Requirements

- **Editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 22.04 LTS
- **Python Version:** `python3` (3.10.\*)
- Each file must:
  - End with a new line
  - Start with `#!/usr/bin/python3`
  - Be executable (`chmod +x filename.py`)
  - Conform to `pycodestyle` (v2.7.\*)
  - Not exceed a specific line count (checked with `wc`)
- A `README.md` file is **mandatory**

---

## 🧠 Tasks

### 0. Import a simple function from a simple file
**File:** `0-add.py`  
- Import `add(a, b)` from `add_0.py`
- Print `1 + 2 = 3` using formatted string
- Use variables `a = 1`, `b = 2`
- Must not execute code when imported

---

### 1. My first toolbox!
**File:** `1-calculation.py`  
- Import functions from `calculator_1.py`: `add`, `sub`, `mul`, `div`
- Use `a = 10`, `b = 5`
- Perform all four operations and print each result
- Only one import of `calculator_1` allowed

---

### 2. How to make a script dynamic!
**File:** `2-args.py`  
- Print the number of arguments and list them
- Format:
  - `0 arguments.` if none
  - `1 argument:` with listing
  - `N arguments:` with listing
- Use `sys.argv`

---

### 3. Infinite addition
**File:** `3-infinite_add.py`  
- Sum all arguments provided to the script
- Print the total sum
- Arguments are assumed to be integers

---

### 4. Who are you?
**File:** `/tmp/4-hidden_discovery.py`  
- Load the compiled module `hidden_4.pyc`
- Print all names not starting with `__` in alphabetical order
- **Run in sandbox only**

---

### 5. Everything can be imported
**File:** `5-variable_load.py`  
- Import variable `a` from `variable_load_5.py`
- Print its value
- Do not use `*` or `__import__`

---

## 🗂️ Repository Structure

```text
holbertonschool-higher_level_programming/
└── python-import_modules/
    ├── 0-add.py
    ├── 1-calculation.py
    ├── 2-args.py
    ├── 3-infinite_add.py
    ├── 4-hidden_discovery.py
    ├── 5-variable_load.py
    └── README.md


