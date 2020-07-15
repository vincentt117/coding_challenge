# https://leetcode.com/problems/reverse-words-in-a-string/description/

def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    s = s.split()
    return ' '.join(s[::-1])

# Faster than 99% of submissions

# Solution from July 15, 2020
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ret = ''
        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            if len(word) > 0:
                ret += word + ' '
        return ret[:-1]
                
        
    