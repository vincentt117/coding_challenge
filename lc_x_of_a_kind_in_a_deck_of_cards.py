# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

class Solution:
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1