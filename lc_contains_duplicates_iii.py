# https://leetcode.com/problems/contains-duplicate-iii/description/

def containsNearbyAlmostDuplicate(nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    for i,v in enumerate(nums):
        for j, n in enumerate(nums[i + 1:min(i + k + 1, len(nums))]):
            if abs(v-n) <= t:
                return True
        if i + k > len(nums):
            return False
    return False

# Too slow for very long inputs