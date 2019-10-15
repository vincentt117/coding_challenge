# From: https://stackoverflow.com/questions/15390807/integer-square-root-in-python

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x