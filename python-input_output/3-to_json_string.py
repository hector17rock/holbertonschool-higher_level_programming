#!/usr/bin/python3
"""Defines a function that converts a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON string representation of `my_obj`.

    Raises:
        TypeError: If `my_obj` contains unserializable types (e.g., set).
    """
    return json.dumps(my_obj)
