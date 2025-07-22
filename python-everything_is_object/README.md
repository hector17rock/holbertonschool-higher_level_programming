# Python: Everything is Object

This project explores various concepts in Python, focusing particularly on objects and their properties, such as mutability and immutability. Understanding these concepts is crucial for efficient memory management and effective programming in Python.

## Table of Contents
- Introduction
- Files and Descriptions
- Concepts Explained
- Author

## Introduction
In this project, we dive into Python's approach to handling objects, understanding the distinction between mutable and immutable types, and learning how these affect performance and functionality.

## Files and Descriptions

- `0-answer.txt` to `28-answer.txt`: These files contain responses to various exercises that help in understanding Python's object handling.
  
- `19-copy_list.py`: A Python script containing a function `copy_list(a_list)` that returns a copy of the input list. It utilizes slicing to create a shallow copy.

- `19-main.py`: A test script to demonstrate the functionality of the `copy_list` function, ensuring that the list is copied correctly.

## Concepts Explained

### Mutable vs Immutable
- **Mutable Objects**: Objects that can be changed after creation, such as lists, dicts, and sets.
- **Immutable Objects**: Objects that cannot be changed after creation, such as strings, tuples, and numbers.

### Why It Matters
Understanding the distinction is vital for memory optimization and avoiding unintended side effects in your programs.

### Function Arguments
Objects are passed by reference in Python. For mutable objects, changes within a function affect the original object, while for immutable objects, changes do not affect the original.

## Author
This project was developed by Hector. The findings here reflect an exploration into understanding Python's object behavior deeply to better write efficient and error-free programs.
