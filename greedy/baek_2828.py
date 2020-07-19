import sys


N, M = map(int, sys.stdin.readline().split())

j = int(sys.stdin.readline())
apple = [0] * j
for i in range(j):
    apple[i] = int(sys.stdin.readline())

start = 1
cnt = 0

for k in apple:
    if start <= k <= M:
        continue
    if start > k:
        cnt += start-k
        M -= start - k
        start = k
    else:
        cnt += k-M
        start += k-M
        M = k

print(cnt)