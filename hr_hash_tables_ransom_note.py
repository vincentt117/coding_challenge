# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magDic = collections.defaultdict(int)
    for i in magazine:
        magDic[i] += 1
    for j in note:
        if j not in magDic or magDic[j] == 0:
            print("No")
            return None
        magDic[j] -= 1
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
