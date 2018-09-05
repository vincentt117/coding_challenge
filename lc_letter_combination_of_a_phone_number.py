# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ret = []
        dictionary = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r", "s"], "8":["t","u","v"], "9":["w","x","y", "z"]}
        ret = dictionary[digits[0]]
        if len(digits) > 1:
            for i in digits[1:]:
                copy = ret[:]
                ret = [j + dictionary[i][0] for j in copy] + [j + dictionary[i][1] for j in copy] + [j + dictionary[i][2] for j in copy]
                if len(dictionary[i]) == 4:
                    ret += [j + dictionary[i][3] for j in copy]
                    
        return ret

# Solution faster than 100% of submissions