from aocinput import AOCInput

input = AOCInput(2024, 9, True)
for line in input.lines():
    digits = line

id = 0
diskmap = []
for i in range(0,len(digits),2):
    diskmap.extend([str(id)] * int(digits[i]))
    if i+1 < len(digits):
        diskmap.extend(['.'] * int(digits[i+1]))
    id += 1

not_filled = []
for i,j in enumerate(diskmap):
    if j == '.':
        not_filled.append(i)

not_filled = not_filled[::-1]
for i in range(len(diskmap)-1,-1,-1):
    if not not_filled or not_filled[-1] >= i: break
    if diskmap[i] != '.':
        diskmap[i],diskmap[not_filled[-1]] = diskmap[not_filled[-1]],diskmap[i]
        not_filled.pop()

print(sum( int(diskmap[i]) * i for i in range(len(diskmap)) if diskmap[i] != '.'))