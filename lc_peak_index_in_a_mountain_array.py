# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

def peakIndexInMountainArray(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    peak = 0
    if len(A) == 1:
        return peak
    for i, v in enumerate(A):
        if i > 0 and v > A[i-1] and (i == len(A) - 1 or v > A[i+1]):
            return i

# Faster than 59% of accepted submissions at 44ms