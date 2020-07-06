import sys

N, M = map(int, sys.stdin.readline().split())
cnt = 0

if N == 1:
    cnt = 1
    print(cnt)
elif N == 2:
    if M <= 2:
        cnt = 1
        print(cnt)
    else:
        cnt = min(4, (M+1) // 2)
        print(cnt)
else:
    if M <= 6:
        cnt = min(4, M)
        print(cnt)
    else:
        cnt = M - 2
        print(cnt)