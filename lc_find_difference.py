# https://leetcode.com/problems/find-the-difference/

import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = collections.defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for j in t:
            s_dict[j] -= 1
        for char in s_dict:
            if s_dict[char] != 0:
                return char
        