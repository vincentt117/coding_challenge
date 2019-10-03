# https://leetcode.com/problems/largest-bst-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.largest_bst_size = 0
        def dfs(root):
            if not root:
                return [float("inf"), float("-inf"), 0]
            left_col = dfs(root.left)
            right_col = dfs(root.right)
            if left_col and right_col: # Both left and right side valid
                if left_col[1] < root.val and root.val < right_col[0]:
                    bst_size = left_col[2] + 1 + right_col[2]
                    self.largest_bst_size = max(bst_size, self.largest_bst_size)                  
                    return [min(left_col[0], root.val), max(root.val, right_col[1]), bst_size]
            return None
                    
        dfs(root)
        return self.largest_bst_size
        