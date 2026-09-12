#!/usr/bin/python3
"""Module that defines a Square class, inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size (width and height) of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
