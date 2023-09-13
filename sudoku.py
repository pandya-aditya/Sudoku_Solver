
from random import randint
import time

bo = [
    [0, 2, 0, 5, 0, 6, 0, 8, 0],
    [0, 6, 0, 0, 7, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 4],
    [7, 0, 0, 0, 0, 8, 9, 0, 2],
    [4, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 2, 9, 0, 0, 0, 0, 3],
    [2, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 5, 0, 0, 1, 0],
    [0, 1, 0, 8, 0, 4, 0, 2, 0]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if(check_valid(board, i, (row, col))):
            board[row][col] = i
        
            if(solve(board)):
                return True
            
            board[row][col] = 0
    
    return False

def find_empty(board):
    pos = ()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                pos = (i, j)
    return pos

def check_valid(bo, num, pos):
    
# Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(board):
    for i in range(len(board)):
        print("\n", board[i])
    print("////////////////////////////")

solve(bo)
print_board(bo)

