#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

# Test cases
print(islower('a'))  # Should return True
print(islower('z'))  # Should return True
print(islower('A'))  # Should return False
print(islower('Z'))  # Should return False
print(islower('m'))  # Should return True
print(islower('1'))  # Should return False
