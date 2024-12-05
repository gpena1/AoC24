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

def correct(sequence):
    for i in range(len(sequence)-1):
        for j in range(i+1, len(sequence)):
            if sequence[i] in G[sequence[j]]:
                sequence[i],sequence[j] = sequence[j], sequence[i]
    if not valid(sequence):
        correct(sequence)

ans = 0
for line in file:
    line = line.strip()
    numbers = list(map(int,line.split(',')))
    if valid(numbers): continue
    correct(numbers)
    ans += numbers[len(numbers)//2]

print(ans)