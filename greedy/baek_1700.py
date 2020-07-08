import sys

N, K = map(int, sys.stdin.readline().split())

hole = list(map(int, sys.stdin.readline().split()))

cnt = 0

if K <= N:
    cnt = 0
elif N == 1:
    holed = hole[0]
    for i in range(1, len(hole)):
        if holed == hole[i]:
            continue
        else:
            holed = hole[i]
            cnt += 1
else:
    stack = []
    for i in range(K):
        if hole[i] in stack:
            continue
        else:
            if len(stack) >= N:
                min_num = 0
                for j in stack:
                    if hole[i:].count(j) == 0:
                        value = j
                        break
                    elif min_num < hole[i:].index(j):
                        min_num = hole[i:].index(j)
                        value = j
                stack.remove(value)
                stack.append(hole[i])
                cnt += 1
            else:
                stack.append(hole[i])

print(cnt)

