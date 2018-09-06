# https://leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    posDict = {}
    for i,v in enumerate(nums):
        if v in posDict and i - posDict[v] <= k:
            return True
        posDict[v] = i
    
    return False

# Faster than 70% of submissions at 52 ms where fastest was 40 ms