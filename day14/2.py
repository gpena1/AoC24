from re import fullmatch
from aocinput import AOCInput
from functools import reduce
input = AOCInput(2024, 14)
robot = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
positions = []
velocities = []

for line in input.lines():
    x,y,dx,dy = map(int,fullmatch(robot, line).groups())
    positions.append([y,x])
    velocities.append([dy,dx])


second = 0
while True:
    second += 1
    grid = [['.' for j in range(101)] for i in range(103)]
    for i in range(len(positions)):
        positions[i][0] += velocities[i][0]
        positions[i][1] += velocities[i][1]
        positions[i][0] %= 103
        positions[i][1] %= 101
        grid[positions[i][0]][positions[i][1]] = 'X'

    longest_streak = 0
    for i in range(len(grid)):
        current_streak = 0
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 0

    if longest_streak > 20:
        print(second)
        print('\n'.join(''.join(row) for row in grid))
        break