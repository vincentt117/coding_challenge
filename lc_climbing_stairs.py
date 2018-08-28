# Climbing Stairs

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        storage = [0]*n
        return self.climbStairsHelper(n, storage)
    
    def climbStairsHelper(self, n, storage):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if not storage[n-2]:
                storage[n-2] = self.climbStairsHelper(n-2, storage)
            if not storage[n-1]:
                storage[n-1] = self.climbStairsHelper(n-1, storage)
            return storage[n-2] + storage[n-1]

# Optimal solution
            
        