from collections import defaultdict
file = open('input.in','r')
G = defaultdict(set)
while (line:=file.readline().strip()) != '':
    a,b = map(int,line.split('|'))
    G[a].add(b)

ans = 0

def valid(sequence):
    for i in range(len(sequence)-1):
        for j in range(i+1, len(sequence)):
            if sequence[i] in G[sequence[j]]: return False

    return True

ans = 0
for line in file:
    line = line.strip()
    numbers = list(map(int,line.split(',')))
    if valid(numbers):
        ans += numbers[len(numbers)//2]

print(ans)