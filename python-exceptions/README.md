# Python - Exceptions & Error Handling

This project explores Python's error and exception handling mechanisms. You'll learn how to identify errors, handle exceptions gracefully, raise errors intentionally, and manage cleanup actions post-exception—all while following Python coding standards.

---

## 📚 Resources

- [Errors and Exceptions - Python Docs](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11: Static & Exception Handling (starting at minute 7)](https://www.youtube.com/watch?v=NIWwJbo-9_8)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- The difference between errors and exceptions
- What exceptions are and how to use them
- When and why to use exceptions
- How to correctly handle exceptions
- The purpose of catching exceptions
- How to raise built-in exceptions
- When to implement cleanup actions after exceptions

---

## ✅ Requirements

- **Editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 20.04 LTS
- **Python Version:** `python3` (3.8.5)
- Each script must:
  - Start with `#!/usr/bin/python3`
  - End with a new line
  - Be executable (`chmod +x`)
  - Follow `pycodestyle` (version 2.7.\*)
  - Respect line-length limits (checked with `wc`)
- A `README.md` file is **mandatory**

---

## 🧠 Tasks

### 0. Safe list printing
**File:** `0-safe_print_list.py`  
- Prints `x` elements of a list.
- Uses `try:/except:` without importing modules.
- Returns the real number of elements printed.

---

### 1. Safe printing of an integers list
**File:** `1-safe_print_integer.py`  
- Safely prints an integer using `"{}"` format.
- Returns `True` if value is an integer, else `False`.

---

### 2. Print and count integers
**File:** `2-safe_print_list_integers.py`  
- Prints only integers from the first `x` elements of a list.
- Skips non-integers silently.
- Returns number of integers printed.
- Raises error if accessing out-of-range index.

---

### 3. Integers division with debug
**File:** `3-safe_print_division.py`  
- Divides two integers.
- Prints result in a `finally` block.
- Returns the result or `None` on error.

---

### 4. Divide a list
**File:** `4-list_division.py`  
- Divides corresponding elements of two lists.
- Handles:
  - Division by zero
  - Wrong types
  - Index out of range
- Returns a new list with division results or `0` when errors occur.

---

### 5. Raise exception
**File:** `5-raise_exception.py`  
- Raises a `TypeError` using `raise`.

---

### 6. Raise a message
**File:** `6-raise_exception_msg.py`  
- Raises a `NameError` with a custom message.

---

## 🗂️ Repository Structure

```text
holbertonschool-higher_level_programming/
└── python-exceptions/
    ├── 0-safe_print_list.py
    ├── 1-safe_print_integer.py
    ├── 2-safe_print_list_integers.py
    ├── 3-safe_print_division.py
    ├── 4-list_division.py
    ├── 5-raise_exception.py
    ├── 6-raise_exception_msg.py
    ├── main test files (0-main.py, 1-main.py, ...)
    └── README.md

