# https://leetcode.com/problems/island-perimeter/
# Sub-optimal

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def bfs():
            for node in self.curr_d:
                check(-1, 0, node[0], node[1])
                check(0, 1, node[0], node[1])
                check(1, 0, node[0], node[1])
                check(0, -1, node[0], node[1])
            self.curr_d, self.next_d = self.next_d, []
            if self.curr_d != []:
                bfs()
        
        def check(v, h, y, x):
            new_y = y + v
            new_x = x + h
            new_coord = tuple([new_y, new_x])
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] == 1:
                if not new_coord in self.seen:
                    self.seen.add(new_coord)
                    self.next_d.append(new_coord)
            else:
                self.perim += 1
                # print([y, x], new_coord)
            
        
        self.perim = 0
        self.curr_d = []
        self.next_d = []
        self.seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.seen.add(tuple([i, j]))
                    self.curr_d.append(tuple([i, j]))
                    bfs()
                    return self.perim
        return self.perim

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        
        return result
    
        