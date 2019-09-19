# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len = float('inf')
        running_sum = 0
        left = right = 0
        while right < len(nums) or running_sum > s:
            running_sum += nums[right]
            while running_sum >= s and left <= right:
                min_len = min(min_len, right - left + 1)
                running_sum -= nums[left]
                left += 1
            right += 1
        if min_len == float('inf'):
            return 0
        return min_len