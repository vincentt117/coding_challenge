# https://leetcode.com/problems/path-sum-ii/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        elif sum - root.val == 0 and not root.left and not root.right:
            return [[root.val]]
        else:
            left = self.pathSum(root.left, sum - root.val)
            right = self.pathSum(root.right, sum - root.val)
            store = []
            if left:
                store = store + left
            if right:
                store = store + right
            return([[root.val] + i for i in store ])

# 64 ms thus faster than 60% of all submissions which were between 50ms and 150ms
        
    