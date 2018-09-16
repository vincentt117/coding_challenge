# https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = [root]
        nextLevel = []
        maxWidth = 0
        if not root:
            return 0
        if not root.right and not root.left:
            return 1

        while set(level) != set([None]):
            leftMost = 0
            rightExtend = 0
            for node in level:
                if node:
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
                else:
                    nextLevel.append(None)
                    nextLevel.append(None)
                if not nextLevel[0] and not leftMost and nextLevel[-2]:
                    leftMost = len(nextLevel) - 1
                elif not nextLevel[0] and not leftMost and nextLevel[-1]:
                    leftMost = len(nextLevel)
                    
                if nextLevel[-2]:
                    rightExtend = len(nextLevel) - 1
                if nextLevel[-1]:
                    rightExtend = len(nextLevel)   
            if leftMost:
                rightExtend += 1
            maxWidth = max(maxWidth, rightExtend - leftMost)
            level = nextLevel
            nextLevel = []

    
        return maxWidth

# Passed 104/108 test cases, too slow for large trees


def widthOfBinaryTree(self, root):
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth+1, pos*2))
            queue.append((node.right, depth+1, pos*2 + 1))
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1, ans)

    return ans

# Found in solution