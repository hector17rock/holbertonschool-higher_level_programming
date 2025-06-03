#!/usr/bin/python3
"""Defines a Student class that can be reloaded from JSON."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance.

        Args:
            attrs (list): Attributes to include (optional).

        Returns:
            dict: Dictionary of attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dict.

        Args:
            json (dict): Dictionary of new attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
