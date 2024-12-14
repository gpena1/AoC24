from re import fullmatch
from aocinput import AOCInput
from functools import reduce
input = AOCInput(2024, 14)
robot = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
c = [[0 for j in range(11)] for i in range(7)]
q = [0] * 4
def quadrant(r,c):
    if 0 <= r <= 50 and 0 <= c <= 49: return 0
    if 0 <= r <= 50 and 51 <= c <= 100: return 1
    if 52 <= r <= 102 and 0 <= c <= 49: return 2
    if 52 <= r <= 102 and 51 <= c <= 100: return 3

for line in input.lines():
    x,y,dx,dy = map(int,fullmatch(robot, line).groups())
    # print(x,y,dx,dy)
    fx,fy = x + dx * 100, y + dy * 100
    fx = fx % 101
    fy = fy % 103
    # c[fy][fx] += 1
    k = quadrant(fy,fx)
    if k is None: continue
    q[k] += 1


# print('\n'.join(''.join(map(str, row)) for row in c))
print(reduce(lambda a,b: a*b, q))