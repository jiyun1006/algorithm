import sys
import heapq

io = sys.stdin.readline

N = int(io())
f = [0] * N
heap = []
cnt = 0

for i in range(N):
    a, b = map(int, io().split())
    f[i] = (a, b)

f.sort()

L, P = map(int, io().split())

for i in range(len(f)):
    while P < f[i][0]:
        if not heap:
            cnt = -1
            break
        P += heapq.heappop(heap)[1]
        cnt += 1
    if cnt == -1:
        break
    heapq.heappush(heap, (-f[i][1], f[i][1]))
    
while P < L:
    if cnt == -1:
        break
    if not heap:
        cnt = -1
        break
    P += heapq.heappop(heap)[1]
    cnt += 1

print(cnt)
