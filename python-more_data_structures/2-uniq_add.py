#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Calculates the sum of all unique integers in a list.

    Args:
        my_list: A list of numbers (defaults to an empty list).

    Returns:
        The sum of all unique integers in the list.
    """

    seen = set()  # Use a set to store unique elements
    total = 0
    for num in my_list:
        if isinstance(num, int):  # Check if element is an integer
            if num not in seen:
                seen.add(num)
                total += num
    return total

# Test cases
test_cases = [
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 1],
    [1, 1, 1, 1, 1],
    [1, 2, 3, 2, 1, 5],
    [1, 2, 3, -2, -1, 5],
    [1],
    []
]

for test_list in test_cases:
  result = uniq_add(test_list)
  print(f"List: {test_list}, Sum: {result}")
