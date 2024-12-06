file = open('../input','r')
board = []
for line in file:
    line = line.strip()
    board.append(line)

x,y = -1,-1
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '^':
            x,y = i,j

d = [[-1,0],[0,1],[1,0],[0,-1]]
k = 0
v = [[False for j in range(len(board[0]))] for i in range(len(board))]
while True:
    v[x][y] = True
    a,b = d[k]
    x2,y2 = x+a, y+b
    if not (0 <= x2 < len(board) and 0 <= y2 < len(board[x2])): break
    if board[x2][y2] == '#':
        k = (k + 1) % 4
        continue
    x,y=x2,y2

print(sum(sum(j for j in i) for i in v))