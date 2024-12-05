f = open('input.in','r')
def safe(levels):
    n = len(levels)
    for i in range(n):
        temp_levels = levels[:i] + levels[i+1:]
        diff = [temp_levels[k+1] - temp_levels[k] for k in range(n-2)]
        safe = all(d < 0 for d in diff) or all(d > 0 for d in diff)
        safe = safe and all(1 <= abs(d) <= 3 for d in diff)
        if safe: return True
    return False

c = 0
for line in f:
    line = line.strip()
    levels = list(map(int, line.split()))
    c += safe(levels)

print(c)