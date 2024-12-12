from collections import defaultdict, deque
from aocinput import AOCInput

input = AOCInput(2024, 12)
board = []
for line in input.lines():
    board.append(line)

horizontal_lines = [[-1,0],[1,0]]
vertical_lines = [[0,-1],[0,1]]
d = horizontal_lines + vertical_lines
v = [[False for j in range(len(board[i]))] for i in range(len(board))]
ans = 0
for t in range(len(board)):
    for u in range(len(board[t])):
        if v[t][u]: continue
        area = 0
        # keys for vertical will be columns
        # values will bet sets containing row numbers
        vertical = defaultdict(set)
        # keys for horizontal will be rows
        # values will be sets containing column numbers
        horizontal = defaultdict(set)
        dq = deque()
        dq.append((t,u))
        v[t][u] = True
        while dq:
            x,y = dq.popleft()
            area += 1
            for a,b in horizontal_lines:
                if not 0 <= x+a < len(board) or board[x+a][y] != board[x][y]:
                    horizontal[x+a+(a<0)].add((a<0, y))

            for a,b in vertical_lines:
                if not 0 <= y+b < len(board[0]) or board[x][y+b] != board[x][y]:
                    vertical[y+b+(b<0)].add((b<0, x))

            for a,b in d:
                x2,y2 = x+a,y+b
                if not (0 <= x2 < len(board) and 0 <= y2 < len(board[x2])): continue
                if board[x2][y2] != board[x][y]: continue
                if v[x2][y2]: continue
                v[x2][y2] = True
                dq.append((x2,y2))

        perimeter = 0
        for col in vertical.keys():
            rows = sorted(vertical[col])
            i = 0
            while i < len(rows):
                j = i+1
                while j < len(rows) and rows[j][1] == rows[j-1][1] + 1 and rows[j][0] == rows[j-1][0]:
                    j += 1
                perimeter += 1
                i = j
        for row in horizontal.keys():
            cols = sorted(horizontal[row])
            i = 0
            while i < len(cols):
                j = i+1
                while j < len(cols) and cols[j][1] == cols[j-1][1] + 1 and cols[j][0] == cols[j-1][0]:
                    j += 1
                perimeter += 1
                i = j
        ans += area * perimeter


print(ans)