# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        root1Leaf = []
        root2Leaf = []
        
        nodeStack = [] 
        nodeStack.append(root1) 
  
        while nodeStack: 
            node = nodeStack.pop() 
            if node.right: 
                nodeStack.append(node.right) 
            if node.left: 
                nodeStack.append(node.left)
            if not node.left and not node.right:
                root1Leaf.append(node.val)
        
        nodeStack = [root2]
        while nodeStack: 
            node = nodeStack.pop() 
            if node.right: 
                nodeStack.append(node.right) 
            if node.left: 
                nodeStack.append(node.left)
            if not node.left and not node.right:
                root2Leaf.append(node.val)
        
        return root1Leaf == root2Leaf
    
# Faster than 87% of accepted submissions at 24ms    
    

            
        