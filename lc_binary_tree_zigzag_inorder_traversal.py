# Binary Tree Zigzag Level Order Traversal

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def zigzagLevelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     if not root:
    #         return []
    #     else:
    #         rtoL = True
    #         retList = []
    #         parentNodes = [root]
    #         childNodes = []
    #         while parentNodes:
    #             if rtoL:
    #                 for i in range(len(parentNodes)-1, -1, -1):
    #                     if parentNodes[i].right:
    #                         childNodes.append(parentNodes[i].right)
    #                     if parentNodes[i].left:
    #                         childNodes.append(parentNodes[i].left)
    #             else:
    #                 for i in range(len(parentNodes)-1, -1, -1):
    #                     if parentNodes[i].left:
    #                         childNodes.append(parentNodes[i].left)
    #                     if parentNodes[i].right:
    #                         childNodes.append(parentNodes[i].right)
    #             rtoL = not rtoL
    #             retList = retList + [[ i.val for i in parentNodes]]
    #             parentNodes = childNodes
    #             childNodes = []
    #         return retList              

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in xrange(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res