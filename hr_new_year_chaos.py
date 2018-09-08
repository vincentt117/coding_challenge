# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):    
    # Fail if element displaced by more than two positions
    for i,v in enumerate(q):
        if v - (i+1) > 2:
            print("Too chaotic")
            return None
    
    # Bubble sort to figure out number of swaps
    bribes = 0
    swapped = False
    for j, w in enumerate(q):
        for k in range(len(q) - j - 1):
            if q[k] > q[k+1]:
                q[k], q[k+1] = q[k+1], q[k]
                bribes += 1
                swaped = True
        if swaped:
            swaped = False
        else:
            break
    print(bribes)
    

          
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


# Had to look at discussion
