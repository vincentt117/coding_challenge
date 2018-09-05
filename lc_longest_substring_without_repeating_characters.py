class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        "abcabcbb"
    
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                # update the res
                res = max(res, i-start)
                # here should be careful, like "abba"
                start = max(start, dic[ch]+1)
            dic[ch] = i
        # return should consider the last 
        # non-repeated substring
        return max(res, len(s)-start)


# Required two line changes between solution and answer found in discussion. Faster than 30% of solutions, slower than best by about 50ms