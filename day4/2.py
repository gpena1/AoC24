wordsearch = []
file = open('input.in','r')
for line in file:
    line = line.strip()
    wordsearch.append(line)

desired = 'MAS'
def match(i,j,dx,dy):
    k = 0
    while 0 <= i < len(wordsearch) and 0 <= j < len(wordsearch[i]) \
        and k < 3 and wordsearch[i][j] == desired[k]:
        i += dx
        j += dy
        k += 1

    return k >= 3

def valid(i,j):
    return (match(i+2,j,-1,1) or match(i,j+2,1,-1)) \
            and (match(i,j,1,1) or match(i+2,j+2,-1,-1))

c = 0
for i in range(len(wordsearch)-2):
    for j in range(len(wordsearch[i])-2):
        c += valid(i,j)
print(c)