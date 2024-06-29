#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size with squared values
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    return new_matrix

# Test cases
test_cases = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2], [4, 5]],
    [[1, 2], [4, 5], [7, 8]],
    [[1]],
    [[1], [2], [3], [4]],
    [[]]
]

for i, matrix in enumerate(test_cases):
    squared_matrix = square_matrix_simple(matrix)
    print(f"Test case {i + 1}:")
    print("Original matrix:")
    for row in matrix:
        print(row)
    print("Squared matrix:")
    for row in squared_matrix:
        print(row)
    print()  # For better readability between test cases
