# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Optimal solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        curr_lvl, next_lvl = [[0, root]], [] 
        max_width = 1
        while curr_lvl:
            left, right = None, None
            for block in curr_lvl:
                idx, node = block[0], block[1]
                if left == None: left = right = idx
                else: right = idx
                if node.left or node.right:
                    if node.left: next_lvl.append([idx * 2, node.left])
                    if node.right: next_lvl.append([idx * 2 + 1, node.right])
            if left != None: max_width = max(max_width, (right - left) + 1)
            curr_lvl, next_lvl = next_lvl, []
        return max_width