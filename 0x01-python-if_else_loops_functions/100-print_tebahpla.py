#!/usr/bin/python3
for as_code in range(122, 96, -1):
    if as_code % 2 == 0:
        a = as_code
    else:
        a = as_code - 32
    print("{}".format(chr(a)), end="")
