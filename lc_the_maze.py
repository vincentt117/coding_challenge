# https://leetcode.com/problems/the-maze/
# Optimal

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(coord, y_delta, x_delta):
            if self.found: return
            
            # Check if this trajectory at this location has been attempted, if it has, return
            # else record and continue
            if (coord[0], coord[1], y_delta, x_delta) in self.done_path:
                return
            else:
                self.done_path.add((coord[0], coord[1], y_delta, x_delta))
                
            # If we're on a wall return
            if coord[0] < 0 or len(maze) == coord[0] or coord[1] < 0 or len(maze[0]) == coord[1] or maze[coord[0]][coord[1]]:
                return
            
            new_loc = [coord[0] + y_delta, coord[1] + x_delta]
            if new_loc[0] < 0 or len(maze) == new_loc[0] or new_loc[1] < 0 or len(maze[0]) == new_loc[1] or maze[new_loc[0]][new_loc[1]]: # Will hit wall on next move
                # Try all pathes not yet done, record those we can try
                if coord == destination:
                    self.found = True
                    return
                opts = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for opt in opts:
                    coord_opt = [coord[0] + opt[0], coord[1] + opt[1]]
                    if not (coord_opt[0], coord_opt[1], opt[0], opt[1]) in self.done_path:
                        dfs(coord_opt, opt[0], opt[1])
                
            else: # Haven't reach wall yet, continue travel
                dfs(new_loc, y_delta, x_delta)
                
        self.done_path = set()
        self.found = False
        
        dfs(start, 1, 0)
        dfs(start, -1, 0)
        dfs(start, 0, 1)
        dfs(start, 0, -1)
        return self.found