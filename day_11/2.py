from functools import cache
from aocinput import AOCInput


input = AOCInput(2024, 11)
for line in input.lines():
    stones = list(map(int, line.split()))

@cache
def dp(n, blinks_remaining):
    if blinks_remaining == 0: return 1
    if n == 0: return dp(1, blinks_remaining - 1)
    if not len(k := str(n)) & 1:
        left = int(k[:len(k)//2])
        right = int(k[len(k)//2:])
        return dp(left, blinks_remaining-1) + dp(right, blinks_remaining-1)

    return dp(n * 2024, blinks_remaining-1)

print(sum(dp(i,75) for i in stones))