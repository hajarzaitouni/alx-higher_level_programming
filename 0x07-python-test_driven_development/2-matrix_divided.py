#!/usr/bin/python3
def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:

        matrix (list of lists): list of lists of integers or floats
        div (int/float): the divider

    Raises:
        TypeError: If the matrix is not list of lists of int/float
        TypeError: If the size of rows is not the same
        TypeError: if div is not int/float
        ZeroDivisionError: div == 0

    Return: a new matrix divided
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(col, (int, float)))
                    for row in matrix for col in row)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
