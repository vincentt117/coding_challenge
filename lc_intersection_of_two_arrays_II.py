# Intersection of Two Arrays II

# https://leetcode.com/explore/interview/card/facebook/5/round-1-phone-interview/270/

# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:

# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    freqCount = {}
    index = max(len(nums1), len(nums2))
    for i in range(index):
        if i < len(nums1):
            if nums1[i] in freqCount:
                freqCount[nums1[i]][0] += 1
            else:
                freqCount[nums1[i]] = [1,0]
        if i < len(nums2):
            if nums2[i] in freqCount:
                freqCount[nums2[i]][1] += 1
            else:
                freqCount[nums2[i]] = [0,1]  
    retList = []
    for j in freqCount:
        retList = retList + [j] * min(freqCount[j][0], freqCount[j][1])
    return retList

# Faster than 69% of solutions


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1index = 0
        n2index = 0
        intersection = []
        while n1index < len(nums1) and n2index < len(nums2):
            if nums1[n1index] == nums2[n2index]:
                intersection.append(nums1[n1index])
                n1index += 1
                n2index += 1
            elif nums1[n1index] > nums2[n2index]:
                n2index += 1
            elif nums1[n1index] < nums2[n2index]:
                n1index += 1
        return intersection
        
