import sys

io = sys.stdin.readline

N = int(io())
cnt = 0

for i in range(N):

    temp = list()
    S = io().rstrip()
    for j in S:
        if not temp:
            temp.append(j)
        else:
            if temp[-1] == j:
                temp.append(j)
            else:
                if j in temp:
                    break
                else:
                    temp.append(j)
    if len(S) == len(temp):
        cnt += 1


print(cnt)


