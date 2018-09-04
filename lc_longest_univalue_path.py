# https://leetcode.com/explore/interview/card/google/67/sql-2/473/

def longestUnivaluePath(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # Time: O(n)
    # Space: O(n)
    longest = [0]
    def traverse(node):
        if not node:
            return 0
        left_len, right_len = traverse(node.left), traverse(node.right)
        left = (left_len + 1) if node.left and node.left.val == node.val else 0 # Determine length of left side
        right = (right_len + 1) if node.right and node.right.val == node.val else 0 # Determin length of right side
        longest[0] = max(longest[0], left + right) # Check if curved path is bigger longer than the previous record
        return max(left, right) # Continue with the longer of the two paths (supposing calling node had the same value)
    traverse(root)
    return longest[0]

# Solution found in discussion