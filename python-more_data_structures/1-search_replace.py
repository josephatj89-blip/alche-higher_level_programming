#!/usr/bin/python3
"""Module that defines search_replace."""


def search_replace(my_list, search, replace):
    """Return a new list with all occurrences of search replaced."""
    return [replace if value == search else value for value in my_list]
