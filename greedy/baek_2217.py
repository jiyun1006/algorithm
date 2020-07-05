import sys

N = int(sys.stdin.readline())

rope = [int(sys.stdin.readline().strip()) for x in range(N)]
rope.sort()

target = []

for i in range(len(rope)):
    target.append(rope[i]*(len(rope)-i))

print(max(target))
