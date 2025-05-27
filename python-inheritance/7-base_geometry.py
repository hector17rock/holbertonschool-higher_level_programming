#!/usr/bin/python3
"""Defines a base class for geometry with an integer validator."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the value (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        # Validate the value - None will be caught here as it's not an int
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
