#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  """
  Computes the square value of all integers in a matrix and returns a new matrix.

  Args:
      matrix: A 2D list representing the matrix. Defaults to an empty list.

  Returns:
      A new 2D list with the squared values of the original matrix.
      The original matrix remains unmodified.
  """

  if not matrix:
    return []  # Handle empty matrix case

  new_matrix = []
  for row in matrix:
    new_row = []
    for element in row:
      # Check if element is an integer before squaring
      if isinstance(element, int):
        new_row.append(element * element)
      else:
        # Handle non-integer elements by keeping them unchanged
        new_row.append(element)
    new_matrix.append(new_row)
  return new_matrix
