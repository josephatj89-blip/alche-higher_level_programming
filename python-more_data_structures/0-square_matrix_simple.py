#!/usr/bin/python3
"""Module that defines square_matrix_simple."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared."""
    return [[value ** 2 for value in row] for row in matrix]
