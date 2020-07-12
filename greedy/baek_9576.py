import sys

t_n = int(sys.stdin.readline())
for _ in range(t_n):
    N, M = map(int, sys.stdin.readline().split())
    num = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
    num.sort(key=lambda x: x[:][1])
    N_list = [0] * (N + 1)

    for i in range(M):
        for j in range(num[i][0], num[i][1] + 1):
            if N_list[j] == 0:
                N_list[j] = 1
                break
    print(sum(N_list))