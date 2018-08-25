# 256. Paint House

# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 

# For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... 

# Find the minimum cost to paint all houses.

# Example:

# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
#              Minimum cost: 2 + 5 + 3 = 10.


class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0

        minRedCost = costs[0][0]
        minBlueCost = costs[0][1]
        minGreenCost = costs[0][2]

        for i in range(1, len(costs)):
            oldMRC = 0 + minRedCost
            oldMBC = 0 + minBlueCost
            oldMGC = 0 + minGreenCost

            minRedCost = min(oldMBC, oldMGC) + costs[i][0]
            minBlueCost = min(oldMRC, oldMGC) + costs[i][1]
            minGreenCost = min(oldMRC, oldMBC) + costs[i][2] 
        
        return min(minRedCost, minBlueCost, minGreenCost)

# OPTIMAL: Faster than 100% of solutions

