#!/usr/bin/python3
"""Module that defines divisible_by_2."""


def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating divisibility by 2."""
    result = []
    for integer in my_list:
        result.append(integer % 2 == 0)
    return result
