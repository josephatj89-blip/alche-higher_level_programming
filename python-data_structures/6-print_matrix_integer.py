#!/usr/bin/python3
"""Module that defines print_matrix_integer."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line."""
    for row in matrix:
        line = ""
        for i, integer in enumerate(row):
            if i > 0:
                line += " "
            line += "{:d}".format(integer)
        print(line)
