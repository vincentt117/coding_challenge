# https://leetcode.com/problems/friend-circles/ 
class Solution:
    def findCircleNum(self, M) -> int:
        circle_count = 0
        seen = set()
        
        def dfs(i):
            nonlocal dfs_visited
            dfs_visited.add(i)
            seen.add(i)
            for idx in range(len(M[i])):
                if not idx in seen and not idx in dfs_visited and M[i][idx]:
                    dfs(idx)
        
        for idx in range(len(M)):
            if not idx in seen:
                dfs_visited = set()
                circle_count += 1
                dfs(idx)
        print(circle_count)
        return circle_count