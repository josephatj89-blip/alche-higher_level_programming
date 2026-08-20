#!/usr/bin/python3
"""Module that provides a function to check for lowercase characters."""


def islower(c):
    """Return True if c is a lowercase letter, False otherwise."""
    return ord('a') <= ord(c) <= ord('z')
