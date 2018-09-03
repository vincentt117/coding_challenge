# Sort Colors

# https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/193/

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

# Straight forward solution
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count = {0:0, 1:0, 2:0}
    for i in nums:
        count[i] += 1
    index = 0
    for j in range(count[0], 0, -1):
        nums[index] = 0
        index += 1
    for j in range(count[1], 0, -1):
        nums[index] = 1
        index += 1
    for j in range(count[2], 0, -1):
        nums[index] = 2
        index += 1


# Found in discussion
# def sortColors(nums):
#     i = j = 0
#     for k in xrange(len(nums)):
#         v = nums[k]
#         nums[k] = 2
#         if v < 2:
#             nums[j] = 1
#             j += 1
#         if v == 0:
#             nums[i] = 0
#             i += 1


