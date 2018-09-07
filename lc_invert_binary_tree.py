# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return []
    return self.invertTreeHelper(root)

def invertTreeHelper(self, root):
    if root:
        root.left, root.right = root.right, root.left
        self.invertTreeHelper(root.left)
        self.invertTreeHelper(root.right)
    return root

# Faster than ~99% of submissions at 36 ms
        
                
                