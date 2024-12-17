from re import fullmatch
from aocinput import AOCInput
from heapq import heappush, heappop
from collections import defaultdict
input = AOCInput(2024, 13)
button = r'Button (.): X\+(\d+), Y\+(\d+)'
prize = r'Prize: X=(\d+), Y=(\d+)'
machine_info = [[]]
for line in input.lines():
    if not line: continue
    if (fm := fullmatch(button, line)):
        button_type, x, y = fm.groups()
        x,y = int(x),int(y)
        machine_info[-1].append([x,y])
    elif (fm := fullmatch(prize, line)):
        x,y = fm.groups()
        x,y = int(x),int(y)
        machine_info[-1].append([x,y])
        machine_info.append([])
machine_info.pop()

least = []
for A,B,prize in machine_info:
    cost = defaultdict(lambda: float('inf'))
    dx_A, dy_A = A
    dx_B, dy_B = B
    fx,fy = prize
    hq = []
    cost[0,0] = 0
    heappush(hq, (0,0,0))
    while hq:
        c,x,y = heappop(hq)
        if x > fx: continue
        if y > fy: continue
        if cost[x,y] < c: continue
        x2,y2 = x+dx_A, y+dy_A
        if c + 3 < cost[x2,y2]:
            cost[x2,y2] = c+3
            heappush(hq, (cost[x2,y2],x2,y2))

        x2,y2 = x+dx_B, y+dy_B
        if c + 1 < cost[x2,y2]:
            cost[x2,y2] = c+1
            heappush(hq, (cost[x2,y2],x2,y2))

    least.append(cost[fx,fy])

ans = 0
for l in least:
    if l == float('inf'): continue
    ans += l
print(ans)