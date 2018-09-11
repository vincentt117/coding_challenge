# https://leetcode.com/problems/hamming-distance/description/

def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    binX = ""
    binY = ""
    hammerDist = 0
    while x or y:
        if x % 2 != y % 2:
            hammerDist += 1
        x //= 2
        y //= 2
    return hammerDist
        
        1
return hammerDist

# Faster than 100% of submissions

# Can do in one line with return bin(x^y).count('1'), where bin() is a bit-wise operation with 1 at position where the corresponding
# bits are the same
        