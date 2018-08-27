# 3Sum
# https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/283/

# #Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        print(i, v)
        if i >= 1 and v == nums[i-1]:
            continue
        d = set()
        for x in nums[i+1:]:
            if x not in d:
                d.add(-v-x)
            else:
                res.add((v, -v-x, x))
    return map(list, res)
print(threeSum([-1, 0, 1, 2, -1, -4]))

# Solution from https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/283/discuss/7384/My-Python-solution-based-on-2-sum-200-ms-beat-93.37


