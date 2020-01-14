# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)