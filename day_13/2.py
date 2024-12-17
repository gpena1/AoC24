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

ans = 0
for A,B,prize in machine_info:
    cost = defaultdict(lambda: float('inf'))
    dx_A, dy_A = A
    dx_B, dy_B = B
    fx,fy = prize
    fx += 10000000000000; fy += 10000000000000
    det = dx_A * dy_B - dx_B * dy_A
    if det == 0: continue
    if (dy_B * fx - dx_B *fy) % det != 0: continue
    A_presses = (dy_B * fx - dx_B * fy) // det
    if (-dy_A * fx + dx_A * fy) % det != 0: continue
    B_presses = (-dy_A * fx + dx_A * fy) // det
    ans += 3 * A_presses + B_presses

print(ans)