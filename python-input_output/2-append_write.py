#!/usr/bin/python3
"""Module that appends a string to the end of a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and return the number
    of characters added.
    """
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
