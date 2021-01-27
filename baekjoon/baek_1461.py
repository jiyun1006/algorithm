import sys

io = sys.stdin.readline

N, M = map(int, io().split())

loc = list(map(int, io().split()))

loc.sort(key=lambda x: -x)

temp1 = list()
temp2 = list()
i, j = 0, 0
ans = list()


def sign(a):
    global i, j
    if a > 0:
        temp1.append(abs(a))
        i += 1

    else:
        temp2.append(abs(a))
        j += 1


for k in loc:
    sign(k)

temp1.sort()
temp2.sort()

# 양수 음수 나눠서 보관했다
if len(temp1) >= M or len(temp2) >= M:
    while len(temp1) >= M and len(temp2) >= M:
        if temp1[-1] > temp2[-1]:
            ans.append(temp1[-1])
            for _ in range(M):
                temp1.pop()
        else:
            ans.append(temp2[-1])
            for _ in range(M):
                temp2.pop()

    while len(temp1) >= M:
        ans.append(temp1[-1])
        for _ in range(M):
            temp1.pop()

    while len(temp2) >= M:
        ans.append(temp2[-1])
        for _ in range(M):
            temp2.pop()


elif len(temp1) < M and len(temp2) < M:
    if temp1[-1] > temp2[-1]:
        ans.append(temp1[-1])
        for _ in range(len(temp1)):
            temp1.pop()
    else:
        ans.append(temp2[-1])
        for _ in range(len(temp2)):
            temp2.pop()

if temp1 and temp2:
    print(sum(ans * 2) - ans[0] + temp1[-1] * 2 + temp2[-1] * 2)
elif temp1 and not temp2:
    print(sum(ans * 2) - ans[0] + temp1[-1] * 2)
elif temp2 and not temp1:
    print(sum(ans * 2) - ans[0] + temp2[-1] * 2)
elif not temp1 and not temp2:
    print(sum(ans * 2) - ans[0])
