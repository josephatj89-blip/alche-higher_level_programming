#!/usr/bin/python3
"""Module that defines uniq_add."""


def uniq_add(my_list=[]):
    """Add all unique integers in a list, each counted once."""
    return sum(set(my_list))
