#!/usr/bin/python3

def matrix_divided(matrix, div):

    if not isinstance(div, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
