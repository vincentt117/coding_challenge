# https://leetcode.com/problems/reverse-bits/
# Optimal solution

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        bits = []
        while n > 0:
            bits.append(n % 2)
            n //= 2
        bits += [0] * (32 - len(bits))
        ctr = 0
        for i in range(len(bits) - 1, - 1, -1):
            if bits[i] == 1: ret += (2 ** ctr)
            ctr += 1
        return ret