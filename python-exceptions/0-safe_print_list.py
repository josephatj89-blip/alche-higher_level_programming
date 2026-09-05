#!/usr/bin/python3
"""Module for safe_print_list function."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of my_list, one per line entry, no newline between.

    Returns the real number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
