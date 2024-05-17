#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    buffer = []
    for row in matrix:
        buffer_row = []
        for x in row:
            buffer_row.append(x**2)
        buffer.append(buffer_row)
    return buffer
