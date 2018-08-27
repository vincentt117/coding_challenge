# Add Binary

# https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/263/

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

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
    