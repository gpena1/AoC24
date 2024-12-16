from heapq import heappush, heappop
from aocinput import AOCInput
input = AOCInput(2024, 16)
board = []
sx,sy = -1,-1
ex,ey = -1,-1
for line in input.lines():
    board.append(line)


directions = [[0,1],[1,0],[0,-1],[-1,0]]
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'S':
            sx,sy = i,j
        if board[i][j] == 'E':
            ex,ey = i,j

cost = [[[float('inf') for k in range(4)] for j in range(len(board[i]))] for i in range(len(board))]

cost[sx][sy][0] = 0
hq = []
heappush(hq, (0, sx, sy, 0))
while hq:
    score, x, y, direction = heappop(hq)
    a,b = directions[direction]
    if score > cost[x][y][direction]: continue
    # Move in current direction
    nx,ny = x+a,y+b
    if board[nx][ny] != '#' and 1 + score < cost[nx][ny][direction]:
        cost[nx][ny][direction] = 1 + score
        heappush(hq, (cost[nx][ny][direction], nx, ny, direction))

    # Change direction
    for k in [-1,1]:
        new_dir = (direction + k) % 4
        if 1000 + score < cost[x][y][new_dir]:
            cost[x][y][new_dir] = 1000 + score
            heappush(hq, (cost[x][y][new_dir], x, y, new_dir))


print(min(cost[ex][ey][d] for d in range(4)))