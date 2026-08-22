#!/usr/bin/python3
"""Module that defines new_in_list."""


def new_in_list(my_list, idx, element):
    """Return a copy of the list with an element replaced at idx."""
    new_list = my_list[:]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
