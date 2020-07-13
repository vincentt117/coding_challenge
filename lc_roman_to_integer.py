# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
# Found in discussion


class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == 'I' and (s[i + 1] == "V" or s[i + 1] == "X"): ret -= 1
            elif i < len(s) - 1 and s[i] == 'X' and (s[i + 1] == "L" or s[i + 1] == "C"): ret -= 10
            elif i < len(s) - 1 and s[i] == 'C' and (s[i + 1] == "D" or s[i + 1] == "M"): ret -= 100
            elif s[i] == "M": ret += 1000
            elif s[i] == "D": ret += 500
            elif s[i] == "C": ret += 100
            elif s[i] == "L": ret += 50
            elif s[i] == "X": ret += 10
            elif s[i] == "V": ret += 5
            elif s[i] == "I": ret += 1
        return ret
# Solution from  July 13, 2020
        