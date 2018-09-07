# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowSet = set()
        columnSet = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if not matrix[r][c]:
                    rowSet.add(r)
                    columnSet.add(c)
        for i in rowSet:
            matrix[i] = [0] * len(matrix[i])
        for j in columnSet:
            for m in range(len(matrix)):
                matrix[m][j] = 0
    
# Fast at 88ms & faster than 96% of accepted submissions