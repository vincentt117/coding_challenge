# https://leetcode.com/problems/reverse-words-in-a-string/description/

def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    s = s.split()
    return ' '.join(s[::-1])

# Faster than 99% of submissions
    