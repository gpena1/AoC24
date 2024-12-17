from collections import defaultdict, deque
from aocinput import AOCInput

input = AOCInput(2024, 12)
board = []
for line in input.lines():
    board.append(line)

d = [[-1,0],[1,0],[0,-1],[0,1]]
v = [[False for j in range(len(board[i]))] for i in range(len(board))]
ans = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if v[i][j]: continue
        perimeter = 0
        area = 0
        dq = deque()
        dq.append((i,j))
        v[i][j] = True
        while dq:
            x,y = dq.popleft()
            area += 1
            # check if it's a perimeter cell
            for a,b in d:
                if not(0 <= x+a < len(board) and 0 <= y+b < len(board[0])):
                    perimeter += 1
                    continue
                if board[x+a][y+b] != board[x][y]:
                    perimeter += 1
                    continue

            for a,b in d:
                x2,y2 = x+a,y+b
                if not (0 <= x2 < len(board) and 0 <= y2 < len(board[x2])): continue
                if board[x2][y2] != board[x][y]: continue
                if v[x2][y2]: continue
                v[x2][y2] = True
                dq.append((x2,y2))
        ans += perimeter * area

print(ans)