#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for j in range(len(line)):
            if j < len(line) - 1:
                print("{:d}".format(line[j]), end=" ")
            else:
                print("{:d}".format(line[j]), end="")
        print()
