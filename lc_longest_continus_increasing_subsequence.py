# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        count = 0
        for i, v in enumerate(nums):
            if i == 0 or v > nums[i-1]:
                count += 1
            else:
                maxLen = max(maxLen, count)
                count = 1
        return max(maxLen, count)

# Faster than 77% of accpeted submissions