# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys
import collections


def freqQuery(queries):
    results = []
    lookup = dict()
    freqs = collections.defaultdict(set)
    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            results.append(1 if freqs[value] else 0)
    return results  
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()


# Found in discussions