# Python OOP - Abstract Classes, Interfaces, Subclassing

## Introduction

Welcome to this advanced Object-Oriented Programming (OOP) project in Python. In this set of exercises, you'll explore key OOP paradigms such as abstract classes, interfaces, duck typing, subclassing built-in types, multiple inheritance, and mixins.

By completing these tasks, you will become proficient in applying OOP principles to design clean, reusable, and scalable Python applications.

---

## Learning Objectives

- **Abstract Classes**: Define abstract methods that must be implemented in derived classes using Python's `abc` module.
- **Interfaces & Duck Typing**: Leverage duck typing and interface-like contracts for flexible and readable code.
- **Subclassing Standard Types**: Extend Python base types like `list` and iterators to implement custom behavior.
- **Method Overriding**: Customize or enhance the behavior of inherited methods.
- **Multiple Inheritance**: Combine features from multiple parent classes using Python’s MRO (Method Resolution Order).
- **Mixins**: Reuse and compose behavior across unrelated classes.

---

## Resources

You are encouraged to review the following:

- [Python 3 Object-Oriented Programming (Book)](https://www.packtpub.com/product/python-3-object-oriented-programming/9781789615852)
- [Python abc module documentation](https://docs.python.org/3/library/abc.html)
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - OOP YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
- [Sentdex - Python OOP Tutorial](https://www.youtube.com/watch?v=JeznW_7DlB0)

---

## Requirements

- Python 3.8.5 (Ubuntu 20.04 LTS)
- All scripts must begin with `#!/usr/bin/env python3`
- Files must be executable and follow [pycodestyle](https://pycodestyle.readthedocs.io/en/latest/) (2.7.*)
- Each module, class, and function must have full-sentence docstrings
- Tests should be thorough and edge cases considered
- Use `super()` when overriding methods

---

## Directory Structure




---

## Tasks

### 0. Abstract Animal Class and Its Subclasses

**File:** `task_00_abc.py`

- Create abstract class `Animal` with abstract method `sound()`.
- Implement subclasses `Dog` and `Cat`, each overriding `sound()`.

💡 Trying to instantiate `Animal` should raise a `TypeError`.

---

### 1. Shapes, Interfaces, and Duck Typing

**File:** `task_01_duck_typing.py`

- Define abstract class `Shape` with methods `area()` and `perimeter()`.
- Create `Circle` and `Rectangle` subclasses.
- Implement `shape_info(obj)` to demonstrate duck typing.

💡 `shape_info()` should not check types, just call methods.

---

### 2. Extending Python List with Notifications

**File:** `task_02_verboselist.py`

- Extend built-in `list` with class `VerboseList`.
- Override `append`, `extend`, `remove`, and `pop` to print notifications.

🛠 Use `super()` to retain original list behavior.

---

### 3. CountedIterator – Track Iteration

**File:** `task_03_countediterator.py`

- Create `CountedIterator` that wraps an iterable and counts how many times `__next__()` has been called.
- Implement method `get_count()` to retrieve iteration count.

💡 Ensure `StopIteration` is handled appropriately.

---

### 4. The Enigmatic FlyingFish – Multiple Inheritance

**File:** `task_04_flyingfish.py`

- Define classes `Fish` and `Bird` with `swim()`, `fly()`, and `habitat()` methods.
- Create `FlyingFish` that inherits from both.
- Override all methods with new behaviors.

🧠 Use `FlyingFish.__mro__` to inspect method resolution order.

---

### 5. The Mystical Dragon – Mixins

**File:** `task_05_dragon.py`

- Create mixins: `SwimMixin` and `FlyMixin` with `swim()` and `fly()`.
- Create class `Dragon` that inherits from both.
- Add a `roar()` method unique to `Dragon`.

💡 Mixins should be small, focused, and reusable.

---

## Example Test Files

You can test each task using the following files:

- `main_00_abc.py`
- `main_01_duck_typing.py`
- `main_02_verboselist.py`
- `main_03_countediterator.py`
- `main_04_flyingfish.py`
- `main_05_dragon.py`

---

## Author

Project developed as part of the Holberton School curriculum.



