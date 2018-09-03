#   Merge Sorted Array

# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/258/

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    # Doesn't run in compiler
    # Duplicate nums1 and keep only initialized components for nums2
    dups1 = nums1[:m]
    nums2 = nums2[:n]
    nums1 = []
    while dups1 and nums2:
        print(nums1)
        if dups1[0] < nums2[0]:
            nums1.append(dups1.pop(0))
        else:
            nums1.append(nums2.pop(0))
    # Add rest of remaining list to nums1
    nums1 = nums1 + dups1 + nums2
    return nums1


    # Solution found in discussion
    # def merge(self, nums1, m, nums2, n):
    #     while m > 0 and n > 0:
    #         if nums1[m-1] >= nums2[n-1]:
    #             nums1[m+n-1] = nums1[m-1]
    #             m -= 1
    #         else:
    #             nums1[m+n-1] = nums2[n-1]
    #             n -= 1
    #     if n > 0:
    #         nums1[:n] = nums2[:n]

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
