from re import match
from functools import cache
file = open('../input','r')

def possible(n, arr):

    def test(i, value):
        if i >= len(arr):
            return value == n
        return test(i+1, arr[i] * value) or test(i+1, arr[i] + value) or test(i+1, value * 10 ** len(str(arr[i])) + arr[i])

    return test(1, arr[0])

ans = 0
for line in file:
    line = line.strip()
    line = match(r'(\d+): (.+)', line)
    n = int(line.group(1))
    arr = list(map(int,line.group(2).split()))
    if possible(n,arr): ans += n

print(ans)