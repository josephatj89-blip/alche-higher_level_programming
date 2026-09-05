#!/usr/bin/python3
"""Module for safe_print_division function."""


def safe_print_division(a, b):
    """Divide a by b and print the result inside the finally clause.

    Returns the result of the division, or None if it failed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
