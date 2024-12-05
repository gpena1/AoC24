from re import findall
file = open('input.in', 'r')
s = 0
for line in file:
    line = line.strip()
    groups = findall(r'mul\((\d+),(\d+)\)', line)
    s += sum(int(a)*int(b) for a,b in groups)

print(s)