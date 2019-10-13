# https://leetcode.com/problems/binary-tree-paths/

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        def dfs(root, path):
            if not root.left and not root.right:
                self.res.append(path + str(root.val))
                return
            if root.left:
                dfs(root.left, path + str(root.val) + "->")
            if root.right:
                dfs(root.right, path + str(root.val) + "->")
        if root:
            dfs(root, "")
        return self.res