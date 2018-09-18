# https://leetcode.com/problems/shifting-letters/description/

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        ret = ""
        # Needed to grab this line from discussion
        for i in range(len(shifts) - 1)[::-1]: shifts[i] += shifts[i + 1]
        for j,v in enumerate(S):
            rolling = 0
            ret += chr(((ord(v) - 97 + shifts[j]) % 26) + 97)
        return ret

# Faster than ~75% of accepted submissions at 68ms
        