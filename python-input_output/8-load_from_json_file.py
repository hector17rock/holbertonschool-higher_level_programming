#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The __dict__ attribute of the object.
    """
    return obj.__dict__
