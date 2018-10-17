# https://leetcode.com/problems/reverse-only-letters/description/
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        ret = ""
        front = 0
        back = len(S) - 1
        while front < len(S) and back > -1:
            if S[front].isalpha() and S[back].isalpha():
                ret += S[back]
                front += 1
                back -= 1
            elif not S[front].isalpha() and S[back].isalpha():
                ret += S[front]
                front += 1
            else:
                back -= 1
        return ret + S[front:]
                
                
            
        
        
        