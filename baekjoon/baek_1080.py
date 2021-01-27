import sys

N, M = map(int, sys.stdin.readline().split())

m1 = [list(map(int, list(sys.stdin.readline().strip()))) for x in range(N)]
m2 = [list(map(int, list(sys.stdin.readline().strip()))) for x in range(N)]

def check(number):
    if number == 1:
        return True
    else:
        return False


count = 0
for i in range(N - 2):
    for j in range(M - 2):
        if m1[i][j] != m2[i][j]:
            count += 1
            for k in range(3):
                if check(m1[i][j + k]):
                    m1[i][j + k] = 0
                else:
                    m1[i][j + k] = 1

                if check(m1[i + 1][j + k]):
                    m1[i + 1][j + k] = 0
                else:
                    m1[i + 1][j + k] = 1

                if check(m1[i + 2][j + k]):
                    m1[i + 2][j + k] = 0
                else:
                    m1[i + 2][j + k] = 1


if m1 == m2:
    print(count)
else:
    print(-1)
