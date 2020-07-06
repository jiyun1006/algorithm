import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
line = [0] * N
for i in reversed(range(N)):
    line.insert(p[i], i + 1)
    line.remove(0)

for i in range(N):
    print(line[i], end=' ')
