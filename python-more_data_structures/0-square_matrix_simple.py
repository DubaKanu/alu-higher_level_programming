#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size with squared values
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    return new_matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
squared_matrix = square_matrix_simple(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("\nSquared matrix:")
for row in squared_matrix:
    print(row)
