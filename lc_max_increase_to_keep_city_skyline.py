# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

def maxIncreaseKeepingSkyline(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    maxInColumn = [] #Top to bottom skyline
    maxInRow = [] # Left to right skyline
    for i in range(len(grid[0])):
        maxInColumn.append(max([v[i] for v in grid]))
    for j in grid:
        maxInRow.append(max(j))
        
    heightInc = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if min(maxInColumn[x], maxInRow[y]) > grid[y][x]:
                heightInc += min(maxInColumn[x], maxInRow[y]) - grid[y][x]
                grid[y][x] = min(maxInColumn[x], maxInRow[y])
            
    return heightInc

# Faster than 54% of accepted submissions at 60ms
    