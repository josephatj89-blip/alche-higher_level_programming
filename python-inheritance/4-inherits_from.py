#!/usr/bin/python3
"""Module that checks if an object's class inherits from a specified class."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited,
    directly or indirectly, from a_class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
