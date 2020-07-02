# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/
# Optimal solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        lvl, nxt_lvl = [root], []
        ret, lvl_val = [], []
        while lvl:
            for node in lvl:
                lvl_val.append(node.val)
                if node.left:
                    nxt_lvl.append(node.left)
                if node.right:
                    nxt_lvl.append(node.right)
            ret.append(lvl_val)
            lvl, nxt_lvl, lvl_val = nxt_lvl, [], []
        return ret[::-1]
                     