import sys
import math

io = sys.stdin.readline

N, L = map(int, io().split())

water = [0] * N

for i in range(N):
    start, end = map(int, io().split())
    water[i] = (start, end)

water.sort()

ans = water[0][0]
cnt = 0
for value in water:
    if ans >= value[0]:
        cnt += math.ceil((value[1] - ans) / L)
        ans += L * math.ceil((value[1] - ans) / L)
    else:
        ans = value[0]
        cnt += math.ceil((value[1] - value[0]) / L)
        ans += L * math.ceil((value[1] - value[0]) / L)

print(cnt)
