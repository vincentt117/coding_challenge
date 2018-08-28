# 713. Subarray Product Less Than K

# https://leetcode.com/problems/subarray-product-less-than-k/description/

# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Note:

# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        validCount = 0
        upper = 0
        lower = 0
        product = nums[0]
        while lower < len(nums):          
            # Case where top limit is reached
            if upper == len(nums) - 1:
                if product < k:
                    validCount += upper - lower + 1
                product = product / nums[lower] 
                lower += 1
            # Case where introduction of new element will not result in product >= k
            elif product * nums[upper + 1] < k:
                product = product * nums[upper + 1]
                upper += 1 
            # Case where introduction of new element will result in product >= k
            else:
                if lower == upper:
                    if nums[upper] < k:
                        validCount += 1
                    upper += 1
                    lower = upper
                    product = nums[upper]
                else:
                    validCount += upper - lower + 1
                    product = product / nums[lower]
                    lower += 1
        return int(validCount)

# Solution faster than 2% of submissions
