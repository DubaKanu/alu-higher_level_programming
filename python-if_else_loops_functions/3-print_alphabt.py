#!/usr/bin/python3

print("".join(["{}".format(chr(i)) for i in range(97, 123) if chr(i) != 'q' and chr(i) != 'e']), end="")
