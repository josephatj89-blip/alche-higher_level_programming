#!/usr/bin/python3
"""Module that returns the dictionary description of an object for
JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structures
    of an object.
    """
    return obj.__dict__
