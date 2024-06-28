#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)

# Example usage:
print_last_digit(12345)  # Output: 5
print_last_digit(-9876)  # Output: 6
print_last_digit(0)      # Output: 0
