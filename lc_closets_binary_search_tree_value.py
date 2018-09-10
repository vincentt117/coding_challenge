# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def closestValue(self, root, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    if not root:
        return None
    
    node = root
    diff = float('inf')
    closets = root.val
    while node:
        if abs(node.val - target) < diff:
            closets = node.val
            diff = abs(node.val - target) 
        
        if abs(node.val - target) <= 0.5:
            return node.val
        elif abs(node.val - target) > 0.5 and node.val > target:
            node = node.left
        else:
            print(diff)
            print(closets)
            node = node.right
    
    return closets
                
        