# https://leetcode.com/problems/game-of-life/description/

def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    nextState = {}
    
    for rowNum, row in enumerate(board):
        for columnNum, cell in enumerate(board[rowNum]):
            liveNeighbours = 0
            # Circle around the cell and get values of all its neighbours
            for i in range (-1, 2):
                for j in range(-1, 2):
                    if 0 <= rowNum + i < len(board) and 0 <= columnNum + j < len(board[rowNum]) and not (i == 0 and j == 0) and board[rowNum + i][columnNum + j]:
                        liveNeighbours += 1             
            # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
            if cell and liveNeighbours < 2:
                nextState[tuple([rowNum, columnNum])] = 0
            # Any live cell with two or three live neighbors lives on to the next generation.
            elif cell and 2 <= liveNeighbours <= 3:
                nextState[tuple([rowNum, columnNum])] = 1
            # Any live cell with more than three live neighbors dies, as if by over-population.
            elif cell and 3 < liveNeighbours:
                nextState[tuple([rowNum, columnNum])] = 0
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            elif not cell and liveNeighbours == 3:
                nextState[tuple([rowNum, columnNum])] = 1
            else:
                nextState[tuple([rowNum, columnNum])] = board[rowNum][columnNum]
    for k in nextState:
        board[k[0]][k[1]] = nextState[k]

# Faster than 50% of accepted submissions at 40ms