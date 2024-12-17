from collections import deque
from aocinput import AOCInput

input = AOCInput(2024, 10, True)
d = [[-1,0],[1,0],[0,-1],[0,1]]
board = []
for line in input.lines():
    board.append(line)

def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    visited = set()
    score = 0
    while dq:
        x1,y1 = dq.popleft()
        score += board[x1][y1] == '9'
        for a,b in d:
            x2,y2 = x1+a,y1+b
            if not (0 <= x2 < len(board) and 0 <= y2 < len(board[x2])): continue
            if (x2,y2) in visited: continue
            if int(board[x2][y2]) != int(board[x1][y1]) + 1: continue
            visited.add((x2,y2))
            dq.append((x2,y2))
    return score

score_sum = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != '0': continue
        score_sum += bfs(i,j)

print(score_sum)