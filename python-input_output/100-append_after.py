#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts `new_string` after every line containing `search_string`.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after matching lines.
    """
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            result.append(line)
            if search_string in line:
                result.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as f:
        f.writelines(result)
