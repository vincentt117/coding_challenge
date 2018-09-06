# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums):
        if i != 0 and nums[i] == nums[i - 1]:
            nums.pop(i)
            i -= 1
        else:
            i += 1
    return len(nums)
# Slow, faster than 9% of accepted solutions


def removeDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    i, j, length = 0, 0, len(nums)
    
    if length < 2:
        return length

    # i: current evaluated index, aka, front running
    # j: actual current index of the final list, no dup
    
    while i < length-1:
        if nums[i+1] != nums[j]:
            nums[j+1] = nums[i+1]
            i += 1
            j += 1
        else:
            i += 1
        print(nums)
            
    return j+1
# Fast solution

print(removeDuplicates1([0,0,1,1,1,2,2,3,3,4]))