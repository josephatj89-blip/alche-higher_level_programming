#!/usr/bin/python3
"""Module that provides the classic FizzBuzz function."""


def fizzbuzz():
    """Print numbers 1 to 100, replacing multiples of 3/5 with words."""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
