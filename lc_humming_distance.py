# https://leetcode.com/problems/hamming-distance/
# Optimal solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                ret += 1
            x //= 2
            y //= 2
        return ret
        