#!/usr/bin/python3
"""Module that defines multiple_returns."""


def multiple_returns(sentence):
    """Return a tuple of the sentence's length and first character."""
    first_char = sentence[0] if len(sentence) > 0 else None
    return (len(sentence), first_char)
