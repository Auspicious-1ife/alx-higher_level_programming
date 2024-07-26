#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 0:
        return 1  # Any number to the power of 0 is 1
    elif b > 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result /= a
    return result
