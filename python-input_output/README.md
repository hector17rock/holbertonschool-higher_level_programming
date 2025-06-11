# Python - Input/Output

## Overview

This project focuses on Python’s file handling and JSON serialization. You'll explore how to read, write, and append to files, convert Python data structures to and from JSON format, serialize and deserialize objects, and parse structured logs.

By the end, you'll also gain experience working with classes that can serialize their data to disk and load it back, as well as parsing text logs using standard input.

---

## Learning Objectives

At the end of this project, you should be able to explain, without the help of Google:

### General

- Why Python programming is awesome
- How to:
  - Open a file
  - Write text to a file
  - Read file contents fully or line-by-line
  - Move the cursor in a file
  - Ensure files are closed properly after usage
- What is the `with` statement and why it’s useful
- What is JSON
- Concepts of serialization and deserialization
- How to:
  - Convert Python data structures to JSON strings
  - Convert JSON strings back to Python data structures
- How to handle command-line arguments in a Python script

---

## Resources

You are encouraged to read or watch the following (in order):

- [7.2. Reading and Writing Files (Python Docs)](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions (Python Docs)](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3 - Chapter 11: Files](https://diveintopython3.problemsolving.io/files.html) _(up to 11.4 Binary Files)_
- [JSON Encoder and Decoder (Python Docs)](https://docs.python.org/3/library/json.html)
- [Learn to Program 8: Reading / Writing Files (Video)](https://www.youtube.com/watch?v=Uh2ebFW8OYM)
- [Automate the Boring Stuff with Python (Chapter 8 & 14)](https://automatetheboringstuff.com/)
- [`sys` Module (Python Docs)](https://docs.python.org/3/library/sys.html)

---

## Project Structure




---

## Requirements

- **Python version:** 3.8.5 (Ubuntu 20.04 LTS)
- **Editor:** `vi`, `vim`, `emacs`
- Files must:
  - Start with `#!/usr/bin/python3`
  - End with a new line
  - Be executable
  - Follow `pycodestyle` (2.7.*)
- Each module, class, and function must have proper documentation
- Test files must be in `tests/` folder and use `.txt` extension

---

## Tasks Summary

### 0. Read file
Reads and prints a UTF-8 text file using `with`.

### 1. Write to a file
Writes a string to a UTF-8 text file (overwrites if exists).

### 2. Append to a file
Appends a string at the end of a file, creates it if it doesn't exist.

### 3. To JSON string
Converts a Python object to a JSON string.

### 4. From JSON string to Object
Converts a JSON string to a Python data structure.

### 5. Save Object to a file
Saves a Python object to a file using JSON format.

### 6. Create object from a JSON file
Loads a Python object from a JSON file.

### 7. Load, add, save
Adds command-line arguments to a list, and saves it to `add_item.json`.

### 8. Class to JSON
Returns a dictionary description suitable for JSON serialization.

### 9. Student to JSON
Defines a `Student` class with a method to serialize its attributes.

### 10. Student to JSON with filter
Adds attribute filtering to the `to_json()` method of the `Student` class.

### 11. Student to disk and reload
Adds `reload_from_json()` to restore a `Student` object from saved data.

### 12. Pascal's Triangle
Generates Pascal’s Triangle as a list of lists for a given number of rows.

### 13. Search and update (Advanced)
Inserts text into a file after each line containing a specific string.

### 14. Log parsing (Advanced)
Reads log entries from `stdin`, computes stats (status code count and total file size), and prints stats every 10 lines or upon interruption.

---

## Author

Project developed as part of the **Holberton School** Software Engineering curriculum.



