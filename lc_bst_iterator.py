# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.storage = self.iter(root)
    
    def iter(self, root):
        if not root:
            return []
        ret = []
        if root.right:
            ret += self.iter(root.right)
        ret += [root.val]
        if root.left:
            ret += self.iter(root.left)
        return ret
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.storage:
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.storage.pop()
        else:
            return None
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


# Faster than 55% of submissions at 50ms