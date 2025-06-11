# Python - Test-driven development

This project introduces the principles and practice of **Test-Driven Development (TDD)** in Python. You'll learn how to write documentation and tests first, develop against those tests, and validate your code with both interactive and unit testing strategies.

---

## 📝 Important Notice on Intranet Checks

- From now on, **tests and documentation must be written before implementation**.
- Intranet checks **will not be released before the first deadline**—focus on TDD!
- Collaborate on test cases (not code implementation) to catch all edge cases.
- **Never trust user input**—always think about how your function could break.

---

## 📚 Resources

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://realpython.com/python-testing/)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome  
- What interactive tests are  
- Why testing is essential  
- How to write **docstrings** to generate `doctest`-based tests  
- How to document modules and functions properly  
- How to use `doctest` options and flags  
- How to identify and cover **edge cases**

---

## ✅ Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- OS: Ubuntu 20.04 LTS
- Python version: 3.8.5
- All scripts must:
  - Start with `#!/usr/bin/python3`
  - End with a new line
  - Be executable (`chmod +x`)
  - Pass `pycodestyle` (v2.7.\*)
  - Respect line-length limits (`wc` will check)

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- Test files must:
  - Be inside the `tests/` folder
  - Use `.txt` for `doctest` or `.py` for `unittest`
  - Be executable via:
    - `python3 -m doctest ./tests/*`
    - `python3 -m unittest tests.6-max_integer_test`

- **All modules and functions must have docstrings**:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  python3 -c 'print(__import__("my_module").my_function.__doc__)'

