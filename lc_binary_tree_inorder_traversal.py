# Binary Tree Inorder Traversal

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if not root:
    #         return []
    #     else:
    #         retList = []
    #         if root.left:
    #             retList = retList + self.inorderTraversal(root.left)
    #         retList = retList + [root.val]
    #         if root.right:
    #             retList = retList + self.inorderTraversal(root.right)
    #         return retList
    # iteratively       
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
    
# Recursive solution faster than 99% of submissions
# Iterative solution found in discussion

    
            