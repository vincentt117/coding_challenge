# Valid Palindrome

# https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/288/

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        print(s)
        if s[0].isalpha() and s[-1].isalpha():
            if s[0].lower() == s[-1].lower() :
                return isPalindrome(s[1:-1])
            else:
                return False
        elif s[0].isalpha() and not s[-1].isalpha():
            return isPalindrome(s[:-1])
        elif not s[0].isalpha() and s[-1].isalpha():
            return isPalindrome(s[1:])
        else:
            return isPalindrome(s[1:-1])
        