from collections import Counter
file = open('../input','r')
arr = []
c = Counter()
for line in file:
    line = line.strip()
    a,b = map(int,line.split())
    arr.append(a); c[b] += 1

print(sum(k * c[k] for k in arr))