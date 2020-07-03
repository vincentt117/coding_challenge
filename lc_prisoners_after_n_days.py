# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/
# Optimal solution
# Used solutions
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0:
            return cells
        repeat = {}
        for i in range(1, 15):
            new = [0] * 8
            for j in range(1, 7):
                if cells[j - 1] == cells[j + 1]:
                    new[j] = 1 
            cells = new
            repeat[i if i != 14 else 0] = cells
        return repeat[N % 14]