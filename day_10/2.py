from functools import cache
from collections import deque
from aocinput import AOCInput

input = AOCInput(2024, 10, True)
d = [[-1,0],[1,0],[0,-1],[0,1]]
board = []

for line in input.lines():
    board.append(line)

def bfs(i,j):

    @cache
    def solve(x,y):
        if board[x][y] == '9': return 1
        ways = 0
        for a,b in d:
            x2,y2 = x+a,y+b
            if not (0 <= x2 < len(board) and 0 <= y2 < len(board[x2])): continue
            if int(board[x2][y2]) != int(board[x][y]) + 1: continue
            ways += solve(x2,y2)
        return ways

    return solve(i,j)

rating_sum = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != '0': continue
        rating_sum += bfs(i,j)

print(rating_sum)