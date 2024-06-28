#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print(f"{result}")

# Test cases
uppercase("hello world")  # Should print "HELLO WORLD"
uppercase("Python")       # Should print "PYTHON"
uppercase("123abc")       # Should print "123ABC"
