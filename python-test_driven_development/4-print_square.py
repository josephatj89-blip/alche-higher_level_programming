#!/usr/bin/python3
"""Defines a function that prints a square made of the '#' character."""


def print_square(size):
    """Print a size x size square using the '#' character."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
