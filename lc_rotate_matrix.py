class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left_top = 0
        right_bot = len(matrix) - 1
        while left_top < right_bot:
            top = matrix[left_top][left_top + 1:right_bot]
            left = [matrix[i][left_top] for i in range(right_bot, left_top - 1, -1)]
            bot = matrix[right_bot][left_top + 1:right_bot]
            right = [matrix[i][right_bot] for i in range(right_bot, left_top - 1, -1)]
            
            
            matrix[left_top][left_top:right_bot + 1] = left
            matrix[right_bot][left_top:right_bot + 1] = right
            idx = 0
            for y in range(left_top + 1, right_bot):
                matrix[y][left_top] = bot[idx]
                matrix[y][right_bot] = top[idx]
                idx += 1
            left_top += 1
            right_bot -= 1
        return matrix
    
# 200 IQ solution
# Flip matrix upside down and zip to transpose
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
            
            
        
        