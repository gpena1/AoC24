from aocinput import AOCInput

input = AOCInput(2024, 9, True)
for line in input.lines():
    digits = line

id = 0
diskmap = []
freespace = []
positions = []
for i in range(0,len(digits),2):
    positions.append([len(diskmap), int(digits[i])])
    diskmap.extend([str(id)] * int(digits[i]))
    if i+1 < len(digits):
        freespace.append([len(diskmap), int(digits[i+1])])
        diskmap.extend(['.'] * int(digits[i+1]))
    id += 1
freespace.pop()
freespace = freespace[::-1]

for a,b in positions[::-1]:
    if not freespace: break
    i = len(freespace)-1
    while i >= 0 and freespace[i][0] < a and freespace[i][1] < b:
        i -= 1

    if i == -1 or freespace[i][0] > a:
        continue

    x,y = a, freespace[i][0]
    for k in range(b):
        diskmap[x],diskmap[y] = diskmap[y],diskmap[x]
        x += 1
        y += 1
    freespace[i] = [y, freespace[i][1] - b]
    if not freespace[i][1]:
        freespace.pop(i)


print(sum( int(diskmap[i]) * i for i in range(len(diskmap)) if diskmap[i] != '.' ))