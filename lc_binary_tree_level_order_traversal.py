def levelOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        stack = [root]
        nextStack = []
        temp = []
        ret = []
        while stack:
            for i in stack:
                temp.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            ret.append(temp)
            temp = []
            stack = nextStack
            nextStack = []
        return ret
# Faster than ~40% of submissions

def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])            
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans
# Found in discussion: faster than ~99% of submissions