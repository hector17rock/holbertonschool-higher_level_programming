# Python - More Classes and Objects

This project builds upon foundational Python knowledge to explore advanced **Object-Oriented Programming (OOP)** concepts, focusing on class construction, special methods, class vs instance attributes, encapsulation, and Pythonic conventions.

---

## 📚 Resources

### Read or Watch:
- [Object Oriented Programming in Python (read up to “Inheritance” excluded)](https://docs.python.org/3/tutorial/classes.html)
- [Object-Oriented Programming Concepts](https://python-course.eu/oop/object-oriented-programming.php) (Only: *General Introduction*, *First-class Everything*, *A Minimal Class in Python*, *Attributes*, *Methods*, *__init__*, *Data Abstraction, Encapsulation, and Hiding*, *__str__ and __repr__*, *Attribute Protection*, *Destructor*)
- [Class and Instance Attributes](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [classmethod and staticmethod](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Properties vs Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (focus on *Public instead of Private Attributes*)
- [str vs repr](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following without using Google:

### General:
- Why Python programming is awesome
- What is Object-Oriented Programming (OOP)
- The idea behind "first-class everything"
- What are classes and instances
- Difference between class and instance
- What is an attribute (object/class)
- Public, protected, and private attributes
- What is `self` and why it’s needed
- What is a method and the `__init__` constructor
- Principles: Abstraction, Encapsulation, and Information Hiding
- What is a property and how it's different from an attribute
- Pythonic way of creating getters/setters using `@property`
- Difference between `__str__` and `__repr__`
- What is a class attribute vs instance attribute
- What are `@classmethod` and `@staticmethod`
- Dynamically adding attributes to instances
- How `__dict__` is used to store object attributes
- How Python looks up attributes (`__getattr__`)
- How to use the built-in `getattr()` function

---

## ✅ Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled using `python3` (version 3.8.5)
- Each file must end with a new line
- First line of each script: `#!/usr/bin/python3`
- A `README.md` file at the project root is **mandatory**
- Code must follow `pycodestyle` (version 2.7.*)
- All scripts must be executable
- File length will be tested with `wc`

---

## 🧠 Tasks Overview

### `0-rectangle.py`
- Defines an empty class `Rectangle`

### `1-rectangle.py`
- Adds private attributes `width` and `height` with proper validation and property setters/getters

### `2-rectangle.py`
- Adds `area()` and `perimeter()` instance methods

### `3-rectangle.py`
- Adds `__str__()` method to print the rectangle using `#`

### `4-rectangle.py`
- Adds `__repr__()` to recreate a new object using `eval()`

### `5-rectangle.py`
- Adds a destructor method `__del__()` that prints a message when the instance is deleted

### `6-rectangle.py`
- Adds a public class attribute `number_of_instances` that tracks how many instances exist

### `7-rectangle.py`
- Adds a class attribute `print_symbol` for string representation

### `8-rectangle.py`
- Adds static method `bigger_or_equal(rect_1, rect_2)` to compare rectangles by area

### `9-rectangle.py`
- Adds class method `square(cls, size=0)` that returns a square instance

---

## 💡 Additional Notes

- All methods handle edge cases (e.g., `0` dimensions) gracefully.
- Properties and `@property` decorators are used extensively for attribute validation.
- Avoids module imports unless explicitly allowed.
- Encourages good OOP design: encapsulation, abstraction, and reusability.

---

## 🗃 Repository Info

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Project directory:** `python-more_classes`

---

## 🏁 Author

Project developed as part of the Holberton School curriculum.

