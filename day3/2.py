from re import split, findall

def eval(s):
    groups = findall(r'mul\((\d+),(\d+)\)', s)
    return sum(int(a) * int(b) for a,b in groups)

execute = True
def process(line):
    global execute
    groups = split(r"(do\(\)|don't\(\))", line)
    ans = 0
    for g in groups:
        if g == "do()":
            execute = True
            continue
        if g == "don't()":
            execute = False
            continue

        if not execute: continue
        ans += eval(g)
    return ans


file = open('input.in', 'r')
ans = 0
for line in file:
    line = line.strip()
    ans += process(line)
print(ans)