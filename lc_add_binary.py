# Add Binary

# https://leetcode.com/problems/add-binary/

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


# Solution from July 19, 2020
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 
        sum_l = []
        idx = -1 
        while abs(idx) <= len(a) or abs(idx) <= len(b):
            a_idx = int(a[idx]) if abs(idx) <= len(a) else None
            b_idx = int(b[idx]) if abs(idx) <= len(b) else None
            idx_sum = (a_idx if a_idx != None else 0) + (b_idx if b_idx != None else 0) + carry
            sum_l.append(str(idx_sum % 2))
            carry = idx_sum // 2
            idx -= 1
        if carry == 1: sum_l.append('1')
        return ''.join(sum_l[::-1])

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lenA = len(a) - 1
        lenB = len(b) - 1
        retString = ""
        hold = 0
        while lenA >= 0 or lenB >= 0 or hold != 0:
            if lenA >= 0:
                holdA = int(a[lenA])
                lenA -= 1
            if lenB >= 0:
                holdB = int(b[lenB])
                lenB -= 1
            holdSum = holdA + holdB + hold 
            if holdSum == 0:
                hold = 0
                retString = "0" + retString
            elif holdSum == 1:
                hold = 0
                retString = "1" + retString
            elif holdSum == 2:
                hold = 1
                retString = "0" + retString
            else:
                hold = 1
                retString = "1" + retString
            holdA = 0
            holdB = 0
        return(retString)        
