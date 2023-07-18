#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """"prints a matrix of integers"""
    for row in matrix:
        for col in range(len(row)):
            if col < len(row) - 1:
                end_col = " "
            else:
                end_col = ""
            print("{:d}".format(row[col]), end=end_col)
        print()
