# https://leetcode.com/problems/word-search/

# Optimal
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, rem):
            if len(rem) == 0:
                return True
            if 0 <= i - 1 and board[i-1][j] == rem[0] and not (i - 1, j) in dive_set:
                    dive_set.add((i-1, j))
                    if dfs(i - 1, j, rem[1:]): return True
                    else: dive_set.remove((i-1, j))
            if 0 <= j - 1 and board[i][j - 1] == rem[0] and not (i, j - 1) in dive_set:
                    dive_set.add((i, j - 1))
                    if dfs(i, j - 1, rem[1:]): return True
                    else: dive_set.remove((i, j - 1))
            if i + 1 < len(board) and board[i+1][j] == rem[0] and not (i + 1, j) in dive_set:
                    dive_set.add((i+1, j))
                    if dfs(i + 1, j, rem[1:]): return True
                    else: dive_set.remove((i+1, j))
            if j+1 < len(board[0]) and board[i][j + 1] == rem[0] and not (i, j + 1) in dive_set:
                    dive_set.add((i, j + 1))
                    if dfs(i, j + 1, rem[1:]): return True
                    else: dive_set.remove((i, j + 1))
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dive_set = set() 
                    dive_set.add((i, j))
                    if dfs(i, j, word[1:]): return True
        return False
        
        