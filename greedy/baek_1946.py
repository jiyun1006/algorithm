import sys

count_list = []
for k in range(int(sys.stdin.readline())):
    score = []
    N = int(sys.stdin.readline())
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        score.append((a, b))
    score.sort()
    count = N
    view_min = N

    for i in range(N - 1):
        if view_min > int(score[i][1]):
            view_min = int(score[i][1])
        if view_min < int(score[i + 1][1]):
            count -= 1
    count_list.append(count)

for i in range(len(count_list)):
    print(count_list[i])
