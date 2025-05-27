#!/usr/bin/python3
"""Defines a base class BaseGeometry with validation methods."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the parameter `value`.

        Args:
            name (str): The name of the parameter (used in the error message).
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
