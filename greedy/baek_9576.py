import sys

t_n = int(sys.stdin.readline())
for _ in range(t_n):
    N, M = map(int, sys.stdin.readline().split())
    num = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
    num.sort(key=lambda x: x[:][1])
    N_list = []
    for i in range(1, N + 1):
        N_list.append(i)

    cnt = 0
    for i in range(M):
        for j in range(num[i][0], num[i][1] + 1):
            if j in N_list:
                N_list.remove(j)
                cnt += 1
                break
    print(cnt)
