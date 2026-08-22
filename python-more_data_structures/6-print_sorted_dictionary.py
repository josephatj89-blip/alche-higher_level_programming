#!/usr/bin/python3
"""Module that defines print_sorted_dictionary."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary's key-value pairs sorted by key."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
