#!/usr/bin/python3
"""
This module defines a function matrix_divided(matrix, div) that divides
all elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): A matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If the matrix elements are not lists of integers/floats,
        if div is not a number, or if the rows of the matrix
        are not of the same size.
        ZeroDivisionError: If div is zero.
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or matrix == []:
        raise TypeError(error)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        if type(row) is not (list) or row == []:
            raise TypeError(error)
        elif len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        divided_row = []
        for n in row:
            if type(n) not in (int, float):
                raise TypeError(error)
            divided_row.append(round(n / div, 2))
        divided_matrix.append(divided_row)

    return divided_matrix
