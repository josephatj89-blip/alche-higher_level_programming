#!/usr/bin/python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raises an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")
