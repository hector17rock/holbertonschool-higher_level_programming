#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
