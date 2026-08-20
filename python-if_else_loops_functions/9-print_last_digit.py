#!/usr/bin/python3
"""Module that provides a function to print the last digit of a number."""


def print_last_digit(number):
    """Print the last digit of number (as a positive digit) and return it."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
