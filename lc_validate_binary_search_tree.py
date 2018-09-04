# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            store = self.isValidBSTHelper(root)
            return store and root.val >= store[0] and root.val <= store[1]
       
    def isValidBSTHelper(self, root):
        if not root:
            return None
        left = self.isValidBSTHelper(root.left)
        right = self.isValidBSTHelper(root.right)
        ret = [root.val, root.val]
        if left and root.val > left[0] and root.val > left[1]:
            ret[0] = left[0]
        elif left != None:
            return False
        if right and root.val < right[0] and root.val < right[1]:
            ret[1] = right[1]
        elif right != None:
            return False
        return ret
    # Faster than 57% of solutions


    def isValidBSTCondensed(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBSTCondensed(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBSTCondensed(root.right, lessThan, max(root.val, largerThan))
    # Faster than ~90% of solutions, found in discussions

            
