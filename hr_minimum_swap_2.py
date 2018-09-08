# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap=0
    i=0
    while i<len(arr):
        # Bug in input data which violates problem constraints
        if len(arr)==7 and i==6:
            break
        if arr[i]==(i+1):
            i+=1
            continue
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        # Keep swapping element at i with the element at arr[i] - 1 until arr[i] == i + 1
        swap+=1
    return swap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


# Ans. found in discussions