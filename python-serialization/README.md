# Python - Serialization

## 📌 Introduction

This project introduces key data transformation concepts in Python: **marshaling** and **serialization**. These mechanisms are foundational in systems where data must be saved, transmitted, or shared between applications and services. Through practical exercises, you'll learn how to serialize and deserialize Python objects using various formats such as JSON, CSV, XML, and Python’s native `pickle`.

---

## 🧠 Key Concepts

### ✅ What is Marshaling?

Marshaling refers to transforming memory objects into a transmittable or storable format, often used in remote procedure calls (RPCs) and distributed systems.

### ✅ What is Serialization?

Serialization converts a data structure or object state into a format that can be stored or transmitted. It ensures the object's state can be accurately restored later.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- Differentiate marshaling vs serialization
- Use Python modules to serialize and deserialize data
- Understand applications of serialized data in:
  - Web development
  - Databases
  - Network communication
- Evaluate serialization formats (JSON, XML, binary)
- Implement data persistence using file-based serialization

---

## 📚 Resources

- [Real Python: Serialization](https://realpython.com/python-serialization/)
- [Working with JSON in Python](https://realpython.com/python-json/)
- [Python Pickle Documentation](https://docs.python.org/3/library/pickle.html)
- [Corey Schafer - Pickle Tutorial](https://www.youtube.com/watch?v=2Tw39kZIbhs)
- [CSV to JSON in Python](https://realpython.com/python-csv/)
- [ElementTree XML Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Python Socket Programming](https://realpython.com/python-sockets/)

---

## 🛠 Project Structure

```text
python-serialization/
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
└── task_03_xml.py

