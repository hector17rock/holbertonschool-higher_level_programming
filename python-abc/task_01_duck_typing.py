#!/usr/bin/env python3
"""Defines Shape abstract base class and its implementations:
Circle and Rectangle."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete Circle class implementing Shape interface."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete Rectangle class implementing Shape interface."""

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
    """Prints the area and perimeter of a shape using duck typing."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
