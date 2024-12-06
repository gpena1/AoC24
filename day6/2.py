file = open('../input','r')
board = []
d = [[-1,0],[0,1],[1,0],[0,-1]]
for line in file:
    line = line.strip()
    board.append([c for c in line])

gx,gy = -1,-1
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '^':
            gx,gy = i,j

def test(ox,oy):
    if (ox,oy) == (gx,gy): return False
    board[ox][oy] = '#'
    v = set()
    x,y = gx,gy
    k = 0
    while 0 <= x < len(board) and 0 <= y < len(board[x]) and (x,y,k) not in v:
        v.add((x,y,k))
        a,b = d[k]
        x2,y2 = x+a,y+b
        if not (0 <= x2 < len(board) and 0 <= y2 < len(board[x2])):
            x,y=x2,y2
            break
        if board[x2][y2] == '#':
            k = (k+1) % 4
            continue
        x,y=x2,y2
    board[ox][oy] = '.'
    return (x,y,k) in v

k = 0
x,y = gx,gy
ans = set()
while True:
    if test(x,y):
        ans.add((x,y))
    a, b = d[k]
    x2, y2 = x + a, y + b
    if not (0 <= x2 < len(board) and 0 <= y2 < len(board[x2])): break
    if board[x2][y2] == '#':
        k = (k + 1) % 4
        continue
    x, y = x2, y2

print(len(ans))