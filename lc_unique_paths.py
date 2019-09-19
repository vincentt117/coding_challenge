# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        # Build map
        grid = [[0] * (m - 1) + [1] for i in range(n - 1)] # Can just do entire grid of ones instead
        grid.append([1] * m)
        print(grid)
        for y in range(n - 2, -1, -1):
            for x in range(m - 2, -1, -1):
                grid[y][x] = grid[y + 1][x] + grid[y][x + 1]
        return grid[0][0]
                