# Python - Classes and Objects

## Description

This project introduces **Object-Oriented Programming (OOP)** in Python by progressively developing a `Square` class. You’ll learn to encapsulate data and behaviors into class structures, use properties, and control access to internal attributes. The tasks focus on understanding attributes, methods, validation, and Pythonic encapsulation using properties.

---

## Learning Objectives

By the end of this project, you will be able to explain, without the help of Google:

### General OOP Concepts
- What is OOP
- What does “first-class everything” mean in Python
- What is a class, and how to define one
- What is an object/instance and the difference from a class
- What are attributes, and how to define/use them
- What are public, protected, and private attributes
- What is `self` and how it works
- What is a method and the purpose of the `__init__` method
- What is:
  - Data Abstraction
  - Data Encapsulation
  - Information Hiding
- What is a property
- Difference between an attribute and a property
- Pythonic way to implement getters and setters
- How to dynamically create new attributes
- How to bind attributes to objects and classes
- What is `__dict__` and what it contains
- How Python finds an attribute
- How to use `getattr()`

---

## Requirements

- **Python version**: 3.8.5
- **OS**: Ubuntu 20.04 LTS
- **Editor**: `vi`, `vim`, or `emacs`
- **Shebang**: All files must start with `#!/usr/bin/python3`
- **Style**: `pycodestyle` 2.7.*
- All files must be **executable**
- All files must end with a **new line**
- All modules, classes, and functions must be documented using **Google-style docstrings**

---

## Resources

You must **read/watch** and **type** the examples (not copy-paste). Explore and experiment:

- [Object Oriented Programming](https://docs.python.org/3/tutorial/classes.html) – Until *Inheritance* (excluded)
- [Object-Oriented Programming Concepts](https://realpython.com/python3-object-oriented-programming/) – Read carefully, especially the correct/incorrect code examples
- [Properties vs Getters and Setters](https://pythonguides.com/python-getters-and-setters/)
- [Learn to Program 9: OOP](https://www.youtube.com/watch?v=1AGyBuVCTeE)
- [Python Classes and Objects (W3Schools)](https://www.w3schools.com/python/python_classes.asp)
- [Object-Oriented Programming (Programiz)](https://www.programiz.com/python-programming/object-oriented-programming)

---

## Tasks Summary

### 0. My First Square
- Define an empty class `Square`.

### 1. Square with Size
- Add a **private instance attribute** `__size`.
- Initialize `size` without validation.

### 2. Size Validation
- Add **type and value checks** for `size`:
  - Must be an `int`, else `TypeError`
  - Must be `>= 0`, else `ValueError`

### 3. Area of a Square
- Add `area(self)` method to return the area.

### 4. Access and Update Size
- Add property:
  - `size(self)` (getter)
  - `size(self, value)` (setter with validation)

### 5. Printing a Square
- Add `my_print(self)` method to print the square using `#`.
- If `size` is

