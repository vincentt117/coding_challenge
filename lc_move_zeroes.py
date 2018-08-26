# Facebook - Move Zeroes

# https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/262/

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroC = 0
        for i in nums:
            if i == 0:
                zeroC += 1
        for j in range(zeroC):
            nums.remove(0)
        nums += [0] * zeroC
        return(nums)