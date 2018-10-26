# https://leetcode.com/problems/long-pressed-name/

class Solution:
     def isLongPressedName(self, name, typed):
            i = 0
            for j in range(len(typed)):
                if i < len(name) and name[i] == typed[j]:
                    i += 1
                elif j == 0 or typed[j] != typed[j - 1]:
                    return False
            return i == len(name)

# Found in discussion