# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.LCAHelper(root, p, q)[0]

    
    def LCAHelper(self, root, p, q):
        if not root:
            return [None, False, False]
        
        ret = [None, root.val == p.val, root.val == q.val]
            
        leftSide = self.LCAHelper(root.left, p, q)
        rightSide = self.LCAHelper(root.right, p, q)
        
        ret[1], ret[2] = ret[1] or leftSide[1] or rightSide[1], ret[2] or leftSide[2] or rightSide[2]

        if ret[1] and ret[2]:
            checkDict = {}
            if leftSide[0]:
                checkDict[leftSide[0].val] = leftSide[0]
            if rightSide[0]:
                checkDict[rightSide[0].val] = rightSide[0]
            if ret[0]:
                checkDict[ret[0].val] =ret[0]
            if not checkDict.keys():
                ret[0] = root
            else:
                ret[0] = checkDict[min(checkDict.keys())]

        return ret
# Solution faster than 14% of submissions

    def lowestCommonAncestor1(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor1(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right
# Found in discussion
        