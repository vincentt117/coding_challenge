# https://leetcode.com/problems/minimum-window-substring/

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        
        t_count = collections.defaultdict(int)
        
        for v in t:
            t_count[v] += 1
        
        missing_letter = dict(t_count)
        extra_letter = collections.defaultdict(int)
        
        l, r = 0, -1
        l_best, r_best = 0, len(s) - 1
        
        while r < len(s) - 1 or not missing_letter:
            while missing_letter and r < len(s) - 1:
                r += 1
                if s[r] in t_count and s[r] in missing_letter:
                    missing_letter[s[r]] -= 1
                    if missing_letter[s[r]] == 0:
                        del missing_letter[s[r]]
                elif s[r] in t_count and s[r] not in missing_letter:
                    extra_letter[s[r]] += 1  
                    
            if l == 0 and r == len(s) - 1 and missing_letter:
                return ''
            
            if r - l < r_best - l_best:
                l_best, r_best = l, r
            
            if r_best + 1 - l_best == len(t) and not missing_letter:
                return s[l_best: r_best + 1]
                
            if s[l] in t_count:
                if extra_letter[s[l]] > 0:
                    extra_letter[s[l]] -= 1
                else:
                    missing_letter[s[l]] = 1
            
            l += 1
        
        return s[l_best: r_best + 1]
                

        
        
            
        