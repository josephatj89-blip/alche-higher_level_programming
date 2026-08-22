#!/usr/bin/python3
"""Module that defines max_integer."""


def max_integer(my_list=[]):
    """Return the biggest integer in a list, or None if empty."""
    if len(my_list) == 0:
        return None
    biggest = my_list[0]
    for integer in my_list[1:]:
        if integer > biggest:
            biggest = integer
    return biggest
