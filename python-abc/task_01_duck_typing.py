#!/usr/bin/env python3
"""Defines Shape ABC and implementations Circle and Rectangle."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Compute and return area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute and return perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape (duck typing)."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
