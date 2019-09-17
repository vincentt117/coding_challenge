# https://leetcode.com/problems/decode-ways/submissions/

# Faster than 97.21, memory better than 16%

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1 and 0 < int(s):
            return 1
        combos = [1, 0]
        for i in range(len(s) - 1, -1, -1):
            this_comb = 0
            if  i < len(s) - 1 and 10 <= int(s[i:i + 2]) <= 26:
                this_comb += 1 * combos[1]
            if 0 < int(s[i]):
                this_comb += 1 * combos[0]
            combos = [this_comb, combos[0]]
        return combos[0]
        
        
    # Time Limit Exceeded    
    # def numDecodings(self, s: str) -> int:
        # done = {}
        # def helper(s):
        #     n = len(s)
        #     if n == 0 or n == 1 and int(s) > 0:
        #         return 1
        #     elif n >= 2:
        #         ret = 0
        #         if  10 <= int(s[:2]) <= 26:
        #             if not s[2:] in done:
        #                 done[s[2:]] = self.numDecodings(s[2:])
        #             ret += 1 * done[s[2:]]
        #         if 0 < int(s[0]):
        #             if not s[1:] in done:
        #                 done[s[1:]] = self.numDecodings(s[1:])
        #             ret += 1 * done[s[1:]]
        #         return ret
        #     else:
        #         return 0
        # return helper(s)
    # "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
                
        
        