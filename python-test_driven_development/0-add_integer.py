#!/usr/bin/python3
"""Defines a function that adds two integers together.

Both arguments are cast to int before the addition, and a
TypeError is raised if either one is not an int or a float.
"""


def add_integer(a, b=98):
    """Add two integers or floats.

    Floats are cast to int before addition."""
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
