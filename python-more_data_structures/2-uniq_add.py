#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Calculates the sum of all unique integers in a list.

    Args:
        my_list: A list of numbers. Defaults to an empty list.

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

# Example usage
my_list = [1, 2, 3, 2, 4, 1, 5]
unique_sum = uniq_add(my_list)
print(unique_sum)  # Output: 11 (1 + 2 + 3 + 4 + 5)
