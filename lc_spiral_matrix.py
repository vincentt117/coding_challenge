# https://leetcode.com/problems/spiral-matrix/description/

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
        return matrix
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)
    ret = []
    while len(ret) < len(matrix[0]) * len(matrix):
        print(ret)
        # left to right
        if len(ret) < len(matrix[0]) * len(matrix):
            ret += [matrix[top][i] for i in range(left, right)]
        print(ret)
        # top to bottom
        if len(ret) < len(matrix[0]) * len(matrix):
            ret += [matrix[j][right - 1] for j in range(top + 1, bottom)]
        print(ret)
        # right to left
        if len(ret) < len(matrix[0]) * len(matrix):
            ret += [matrix[bottom - 1][k] for k in range(right - 2, left - 1, -1)]
        # bottom to top
        if len(ret) < len(matrix[0]) * len(matrix):
            ret += [matrix[l][left] for l in range(bottom - 2, top, -1)]
        
        # Move to inner
        left += 1
        right -= 1
        bottom -= 1
        top += 1
    return ret
# Faster than 31% of submissions. Range of accepted submissions between 20ms to 50ms