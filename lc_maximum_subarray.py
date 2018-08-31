# Maximum Subarray

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        else:
            maxSum = tracking = nums[0]
            for i in range(1, len(nums)):
                tracking = max(nums[i], tracking + nums[i])
                maxSum = max(maxSum, tracking)        
            return maxSum


# Solution found in discussion

        
        