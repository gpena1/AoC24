from collections import defaultdict
file = open('../input','r')
board = []
locations = defaultdict(list)
for line in file:
    line = line.strip()
    board.append(line)

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '.': continue
        locations[board[i][j]].append((i,j))

unique_locations = set()
def count(frequency):
    global unique_locations
    l = locations[frequency]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            x1,y1 = l[i]
            x2,y2 = l[j]
            v1 = (x2-x1,y2-y1)
            v2 = (x1-x2,y1-y2)
            x3,y3 = x1,y1
            while 0 <= x3 < len(board) and 0 <= y3 < len(board[x3]):
                # use v1 here
                unique_locations.add((x3,y3))
                x3 += v1[0]
                y3 += v1[1]
            x3,y3 = x2,y2
            while 0 <= x3 < len(board) and 0 <= y3 < len(board[x3]):
                # use v2 here
                unique_locations.add((x3,y3))
                x3 += v2[0]
                y3 += v2[1]

for f in locations.keys():
    count(f)

print(len(unique_locations))