#!/usr/bin/python3
"""Module that provides a function to print a string in uppercase."""


def uppercase(str):
    """Print the given string in uppercase, followed by a newline."""
    for c in str:
        print("{:s}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c),
              end="")
    print()
