#!/usr/bin/env python3
"""Defines an abstract Animal class and its concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animals."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"
