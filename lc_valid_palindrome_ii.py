# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                op1 = s[l:r]
                op2 = s[l + 1: r + 1]
                if op1 == op1[::-1] or op2 == op2[::-1]:
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return True
        