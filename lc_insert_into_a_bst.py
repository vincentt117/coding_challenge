# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

def insertIntoBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    node = root
    placing = True
    while placing:
        if val > node.val:
            if not node.right:
                node.right = TreeNode(val)
                placing = not placing
            else:
                node = node.right
        else:
            if not node.left:
                node.left = TreeNode(val)
                placing = not placing
            else:
                node = node.left
    return root

# Faster than 93% of accepted submissions
                
                
