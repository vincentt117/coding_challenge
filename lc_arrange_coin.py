# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/
# Suboptimal
# Binary search and math better
class Solution:
    def arrangeCoins(self, n: int) -> int:
        ret_cnt = 0
        while n >= ret_cnt + 1:
            ret_cnt += 1
            n -= ret_cnt
        return ret_cnt
        