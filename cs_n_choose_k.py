# https://app.codesignal.com/challenge/a8GNsYr8FQxZmMhJj

import math

def countWays(n, k):
    if k > n:
        return 0
    return math.factorial(n)//(math.factorial(k) * math.factorial(n-k)) % 1000000007
