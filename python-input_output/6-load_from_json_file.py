#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python object resulting from the JSON deserialization.

    Raises:
        FileNotFoundError: If the file does not exist.
        JSONDecodeError: If the file content is not valid JSON.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
