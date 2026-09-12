#!/usr/bin/python3
"""Module that reads and prints the content of a UTF-8 text file."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout."""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
