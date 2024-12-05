wordsearch = []
file = open('input.in','r')
for line in file:
    line = line.strip()
    wordsearch.append(line)

desired = 'XMAS'

def match(i,j,dx,dy):
    k = 0
    while 0 <= i < len(wordsearch) and 0 <= j < len(wordsearch[i]) \
        and k < 4 and wordsearch[i][j] == desired[k]:
        i += dx
        j += dy
        k += 1

    return k >= 4

d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

c = 0
for i in range(len(wordsearch)):
    for j in range(len(wordsearch[i])):
        for a,b in d:
            c += match(i,j,a,b)

print(c)