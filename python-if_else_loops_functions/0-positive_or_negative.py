#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    status = "is positive"
elif number == 0:
    status = "is zero"
else:
    status = "is negative"
print(f"{number} {status}")
