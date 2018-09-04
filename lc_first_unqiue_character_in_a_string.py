# https://leetcode.com/explore/interview/card/bloomberg/68/array-and-strings/373/

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charCount = collections.defaultdict(int)
        for i in s:
            charCount[i] += 1
        for j, v in enumerate(s):
            if charCount[v] == 1:
                return j
        return -1
    # Two pass through string and counted occurances. Faster than ~81% of submissions

    def firstUniqCharOneLine(self, s):
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
    # Check if count of character is 1 for all all letters in the alphabet if the letter is in the string
            