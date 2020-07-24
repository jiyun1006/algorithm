import sys

io = sys.stdin.readline

n, m = map(int, io().split())

mile_list = []
value = 0
cnt = 0

for _ in range(n):
    p, L = map(int, io().split())
    if p < L:
        cnt += 1
        m -= 1
        io().split()
    else:
        value = p - L
        mile = sorted((list(map(int, io().split()))), key=lambda x: -x)
        for _ in range(value):
            mile.pop()
        mile_list.append(mile)

if m < 0:
    print(cnt + m)
else:
    mile_list.sort(key=lambda x: x[:][-1])

    for k in mile_list:
        if m - k[-1] < 0:
            break
        m -= k[-1]
        cnt += 1
        if m == 0:
            break
    print(cnt)
