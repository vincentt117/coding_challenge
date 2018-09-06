# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))
# Perfect, faster than 100% of solutions