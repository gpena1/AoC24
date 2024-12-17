import sys
from aocinput import AOCInput
sys.setrecursionlimit(10**9)
input = AOCInput(2024, 15)
board = []
it = input.lines()
charmap = {
    '#': '##',
    'O': '[]',
    '.': '..',
    '@': '@.'
}
while (k:=next(it)) != '':
    board.append([])
    for c in k:
        board[-1].extend(list(charmap[c]))


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

    if a == 0:
        x2, y2 = rx + a, ry + b
        while 0 <= x2 < len(board) and 0 <= y2 < len(board[x2]) and board[x2][y2] in '[]':
            x2, y2 = x2 + a, y2 + b
        if board[x2][y2] == '#': continue
        while (x2,y2) != (rx,ry):
            t = board[x2][y2]
            board[x2][y2] = board[x2-a][y2-b]
            board[x2-a][y2-b] = t
            x2 -= a
            y2 -= b
        rx += a
        ry += b
    else:
        if board[rx+a][ry+b] == '.':
            t = board[rx+a][ry+b]
            board[rx+a][ry+b] = board[rx][ry]
            board[rx][ry] = t
            rx += a
            ry += b
            continue
        if board[rx+a][ry+b] == '#':
            continue

        will_be_moved = set()
        def visit(i,j):
            if (i,j) in will_be_moved: return True
            will_be_moved.add((i, j))
            if board[i][j] == '[':
                visit(i,j+1)
            elif board[i][j] == ']':
                visit(i,j-1)
            if board[i+a][j+b] in '[]':
                visit(i+a,j+b)

        visit(rx+a,ry+b)
        if any(board[i+a][j+b] == '#' for i,j in will_be_moved): continue
        cells = sorted(will_be_moved, key=lambda k: k[0] * (-1 if a == 1 else 1))
        for i,j in cells:
            t = board[i+a][j+b]
            board[i+a][j+b] = board[i][j]
            board[i][j] = t
        t = board[rx][ry]
        board[rx][ry] = board[rx+a][ry+b]
        board[rx+a][ry+b] = t
        rx += a
        ry += b



print('\n'.join(''.join(row) for row in board))
ans = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != '[': continue
        ans += i * 100 + j

print(ans)