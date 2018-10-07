# https://leetcode.com/problems/binary-gap/description/

def binaryGap(self, N):
    if N == 0:
        return 0
    else:
        maxDist = 0
        record = 0
        oneBefore = False
        while N > 0:
            resi = N % 2
            if not oneBefore and resi:
                oneBefore = True
            elif oneBefore:
                record += 1
                maxDist = max(maxDist, record)
                if resi:
                    record = 0
            N //= 2
        return maxDist

# Faster than 93% of accepted submissions at 40ms        