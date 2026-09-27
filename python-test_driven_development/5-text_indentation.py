#!/usr/bin/python3
"""Defines a function that prints text with extra indentation.

Two new lines are printed after each '.', '?', or ':' character.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', and ':'."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        if char == "\n":
            if line.strip():
                print(line.strip())
            line = ""
        else:
            line += char
            if char in ".?:":
                print(line.strip())
                print()
                line = ""
    if line.strip():
        print(line.strip(), end="")
