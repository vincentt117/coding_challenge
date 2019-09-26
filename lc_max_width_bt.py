class Solution:    
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        depth_extreme = []
        self.max_width = 0
        def dfs(root, depth=0, displacement=1):
            if len(depth_extreme) <= depth:
                depth_extreme.append([float("inf"), float("-inf")])
            depth_extreme[depth][0] = min(depth_extreme[depth][0], displacement)
            depth_extreme[depth][1] = max(depth_extreme[depth][1], displacement)
            self.max_width = max(self.max_width, depth_extreme[depth][1] - depth_extreme[depth][0] + 1)
            if root.left:
                dfs(root.left, depth+1, 2 * displacement - 1)
            if root.right:
                dfs(root.right, depth+1, 2 * displacement)
        dfs(root)
        return self.max_width