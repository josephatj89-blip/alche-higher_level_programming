#!/usr/bin/python3
"""Module for safe_print_integer function."""


def safe_print_integer(value):
    """Print value as an integer using "{:d}".format().

    Returns True if value was printed successfully (i.e. is an integer),
    False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
