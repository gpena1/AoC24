f = open('input.in','r')
c = 0
for line in f:
    line = line.strip()
    levels = list(map(int, line.split()))
    diff = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    safe = all(d > 0 for d in diff) or all(d < 0 for d in diff)
    safe = safe and all(1 <= abs(d) <= 3 for d in diff)
    c += safe

print(c)