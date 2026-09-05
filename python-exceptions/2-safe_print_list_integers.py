#!/usr/bin/python3
"""Module for safe_print_list_integers function."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of my_list that are integers.

    Non-integer elements are skipped silently. If x is bigger than the
    list, an IndexError is raised (not caught).

    Returns the real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
