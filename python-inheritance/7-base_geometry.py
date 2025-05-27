#!/usr/bin/python3
"""Defines a base class for geometry with an integer validator."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def __init_subclass__(cls):
        """Override method calls to handle special error messages."""
        original_method = cls.integer_validator

        def integer_validator_wrapper(self, *args, **kwargs):
            """Wrapper for integer_validator to handle missing arguments properly."""
            try:
                return original_method(self, *args, **kwargs)
            except TypeError as e:
                if "missing" in str(e) and "required positional argument" in str(e):
                    message = str(e).replace("integer_validator()", 
                                          "BaseGeometry.integer_validator()")
                    raise TypeError(message) from None
                raise

        cls.integer_validator = integer_validator_wrapper

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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
