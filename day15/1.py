from aocinput import AOCInput
input = AOCInput(2024, 15)
board = []
it = input.lines()
while (k:=next(it)) != '':
    board.append(list(k))

rx,ry = 0,0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '@':
            rx,ry = i,j

robot_moves = []
while (k:=next(it, '')):
    robot_moves.append(k)

robot_moves = ''.join(robot_moves)
d = {
    '^': [-1,0],
    'v': [1,0],
    '<': [0,-1],
    '>': [0,1]
}

for move in robot_moves:
    a,b = d[move]
    x2,y2 = rx+a,ry+b
    while 0 <= x2 < len(board) and 0 <= y2 < len(board[x2]) and board[x2][y2] == 'O':
        x2,y2 = x2+a,y2+b

    if board[x2][y2] == '#': continue
    while (x2,y2) != (rx,ry):
        t = board[x2][y2]
        board[x2][y2] = board[x2-a][y2-b]
        board[x2-a][y2-b] = t
        x2 -= a
        y2 -= b
    rx += a
    ry += b

ans = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != 'O': continue
        ans += i * 100 + j

print(ans)